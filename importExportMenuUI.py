import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QTextCursor
import json
import os
import Globals
import random

class GenericNPCObject:
    def __init__(self, ID, Name, Status):
        self.ID = ID
        self.Name = Name
        self.Status = Status
        with open(f'''NPCdata/{self.Name}{ID}/{Name}{ID}Data.json''', 'rb') as f:
            self.Data = json.load(f)

    def GetWidget(self):
        NPCWidget = QWidget()
        NPCWidget.setMinimumWidth(365)
        NPCWidget.setMaximumWidth(365)
        NPCWidget.setMinimumHeight(130)
        NPCWidget.setMaximumHeight(130)
        NPCWidget.setStyleSheet('''
        .QWidget{
        border: 1px solid black;
        background : rgb(23, 23, 23)
        }
        QLabel{
        border: 1px solid black;
        background : rgb(35, 35, 35)
        }
        ''')

        LabelStatus = QLabel(NPCWidget)
        LabelStatus.setGeometry(0,0,20,130)


        try:
            ListPortraits, ListFullBody = Globals.References["SoLFunctions"].GetImages(self.Data)
            ImageType = "Portrait"

            if ImageType == "Portrait" or ListFullBody == []:
                ImageName = random.choice(ListPortraits)
            if ImageType == "FullBody" or ListPortraits == []:
                ImageName = random.choice(ListFullBody)

            LabelImage = QLabel(NPCWidget)
            LabelImage.setGeometry(20,0,130,130)
            LabelImage.setPixmap(QPixmap(f'''NPCdata/{self.Name}{self.ID}/{ImageName}'''))
            LabelImage.setScaledContents(True)
        except Exception as e:
            LabelImage = QLabel(NPCWidget)
            LabelImage.setGeometry(20,5,130,130)
            LabelImage.setStyleSheet('''
            QLabel{
            background : rgb(23, 23, 23)
            }
            ''')

        LabelName = QLabel(NPCWidget, objectName = "SubTitle")
        LabelName.setGeometry(155,0,205,40)
        LabelName.setText(f'''{self.Data["Name"]} {self.ID}''')
        LabelName.setFont(QFont('Segoe UI', 14))
        LabelName.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        def DetailsFunc(self):
            ""
        ButtonDetails = QPushButton("Details", NPCWidget, clicked = lambda: DetailsFunc(self))
        ButtonDetails.setGeometry(155,45,100,40)
        ButtonDetails.setFont(QFont('Segoe UI', 12))

        def ImportFunc(self):
            with open(f'''NPCdata/{self.Name}{self.ID}/{self.Name}{self.ID}Data.json''', 'rb') as f:
                NPCData = json.load(f)
            try:
                Globals.References["SoLFunctions"].ImportNPC(NPCData)
                Globals.Layouts["ImportUI"].LabelStatus.setText(f'''Succesfully Imported {self.Name} {self.ID} ''')
            except Exception as e:
                Log(2, "ERROR IMPORTING NPC", e, self.ID, self.Name)
                Globals.Layouts["ImportUI"].LabelStatus.setText(f'''Error Importing {self.Name} {self.ID} ''')

            Globals.Layouts["ImportUI"].Refresh()
        ButtonImport = QPushButton("Import", NPCWidget, clicked = lambda: ImportFunc(self))
        ButtonImport.setGeometry(260,45,100,40)
        ButtonImport.setFont(QFont('Segoe UI', 12))

        def RemoveFunc(self):
            try:
                Globals.References["SoLFunctions"].RemoveNPC(self.ID)
                Globals.Layouts["ImportUI"].LabelStatus.setText(f'''Succesfully Removed {self.Name} {self.ID} ''')
            except Exception as e:
                Globals.Layouts["ImportUI"].LabelStatus.setText(f'''Failed to Remove {self.Name} {self.ID} ''')
                Log(4, "ERROR REMOVING NPC", e, self.ID, self.Name)

            Globals.Layouts["ImportUI"].Refresh()
        ButtonRemove = QPushButton("Remove", NPCWidget, clicked = lambda: RemoveFunc(self))
        ButtonRemove.setGeometry(155,90,100,40)
        ButtonRemove.setFont(QFont('Segoe UI', 12))

        def ExportFunc(self):
            ""
        ButtonExport = QPushButton("Export", NPCWidget, clicked = lambda: ExportFunc(self))
        ButtonExport.setGeometry(260,90,100,40)
        ButtonExport.setFont(QFont('Segoe UI', 12))

        if self.Status == "Active":
            LabelStatus.setStyleSheet('''
            QLabel{
            border: 1px solid black;
            background:rgb(0,255,0);
            }
            ''')
            ButtonImport.setCheckable(True)
            ButtonImport.setChecked(True)
            ButtonImport.setEnabled(False)
        elif self.Status == "Inactive":
            LabelStatus.setStyleSheet('''
            QLabel{
            border: 1px solid black;
            background:rgb(255,0,0);
            }
            ''')
            ButtonExport.setCheckable(True)
            ButtonExport.setChecked(True)
            ButtonExport.setEnabled(False)
        elif self.Status == "Temporal":
            LabelStatus.setStyleSheet('''
            QLabel{
            border: 1px solid black;
            background:rgb(255,255,0);
            }
            ''')
            ButtonImport.setCheckable(True)
            ButtonImport.setChecked(True)
            ButtonImport.setEnabled(False)

        return NPCWidget



class UiLayoutImportMenu(object):
    def __init__(self):
        Globals.Layouts["ImportUI"] = self
        Globals.LayoutsData["ImportUI"] = {"Source":"importMenuUI", "Initialized":0}


    def UI(self):
        MainWindow = Globals.Layouts["MainF"]

        self.GUI = QWidget(MainWindow)


        self.labelBack = QLabel(self.GUI)
        self.labelBack.setGeometry(237,5,1125,950)
        self.labelBack.setProperty("Color","Dark")

        self.scrollNPC = QScrollArea(self.GUI)
        self.scrollNPC.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollNPC.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollNPC.setGeometry(237,5,1125,950)


        self.LabelControl = QLabel(self.GUI)
        self.LabelControl.setGeometry(5,964,1592,55)
        self.LabelControl.setStyleSheet('''
        QLabel{
        background-color:rgb(23,23,23);
        }
        ''')

        self.ButtonMenu = QPushButton("Back", self.GUI, clicked = lambda: MainWindow.gotoPreviousLayout())
        self.ButtonMenu.setGeometry(15,970,200,45)

        self.LabelStatus = QLabel(self.GUI)
        self.LabelStatus.setGeometry(595,970,400,45)
        self.LabelStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelStatus.setStyleSheet('''
        QLabel{
        background-color:rgb(23,23,23);
        color:white;
        font-size: 16pt;
        font-family: Segoe UI;
        }
        ''')

        self.myformNPC = QGridLayout()
        self.myformNPC.WidgetsList = []
        self.mygroupboxNPC = QGroupBox()

        self.Refresh()

    def Refresh(self):
        for Widget in self.myformNPC.WidgetsList:
            self.myformNPC.removeWidget(Widget)

        NPCFiles = {}
        NPCCurrent = {}
        NPCStatus = {}

        DirList = os.listdir("NPCdata")
        for DirName in DirList:
            try:
                with open(f'''NPCdata/{DirName}/{DirName}Data.json''', 'rb') as f:
                    NPCdata = json.load(f)
                Name = NPCdata["Name"]
                ID = NPCdata["ID"]

                NPCFiles[ID] = NPCdata

            except Exception as e:
                ""
        NPCCurrent = list(Globals.SoLNPCData.keys())

        for NPCID in NPCFiles:
            if NPCID in NPCCurrent:
                NPCStatus[NPCID] = "Active"
            else:
                NPCStatus[NPCID] = "Inactive"

        for NPCID in NPCCurrent:
            if NPCID not in NPCCurrent:
                NPCStatus[NPCID] = "Temporal"





        Layer, Row = 0,0

        for NPCID in NPCStatus:
            if NPCID == Globals.SoLPCData["ID"]:
                continue
            try:
                Name = NPCFiles[NPCID]["Name"]
            except:
                Name = Globals.SoLNPCData[NPCID]["Name"]

            Object = GenericNPCObject(NPCID, Name, NPCStatus[NPCID])
            Widget = Object.GetWidget()
            self.myformNPC.addWidget(Widget, Layer, Row)
            self.myformNPC.WidgetsList.append(Widget)
            Row += 1
            if Row >= 3:
                Layer += 1
                Row = 0

        self.mygroupboxNPC.setLayout(self.myformNPC)
        self.scrollNPC.setWidget(self.mygroupboxNPC)
        # self.scrollNPC.setMinimumWidth(1125)
        # self.scrollNPC.setMaximumWidth(1125)
        # self.scrollNPC.setMinimumHeight(950)
        # self.scrollNPC.setMaximumHeight(950)
        # self.myformNPC.setContentsMargins(10, 0, 5, 5)


def Initialize(self, Reference):
    if "ImportUI" not in Globals.Layouts:
        Object = UiLayoutImportMenu()
