import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QTextCursor
import Globals
import os
import webbrowser
Log = Globals.Layouts["MainF"].Log

class UiLayoutMainMenu(QWidget):
    def __init__(self):
        super().__init__()
        Globals.Layouts["MainMenuUI"] = self
        Globals.LayoutsData["MainMenuUI"] = {"Source":"MainMenuUI", "Initialized":0}

    def UI(self):
        MainWindow = Globals.Layouts["MainF"]
        self.GUI = QWidget(MainWindow)

        self.labelTitle = QLabel(self.GUI, objectName = "MainTitle")
        self.labelTitle.setFont(QFont('Segoe UI', 36))
        self.labelTitle.setGeometry(360,110,700,260)
        self.labelTitle.setText("Another Chance")
        self.labelTitle.setAlignment(Qt.AlignCenter)
        self.labelTitle.setProperty("Color","Dark")

        self.labelCommandsHolder = QLabel(self.GUI)
        self.labelCommandsHolder.setGeometry(325,470,770,130)
        self.labelCommandsHolder.setProperty("Color","Dark")


        self.buttonContinue = QPushButton('Continue', self.GUI, clicked = lambda: MainWindow.gotoLayout("SoLUI"))
        self.buttonContinue.setGeometry(335, 480, 180, 30)
        self.buttonContinue.setProperty("Color","Light")


        self.buttonData = QPushButton('Save/Load', self.GUI, clicked = lambda: MainWindow.gotoLayout("SaveUI"))
        self.buttonData.setGeometry(525, 480, 180, 30)
        self.buttonData.setProperty("Color","Light")

        self.buttonImport = QPushButton('Manage Characters', self.GUI, clicked = lambda: MainWindow.gotoLayout("ImportUI"))
        self.buttonImport.setGeometry(715, 480, 180, 30)
        self.buttonImport.setProperty("Color","Light")

        self.buttonMaker = QPushButton('Character Maker', self.GUI, clicked = lambda: MainWindow.gotoLayout("MakerUI"))
        self.buttonMaker.setGeometry(905, 480, 180, 30)
        self.buttonMaker.setProperty("Color","Light")


        self.buttonOptions = QPushButton('Options', self.GUI)
        self.buttonOptions.setGeometry(335, 520, 180, 30)
        self.buttonOptions.setProperty("Color","Light")

        self.buttonDiscord = QPushButton('Discord', self.GUI, clicked = lambda: webbrowser.open("https://discord.gg/rjBW7Uj48g"))
        self.buttonDiscord.setGeometry(525, 520, 180, 30)
        self.buttonDiscord.setStyleSheet('''color:rgb(88, 101, 242);''')
        self.labelDiscord = QLabel(self.GUI)
        self.labelDiscord.setStyleSheet('''background:none;border:none;''')
        self.labelDiscord.setPixmap(QPixmap("images/OtherResources/discord-mark-blue.png"))
        self.labelDiscord.setGeometry(529,522,30,26)
        self.labelDiscord.setScaledContents(True)

        self.buttonPatreon = QPushButton('Patreon', self.GUI)
        self.buttonPatreon.setGeometry(715, 520, 180, 30)
        self.buttonPatreon.setStyleSheet('''color:rgb(249, 104, 84);''')
        self.labelPatreon = QLabel(self.GUI)
        self.labelPatreon.setStyleSheet('''background:none;border:none;''')
        self.labelPatreon.setPixmap(QPixmap("images/OtherResources/Digital-Patreon-Logo_FieryCoral.png"))
        self.labelPatreon.setGeometry(719,522,26,26)
        self.labelPatreon.setScaledContents(True)

        self.buttonHelp = QPushButton('Help', self.GUI)
        self.buttonHelp.setGeometry(905, 520, 180, 30)
        self.buttonHelp.setProperty("Color","Light")


        self.buttonChangelog = QPushButton('V. M1', self.GUI, clicked = lambda: webbrowser.open("https://github.com/AntCDev/Another-Chance"))
        self.buttonChangelog.setGeometry(335, 560, 180, 30)
        self.buttonChangelog.setProperty("Color","Light")

        # self.buttonCredits = QPushButton('Credits (Bat)', self.GUI, clicked = lambda: MainWindow.gotoLayout("BattleScene"))
        self.buttonCredits = QPushButton('Credits', self.GUI, clicked = lambda: MainWindow.gotoLayout("CreditsUI"))
        self.buttonCredits.setGeometry(525, 560, 180, 30)
        self.buttonCredits.setProperty("Color","Light")

        self.buttonDisclaimer = QPushButton('Disclaimer', self.GUI, clicked = lambda: MainWindow.gotoLayout("DisclaimerUI"))
        self.buttonDisclaimer.setGeometry(715, 560, 180, 30)
        self.buttonDisclaimer.setProperty("Color","Light")

        def NG(MainWindow):
            try:
                Globals.CurrentSession = {}
                Globals.References["BasicMod"].SetBaseData()
                Globals.SoLNPCData["0"] = {"Name": "Aria", "ID": "0", "Personality": "Standard0", "State": {"Energy": 2000, "Mood": 0, "Arousal": 0, "Alcohol": 0, "Drugs": 0, "PConscious": 1, "MConscious": 1}, "Relations": {}, "BodyData": {"FullName": "Aria", "SkinColor": "Pale", "HairColor": "Dark", "PhysicalAge": 2, "Race": "Human", "Face": 5, "Eyes": "Brown", "Lips": 2, "Height": 4, "Complexion": 3, "Sex": "Female", "Pronouns": {"PSub": "She", "PObj": "Her", "PPos": "Her", "PIPos": "Hers"}, "Hips": 3, "Ass": 3, "Chest": 4, "VTightness": 3, "ATightness": 3, "PenisSize": 0, "BallsSize": 0, "VVirgin": 1, "AVirgin": 1, "PVirgin": 1, "MVirgin": 1}, "OtherData": {"Home": None}, "Traits": {"Courage0": 0, "Attitude0": 0, "Pride0": 0, "Dere0": 0, "SelfControl0": 0, "Cheerfulness0": 0, "Shyness0": 0, "Gullible0": 0, "Charm0": 0, "SubstanceResistance0": 0, "SexualInterest0": 0, "Virtue0": 0, "Chastity0": 0, "Openess0": 0, "PainResistance0": 0, "ArousalEase0": 0, "ResponseToPleasure0": 0, "Perversion0": 0, "Dominance0": 0, "Forceful0": 0, "Loyalty0": 0, "Violence0": 0, "Beauty0": 0, "Shame0": 0, "Will0": 0, "Influence0": 0, "Fertility0": 0, "LewdBody0": {"V": False, "A": False, "B": False, "P": False, "M": False}}, "GeneralFlags": {}, "GeneralAbilities": {"MaxEnergy": 2000}, "CombatAbilities": {"DeckName": None}, "Descriptions": {"Backstory": "", "Core": "", "Head": "", "Arms": "", "Legs": "", "Genitals": ""}, "Actions": {"Intention": None, "Action": None, "PreviousTask": {"HourStart": 0, "HourFinish": 1, "Task": ["Idling", {"BriefFluff": "Idling in the streets of ", "LongFluff": ""}], "InterruptionPenalty": 0, "Location": "ResidentialArea"}, "CurrentTask": {"HourStart": 0, "HourFinish": 1, "Task": ["Idling", {"BriefFluff": "Idling in the streets of ", "LongFluff": ""}], "InterruptionPenalty": 0, "Location": "ResidentialArea"}, "FutureTask": {"HourStart": 0, "HourFinish": 1, "Task": ["Idling", {"BriefFluff": "Idling in the streets of ", "LongFluff": ""}], "InterruptionPenalty": 0, "Location": "ResidentialArea"}, "TaskData": {}, "HasFollowing": [], "InteractionParty": [], "SexualPary": [], "IsFollowing": None, "isInSexScene": [], "Targeting": None}, "Items": {}, "isInSexScene": 0, "Version": 2}
                Globals.SoLPCData["ID"] = "0"
                MainWindow.gotoLayout("SoLUI")

            except Exception as e:
                print(e)
                ""

        self.buttonReset = QPushButton('New Game', self.GUI, clicked = lambda: MainWindow.gotoLayout("NewGameUI"))
        self.buttonReset.setGeometry(905, 560, 180, 30)
        self.buttonReset.setProperty("Color","Light")

    def Refresh(self):
        if Globals.SoLNPCData == {}:
            self.buttonContinue.setProperty("Enabled","0")
            self.buttonContinue.setEnabled(False)
            self.buttonImport.setProperty("Enabled","0")
            self.buttonImport.setEnabled(False)
        else:
            self.buttonContinue.setEnabled(True)
            self.buttonContinue.setProperty("Enabled","1")
            self.buttonContinue.style().polish(self.buttonContinue)
            self.buttonImport.setEnabled(True)
            self.buttonImport.setProperty("Enabled","1")
            self.buttonImport.style().polish(self.buttonImport)




def Initialize(self, Reference):
    if "MainMenu" not in Globals.Layouts:
        Object = UiLayoutMainMenu()
