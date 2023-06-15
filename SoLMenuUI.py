
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QTextCursor
import Globals
# from UiStyle import *
# from SoLMenuFunctions import *
from time import sleep
import os
Log = Globals.Layouts["MainF"].Log
import pathlib

class UiLayoutSoLMenu(QWidget):
    RefreshSignal1 = pyqtSignal()
    RefreshSignal2 = pyqtSignal()
    RefreshSignal3 = pyqtSignal()

    CTS1 = pyqtSignal()
    CTS2 = pyqtSignal()
    CTS3 = pyqtSignal()

    CommandCheckSignal = pyqtSignal()

    def __init__(self):
        try:
            super().__init__()
            Globals.Layouts["SoLUI"] = self
            Globals.LayoutsData["SoLUI"] = {"Source":"SoLMenuUI", "Initialized":0}

        except Exception as e:
            Log(4, "ERROR SOL UI INITIALIZE", e)


    def UI(self):
        MainWindow = Globals.Layouts["MainF"]
        self.GUI = QWidget(MainWindow)

        # STATUS LABEL AT THE TOP
        self.labelStatus = QLabel(self.GUI)
        self.labelStatus.setGeometry(365,5,875,30)
        self.labelStatus.setWordWrap(True)
        self.labelStatus.setFont(QFont('Segoe UI', 11))
        self.labelStatus.setText("10:40        18 June 2050        Temple       Get some slime        Defeat the bees.")
        self.labelStatus.setAlignment(Qt.AlignCenter)
        self.labelStatus.setProperty("Color","Dark")

        # MAIN LABEL AT THE CENTRE
        self.labelMain = QLabel(self.GUI)
        self.labelMain.setWordWrap(True)
        self.labelMain.setFont(QFont('Segoe UI', 13))
        self.labelMain.setAlignment(Qt.AlignLeft)
        self.labelMain.setIndent(9)
        self.labelMain.setProperty("Color","Dark")

        self.scrollMain = QScrollArea(self.GUI)
        self.scrollMain.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollMain.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollMain.setGeometry(365,40,875,580)
        self.scrollMain.setWidgetResizable(True)
        self.scrollMain.setWidget(self.labelMain)


        self.BackNPCLabel = QLabel(self.GUI)
        self.BackNPCLabel.setGeometry(1245,5,355,1015)
        self.BackNPCLabel.setProperty("Color","Dark")

        self.FormNPC = QVBoxLayout()
        self.ScrollNPC = QScrollArea(self.GUI)
        self.ScrollNPC.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollNPC.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollNPC.setGeometry(1245,5,355,1015)

        self.GroupBoxNPC = QGroupBox()
        self.GroupBoxNPC.setLayout(self.FormNPC)
        self.GroupBoxNPC.setMinimumWidth(350)
        self.ScrollNPC.setWidget(self.GroupBoxNPC)
        self.FormNPC.setContentsMargins(0, 0, 0, 5)
        self.FormNPC.WigetsDict = {}

        self.ScrollPC = QScrollArea(self.GUI)
        self.ScrollPC.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollPC.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollPC.setGeometry(5,5,355,1015)
        self.ScrollPC.setProperty("Color","Dark")

        self.FormPC = QVBoxLayout()
        self.GroupBoxPC = QGroupBox()
        self.GroupBoxPC.setLayout(self.FormPC)
        self.ScrollPC.setWidget(self.GroupBoxPC)
        self.ScrollPC.setMinimumWidth(355)
        self.ScrollPC.setMaximumWidth(355)
        self.ScrollPC.setMinimumHeight(1015)
        self.ScrollPC.setMaximumHeight(1015)
        self.GroupBoxPC.setMinimumWidth(355)
        self.GroupBoxPC.setMaximumWidth(355)
        self.FormPC.setContentsMargins(3, 5, 3, 5)
        self.FormPC.WidgetsList = []

        self.labelButtons = QLabel(self.GUI)
        self.labelButtons.setGeometry(365,625,875,395)
        self.labelButtons.setProperty("Color","Dark")


        self.ScrollSoLButtons = QScrollArea(self.GUI)
        self.ScrollSoLButtons.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollSoLButtons.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollSoLButtons.setGeometry(370,630,870,245)

        self.FormSoLButtons = QGridLayout()
        self.FormSoLButtons.setContentsMargins(0, 0, 0, 0)
        self.GroupBoxSoLButtons = QGroupBox()
        self.GroupBoxSoLButtons.setLayout(self.FormSoLButtons)
        self.ScrollSoLButtons.setWidget(self.GroupBoxSoLButtons)
        self.GroupBoxSoLButtons.setMinimumWidth(870)
        self.FormSoLButtons.WidgetsList = []

        self.ScrollSoLEventButtons = QScrollArea(self.GUI)
        self.ScrollSoLEventButtons.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollSoLEventButtons.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollSoLEventButtons.setGeometry(370,885,870,80)

        self.FormSOLEventButtons = QGridLayout()
        self.FormSOLEventButtons.setContentsMargins(0, 0, 0, 0)
        self.GroupBoxSolEventButtons = QGroupBox()
        self.GroupBoxSolEventButtons.setLayout(self.FormSOLEventButtons)
        self.ScrollSoLEventButtons.setWidget(self.GroupBoxSolEventButtons)
        self.GroupBoxSolEventButtons.setMinimumWidth(870)
        self.FormSOLEventButtons.WidgetsList = []

        self.ScrollControlCommands = QScrollArea(self.GUI)
        self.ScrollControlCommands.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollControlCommands.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollControlCommands.setGeometry(370,970,870,50)

        self.FormControlCommands = QGridLayout()
        self.FormControlCommands.setContentsMargins(0, 0, 0, 0)
        self.GroupBoxControlCommands = QGroupBox()
        self.GroupBoxControlCommands.setLayout(self.FormControlCommands)
        self.ScrollControlCommands.setWidget(self.GroupBoxControlCommands)
        self.GroupBoxControlCommands.setMinimumWidth(870)
        self.FormControlCommands.WidgetsList = []


        self.Refresh()

    def Refresh(self):
        Globals.References["SoLFunctions"].Refresh(self)


class UiLayoutBattleWindow(QWidget):
    def Ui(self, MainWindow):

        self.GUI = QWidget(MainWindow)
        self.backButton = QPushButton("Back", self.GUI)
        MainWindow.setCentralWidget(self.GUI)

def Initialize(self, Reference):
    if "SoLUI" not in Globals.Layouts:
        Object = UiLayoutSoLMenu()
