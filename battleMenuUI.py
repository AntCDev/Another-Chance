import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QLineEdit, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QApplication

from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QTextCursor
import json
import os
import Globals
import random
import Globals

from PyQt5 import QtCore, QtGui, QtWidgets
import random, math
import time

from PyQt5 import QtGui, QtSvg
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem
from PyQt5.QtGui import QPen, QBrush, QPolygonF
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.QtSvg import QGraphicsSvgItem
path = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(0,path)
Log = Globals.Layouts["MainF"].Log


from math import sqrt
class UiLayoutBattleMenu(QWidget):
    def __init__(self):
        Globals.Layouts["BattleMenu"] = self
        Globals.LayoutsData["BattleMenu"] = {"Source":"battleMenuUI", "Initialized":0}

    def UI(self):
        MainWindow = Globals.Layouts["MainF"]
        Encounter = Globals.LayoutsData["BattleMenu"]["Encounter"]
        Coordinates = Globals.LayoutsData["BattleMenu"]["Coordinates"]


        self.GUI = QWidget(MainWindow)
        self.Encounter = Encounter
        self.Coordinates = Coordinates
        # mainwindow.setWindowIcon(QtGui.QIcon('PhotoIcon.png'))
        self.GUI.setStyleSheet('''
        QWidget{
    	background-color:rgb(35, 35, 35);
        }
        QPushButton{
        	color:rgb(255, 255, 255)
        }
        QPushButton:hover{
        	color:rgb(255, 255, 0)
        }
        QLabel{
         border: 1px solid black;
         background : rgb(23, 23, 23);
         color:rgb(255, 255, 255)
        }
        QLineEdit{
        color:rgb(255, 255, 255)
        }
		QWidget{ background-color:rgb(35, 35, 35); border-color:rgb(200,200,200)
        }
        QPushButton{
        	color:rgb(255, 255, 255)
        }
        QPushButton:hover{
        	color:rgb(255, 255, 0)
        }
        QLabel{
         border: 1px solid black;
         background : rgb(35, 35, 35);
         color:rgb(255, 255, 255)
        }
        QLineEdit{
		border: 1px solid black;
        color:rgb(255, 255, 255)
        }
        QGroupBox{
        border: 1px solid black;
        background-color:rgb(35, 35, 35);
        }
        QScrollArea{
        border: 1px solid black;
        background-color:rgb(23, 23, 23);
        }
         ''')
        # MainWindow.setCentralWidget(self.GUI)
        # MainWindow.resize(1600, 1024)

        # self.RewardsWidget = QWidget(self.GUI)
        # self.RewardsWidget.setStyleSheet('''
        # QWidget{
        #   background-color:rgb(23, 23, 23);
        # }
        # .QWidget{
        #   border: 1px solid yellow
        # }
        # ''')

        self.labelArtifacts = QLabel("Label Artifacts", self.GUI)
        self.labelArtifacts.setGeometry(430,65,740,50)
        self.labelArtifacts.setFont(QFont('Segoe UI', 14))
        self.labelArtifacts.setStyleSheet('''
                QLabel{
         border: 1px solid black;
         background : rgb(23, 23, 23);
         color:rgb(255, 255, 255);
        }
        ''')

        self.labelMain = QLabel("Label Main", self.GUI)
        self.labelMain.setGeometry(430,125,740,425)
        self.labelMain.setFont(QFont('Segoe UI', 14))
        self.labelMain.setStyleSheet('''
                QLabel{
         border: 1px solid black;
         background : rgb(23, 23, 23);
         color:rgb(255, 255, 255);
        }
        ''')

        self.labelBackCard = QScrollArea(self.GUI)
        self.labelBackCard.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.labelBackCard.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.labelBackCard.setWidgetResizable(True)
        self.labelBackCard.setGeometry(430,560,290,445)
        self.labelBackCard.setWidgetResizable(True)

        self.scrollE = QScrollArea(self.GUI)
        self.scrollE.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollE.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollE.setGeometry(1180,10,410,1000)
        self.scrollE.setStyleSheet('''
        QScrollArea{
        background-color:rgb(23, 23, 23);
        border: 1px solid black;
        ''')

        self.scrollA = QScrollArea(self.GUI)
        self.scrollA.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollA.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollA.setGeometry(10,10,410,1000)
        self.scrollA.setStyleSheet('''
        QScrollArea{
        background-color:rgb(23, 23, 23);
        border: 1px solid black;
        ''')

        self.scrollR = QScrollArea(self.GUI)
        self.scrollR.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollR.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollR.setGeometry(430,65,740,50)
        self.scrollR.setStyleSheet('''
        QScrollArea{
        background-color:rgb(23, 23, 23);
        border: 1px
        ''')

        self.scrollH = QScrollArea(self.GUI)
        self.scrollH.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollH.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollH.setGeometry(730,560,440,280)
        self.scrollH.setStyleSheet('''
        QScrollArea{
        background-color:rgb(23, 23, 23);
        border: 1px solid black;
        ''')
        self.myformH = QGridLayout()
        self.mygroupboxH = QGroupBox()
        self.mygroupboxH.setStyleSheet('''
        QGroupBox{
        background-color:rgb(23,23,23);
        border: none;kk
        }
        ''')
        self.buttonsList = []


        self.srback = QLabel("SRBack", self.GUI)
        self.srback.setGeometry(430,20,740,40)
        self.srback.setStyleSheet('''
        QLabel{
        background-color:rgb(23,23,23)
        }
        ''')

        self.srscroll = QScrollArea(self.GUI)
        self.srscroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.srscroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.srscroll.setGeometry(430,20,740,40)
        self.srscroll.setStyleSheet('''
        QScrollArea{
        background-color:rgb(23, 23, 23);
        border: 1px solid black;
        }''')


        self.labelCommands = QLabel(self.GUI)
        self.labelCommands.setFont(QFont('Segoe UI', 14))
        self.labelCommands.setGeometry(730,850,440,155)
        self.labelCommands.setStyleSheet('''
        QLabel{
        background-color:rgb(23, 23, 23);
        border: 1px solid black;
        }''')


        self.buttonNextTurn = QPushButton("Next Turn", self.GUI, clicked = lambda: self.EndOfTurn())
        self.buttonNextTurn.setFont(QFont('Segoe UI', 14))
        self.buttonNextTurn.setGeometry(735,860,140,40)

        self.buttonDrawDeck = QPushButton("Draw Pile", self.GUI)
        self.buttonDrawDeck.setFont(QFont('Segoe UI', 14))
        self.buttonDrawDeck.setGeometry(735,910,140,40)

        self.buttonDiscardDeck = QPushButton("Discard Pile", self.GUI)
        self.buttonDiscardDeck.setFont(QFont('Segoe UI', 14))
        self.buttonDiscardDeck.setGeometry(880,910,140,40)

        self.buttonExhaustDeck = QPushButton("Exhaust Pile", self.GUI)
        self.buttonExhaustDeck.setFont(QFont('Segoe UI', 14))
        self.buttonExhaustDeck.setGeometry(1025,910,140,40)

        self.buttonMap = QPushButton("Map", self.GUI, clicked = lambda: MainWindow.gotoLayout("BattleScene") )
        self.buttonMap.setFont(QFont('Segoe UI', 14))
        self.buttonMap.setGeometry(735,960,140,40)

        self.buttonWholeDeck = QPushButton("Whole Deck", self.GUI)
        self.buttonWholeDeck.setFont(QFont('Segoe UI', 14))
        self.buttonWholeDeck.setGeometry(880,960,140,40)

        self.buttonMenu = QPushButton("Menu", self.GUI)
        self.buttonMenu.setFont(QFont('Segoe UI', 14))
        self.buttonMenu.setGeometry(1025,960,140,40)

        self.buttonBack = QPushButton("Back", self.GUI)

        Globals.Layouts["BattleMenu"] = self

    def ressEvent(self):
        self.scrollS.resize(200,200)
    def Initialize(self):
        try:
            Globals.BattleInfo["Deck"]["WholeDeck"] = Globals.CombatDecks["FullDeckWhole"]
            Globals.BattleInfo["Deck"]["DrawDeck"] = Globals.CombatDecks["DrawDeckWhole"]
            Globals.BattleInfo["Deck"]["DiscardDeck"] = Globals.CombatDecks["DiscardDeckWhole"]
            Globals.BattleInfo["Deck"]["CurrentHand"] = Globals.CombatDecks["CurrentHandWhole"]
            Globals.BattleInfo["Deck"]["ExhaustDeck"] = Globals.CombatDecks["ExhaustDeckWhole"]

            # ASIGNS A BUTTON TO EACH ATTACK
            DeckList = ["WholeDeck", "DrawDeck", "DiscardDeck", "CurrentHand", "ExhaustDeck"]
            tempDecks = { "WholeDeck":{}, "DrawDeck":{}, "DiscardDeck":{}, "CurrentHand":{}, "ExhaustDeck":{} }
            for Deck in DeckList:
                for ID in Globals.BattleInfo["Deck"][Deck]:
                    IDNumber = Globals.BattleInfo["Deck"][Deck][ID]["IDNumber"]
                    if type(Globals.BattleInfo["Deck"][Deck][ID]) is tuple or type(Globals.BattleInfo["Deck"][Deck][ID]) is list:
                        if Globals.BattleInfo["Deck"][Deck][ID][0] != "Button":
                            continue
                    Attack = Globals.BattleInfo["Deck"][Deck][ID]
                    Button = CardButton(self.GUI, IDNumber, Attack)
                    Card = [Button, Attack]
                    tempDecks[Deck][IDNumber] = Card
            for Deck in tempDecks:
                Globals.BattleInfo["Deck"][Deck] = tempDecks[Deck]
                ""

            Globals.Map[self.Coordinates[0]][self.Coordinates[1]]["Status"] = "Current"
            Globals.MapData["PlayerPath"].append(self.Coordinates)
            # self.StartOfCombat()

            Globals.LayoutsData["BattleMenu"]["Initialized"] = 1
        except Exception as e:
            Log(4, "ERROR BATTLE MENU INITIALIZE", e)

    def Refresh(self):
        try:
            if Globals.LayoutsData["BattleMenu"]["Initialized"] == 0:
                self.Initialize()

            ### Draws the enemies form on the right
            self.myformE = QVBoxLayout()
            isEmpty = 1
            for EnemyID in Globals.BattleObjects["Enemies"]:
                Enemy = Globals.BattleObjects["Enemies"][EnemyID]["Object"]
                Object = Enemy.ObjectWidget()
                Globals.BattleObjects["Enemies"][EnemyID]["Widget"] = Object
                if Enemy.Status != "Defeated":
                    x = self.myformE.addWidget(Object)
                    isEmpty = 0
                    # print(Object.rect())
            mygroupboxE = QGroupBox()
            if isEmpty == 0:
                mygroupboxE.setLayout(self.myformE)
            else:
                if self.Encounter["Status"] == "":
                    self.EndOfEncounter("Victory")
            self.scrollE.setWidget(mygroupboxE)
            self.myformE.setContentsMargins(3, 3, 2, 3)

            ### Draws the allies form on the left
            self.myformA = QVBoxLayout()
            isEmpty = 1
            for AllyID in Globals.BattleObjects["Allies"]:
                Ally = Globals.BattleObjects["Allies"][AllyID]["Object"]
                Object = Ally.ObjectWidget()
                Globals.BattleObjects["Allies"][AllyID]["Widget"] = Object
                if Ally.Status != "Defeated":
                    self.myformA.addWidget(Object)
                    isEmpty = 0
            mygroupboxA = QGroupBox()
            if isEmpty == 0:
                mygroupboxA.setLayout(self.myformA)
            else:
                self.EndOfEncounter("Defeat")
            self.scrollA.setWidget(mygroupboxA)
            self.myformA.setContentsMargins(3, 3, 2, 3)

            ### Draws the cards on the middle bottom.
            for Button in self.buttonsList:
                Button.hide()
                try:
                    self.myformH.removeWidget(Button)
                except:
                    ""
            isEmpty = 1
            Row, Layer = 0, 0
            lst = {}
            for ID in Globals.BattleInfo["Deck"]["CurrentHand"]:
                Button = Globals.BattleInfo["Deck"]["CurrentHand"][ID][0]
                Button.Update()
                Button.show()
                if Row > 2:
                    Row = 0
                    Layer += 1
                self.myformH.addWidget(Button, Layer, Row)
                Row += 1
                isEmpty = 0
            self.myformH.setContentsMargins(3, 5, 5, 5)
            self.myformH.setHorizontalSpacing(5)
            self.myformH.setVerticalSpacing(5)
            if isEmpty == 0:
                self.mygroupboxH.setLayout(self.myformH)
            Height = (Layer + 1) * 50
            Width = Row * 150
            if Width >= 440 or Layer >= 1: Width = 440
            self.mygroupboxH.setGeometry(0,0,Width, Height)
            self.scrollH.setWidget(self.mygroupboxH)


            ### Draws the relics on the top bottom
            self.myformR = QHBoxLayout()
            isEmpty = 1
            for Relic in Globals.BattleInfo["Relics"]:
                RelicWidget = Globals.BattleInfo["RelicsDict"][Relic]["Reference"].getIcon(self, Relic)
                RelicWidget.setMinimumWidth(30)
                RelicWidget.setMinimumHeight(30)
                # self.scrollR.setMinimumWidth(50)
                # self.scrollR.setMinimumHeight(50)
                self.myformR.addWidget(RelicWidget)
                isEmpty = 0
            mygroupboxR = QGroupBox()
            if isEmpty == 0:
                mygroupboxR.setLayout(self.myformR)
            self.scrollR.setWidget(mygroupboxR)
            self.myformR.setContentsMargins(3, 3, 2, 3)

            self.SRUpdate()
            self.CardUpdate()
        except Exception as e:
            Log(4, "ERROR REFRESH", e)
    def ReturnToLayout(self):
        # self.StartOfCombat()
        self.Refresh()
    def SRUpdate(self):
        ### Draws the Skill Rolls at the top
        try:
            self.srform = QHBoxLayout()
            self.srform.setAlignment(Qt.AlignRight)
            isEmpty = 1
            for RollID in Globals.SkillRolls:
                Roll = Globals.SkillRolls[RollID]
                Object = Roll.ObjectWidget()
                self.srform.addWidget(Object)
                isEmpty = 0

            srgroupbox = QGroupBox()
            srgroupbox.setStyleSheet('''
            QGroupBox{
            background-color:rgb(23,23,23);
            border: 0px solid black;
            }
            ''')
            srgroupbox.setAlignment(Qt.AlignRight)

            # CENTERS THE WIDGETS
            if isEmpty == 0:
                srgroupbox.setLayout(self.srform)
            self.srscroll.setWidget(srgroupbox)
            XLocation = 660 - (20 * len(Globals.SkillRolls))
            XLength = (40 * len(Globals.SkillRolls))
            if XLength > 540:
                if XLength > 560:
                    self.srscroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
                XLength = 540
            if XLocation < 360:
                XLocation = 360
            self.srscroll.setGeometry(XLocation,20,XLength,60)
            self.srscroll.setStyleSheet('''
            QScrollArea{
            border: 1px solid black;
            border-right: none;
            border-left: none;
            }
            ''')

        except Exception as e:
            Log(4, "ERROR SRUPDATE", e)
            ""

        ""
    def CardUpdate(self):
        try:
            Attack = Globals.BattleInfo["CurrentCard"]
            AttackReference = Attack["DeckReference"]
            if "Shift" in Globals.Keys:
                Card = AttackReference.getCard(self, Attack, "Details")
            else:
                Card = AttackReference.getCard(self, Attack, "Normal")
            Card.setGeometry(1,1,1000,1000)
            Card.raise_()
            Globals.Layouts["BattleMenu"].labelBackCard.setWidget(Card)
            Globals.BattleInfo["CurrentCard"] = Attack
        except Exception as e:
            ""

    def StartOfCombat(self):
        Globals.DeadEnemies = {}
        self.Initialize()
        self.StartOfTurn()
    def EndOfCombat(self):
        # CLEANS THE DICS USED
        Globals.BattleInfo["Target"] = []
        Globals.BattleInfo["Allies"] = {}
        Globals.BattleInfo["Enemies"] = {}
        Globals.BattleInfo["SR"] = []
        Globals.BattleInfo["Attack"] = ''
        Globals.BattleInfo["Deck"] = {"WholeDeck":[],"DrawDeck":[],"DiscardDeck":[],"CurrentHand":[], "ExhaustDeck":[]}
        Globals.BattleInfo["CurrentCard"] = ''
        Globals.BattleInfo["IDCounter"] = 0
        Globals.SkillRolls = {}
        # Globals.BattleInfo = {"Target":[], "Allies":{}, "Enemies":{},"SR":[],"Attack":'',"Deck":{"WholeDeck":[],"DrawDeck":[],"DiscardDeck":[],"CurrentHand":[], "ExhaustDeck":[]}, "CurrentCard":"", "IDCounter":0, "EffectStages":{"ProcessingStage1":{}, "ProcessingStage2":{}, "ProcessingStage3":{}, "ProcessingStageSOT":{}, "ProcessingStageEOT":{}, "ProcessingStageCRSR":{}, "ProcessingStageEXSR":{}, "ProcessingStageDRCARD":{}, "ProcessingStageDCCARD":{}, "ProcessingStageSMCARD":{}, "ProcessingStageEXCARD":{},  "UniversalEffects":{}, "ProcessingUniversalEffects":{}} }

        Globals.Map[self.Coordinates[0]][self.Coordinates[1]]["Status"] = "Unavailable"
        Globals.LayoutsData["BattleMenu"]["Initialized"] = 0

        Globals.Layouts["MainF"].gotoLayout("BattleScene", "battleMenuUI")
        Globals.Layouts["BattleScene"].ReturnToLayout()
    def EndOfEncounter(self, Type):
        if Type == "Victory":
            self.Encounter["Status"] = "Victory"
            self.GenericReward(self.Encounter, self.Coordinates)

    def GenericReward(self, Encounter, Coordinates):
        self.Rewards = self.CalculateGenericRewards(Encounter, Coordinates)
        self.ShowGenericRewards()
    def CalculateGenericRewards(self, Encounter, Coordinates):
        CR = Encounter["Other"]["CR"]
        Type = Encounter["Type"]

        Reward = []
        if Type == "Encounter":
            # GETS THE GUARANTEED GOLD
            GoldLB = 15 + CR*2
            GoldUB = 45 + CR*8
            Gold = random.randint(int(GoldLB), int(GoldUB))
            Reward.append({"Gold":Gold})

            MCardChance = 20
            NCardChance = 45
            RCardChance = 25
            SRCardChance = 10

            NoRelicChance = 0
            MRelicChance = 100
            NRelicChance = 0
            RRelicChance = 0
            SRRelicChance = 0
        elif Type == "Elite":
            # GETS THE GUARANTEED GOLD
            GoldLB = 55 + CR*2
            GoldUB = 90 + CR*8
            Gold = random.randint(int(GoldLB), int(GoldUB))
            Reward.append({"Gold":Gold})

            MCardChance = 0
            NCardChance = 25
            RCardChance = 55
            SRCardChance = 20

            NoRelicChance = 0
            MRelicChance = 0
            NRelicChance = 65
            RRelicChance = 35
            SRRelicChance = 0
        elif Type == "Boss":
            # GETS THE GUARANTEED GOLD
            GoldLB = 90 + CR*2
            GoldUB = 150 + CR*8
            Gold = random.randint(int(GoldLB), int(GoldUB))
            Reward.append({"Gold":Gold})

            MCardChance = 0
            NCardChance = 0
            RCardChance = 0
            SRCardChance = 100

            NoRelicChance = 0
            MRelicChance = 0
            NRelicChance = 0
            RRelicChance = 0
            SRRelicChance = 100

        # GETS THE GUARANTEED CARD
        CardOptionAmount = 3
        TotalCardChance = MCardChance + NCardChance + RCardChance + SRCardChance
        CardOptions = []
        for i in range(CardOptionAmount):
            RN = random.randint(1,TotalCardChance)
            if RN <= MCardChance:
                AvailableCards = [Globals.CombatDecks["AvailableCardsWhole"][AttackID] for AttackID in Globals.CombatDecks["AvailableCardsWhole"] if Globals.CombatDecks["AvailableCardsWhole"][AttackID]["Rarity"] == "Mundane"]
            elif RN <= (MCardChance + NCardChance):
                AvailableCards = [Globals.CombatDecks["AvailableCardsWhole"][AttackID] for AttackID in Globals.CombatDecks["AvailableCardsWhole"] if Globals.CombatDecks["AvailableCardsWhole"][AttackID]["Rarity"] == "Normal"]
            elif RN <= (MCardChance + NCardChance + RCardChance):
                AvailableCards = [Globals.CombatDecks["AvailableCardsWhole"][AttackID] for AttackID in Globals.CombatDecks["AvailableCardsWhole"] if Globals.CombatDecks["AvailableCardsWhole"][AttackID]["Rarity"] == "Rare"]
            else:
                AvailableCards = [Globals.CombatDecks["AvailableCardsWhole"][AttackID] for AttackID in Globals.CombatDecks["AvailableCardsWhole"] if Globals.CombatDecks["AvailableCardsWhole"][AttackID]["Rarity"] == "SuperRare"]
            Card = random.choice(AvailableCards)
            CardOptions.append(Card)
        Reward.append({"Card":CardOptions})

        # GETS THE RELIC IF POSSIBLE
        TotalRelicChance = NoRelicChance + MRelicChance + NRelicChance + RRelicChance + SRRelicChance
        RelicOptions = []
        MRelics = [Relic for Relic in Globals.BattleInfo["RelicsDict"] if Globals.BattleInfo["RelicsDict"][Relic]["Rarity"] == "Mundane" and Globals.BattleInfo["RelicsDict"][Relic]["Available"] == 1]
        NRelics = [Relic for Relic in Globals.BattleInfo["RelicsDict"] if Globals.BattleInfo["RelicsDict"][Relic]["Rarity"] == "Normal" and Globals.BattleInfo["RelicsDict"][Relic]["Available"] == 1]
        RRelics = [Relic for Relic in Globals.BattleInfo["RelicsDict"] if Globals.BattleInfo["RelicsDict"][Relic]["Rarity"] == "Rare" and Globals.BattleInfo["RelicsDict"][Relic]["Available"] == 1]
        SRRelics = [Relic for Relic in Globals.BattleInfo["RelicsDict"] if Globals.BattleInfo["RelicsDict"][Relic]["Rarity"] == "SuperRare" and Globals.BattleInfo["RelicsDict"][Relic]["Available"] == 1]

        RN = random.randint(1,TotalRelicChance)
        if RN <= MCardChance:
            if MRelics != []:
                PossibleRelics = MRelics
            elif NRelics != []:
                PossibleRelics = NRelics
            elif RRelics != []:
                PossibleRelics = RRelics
            elif SRRelics != []:
                PossibleRelics = SRRelics
            Relic = random.choice(PossibleRelics)
            Reward.append({"Relic":Relic})
            # Globals.BattleInfo["RelicsDict"][Relic]["Reference"].GainRelic(self, Relic)
        elif RN <= (MCardChance + NCardChance):
            if NRelics != []:
                PossibleRelics = NRelics
            elif MRelics != []:
                PossibleRelics = MRelics
            elif RRelics != []:
                PossibleRelics = RRelics
            elif SRRelics != []:
                PossibleRelics = SRRelics
            Relic = random.choice(PossibleRelics)
            Reward.append({"Relic":Relic})
        elif RN <= (MCardChance + NCardChance + RCardChance):
            if RRelics != []:
                PossibleRelics = RRelics
            elif NRelics != []:
                PossibleRelics = NRelics
            elif MRelics != []:
                PossibleRelics = MRelics
            elif SRRelics != []:
                PossibleRelics = SRRelics
            Relic = random.choice(PossibleRelics)
            Reward.append({"Relic":Relic})
        else:
            if SRRelics != []:
                PossibleRelics = SRRelics
            elif RRelics != []:
                PossibleRelics = RRelics
            elif NRelics != []:
                PossibleRelics = NRelics
            elif MRelics != []:
                PossibleRelics = MRelics
            Relic = random.choice(PossibleRelics)
            Reward.append({"Relic":Relic})

        return Reward
    def ShowGenericRewards(self):
        try:
            self.RewardsWidget.hide()
        except:
            ""

        class GoldReward:
            def __init__(self, Reward):
                self.Reward = Reward
                ""
            def getWidget(self):
                GoldWidget = QLabel("Gold" + " " + str(self.Reward["Gold"]))
                def GG():
                    Globals.Layouts["BattleMenu"].ConsumeReward(self.Reward)
                    try:
                        if "Gold" not in Globals.LayoutsData["BattleScene"]:
                            Globals.LayoutsData["BattleScene"]["Gold"] = self.Reward["Gold"]
                        else:
                            Globals.LayoutsData["BattleScene"]["Gold"] += self.Reward["Gold"]
                    except:
                        ""


                GoldWidget.mouseReleaseEvent = lambda event: GG()
                GoldWidget.setMinimumWidth(380)
                GoldWidget.setMinimumHeight(40)
                GoldWidget.setFont(QFont('Segoe UI', 14))
                GoldWidget.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                GoldWidget.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                return GoldWidget

        class CardReward:
            def __init__(self, Reward):
                self.Reward = Reward

            def getWidget(self):
                CardWidget = QPushButton("Card")
                CardWidget.setMinimumWidth(380)
                CardWidget.setMinimumHeight(40)
                CardWidget.setFont(QFont('Segoe UI', 14))
                def CG():
                    Globals.Layouts["BattleMenu"].ConsumeReward(self.Reward)
                    Globals.Layouts["BattleMenu"].DisplayCardOptions(self.Reward)
                CardWidget.mouseReleaseEvent = lambda event: CG()

                return CardWidget

        class RelicReward:
            def __init__(self, Reward):
                self.Reward = Reward

            def getWidget(self):
                Relic = self.Reward["Relic"]
                RelicWidget = QWidget()
                RelicWidget.setMinimumHeight(40)
                RelicWidget.setMinimumWidth(380)


                RelicLabel = QLabel(RelicWidget)
                Text = Globals.BattleInfo["RelicsDict"][Relic]["Reference"].GetText(self, Relic)
                RelicLabel.setText(Text)
                RelicLabel.setMinimumWidth(380)
                RelicLabel.setMinimumHeight(40)
                RelicLabel.setFont(QFont('Segoe UI', 14))
                RelicLabel.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                RelicLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                RelicLabel.mouseReleaseEvent = lambda event: CR()
                def CR():
                    Globals.Layouts["BattleMenu"].ConsumeReward(self.Reward)
                    Globals.BattleInfo["RelicsDict"][Relic]["Reference"].GainRelic(self, Relic)
                    Globals.Layouts["BattleMenu"].Refresh()

                RelicIcon = Globals.BattleInfo["RelicsDict"][Relic]["Reference"].getIcon(self, Relic)
                RelicIcon.setParent(RelicWidget)
                RelicIcon.setGeometry(2,2,36,36)
                RelicIcon.setMinimumWidth(36)
                RelicIcon.setMinimumHeight(36)
                return RelicWidget


        Rewards = self.Rewards
        self.RewardsWidget = QWidget(self.GUI)
        self.RewardsWidget.setGeometry(600,100,400,600)
        self.RewardsWidget.setStyleSheet('''
        .QScrollArea{
        background-color:rgb(23, 23, 23);
        border: 0px solid black;
        }
        .QWidget{
        background-color:rgb(23, 23, 23);
        border: 2px solid black;
        }
        .QGroupBox{
        background-color:rgb(23, 23, 23);
        border: 0px solid black;
        }
        QPushButton:!pressed{
        border-left: 1px solid black;
        border-top: 1px solid black;
        border-right: 2px solid black;
        border-bottom: 2px solid black;
        }
        QPushButton:pressed{
        border-left: 2px solid black;
        border-top: 2px solid black;
        border-right: 1px solid black;
        border-bottom: 1px solid black;
        }
        ''')

        VictoryLabel = QLabel("Victory", self.RewardsWidget)
        VictoryLabel.setGeometry(10,10,380,50)
        VictoryLabel.setFont(QFont('Segoe UI', 18))
        VictoryLabel.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
        VictoryLabel.setStyleSheet('''
        background-color:rgb(35,35,35);
        border: 2px solid black;
        color:white;
        ''')

        ScrollRewards = QScrollArea(self.RewardsWidget)
        ScrollRewards.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        ScrollRewards.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        ScrollRewards.setGeometry(10,70,380,480)
        ScrollRewards.setStyleSheet('''
        QScrollArea{
        background-color:rgb(23, 23, 23);
        ''')

        RewardsLayout = QVBoxLayout(self.RewardsWidget)

        Layer = 0
        RewardItems = {}
        for Reward in Rewards:
            if list(Reward.keys())[0] == "Gold":
                GoldObject = GoldReward(Reward)
                GoldWidget = GoldObject.getWidget()

                RewardsLayout.addWidget(GoldWidget, Layer)
                Layer += 1
            elif list(Reward.keys())[0] == "Card":
                CardObject = CardReward(Reward)
                CardWidget = CardObject.getWidget()

                RewardsLayout.addWidget(CardWidget, Layer)
                Layer += 1
            elif list(Reward.keys())[0] == "Relic":
                RelicObject = RelicReward(Reward)
                RelicWidget = RelicObject.getWidget()

                RewardsLayout.addWidget(RelicWidget, Layer)
                Layer += 1


        RewardsLayout.setContentsMargins(0, 0, 0, 0)
        RewardsBox = QGroupBox()
        RewardsBox.setLayout(RewardsLayout)
        ScrollRewards.setWidget(RewardsBox)
        RewardsBox.setContentsMargins(0, 0, 0, 0)


        def CloseRewards():
            self.Rewards = []
            self.RewardsWidget.hide()
            self.EndOfCombat()
        DoneButton = QPushButton("Done", self.RewardsWidget, clicked = lambda: CloseRewards())
        DoneButton.setGeometry(10,560,380,40)
        # DoneButton.setFont(QFont('Segoe UI', 18))


        self.RewardsWidget.raise_()
        self.RewardsWidget.show()
    def DisplayCardOptions(self, Reward):
        Cards = Reward["Card"]
        try:
            class CardWhole:
                def __init__(self, Attack):
                    self.Attack = Attack

                def getWidget(self):
                    Attack = self.Attack
                    AttackReference = Attack["DeckReference"]

                    CardWhole = QWidget()
                    CardWhole.setStyleSheet('''
                    QWidget{
                    border: None;
                    }
                    ''')

                    CardsLayout = QVBoxLayout(CardWhole)
                    CardsLayout.setContentsMargins(0, 5, 5, 0)

                    Text = AttackReference.getButtonText(self, Attack["AttackID"])
                    AttackLabel = QLabel(Text)
                    AttackLabel.setGeometry(0,0,380,30)
                    AttackLabel.setFont(QFont('Segoe UI', 18))
                    AttackLabel.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                    CardsLayout.addWidget(AttackLabel, 0)

                    def CC():
                        Globals.Layouts["BattleMenu"].CreateCard(Attack)
                        Globals.Layouts["BattleMenu"].CardReward.hide()
                        # Globals.Layouts["BattleMenu"].ConsumeReward(Reward)

                    Card = AttackReference.getCard(self, Attack, "Details")
                    Card.setMinimumWidth(290)
                    Card.setMinimumHeight(445)
                    Card.mouseReleaseEvent = lambda event: CC()
                    CardsLayout.addWidget(Card, 1)


                    return CardWhole


            self.CardReward = QWidget(self.GUI)
            self.CardReward.setGeometry(495,62,620,900)
            self.CardReward.setStyleSheet('''
            .QScrollArea{
            background-color:rgb(23, 23, 23);
            border: 0px solid black;
            }
            .QWidget{
            background-color:rgb(23, 23, 23);
            border: 2px solid black;
            }
            .QGroupBox{
            background-color:rgb(23, 23, 23);
            border: 0px solid black;
            }
            QPushButton:!pressed{
            border-left: 1px solid black;
            border-top: 1px solid black;
            border-right: 2px solid black;
            border-bottom: 2px solid black;
            }
            QPushButton:pressed{
            border-left: 2px solid black;
            border-top: 2px solid black;
            border-right: 1px solid black;
            border-bottom: 1px solid black;
            }
            ''')

            ScrollCards = QScrollArea(self.CardReward)
            ScrollCards.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            ScrollCards.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            ScrollCards.setGeometry(10,10,600,880)
            ScrollCards.setStyleSheet('''
            QScrollArea{
            background-color:rgb(23, 23, 23);
            ''')

            CardsLayoutWhole = QGridLayout(self.CardReward)

            Layer = 0
            CardsWholeList = {}
            CardList = {}

            Row = 0
            Layer = 0
            for Attack in Cards:
                C = CardWhole(Attack)
                Card = C.getWidget()
                CardsLayoutWhole.addWidget(Card, Layer, Row)
                Row += 1
                if Row == 2:
                    Layer += 1
                    Row = 0

            CardsLayoutWhole.setContentsMargins(0, 0, 0, 0)
            CardBox = QGroupBox()
            CardBox.setLayout(CardsLayoutWhole)
            ScrollCards.setWidget(CardBox)
            CardBox.setContentsMargins(0, 0, 0, 0)


            self.CardReward.raise_()
            self.CardReward.show()
        except Exception as e:
            Log(3, "ERROR DISPLAYING CARD OPTIONS", e)
    def ConsumeReward(self, Reward):
        self.Rewards.pop(self.Rewards.index(Reward))
        self.ShowGenericRewards()

    def CreateCard(self, Attack):
        Attack["IDNumber"] = Globals.BattleInfo["IDCounter"]
        Deck = Attack["Deck"]
        Globals.CombatDecks[Deck][Globals.BattleInfo["IDCounter"]] = Attack
        Globals.BattleInfo["IDCounter"] += 1

    def StartOfTurn(self):
        try:
            Globals.SkillRolls = {}
            SRList = Globals.SR
            BaseDraw = 5
            ExtraDraw = 0
            TotalDraw = BaseDraw + ExtraDraw
            MaxCards = 9

            # CALLS TO EFFECTS
            for AllyID in Globals.BattleObjects["Allies"]:
                Parent = AllyID
                try:
                    if Parent in list(Globals.BattleObjects["Enemies"].keys()):
                        ParentType = "Enemies"
                    elif Parent in list(Globals.BattleObjects["Allies"].keys()):
                        ParentType = "Allies"
                except:
                    ""
                for Effect in Globals.BattleInfo["EffectStages"]["ProcessingStageSOT"]:
                    if Effect in Globals.BattleObjects[ParentType][Parent]["Object"].Effects:
                        Data = {"Effect":Effect, "Stage":"SOT", "Parent":Parent, "Who":"Ally", "SRList":SRList, "BaseDraw":BaseDraw, "ExtraDraw":ExtraDraw, "TotalDraw":TotalDraw, "MaxCards":MaxCards}
                        Data = Globals.BattleInfo["EffectStages"]["ProcessingStageSOT"][Effect].EffectTrigger(self, Data)
                        SRList, BaseDraw, ExtraDraw, TotalDraw, MaxCards = Data["SRList"], Data["BaseDraw"], Data["ExtraDraw"], Data["TotalDraw"], Data["MaxCards"]
            for EnemyID in Globals.BattleObjects["Enemies"]:
                Parent = EnemyID
                try:
                    if Parent in list(Globals.BattleObjects["Enemies"].keys()):
                        ParentType = "Enemies"
                    elif Parent in list(Globals.BattleObjects["Allies"].keys()):
                        ParentType = "Allies"
                except:
                    ""
                for Effect in Globals.BattleInfo["EffectStages"]["ProcessingStageSOT"]:
                    if Effect in Globals.BattleObjects[ParentType][Parent]["Object"].Effects:
                        Data = {"Effect":Effect, "Stage":"SOT", "Parent":Parent, "Who":"Enemy", "SRList":SRList, "BaseDraw":BaseDraw, "ExtraDraw":ExtraDraw, "TotalDraw":TotalDraw, "MaxCards":MaxCards}
                        Data = Globals.BattleInfo["EffectStages"]["ProcessingStageSOT"][Effect].EffectTrigger(self, Data)
                        SRList, BaseDraw, ExtraDraw, TotalDraw, MaxCards = Data["SRList"], Data["BaseDraw"], Data["ExtraDraw"], Data["TotalDraw"], Data["MaxCards"]
            for Effect in Globals.BattleInfo["EffectStages"]["ProcessingStageSOT"]:
                if Effect in Globals.BattleInfo["EffectStages"]["UniversalEffects"]:
                    Data = {"Effect":Effect, "Stage":"SOT", "Parent":"Universal", "Who":"Universal", "SRList":SRList, "BaseDraw":BaseDraw, "ExtraDraw":ExtraDraw, "TotalDraw":TotalDraw, "MaxCards":MaxCards}
                    Data = Globals.BattleInfo["EffectStages"]["ProcessingStageSOT"][Effect].EffectTrigger(self, Data)
                    SRList, BaseDraw, ExtraDraw, TotalDraw, MaxCards = Data["SRList"], Data["BaseDraw"], Data["ExtraDraw"], Data["TotalDraw"], Data["MaxCards"]

            # GENERATES THE SkillROlls
            self.CreateSR(SRList)

            # DRAWES THE HAND
            for i in range(TotalDraw):
                self.drawCard(MaxCards)

            # REFRESHES THE SCREEN
            self.Refresh()
        except Exception as e:
            Log(4, "ERROR START OF TURN", e)
    def EndOfTurn(self):
        try:
            DiscardList = []
            for ID in Globals.BattleInfo["Deck"]["CurrentHand"]:
                Card = Globals.BattleInfo["Deck"]["CurrentHand"][ID]
                DiscardList.append(Card)

            SRDiscard = list(Globals.SkillRolls.keys())

            # CALLS TO EFFECTS
            for AllyID in Globals.BattleObjects["Allies"]:
                Parent = AllyID
                try:
                    if Parent in list(Globals.BattleObjects["Enemies"].keys()):
                        ParentType = "Enemies"
                    elif Parent in list(Globals.BattleObjects["Allies"].keys()):
                        ParentType = "Allies"
                except:
                    ""
                for Effect in Globals.BattleInfo["EffectStages"]["ProcessingStageEOT"]:
                    if Effect in Globals.BattleObjects[ParentType][Parent]["Object"].Effects:
                        Data = {"Effect":Effect, "Stage":"EOT", "Parent":Parent, "Who":"Ally", "DiscardList":DiscardList, "SRDiscard":SRDiscard}
                        Data = Globals.BattleInfo["EffectStages"]["ProcessingStageEOT"][Effect].EffectTrigger(self, Data)
                        DiscardList, SRDiscard = Data["DiscardList"], Data["SRDiscard"]
            for EnemyID in Globals.BattleObjects["Enemies"]:
                Parent = EnemyID
                try:
                    if Parent in list(Globals.BattleObjects["Enemies"].keys()):
                        ParentType = "Enemies"
                    elif Parent in list(Globals.BattleObjects["Allies"].keys()):
                        ParentType = "Allies"
                except:
                    ""
                for Effect in Globals.BattleInfo["EffectStages"]["ProcessingStageEOT"]:
                    if Effect in Globals.BattleObjects[ParentType][Parent]["Object"].Effects:
                        Data = {"Effect":Effect, "Stage":"EOT", "Parent":Parent, "Who":"Enemy", "DiscardList":DiscardList, "SRDiscard":SRDiscard}
                        Data = Globals.BattleInfo["EffectStages"]["ProcessingStageEOT"][Effect].EffectTrigger(self, Data)
                        DiscardList, SRDiscard = Data["DiscardList"], Data["SRDiscard"]
            for Effect in Globals.BattleInfo["EffectStages"]["ProcessingStageEOT"]:
                if Effect in Globals.BattleInfo["EffectStages"]["UniversalEffects"]:
                    Data = {"Effect":Effect, "Stage":"EOT", "Parent":"Universal", "Who":"Universal", "DiscardList":DiscardList, "SRDiscard":SRDiscard}
                    Data = Globals.BattleInfo["EffectStages"]["ProcessingStageEOT"][Effect].EffectTrigger(self, Data)
                    DiscardList, SRDiscard = Data["DiscardList"], Data["SRDiscard"]

            # DISCARDS THE CURRENT HARD
            for Card in DiscardList:
                self.discardCard(Card, "CurrentHand")

            # DISCARDS THE SR
            for SR in SRDiscard:
                Globals.SkillRolls[SR].SRClick()
                try:
                    # Globals.SkillRolls[SR].Selected = 0
                    Globals.BattleInfo["SR"].remove(Globals.SkillRolls[SR].ID)
                except:
                    ""

            # CALLS FOR ENEMY ACTIONS
            for EnemyID in Globals.BattleObjects["Enemies"]:
                Parent = EnemyID
                try:
                    if Parent in list(Globals.BattleObjects["Enemies"].keys()):
                        ParentType = "Enemies"
                    elif Parent in list(Globals.BattleObjects["Allies"].keys()):
                        ParentType = "Allies"
                except:
                    ""
                Globals.BattleObjects[ParentType][Parent]["Object"].CallToAction()

            # CALLS THE START OF THE NEW TURN
            self.StartOfTurn()
        except Exception as e:
            Log(4, "ERROR END OF TURN", e)

    def KeyHandling(self, Type, key, e):
        try:
            if Type == "Pressed":
                if key == "Shift":     # Key Shift
                    self.CardUpdate()
            elif Type == "Released":
                if "Control" in Globals.Keys:
                    SRList = list(Globals.SkillRolls.keys())
                    if key == "Shift":
                        self.CardUpdate()
                    elif key == "1":
                        Globals.SkillRolls[SRList[0]].SRClick()
                    elif key == "2":
                        Globals.SkillRolls[SRList[1]].SRClick()
                    elif key == "3":
                        Globals.SkillRolls[SRList[2]].SRClick()
                    elif key == "4":
                        Globals.SkillRolls[SRList[3]].SRClick()
                    elif key == "5":
                        Globals.SkillRolls[SRList[4]].SRClick()
                    elif key == "6":
                        Globals.SkillRolls[SRList[5]].SRClick()
                    elif key == "7":
                        Globals.SkillRolls[SRList[6]].SRClick()
                    elif key == "8":
                        Globals.SkillRolls[SRList[7]].SRClick()
                    elif key == "9":
                        Globals.SkillRolls[SRList[8]].SRClick()
                    elif key == "0":
                        Globals.SkillRolls[SRList[9]].SRClick()
                    elif key == "Control":
                        ""
                    elif key == "Tilde":
                        try:
                            for SR in SRList:
                                if Globals.SkillRolls[SR].Selected == 1:
                                    Globals.SkillRolls[SR].SRClick()
                            Globals.Layouts["BattleMenu"].Refresh()
                        except Exception as e:
                            Log(1, "ERROR TILDE KEY", e)
                elif "Shift" in Globals.Keys:
                    if key == "Shift":
                        self.CardUpdate()
                    elif key == "1":
                        if len(list(Globals.BattleObjects["Allies"].keys())) >= 1:
                            Globals.BattleObjects["Allies"][list(Globals.BattleObjects["Allies"].keys())[0]]["Object"].AllyClick()
                    elif key == "2":
                        if len(list(Globals.BattleObjects["Allies"].keys())) >= 2:
                            Globals.BattleObjects["Allies"][list(Globals.BattleObjects["Allies"].keys())[1]]["Object"].AllyClick()
                    elif key == "3":
                        if len(list(Globals.BattleObjects["Allies"].keys())) >= 3:
                            Globals.BattleObjects["Allies"][list(Globals.BattleObjects["Allies"].keys())[2]]["Object"].AllyClick()
                    elif key == "4":
                        if len(list(Globals.BattleObjects["Allies"].keys())) >= 4:
                            Globals.BattleObjects["Allies"][list(Globals.BattleObjects["Allies"].keys())[3]]["Object"].AllyClick()
                    elif key == "5":
                        if len(list(Globals.BattleObjects["Allies"].keys())) >= 5:
                            Globals.BattleObjects["Allies"][list(Globals.BattleObjects["Allies"].keys())[4]]["Object"].AllyClick()
                    elif key == "6":
                        if len(list(Globals.BattleObjects["Allies"].keys())) >= 6:
                            Globals.BattleObjects["Allies"][list(Globals.BattleObjects["Allies"].keys())[5]]["Object"].AllyClick()
                    elif key == "7":
                        if len(list(Globals.BattleObjects["Allies"].keys())) >= 7:
                            Globals.BattleObjects["Allies"][list(Globals.BattleObjects["Allies"].keys())[6]]["Object"].AllyClick()
                    elif key == "8":
                        if len(list(Globals.BattleObjects["Allies"].keys())) >= 8:
                            Globals.BattleObjects["Allies"][list(Globals.BattleObjects["Allies"].keys())[7]]["Object"].AllyClick()
                    elif key == "9":
                        if len(list(Globals.BattleObjects["Allies"].keys())) >= 9:
                            Globals.BattleObjects["Allies"][list(Globals.BattleObjects["Allies"].keys())[8]]["Object"].AllyClick()
                    elif key == "0":
                        if len(list(Globals.BattleObjects["Allies"].keys())) >= 0:
                            Globals.BattleObjects["Allies"][list(Globals.BattleObjects["Allies"].keys())[9]]["Object"].AllyClick()
                    elif key == "Tilde":
                        for Ally in Globals.BattleObjects["Allies"]:
                            if Globals.BattleObjects["Allies"][Ally]["Object"].Selected == 1:
                                Globals.BattleObjects["Allies"][Ally]["Object"].AllyClick()
                else:
                    if key == "Shift":
                        self.CardUpdate()
                    elif key == "1":
                        if len(list(Globals.BattleObjects["Enemies"])) >= 1:
                            Globals.BattleObjects["Enemies"][list(Globals.BattleObjects["Enemies"].keys())[0]]["Object"].EnemyClick()
                    elif key == "2":
                        if len(list(Globals.BattleObjects["Enemies"])) >= 2:
                            Globals.BattleObjects["Enemies"][list(Globals.BattleObjects["Enemies"].keys())[1]]["Object"].EnemyClick()
                    elif key == "3":
                        if len(list(Globals.BattleObjects["Enemies"])) >= 3:
                            Globals.BattleObjects["Enemies"][list(Globals.BattleObjects["Enemies"].keys())[2]]["Object"].EnemyClick()
                    elif key == "4":
                        if len(list(Globals.BattleObjects["Enemies"])) >= 4:
                            Globals.BattleObjects["Enemies"][list(Globals.BattleObjects["Enemies"].keys())[3]]["Object"].EnemyClick()
                    elif key == "5":
                        if len(list(Globals.BattleObjects["Enemies"])) >= 5:
                            Globals.BattleObjects["Enemies"][list(Globals.BattleObjects["Enemies"].keys())[4]]["Object"].EnemyClick()
                    elif key == "6":
                        if len(list(Globals.BattleObjects["Enemies"])) >= 6:
                            Globals.BattleObjects["Enemies"][list(Globals.BattleObjects["Enemies"].keys())[5]]["Object"].EnemyClick()
                    elif key == "7":
                        if len(list(Globals.BattleObjects["Enemies"])) >= 7:
                            Globals.BattleObjects["Enemies"][list(Globals.BattleObjects["Enemies"].keys())[6]]["Object"].EnemyClick()
                    elif key == "8":
                        if len(list(Globals.BattleObjects["Enemies"])) >= 8:
                            Globals.BattleObjects["Enemies"][list(Globals.BattleObjects["Enemies"].keys())[7]]["Object"].EnemyClick()
                    elif key == "9":
                        if len(list(Globals.BattleObjects["Enemies"])) >= 9:
                            Globals.BattleObjects["Enemies"][list(Globals.BattleObjects["Enemies"].keys())[8]]["Object"].EnemyClick()
                    elif key == "0":
                        if len(list(Globals.BattleObjects["Enemies"])) >= 10:
                            Globals.BattleObjects["Enemies"][list(Globals.BattleObjects["Enemies"].keys())[9]]["Object"].EnemyClick()
                    elif key == "Tilde":
                        for Enemy in Globals.BattleObjects["Enemies"]:
                            if Globals.BattleObjects["Enemies"][Enemy]["Object"].Selected == True:
                                Globals.BattleObjects["Enemies"][Enemy]["Object"].EnemyClick()
                    elif key == "T":
                        if "T" == list(Globals.Keys.keys())[-1]:
                            self.EndOfTurn()
                    else:
                        ""
                        # print("Key", key)
        except Exception as e:
            Log(2, "ERROR KEY HANDLING", e)

    def enemyCreate(self):

        ####
        EnemiesPath = os.path.abspath(__file__)
        nameLength = len(os.path.basename(__file__))
        fullLength = len(EnemiesPath)
        EnemiesPath = EnemiesPath[0:fullLength-nameLength]
        EnemiesPath += "Combat\\Enemies"
        if EnemiesPath not in sys.path:
            sys.path.insert(0, EnemiesPath)

        x = os.listdir("Combat/Enemies")
        for file in x:
            if ".py" in file:
                file = file[0:len(file)-3]
                try:
                    print("File", file)
                    EnemyClass = __import__(file)
                    ID = len(Globals.Enemies)
                    EnemyID = f'{file}{ID}'
                    Enemy = EnemyClass.Enemy("Aria", 25, EnemyID)
                    BaseData = Enemy.BaseData()
                    Globals.Enemies[EnemyID] = Enemy
                except:
                    print("NOoo")

        # Globals.Layouts["MainF"].wrking()
        self.refresh()
        ####
    def allyCreate(self, AllyID):
        with open('tempData.json', 'rb') as f:
            tempData = json.load(f)
        with open('NPCData.json', 'rb') as f:
            NPCData = json.load(f)

        # TRIES TO CHECK FOR CUSTOM OBJECTS FOR THE CHARACTER
        try:
            FullPath = os.path.abspath(__file__)
            nameLength = len(os.path.basename(__file__))
            fullLength = len(DeckPath)
            FullPath = FullPath[0:fullLength-nameLength]

            ObjectPath = f'''\\NPCData\\{str(NPCData[ID]["Name"]) + str(ID)}'''
            ObjectFullPath = FullPath + ObjectPath
            if OnjectFullPath not in sys.path:
                sys.path.insert(0, ObjectFullPath)
            Name = NPCData[ID]["Name"]
            Object = __import__(Name)
            Ally = Object.getObject(self)
        except:
            ID = tempData["PlayerID"]
            Name = NPCData[ID]["Name"]
            HP = NPCData[ID]["CombatAbilities"]["HP"]
            Ally = AllyClass(Name, HP, ID)
        Globals.Allies[ID] = Ally
        # {"AttackID":Strike0, "DeckReference":0x0002, "ID":"03", "Flags":{"CanBeUpgraded":1,"CanBeUsed":1,"NumberOfUpgrades":0}}
        # [AttackID, DeckReference]

        # GETS THE DECK OF THE CHARACTER
        try:    # TRIES TO SEE IF THE CHARACTER HAS A CUSTOM DECK
            if NPCData[ID]["CombatAbilities"]["DeckLocation"] != []:
                FullPath = os.path.abspath(__file__)
                nameLength = len(os.path.basename(__file__))
                fullLength = len(DeckPath)
                FullPath = FullPath[0:fullLength-nameLength]

                DeckPath = NPCData[ID]["CombatAbilities"]["DeckLocation"]
                DeckFullPath = FullPath + DeckPath
                if DeckFullPath not in sys.path:
                    sys.path.insert(0, DeckFullPath)
                DeckName = NPCData[ID]["CombatAbilities"]["DeckName"]
                Deck = __import__(DeckName)
                Globals.Decks[DeckName] = Deck
                RawDeck = Deck.getDeck(self)
            else:
                raise
            # RawDeck = Globals.Allies[ID].Deck()
        except:
            try:    # IF NOT THEN IT CHECKS FOR A SPECIFIC CLASS AND CHECKS TO SEE IF THEY EXISTS ON THE /COMBAT/DECKS FOLDER
                if NPCData[ID]["CombatAbilities"]["Class"] != []:
                    FullPath = os.path.abspath(__file__)
                    nameLength = len(os.path.basename(__file__))
                    fullLength = len(DeckPath)
                    FullPath = FullPath[0:fullLength-nameLength]

                    DeckPath = r"\\Combat\\Decks"
                    DeckFullPath = FullPath + DeckPath
                    if DeckFullPath not in sys.path:
                        sys.path.insert(0, DeckFullPath)
                    DeckName = NPCData[ID]["CombatAbilities"]["Class"]
                    Deck = __import__(DeckName)
                    Globals.Decks[DeckName] = Deck
                    RawDeck = Deck.getDeck(self)
                else:
                    raise
            except: # OTHERWISE IT ASSIGNS IT THE WARRIOR CLASS
                FullPath = os.path.abspath(__file__)
                nameLength = len(os.path.basename(__file__))
                fullLength = len(DeckPath)
                FullPath = FullPath[0:fullLength-nameLength]

                DeckPath = r"\\Combat\\Decks"
                DeckFullPath = FullPath + DeckPath
                if DeckFullPath not in sys.path:
                    sys.path.insert(0, DeckFullPath)
                DeckName = "Warrior0"
                Deck = __import__(DeckName)
                Globals.Decks[DeckName] = Deck
                RawDeck = Deck.getDeck(self)
        Deck = []
        for i in RawDeck:
            i["Parent"] = ID
            # Deck
            Deck.append(i)
        # [AttackID, DeckReference, ID]
        Globals.BattleInfo["Deck"]["WholeDeck"] += Deck
        Globals.BattleInfo["Deck"]["DiscardDeck"] += Deck
        self.refresh()

    def CastAttack(self, Data):
        # Flags Type: "Attack", "Effect"
        # Data = { "Target":Target, "Parent":Parent, "Flags":{ "Confirmation":1, "Type":"Attack", "EffectsTrigger":1 }, "Source":<module WarriorDeck0>, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"Weak":{"ID":"Weak","Level":1,"Data":{}}}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
        try:
            if Data["Target"] in list(Globals.BattleObjects["Enemies"].keys()):
                Type = "Enemies"
            elif Data["Target"] in list(Globals.BattleObjects["Allies"].keys()):
                Type = "Allies"
            Parent = Data["Parent"]
            if Parent in list(Globals.BattleObjects["Enemies"].keys()):
                ParentType = "Enemies"
            elif Parent in list(Globals.BattleObjects["Allies"].keys()):
                ParentType = "Allies"
            # SETS THE RESULTS
            OriginalData = Data
            FinalData = Data
            Target = Data["Target"]
            Flags = Data["Flags"]
            Results = { "DamageDealt":0, "MentalDealt":0, "ShieldDamage":0, "HealingDealt":0, "MentalHealingDealt":0, "ShieldApplied":0, "EffectsApplied":{}, "Target":Target, "Flags":Flags }
            # PINGS EVERYONE FOR THE ProcessingStage1
            if FinalData["Flags"]["EffectsTrigger"] == 1:
                for Effect in Globals.BattleInfo["EffectStages"]["ProcessingStage1"]:
                    if Effect in Globals.BattleObjects[Type][Target]["Object"].Effects:
                        Data = {"Effect":Effect, "OriginalData":OriginalData, "FinalData":FinalData, "Results":Results, "Stage":1, "Who":"Target"}
                        Data = Globals.BattleInfo["EffectStages"]["ProcessingStage1"][Effect].EffectTrigger(self, Data)
                        OriginalData, FinalData, Results = Data["OriginalData"], Data["FinalData"], Data["Results"]
                    if Effect in Globals.BattleObjects[ParentType][Parent]["Object"].Effects:
                        Data = {"Effect":Effect, "OriginalData":OriginalData, "FinalData":FinalData, "Results":Results, "Stage":1, "Who":"Caster"}
                        Data = Globals.BattleInfo["EffectStages"]["ProcessingStage1"][Effect].EffectTrigger(self, Data)
                        OriginalData, FinalData, Results = Data["OriginalData"], Data["FinalData"], Data["Results"]
                    if Effect in Globals.BattleInfo["EffectStages"]["UniversalEffects"]:
                        Data = {"Effect":Effect, "OriginalData":OriginalData, "FinalData":FinalData, "Results":Results, "Stage":1, "Who":"Universal"}
                        Data = Globals.BattleInfo["EffectStages"]["ProcessingStage1"][Effect].EffectTrigger(self, Data)
                        OriginalData, FinalData, Results = Data["OriginalData"], Data["FinalData"], Data["Results"]
                    if Effect in Globals.BattleInfo["Relics"]:
                        Data = {"Effect":Effect, "OriginalData":OriginalData, "FinalData":FinalData, "Results":Results, "Stage":1}
                        Data = Globals.BattleInfo["RelicsDict"][Effect]["Reference"].EffectTrigger(self, Data)
                        OriginalData, FinalData, Results = Data["OriginalData"], Data["FinalData"], Data["Results"]

            # SENDS THE DATA TO BE PROCESSED TO THE EnmyFunc
            Damage = FinalData["Damage"]
            if Damage != 0:
                DamageTaken, ShieldDamage, OriginalData, FinalData, Results = Globals.BattleObjects[Type][Target]["Object"].DamageRecieved(Damage, OriginalData, FinalData, Results)
                Results["DamageDealt"] += DamageTaken
                Results["ShieldDamage"] += ShieldDamage

            Healing = FinalData["Healing"]
            if Healing != 0:
                HealingTaken, OriginalData, FinalData, Results = Globals.BattleObjects[Type][Target]["Object"].HealingRecieved(Healing, OriginalData, FinalData, Results)
                Results["HealingDealt"] += HealingTaken


            MentalDamage = FinalData["MentalDamage"]
            if MentalDamage != 0:
                MentalDamageTaken, OriginalData, FinalData, Results = Globals.BattleObjects[Type][Target]["Object"].MentalDamageRecieved(MentalDamage, OriginalData, FinalData, Results)
                Results["MentalDealt"] += MentalDamageTaken

            MentalHealing = FinalData["MentalHealing"]
            if MentalHealing != 0:
                MentalHealingTaken, OriginalData, FinalData, Results = Globals.BattleObjects[Type][Target]["Object"].MentalHealingRecieved(MentalHealing, OriginalData, FinalData, Results)
                Results["MentalHealingDealt"] += MentalHealingTaken


            Shield = FinalData["Shield"]
            if Shield != 0:
                ShieldTaken, OriginalData, FinalData, Results = Globals.BattleObjects[Type][Target]["Object"].ShieldRecieved(Shield, OriginalData, FinalData, Results)
                Results["ShieldApplied"] += ShieldTaken

            ShieldDamage = FinalData["ShieldDamage"]
            if ShieldDamage != 0:
                ShieldTaken, OriginalData, FinalData, Results = Globals.BattleObjects[Type][Target]["Object"].ShieldDamageRecieved(ShieldDamage, OriginalData, FinalData, Results)
                Results["ShieldDamage"] += ShieldTaken


            Effects = FinalData["Effects"]
            if Effects != []:
                EffectsApplied, OriginalData, FinalData, Results = Globals.BattleObjects[Type][Target]["Object"].EffectRecieved(Effects, OriginalData, FinalData, Results)
                for Effect in EffectsApplied:
                    if Effect in list(Results["EffectsApplied"].keys()):
                        Results["EffectsApplied"][Effect]["Level"] += Effects[Effect]["Level"]
                    else:
                        Results["EffectsApplied"][Effect] = Effects[Effect]

            # PINGS EVERYONE FOR THE ProcessingStage1
            if FinalData["Flags"]["EffectsTrigger"] == 1:
                for Effect in Globals.BattleInfo["EffectStages"]["ProcessingStage2"]:
                    if Effect in Globals.BattleObjects[Type][Target]["Object"].Effects:
                        Data = {"Effect":Effect, "OriginalData":OriginalData, "FinalData":FinalData, "Results":Results, "Stage":2, "Who":"Target"}
                        Data = Globals.BattleInfo["EffectStages"]["ProcessingStage2"][Effect].EffectTrigger(self, Data)
                        OriginalData, FinalData, Results = Data["OriginalData"], Data["FinalData"], Data["Results"]
                    if Effect in Globals.BattleObjects[ParentType][Parent]["Object"].Effects:
                        Data = {"Effect":Effect, "OriginalData":OriginalData, "FinalData":FinalData, "Results":Results, "Stage":2, "Who":"Caster"}
                        Data = Globals.BattleInfo["EffectStages"]["ProcessingStage2"][Effect].EffectTrigger(self, Data)
                        OriginalData, FinalData, Results = Data["OriginalData"], Data["FinalData"], Data["Results"]
                    if Effect in Globals.BattleInfo["EffectStages"]["UniversalEffects"]:
                        Data = {"Effect":Effect, "OriginalData":OriginalData, "FinalData":FinalData, "Results":Results, "Stage":2, "Who":"Universal"}
                        Data = Globals.BattleInfo["EffectStages"]["ProcessingStage2"][Effect].EffectTrigger(self, Data)
                        OriginalData, FinalData, Results = Data["OriginalData"], Data["FinalData"], Data["Results"]

            # SENDS THE DATA TO BE PROCESSED AT AttackConfirmed ON THE DeckFunc
            if FinalData["Flags"]["Confirmation"] == 1:
                if FinalData["Type"] == "Attack":
                    Reference = FinalData["Source"]
                    OriginalData, FinalData, Results = Reference.AttackConfirmed(OriginalData, FinalData, Results)
                elif FinalData["Type"] == "Effect":
                    Reference = FinalData["Source"]
                    OriginalData, FinalData, Results = Reference.EffectConfirmed(OriginalData, FinalData, Results)

            # PINGS EVERYONE FOR THE ProcessingStage3
            if FinalData["Flags"]["EffectsTrigger"] == 1:
                for Effect in Globals.BattleInfo["EffectStages"]["ProcessingStage3"]:
                    if Effect in Globals.BattleObjects[Type][Target]["Object"].Effects:
                        Data = {"Effect":Effect, "OriginalData":OriginalData, "FinalData":FinalData, "Results":Results, "Stage":3, "Who":"Target"}
                        Data = Globals.BattleInfo["EffectStages"]["ProcessingStage3"][Effect].EffectTrigger(self, Data)
                        OriginalData, FinalData, Results = Data["OriginalData"], Data["FinalData"], Data["Results"]
                    if Effect in Globals.BattleObjects[ParentType][Parent]["Object"].Effects:
                        Data = {"Effect":Effect, "OriginalData":OriginalData, "FinalData":FinalData, "Results":Results, "Stage":3, "Who":"Caster"}
                        Data = Globals.BattleInfo["EffectStages"]["ProcessingStage3"][Effect].EffectTrigger(self, Data)
                        OriginalData, FinalData, Results = Data["OriginalData"], Data["FinalData"], Data["Results"]
                    if Effect in Globals.BattleInfo["EffectStages"]["UniversalEffects"]:
                        Data = {"Effect":Effect, "OriginalData":OriginalData, "FinalData":FinalData, "Results":Results, "Stage":3, "Who":"Universal"}
                        Data = Globals.BattleInfo["EffectStages"]["ProcessingStage3"][Effect].EffectTrigger(self, Data)
                        OriginalData, FinalData, Results = Data["OriginalData"], Data["FinalData"], Data["Results"]


        except Exception as e:
            Log(3, "ERROR ATTACK CASTING,", e)
    def CastUniversalEffect(self, Data):
        # Data = {"Parent":Parent, "Effects":{"ID":"Endless","Level":1,"Data":{}}, "Flags":{"EffectsTrigger":1}}
        for Effect in Globals.BattleInfo["EffectStages"]["ProcessingUniversalEffects"]:
            Data2 = {"Effect":Effect, Data:"Data"}
            Data2 = Globals.BattleInfo["EffectStages"]["ProcessingUniversalEffects"][Effect].EffectTrigger(self, Effect, Data2)
            Data = Data2["Data"]

        for Effect in Data["Effects"]:
            EffectFull = Data["Effects"][Effect]
            # print(EffectFull)
            # print(Data["Effects"])
            if EffectFull["Level"] >= 1:
                if Effect in list(Globals.BattleInfo["EffectStages"]["UniversalEffects"].keys()):
                    Globals.BattleInfo["EffectStages"]["UniversalEffects"][Effect]["Level"] += EffectFull["Level"]
                else:
                    Globals.BattleInfo["EffectStages"]["UniversalEffects"][Effect] = EffectFull

    def Fade(self, widget):
        self.effect = QGraphicsOpacityEffect()
        widget.setGraphicsEffect(self.effect)

        try:
            index = max(list(Globals.Animations.keys()))
        except:
            index = 0
        index += 1
        Globals.Animations[index] = QtCore.QPropertyAnimation(self.effect, b"opacity")


        # self.animation = QtCore.QPropertyAnimation(self.effect, b"opacity")
        Globals.Animations[index].setDuration(1000)
        Globals.Animations[index].setStartValue(1)
        Globals.Animations[index].setEndValue(0)
        Globals.Animations[index].start()

        def AnimationOver(self, widget):
            widget.setParent(None)
        Globals.Animations[index].finished.connect(lambda: AnimationOver(self, widget))

    def shuffleCards(self):
        try:
            Discard = Globals.BattleInfo["Deck"]["DiscardDeck"].copy()
            Keys = list(Discard.keys())
            random.shuffle(Keys)
            temp = {}
            tempKeys = Keys.copy()
            for i in range(len(Keys)):
                Key = random.choice(tempKeys)
                tempKeys.remove(Key)
                temp[Key] = Discard[Key]
            temp2 = {**Globals.BattleInfo["Deck"]["DrawDeck"], **temp}
            Globals.BattleInfo["Deck"]["DrawDeck"] = temp2

            Globals.BattleInfo["Deck"]["DiscardDeck"] = {}
        except Exception as e:
            Log(3, "ERROR SHUFFLE,", e)
    def drawCard(self, MaxCards):
        if len(Globals.BattleInfo["Deck"]["DrawDeck"]) > 0 or len(Globals.BattleInfo["Deck"]["DiscardDeck"]) > 0:
            if Globals.BattleInfo["Deck"]["DrawDeck"] == {}:
                self.shuffleCards()
            if len(Globals.BattleInfo["Deck"]["CurrentHand"]) < MaxCards:   # TO DRAW A CARD
                try:
                    # GETS THE CARD
                    Key = list(Globals.BattleInfo["Deck"]["DrawDeck"].keys())[0]
                    Card = Globals.BattleInfo["Deck"]["DrawDeck"].pop(Key)

                    # FOR POSSIBLE STATUS EFFECTS
                    try:
                        Parent = Card[1]["Parent"]
                        if Parent in list(Globals.BattleObjects["Enemies"].keys()):
                            ParentType = "Enemies"
                        elif Parent in list(Globals.BattleObjects["Allies"].keys()):
                            ParentType = "Allies"
                    except:
                        ""
                    for Effect in Globals.BattleInfo["EffectStages"]["ProcessingStageDRCARD"]:
                        if Effect in Globals.BattleObjects[ParentType][Parent]["Object"].Effects:
                            Data = {"Effect":Effect, "Stage":"DRCARD", "Card":Card, "Parent":Parent}
                            Data = Globals.BattleInfo["EffectStages"]["ProcessingStageDRCARD"][Effect].EffectTrigger(self, Data)
                            Card = Data["Card"]
                        if Effect in Globals.BattleInfo["EffectStages"]["UniversalEffects"]:
                            Data = {"Effect":Effect, "Stage":"DRCARD", "Card":Card, "Parent": 'Universal'}
                            Data = Globals.BattleInfo["EffectStages"]["ProcessingStageDRCARD"][Effect].EffectTrigger(self, Data)
                            Card = Data["Card"]

                    if Card != []:  # PUTTING THE CARD ON THE CURRENT HAND
                        Globals.BattleInfo["Deck"]["CurrentHand"][Key] = Card
                except Exception as e:
                    print("FAILED DRAW", e)
            else:                                                           # TO DISCARD A CARD
                try:
                    # GETS THE CARD
                    Key = list(Globals.BattleInfo["Deck"]["DrawDeck"].keys())[0]
                    Card = Globals.BattleInfo["Deck"]["DrawDeck"][Key]
                    self.discardCard(Card, "DrawDeck")
                except Exception as e:
                    print("FAILED DRAWDISCARD", e)
    def discardCard(self, Card, Deck):
        try:
            ID = Card[1]["IDNumber"]
            if Card[0] != "Button":
                Card[0].Status = "Enabled"

            try:
                # FOR POSSIBLE STATUS EFFECTS
                try:
                    Parent = Attack["Parent"]
                    if Parent in list(Globals.BattleObjects["Enemies"].keys()):
                        ParentType = "Enemies"
                    elif Parent in list(Globals.BattleObjects["Allies"].keys()):
                        ParentType = "Allies"
                except:
                    ""
                for Effect in Globals.BattleInfo["EffectStages"]["ProcessingStageDCCARD"]:
                    if Effect in Globals.BattleObjects[ParentType][Parent]["Object"].Effects:
                        Data = {"Effect":Effect, "Stage":"DCCARD", "Card":Card, "Parent":Parent, "Deck":Deck}
                        Data = Globals.BattleInfo["EffectStages"]["ProcessingStageDCCARD"][Effect].EffectTrigger(self, Data)
                        Card, Deck = Data["Card"], Data["Deck"]
                    if Effect in Globals.BattleInfo["EffectStages"]["UniversalEffects"]:
                        Data = {"Effect":Effect, "Stage":"DCCARD", "Card":Card, "Parent": 'Universal', "Deck":Deck}
                        Data = Globals.BattleInfo["EffectStages"]["ProcessingStageDCCARD"][Effect].EffectTrigger(self, Data)
                        Card, Deck = Data["Card"], Data["Deck"]
            except Exception as e:
                Log(2, "ERROR DCCARD EFFECT", e)

            if Card != []:
                if Deck == "DrawDeck":
                    Globals.BattleInfo["Deck"]["DiscardDeck"][ID] = Globals.BattleInfo["Deck"]["DrawDeck"].pop(ID)
                    # Globals.BattleInfo["Deck"]["DiscardDeck"][ID] = Card
                    # ANIMATION FOR DRAW TO DISCARD
                elif Deck == "CurrentHand":
                    Globals.BattleInfo["Deck"]["DiscardDeck"][ID] = Globals.BattleInfo["Deck"]["CurrentHand"].pop(ID)
                    # Globals.BattleInfo["Deck"]["DiscardDeck"][ID] = Card
                    # ANIMATION FOR HAND TO DISCARD

        except Exception as e:
            Log(2, "ERROR DISCARD,", e, Deck, Card)
            ""
        # Globals.BattleInfo["Deck"]["DiscardDeck"][ID] = Card


    def SummonCard(self, Attack, Deck, Position, Parent):
        if Attack["IDNumber"] < 1:
            IDNumber = Globals.BattleInfo["IDCounter"]
            Globals.BattleInfo["IDCounter"] += 1
            Attack["IDNumber"] = IDNumber
            Attack["Parent"] = Parent
        else:
            IDNumber = Attack["IDNumber"]

        Button = CardButton(self.GUI, IDNumber, Attack)
        Card = (Button, Attack)
        # print(Attack)
        if Position == "Top":
            tempDict = {IDNumber:Attack}
            tempDict.update(Globals.BattleInfo["Deck"][Deck])
            Globals.BattleInfo["Deck"][Deck] = tempDict
        elif Position == "Bot":
            Globals.BattleInfo["Deck"][Deck][IDNumber] = Attack
        elif Position == "Random":
            listt = list(Globals.BattleInfo["Deck"][Deck].keys())
            Max = len(listt) - 1
            RN = random.randint(0,Max)
            tempDeck = {}
            Counter = 0
            for i in range(Max+2):
                if i == RN:
                    tempDeck[IDNumber] = Attack
                else:
                    tempID = listt[Counter]
                    tempDeck[tempID] = Globals.BattleInfo["Deck"][Deck][tempID]
                    Counter += 1
            Globals.BattleInfo["Deck"][Deck] = tempDeck
    def ExhaustCard(self, Attack, Button):
        try:
            # FINDS THE CARD ON THE DECK AND REMOVES IT
            ID = Button.ID
            Card = Globals.BattleInfo["Deck"]["CurrentHand"].pop(ID)

            # ADDS THE CARD TO THE EXHAUST PILE
            Globals.BattleInfo["Deck"]["ExhaustDeck"][ID] = Card

            # FOR POSSIBLE STATUS EFFECTS
            for Effect in Globals.BattleInfo["EffectStages"]["ProcessingStageEXCARD"]:
                if Effect in Globals.BattleInfo["EffectStages"]["UniversalEffects"]:
                    EffectFull = Globals.BattleInfo["EffectStages"]["UniversalEffects"][Effect]
                    Data = {"Effect":Effect, "Stage":"EXCARD", "Attack":Attack, "Button":Button, "EffectFull":EffectFull}
                    Data = Globals.BattleInfo["EffectStages"]["ProcessingStageEXCARD"][Effect].EffectTrigger(self, Data)
                    Attack, Button = Data["Attack"], Data["Button"]

            # EXHAUST ANIMATION
            # TODO
        except:
            ""

    def CreateSR(self, SRList):
        try:
            # TO HANDLE EFFECTS
            for AllyID in Globals.BattleObjects["Allies"]:
                Parent = AllyID
                try:
                    if Parent in list(Globals.BattleObjects["Enemies"].keys()):
                        ParentType = "Enemies"
                    elif Parent in list(Globals.BattleObjects["Allies"].keys()):
                        ParentType = "Allies"
                except:
                    ""
                for Effect in Globals.BattleInfo["EffectStages"]["ProcessingStageCRSR"]:
                    if Effect in Globals.BattleObjects[ParentType][Parent]["Object"].Effects:
                        Data = {"Effect":Effect, "Stage":"CRSR", "SRList":SRList, "Parent":Parent, "Who":"Ally"}
                        Data = Globals.BattleInfo["EffectStages"]["ProcessingStageDRCARD"][Effect].EffectTrigger(self, Data)
                        SRList = Data["SRList"]
            for EnemyID in Globals.BattleObjects["Enemies"]:
                Parent = EnemyID
                try:
                    if Parent in list(Globals.BattleObjects["Enemies"].keys()):
                        ParentType = "Enemies"
                    elif Parent in list(Globals.BattleObjects["Allies"].keys()):
                        ParentType = "Allies"
                except:
                    ""
                for Effect in Globals.BattleInfo["EffectStages"]["ProcessingStageCRSR"]:
                    if Effect in Globals.BattleObjects[ParentType][Parent]["Object"].Effects:
                        Data = {"Effect":Effect, "Stage":"CRSR", "SRList":SRList, "Parent":Parent, "Who":"Enemy"}
                        Data = Globals.BattleInfo["EffectStages"]["ProcessingStageDRCARD"][Effect].EffectTrigger(self, Data)
                        SRList = Data["SRList"]
            for Effect in Globals.BattleInfo["EffectStages"]["ProcessingStageCRSR"]:
                if Effect in Globals.BattleInfo["EffectStages"]["UniversalEffects"]:
                    Data = {"Effect":Effect, "Stage":"CRSR", "SRList":SRList, "Parent":'Universal', "Who":"Universal"}
                    Data = Globals.BattleInfo["EffectStages"]["ProcessingStageDRCARD"][Effect].EffectTrigger(self, Data)
                    SRList = Data["SRList"]

            for Roll in SRList:
                # Roll = {'Upper': 7, 'Lower': 3, 'Bonus': 0, 'Minus': 0, 'Parent': '0', 'Status': 'Enabled'}
                if Roll["Status"] == "Enabled":
                    try:
                        IDList = {k for k in list(Globals.SkillRolls.keys())}
                        ID = max(IDList) + 1
                    except Exception as e:
                        ID = 0
                    RN = random.randint(Roll["Lower"], Roll["Upper"])
                    SkillObject = SRObject(0, RN, Roll["Lower"], Roll["Upper"], Roll["Bonus"], Roll["Minus"], 0, ID)
                    SkillObject.Update()
                    Globals.SkillRolls[ID] = SkillObject
        except Exception as e:
            Log(4, "ERROR CREATE SR", e)
    def ExhaustSR(self, SRList):
        for SRID in SRList:
            Globals.SkillRolls.pop(SRID)
            Globals.BattleInfo["SR"].remove(SRID)


class SRObject:
    def __init__(self, Total, Base, Lower, Upper, Bonus, Minus, Selected, ID):
        self.Total = Total
        self.Base = Base
        self.Lower = Lower
        self.Upper = Upper
        self.Bonus = Bonus
        self.Minus = Minus
        self.Selected = Selected
        self.Status = "Enabled"
        self.ID = ID

    def ObjectWidget(self):
        SRLabel = QLabel()

        TextTop = '''<html><head/><body>'''
        TextBody = ''

        # if self.State == "Used":
        # TextBody += f'''<span style=" font-size:20pt; font-weight:600; color:#8A8A8A;">'''
        # elif self.State == "Preset":
        #     TextBody += f'''<span style=" font-size:20pt; font-weight:600; color:#ffff7f;">'''
        # else:
        TextBody += f'''<span style=" font-size:20pt; font-weight:600; color:#ffff00;">'''

        if self.Selected == 1:
            SRLabel.setStyleSheet('''
            QLabel{
            color:rgb(255, 255, 0);
            border:2px solid black;
            border-color:rgb(80, 80, 120);
            background-color:rgb(23,23,23);
            }''')
        else:
            SRLabel.setStyleSheet('''
            QLabel{
            color:rgb(255, 255, 0);
            border:2px solid black;
            background-color:rgb(23,23,23);
            }''')

        TextBody += f'''{self.Total}'''
        TextBody += '''</span> '''
        TextBottom = '''</body></html>'''
        TextWhole = TextTop + TextBody + TextBottom
        SRLabel.setText(TextWhole)
        SRLabel.mouseReleaseEvent = lambda event: self.SRClick()

        return SRLabel

    def SRClick(self):
        if self.Selected == 1:
            if self.ID in Globals.BattleInfo["SR"]:
                Globals.BattleInfo["SR"].remove(self.ID)
            self.Selected = 0
        else:
            if self.ID not in Globals.BattleInfo["SR"]:
                Globals.BattleInfo["SR"].append(self.ID)
            self.Selected = 1
        Globals.Layouts["BattleMenu"].Refresh()

        # if self.ID in Globals.BattleInfo["SR"]:
        #     Globals.BattleInfo["SR"].remove(self.ID)
        #     self.Selected = 0
        # else:
        #     Globals.BattleInfo["SR"].append(self.ID)

    def Update(self):
        self.Total = self.Base + self.Bonus

class CardButton(QPushButton):
    def __init__(self, Data, ID, Attack):
        parent = Data
        super(CardButton, self).__init__(parent)
        self.ParentWidget = Data
        self.Attack = Attack
        self.ID = ID
        self.AttackReference = Attack["DeckReference"]
        self.Available = 1
        self.Status = "Enabled"

        self.released.connect(lambda: self.AttackReference.AttackTrigger([self, self.Attack]))
        self.setFont(QFont('Segoe UI', 14))
        self.setMinimumWidth(140)
        self.setMaximumWidth(140)
        self.setMinimumHeight(40)
        self.setMaximumHeight(40)
        Globals.Layouts["BattleMenu"].buttonsList.append(self)

        ID = self.ID
        # Globals.BattleInfo["Deck"]["CurrentHand"][ID] = [self, self.Attack]

    def Update(self):
        Text = self.AttackReference.getButtonText(self, self.Attack["AttackID"])
        self.setText(Text)

        self.AttackReference.checkStatus(self.Attack, self)

        if self.Available == 1 and self.Status == "Enabled":
            self.setEnabled(True)
            self.setCheckable(False)
            self.setChecked(False)
        else:
            self.setEnabled(False)
            self.setCheckable(True)
            self.setChecked(True)

    def enterEvent(self, event):
        try:
            Globals.BattleInfo["CurrentCard"] = self.Attack
            Globals.Layouts["BattleMenu"].CardUpdate()
        except Exception as e:
            print("FAILED", e)
        ""

    def leaveEvent(self, event):
        ""

    def mouseMoveEvent(self,event):
        ""

    # def __init__(self, ID, Attack):
    #     self.Attack = Attack
    #     self.ID = ID
    #     self.Status = "Available"
    #     self.AttackReference = Attack["Card"]["DeckReference"]
    #
    #     Text = self.AttackReference.getButtonText(Attack["Card"]["AttackID"])



##### SCENE

class Scene(QtWidgets.QGraphicsScene):
    def __init__(self, parent=None):
        super(Scene, self).__init__(parent)
        pixmap = QtGui.QPixmap(100, 100)
        pixmap.fill(QtCore.Qt.red)

        self.pixmap_item = self.addPixmap(pixmap)
        # random position
        self.pixmap_item.setPos(*random.sample(range(-100, 100), 2))
        self.pixmap_item.setPos(10, 2)


        pixmap2 = QtGui.QPixmap(100, 100)
        pixmap2.fill(QtCore.Qt.red)

        self.pixmap_item2 = self.addPixmap(pixmap2)
        # random position
        self.pixmap_item2.setPos(*random.sample(range(-500, 100), 2))
        self.pixmap_item2.setPos(300, 2)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            items = self.items(event.scenePos())
            if items != []:
                # CHECKS IF THE CLICK HAPPENED ON A NODE
                for item in items:
                    try:
                        if item.Coor != []:
                            Globals.Layouts["BattleScene"].nodeTrigger(item)
                    except:
                        ""
            else:   # IF NOTHING IS CLICKED THEN IT STARTS TEH DRAGGIN MODE
                Globals.Layouts["BattleScene"].window.draggingScreen = True
                Globals.Layouts["BattleScene"].window.currentPos = QCursor.pos()
                Globals.Layouts["BattleScene"].window.nextPos = QCursor.pos()
    def mouseReleaseEvent(self, event):
        items = self.items(event.scenePos())
        if items != []:
            ""
        Globals.Layouts["BattleScene"].window.draggingScreen = False
        self.updateMouse(event)
    def mouseMoveEvent(self, event):
        ### HANDLES THE CURSOS IMAGE
        self.updateMouse(event)

        ### Dragging
        try:
            if Globals.Layouts["BattleScene"].window.draggingScreen == True:
                Globals.Layouts["BattleScene"].window.nextPos = QCursor.pos()
                MovX = Globals.Layouts["BattleScene"].window.currentPos.x() - Globals.Layouts["BattleScene"].window.nextPos.x()
                MovY = Globals.Layouts["BattleScene"].window.currentPos.y() - Globals.Layouts["BattleScene"].window.nextPos.y()
                CurX = Globals.Layouts["BattleScene"].scene.sceneRect().x()
                CurY = Globals.Layouts["BattleScene"].scene.sceneRect().y()
                Globals.Layouts["BattleScene"].scene.setSceneRect(CurX + (MovX / Globals.Layouts["BattleScene"].window.transform().m11() ), CurY + (MovY / Globals.Layouts["BattleScene"].window.transform().m11() ),1,1)
                Globals.Layouts["BattleScene"].window.currentPos = QCursor.pos()
        except Exception as e:
            Log(2, "ERROR COMBAT SCENE DRAGGING", e)
    def wheelEvent(self, event):
        if event.delta() > 0:
            Globals.Layouts["BattleScene"].window.scale(1.1,1.1)
            if Globals.Layouts["BattleScene"].window.transform().m11() > 0.95 and Globals.Layouts["BattleScene"].window.transform().m11() < 1.05:
                Globals.Layouts["BattleScene"].window.resetTransform()
        else:
            Globals.Layouts["BattleScene"].window.scale(0.9,0.9)
            if Globals.Layouts["BattleScene"].window.transform().m11() > 0.95 and Globals.Layouts["BattleScene"].window.transform().m11() < 1.05:
                Globals.Layouts["BattleScene"].window.resetTransform()

    def updateMouse(self, event):
        try:
            if Globals.Layouts["BattleScene"].window.draggingScreen != True:
                items = self.items(event.scenePos())
                for item in items:
                    try:
                        if item.Coor != []:
                            Globals.Layouts["BattleScene"].window.setCursor(Qt.PointingHandCursor)
                            break
                    except:
                        ""
                else:
                    Globals.Layouts["BattleScene"].window.setCursor(Qt.ArrowCursor)
            else:
                Globals.Layouts["BattleScene"].window.setCursor(Qt.ClosedHandCursor)
        except Exception as e:
            Log(1, "ERROR COMBAT SCENE updateMouse", e)

class RectItem(QtWidgets.QGraphicsRectItem):
    def paint(self, painter, option, widget=None):
        super(RectItem, self).paint(painter, option, widget)
        painter.save()
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        painter.setBrush(QtCore.Qt.cyan)
        painter.restore()

class AllyClass:
    def __init__(self, ID, Stats):
        with open('NPCData.json', 'rb') as f:
            NPCfullData = json.load(f)
        NPCData = NPCfullData[ID]

        self.Name = NPCData["Name"]
        self.MaxHP = Stats["HP"] + 17
        self.HP = Stats["HP"]
        self.Shield = 60
        self.Mental = 150
        self.ID = ID
        self.Status = "Alive"
        self.Selected = 0
        self.Effects = {}
        self.CanBeTargeted = 1

        self.STR = Stats["STR"]
        self.DEX = Stats["DEX"]
        self.CHA = Stats["CHA"]

        self.SR = Stats["SR"]

    def __del__(self):
        print(f"")

    def Testa(self):
        print("Ohno")

    def DamageTaken(self, DMG):
        self.HP -= DMG
        if self.HP <= 0:
            self.Events("Unconcious")
        Globals.Layouts["BattleMenu"].refresh()

    def BaseData(self):
        BD = {"CR":0.5, "DL":1}
        return BD

    def ObjectWidget(self):
        TWidget = QWidget()
        # self.Enemy1.setGeometry(300,300,220,320)
        TWidget.setFixedSize(400,240)
        TWidget.setStyleSheet('''
        QWidget{
        border: 1px solid black;
        background-color:rgb(23, 23, 23);
        }
        ''')
        # TWidget.mouseReleaseEvent = lambda event: print(f'{self}      {Globals.Enemies["MainW"]}')
        # TWidget.mouseReleaseEvent = lambda event: Globals.Enemies["MainW"].wrking()
        TWidget.mouseReleaseEvent = lambda event: self.AllyClick()

        if self.CanBeTargeted != 0:
            if self.Selected == 1:
                TWidget.setStyleSheet('''
                QWidget{
                border: 1px solid black;
                background-color:rgb(23, 23, 23);
                }
                .QWidget
                {
                border: 1px solid black;
                border-color:rgb(160,160,50)
                }''')
            else:
                TWidget.setStyleSheet('''
                QWidget{
                border: 1px solid black;
                background-color:rgb(23, 23, 23);
                }
                .QWidget
                {
                border: 1px solid black;
                border-color:rgb(23,23,23)
                }
                ''')
        else:
            TWidget.setStyleSheet('''
            QWidget{
            border: 1px solid black;
            background-color:rgb(23, 23, 23);
            }
            .QWidget
            {
            border: 3px solid black;
            border-color:rgb(80,35,35)
            }
            ''')

        EnemyName = QPushButton(self.Name, TWidget, clicked = lambda: print("Name"))
        EnemyName.setFont(QFont('Segoe UI', 12))
        EnemyName.setGeometry(110,5,280,30)
        EnemyName.setStyleSheet('''
        QPushButton{
        border: 1px solid black;
        background : rgb(35, 35, 35);
        color:rgb(255, 255, 255)
        }
        ''')

        EnemyPortrait = QLabel(TWidget)
        EnemyPortrait.setGeometry(5, 5, 100, 100)

        labelHP = QLabel(TWidget)
        labelHP.setGeometry(110,40,90,30)
        labelHP.setText(f'''<p><span style=" font-weight:600; color:#ff0000;">HP: {self.HP}</span></p> ''')
        labelHP.setFont(QFont('Segoe UI', 10))
        labelHP.setStyleSheet('''
        QLabel{
            color:red;
            background-color:rgb(35,35,35);
            }
        ''')
        labelSHP1 = QLabel(TWidget)
        labelSHP1.setGeometry(110,77,18,25)
        labelSHP1.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')
        labelSHP2 = QLabel(TWidget)
        labelSHP2.setGeometry(128,77,18,25)
        labelSHP2.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')
        labelSHP3 = QLabel(TWidget)
        labelSHP3.setGeometry(146,77,18,25)
        labelSHP3.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')
        labelSHP4 = QLabel(TWidget)
        labelSHP4.setGeometry(164,77,18,25)
        labelSHP4.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')
        labelSHP5 = QLabel(TWidget)
        labelSHP5.setGeometry(182,77,18,25)
        labelSHP5.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')


        labelSH = QLabel(TWidget)
        labelSH.setGeometry(205,40,90,30)
        labelSH.setText(f'''<p><span style=" font-weight:600;">SH: {self.Shield}</span></p> ''')
        labelSH.setFont(QFont('Segoe UI', 10))
        labelSH.setStyleSheet('''
        QLabel{
            color:rgb(150,150,150);
            background-color:rgb(35,35,35);
            }
        ''')
        labelSSH1 = QLabel(TWidget)
        labelSSH1.setGeometry(205,77,18,25)
        labelSSH1.setStyleSheet('''QLabel{background-color:rgb(150,150,150) }''')
        labelSSH2 = QLabel(TWidget)
        labelSSH2.setGeometry(223,77,18,25)
        labelSSH2.setStyleSheet('''QLabel{background-color:rgb(150,150,150) }''')
        labelSSH3 = QLabel(TWidget)
        labelSSH3.setGeometry(241,77,18,25)
        labelSSH3.setStyleSheet('''QLabel{background-color:rgb(150,150,150) }''')
        labelSSH4 = QLabel(TWidget)
        labelSSH4.setGeometry(259,77,18,25)
        labelSSH4.setStyleSheet('''QLabel{background-color:rgb(150,150,150) }''')
        labelSSH5 = QLabel(TWidget)
        labelSSH5.setGeometry(277,77,18,25)
        labelSSH5.setStyleSheet('''QLabel{background-color:rgb(150,150,150) }''')


        labelMT = QLabel(TWidget)
        labelMT.setGeometry(300,40,90,30)
        labelMT.setText(f'''<p><span style=" font-weight:600;">MT: {self.Mental}</span></p> ''')
        labelMT.setFont(QFont('Segoe UI', 10))
        labelMT.setStyleSheet('''
        QLabel{
            color:rgb(214, 0, 255);
            background-color:rgb(35,35,35);
            }
        ''')
        labelSMT1 = QLabel(TWidget)
        labelSMT1.setGeometry(300,77,18,25)
        labelSMT1.setStyleSheet('''QLabel{background-color:rgb(214, 0, 255) }''')
        labelSMT2 = QLabel(TWidget)
        labelSMT2.setGeometry(318,77,18,25)
        labelSMT2.setStyleSheet('''QLabel{background-color:rgb(214, 0, 255) }''')
        labelSMT3 = QLabel(TWidget)
        labelSMT3.setGeometry(336,77,18,25)
        labelSMT3.setStyleSheet('''QLabel{background-color:rgb(214, 0, 255) }''')
        labelSMT4 = QLabel(TWidget)
        labelSMT4.setGeometry(354,77,18,25)
        labelSMT4.setStyleSheet('''QLabel{background-color:rgb(214, 0, 255) }''')
        labelSMT5 = QLabel(TWidget)
        labelSMT5.setGeometry(372,77,18,25)
        labelSMT5.setStyleSheet('''QLabel{background-color:rgb(214, 0, 255) }''')


        labelActions = QLabel(TWidget)
        labelActions.setGeometry(5,110,390,75)
        labelActions.setText('''<html><head/><body>Quick Attack:<br/><span style=" font-weight:600; color:#00ff7f;">Quick.</span> 5 x 2 to Chraum<br/><span style=" font-weight:600; color:#1e74ff;">2nd Line</span><br/><span style=" font-weight:600; color:#1e74ff;">3rd Line</span></body></html> ''')
        labelActions.setFont(QFont('Segoe UI', 9))
        labelActions.setAlignment(Qt.AlignLeft)
        labelActions.setAlignment(Qt.AlignTop)
        labelActions.setStyleSheet('''
        QLabel{
            background-color:rgb(23,23,23);
            }
        ''')

        labelStatus = QLabel(TWidget)
        labelStatus.setGeometry(5,190,390,40)
        labelStatus.setAlignment(Qt.AlignLeft)
        labelStatus.setStyleSheet('''QLabel{background-color:rgb(214, 0, 255) }''')

        self.scrollEF = QScrollArea(TWidget)
        self.scrollEF.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollEF.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollEF.setGeometry(5,190,390,40)
        self.scrollEF.setStyleSheet('''
        QScrollArea{
        background-color:rgb(23, 23, 23);
        border: 1px solid black;
        border-right: none;
        border-left: none;
        ''')

        ### Draws the allies form on the left
        try:
            self.myformEF = QHBoxLayout()
            isEmpty = 1
            for Effect in self.Effects:
                self.Effects[Effect]["ID"]
                IconWidget = Globals.BattleInfo["EffectsDict"][self.Effects[Effect]["ID"]].getIcon(Effect, self)
                IconWidget.setFixedSize(40, 40)
                self.myformEF.addWidget(IconWidget)
                isEmpty = 0
            self.myformEF.setContentsMargins(0, 0, 0, 0)
            mygroupboxEF = QGroupBox()
            if isEmpty == 0:
                mygroupboxEF.setLayout(self.myformEF)
            self.scrollEF.setWidget(mygroupboxEF)
        except Exception as e:
            Log(2, "ERROR AllyObject EFFECT ICON", self, e)


        return TWidget

    def AllyClick(self):
        try:
            if self.Selected == 1:
                if self.ID in list(Globals.BattleInfo["Allies"].keys()):
                    Globals.BattleInfo["Allies"].pop(self.ID)
                self.Selected = 0
            else:
                if self.CanBeTargeted != 0:
                    if self.ID not in list(Globals.BattleInfo["Allies"].keys()):
                        Index = list(Globals.BattleObjects["Allies"].keys()).index(self.ID)
                        Globals.BattleInfo["Allies"][self.ID] = Index
                    self.Selected = 1
            Globals.Layouts["BattleMenu"].Refresh()
        except Exception as e:
            Log(3, "ERROR AllyObject CLICK", self, e)
            ""

    def Events(self, EventID):
        if EventID == "Unconcious":
            self.Status = "Unconcious"
        # if ID == "Targeting":
        #     self.HP -= 10
        #     if self.HP > 0:
        #         # print("You'll never get me")
        #         ""
        #     else:
        #         # print("I've been gotten")
        #         ""
        #         self.Status = "Dead"
        #     Globals.Layouts["BattleMenu"].refresh()
        # self


    def DamageRecieved(self, Damage, OriginalData, FinalData, Results):
        OrigianlHP = self.HP
        OriginalShield = self.Shield
        Shield = self.Shield
        if Shield != 0:
            if Shield >= Damage:
                Shield -= Damage
                self.Shield -= Damage
            else:
                Damage -= Shield
                self.Shield = 0

                self.HP -= Damage
        else:
            self.HP -= Damage

        if self.HP <= 0:
            self.Defeated()

        DamageTaken = OrigianlHP - self.HP
        ShieldDamage = OriginalShield - self.Shield
        return DamageTaken, ShieldDamage, OriginalData, FinalData, Results

    def Defeated(self):
        self.Status = "Defeated"
        self.HP = 0
        if self.Selected == 1:
            if self.ID in list(Globals.BattleInfo["Allies"].keys()):
                Globals.BattleInfo["Allies"].pop(self.ID)
            self.Selected = 0

    def HealingRecieved(self, Healing, OriginalData, FinalData, Results):
        self.HP += Healing
        HealingTaken = Healing
        return HealingTaken, OriginalData, FinalData, Results


    def MentalDamageRecieved(self, MentalDamage, OriginalData, FinalData, Results):
        OrigianlMental = self.Mental
        self.Mental -= MentalDamage
        if self.Mental < 0:
            self.Mental = 0

        MentalDamageTaken = OrigianlMental - self.Mental
        return MentalDamageTaken, OriginalData, FinalData, Results

    def MentalHealingRecieved(self, MentalHealing, OriginalData, FinalData, Results):
        OrigianlMental = self.Mental
        self.Mental += MentalHealing

        MentalDamageTaken = self.Mental - OrigianlMental
        return MentalHealingTaken, OriginalData, FinalData, Results


    def ShieldDamageRecieved(self, ShieldDamage, OriginalData, FinalData, Results):
        OrigianlShield = self.Shield
        self.Shield -= ShieldDamage
        if self.Shield < 0:
            self.Shield = 0

        ShieldDamageTaken = OrigianlShield - self.Shield
        return ShieldDamageTaken, OriginalData, FinalData, Results

    def ShieldRecieved(self, Shield, OriginalData, FinalData, Results):
        OrigianlShield = self.Shield
        self.Shield += Shield

        ShieldTaken = self.Shield - OrigianlShield
        return ShieldTaken, OriginalData, FinalData, Results


    def EffectRecieved(self, Effects, OriginalData, FinalData, Results):
        for Effect in Effects:
            if Effect in list(self.Effects.keys()):
                self.Effects[Effect]["Level"] += Effects[Effect]["Level"]
            else:
                self.Effects[Effect] = Effects[Effect]
        #     EffectName = Effect[0]
        # self.Effects = [*self.Effects, *Effects]
        EffectsApplied = Effects
        return EffectsApplied, OriginalData, FinalData, Results



class UiLayoutBattleScene(QWidget):
    def __init__(self):
        Globals.Layouts["BattleScene"] = self
        Globals.LayoutsData["BattleScene"] = {"Initialized":0, "Gold":0,}

    def UI(self):
        MainWindow = Globals.Layouts["MainF"]
        self.GUI = QWidget(MainWindow)
        # mainwindow.setWindowIcon(QtGui.QIcon('PhotoIcon.png'))
        self.GUI.setStyleSheet('''
        QWidget{
    	background-color:rgb(35, 35, 35);
        }
        QPushButton{
        	color:rgb(255, 255, 255)
        }
        QPushButton:hover{
        	color:rgb(255, 255, 0)
        }
        QLabel{
         border: 1px solid black;
         background : rgb(23, 23, 23);
         color:rgb(255, 255, 255)
        }
        QLineEdit{
        color:rgb(255, 255, 255)
        }
		QWidget{
    	background-color:rgb(35, 35, 35);
        border-color:rgb(200,200,200)
        }
        QPushButton{
        	color:rgb(255, 255, 255)
        }
        QPushButton:hover{
        	color:rgb(255, 255, 0)
        }
        QLabel{
         border: 1px solid black;
         background : rgb(35, 35, 35);
         color:rgb(255, 255, 255)
        }
        QLineEdit{
		border: 1px solid black;
        color:rgb(255, 255, 255)
        }
        QGroupBox{
        border: 1px solid black;
        background-color:rgb(35, 35, 35);
        }
        QScrollArea{
        border: 1px solid black;
        background-color:rgb(23, 23, 23);
        }
         ''')
        MainWindow.setCentralWidget(self.GUI)
        MainWindow.resize(1600, 1024)

        self.scene = Scene(self.GUI)
        self.scene.setSceneRect(1, 1, 1, 1)

        self.labelCommands = QLabel(self.GUI)
        self.labelCommands.setFont(QFont('Segoe UI', 14))
        self.labelCommands.setGeometry(10,970,1580,49)
        self.labelCommands.setStyleSheet('''
        QLabel{
        background-color:rgb(23, 23, 23);
        border: 1px solid black ;
        }''')


        self.buttonBack = QPushButton('Back To Menu', self.GUI, clicked = lambda: MainWindow.gotoLayout("MainMenu", "mainMenuUI"))
        self.buttonBack.setFont(QFont('Segoe UI', 14))
        self.buttonBack.setGeometry(50,975,140,40)


        self.window = QtWidgets.QGraphicsView(self.scene)
        self.window.setMouseTracking(True)
        self.hbox = QHBoxLayout()
        self.hbox.addWidget(self.window)

        self.layoutWidget = QWidget(self.GUI)
        self.layoutWidget.setLayout(self.hbox);
        self.layoutWidget.setGeometry(0,0,1600,970);



        Polygon = QPolygonF( [ QtCore.QPointF(10, 60),QtCore.QPointF(270, 40),QtCore.QPointF(400, 200),QtCore.QPointF(120, 150), ] )
        Pen = QPen(Qt.darkGreen, 10, Qt.SolidLine)
        Brush = QBrush(Qt.red)
        Object = self.scene.addPolygon(Polygon, Pen, Brush )

        self.window.draggingScreen = False
        # Globals.Layouts["BattleScene"] = self


        self.window.setAlignment(Qt.AlignBottom | Qt.AlignLeft)

    def drawNode(self, pen, brush, coordinates):
        CoordinateX = coordinates[0]
        CoordinateY = coordinates[1]

        MapData = Globals.MapData
        Map = Globals.Map
        Layer = coordinates[1]
        Node = coordinates[0]

        kind = "Separated"
        if kind == "Flat":
            Size = 150

            Width = Size * 2
            Height = (Size**2 - (Size/2)**2)**(1/2) * 2

            # For separated grid
            # OriginX = 50 + (CoordinateX * 400) + random.randint(100,100)
            # OriginY = 50 + (CoordinateY * 400) + random.randint(0,100)

            # For conjoined grid
            OriginX = 50 + (CoordinateX * (Width - Width/4))
            OriginY = 50 + (CoordinateY * Height)
            if CoordinateX % 2 == 0:
                OriginY += Height / 2


            Points = []

            x = OriginX
            y = OriginY * -1
            point = [x, y]
            Points.append(point)

            x = OriginX + (Width / 4) * 2
            y = OriginY * -1
            point = [x, y]
            Points.append(point)

            x = (OriginX + (Width / 4) * 3)
            y = (OriginY + Height/2) * -1
            point = [x, y]
            Points.append(point)

            x = OriginX + (Width / 4) * 2
            y = (OriginY + Height) * -1
            point = [x, y]
            Points.append(point)

            x = OriginX
            y = (OriginY + Height) * -1
            point = [x, y]
            Points.append(point)

            x = (OriginX - (Width / 4))
            y = (OriginY + Height/2) * -1
            point = [x, y]
            Points.append(point)

            x = QPolygonF([QtCore.QPoint(Points[0][0],Points[0][1]), QtCore.QPoint(Points[1][0],Points[1][1]), QtCore.QPoint(Points[2][0],Points[2][1]), QtCore.QPoint(Points[3][0],Points[3][1]), QtCore.QPoint(Points[4][0],Points[4][1]), QtCore.QPoint(Points[5][0],Points[5][1])])
            y = self.scene.addPolygon(x)
            y.setPen(pen)
            y.setBrush(brush)
        elif kind == "Point":
            Size = 150

            Width = (Size - math.sqrt(Size/2)) * 2
            Height = Size * 2

            # For separated grid
            # OriginX = 50 + (CoordinateX * 400) + random.randint(100,100)
            # OriginY = 50 + (CoordinateY * 400) + random.randint(0,100)

            # For conjoined grid
            OriginX = 50 + (CoordinateX * Width)
            OriginY = 50 + (CoordinateY * (Height-Height / 4))
            if CoordinateY % 2 == 0:
                OriginX += Width / 2

            Points = []

            x = OriginX
            y = OriginY * -1
            point = [x, y]
            Points.append(point)

            x = OriginX + (Width/2)
            y = (OriginY - (Height/4)) * -1
            point = [x, y]
            Points.append(point)

            x = OriginX + (Width/2)
            y = (OriginY - (Height/4 * 3)) * -1
            point = [x, y]
            Points.append(point)

            x = OriginX
            y = (OriginY - (Height)) * -1
            point = [x, y]
            Points.append(point)

            x = OriginX - (Width/2)
            y = (OriginY - (Height/4 * 3)) * -1
            point = [x, y]
            Points.append(point)

            x = OriginX - (Width/2)
            y = (OriginY - (Height/4)) * -1
            point = [x, y]
            Points.append(point)


            # x = QPolygonF([QtCore.QPoint(Points[0][0],Points[0][1]), QtCore.QPoint(Points[1][0],Points[1][1]), QtCore.QPoint(Points[2][0],Points[2][1]), QtCore.QPoint(Points[3][0],Points[3][1]), QtCore.QPoint(Points[4][0],Points[4][1]), QtCore.QPoint(Points[5][0],Points[5][1])])
            # y = self.scene.addPolygon(x)
            # y.setPen(pen)
            # y.setBrush(brush)
            # print(Points)
            for i in range(len(Points)):
                for j in range(len(Points[i])):
                    Points[i][j] = int(Points[i][j])
            # X = QPolygonF([ QtCore.QPoint(50,75), QtCore.QPoint(100,125) ])
            # print(Points)

            QPolygon = QPolygonF([QtCore.QPoint(Points[0][0],Points[0][1]), QtCore.QPoint(Points[1][0],Points[1][1]), QtCore.QPoint(Points[2][0],Points[2][1]), QtCore.QPoint(Points[3][0],Points[3][1]), QtCore.QPoint(Points[4][0],Points[4][1]), QtCore.QPoint(Points[5][0],Points[5][1])])
            # print(6)

        elif kind == "Separated":

            Size = 150
            Width = (Size - math.sqrt(Size/2)) * 2
            Height = Size * 2

            OriginX = 50 + (CoordinateX * 2 * Width)
            OriginY = (50 + (CoordinateY * 2 * (Height-Height / 4))) * -1
            if Map[Layer][Node]["Status"] == "Available" or Map[Layer][Node]["Status"] == "Current":
                Size = 200
                Width = (Size - math.sqrt(Size/2)) * 2
                Height = Size * 2
            elif Map[Layer][Node]["Status"] == "Unavailable":
                Size = 150
                Width = (Size - math.sqrt(Size/2)) * 2
                Height = Size * 2


            Points = []

            x = OriginX
            y = OriginY - (Height/2)
            point = [x, y]
            Points.append(point)

            x = OriginX + (Width/2)
            y = OriginY - (Height/4)
            point = [x, y]
            Points.append(point)

            x = OriginX + (Width/2)
            y = OriginY + (Height/4)
            point = [x, y]
            Points.append(point)

            x = OriginX
            y = OriginY + (Height/2)
            point = [x, y]
            Points.append(point)

            x = OriginX - (Width/2)
            y = OriginY + (Height/4)
            point = [x, y]
            Points.append(point)

            x = OriginX - (Width/2)
            y = OriginY - (Height/4)
            point = [x, y]
            Points.append(point)

            for i in range(len(Points)):
                for j in range(len(Points[i])):
                    Points[i][j] = int(Points[i][j])

            QPolygon = QPolygonF([QtCore.QPoint(Points[0][0],Points[0][1]), QtCore.QPoint(Points[1][0],Points[1][1]), QtCore.QPoint(Points[2][0],Points[2][1]), QtCore.QPoint(Points[3][0],Points[3][1]), QtCore.QPoint(Points[4][0],Points[4][1]), QtCore.QPoint(Points[5][0],Points[5][1])])


        return QPolygon

    def Intiliaze(self):
        try:
            ### PULLS FROM THE CURRENT PARTY MEMEBERS TO GENERATE THE WHOLE DECK AS WELL AS THE DRAWING DECK
            # with open('NPCData.json', 'rb') as f:
            #     NPCfullData = json.load(f)
            # with open('tempData.json', 'rb') as f:
            #     tempData = json.load(f)
            NPCfullData = Globals.SoLNPCData
            tempData = Globals.SoLTempData

            PCID = tempData["PlayerID"]

            Followers = NPCfullData[PCID]["Actions"]["HasFollowing"]
            Followers.append(PCID)
            PartyMembers = 1
            MaxParty = 3
            FullDeck = []
            FullDrawDeck = []
            Globals.CombatDecks = {"AvailableCardsWhole":{}, "FullDeckWhole":{}, "CurrentHandWhole":{}, "DrawDeckWhole":{}, "DiscardDeckWhole":{}, "ExhaustDeckWhole":{}, "CurseDeckWhole":{}}
            Globals.SR = []

            ### GENERATES THE PARTY AND IT'S OBJECTS
            PartyObjects = {}
            AvailableCards, FullDeck, CurrentHand, DrawDeck, DiscardDeck, ExhaustDeck, CurseDeck = [], [], [], [], [], [], []
            AvailableCardsWhole, FullDeckWhole, CurrentHandWhole, DrawDeckWhole, DiscardDeckWhole, ExhaustDeckWhole, CurseDeckWhole = {}, {}, {}, {}, {}, {}, {}
            lstWhole = [AvailableCardsWhole, FullDeckWhole, CurrentHandWhole, DrawDeckWhole, DiscardDeckWhole, ExhaustDeckWhole, CurseDeckWhole]
            SR = []
            lstID = []

            for NPCID in Followers:
                if PartyMembers < MaxParty:
                    PathFull = os.path.abspath(__file__)
                    NameLen = len(os.path.basename(__file__))
                    Path = PathFull[0:-NameLen]
                    # TRIES TO GET OBJECT AND DECK, IF NOT THEN SKIPS OVER TO THE NEXT NPC WITHOUT ADDING IT TO THE PARTY
                    try:

                        # GETS THE DECK OF THE NPC
                        try:
                            try:
                                Name = "TODO"
                                NPCPath = Path + f'''NPCData\\{Name}{NPCID}\\'''
                                FileName = f'''{Name}{NPCID}Functions'''
                                if FileName not in Globals.References:

                                    if NPCPath not in sys.path:
                                        sys.path.insert(0, NPCPath)
                                    NPCfunc = __import__(FileName)
                                    Globals.References[FileName] = NPCfunc
                                else:
                                    NPCfunc = Globals.References[FileName]
                                UseClass, AvailableCards, FullDeck, CurrentHandWhole, DrawDeck, DiscardDeck, ExhaustDeck, CurseDeck, SR = NPCfunc.getDeck(FullDeck, DrawDeck)
                            except Exception as e:
                                Log(1, "ERROR IMPORTING NPC CUSTOM DECK DATA", e, NPCID, FileName)
                                NPCfunc = ''
                                UseClass = True

                            if UseClass == True:
                                try:
                                    DeckName = ''
                                    DeckName = NPCfullData[NPCID]["CombatAbilities"]["DeckName"]
                                    if DeckName not in Globals.References:
                                        DeckPath = NPCfullData[NPCID]["CombatAbilities"]["DeckLocation"]
                                        if DeckPath not in sys.path:
                                            sys.path.insert(0, DeckPath)
                                        DeckReference = __import__(DeckName)
                                    else:
                                        DeckReference = Globals.References[DeckName]
                                    Globals.Decks[DeckName] = DeckReference
                                    AvailableCards, FullDeck, CurrentHandWhole, DrawDeck, DiscardDeck, ExhaustDeck, CurseDeck, SR = DeckReference.getDeck(AvailableCards, FullDeck, CurrentHandWhole, DrawDeck, DiscardDeck, ExhaustDeck, CurseDeck, SR, DeckReference)
                                except:
                                    Log(1, "ERROR IMPORTING NPC GENERIC DECK DATA", e, NPCID, DeckName)

                            lst = [AvailableCards, FullDeck, CurrentHand, DrawDeck, DiscardDeck, ExhaustDeck, CurseDeck]

                            DeckList = {"AvailableCards":AvailableCards, "FullDeck":FullDeck, "CurrentHand":CurrentHand, "DrawDeck":DrawDeck, "DiscardDeck":DiscardDeck, "ExhaustDeck":ExhaustDeck, "CurseDeck":CurseDeck}
                            DeckWhole = {"AvailableCards":{}, "FullDeck":{}, "CurrentHand":{}, "DrawDeck":{}, "DiscardDeck":{}, "ExhaustDeck":{}, "CurseDeck":{} }
                            for Deck in DeckList:
                                for Attack in DeckList[Deck]:
                                    Attack["Parent"] = NPCID
                                    IDCounter = Globals.BattleInfo["IDCounter"]
                                    Attack["IDNumber"] = IDCounter
                                    DeckWhole[Deck][IDCounter] = Attack

                                    if Deck != "AvailableCards":
                                        Deck2 = "FullDeck"
                                        DeckWhole[Deck2][IDCounter] = Attack

                                    Globals.BattleInfo["IDCounter"] += 1
                                    # print(Attack)
                            for SkillRoll in SR:
                                SkillRoll["Parent"] = NPCID
                                SkillRoll["Status"] = "Enabled"
                                Globals.SR.append(SkillRoll)

                        except Exception as e:
                            Log(1, "ERROR IMPORTING NPC DECK DATA", e, NPCID)
                        # GETS THE OBJECT OF THE NPC
                        try:
                            # PINGS FOR THE FUNCTION REFERENCE OR MAKES IT
                            ID = NPCID
                            Name = NPCfullData[ID]["Name"]
                            NPCPath = Path + f'''NPCData\\{Name}{ID}\\'''
                            FileName = f'''{Name}{ID}Functions'''
                            if FileName not in Globals.References:

                                if NPCPath not in sys.path:
                                    sys.path.insert(0, NPCPath)
                                NPCfunc = __import__(FileName)
                                Globals.References[FileName] = NPCfunc
                            else:
                                NPCfunc = Globals.References[FileName]

                            try:    # CHECKS FOR A CUSTOM OBJECT, OTHERWISE IT GENERATES A GENERIC ONE
                                NPCobject = NPCfunc.getCombatObject(self)
                            except:
                                NPCfunc = ''
                                raise
                        except: # IF NO CUSTOM OBJECT OR ANY OTEHR ERROR THEN IT TRIES TO GENERATE A GENERIC OBJECT
                            Stats = DeckReference.getStats(NPCID)
                            NPCObject = self.getGenericAllyObject(NPCID, Stats)
                            if NPCObject == "Failed":
                                raise

                        Globals.CombatDecks["AvailableCardsWhole"] = Globals.CombatDecks["AvailableCardsWhole"] | DeckWhole["AvailableCards"]
                        Globals.CombatDecks["FullDeckWhole"] = Globals.CombatDecks["FullDeckWhole"] | DeckWhole["FullDeck"]
                        Globals.CombatDecks["CurrentHandWhole"] = Globals.CombatDecks["CurrentHandWhole"] | DeckWhole["CurrentHand"]
                        Globals.CombatDecks["DrawDeckWhole"] = Globals.CombatDecks["DrawDeckWhole"] | DeckWhole["DrawDeck"]
                        Globals.CombatDecks["DiscardDeckWhole"] = Globals.CombatDecks["DiscardDeckWhole"] | DeckWhole["DiscardDeck"]
                        Globals.CombatDecks["ExhaustDeckWhole"] = Globals.CombatDecks["ExhaustDeckWhole"] | DeckWhole["ExhaustDeck"]
                        Globals.CombatDecks["CurseDeckWhole"] = Globals.CombatDecks["CurseDeckWhole"] | DeckWhole["CurseDeck"]




                        # TODO
                        Globals.PartyObjects[NPCID] = NPCObject

                        PartyMembers += 1
                    except Exception as e:
                        Log(1, "ERROR SETTING NPC COMBAT DATA", e)
                        ""
                    # print(Globals.PartyObjects)

            ### GENERATES THE MAP
            try:
                Globals.MapPath = []
                self.generateMap()
                self.checkAvailable(Globals.Map, Globals.MapData)
                self.getEvents()  # GETS EVENTS
                self.setEvents()
                # self.Refresh()
                self.setMap(Globals.Map, Globals.MapData)
                self.setLines(Globals.Map, Globals.MapData)

                # self.returnToMap()
            except Exception as e:
                Log(4, "ERROR GENERATING MAP", e, NPCID)


            ### PINGS THE FILES IN Combat/Effects TO START SETTING UP ALL THE EFFECTS
            try:
                PathFull = os.path.abspath(__file__)
                NameLen = len(os.path.basename(__file__))
                Path = PathFull[0:-NameLen]

                PathEffects = Path + "Combat\\Effects"
                if PathEffects not in sys.path:
                    sys.path.insert(0, PathEffects)

                FileList = os.listdir(PathEffects)
                for FileName in FileList:
                    if FileName.endswith(('.py')):
                        FileName = FileName[0:-3]

                        try:
                            FileReference = __import__(FileName)
                            if FileName not in list(Globals.References.keys()):
                                Globals.References[FileName] = FileReference
                                FileReference.GetEffects(self, FileReference)
                        except Exception as e:
                            Log(2, "ERROR IMPORTING EFFECT FILE", FileName, e)
            except Exception as e:
                Log(2, "ERROR IMPORTING EFFECTS,", e)


            ### PINGS THE FILES IN Combat/Relics TO START SETTING UP ALL THE RELICS
            try:
                PathFull = os.path.abspath(__file__)
                NameLen = len(os.path.basename(__file__))
                Path = PathFull[0:-NameLen]

                PathEffects = Path + "Combat\\Relics"
                if PathEffects not in sys.path:
                    sys.path.insert(0, PathEffects)

                FileList = os.listdir(PathEffects)
                for FileName in FileList:
                    if FileName.endswith(('.py')):
                        FileName = FileName[0:-3]

                        try:
                            FileReference = __import__(FileName)
                            if FileName not in list(Globals.References.keys()):
                                Globals.References[FileName] = FileReference
                                FileReference.GetRelics(self, FileReference)
                        except Exception as e:
                            Log(2, "ERROR IMPORTING RELIC FILE", FileName, e)
            except Exception as e:
                Log(2, "ERROR IMPORTING RELICS", e)


            Globals.LayoutsData["BattleScene"]["Initialized"] = 1
        except Exception as e:
            Log(4, "ERROR BATLLE SCENE INITIALIZE", e)


    def getGenericAllyObject(self, NPCID, Stats):
        try:
            Ally = AllyClass(NPCID, Stats)
            return Ally
            ""
        except:
            return "Failed"

    def nodeTrigger(self, Object):
        Layer = Object.Coor[0]
        Node = Object.Coor[1]
        try:
            if Globals.Map[Layer][Node]["Status"] == "Available" or Globals.Map[Layer][Node]["Status"] == "Current":
                if Globals.Map[Layer][Node]["Type"] == "Enemy":
                    if Globals.Map[Layer][Node]["Encounter"]["ID"] == "Generic":
                        try:
                            Initialized = Globals.LayoutsData["BattleMenu"]["Initialized"]
                        except:
                            Initialized = 0
                        if Initialized == 0:
                            # GETS ALLY OBJECTS
                            for Ally in Globals.PartyObjects:
                                Globals.BattleObjects["Allies"][Ally] = {"Object":Globals.PartyObjects[Ally], "Widget":''}

                            # GETS ENEMY OBJECTS
                            IDCounter = 0
                            for Enemy in Globals.Map[Layer][Node]["Encounter"]["Enemies"]:
                                EnemyID = Enemy["ID"]
                                Reference = Globals.References[Enemy["Origin"]]
                                ID = str(EnemyID) + str(IDCounter)
                                EnemyObject = Reference.getObject(self, EnemyID, ID, IDCounter)
                                Globals.BattleObjects["Enemies"][ID] = {"Object":EnemyObject, "Widget":''}
                                IDCounter += 1

                            Globals.LayoutsData["BattleMenu"]["Encounter"] = Globals.Map[Layer][Node]["Encounter"]
                            Globals.LayoutsData["BattleMenu"]["Coordinates"] = [Layer, Node]
                            # UiLayoutBattleMenu().Ui(Globals.Layouts["MainF"], Globals.Map[Layer][Node]["Encounter"], [Layer, Node])
                        Globals.Layouts["MainF"].gotoLayout("BattleMenu")

                        # self.LabelFront = QLabel(self.GUI)
                        # self.LabelFront.setFont(QFont('Segoe UI', 14))
                        # self.LabelFront.setGeometry(100,850,240,240)
                        # self.LabelFront.setStyleSheet('''
                        # QLabel{
                        # background-color:rgb(255, 23, 23);
                        # border: 1px solid black ;
                        # }''')
                        # self.LabelFront.raise_()
                        # self.LabelFront.show()

                        self.checkAvailable(Globals.Map, Globals.MapData)

                        if Globals.LayoutsData["BattleMenu"]["Initialized"] == 1:
                            Globals.Layouts["BattleMenu"].ReturnToLayout()
                        else:
                            Globals.Layouts["BattleMenu"].StartOfCombat()
                        # self.ResetMap()
                        self.Refresh()
                elif Globals.Map[Layer][Node]["Type"] == "Event":
                    Event = Globals.Map[Layer][Node]["Encounter"]
                    Globals.Map[Layer][Node]["Encounter"]["Origin"].EventTriggered(self, Event, [Layer,Node])
            else:
                print([Layer, Node])
        except Exception as e:
            Log(4, "ERROR NODE TRIGGER:", e, [Layer, Node])

    def ReturnToLayout(self):
        self.Refresh()
        Globals.Layouts["BattleScene"].setEvents()

    def Refresh(self):
        if Globals.LayoutsData["BattleScene"]["Initialized"] == 0:
            self.Intiliaze()
        self.checkAvailable(Globals.Map, Globals.MapData)
        self.ResetMap()

    def ResetMap(self):
        # DELETES THE PREVIOUS MAP
        MapData = Globals.MapData
        Map = Globals.Map

        for Layer in Map:
            for Node in Map[Layer]:
                Object = Map[Layer][Node]["Object"]
                Globals.Layouts["BattleScene"].scene.removeItem(Object)
                Pic = Map[Layer][Node]["ImagePixmap"]
                Globals.Layouts["BattleScene"].scene.removeItem(Pic)

        # SETS THE NEWMAP
        self.setMap(Map, MapData)

    def generateMap(self):
        MapData = {"Width":8, "Height":15, "InitialLanes":4, "BalanceLanes":3, "EliteFrequency":6, "TreasureFrequency":7, "CombatChance":0.4, "EventChance":0.5, "CR":1, "PlayerPath":[], "Initialized":1, "Enemies":[], "Encounters":{"Generic":[], "Custom":[]}, "EliteEnemies":[],"EliteEncounters":{"Generic":[], "Custom":[]},"BossEncounters":{"Generic":[], "Custom":[]}, "Events":[], "TreasureEvents":[]}
        Map = self.getMap(MapData)
        Map, MapData = self.getType(Map, MapData)

        Globals.Map = Map
        Globals.MapData = MapData

    def getMap(self, MapData):
        def addConnection(Start, End):
            Layer1 = Start[0]
            Node1 = Start[1]

            Layer2 = End[0]
            Node2 = End[1]

            NodeData = Map[Start[0]][Start[1]]


            if Node2 not in list(Map[Layer2].keys()):
                Data = {"Type":"", "Encounter":"", "Flags":{"Pathed":0},"Connections":{"Lower":[(Layer1,Node1)],"Upper":[]},"Polygon":"","Object":"", "Status":"Unavailable"}
                Map[Layer2][Node2] = Data
            else:
                ""
            if [Layer1,Node1] not in Map[Layer2][Node2]["Connections"]["Lower"]:
                # print("Lower")
                Map[Layer2][Node2]["Connections"]["Lower"].append([Layer1,Node1])

            if [Layer2,Node2] not in Map[Layer1][Node1]["Connections"]["Upper"]:
                # print("Upper")
                Map[Layer1][Node1]["Connections"]["Upper"].append([Layer2,Node2])

            Map[Layer1][Node1]["Flags"]["Pathed"] = 1

        Width = MapData["Width"]
        Height = MapData["Height"]
        InitialLanes = MapData["InitialLanes"]
        BalanceLanes = MapData["BalanceLanes"]
        Map = {}

        ### Initial Layer
        Map[0] = {}

        for i in range(InitialLanes):

            Data = {"Type":"", "Encounter":"", "Flags":{"Pathed":0},"Connections":{"Lower":[],"Upper":[]},"Polygon":"","Object":""}

            Counter = 0     # Counter to prevent the loop going infitnite
            while True:
                RN = random.randint(0,Width)

                if RN not in Map[0].keys():
                    Map[0][RN] = Data
                    break
                if Counter >= 15:
                    break
                Counter += 1


        Map[0] = {k: Map[0][k] for k in sorted(Map[0])}     # Sorts the initial layer of the map

        for Layer in range(Height-1):
            Map[Layer + 1] = {}
            Map[Layer] = {k: Map[Layer][k] for k in sorted(Map[Layer])}
            # First checks for merging or movement
            for Node in Map[Layer]:
                NodeData = Map[Layer][Node]
                if Map[Layer][Node]["Flags"]["Pathed"] == 0:

                    Stretch = len(Map[Layer]) - Width
                    if Stretch <= 1: Stretch = 1
                    Prob = 0.5 ** 1/(Stretch)        # The likelyhood of merging increases the more lanes are compared to the balance amount of nodes

                    if random.random() >= Prob:       # Attempts to merge if it isn't the last node and passes the probability
                        # Checks the previous node connections, the lower bound is the rightmost upper connection it has
                        NIndex = list(Map[Layer].keys()).index(Node)

                        LNode = list(Map[Layer].keys())[NIndex-1]
                        LNodeCon = Map[Layer][LNode]["Connections"]
                        try:
                            LB = LNodeCon["Upper"][-1][1]
                            LB = max(list(Map[Layer+1].keys()))
                        except:
                            LB = 0
                        # Checks if there is space for the UB to appear in front of the node to the right, otherwise the upper bond is the space previous to the right Node. If it doesn't exist then it is the width of the map.
                        try:
                            if list(Map[Layer].keys())[NIndex+1] + 1 <= Width - (len(Map[Layer].keys()) - NIndex) - 1:
                                UB = list(Map[Layer].keys())[NIndex+1]
                            else:
                                UB = (list(Map[Layer].keys())[NIndex+1]) - 1
                        except:
                            UB = Width
                        Dir = random.randint(LB,UB)


                        addConnection((Layer,Node), (Layer+1,Dir))

                    ### If the node hasn't merged then it calculates the path will take. Takes into consideration how much space is at the right to not choke the other nodes.
                    if Map[Layer][Node]["Flags"]["Pathed"] == 0:
                        PossibleDir = []

                        if (Node-1) not in Map[Layer+1] and Node-1 >= 0:
                            PossibleDir.append("Left")

                        if Node not in Map[Layer+1]:
                            PossibleDir.append("Center")

                        temp = list(Map[Layer].keys())
                        if (Node+1) not in Map[Layer+1] and Node+1 <= Width and (len(Map[Layer]) - temp.index(Node) - 1) < Width - Node:        # IF the node at the next layer on the right doesn't exist. If the node doesn't exceed the width of the map. And if the remaining amount of nodes are less than the space remaining on the right of the map
                            PossibleDir.append("Right")

                        try:
                            Dir = random.choice(PossibleDir)
                        except:
                            raise

                        if Dir == "Left":
                            addConnection((Layer,Node), (Layer+1,Node-1))
                        elif Dir == "Center":
                            addConnection((Layer,Node), (Layer+1,Node))
                        elif Dir == "Right":
                            addConnection((Layer,Node), (Layer+1,Node+1))
                        # Map[Layer][Node]["Flags"]["Pathed"] = 1

            # Then checks for possible splitting
            for Node in Map[Layer]:
                Compress = (BalanceLanes - len(Map[Layer])) + 1
                if Compress <= 0: Compress = 1

                Prob = 0.9 ** 1/(Compress)        # The likelyhood of merging increases the more lanes are compared to the balance amount of nodes

                # Calculates the possible range for splitting

                Index = list(Map[Layer].keys()).index(Node)
                try:
                    LB = list(Map[Layer].keys())[Index-1]
                except:
                    if Node != 0:
                        LB = 0
                    else:
                        LB = Node
                try:
                    UB = list(Map[Layer].keys())[Index+1]
                except:
                    if Node != Width:
                        UB = Width
                    else:
                        UB = Node
                    ""

                Range = []
                for i in range(UB - LB - 1):
                    Pos = LB + i + 1
                    if Pos != Node:
                        Range.append(Pos)

                if random.random() >= Prob and Range != []:
                    Dir = random.choice(Range)
                    addConnection((Layer,Node), (Layer+1,Dir))
            Map[Layer] = {k: Map[Layer][k] for k in sorted(Map[Layer])}     ### Sorts the map layer to prevent issues
        for Layer in Map:
            Map[Layer] = {k: Map[Layer][k] for k in sorted(Map[Layer])}

        return Map

    def getType(self, Map, MapData):
        def getEncounter(Layer,Node):

            Type = ""
            # lst = list(Map.keys()).index(2)
            if Layer == 0:  # Checks if it's the first room for a standard combat
                # print(Layer, "Enemy")
                Map[Layer][Node]["Type"] = "Enemy"
            elif Layer+1 not in list(Map.keys()):   # Checks if lastt layer to make a boss appear
                # print(Layer,"Boss")
                Map[Layer][Node]["Type"] = "Boss"
                ""
            elif list(Map.keys()).index(Layer) % MapData["EliteFrequency"] == 0 or list(Map.keys()).index(Layer) % MapData["TreasureFrequency"] == 0:     # Checks if the enemy is a set elite or treasure location
                if list(Map.keys()).index(Layer) % MapData["EliteFrequency"] == 0 and list(Map.keys()).index(Layer) % MapData["TreasureFrequency"] == 0:
                    RN = random.random()
                    # print("Both")
                    if RN >= 0.5:
                        # print(Layer,"SetElite")
                        Map[Layer][Node]["Type"] = "Elite"
                    else:
                        # print(Layer,"Treasure")
                        Map[Layer][Node]["Type"] = "Treasure"
                elif list(Map.keys()).index(Layer) % MapData["EliteFrequency"] == 0:
                    # print(Layer,"SetElite")
                    Map[Layer][Node]["Type"] = "Elite"
                else:
                    # print(Layer,"Treasure")
                    Map[Layer][Node]["Type"] = "Treasure"
            else:   # If none of the other conditions are true, then it rolls for a chance at a normal combat,
                EnemyChance = MapData["CombatChance"]
                EventChance = MapData["EventChance"]
                RN = random.random()
                if RN <= EnemyChance:
                    # print(Layer,"Enemy")
                    Map[Layer][Node]["Type"] = "Enemy"
                    # print(Map[Layer][Node])
                    # CR = MapData["CR"]
                    # Encounter = getEnemy(CR)
                    # return Encounter
                elif RN <= EnemyChance+EventChance:
                    # print(Layer,"Event")
                    Map[Layer][Node]["Type"] = "Event"
                else:
                    # print(Layer,"Elite")
                    Map[Layer][Node]["Type"] = "Elite"
                ""


            # return

        for Layer in Map:
            for Node in Map[Layer]:
                Encounter = getEncounter(Layer, Node)
        return Map, MapData

    def checkAvailable(self, Map, MapData):
        try:
            try:
                Coordinates = MapData["PlayerPath"][-1]
            except:
                ""
            for Layer in Map:
                for Node in Map[Layer]:
                    if MapData["PlayerPath"] == []:
                        if Layer == 0:
                            Globals.Map[Layer][Node]["Status"] = "Available"
                        else:
                            Globals.Map[Layer][Node]["Status"] = "Unavailable"
                    else:
                        if Map[Coordinates[0]][Coordinates[1]]["Status"] == "Current":
                            if Layer != Coordinates[0] or Node != Coordinates[1]:
                                Globals.Map[Layer][Node]["Status"] = "Unavailable"
                            else:
                                Globals.Map[Layer][Node]["Status"] = "Current"
                        else:
                            if MapData["PlayerPath"][-1] in Map[Layer][Node]["Connections"]["Lower"]:
                                Globals.Map[Layer][Node]["Status"] = "Available"
                            else:
                                Globals.Map[Layer][Node]["Status"] = "Unavailable"
        except Exception as e:
            Log(4, "ERROR CHECK AVAILABLE", e)
        ""

    def setMap(self, Map, MapData):
        Map = Globals.Map
        MapData = Globals.MapData

        pen = QPen(Qt.darkGreen)
        brush = QBrush(Qt.red)



        for Layer in Map:
            for Node in Map[Layer]:

                # GETS THE OBJECT FROM THE LAYER AND NODE COORDINATES
                coordinates = (Node,Layer)
                QPolygon = self.drawNode(pen, brush, coordinates)
                Map[Layer][Node]["Polygon"] = QPolygon

                # GENERATES AND SETS UP THE POLYGON OBJECT
                # try:
                Object = self.scene.addPolygon(QPolygon)
                # except Exception as e:
                #     print("type error: " + str(e))

                Object.Coor = [Layer, Node]
                # Object = self.scene.addPolygon(Polygon)

                if Globals.Map[Layer][Node]["Status"] == "Current":
                    pen = QPen(Qt.darkGreen)
                    brush = QBrush(Qt.blue)
                    Object.setPen(pen)
                    Object.setBrush(brush)
                elif [Layer, Node] in Globals.MapData["PlayerPath"]:
                    pen = QPen(Qt.darkGreen)
                    brush = QBrush(Qt.yellow)
                    Object.setPen(pen)
                    Object.setBrush(brush)
                else:
                    pen = QPen(Qt.darkGreen)
                    brush = QBrush(Qt.red)
                    Object.setPen(pen)
                    Object.setBrush(brush)

                Map[Layer][Node]["Object"] = Object

                # SETS UP THE ICONS ON TOP OF THE POLYGONS
                Type = Map[Layer][Node]["Type"]
                if Type == "Enemy":
                    Path = f'''images/CombatResources/BasicEncounter.png'''
                elif Type == "Elite":
                    Path = f'''images/CombatResources/EliteEncounter.png'''
                elif Type == "Event":
                    Path = f'''images/CombatResources/Event.png'''
                elif Type == "Treasure":
                    Path = f'''images/CombatResources/Treasure.png'''
                elif Type == "Boss":
                    Path = f'''images/CombatResources/BossEncounter.png'''

                image_qt = QImage(Path)

                pic = QGraphicsPixmapItem()
                pic.setPixmap(QPixmap.fromImage(image_qt))

                Size = 150
                Width = (Size - math.sqrt(Size/2)) * 2
                Height = Size * 2

                OriginX = 50 + (Node * 2 * Width)
                OriginY = (50 + (Layer * 2 * (Height-Height / 4))) * -1

                PicWidth = 225
                PicHeight = 225

                OriginX -= PicWidth / 2
                OriginY -= PicHeight / 2

                pc = self.scene.addItem(pic)
                pic.setOffset(OriginX,OriginY)


                Map[Layer][Node]["ImagePixmap"] = pic
                # Map[Layer][Node]["ImageObject"] = pc

    def setLines(self, Map, MapData):
        Map = Globals.Map
        MapData = Globals.MapData

        pen = QPen(Qt.yellow, 10, Qt.SolidLine)

        for Layer in Map:
            for Node in Map[Layer]:
                NodeData = Map[Layer][Node]
                Polygon = NodeData["Polygon"]
                # Starting Point = 50 + (Node1 * 2 * Width)


                Size = 150
                Width = (Size - math.sqrt(Size/2)) * 2
                Height = Size * 2

                OriginX = 50 + (Node * 2 * Width)
                OriginY = (50 + (Layer * 2 * (Height-Height / 4))) * -1

                OX = OriginX - (Width/2)
                OY = OriginY - (Size/2)
                UpLeft = (OX,OY)

                OX = OriginX + (Width/2)
                OY = OriginY
                BotRight = (OX,OY)

                while True:
                    OX = random.randint(int(UpLeft[0]),int(BotRight[0]))
                    OY = random.randint(int(UpLeft[1]),int(BotRight[1]))
                    # print(RX,RY)
                    Point = QtCore.QPointF(OX,OY)
                    # print(Point)
                    # print(Object)
                    # print(Polygon.containsPoint(Point, 1))
                    if Polygon.containsPoint(Point, 1):
                        break

                StartingCoordinates = (OX,OY)
                StartingPoint = QtCore.QPoint(OX,OY)

                Connections = NodeData["Connections"]["Upper"]
                # print(i)
                for i in Connections:
                    Layer2 = i[0]
                    Node2 = i[1]

                    Polygon = Map[Layer2][Node2]["Polygon"]
                    # Starting Point = 50 + (Node1 * 2 * Width)
                    Size = 150
                    Width = (Size - math.sqrt(Size/2)) * 2
                    Height = Size * 2

                    OriginX = 50 + (Node2 * 2 * Width)
                    OriginY = (50 + (Layer2 * 2 * (Height-Height / 4))) * -1

                    OX = OriginX - (Width/2)
                    OY = OriginY
                    UpLeft = (OX,OY)

                    OX = OriginX + (Width/2)
                    OY = OriginY + (Size/2)
                    BotRight = (OX,OY)

                    while True:
                        OX = random.randint(int(UpLeft[0]),int(BotRight[0]))
                        OY = random.randint(int(UpLeft[1]),int(BotRight[1]))
                        # print(RX,RY)
                        Point = QtCore.QPointF(OX,OY)
                        # print(Point)
                        # print(Object)
                        # print(Polygon.containsPoint(Point, 1))
                        if Polygon.containsPoint(Point, 1):
                            break



                    EndCoordinates = (OX,OY)
                    EndPoint = QtCore.QPoint(OX,OY)

                    # print(StartingCoordinates, EndCoordinates)
                    Polygon = QPolygonF([ QtCore.QPoint(StartingCoordinates[0],StartingCoordinates[1]), QtCore.QPoint(EndCoordinates[0],EndCoordinates[1])] )
                    y = self.scene.addPolygon(Polygon)
                    y.setPen(pen)
                    y.setZValue(-1)
                    # print(10)

    def getEvents(self):
        try:
            Map = Globals.Map
            MapData = Globals.MapData

            Width = MapData["Width"]

            ### PINGS FOR ENEMIES
            PathFull = os.path.abspath(__file__)
            NameLen = len(os.path.basename(__file__))
            Path = PathFull[0:-NameLen]
            PathEnemies = Path + "Combat\\Enemies"
            if PathEnemies not in sys.path:
                sys.path.insert(0, PathEnemies)
            FileList = os.listdir(PathEnemies)
            for FileName in FileList:
                if FileName.endswith(('.py')):
                    FileName = FileName[0:-3]
                    # print(FileName)
                    try:
                        FileReference = __import__(FileName)
                        if FileName not in list(Globals.References.keys()):
                            Globals.References[FileName] = FileReference

                        lst = {"Enemies":[], "Encounters":{"Generic":[], "Custom":[]}, "EliteEnemies":[], "EliteEncounters":{"Generic":[], "Custom":[]}, "BossEncounters":{"Generic":[], "Custom":[]}}
                        try:
                            if len(Globals.MapData["Enemies"]) == 0:
                                lst = FileReference.getEnemies(self, FileReference, lst, "Initial")
                            else:
                                lst = FileReference.getEnemies(self, FileReference, lst, "Post")
                        except Exception as e:
                            ""
                            # print(e)
                        lst["Enemies"] = [k for k in lst["Enemies"] if k not in Globals.MapData["Enemies"]]
                        Globals.MapData["Enemies"] += lst["Enemies"]

                        lst["EliteEnemies"] = [k for k in lst["EliteEnemies"] if k not in Globals.MapData["EliteEnemies"]]
                        Globals.MapData["EliteEnemies"] += lst["EliteEnemies"]

                        lst["Encounters"]["Custom"] = [k for k in lst["Encounters"]["Custom"] if k not in Globals.MapData["Encounters"]["Custom"]]
                        Globals.MapData["Encounters"]["Generic"] += lst["Encounters"]["Generic"]
                        Globals.MapData["Encounters"]["Custom"] += lst["Encounters"]["Custom"]

                        lst["EliteEncounters"]["Custom"] = [k for k in lst["EliteEncounters"]["Custom"] if k not in Globals.MapData["EliteEncounters"]["Custom"]]
                        Globals.MapData["EliteEncounters"]["Generic"] += lst["EliteEncounters"]["Generic"]
                        Globals.MapData["EliteEncounters"]["Custom"] += lst["EliteEncounters"]["Custom"]

                        lst["BossEncounters"]["Custom"] = [k for k in lst["BossEncounters"]["Custom"] if k not in Globals.MapData["BossEncounters"]["Custom"]]
                        Globals.MapData["BossEncounters"]["Generic"] += lst["BossEncounters"]["Generic"]
                        Globals.MapData["BossEncounters"]["Custom"] += lst["BossEncounters"]["Custom"]
                    except:
                        ""

                        ""

            ### PINGS FOR EVENTS
            PathFull = os.path.abspath(__file__)
            NameLen = len(os.path.basename(__file__))
            Path = PathFull[0:-NameLen]
            PathEvents = Path + "Combat\\Events"
            if PathEvents not in sys.path:
                sys.path.insert(0, PathEvents)
            FileList = os.listdir(PathEvents)
            for FileName in FileList:
                if FileName.endswith(('.py')):
                    FileName = FileName[0:-3]
                    try:
                        FileReference = __import__(FileName)
                        if FileName not in list(Globals.References.keys()):
                            Globals.References[FileName] = FileReference

                        lst = {"Events":[], "TreasureEvents":[]}
                        if len(Globals.MapData["Events"]) == 0:
                            Signal = "Initial"
                            lst = FileReference.getEvents(Globals, FileReference, lst, Signal)
                        else:
                            Signal = "Post"
                            lst = FileReference.getEvents(Globals, FileReference, lst, Signal)

                        # lst["Events"] = [k for k in lst["Events"] if k not in Globals.MapData["Events"]]
                        Globals.MapData["Events"] += lst["Events"]
                        # lst["TreasureEvents"] = [k for k in lst["TreasureEvents"] if k not in Globals.MapData["TreasureEvents"]]
                        Globals.MapData["TreasureEvents"] += lst["TreasureEvents"]
                    except Exception as e:
                        Log(2, "ERROR RETRIEVING EVENTS", e, FileName, Signal)

            ### IF THERE ARE NOT ENOUGH ENCOUNTERS IT GENERATES MORE GENERIC ONES
            while len(Globals.MapData["Encounters"]["Generic"]) < Width:
                MapCR = MapData["CR"]
                # MapCR += 1
                AverageCR = 1
                Counter = 1.5
                for i in range(MapCR-1):
                    AverageCR += Counter
                    Counter += 0.5


                MinCR = AverageCR * 0.85
                MaxCR = AverageCR * 1.15

                MinCR = round(MinCR*4)/4
                MaxCR = round(MaxCR*4)/4

                Encounter = {"Enemies":[], "ID":"Generic", "Type":"Encounter", "Source":Globals.Layouts["BattleScene"], "Other":{}, "Status":""}

                FullEnemies = Globals.MapData["Enemies"]

                BaseCR = 0
                TotalCR = 0
                Multiplier = 1
                EnemyCount = 0
                while True:
                    TempCount = EnemyCount + 1

                    # MORE ENEMIES MEAN A BIGGER MULTIPLIER TO DEAL WITH SWARMS
                    if TempCount == 1:
                        Multiplier = 1
                    elif TempCount == 2:
                        Multiplier = 1.5
                    elif TempCount <= 6:
                        Multiplier = 2.0
                    elif TempCount <= 10:
                        Multiplier = 2.5
                    elif TempCount <= 14:
                        Multiplier = 3.0
                    else:
                        Multiplier = 4.0

                    if BaseCR * Multiplier < MaxCR and BaseCR * Multiplier >= MinCR:    # IF INCREASING THE AMOUNT OF ENEMIES BRINGS THE TOTAL WITHIN ACCEPTABLE RANGE OF CR THEN THERE IS A CHANCE IT TRIES TO ROLL FOR ANOTHER ENEMY
                        if random.random() >= 0.5:
                            break
                    elif BaseCR * Multiplier >= MaxCR:  # IF THE TOAL WOULD INCREASE THE MAX THEN IT STOPS THERE
                        break

                    PossibleEnemies = []
                    for i in Globals.MapData["Enemies"]:     # GETS POSSIBLE ENEMIES TO PICK FROM
                        if (BaseCR + i["CR"]) * Multiplier <= MaxCR:
                            PossibleEnemies.append(i)

                    if PossibleEnemies == []:   # IF THERE IS NO ENEMIES TO PICK FROM THEN IT FINISHES THE ENCOUNTER MAKING/
                        break

                    Enemy = random.choice(PossibleEnemies)
                    Encounter["Enemies"].append(Enemy)

                    EnemyCount += 1
                    BaseCR += Enemy["CR"]
                    TotalCR = BaseCR * Multiplier

                if Encounter["Enemies"] != []:
                    Encounter["Other"]["CR"] = TotalCR
                    Globals.MapData["Encounters"]["Generic"].append(Encounter)

            ### IF THERE ARE NOT ENOUGH ELITE ENCOUNTERS IT GENERATES MORE GENERIC ONES
            while len(Globals.MapData["EliteEncounters"]["Generic"]) < Width:
                MapCR = MapData["CR"]
                # MapCR += 1
                AverageCR = 1
                Counter = 1.5
                for i in range(MapCR-1):
                    AverageCR += Counter
                    Counter += 0.5

                MinCR = AverageCR * 0.85
                MaxCR = AverageCR * 1.15

                MinCR = round(MinCR*4)/4
                MaxCR = round(MaxCR*4)/4

                Encounter = {"Enemies":[], "ID":"Generic", "Type":"Elite", "Source":Globals.Layouts["BattleScene"], "Other":{}, "Status":""}

                FullEnemies = Globals.MapData["EliteEnemies"]

                BaseCR = 0
                TotalCR = 0
                Multiplier = 1
                EnemyCount = 0

                while True:
                    TempCount = EnemyCount + 1

                    # MORE ENEMIES MEAN A BIGGER MULTIPLIER TO DEAL WITH SWARMS
                    if TempCount == 1:
                        Multiplier = 1
                    elif TempCount == 2:
                        Multiplier = 1.5
                    elif TempCount <= 6:
                        Multiplier = 2.0
                    elif TempCount <= 10:
                        Multiplier = 2.5
                    elif TempCount <= 14:
                        Multiplier = 3.0
                    else:
                        Multiplier = 4.0

                    if BaseCR * Multiplier < MaxCR and BaseCR * Multiplier >= MinCR:    # IF INCREASING THE AMOUNT OF ENEMIES BRINGS THE TOTAL WITHIN ACCEPTABLE RANGE OF CR THEN THERE IS A CHANCE IT TRIES TO ROLL FOR ANOTHER ENEMY
                        if random.random() >= 0.5:
                            break
                    elif BaseCR * Multiplier >= MaxCR:  # IF THE TOAL WOULD INCREASE THE MAX THEN IT STOPS THERE
                        break

                    PossibleEnemies = []
                    for i in Globals.MapData["EliteEnemies"]:     # GETS POSSIBLE ENEMIES TO PICK FROM
                        if (BaseCR + i["CR"]) * Multiplier <= MaxCR:
                            PossibleEnemies.append(i)

                    if PossibleEnemies == []:   # IF THERE IS NO ENEMIES TO PICK FROM THEN IT FINISHES THE ENCOUNTER MAKING/
                        break

                    Enemy = random.choice(PossibleEnemies)
                    Encounter["Enemies"].append(Enemy)

                    EnemyCount += 1
                    BaseCR += Enemy["CR"]
                    TotalCR = BaseCR * Multiplier

                if Encounter["Enemies"] != []:
                    Encounter["Other"]["CR"] = TotalCR
                    Globals.MapData["EliteEncounters"]["Generic"].append(Encounter)

            ### IF THERE ARE NOT ENOUGH ELITE ENCOUNTERS IT GENERATES MORE GENERIC ONES
            while len(Globals.MapData["BossEncounters"]["Generic"]) < Width:
                MapCR = MapData["CR"]
                MapCR += 2
                AverageCR = MapCR
                Counter = 1.5
                for i in range(MapCR-1):
                    AverageCR += Counter
                    Counter += 0.5

                MinCR = AverageCR * 0.85
                MaxCR = AverageCR * 1.15

                MinCR = round(MinCR*4)/4
                MaxCR = round(MaxCR*4)/4

                Encounter = {"Enemies":[], "ID":"Generic", "Type":"Boss", "Source":Globals.Layouts["BattleScene"], "Other":{}, "Status":""}

                FullEnemies = Globals.MapData["EliteEnemies"]

                BaseCR = 0
                TotalCR = 0
                Multiplier = 1
                EnemyCount = 0

                while True:
                    TempCount = EnemyCount + 1

                    # MORE ENEMIES MEAN A BIGGER MULTIPLIER TO DEAL WITH SWARMS
                    if TempCount == 1:
                        Multiplier = 1
                    elif TempCount == 2:
                        Multiplier = 1.5
                    elif TempCount <= 6:
                        Multiplier = 2.0
                    elif TempCount <= 10:
                        Multiplier = 2.5
                    elif TempCount <= 14:
                        Multiplier = 3.0
                    else:
                        Multiplier = 4.0

                    if BaseCR * Multiplier < MaxCR and BaseCR * Multiplier >= MinCR:    # IF INCREASING THE AMOUNT OF ENEMIES BRINGS THE TOTAL WITHIN ACCEPTABLE RANGE OF CR THEN THERE IS A CHANCE IT TRIES TO ROLL FOR ANOTHER ENEMY
                        if random.random() >= 0.5:
                            break
                    elif BaseCR * Multiplier >= MaxCR:  # IF THE TOAL WOULD INCREASE THE MAX THEN IT STOPS THERE
                        break

                    PossibleEnemies = []
                    for i in Globals.MapData["EliteEnemies"]:     # GETS POSSIBLE ENEMIES TO PICK FROM
                        if (BaseCR + i["CR"]) * Multiplier <= MaxCR:
                            PossibleEnemies.append(i)

                    if PossibleEnemies == []:   # IF THERE IS NO ENEMIES TO PICK FROM THEN IT FINISHES THE ENCOUNTER MAKING/
                        break

                    Enemy = random.choice(PossibleEnemies)
                    Encounter["Enemies"].append(Enemy)

                    EnemyCount += 1
                    BaseCR += Enemy["CR"]
                    TotalCR = BaseCR * Multiplier

                if Encounter["Enemies"] != []:
                    Encounter["Other"]["CR"] = TotalCR
                    Globals.MapData["BossEncounters"]["Generic"].append(Encounter)


        except Exception as e:
            Log(4, "ERROR GET EVENTS AND ENCOUNTERS", e)

    def setEvents(self):
        self.getEvents()

        if Globals.MapData["Encounters"]["Generic"] == [] and Globals.MapData["Encounters"]["Custom"] == []:
            Log(3, "ERROR NO NORMAL ENCOUNTER")
        if Globals.MapData["EliteEncounters"]["Generic"] == [] and Globals.MapData["EliteEncounters"]["Custom"] == []:
            Log(3, "ERROR NO ELITE ENCOUNTER AVAILABLE")
        if Globals.MapData["Events"] == []:
            Log(3, "ERROR NO EVENTS AVAILABLE")
        if Globals.MapData["TreasureEvents"] == []:
            Log(3, "ERROR NO TREASURE EVENTS AVAILABLE")
        if Globals.MapData["BossEncounters"]["Generic"] == [] and Globals.MapData["BossEncounters"]["Custom"] == []:
            Log(3, "ERROR NO BOSS ENCOUNTER AVAILABLE")

        Map, MapData = Globals.Map, Globals.MapData
        try:
            for Layer in Map:
                for Node in Map[Layer]:
                    try:
                        if Map[Layer][Node]["Status"] == "Available" and Map[Layer][Node]["Encounter"] == '':
                            Type = Map[Layer][Node]["Type"]
                            if Type  == "Enemy":
                                if Globals.MapData["Encounters"]["Custom"] == [] and Globals.MapData["Encounters"]["Generic"] == []:
                                    self.getEvents()
                                if Globals.MapData["Encounters"]["Custom"] == []:
                                    Encounter = Globals.MapData["Encounters"]["Generic"].pop(random.randrange(len(Globals.MapData["Encounters"]["Generic"])))
                                    Globals.Map[Layer][Node]["Encounter"] = Encounter
                                else:
                                    if random.random() >= 0.6:
                                        Encounter = Globals.MapData["Encounters"]["Generic"].pop(random.randrange(len(Globals.MapData["Encounters"]["Generic"])))
                                        Globals.Map[Layer][Node]["Encounter"] = Encounter
                                    else:
                                        Encounter = Globals.MapData["Encounters"]["Custom"].pop(random.randrange(len(Globals.MapData["Encounters"]["Custom"])))
                                        Globals.Map[Layer][Node]["Encounter"] = Encounter
                            elif Type == "Elite":
                                if Globals.MapData["EliteEncounters"]["Custom"] == [] and Globals.MapData["EliteEncounters"]["Generic"] == []:
                                    self.getEvents()
                                if Globals.MapData["EliteEncounters"]["Custom"] == []:
                                    Encounter = Globals.MapData["EliteEncounters"]["Generic"].pop(random.randrange(len(Globals.MapData["EliteEncounters"]["Generic"])))
                                    Globals.Map[Layer][Node]["Encounter"] = Encounter
                                else:
                                    if random.random() >= 0.6:
                                        Encounter = Globals.MapData["EliteEncounters"]["Generic"].pop(random.randrange(len(Globals.MapData["EliteEncounters"]["Generic"])))
                                        Globals.Map[Layer][Node]["Encounter"] = Encounter
                                    else:
                                        Encounter = Globals.MapData["EliteEncounters"]["Custom"].pop(random.randrange(len(Globals.MapData["EliteEncounters"]["Custom"])))
                                        Globals.Map[Layer][Node]["Encounter"] = Encounter
                            elif Type == "Event":
                                if Globals.MapData["Events"]:
                                    self.getEvents()
                                Event = Globals.MapData["Events"].pop(random.randrange(len(Globals.MapData["Events"])))
                                Globals.Map[Layer][Node]["Encounter"] = Event
                            elif Type == "Treasure":
                                if Globals.MapData["TreasureEvents"]:
                                    self.getEvents()
                                Event = Globals.MapData["TreasureEvents"].pop(random.randrange(len(Globals.MapData["TreasureEvents"])))
                                Globals.Map[Layer][Node]["Encounter"] = Event
                            elif Type == "Boss":
                                if Globals.MapData["BossEncounters"]["Custom"] == [] and Globals.MapData["BossEncounters"]["Generic"] == []:
                                    self.getEvents()
                                if Globals.MapData["BossEncounters"]["Custom"] == []:
                                    Encounter = Globals.MapData["BossEncounters"]["Generic"].pop(random.randrange(len(Globals.MapData["BossEncounters"]["Generic"])))
                                    Globals.Map[Layer][Node]["Encounter"] = Encounter
                                else:
                                    if random.random() >= 0.6:
                                        Encounter = Globals.MapData["BossEncounters"]["Generic"].pop(random.randrange(len(Globals.MapData["BossEncounters"]["Generic"])))
                                        Globals.Map[Layer][Node]["Encounter"] = Encounter
                                    else:
                                        Encounter = Globals.MapData["BossEncounters"]["Custom"].pop(random.randrange(len(Globals.MapData["BossEncounters"]["Custom"])))
                                        Globals.Map[Layer][Node]["Encounter"] = Encounter
                    except Exception as e:
                        Log(2, "ERROR WHILE SET EVENTS", e, Type)
                        continue
        except Exception as e:
            Log(2, "ERROR SET EVENTS", e, Type)




def Initialize(self, Reference):
    if "BattleScene" not in Globals.Layouts:
        UiLayoutBattleScene()
    if "BattleMenu" not in Globals.Layouts:
        UiLayoutBattleMenu()
