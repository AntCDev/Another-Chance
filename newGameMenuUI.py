import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QTextCursor
import json
import os
import Globals

class UiLayoutNewGameMenuOld(object):
    def __init__(self):
        Globals.Layouts["NewGameUI"] = self
        Globals.LayoutsData["NewGameUI"] = {"Source":"sleepMenuUI"}


    def UI(self):
        MainWindow = Globals.Layouts["MainF"]
        self.GUI = QWidget(MainWindow)

        self.labelBack = QLabel(self.GUI)
        self.labelBack.setGeometry(288,5,1024,954)
        self.labelBack.setFont(QFont('Segoe UI', 14))
        self.labelBack.setProperty("Color","Dark")

        self.statusLabelBack = QLabel(self.GUI)
        self.statusLabelBack.setGeometry(5,964,1592,55)
        self.statusLabelBack.setProperty("Color","Dark")

        self.statusLabel = QLabel(self.GUI, objectName = "Title")
        self.statusLabel.setGeometry(505,964,600,55)
        self.statusLabel.setProperty("Color","Dark")
        self.statusLabel.setAlignment(Qt.AlignCenter)

        self.buttonBack = QPushButton("Back", self.GUI, clicked = lambda: MainWindow.gotoPreviousLayout())
        self.buttonBack.setGeometry(15,970,200,45)

        self.scroll = QScrollArea(self.GUI)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setGeometry(288,5,1024,954)

        myform = QVBoxLayout()

        #### INTRODUCTION
        self.introductionWidget = QWidget()
        self.introductionWidget.setFixedSize(1004,500)
        self.introductionWidget.setStyleSheet('''
        QWidget{
    	background-color:rgb(23, 23, 23);
        }
        ''')

        self.titleLabel = QLabel("Introduction", self.introductionWidget, objectName = "Title")
        self.titleLabel.setFont(QFont('Segoe UI', 20))
        self.titleLabel.setGeometry(10,10,984,40)
        self.titleLabel.setAlignment(Qt.AlignVCenter)
        self.titleLabel.setAlignment(Qt.AlignHCenter)
        self.titleLabel.setStyleSheet('''
        QLabel{
        border: 1px solid black;
        background : rgb(35, 35, 35);
        color:rgb(255, 255, 255)
        }
        ''')

        self.bodyLabel = QLabel(self.introductionWidget)
        self.bodyLabel.setFont(QFont('Segoe UI', 16))
        self.bodyLabel.setGeometry(10,60,984,80)
        self.bodyLabel.setAlignment(Qt.AlignTop)
        self.bodyLabel.setAlignment(Qt.AlignLeft)
        self.bodyLabel.setText("Welcome to Another Chance, a Slice of Life erotic game. The game is still in alpha state, and there might be a lot of bugs around, so if you notice any crash or weird behaivor, please let me know in the discord.")
        self.bodyLabel.setWordWrap(True)

        myform.addWidget(self.introductionWidget)



        #### CHARACTER SELECTION
        self.characterWidget = QWidget()
        self.characterWidget.setFixedSize(1004,210)
        self.characterWidget.setStyleSheet('''
        QWidget{
    	background-color:rgb(23, 23, 23);
        }
        QPushButton{
        background-color:rgb(35, 35, 35)
        }
        QLineEdit{
        color:rgb(255,255,255);
        }
        ''')

        self.characterTitle = QLabel("Character", self.characterWidget, objectName = "Title")
        self.characterTitle.setFont(QFont('Segoe UI', 16))
        self.characterTitle.setGeometry(10,10,984,40)
        self.characterTitle.setAlignment(Qt.AlignVCenter)
        self.characterTitle.setAlignment(Qt.AlignHCenter)
        self.characterTitle.setStyleSheet('''
        QLabel{
        border: 1px solid black;
        background : rgb(35, 35, 35);
        color:rgb(255, 255, 255)
        }
        ''')

        self.characterLabel = QLabel("Select your character", self.characterWidget, objectName = "SubTitle")
        self.characterLabel.setFont(QFont('Segoe UI', 14))
        self.characterLabel.setGeometry(10,60,984,40)
        self.characterLabel.setAlignment(Qt.AlignVCenter)
        self.characterLabel.setAlignment(Qt.AlignHCenter)

        self.maleCharacterButton = QPushButton("Male", self.characterWidget, clicked = lambda: self.NewGame("Male"))
        self.maleCharacterButton.setFont(QFont('Segoe UI', 12))
        self.maleCharacterButton.setGeometry(10,110,180,40)

        self.femaleCharacterButton = QPushButton("Female", self.characterWidget, clicked = lambda: self.NewGame("Female"))
        self.femaleCharacterButton.setFont(QFont('Segoe UI', 12))
        self.femaleCharacterButton.setGeometry(10,160,180,40)

        self.futanariCharacterButton = QPushButton("Futanari", self.characterWidget, clicked = lambda: self.NewGame("Futanari"))
        self.futanariCharacterButton.setFont(QFont('Segoe UI', 12))
        self.futanariCharacterButton.setGeometry(200,160,180,40)

        self.nameCharacterLine = QLineEdit(self.characterWidget)
        self.nameCharacterLine.setFont(QFont('Segoe UI', 12))
        self.nameCharacterLine.setGeometry(200,110,180,40)
        self.nameCharacterLine.setPlaceholderText("Name")

        self.customCharacterButton = QPushButton("Custom", self.characterWidget, clicked = lambda: self.NewGame("Custom"))
        self.customCharacterButton.setFont(QFont('Segoe UI', 12))
        self.customCharacterButton.setGeometry(580,110,130,40)

        self.customCharacterLine = QLineEdit(self.characterWidget)
        self.customCharacterLine.setFont(QFont('Segoe UI', 12))
        self.customCharacterLine.setGeometry(715,110,75,40)
        self.customCharacterLine.setPlaceholderText("ID")

        self.characterButtonMaker = QPushButton("Character Maker", self.characterWidget, clicked = lambda: MainWindow.gotoLayout("MakerUI"))
        self.characterButtonMaker.setFont(QFont('Segoe UI', 12))
        self.characterButtonMaker.setGeometry(580,160,130,40)
        self.characterButtonMaker.setStyleSheet('''font-size: 12pt;''')

        myform.addWidget(self.characterWidget)

        #### FIRST STEPS

        self.endingWidget = QWidget()
        self.endingWidget.setFixedSize(1004,500)
        self.endingWidget.setStyleSheet('''
        QWidget{
    	background-color:rgb(23, 23, 23);
        }
        ''')

        self.titleLabel = QLabel("After Starting", self.endingWidget, objectName = "Title")
        self.titleLabel.setFont(QFont('Segoe UI', 20))
        self.titleLabel.setGeometry(10,10,984,40)
        self.titleLabel.setAlignment(Qt.AlignVCenter)
        self.titleLabel.setAlignment(Qt.AlignHCenter)
        self.titleLabel.setStyleSheet('''
        QLabel{
        border: 1px solid black;
        background : rgb(35, 35, 35);
        color:rgb(255, 255, 255)
        }
        ''')

        self.AfterLabel = QLabel(self.endingWidget)
        self.AfterLabel.setFont(QFont('Segoe UI', 16))
        self.AfterLabel.setGeometry(10,60,984,240)
        self.AfterLabel.setAlignment(Qt.AlignVCenter)
        self.AfterLabel.setAlignment(Qt.AlignTop)
        self.AfterLabel.setText("After starting you might notice the game being barren of characters, that is because you need to go back to the mennu, and into the 'Manage Character' tab, here you'll find all the characters you can import into your current game, and if you want more than just those, you can always make them in the 'Character Maker' tab, or checking to see if anyone has made any character that might interest you..")
        self.AfterLabel.setWordWrap(True)

        myform.addWidget(self.endingWidget)


        mygroupbox = QGroupBox()
        # mygroupbox.setFont(QFont('Segoe UI', 14))
        mygroupbox.setLayout(myform)
        self.scroll.setWidget(mygroupbox)

        # self.startCheck()

        ##################


    # def testFun(self):
    #     self.characterWidget.hide()
    # def testFun2(self):
    #     self.characterWidget.show()

    def buttonTest(self, text):
        print(text)

    def buttonCharacter(self, button):
        ""
        # if button == "Male":
        #     ""
        #     # self.femaleCharacterButton.setChecked(0)
        #     # self.futanariCharacterButton.setChecked(0)
        #     # self.customCharacterButton.setChecked(0)
        # elif button == "Female":
        #     # self.maleCharacterButton.setChecked(0)
        #     # self.futanariCharacterButton.setChecked(0)
        #     # self.customCharacterButton.setChecked(0)
        # elif button == "Futanari":
        #     # self.maleCharacterButton.setChecked(0)
        #     # self.femaleCharacterButton.setChecked(0)
        #     # self.customCharacterButton.setChecked(0)
        # elif button == "Custom":
        #     # self.maleCharacterButton.setChecked(0)
        #     # self.femaleCharacterButton.setChecked(0)
        #     # self.futanariCharacterButton.setChecked(0)

    def NewGame(self, Who):
        if Who == "Female":
            Name = self.nameCharacterLine.text()
            if Name == "":
                self.statusLabel.setText("Please introduce a name for your character.")
            else:
                NPCData = {
                "Name": Name,
                "ID": "0",
                "Personality": "Standard0",
                "State": {
                    "Energy": 2000,
                    "Mood": 0,
                    "Arousal": 0,
                    "Alcohol": 0,
                    "Drugs": 0,
                    "PConscious": 1,
                    "MConscious": 1,
                },
                "Relations": {},
                "BodyData": {
                    "FullName": Name,
                    "SkinColor": "Pale",
                    "HairColor": "Dark",
                    "PhysicalAge": 2,
                    "Race": "Human",
                    "Face": 5,
                    "Eyes": "Brown",
                    "Lips": 2,
                    "Height": 4,
                    "Complexion": 3,
                    "Sex": "Female",
                    "Pronouns": {"PSub": "She", "PObj": "Her", "PPos": "Her", "PIPos": "Hers"},
                    "Hips": 3,
                    "Ass": 3,
                    "Chest": 4,
                    "VTightness": 3,
                    "ATightness": 3,
                    "PenisSize": 0,
                    "BallsSize": 0,
                    "VVirgin": True,
                    "AVirgin": True,
                    "PVirgin": True,
                    "MVirgin": True,
                },
                "OtherData": {"Home": f"{Name}'s Home"},
                "Traits": {
                    "Courage0": 0,
                    "Attitude0": 0,
                    "Pride0": 0,
                    "Dere0": 0,
                    "SelfControl0": 0,
                    "Cheerfulness0": 0,
                    "Shyness0": 0,
                    "Gullible0": 0,
                    "Charm0": 0,
                    "SubstanceResistance0": 0,
                    "SexualInterest0": 0,
                    "Virtue0": 0,
                    "Chastity0": 0,
                    "Openess0": 0,
                    "PainResistance0": 0,
                    "ArousalEase0": 0,
                    "ResponseToPleasure0": 0,
                    "Perversion0": 0,
                    "Dominance0": 0,
                    "Forceful0": 0,
                    "Loyalty0": 0,
                    "Violence0": 0,
                    "Beauty0": 0,
                    "Shame0": 0,
                    "Will0": 0,
                    "Influence0": 0,
                    "Fertility0": 0,
                    "LewdBody0": {"V": False, "A": False, "B": False, "P": False, "M": False},
                },
                "GeneralFlags": {},
                "GeneralAbilities": {"MaxEnergy": 2000},
                "CombatAbilities": {"DeckName": None},
                "Descriptions": {
                    "Backstory": "",
                    "Core": "",
                    "Head": "",
                    "Arms": "",
                    "Legs": "",
                    "Genitals": "",
                },
                "Actions": {
                    "Intention": None,
                    "Action": None,
                    "PreviousTask": {
                        "HourStart": 0,
                        "HourFinish": 1,
                        "Task": [
                            "Idling",
                            {"BriefFluff": "Idling in the streets of ", "LongFluff": ""},
                        ],
                        "InterruptionPenalty": 0,
                        "Location": "ResidentialArea",
                    },
                    "CurrentTask": {
                        "HourStart": 0,
                        "HourFinish": 1,
                        "Task": [
                            "Idling",
                            {"BriefFluff": "Idling in the streets of ", "LongFluff": ""},
                        ],
                        "InterruptionPenalty": 0,
                        "Location": "ResidentialArea",
                    },
                    "FutureTask": {
                        "HourStart": 0,
                        "HourFinish": 1,
                        "Task": [
                            "Idling",
                            {"BriefFluff": "Idling in the streets of ", "LongFluff": ""},
                        ],
                        "InterruptionPenalty": 0,
                        "Location": "ResidentialArea",
                    },
                    "TaskData": {},
                    "HasFollowing": [],
                    "InteractionParty": {},
                    "SexualPary": [],
                    "IsFollowing": None,
                    "isInSexScene": [],
                    "Targeting": None,
                },
                "Items": {},
                "isInSexScene": 0,
                "Version": 2,
            }
        elif Who == "Male":
            Name = self.nameCharacterLine.text()
            if Name == "":
                self.statusLabel.setText("Please introduce a name for your character.")
            else:
                NPCData = {
                "Name": Name,
                "ID": "0",
                "Personality": "Standard0",
                "State": {
                    "Energy": 2000,
                    "Mood": 0,
                    "Arousal": 0,
                    "Alcohol": 0,
                    "Drugs": 0,
                    "PConscious": 1,
                    "MConscious": 1,
                },
                "Relations": {},
                "BodyData": {
                    "FullName": Name,
                    "SkinColor": "Pale",
                    "HairColor": "Dark",
                    "PhysicalAge": 2,
                    "Race": "Human",
                    "Face": 5,
                    "Eyes": "Brown",
                    "Lips": 2,
                    "Height": 4,
                    "Complexion": 3,
                    "Sex": "Male",
                    "Pronouns": {"PSub": "He", "PObj": "Him", "PPos": "His", "PIPos": "His"},
                    "Hips": 3,
                    "Ass": 3,
                    "Chest": 4,
                    "VTightness": 0,
                    "ATightness": 3,
                    "PenisSize": 3,
                    "BallsSize": 3,
                    "VVirgin": True,
                    "AVirgin": True,
                    "PVirgin": True,
                    "MVirgin": True,
                },
                "OtherData": {"Home": "Aria0 Room"},
                "Traits": {
                    "Courage0": 0,
                    "Attitude0": 0,
                    "Pride0": 0,
                    "Dere0": 0,
                    "SelfControl0": 0,
                    "Cheerfulness0": 0,
                    "Shyness0": 0,
                    "Gullible0": 0,
                    "Charm0": 0,
                    "SubstanceResistance0": 0,
                    "SexualInterest0": 0,
                    "Virtue0": 0,
                    "Chastity0": 0,
                    "Openess0": 0,
                    "PainResistance0": 0,
                    "ArousalEase0": 0,
                    "ResponseToPleasure0": 0,
                    "Perversion0": 0,
                    "Dominance0": 0,
                    "Forceful0": 0,
                    "Loyalty0": 0,
                    "Violence0": 0,
                    "Beauty0": 0,
                    "Shame0": 0,
                    "Will0": 0,
                    "Influence0": 0,
                    "Fertility0": 0,
                    "LewdBody0": {"V": False, "A": False, "B": False, "P": False, "M": False},
                },
                "GeneralFlags": {},
                "GeneralAbilities": {"MaxEnergy": 2000},
                "CombatAbilities": {"DeckName": None},
                "Descriptions": {
                    "Backstory": "",
                    "Core": "",
                    "Head": "",
                    "Arms": "",
                    "Legs": "",
                    "Genitals": "",
                },
                "Actions": {
                    "Intention": None,
                    "Action": None,
                    "PreviousTask": {
                        "HourStart": 0,
                        "HourFinish": 1,
                        "Task": [
                            "Idling",
                            {"BriefFluff": "Idling in the streets of ", "LongFluff": ""},
                        ],
                        "InterruptionPenalty": 0,
                        "Location": "ResidentialArea",
                    },
                    "CurrentTask": {
                        "HourStart": 0,
                        "HourFinish": 1,
                        "Task": [
                            "Idling",
                            {"BriefFluff": "Idling in the streets of ", "LongFluff": ""},
                        ],
                        "InterruptionPenalty": 0,
                        "Location": "ResidentialArea",
                    },
                    "FutureTask": {
                        "HourStart": 0,
                        "HourFinish": 1,
                        "Task": [
                            "Idling",
                            {"BriefFluff": "Idling in the streets of ", "LongFluff": ""},
                        ],
                        "InterruptionPenalty": 0,
                        "Location": "ResidentialArea",
                    },
                    "TaskData": {},
                    "HasFollowing": [],
                    "InteractionParty": {},
                    "SexualPary": [],
                    "IsFollowing": None,
                    "isInSexScene": [],
                    "Targeting": None,
                },
                "Items": {},
                "isInSexScene": 0,
                "Version": 2,
            }
        elif Who == "Futanari":
            Name = self.nameCharacterLine.text()
            if Name == "":
                self.statusLabel.setText("Please introduce a name for your character.")
            else:
                NPCData = {
                "Name": Name,
                "ID": "0",
                "Personality": "Standard0",
                "State": {
                    "Energy": 2000,
                    "Mood": 0,
                    "Arousal": 0,
                    "Alcohol": 0,
                    "Drugs": 0,
                    "PConscious": 1,
                    "MConscious": 1,
                },
                "Relations": {},
                "BodyData": {
                    "FullName": Name,
                    "SkinColor": "Pale",
                    "HairColor": "Dark",
                    "PhysicalAge": 2,
                    "Race": "Human",
                    "Face": 5,
                    "Eyes": "Brown",
                    "Lips": 2,
                    "Height": 4,
                    "Complexion": 3,
                    "Sex": "Male",
                    "Pronouns": {"PSub": "She", "PObj": "Her", "PPos": "Her", "PIPos": "Hers"},
                    "Hips": 3,
                    "Ass": 3,
                    "Chest": 4,
                    "VTightness": 3,
                    "ATightness": 3,
                    "PenisSize": 3,
                    "BallsSize": 3,
                    "VVirgin": True,
                    "AVirgin": True,
                    "PVirgin": True,
                    "MVirgin": True,
                },
                "OtherData": {"Home": "Aria0 Room"},
                "Traits": {
                    "Courage0": 0,
                    "Attitude0": 0,
                    "Pride0": 0,
                    "Dere0": 0,
                    "SelfControl0": 0,
                    "Cheerfulness0": 0,
                    "Shyness0": 0,
                    "Gullible0": 0,
                    "Charm0": 0,
                    "SubstanceResistance0": 0,
                    "SexualInterest0": 0,
                    "Virtue0": 0,
                    "Chastity0": 0,
                    "Openess0": 0,
                    "PainResistance0": 0,
                    "ArousalEase0": 0,
                    "ResponseToPleasure0": 0,
                    "Perversion0": 0,
                    "Dominance0": 0,
                    "Forceful0": 0,
                    "Loyalty0": 0,
                    "Violence0": 0,
                    "Beauty0": 0,
                    "Shame0": 0,
                    "Will0": 0,
                    "Influence0": 0,
                    "Fertility0": 0,
                    "LewdBody0": {"V": False, "A": False, "B": False, "P": False, "M": False},
                },
                "GeneralFlags": {},
                "GeneralAbilities": {"MaxEnergy": 2000},
                "CombatAbilities": {"DeckName": None},
                "Descriptions": {
                    "Backstory": "",
                    "Core": "",
                    "Head": "",
                    "Arms": "",
                    "Legs": "",
                    "Genitals": "",
                },
                "Actions": {
                    "Intention": None,
                    "Action": None,
                    "PreviousTask": {
                        "HourStart": 0,
                        "HourFinish": 1,
                        "Task": [
                            "Idling",
                            {"BriefFluff": "Idling in the streets of ", "LongFluff": ""},
                        ],
                        "InterruptionPenalty": 0,
                        "Location": "ResidentialArea",
                    },
                    "CurrentTask": {
                        "HourStart": 0,
                        "HourFinish": 1,
                        "Task": [
                            "Idling",
                            {"BriefFluff": "Idling in the streets of ", "LongFluff": ""},
                        ],
                        "InterruptionPenalty": 0,
                        "Location": "ResidentialArea",
                    },
                    "FutureTask": {
                        "HourStart": 0,
                        "HourFinish": 1,
                        "Task": [
                            "Idling",
                            {"BriefFluff": "Idling in the streets of ", "LongFluff": ""},
                        ],
                        "InterruptionPenalty": 0,
                        "Location": "ResidentialArea",
                    },
                    "TaskData": {},
                    "HasFollowing": [],
                    "InteractionParty": {},
                    "SexualPary": [],
                    "IsFollowing": None,
                    "isInSexScene": [],
                    "Targeting": None,
                },
                "Items": {},
                "isInSexScene": 0,
                "Version": 2,
            }
        elif Who == "Custom":
            ID = None
            try:
                ID = self.customCharacterLine.text()
                if ID.strip() == "" or ID == None:
                    raise
                else:
                    print(ID)
                print(ID)
                NPCList = os.listdir("NPCdata")
                for ItemName in NPCList:
                    if ItemName.endswith(ID):
                        NPCName = ItemName

                with open(f"NPCdata/{NPCName}/{NPCName}Data.json", 'rb') as f:
                    NPCData = json.load(f)
            except:
                if ID == None or ID.strip() == "":
                    self.statusLabel.setText("Please introduce the ID for your character.")
                ""

        try:
            NPCData
            Globals.CurrentSession = {}
            Globals.References["BasicMod"].SetBaseData()
            ID = NPCData["ID"]
            Globals.SoLNPCData[ID] = NPCData
            Globals.SoLPCData["ID"] = ID
            Globals.Layouts["MainF"].gotoLayout("SoLUI")
        except Exception as e:
            ""



    def saveFunction(self):
        #### FIRST GETS THE CHARACTER OF THE PLAYER
        with open("ResetData/baseRelationship.json", 'rb') as f:
            baseRelationship = json.load(f)
        Character = ""
        if self.customCharacterButton.isChecked() == False:
            Name = self.nameCharacterLine.text()
            if self.maleCharacterButton.isChecked() == True:
                BodyType = {'Pronouns': {'Pronoun1': 'He', 'Pronoun2': 'Him', 'Pronoun3': 'His', 'Structure': 'Male'}, 'Race': 'Human', 'SkinColor': 'Pale', 'HairColor': 'Dark', 'FaceType': 1, 'BodySize': 3, 'ChestSize': 0, 'Complexion': 3, 'AssSize': 0, 'HipsSize': 0, 'VTightness': 0, 'ATightness': 3, 'PenisSize': 3, 'BallsSize': 3, 'LipsSize': 2}
            elif self.femaleCharacterButton.isChecked() == True:
                BodyType = {'Pronouns': {'Pronoun1': 'She', 'Pronoun2': 'Her', 'Pronoun3': 'Hers', 'Structure': 'Female'}, 'Race': 'Human', 'SkinColor': 'Pale', 'HairColor': 'Dark', 'FaceType': 5, 'BodySize': 3, 'ChestSize': 4, 'Complexion': 3, 'AssSize': 3, 'HipsSize': 3, 'VTightness': 3, 'ATightness': 3, 'PenisSize': 0, 'BallsSize': 0, 'LipsSize': 2}
            else:
                BodyType = {'Pronouns': {'Pronoun1': 'She', 'Pronoun2': 'Her', 'Pronoun3': 'Hers', 'Structure': 'Female'}, 'Race': 'Human', 'SkinColor': 'Pale', 'HairColor': 'Dark', 'FaceType': 3, 'BodySize': 3, 'ChestSize': 4, 'Complexion': 3, 'AssSize': 3, 'HipsSize': 3, 'VTightness': 3, 'ATightness': 3, 'PenisSize': 3, 'BallsSize': 3, 'LipsSize': 2}


            State = {'Energy': 1500, 'Mood': 0, 'Arousal': 0, 'Alcohol': 0, 'Drugs': 0, 'Unconcious': 0}
            Relations = {'0': baseRelationship}
            GeneralFlags = {'HasUniqueDialog': 0, 'HasUniqueBodyDescriptor': 0}
            Traits = {'isCourage': 0, 'isAttitude': 0, 'isPride': 0, 'isDere': 0, 'isControl': 0, 'isCheerful': 0, 'isShy': 0, 'isGullible': 0, 'isCharm': 0, 'isSubstanceResistance': 0, 'isSexualInterest': 0, 'isVirtue': 0, 'isChastity': 0, 'isOpenessTrait': 0, 'isPainResistance': 0, 'isAroussalEase': 0, 'isResponseToPleasure': 0, 'isPerversion': 0, 'isDominanceTrait': 0, 'isForcefulTrait': 0, 'isLoyaltyTrait': 0, 'isViolenceTrait': 0, 'isBeautyTrait': 0, 'isShameTrait': 0, 'isWillTrait': 0, 'isInfluenceTrait': 0, 'isFertility': 0, 'isVirginV': 1, 'isVirginA': 1, 'isVirginM': 1, 'isVirginP': 1, 'isLewdV': 0, 'isLewdA': 0, 'isLewdB': 0, 'isLewdM': 0, 'isLewdP': 0}
            GeneralAbilities = {'Work': 0, "MaxEnergy":6000}
            CombatAbilities = {'CombatAbilities': 0}
            Descriptions = {'Backstory': '', 'Core': '', 'Head': '', 'Arms': '', 'Legs': '', 'Genitals': ''}
            Version = 1
            Actions = {"PreviousTask": {"HourStart": 0, "HourFinish": 1, "Task": ["Idlying", {"Fluff": "Idlying in the streets of "}], "Location": "Residential Area"}, "CurrentTask": {"HourStart": 2, "HourFinish": 3, "Task": ["Idlying", {"Fluff": "Idlying in the streets of "}], "Location": "Residential Area"}, "FutureTask": {"HourStart": 4, "HourFinish": 5, "Task": ["Idlying", {"Fluff": "Idlying in the streets of "}], "Location": "Residential Area"}, "HasFollowing": [], "InteractionParty": {}, "IsFollowing": 0, "isInSexScene": []}

            NPCdata = {"Name":Name, "FullName":Name, "ID":"0", "State":State, "Relations":Relations, "BodyType":BodyType, "GeneralFlags":GeneralFlags, "Traits":Traits, "GeneralAbilities":GeneralAbilities, "CombatAbilities":CombatAbilities, "Descriptions":Descriptions, "Version":Version, "Actions":Actions}
            ID = "0"
            ShortName = Name
            if ID == "" or ShortName == "":
                print("Please fill the ID or Short Name")
            else:
                path = "NPCdata/" + ShortName + ID
                if not os.path.exists(path):
                    os.makedirs(path)
                x = path + "/" + ShortName + ID + "Data.json"
                with open(x, 'w') as f:
                    json.dump(NPCdata, f)

        else:
            if self.customCharacterLine.text() == "":
                print("Please add the ID.")
            else:
                try:
                    #### TRIES TO RETRIEVE TEH NPCDATA BASED ON THE ID
                    ID = self.customCharacterLine.text()
                    NPClist = os.listdir("NPCdata")
                    NameWhole = ""
                    for NPC in NPClist:
                        y = len(NPC)
                        z = len(ID)
                        NPCID = NPC[y-z:y]
                        if NPCID == ID:
                            NameWhole = NPC
                    path = "NPCdata/" + str(NameWhole) + "/" + str(NameWhole) + "Data.json"
                    with open(path, 'rb') as f:
                        NPCdata = json.load(f)
        #### WITH THE NPCdata RETRIEVED THEN IT RESETS THE FILES
                except:
                    print("An error occured when reading the NPC data")
        # enviorementData
        with open("ResetData/enviorementData.json", 'rb') as f:
            enviorementData = json.load(f)
        with open("enviorementData.json", 'w') as f:
            json.dump(enviorementData, f)

        # with open("enviorementData.json", 'rb') as f:
        #     enviorementData = json.load(f)
        # locations = enviorementData["Locations"]
        # for i in locations:
        #     locations[i]["inHere"] = []
        # enviorementData["Locations"] = locations
        #
        # dateData = enviorementData["DateData"]
        # dateData["Hour"] = 480
        # dateData["Day"] = 12
        # dateData["Month"] = 3
        # dateData["Year"] = 1395
        # dateData["Weather"] = "Sunny"
        # dateData["DaysPlayed"] = 0
        # dateData["Previous"] = 480
        #
        # enviorementData["DateData"] = dateData
        # print(enviorementData)
        # # with open("enviorementData.json", 'w') as f:
        # #     json.dump(enviorementData, f)

        #PCdata
        with open("PCdata.json", 'rb') as f:
            PCdata = json.load(f)
        PCdata["Name"] = NPCdata["Name"]
        PCdata["ID"] = NPCdata["ID"]
        PCdata["Quest"] = {"CurrentQuestText": "", "CurrentQuest": ""}
        PCdata["Items"] = {"Alcohol": 60}
        PCdata["Others"] = {"Others": "Others", "PinnedText": ""}
        PCdata["Status"] = {"Energy": 6000}
        with open("PCdata.json", 'w') as f:
            json.dump(PCdata, f)
        #NPCdata
        NPCdataWhole = {ID:NPCdata}
        with open("NPCdata.json", 'w') as f:
            json.dump(NPCdataWhole, f)

        #tempData
        with open("tempData.json", 'rb') as f:
            tempData = json.load(f)
        tempData["Name"] = NPCdata["Name"]
        tempData["commandPage"] = 1
        tempData["isInSexScene"] = 0
        tempData["ID"] = NPCdata["ID"]
        tempData["NPCpage"] = 1
        tempData["Following"] = {}
        tempData["PlayerID"] = NPCdata["ID"]
        tempData["Location"] = "Home"
        tempData["PlayerTargetID"] = "0"
        tempData["FlavorText"] = {"LocationText": "", "NPCtext": "", "AttitudeText": "", "CommandText": ""}
        with open("tempData.json", 'w') as f:
            json.dump(tempData, f)
        print("Everything alright")

    def Refresh(self):
        ""

class UiLayoutNewGameMenu(object):
    def __init__(self):
        Globals.Layouts["NewGameUI"] = self
        Globals.LayoutsData["NewGameUI"] = {"Source":"sleepMenuUI"}


    def UI(self):
        MainWindow = Globals.Layouts["MainF"]
        self.GUI = QWidget(MainWindow)

        BoxLabel = QLabel("Maker", self.GUI)
        BoxLabel.setGeometry(50,50,1014,45)
        BoxLabel.setProperty("Color","Dark")


        self.MakerScroll = QScrollArea(self.GUI)
        self.MakerScroll.setGeometry(50,100,1014,904)
        self.MakerScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.MakerScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.MakerScroll.setStyleSheet('''background-color:rgb(23,23,23)''')

        self.MakerForm = QGridLayout()
        self.MakerBox = QGroupBox()
        self.MakerBox.setLayout(self.MakerForm)
        self.MakerBox.setMaximumWidth(1014)
        self.MakerBox.setMinimumWidth(1014)
        self.MakerBox.setMaximumHeight(504)
        self.MakerBox.setMinimumHeight(504)
        self.MakerScroll.setWidget(self.MakerBox)
        self.MakerForm.setContentsMargins(0, 0, 0, 0)
        self.MakerForm.WidgetsDict = {}

        Object = Globals.Layouts["MakerUI"]

        try:
            Layout = Object.GUI
            # if Object.GUI not in self.LayoutsBox.LayoutsList:
            #     self.LayoutsBox.LayoutsList.append(Object.GUI)
            #     self.LayoutsBox.addWidget(Object.GUI)
        except:
            Object.UI()
            Layout = Object.GUI
            # if Object.GUI not in self.LayoutsBox.LayoutsList:
            #     self.LayoutsBox.LayoutsList.append(Object.GUI)
            #     self.LayoutsBox.addWidget(Object.GUI)
        self.MakerForm.addWidget(Layout)



    def Refresh(self):
        ""


def Initialize(self, Reference):
    if "NewGameUI" not in Globals.Layouts:
        Object = UiLayoutNewGameMenuOld()
