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
from battleMenuUI import SRObject
Log = Globals.Layouts["MainF"].Log

def getEvents(self, Reference, FullList, Signal):

    # Reference.getEnemies(self, FileReference, lst, "Initial")
    if Signal == "Initial":
        # lst = {"Enemies":[], "Encounters":[], "EliteEnemies":[], "EliteEncounters":[], "BossEncounters":[]}
        EventsList = [{"ID":"Merchant", "Origin":Reference, "Data":{}} , {"ID":"Campfire", "Origin":Reference, "Data":{}}, {"ID":"BrokenCarriage", "Origin":Reference, "Data":{}}]
        for i in EventsList:
            FullList["Events"].append(i)

        TreasureEventsList = [{"ID":"Chest", "Origin":Reference, "Data":{}}]
        for i in TreasureEventsList:
            FullList["TreasureEvents"].append(i)

    elif Signal == "Post":
        EventsList = [{"ID":"Merchant", "Origin":Reference, "Data":{}} , {"ID":"Campfire", "Origin":Reference, "Data":{}}, {"ID":"BrokenCarriage", "Origin":Reference, "Data":{}}]
        for i in EventsList:
            if i not in Globals.MapData["Events"]:
                FullList["Events"].append(i)

        TreasureEventsList = [{"ID":"Chest", "Origin":Reference, "Data":{}}]
        for i in TreasureEventsList:
            if i not in Globals.MapData["TreasureEvents"]:
                FullList["TreasureEvents"].append(i)

    return FullList

def EventTriggered(self, Event, Coordinates):
    try:
        def Initialize():
            Globals.Map[Coordinates[0]][Coordinates[1]]["Status"] = "Current"
            Globals.MapData["PlayerPath"].append(Coordinates)
            Globals.Layouts["BattleScene"].Refresh()

        # if Event["ID"] == "Merchant":
        if True:
            if "Merchant" in Globals.EventData:
                try:
                    self.EventWindow.show()
                except:
                    ""
            else:
                Initialize()
                Globals.EventData["Merchant"] = {"Initialized":1}

                self.EventWindow = QWidget(self.GUI)
                self.EventWindow.setGeometry(350,10,930,950)
                self.EventWindow.show()
                self.EventWindow.setStyleSheet('''
                .QWidget{
                border: 2px solid green;
                }
                .QScrollArea{
                border: 2px solid black;
                }
                QGroupBox{
                background-color:rgb(23, 23, 23);
                }

                ''')

                EventFlavor = QLabel(self.EventWindow)
                EventFlavor.setText('''A humble merchant appears in your way "Would you care to see my wares traveler?" ''')
                EventFlavor.setGeometry(10,10,830,40)
                EventFlavor.setFont(QFont('Segoe UI', 14))
                EventFlavor.setStyleSheet('''
                QLabel{
                background-color:rgb(23, 23, 23);
                border: 2px solid black;
                color: white;
                }
                ''')
                EventFlavor.show()

                def EC():
                    Globals.Map[Coordinates[0]][Coordinates[1]]["Status"] = "Unavailable"
                    self.ReturnToLayout()
                    self.EventWindow.hide()
                    self.EventWindow = None
                    Globals.EventData.pop("Merchant")

                DoneButton = QPushButton("Done", self.EventWindow, clicked = lambda: EC())
                DoneButton.setGeometry(850,10,70,40)
                DoneButton.show()
                DoneButton.setFont(QFont('Segoe UI', 14))
                # DoneButton.setStyleSheet('''
                # ''')


                ### CALCULATES AND SETS UP THE CARDS
                def CalculateCards(Amount):
                    MCardChance = 0
                    NCardChance = 50
                    RCardChance = 35
                    SRCardChance = 15

                    TotalCardChance = MCardChance + NCardChance + RCardChance + SRCardChance
                    CardOptions = []
                    for i in range(Amount):
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
                    return CardOptions
                class CardWhole:
                    def __init__(self, Attack):
                        self.Attack = Attack
                        Rarity = Attack["Rarity"]
                        if Rarity == "Mundane":
                            self.Price = random.randint(15,45)
                        if Rarity == "Normal":
                            self.Price = random.randint(35,65)
                        if Rarity == "Rare":
                            self.Price = random.randint(55,85)
                        if Rarity == "SuperRare":
                            self.Price = random.randint(85,125)

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
                            print("Oh")
                            print(self.Price)
                            # Globals.Layouts["BattleMenu"].CreateCard(Attack)
                            # Globals.Layouts["BattleMenu"].CardReward.hide()
                            # # Globals.Layouts["BattleMenu"].ConsumeReward(Reward)

                        Card = AttackReference.getCard(self, Attack, "Details")
                        Card.setMinimumWidth(290)
                        Card.setMinimumHeight(445)
                        Card.mouseReleaseEvent = lambda event: CC()
                        CardsLayout.addWidget(Card, 1)


                        return CardWhole

                ScrollCards = QScrollArea(self.EventWindow)
                ScrollCards.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                ScrollCards.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
                ScrollCards.setGeometry(10,380,900,520)

                CardsLayoutWhole = QGridLayout(self.EventWindow)

                AmountCards = random.randint(3,6)
                Attacks = CalculateCards(AmountCards)
                Layer = 0
                Row = 0
                for Attack in Attacks:
                    CardObject = CardWhole(Attack)
                    CardWidget = CardObject.getWidget()
                    CardsLayoutWhole.addWidget(CardWidget, Layer, Row)
                    Row += 1
                    if Row == 3:
                        Layer += 1
                        Row = 0

                CardsLayoutWhole.setContentsMargins(0, 0, 0, 5)
                CardBox = QGroupBox()
                CardBox.setLayout(CardsLayoutWhole)
                ScrollCards.setWidget(CardBox)
                CardBox.setContentsMargins(0, 0, 0, 0)
                ScrollCards.show()

                # def CalculateRelics(Amount):
                #     ""






        else:
            print(Event["ID"])
    except Exception as e:
        print("ERROR EVENT TRIGGERED", e, Event)
