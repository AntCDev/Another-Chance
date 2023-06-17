import os
import pathlib
import random

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import Globals

Log = Globals.Layouts["MainF"].Log
class EnhanceGenericNPCObject:
    def __init__(self, NPCData):
        self.Data = NPCData

    def GetWidget(self):
        NPCWidget = QWidget(objectName = "Transparent")
        NPCWidget.setGeometry(300,300,500,500)
        NPCWidget.setMaximumWidth(200)
        NPCWidget.setMinimumWidth(200)
        NPCWidget.setMaximumHeight(240)
        NPCWidget.setMinimumHeight(240)

        NPCName = QLabel(NPCWidget, objectName = "SubTitle")
        NPCName.setText(self.Data["Name"])
        NPCName.setGeometry(0,0,200,35)
        NPCName.setProperty("Color","Light")
        NPCName.setAlignment(Qt.AlignCenter)

        NPCImage = QLabel(NPCWidget)
        NPCImage.setGeometry(0,40,200,200)
        NPCImage.setProperty("Color","Dark")

        try:
            ListPortraits, ListFullBody = Globals.References["SoLFunctions"].GetImages(self.Data)
            ImageType = "Portrait"
            if ImageType == "Portrait" or ListFullBody == []:
                ImageName = random.choice(ListPortraits)
            if ImageType == "FullBody" or ListPortraits == []:
                ImageName = random.choice(ListFullBody)

            NPCImage.setPixmap(QPixmap(  os.path.abspath( pathlib.Path() / "NPCData" / f'''{self.Data["Name"]}{self.Data["ID"]}''' / ImageName )   ))
            NPCImage.setScaledContents(True)
        except Exception as e:
            print(e)
            ""
        def CC():
            Globals.LayoutsData["EnhanceUI"]["TargetID"] = self.Data["ID"]
            Globals.LayoutsData["EnhanceUI"]["ActorID"] = Globals.SoLPCData["ID"]
            Globals.Layouts["MainF"].gotoLayout("EnhanceUI")

        NPCImage.mouseReleaseEvent = lambda event: CC()


        return NPCWidget




class UiLayoutSleepMenu:
    def __init__(self):
        Globals.Layouts["SleepUI"] = self
        Globals.LayoutsData["SleepUI"] = {"Source":"sleepMenuUI"}

    def UI(self):
        MainWindow = Globals.Layouts["MainF"]
        self.GUI = QWidget(MainWindow)

        # self.labelBack = QLabel(self.GUI)
        # self.labelBack.setGeometry(5,5,1590,1014)
        # self.labelBack.setProperty("Color","Dark")

        self.EnhanceLabelBack = QLabel(self.GUI)
        self.EnhanceLabelBack.setGeometry(5,5,420,1014)
        self.EnhanceLabelBack.setProperty("Color","Dark")

        self.EnhanceLabel = QLabel("Enhance Relations", self.GUI, objectName = "Title")
        self.EnhanceLabel.setGeometry(10,10,410,35)
        self.EnhanceLabel.setProperty("Color","Light")
        self.EnhanceLabel.setAlignment(Qt.AlignCenter)

        self.EnhanceScroll = QScrollArea(self.GUI)
        self.EnhanceScroll.setGeometry(10,50,410,964)
        self.EnhanceScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.EnhanceScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.EnhanceForm = QGridLayout()
        self.EnhanceBox = QGroupBox()
        self.EnhanceScroll.setWidget(self.EnhanceBox)
        self.EnhanceForm.setContentsMargins(0, 0, 0, 0)
        self.EnhanceBox.setLayout(self.EnhanceForm)
        self.EnhanceForm.WidgetsDict = {}


        self.BottomLabel = QLabel(self.GUI)
        self.BottomLabel.setGeometry(430,964,1165,55)
        self.BottomLabel.setProperty("Color", "Dark")

        self.buttonContinue = QPushButton('Wake Up', self.GUI, clicked = lambda: MainWindow.gotoLayout("SoLUI"))
        self.buttonContinue.setGeometry(435,969,200,45)

    def Refresh(self):
        for Key in self.EnhanceForm.WidgetsDict:
            self.EnhanceForm.removeWidget(self.EnhanceForm.WidgetsDict[Key])

        # Globals.References["SoLFunctions"].ResetGenericNPC()
        PCID = Globals.SoLPCData["ID"]
        for OtherID in Globals.SoLNPCData[PCID]["Relations"]:
            OtherData = Globals.SoLNPCData[OtherID]
            Object = EnhanceGenericNPCObject(OtherData)
            self.EnhanceForm.WidgetsDict[OtherID] = Object.GetWidget()

        MaxWidth = 410
        Width, Height = Globals.References["SoLFunctions"].GridLayoutMaker(self, self.EnhanceForm, self.EnhanceForm.WidgetsDict, MaxWidth, 10)

        self.EnhanceBox.setMaximumHeight(Height)
        self.EnhanceBox.setMinimumHeight(Height)
        self.EnhanceBox.setMaximumWidth(Width)
        self.EnhanceBox.setMinimumWidth(Width)



def Initialize(self, Reference):
    if "SleepUI" not in Globals.Layouts:
        Object = UiLayoutSleepMenu()
