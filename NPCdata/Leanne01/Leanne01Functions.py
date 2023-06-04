import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QTextCursor
import json
import os


from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import random
import pathlib
import Globals
import time
import threading
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from time import sleep
# from battleMenuUI import SRObject
Log = Globals.Layouts["MainF"].Log

def Initialize(self, Reference):
    ID = "01"
    List = ["Leanne Confession", "Train with Leanne", "General Shop", "Find Rogue Merchant"]
    for EventID in List:
        Globals.EventCommands[EventID] = {"ID":EventID, "Reference":Reference, "OtherData":{}}

# def Initializee(self, Reference, ID):
#     Globals.SoLNPCFunctions[ID] = Reference
#     List = ["Leanne Confession", "Train with Leanne", "General Shop", "Find Rogue Merchant"]
#     for EventID in List:
#         Globals.EventCommands[EventID] = {"ID":EventID, "Reference":Reference, "OtherData":{}}

class NPCObject:
    def __init__(self, ID):
        try:
            # self.Data = Globals.InteractNPCData[ID]

            with open(f'''NPCdata.json''', 'rb') as f:
                self.Data = json.load(f)
            self.ID = ID
            self.Data = self.Data["01"]
            self.Name = self.Data["Name"]
        except:
            with open(f'''NPCdata/{self.Name}{ID}/{self.Name}{ID}Data.json''', 'rb') as f:
                self.Data = json.load(f)

        # self.Name = self.Data["Name"]
        # self.IDNumber = 0
        # self.ID = ID
        # self.Descriptions = {
        # "FullName":"Leanne Von",
        # "UpperBody":"Flat"
        # }
        # self.Traits = {}
        # self.Abilities = {}
        # self.Energy = 1000
        # self.ImageType = self.Data["OtherData"]["ImageType"]
        # self.Targeted = False

    def GetWidget(self):
        NPCWidget = QWidget()
        NPCWidget.setMinimumWidth(350)
        NPCWidget.setMinimumHeight(200)
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

        try:
            Files = os.listdir(f'''NPCdata/{self.Name}{self.ID}''')
            # if self.ImageType == "Portrait":
            ImageType = "Portrait"
            list = [File for File in Files if File.endswith((".png")) or File.endswith((".jpg")) or File.endswith((".jpeg"))]
            ListPortraits, ListFullBody = [], []
            ListPortraits = [File for File in list if File.startswith("Portrait")]
            ListFullBody = [File for File in list if File.startswith("FullBody")]
            if ImageType == "Portrait" or ListFullBody == []:
                ImageName = random.choice(ListPortraits)
            if ImageType == "FullBody" or ListPortraits == []:
                ImageName = random.choice(ListFullBody)

            LabelImage = QLabel(NPCWidget)
            LabelImage.setGeometry(5,5,130,130)
            LabelImage.setPixmap(QPixmap(f'''NPCdata/{self.Name}{self.ID}/{ImageName}'''))
            LabelImage.setScaledContents(True)
        except Exception as e:
            LabelImage = QLabel(NPCWidget)
            LabelImage.setGeometry(5,5,130,130)
            LabelImage.setStyleSheet('''
            QLabel{
            background : rgb(23, 23, 23)
            }
            ''')

        LabelName = QLabel(NPCWidget)
        LabelName.setGeometry(140,5,205,40)
        LabelName.setText(self.Data["Name"])
        LabelName.setFont(QFont('Segoe UI', 14))
        LabelName.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        ButtonDetails = QPushButton("Details", NPCWidget)
        ButtonDetails.setGeometry(270,50,75,40)
        ButtonDetails.setFont(QFont('Segoe UI', 12))

        ButtonSwitch = QPushButton("Switch", NPCWidget)
        ButtonSwitch.setGeometry(270,95,75,40)
        ButtonSwitch.setFont(QFont('Segoe UI', 12))

        LabelAction = QLabel(NPCWidget)
        LabelAction.setGeometry(5,140,340,55)
        LabelAction.setText(f'''{self.Data["Name"]} angrily scolds Player''')
        LabelAction.setFont(QFont('Segoe UI', 12))
        LabelAction.setAlignment(Qt.AlignTop | Qt.AlignLeft)

        # FOR EASE OF CONTAINING THE REPEATED LABLES
        if True:
            LabelArousal1 = QLabel(NPCWidget)
            LabelArousal1.setGeometry(140,50,25,25)
            LabelArousal1.setScaledContents(True)
            LabelArousal1.setStyleSheet('''QLabel{background: none;}''')

            LabelArousal2 = QLabel(NPCWidget)
            LabelArousal2.setGeometry(165,50,25,25)
            LabelArousal2.setScaledContents(True)
            LabelArousal2.setStyleSheet('''QLabel{background: none;}''')

            LabelArousal3 = QLabel(NPCWidget)
            LabelArousal3.setGeometry(190,50,25,25)
            LabelArousal3.setScaledContents(True)
            LabelArousal3.setStyleSheet('''QLabel{background: none;}''')

            LabelArousal4 = QLabel(NPCWidget)
            LabelArousal4.setGeometry(215,50,25,25)
            LabelArousal4.setScaledContents(True)
            LabelArousal4.setStyleSheet('''QLabel{background: none;}''')

            LabelArousal5 = QLabel(NPCWidget)
            LabelArousal5.setGeometry(240,50,25,25)
            LabelArousal5.setScaledContents(True)
            LabelArousal5.setStyleSheet('''QLabel{background: none;}''')

            self.Data["State"]["Arousal"] = 67
            if self.Data["State"]["Arousal"] >= 20:
                LabelArousal1.setPixmap(QPixmap(f'''images/SoLResources/FilledHeart'''))
            else:
                LabelArousal1.setPixmap(QPixmap(f'''images/SoLResources/EmptyHeart'''))

            if self.Data["State"]["Arousal"] >= 40:
                LabelArousal2.setPixmap(QPixmap(f'''images/SoLResources/FilledHeart'''))
            else:
                LabelArousal2.setPixmap(QPixmap(f'''images/SoLResources/EmptyHeart'''))

            if self.Data["State"]["Arousal"] >= 60:
                LabelArousal3.setPixmap(QPixmap(f'''images/SoLResources/FilledHeart'''))
            else:
                LabelArousal3.setPixmap(QPixmap(f'''images/SoLResources/EmptyHeart'''))

            if self.Data["State"]["Arousal"] >= 80:
                LabelArousal4.setPixmap(QPixmap(f'''images/SoLResources/FilledHeart'''))
            else:
                LabelArousal4.setPixmap(QPixmap(f'''images/SoLResources/EmptyHeart'''))

            if self.Data["State"]["Arousal"] >= 100:
                LabelArousal5.setPixmap(QPixmap(f'''images/SoLResources/FilledHeart'''))
            else:
                LabelArousal5.setPixmap(QPixmap(f'''images/SoLResources/EmptyHeart'''))

        if True:
            LabelEnergy1 = QLabel(NPCWidget)
            LabelEnergy1.setGeometry(140,80,25,25)
            LabelEnergy1.setScaledContents(True)
            LabelEnergy1.setStyleSheet('''QLabel{background: none;}''')

            LabelEnergy2 = QLabel(NPCWidget)
            LabelEnergy2.setGeometry(165,80,25,25)
            LabelEnergy2.setScaledContents(True)
            LabelEnergy2.setStyleSheet('''QLabel{background: none;}''')

            LabelEnergy3 = QLabel(NPCWidget)
            LabelEnergy3.setGeometry(190,80,25,25)
            LabelEnergy3.setScaledContents(True)
            LabelEnergy3.setStyleSheet('''QLabel{background: none;}''')

            LabelEnergy4 = QLabel(NPCWidget)
            LabelEnergy4.setGeometry(215,80,25,25)
            LabelEnergy4.setScaledContents(True)
            LabelEnergy4.setStyleSheet('''QLabel{background: none;}''')

            LabelEnergy5 = QLabel(NPCWidget)
            LabelEnergy5.setGeometry(240,80,25,25)
            LabelEnergy5.setScaledContents(True)
            LabelEnergy5.setStyleSheet('''QLabel{background: none;}''')

            if self.Data["State"]["Energy"] >= self.Data["GeneralAbilities"]["MaxEnergy"] / 5:
                LabelEnergy1.setPixmap(QPixmap(f'''images/SoLResources/FilledEnergy'''))
            else:
                LabelEnergy1.setPixmap(QPixmap(f'''images/SoLResources/EmptyEnergy'''))

            if self.Data["State"]["Energy"] >= (self.Data["GeneralAbilities"]["MaxEnergy"] / 5) * 2:
                LabelEnergy2.setPixmap(QPixmap(f'''images/SoLResources/FilledEnergy'''))
            else:
                LabelEnergy2.setPixmap(QPixmap(f'''images/SoLResources/EmptyEnergy'''))

            if self.Data["State"]["Energy"] >= (self.Data["GeneralAbilities"]["MaxEnergy"] / 5) * 3:
                LabelEnergy3.setPixmap(QPixmap(f'''images/SoLResources/FilledEnergy'''))
            else:
                LabelEnergy3.setPixmap(QPixmap(f'''images/SoLResources/EmptyEnergy'''))

            if self.Data["State"]["Energy"] >= (self.Data["GeneralAbilities"]["MaxEnergy"] / 5) * 4:
                LabelEnergy4.setPixmap(QPixmap(f'''images/SoLResources/FilledEnergy'''))
            else:
                LabelEnergy4.setPixmap(QPixmap(f'''images/SoLResources/EmptyEnergy'''))

            if self.Data["State"]["Energy"] >= (self.Data["GeneralAbilities"]["MaxEnergy"] / 5) * 5:
                LabelEnergy5.setPixmap(QPixmap(f'''images/SoLResources/FilledEnergy'''))
            else:
                LabelEnergy5.setPixmap(QPixmap(f'''images/SoLResources/EmptyEnergy'''))

        if True:
            LabelMood1 = QLabel(NPCWidget)
            LabelMood1.setGeometry(140,110,25,25)
            LabelMood1.setScaledContents(True)
            LabelMood1.setStyleSheet('''QLabel{background: none;}''')

            LabelMood2 = QLabel(NPCWidget)
            LabelMood2.setGeometry(165,110,25,25)
            LabelMood2.setScaledContents(True)
            LabelMood2.setStyleSheet('''QLabel{background: none;}''')

            LabelMood3 = QLabel(NPCWidget)
            LabelMood3.setGeometry(190,110,25,25)
            LabelMood3.setScaledContents(True)
            LabelMood3.setStyleSheet('''QLabel{background: none;}''')

            LabelMood4 = QLabel(NPCWidget)
            LabelMood4.setGeometry(215,110,25,25)
            LabelMood4.setScaledContents(True)
            LabelMood4.setStyleSheet('''QLabel{background: none;}''')

            LabelMood5 = QLabel(NPCWidget)
            LabelMood5.setGeometry(240,110,25,25)
            LabelMood5.setScaledContents(True)
            LabelMood5.setStyleSheet('''QLabel{background: none;}''')

            if self.Data["State"]["Mood"] >= 0:
                if self.Data["State"]["Mood"] >= 20:
                    LabelMood1.setPixmap(QPixmap(f'''images/SoLResources/BlueDiamond'''))
                else:
                    LabelMood1.setPixmap(QPixmap(f'''images/SoLResources/EmptyDiamond'''))

                if self.Data["State"]["Mood"] >= 40:
                    LabelMood2.setPixmap(QPixmap(f'''images/SoLResources/BlueDiamond'''))
                else:
                    LabelMood2.setPixmap(QPixmap(f'''images/SoLResources/EmptyDiamond'''))

                if self.Data["State"]["Mood"] >= 60:
                    LabelMood3.setPixmap(QPixmap(f'''images/SoLResources/BlueDiamond'''))
                else:
                    LabelMood3.setPixmap(QPixmap(f'''images/SoLResources/EmptyDiamond'''))

                if self.Data["State"]["Mood"] >= 80:
                    LabelMood4.setPixmap(QPixmap(f'''images/SoLResources/BlueDiamond'''))
                else:
                    LabelMood4.setPixmap(QPixmap(f'''images/SoLResources/EmptyDiamond'''))

                if self.Data["State"]["Mood"] >= 100:
                    LabelMood5.setPixmap(QPixmap(f'''images/SoLResources/BlueDiamond'''))
                else:
                    LabelMood5.setPixmap(QPixmap(f'''images/SoLResources/EmptyDiamond'''))
            elif self.Data["State"]["Mood"] <= 0:
                if self.Data["State"]["Mood"] <= 20:
                    LabelMood1.setPixmap(QPixmap(f'''images/SoLResources/RedDiamond'''))
                else:
                    LabelMood1.setPixmap(QPixmap(f'''images/SoLResources/EmptyDiamond'''))

                if self.Data["State"]["Mood"] <= 40:
                    LabelMood2.setPixmap(QPixmap(f'''images/SoLResources/RedDiamond'''))
                else:
                    LabelMood2.setPixmap(QPixmap(f'''images/SoLResources/EmptyDiamond'''))

                if self.Data["State"]["Mood"] <= 60:
                    LabelMood3.setPixmap(QPixmap(f'''images/SoLResources/RedDiamond'''))
                else:
                    LabelMood3.setPixmap(QPixmap(f'''images/SoLResources/EmptyDiamond'''))

                if self.Data["State"]["Mood"] <= 80:
                    LabelMood4.setPixmap(QPixmap(f'''images/SoLResources/RedDiamond'''))
                else:
                    LabelMood4.setPixmap(QPixmap(f'''images/SoLResources/EmptyDiamond'''))

                if self.Data["State"]["Mood"] <= 100:
                    LabelMood5.setPixmap(QPixmap(f'''images/SoLResources/RedDiamond'''))
                else:
                    LabelMood5.setPixmap(QPixmap(f'''images/SoLResources/EmptyDiamond'''))


        return NPCWidget

    def LoadData(self):
        ""

    def SaveData(self):
        ""

    def TriggerAction(self):
        ""


def CheckEventCommandAvailable(self, EventID, PCID, NPCID, PCLocation):
    if True:
        return 1
    ""

def GetEventCommandButton(self, EventID, PCID, NPCID, PCLocation):
    try:
        if True:
            def BG():
                try:
                    TriggerEventCommand(self, EventID, PCID, NPCID)
                except Exception as e:
                    Log(3, "ERROR COMMAND EVENT PRESSED", e, EventID, __name__)
            Button = QPushButton(clicked = lambda: BG())
            Button.setText(EventID)
            Button.setMinimumWidth(165)
            Button.setMinimumHeight(35)
            Button.setMaximumWidth(165)
            Button.setMaximumHeight(35)
            Button.setFont(QFont('Segoe UI', 14))

            Globals.References["SoLFunctions"].CheckButtonFontSize(self, Button)
            return Button
    except Exception as e:
        Log(3, "ERROR GetCommandButton", e, EventID, __name__)

def TriggerEventCommand(self, EventID, PCID, NPCID):
    print(EventID)

# print(os.listdir())
# x = NPCObject("Leanne0")
# print(x.Data)
# print(os.listdir("NPCdata/Leanne01"))
