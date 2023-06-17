import json
import os
import random
from time import sleep

from PyQt5.QtCore import *
from PyQt5.QtCore import QObject, QThread, pyqtSignal
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import Globals
from battleMenuUI import SRObject

Log = Globals.Layouts["MainF"].Log


class Worker(QObject):
    def __init__(self, Func, Data, AnimationID, Cast, parent = None):
        super(Worker, self).__init__()
        self.Func = Func
        self.Data = Data
        self.AnimationID = AnimationID
        self.Cast = Cast
        self._isRunning = True

        ID = list(Globals.Threads.keys())[-1]
        self.ThreadID = ID

    finished = pyqtSignal()
    progress = pyqtSignal(int)
    ping = pyqtSignal()
    ping2 = pyqtSignal()

    def run(self):
        self.Func(self, self.AnimationID)

    def task(self):
        try:
            if self._isRunning:
                # print("Thread", hex(id(self.Data)))
                Globals.AnimationData[self.AnimationID]["Thread"] = self
                # Globals.BattleAniData["Thread"] = self
                self.Func(self, self.AnimationID, self.Cast)
        except Exception as e:
            Log(2, "ERROR THREAD TASK", e, self.Func, "WarriorDeck0")

    def clean(self):
        Globals.AnimationData[AnimationID].pop(self.AnimationID)
        Globals.FinishedThreads.append(self.ThreadID)


    def stop(self):
        self._isRunning = False
def CleanThreads(self):
    lst = Globals.FinishedThreads
    try:
        for ThreadID in lst:
            Globals.Threads[ThreadID]["Worker"].stop()
            Globals.Threads[ThreadID]["Thread"].quit()
            Globals.Threads[ThreadID]["Thread"].wait()

            Globals.Threads.pop(ThreadID)
            Globals.FinishedThreads.remove(ThreadID)

            # if Globals.Threads[ThreadID]["Thread"].isFinished():
            #     Globals.Threads[ThreadID]["Thread"].quit()
            #     Globals.Threads[ThreadID]["Worker"].deleteLater()
            #     # Globals.Threads[ThreadID]["Thread"].deleteLater()
            #     Globals.Threads[ThreadID]["Thread"].deleteLater()
            #
            #     Globals.Threads.pop(ThreadID)
            #     Globals.FinishedThreads.remove(ThreadID)
            # else:
            #     print("Unfinished:", ThreadID)
    except Exception as e:
        Log(2, "ERROR CLEANING THREADS:", e)

def getDeck(AvailableCards, FullDeck, CurrentHandWhole, DrawDeck, DiscardDeck, ExhaustDeck, CurseDeck, SR, DeckReference):
    def ApllyRarity(Attack):
        MList = ["Strike0", "HeavyStrike0", "Defend0", "FearsomeGaze0"]
        NList = ["TauntingBlow0", "CheapStrike0", "Jab0", "FlurryOfBlows0", "Swipe0", "Charge0", "Parry0", "Concentrate0", "HunkerDown0", "Feint0", "EndlessCombat0", "Preparation0", "FearsomeGaze0", "Terrify0", "LongHunt0", "PainfullFear0", "MassPanic0", "Unyielding0", "Nightmares0", "Intimidate0"]
        RList = ["ShowOfForce0", "BrokenGuard0", "DisarmingStrike0", "FullCombo0", "ShieldBreaker0", "Counter0", "Barricade0", "ThrillOfBattle0", "RelentlessForce0", "SupressionAssault0", "Guillotine0", "ShowOfMight0", "BloodyHorror0", "CripplingHorror0", "ShakySteps0", "PreyInstincts0"]
        SRList = ["Bloodlust0", "ScorchedLand0", "FinalStand0"]
        if Attack["AttackID"] in MList:
            Attack["Rarity"] = "Mundane"
        elif Attack["AttackID"] in NList:
            Attack["Rarity"] = "Normal"
        elif Attack["AttackID"] in RList:
            Attack["Rarity"] = "Rare"
        elif Attack["AttackID"] in SRList:
            Attack["Rarity"] = "SuperRare"
        return Attack


    AvailableList = ["Strike0", "HeavyStrike0", "Bloodlust0", "ShowOfForce0", "FlurryOfBlows0", "TauntingBlow0", "CheapStrike0", "BrokenGuard0", "DisarmingStrike0", "Jab0", "FullCombo0", "Swipe0", "ShieldBreaker0", "ScorchedLand0", "Charge0", "Defend0", "Parry0", "Counter0", "Concentrate0", "HunkerDown0", "Barricade0", "Feint0", "ThrillOfBattle0", "RelentlessForce0", "SupressionAssault0", "EndlessCombat0", "FinalStand0", "Preparation0", "Guillotine0", "ShowOfMight0", "FearsomeGaze0", "Terrify0", "LongHunt0", "BloodyHorror0", "PainfullFear0", "CripplingHorror0", "MassPanic0", "ShakySteps0", "Unyielding0", "Nightmares0", "PreyInstincts0", "Intimidate0"]
    for i in AvailableList:
        Attack = ApllyRarity({"AttackID":i, "DeckReference":DeckReference, "Origin":r"Combat\Decks\WarriorDeck0", "Flags":{"CanBeUpgraded":1,"CanBeUsed":1,"NumberOfUpgrades":0}, "Parent":"", "Rarity":"", "Deck":"DiscardDeckWhole"})
        AvailableCards.append(Attack)

    CurrentList = []
    for i in CurrentList:
        Attack = ApllyRarity({"AttackID":i, "DeckReference":DeckReference, "Origin":r"Combat\Decks\WarriorDeck0", "Flags":{"CanBeUpgraded":1,"CanBeUsed":1,"NumberOfUpgrades":0}, "Parent":"", "Rarity":"", "Deck":"DrawDeckWhole"})
        DrawDeck.append(Attack)

    # DiscardList = AvailableList
    DiscardList = ["Strike0","Strike0","Strike0","Strike0","Strike0", "Defend0", "Defend0", "Defend0", "Defend0", "Defend0", "HeavyStrike0"]
    for i in DiscardList:
        Attack = ApllyRarity({"AttackID":i, "DeckReference":DeckReference, "Origin":r"Combat\Decks\WarriorDeck0", "Flags":{"CanBeUpgraded":1,"CanBeUsed":1,"NumberOfUpgrades":0}, "Parent":"", "Rarity":"", "Deck":"DiscardDeckWhole"})
        DiscardDeck.append(Attack)

    SR.append({"Upper":7, "Lower":3, "Bonus":0, "Minus":0})
    SR.append({"Upper":7, "Lower":3, "Bonus":0, "Minus":0})
    SR.append({"Upper":7, "Lower":3, "Bonus":0, "Minus":0})
    SR.append({"Upper":7, "Lower":3, "Bonus":0, "Minus":0})
    return AvailableCards, FullDeck, CurrentHandWhole, DrawDeck, DiscardDeck, ExhaustDeck, CurseDeck, SR
def getStats(NPCID):
    with open('NPCdata.json', 'rb') as f:
        NPCfullData = json.load(f)
    NPCData = NPCfullData[NPCID]
    return {"HP":50, "STR":3, "DEX":0, "CHA":1, "SR":[[1,6,2],[1,6,2]]}

    # return dict

def getCard(self, Attack, Type):
    Parent = Attack["Parent"]
    Move = Attack["AttackID"]
    # ID = Attack["AttackID"]
    # print(self)
    self = Globals.Layouts["BattleMenu"]
    try:
        if Move == "Strike0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal 5 Damage<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setText("E")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal 5 Damage<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "HeavyStrike0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel("5", CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 >= 5:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:red;
                        ''')

                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = 0
                if SR2 > 0:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-left-color:rgb(35,35,35);
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:grey;
                        ''')
                    else:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:white;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>{SR1 + SR2}</b></span> Damage<br>
                Applies 1 Vulnerable<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel("5", CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 >= 5:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    color:grey;
                    ''')

                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:rgb(255, 255, 255);
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = "SR2"
                    SRSlot2.setText(str(SR2))
                try:
                    if SR2 > 0:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:grey;
                        ''')
                    else:
                        raise
                except:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-left-color:rgb(35,35,35);
                    color:white;
                    ''')


                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setText("E")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>{SR1} + {SR2}</b></span> Damage<br>
                Applies 1 Vulnerable<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "Bloodlust0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                border-right-color:rgb(35,35,35);
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:grey;
                        ''')

                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                border-left-color:rgb(35,35,35);
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = 0
                if SR2 > 0:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-left-color:rgb(35,35,35);
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:grey;
                        ''')

                SRSlot3 =  QLabel(CardNew)
                SRSlot3.setGeometry(90,10,40,40)
                SRSlot3.setFont(QFont('Segoe UI', 14))
                SRSlot3.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot3.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][2]]
                    SR = SR.Total
                    SR3 = SR
                    SRSlot3.setText(str(SR3))
                except Exception as e:
                    SR3 = 0
                if SR3 > 0:
                    SRSlot3.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 3:
                        SRSlot3.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot3.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyIndex = Globals.BattleInfo["Allies"][0]
                    EnemyLabel1.setText(str(AllyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')
                except:
                    EnemyLabel1.setText("RE")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                # CardText.setText(f'''
                # <html><head/><body>
                # <p style="line-height:1.3"><span>
                # Randomly deal <span style="color:red;"><b>{SR1 + SR2}</b></span> Damage <span style="color:red;"><b>{int((SR3 / 2)//1)}</b></span> times <br>
                # Heal for half the Damage dealt<br/>
                # </span></p>
                # </body></html>
                # ''')

                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Randomly deal <span style="color:red;"><b>{SR1 + SR2}</b></span> Damage and heal for half the damage <span style="color:red;"><b>{int((SR3 / 2)//1)}</b></span> Times
                </span></p>
                </body></html>
                ''')


                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                border-right-color:rgb(35,35,35);
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    color:grey;
                    ''')

                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                border-left-color:rgb(35,35,35);
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = 0
                    SR2 = "SR2"
                    SRSlot2.setText(str(SR2))
                try:
                    if SR2 > 0:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-left-color:rgb(35,35,35);
                    color:grey;
                    ''')

                SRSlot3 =  QLabel(CardNew)
                SRSlot3.setGeometry(90,10,40,40)
                SRSlot3.setFont(QFont('Segoe UI', 14))
                SRSlot3.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot3.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][2]]
                    SR = SR.Total
                    SR3 = SR
                    SRSlot3.setText(str(SR3))
                except Exception as e:
                    SR3 = 0
                    SR3 = "SR3"
                    SRSlot3.setText(str(SR3))
                try:
                    if SR3 > 0:
                        SRSlot3.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 3:
                        SRSlot3.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot3.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')


                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

                try:
                    EnemyIndex = Globals.BattleInfo["Allies"][0]
                    EnemyLabel1.setText(str(AllyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')
                except:
                    EnemyLabel1.setText("RE")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')

                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Randomly deal <span style="color:red;"><b>{SR1} + {SR2}</b></span> Damage and heal for half the damage <span style="color:red;"><b>{SR3}</b></span> / 2 times
                Heal for half the Damage dealt<br>
                </span></p>
                </body></html>
                ''')



                return CardNew
        elif Move == "ShowOfForce0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel("7", CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 >= 7:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setWordWrap(True)
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>{SR1}</b></span> Damage<br>
                Apply Vulnerable for 1/3 the Damage dealt
                </span></p>
                </body></html>
                ''')
                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel("7", CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 >= 7:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setText("E")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>{SR1}</b></span> Damage<br>
                Apply Vulnerable for 1/3 the Damage dealt
                </span></p>
                </body></html>
                ''')
                return CardNew
        elif Move == "FlurryOfBlows0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:grey;
                        ''')


                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = 0
                if SR2 > 0:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-left-color:rgb(35,35,35);
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:grey;
                        ''')

                SRSlot3 =  QLabel("4", CardNew)
                SRSlot3.setGeometry(90,10,40,40)
                SRSlot3.setFont(QFont('Segoe UI', 14))
                SRSlot3.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot3.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][2]]
                    SR = SR.Total
                    SR3 = SR
                    SRSlot3.setText(str(SR3))
                except Exception as e:
                    SR3 = 0
                if SR3 >= 4:
                    SRSlot3.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 3:
                        SRSlot3.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot3.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')


                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>{SR1}</b></span> Damage <span style="color:red;"><b>{SR2}</b></span> times <br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    color:grey;
                    ''')

                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = "SR2"
                    SRSlot2.setText(str(SR2))
                try:
                    if SR2 > 0:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-left-color:rgb(35,35,35);
                    color:grey;
                    ''')


                SRSlot3 =  QLabel("4", CardNew)
                SRSlot3.setGeometry(90,10,40,40)
                SRSlot3.setFont(QFont('Segoe UI', 14))
                SRSlot3.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot3.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][2]]
                    SR = SR.Total
                    SR3 = SR
                    SRSlot3.setText(str(SR3))
                except Exception as e:
                    SR3 = "SR3"
                    SRSlot3.setText(str(SR3))
                try:
                    if SR3 >= 4:
                        SRSlot3.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 3:
                        SRSlot3.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot3.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')


                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setText("E")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>{SR1}</b></span> Damage <span style="color:red;"><b>{SR2}</b></span> times <br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "TauntingBlow0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>{SR1}</b></span> Damage and switch target to self<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')


                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setText("E")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>{SR1}</b></span> Damage and switch target to self<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "CheapStrike0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal 4 Damage<br>
                Apply 1 Vulnerable<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setText("E")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal 4 Damage<br>
                Apply 1 Vulnerable<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "BrokenGuard0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel("5", CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:grey;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 >= 5:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')


                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:grey;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = 0
                if SR2 > 0:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')


                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                # TODO
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal Vulnerable x 4 as Damage<br>
                Double the target Vulnerable<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel("5", CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:grey;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 >= 5:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:grey;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = "SR2"
                    SRSlot2.setText(str(SR2))
                try:
                    if SR2 > 0:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setText("E")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                # TODO
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal Vulnerable x 4 as Damage<br>
                Double the target Vulnerable<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "DisarmingStrike0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')


                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal 4 Damage<br>
                Apply 1 Weak<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setText("E")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal 4 Damage<br>
                Apply 1 Weak<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "Jab0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal 4 Damage<br>
                Create a Jab on top of the draw pile<br>
                Exhaust<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setText("E")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal 4 Damage<br>
                Create a Jab on top of the draw pile<br>
                Exhaust<br>
                </span></p>
                </body></html>
                ''')
                return CardNew
        elif Move == "FullCombo0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                border-right-color:rgb(35,35,35);
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:grey;
                        ''')


                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = 0
                if SR2 > 0:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    border-left-color:rgb(35,35,35);
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        border-left-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        border-left-color:rgb(35,35,35);
                        color:grey;
                        ''')


                SRSlot3 =  QLabel(CardNew)
                SRSlot3.setGeometry(90,10,40,40)
                SRSlot3.setFont(QFont('Segoe UI', 14))
                SRSlot3.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot3.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][2]]
                    SR = SR.Total
                    SR3 = SR
                    SRSlot3.setText(str(SR3))
                except Exception as e:
                    SR3 = 0
                if SR3 > 0:
                    SRSlot3.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-left-color:rgb(35,35,35);
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 3:
                        SRSlot3.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        SRSlot3.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal 8 Damage 3 times<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    color:grey;
                    ''')


                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = "SR2"
                    SRSlot2.setText(str(SR2))
                try:
                    if SR2 > 0:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        border-left-color:rgb(35,35,35);
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        border-left-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    border-left-color:rgb(35,35,35);
                    color:grey;
                    ''')


                SRSlot3 =  QLabel(CardNew)
                SRSlot3.setGeometry(90,10,40,40)
                SRSlot3.setFont(QFont('Segoe UI', 14))
                SRSlot3.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot3.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][2]]
                    SR = SR.Total
                    SR3 = SR
                    SRSlot3.setText(str(SR3))
                except Exception as e:
                    SR3 = "SR3"
                    SRSlot3.setText(str(SR3))
                try:
                    if SR3 > 0:
                        SRSlot3.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 3:
                        SRSlot3.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot3.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-left-color:rgb(35,35,35);
                    color:grey;
                    ''')


                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setText("E")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal 8 Damage 3 times<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "Swipe0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                SRSlot2 =  QLabel("5", CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = 0
                if SR2 >= 5:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyIndex = Globals.BattleInfo["Allies"][0]
                    EnemyLabel1.setText("AllE")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')
                except:
                    EnemyLabel1.setText("AllE")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>{SR1}</b></span> Damage to every enemy<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel("5", CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = "SR2"
                    SRSlot2.setText(str(SR2))
                try:
                    if SR2 >= 5:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')


                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

                try:
                    EnemyIndex = Globals.BattleInfo["Allies"][0]
                    EnemyLabel1.setText("AllE")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')
                except:
                    EnemyLabel1.setText("AllE")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>{SR1}</b></span> Damage to every enemy<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "ShieldBreaker0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 >= 5:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')


                SRSlot2 =  QLabel("5", CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = 0
                if SR2 > 0:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')



                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Remove the enemy shield<br>
                Deal <span style="color:red;"><b>{SR1}</b></span> Damage<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 >= 5:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                SRSlot2 =  QLabel("5", CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = "SR2"
                    SRSlot2.setText(str(SR2))
                try:
                    if SR2 > 0:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')


                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setText("E")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Remove the enemy shield<br>
                Deal <span style="color:red;"><b>{SR1}</b></span> Damage<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "ScorchedLand0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = 0
                if SR2 > 0:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')


                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

                try:
                    EnemyIndex = Globals.BattleInfo["Allies"][0]
                    EnemyLabel1.setText("AllE")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')
                except:
                    EnemyLabel1.setText("AllE")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal 25 Damage to every enemy<br>
                Recieve 8 Damage<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = "SR2"
                    SRSlot2.setText(str(SR2))
                try:
                    if SR2 > 0:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyIndex = Globals.BattleInfo["Allies"][0]
                    EnemyLabel1.setText("AllE")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')
                except:
                    EnemyLabel1.setText("AllE")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal 25 Damage to every enemy<br>
                Recieve 8 Damage<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "Charge0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel("5", CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 >= 5:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal Shield as Damage<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel("5", CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 >= 5:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')


                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setText("E")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal Shield as Damage<br>
                </span></p>
                </body></html>
                ''')

                return CardNew

        elif Move == "Defend0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                AllyLabel1 =  QLabel(CardNew)
                AllyLabel1.setGeometry(240,52,40,40)
                AllyLabel1.setFont(QFont('Segoe UI', 14))
                AllyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    AllyID = list(Globals.BattleInfo["Allies"].keys())[0]
                    AllyIndex = list(Globals.BattleObjects["Allies"].keys()).index(AllyID)
                    AllyLabel1.setText(str(AllyIndex))
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Gain 5 Block<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                AllyLabel1 =  QLabel(CardNew)
                AllyLabel1.setGeometry(240,52,40,40)
                AllyLabel1.setFont(QFont('Segoe UI', 14))
                AllyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    AllyID = list(Globals.BattleInfo["Allies"].keys())[0]
                    AllyIndex = list(Globals.BattleObjects["Allies"].keys()).index(AllyID)
                    AllyLabel1.setText(str(AllyIndex))
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    AllyLabel1.setText("A")
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Gain 5 Block<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "Parry0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                border-right-color:rgb(35,35,35);
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:grey;
                        ''')


                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                border-left-color:rgb(35,35,35);
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = 0
                if SR2 > 0:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-left-color:rgb(35,35,35);
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:grey;
                        ''')
                    else:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:white;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                AllyLabel1 =  QLabel(CardNew)
                AllyLabel1.setGeometry(240,52,40,40)
                AllyLabel1.setFont(QFont('Segoe UI', 14))
                AllyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    if Globals.BattleInfo["Allies"][0] == Parent:
                        AllyLabel1.setText(Globals.BattleInfo["Allies"][0])
                        AllyLabel1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    else:
                        AllyLabel1.setText(Globals.BattleInfo["Allies"][0])
                        AllyLabel1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                except:
                    AllyLabel1.setText(str(Parent))
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Block the first hit<br>
                Reflects up to <span style="color:red;"><b>{SR1 + SR2}</b></span> Damage<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                border-right-color:rgb(35,35,35);
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    color:grey;
                    ''')

                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                border-left-color:rgb(35,35,35);
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = "SR2"
                    SRSlot2.setText(str(SR2))
                try:
                    if SR2 > 0:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:grey;
                        ''')
                    else:
                        raise
                except:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-left-color:rgb(35,35,35);
                    color:white;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                AllyLabel1 =  QLabel(CardNew)
                AllyLabel1.setGeometry(240,52,40,40)
                AllyLabel1.setFont(QFont('Segoe UI', 14))
                AllyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    if Globals.BattleInfo["Allies"][0] == Parent:
                        AllyLabel1.setText(Globals.BattleInfo["Allies"][0])
                        AllyLabel1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    else:
                        AllyLabel1.setText(Globals.BattleInfo["Allies"][0])
                        AllyLabel1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                except:
                    AllyLabel1.setText("S")
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Block the first hit<br>
                Reflects up to <span style="color:red;"><b>{SR1} + {SR2}</b></span> Damage<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "Counter0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')


                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                AllyLabel1 =  QLabel(CardNew)
                AllyLabel1.setGeometry(240,52,40,40)
                AllyLabel1.setFont(QFont('Segoe UI', 14))
                AllyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    AllyID = list(Globals.BattleInfo["Allies"].keys())[0]
                    AllyIndex = list(Globals.BattleObjects["Allies"].keys()).index(AllyID)
                    AllyLabel1.setText(str(AllyIndex))
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    # AllyLabel1.setText("A")
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>{int(SR1/2)}</b></span> Damage back for every attack blocked<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                AllyLabel1 =  QLabel(CardNew)
                AllyLabel1.setGeometry(240,52,40,40)
                AllyLabel1.setFont(QFont('Segoe UI', 14))
                AllyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    AllyID = list(Globals.BattleInfo["Allies"].keys())[0]
                    AllyIndex = list(Globals.BattleObjects["Allies"].keys()).index(AllyID)
                    AllyLabel1.setText(str(AllyIndex))
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    AllyLabel1.setText("A")
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>{SR1}</b></span> / 2 Damage back for every attack blocked<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "Concentrate0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Add <span style="color:red;"><b>{int(SR1/2)}</b></span> bonus at all your current SR<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Add <span style="color:red;"><b>{SR1}</b></span> / 2 bonus at all your current SR<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "HunkerDown0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:grey;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:grey;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = 0
                if SR2 > 0:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')


                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                AllyLabel1 =  QLabel(CardNew)
                AllyLabel1.setGeometry(240,52,40,40)
                AllyLabel1.setFont(QFont('Segoe UI', 14))
                AllyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    AllyID = list(Globals.BattleInfo["Allies"].keys())[0]
                    AllyIndex = list(Globals.BattleObjects["Allies"].keys()).index(AllyID)
                    AllyLabel1.setText(str(AllyIndex))
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    # AllyLabel1.setText("A")
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')


                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Reduce incoming Damage by 1/2<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:grey;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:grey;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = "SR2"
                    SRSlot2.setText(str(SR2))
                try:
                    if SR2 > 0:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                AllyLabel1 =  QLabel(CardNew)
                AllyLabel1.setGeometry(240,52,40,40)
                AllyLabel1.setFont(QFont('Segoe UI', 14))
                AllyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    AllyID = list(Globals.BattleInfo["Allies"].keys())[0]
                    AllyIndex = list(Globals.BattleObjects["Allies"].keys()).index(AllyID)
                    AllyLabel1.setText(str(AllyIndex))
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    AllyLabel1.setText("A")
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Reduce incoming Damage by 1/2<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "Barricade0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')


                SRSlot2 =  QLabel("5", CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = 0
                if SR2 >= 5:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')



                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                AllyLabel1 =  QLabel(CardNew)
                AllyLabel1.setGeometry(240,52,40,40)
                AllyLabel1.setFont(QFont('Segoe UI', 14))
                AllyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

                try:
                    AllyID = list(Globals.BattleInfo["Allies"].keys())[0]
                    AllyIndex = list(Globals.BattleObjects["Allies"].keys()).index(AllyID)
                    AllyLabel1.setText("AllA")
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')
                except:
                    AllyLabel1.setText("AllA")
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                All allies gain <span style="color:red;"><b>{SR1}</b></span> Block<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')


                SRSlot2 =  QLabel("5", CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = "SR2"
                    SRSlot2.setText(str(SR2))
                try:
                    if SR2 >= 5:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')


                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                AllyLabel1 =  QLabel(CardNew)
                AllyLabel1.setGeometry(240,52,40,40)
                AllyLabel1.setFont(QFont('Segoe UI', 14))
                AllyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

                try:
                    AllyID = list(Globals.BattleInfo["Allies"].keys())[0]
                    AllyIndex = list(Globals.BattleObjects["Allies"].keys()).index(AllyID)
                    AllyLabel1.setText("AllA")
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')
                except:
                    AllyLabel1.setText("AllA")
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                All allies gain <span style="color:red;"><b>{SR1}</b></span> Block<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "Feint0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel("5", CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 >= 5:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Discard a card<br>
                Draw <span style="color:red;"><b>{int(SR1/3)}</b></span> cards<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel("5", CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 >= 5:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Discard a card<br>
                Draw <span style="color:red;"><b>{SR1}</b></span> / 3 cards<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "ThrillOfBattle0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel("5", CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 >= 5:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:grey;
                        ''')

                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = 0
                if SR2 > 0:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-left-color:rgb(35,35,35);
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                AllyLabel1 =  QLabel(CardNew)
                AllyLabel1.setGeometry(240,52,40,40)
                AllyLabel1.setFont(QFont('Segoe UI', 14))
                AllyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    AllyID = list(Globals.BattleInfo["Allies"].keys())[0]
                    AllyIndex = list(Globals.BattleObjects["Allies"].keys()).index(AllyID)
                    AllyLabel1.setText("AllA")
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')
                except:
                    AllyLabel1.setText("AllA")
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Draw a card<br>
                Every subsequent attack grants 1 Strength<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel("5", CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 >= 5:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    color:grey;
                    ''')

                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = "SR2"
                    SRSlot2.setText(str(SR2))
                try:
                    if SR2 > 0:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-left-color:rgb(35,35,35);
                    color:grey;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                AllyLabel1 =  QLabel(CardNew)
                AllyLabel1.setGeometry(240,52,40,40)
                AllyLabel1.setFont(QFont('Segoe UI', 14))
                AllyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    AllyID = list(Globals.BattleInfo["Allies"].keys())[0]
                    AllyIndex = list(Globals.BattleObjects["Allies"].keys()).index(AllyID)
                    AllyLabel1.setText("AllA")
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')
                except:
                    AllyLabel1.setText("AllA")
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Draw a card<br>
                Every subsequent attack grants 1 Strength<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "RelentlessForce0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                AllyLabel1 =  QLabel(CardNew)
                AllyLabel1.setGeometry(240,52,40,40)
                AllyLabel1.setFont(QFont('Segoe UI', 14))
                AllyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    if Globals.BattleInfo["Allies"][0] == Parent:
                        AllyLabel1.setText(Globals.BattleInfo["Allies"][0])
                        AllyLabel1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    else:
                        AllyLabel1.setText(Globals.BattleInfo["Allies"][0])
                        AllyLabel1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                except:
                    AllyLabel1.setText(str(Parent))
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Gain 2 D6+2<br>
                Next turn gain 1 Stun<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                AllyLabel1 =  QLabel(CardNew)
                AllyLabel1.setGeometry(240,52,40,40)
                AllyLabel1.setFont(QFont('Segoe UI', 14))
                AllyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    if Globals.BattleInfo["Allies"][0] == Parent:
                        AllyLabel1.setText(Globals.BattleInfo["Allies"][0])
                        AllyLabel1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    else:
                        AllyLabel1.setText(Globals.BattleInfo["Allies"][0])
                        AllyLabel1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                except:
                    AllyLabel1.setText("S")
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Gain 2 D6+2<br>
                Next turn gain 1 Stun<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "SupressionAssault0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = 0
                if SR2 > 0:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyIndex = Globals.BattleInfo["Allies"][0]
                    EnemyLabel1.setText("AllE")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')
                except:
                    EnemyLabel1.setText("AllE")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Apply 1 Vulnerable to all enemies<br>
                Apply 1 Weak to all enemies<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')


                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = "SR2"
                    SRSlot2.setText(str(SR2))
                try:
                    if SR2 > 0:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')


                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

                try:
                    EnemyIndex = Globals.BattleInfo["Allies"][0]
                    EnemyLabel1.setText("AllE")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')
                except:
                    EnemyLabel1.setText("AllE")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Apply 1 Vulnerable to all enemies<br>
                Apply 1 Weak to all enemies<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "EndlessCombat0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                AllyLabel1 =  QLabel(CardNew)
                AllyLabel1.setGeometry(240,52,40,40)
                AllyLabel1.setFont(QFont('Segoe UI', 14))
                AllyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    AllyID = list(Globals.BattleInfo["Allies"].keys())[0]
                    AllyIndex = list(Globals.BattleObjects["Allies"].keys()).index(AllyID)
                    AllyLabel1.setText("AllA")
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')
                except:
                    AllyLabel1.setText("AllA")
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')


                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                For every card Echausted draw one more<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                AllyLabel1 =  QLabel(CardNew)
                AllyLabel1.setGeometry(240,52,40,40)
                AllyLabel1.setFont(QFont('Segoe UI', 14))
                AllyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    AllyID = list(Globals.BattleInfo["Allies"].keys())[0]
                    AllyIndex = list(Globals.BattleObjects["Allies"].keys()).index(AllyID)
                    AllyLabel1.setText("AllA")
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')
                except:
                    AllyLabel1.setText("AllA")
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                For every card Echausted draw one more<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "FinalStand0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                AllyLabel1 =  QLabel(CardNew)
                AllyLabel1.setGeometry(240,52,40,40)
                AllyLabel1.setFont(QFont('Segoe UI', 14))
                AllyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    AllyID = list(Globals.BattleInfo["Allies"].keys())[0]
                    AllyIndex = list(Globals.BattleObjects["Allies"].keys()).index(AllyID)
                    AllyLabel1.setText("AllA")
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')
                except:
                    AllyLabel1.setText("AllA")
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')


                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Gain 3 D8+2<br>
                Exhaust every card this turn<br>
                Next Turn gain 3 Weak and 3 Vulnerable<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            if Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                AllyLabel1 =  QLabel(CardNew)
                AllyLabel1.setGeometry(240,52,40,40)
                AllyLabel1.setFont(QFont('Segoe UI', 14))
                AllyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    AllyID = list(Globals.BattleInfo["Allies"].keys())[0]
                    AllyIndex = list(Globals.BattleObjects["Allies"].keys()).index(AllyID)
                    AllyLabel1.setText("AllA")
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')
                except:
                    AllyLabel1.setText("AllA")
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Gain 3 D8+2<br>
                Exhaust every card this turn<br>
                Next Turn gain 3 Weak and 3 Vulnerable<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "Preparation0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Draw 2 cards<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Draw 2 cards<br>
                </span></p>
                </body></html>
                ''')

                return CardNew

        elif Move == "Guillotine0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel("5", CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                border-right-color:rgb(35,35,35);
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 >= 5:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:grey;
                        ''')

                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                border-right-color:rgb(35,35,35);
                border-left-color:rgb(35,35,35);
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = 0
                if SR2 > 0:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    border-left-color:rgb(35,35,35);
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        border-left-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        border-left-color:rgb(35,35,35);
                        color:grey;
                        ''')

                SRSlot3 =  QLabel(CardNew)
                SRSlot3.setGeometry(90,10,40,40)
                SRSlot3.setFont(QFont('Segoe UI', 14))
                SRSlot3.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot3.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                border-left-color:rgb(35,35,35);
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][2]]
                    SR = SR.Total
                    SR3 = SR
                    SRSlot3.setText(str(SR3))
                except Exception as e:
                    SR3 = 0
                if SR3 > 0:
                    SRSlot3.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-left-color:rgb(35,35,35);
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 3:
                        SRSlot3.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        SRSlot3.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>{SR1 + SR2 + SR3}</b></span> Damage<br>
                If it incapacitates an enemy deal its max health as Mental to all enemies
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel("5", CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                border-right-color:rgb(35,35,35);
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 >= 5:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    color:grey;
                    ''')

                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                border-right-color:rgb(35,35,35);
                border-left-color:rgb(35,35,35);
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = "SR2"
                    SRSlot2.setText(str(SR2))
                try:
                    if SR2 > 0:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        border-left-color:rgb(35,35,35);
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        border-left-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    border-left-color:rgb(35,35,35);
                    color:grey;
                    ''')

                SRSlot3 =  QLabel(CardNew)
                SRSlot3.setGeometry(90,10,40,40)
                SRSlot3.setFont(QFont('Segoe UI', 14))
                SRSlot3.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot3.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                border-left-color:rgb(35,35,35);
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][2]]
                    SR = SR.Total
                    SR3 = SR
                    SRSlot3.setText(str(SR3))
                except Exception as e:
                    SR3 = "SR3"
                    SRSlot3.setText(str(SR3))
                try:
                    if SR3 > 0:
                        SRSlot3.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 3:
                        SRSlot3.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot3.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-left-color:rgb(35,35,35);
                    color:grey;
                    ''')


                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setText("E")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>{SR1} + {SR2} + {SR3}</b></span> Damage<br>
                If it incapacitates an enemy deal its max health as Mental to all enemies
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "ShowOfMight0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                border-right-color:rgb(35,35,35);
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:grey;
                        ''')

                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                border-left-color:rgb(35,35,35);
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = 0
                if SR2 > 0:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-left-color:rgb(35,35,35);
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>{int(SR1 + SR2 - 5)}</b></span> Mental twice<br>
                Apply {int(SR1 / 2)} Fear<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                border-right-color:rgb(35,35,35);
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    color:grey;
                    ''')


                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                border-left-color:rgb(35,35,35);
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = "SR2"
                    SRSlot2.setText(str(SR2))
                try:
                    if SR2 > 0:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-left-color:rgb(35,35,35);
                    color:grey;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setText("E")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>{SR1} + {SR2} - 5</b></span> Mental twice<br>
                Apply {SR1} / 2 Fear<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "FearsomeGaze0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>{SR1}</b></span> Mental<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setText("E")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>{SR1}</b></span> Mental<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "Terrify0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')


                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>{SR1}</b></span> Mental<br>
                Apply 1 Fear<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setText("E")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>{SR1}</b></span> Mental<br>
                Apply 1 Fear<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "LongHunt0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>{SR1}</b></span> Mental<br>
                When you play a card deal 4 Mental<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setText("E")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>{SR1}</b></span> Mental<br>
                When you play a card deal 4 Mental<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "BloodyHorror0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:grey;
                        ''')

                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = 0
                if SR2 > 0:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-left-color:rgb(35,35,35);
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal missing health as Mental<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == 'Details':
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    color:grey;
                    ''')

                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = "SR2"
                    SRSlot2.setText(str(SR2))
                try:
                    if SR2 > 0:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-left-color:rgb(35,35,35);
                    color:grey;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setText("E")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal missing health as Mental<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "PainfullFear0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:grey;
                        ''')

                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                border-right-color:rgb(35,35,35);
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = 0
                if SR2 > 0:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-left-color:rgb(35,35,35);
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:grey;
                        ''')
                    else:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:white;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>{int( (SR1 + SR2) / 2 )}</b></span> Damage every time the target recives Mental<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    color:grey;
                    ''')

                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                border-right-color:rgb(35,35,35);
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = "SR2"
                    SRSlot2.setText(str(SR2))
                try:
                    if SR2 > 0:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:grey;
                        ''')
                    else:
                        raise
                except:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-left-color:rgb(35,35,35);
                    color:white;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setText("E")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')

                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>{SR1} + {SR2}</b></span> / 2 Damage every time the target recives Mental<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "CripplingHorror0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:grey;
                        ''')

                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = 0
                if SR2 > 0:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-left-color:rgb(35,35,35);
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:grey;
                        ''')
                    else:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:white;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                If the target has <span style="color:red;"><b>{int( (SR1 + SR2) * 1.5 )}</b></span> or less mental, stun them<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-right-color:rgb(35,35,35);
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-right-color:rgb(35,35,35);
                    color:grey;
                    ''')

                SRSlot2 =  QLabel(CardNew)
                SRSlot2.setGeometry(50,10,40,40)
                SRSlot2.setFont(QFont('Segoe UI', 14))
                SRSlot2.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot2.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][1]]
                    SR = SR.Total
                    SR2 = SR
                    SRSlot2.setText(str(SR2))
                except Exception as e:
                    SR2 = "SR2"
                    SRSlot2.setText(str(SR2))
                try:
                    if SR2 > 0:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 2:
                        SRSlot2.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        border-left-color:rgb(35,35,35);
                        color:grey;
                        ''')
                    else:
                        raise
                except:
                    SRSlot2.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    border-left-color:rgb(35,35,35);
                    color:white;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setText("E")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText(f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                If the target has <span style="color:red;"><b>{SR1} + {SR2}</b></span> * 1.5 or less mental, stun them<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "MassPanic0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                If the target has Fear, apply 1 Fear to every enemy<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setText("E")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                If the target has Fear, apply 1 Fear to every enemy<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "ShakySteps0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                If the enemy has Fear, apply 1 Weak and Vulnerable<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setText("E")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                If the enemy has Fear, apply 1 Weak and Vulnerable<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "Unyielding0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                AllyLabel1 =  QLabel(CardNew)
                AllyLabel1.setGeometry(240,52,40,40)
                AllyLabel1.setFont(QFont('Segoe UI', 14))
                AllyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

                try:
                    AllyID = list(Globals.BattleInfo["Allies"].keys())[0]
                    AllyIndex = list(Globals.BattleObjects["Allies"].keys()).index(AllyID)
                    AllyLabel1.setText(str(AllyIndex))
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Upon being hit deal 3 Mental<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                AllyLabel1 =  QLabel(CardNew)
                AllyLabel1.setGeometry(240,52,40,40)
                AllyLabel1.setFont(QFont('Segoe UI', 14))
                AllyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    AllyID = list(Globals.BattleInfo["Allies"].keys())[0]
                    AllyIndex = list(Globals.BattleObjects["Allies"].keys()).index(AllyID)
                    AllyLabel1.setText(str(AllyIndex))
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    AllyLabel1.setText("A")
                    AllyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Upon being hit deal 3 Mental<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "Nightmares0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')


                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Draw two cards<br>
                If the enemy has Fear gain 1D8+2<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')


                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setText("E")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Draw two cards<br>
                If the enemy has Fear gain 1D8+2<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "PreyInstincts0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel("5", CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 >= 5:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Apply 1 Fear to every enemy Damaged this turn.<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel("5", CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 >= 5:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Apply 1 Fear to every enemy Damaged this turn.<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
        elif Move == "Intimidate0":
            if Type == "Normal":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = 0
                if SR1 > 0:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                else:
                    if len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:grey;
                        ''')

                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Randomly change enemy target<br>
                </span></p>
                </body></html>
                ''')

                return CardNew
            elif Type == "Details":
                CardNew = QWidget()
                CardNew.setGeometry(500,100,290,445)
                CardNew.setStyleSheet('''
                QWidget{
                  background-color:rgb(23, 23, 23);
                }
                .QWidget{
                  border: 1px solid yellow
                }
                ''')

                SRSlot1 =  QLabel(CardNew)
                SRSlot1.setGeometry(10,10,40,40)
                SRSlot1.setFont(QFont('Segoe UI', 14))
                SRSlot1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                SRSlot1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                try:
                    SR = Globals.SkillRolls[Globals.BattleInfo["SR"][0]]
                    SR = SR.Total
                    SR1 = SR
                    SRSlot1.setText(str(SR1))
                except Exception as e:
                    SR1 = "SR1"
                    SRSlot1.setText(str(SR1))
                try:
                    if SR1 > 0:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:yellow;
                        ''')
                    elif len(Globals.BattleInfo["SR"]) == 1:
                        SRSlot1.setStyleSheet('''
                        background-color:rgb(35,35,35);
                        border: 2px solid black;
                        color:red;
                        ''')
                    else:
                        raise
                except:
                    SRSlot1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:grey;
                    ''')


                ParentLabel1 =  QLabel(CardNew)
                ParentLabel1.setGeometry(10,52,40,40)
                ParentLabel1.setFont(QFont('Segoe UI', 14))
                ParentLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                ParentLabel1.setStyleSheet('''
                background-color:rgb(35,35,35);
                border: 2px solid black;
                color:white;
                ''')
                ParentLabel1.setText(str(Parent))

                EnemyLabel1 =  QLabel(CardNew)
                EnemyLabel1.setGeometry(240,52,40,40)
                EnemyLabel1.setFont(QFont('Segoe UI', 14))
                EnemyLabel1.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)
                try:
                    # EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    # EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyID = list(Globals.BattleInfo["Enemies"].keys())[0]
                    EnemyIndex = list(Globals.BattleObjects["Enemies"].keys()).index(EnemyID)
                    EnemyLabel1.setText(str(EnemyIndex))
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:yellow;
                    ''')
                except:
                    EnemyLabel1.setText("E")
                    EnemyLabel1.setStyleSheet('''
                    background-color:rgb(35,35,35);
                    border: 2px solid black;
                    color:red;
                    ''')

                CardTypeLabel = QLabel(CardNew)
                CardTypeLabel.setGeometry(240,10,40,40)
                CardTypeLabel.setScaledContents(True)
                CardTypeLabel.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/Attack.png")
                imagepix = QPixmap.fromImage(image)
                CardTypeLabel.setPixmap(imagepix)

                CardImage = QLabel(CardNew)
                CardImage.setGeometry(70,60,150,150)
                CardImage.setScaledContents(True)
                CardImage.setStyleSheet('''
                background-color:rgb(35,35,35);
                ''')
                image = QImage("Resources/CombatResources/AttackCard.png")
                imagepix = QPixmap.fromImage(image)
                CardImage.setPixmap(imagepix)

                CardText = QLabel(CardNew)
                CardText.setFont(QFont('Segoe UI', 11))
                CardText.setGeometry(10,220,270,210)
                CardText.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
                CardText.setWordWrap(True)
                CardText.setStyleSheet('''
                border:0px solid black
                ''')
                CardText.setText('''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Randomly change enemy target<br>
                </span></p>
                </body></html>
                ''')

                return CardNew

    except Exception as e:
        Log(3, "ERROR getCard", e, Attack, Type)

def getAnimationID():
    try:
        ID = max(Globals.AnimationData.keys()) + 1
    except:
        ID = 0
    Globals.AnimationData[ID] = {}
    return ID
def AttackAnimation(self, AnimationID, Cast):
    Data = Globals.AnimationData[AnimationID]
    try:
        try:
            if Data["Target"] in list(Globals.BattleObjects["Enemies"].keys()):
                Type = "Enemies"
            elif Data["Target"] in list(Globals.BattleObjects["Allies"].keys()):
                Type = "Allies"
        except:
            ""
        if Data["AttackID"] == "Strike0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))

                Globals.Threads[ID]["Thread"].start()

            elif Cast == 1:
                Globals.AnimationData[AnimationID]["Thread"].ping.emit()
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage("Resources/CombatResources/AttackEffect1.png")
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "HeavyStrike0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))

                Globals.Threads[ID]["Thread"].start()

            elif Cast == 1:
                Globals.AnimationData[AnimationID]["Thread"].ping.emit()
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage("Resources/CombatResources/AttackEffect3.png")
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "Bloodlust0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                AnimationList = Globals.AnimationData[AnimationID]["Animation"]
                for Animation in AnimationList:
                    Target = Animation["Target"]
                    ImgName = Animation["ImgName"]
                    Sleep = Animation["Sleep"]
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["ImgName"] = ImgName
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(Sleep)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage(f'''Resources/CombatResources/{Globals.AnimationData[AnimationID]["ImgName"]}.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "ShowOfForce0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                AnimationList = Globals.AnimationData[AnimationID]["Animation"]
                for Animation in AnimationList:
                    Target = Animation["Target"]
                    ImgName = Animation["ImgName"]
                    Sleep = Animation["Sleep"]
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["ImgName"] = ImgName
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(Sleep)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage(f'''Resources/CombatResources/{Globals.AnimationData[AnimationID]["ImgName"]}.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "FlurryOfBlows0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                AnimationList = Globals.AnimationData[AnimationID]["Animation"]
                for Target in Globals.AnimationData[AnimationID]["Targets"]:
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(0.15)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage('''Resources/CombatResources/AttackEffect1.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "TauntingBlow0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                AnimationList = Globals.AnimationData[AnimationID]["Animation"]
                for Animation in AnimationList:
                    Target = Animation["Target"]
                    ImgName = Animation["ImgName"]
                    Sleep = Animation["Sleep"]
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["ImgName"] = ImgName
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(Sleep)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage(f'''Resources/CombatResources/{Globals.AnimationData[AnimationID]["ImgName"]}.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "CheapStrike0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                AnimationList = Globals.AnimationData[AnimationID]["Animation"]
                for Animation in AnimationList:
                    Target = Animation["Target"]
                    ImgName = Animation["ImgName"]
                    Sleep = Animation["Sleep"]
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["ImgName"] = ImgName
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(Sleep)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage(f'''Resources/CombatResources/{Globals.AnimationData[AnimationID]["ImgName"]}.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "BrokenGuard0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                AnimationList = Globals.AnimationData[AnimationID]["Animation"]
                for Animation in AnimationList:
                    Target = Animation["Target"]
                    ImgName = Animation["ImgName"]
                    Sleep = Animation["Sleep"]
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["ImgName"] = ImgName
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(Sleep)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage(f'''Resources/CombatResources/{Globals.AnimationData[AnimationID]["ImgName"]}.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "DisarmingStrike0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                AnimationList = Globals.AnimationData[AnimationID]["Animation"]
                for Animation in AnimationList:
                    Target = Animation["Target"]
                    ImgName = Animation["ImgName"]
                    Sleep = Animation["Sleep"]
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["ImgName"] = ImgName
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(Sleep)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage(f'''Resources/CombatResources/{Globals.AnimationData[AnimationID]["ImgName"]}.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "Jab0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))

                Globals.Threads[ID]["Thread"].start()

            elif Cast == 1:
                Globals.AnimationData[AnimationID]["Thread"].ping.emit()
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage("Resources/CombatResources/PunchEffect1.png")
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "FullCombo0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                AnimationList = Globals.AnimationData[AnimationID]["Animation"]
                for Target in Globals.AnimationData[AnimationID]["Targets"]:
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(0.15)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage('''Resources/CombatResources/PunchEffect1.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "Swipe0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                AnimationList = Globals.AnimationData[AnimationID]["Animation"]
                for Target in Globals.AnimationData[AnimationID]["Targets"]:
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(0.15)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage('''Resources/CombatResources/AttackEffect4.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "ShieldBreaker0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                AnimationList = Globals.AnimationData[AnimationID]["Animation"]
                for Animation in AnimationList:
                    Target = Animation["Target"]
                    ImgName = Animation["ImgName"]
                    Sleep = Animation["Sleep"]
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["ImgName"] = ImgName
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(Sleep)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage(f'''Resources/CombatResources/{Globals.AnimationData[AnimationID]["ImgName"]}.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "ScorchedLand0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                AnimationList = Globals.AnimationData[AnimationID]["Animation"]
                for Target in Globals.AnimationData[AnimationID]["Targets"]:
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(0.15)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage('''Resources/CombatResources/Flame.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "Charge0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))

                Globals.Threads[ID]["Thread"].start()

            elif Cast == 1:
                Globals.AnimationData[AnimationID]["Thread"].ping.emit()
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage("Resources/CombatResources/ShieldBash.png")
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)


        elif Data["AttackID"] == "Defend0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))

                Globals.Threads[ID]["Thread"].start()

            elif Cast == 1:
                Globals.AnimationData[AnimationID]["Thread"].ping.emit()
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage("Resources/CombatResources/Shield1.png")
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "Parry0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                AnimationList = Globals.AnimationData[AnimationID]["Animation"]
                for Animation in AnimationList:
                    Target = Animation["Target"]
                    ImgName = Animation["ImgName"]
                    Sleep = Animation["Sleep"]
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["ImgName"] = ImgName
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(Sleep)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage(f'''Resources/CombatResources/{Globals.AnimationData[AnimationID]["ImgName"]}.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "Counter0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                AnimationList = Globals.AnimationData[AnimationID]["Animation"]
                for Animation in AnimationList:
                    Target = Animation["Target"]
                    ImgName = Animation["ImgName"]
                    Sleep = Animation["Sleep"]
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["ImgName"] = ImgName
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(Sleep)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage(f'''Resources/CombatResources/{Globals.AnimationData[AnimationID]["ImgName"]}.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "Concentrate0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))

                Globals.Threads[ID]["Thread"].start()

            elif Cast == 1:
                Globals.AnimationData[AnimationID]["Thread"].ping.emit()
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage("Resources/CombatResources/Buff1.png")
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "HunkerDown0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                AnimationList = Globals.AnimationData[AnimationID]["Animation"]
                for Animation in AnimationList:
                    Target = Animation["Target"]
                    ImgName = Animation["ImgName"]
                    Sleep = Animation["Sleep"]
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["ImgName"] = ImgName
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(Sleep)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage(f'''Resources/CombatResources/{Globals.AnimationData[AnimationID]["ImgName"]}.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "Barricade0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                AnimationList = Globals.AnimationData[AnimationID]["Animation"]
                for Target in Globals.AnimationData[AnimationID]["Targets"]:
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(0.15)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage('''Resources/CombatResources/Shield1.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "Feint0":
            ""
        elif Data["AttackID"] == "ThrillOfBattle0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                for Target in Globals.AnimationData[AnimationID]["Targets"]:
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(0.15)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage('''Resources/CombatResources/Buff1.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "RelentlessForce0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                AnimationList = Globals.AnimationData[AnimationID]["Animation"]
                for Animation in AnimationList:
                    Target = Animation["Target"]
                    ImgName = Animation["ImgName"]
                    Sleep = Animation["Sleep"]
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["ImgName"] = ImgName
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(Sleep)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage(f'''Resources/CombatResources/{Globals.AnimationData[AnimationID]["ImgName"]}.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "SupressionAssault0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                AnimationList = Globals.AnimationData[AnimationID]["Animation"]
                for Animation in AnimationList:
                    Target = Animation["Target"]
                    ImgName = Animation["ImgName"]
                    Sleep = Animation["Sleep"]
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["ImgName"] = ImgName
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(Sleep)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage(f'''Resources/CombatResources/{Globals.AnimationData[AnimationID]["ImgName"]}.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "EndlessCombat0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                for Target in Globals.AnimationData[AnimationID]["Targets"]:
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(0.15)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage('''Resources/CombatResources/Buff1.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "FinalStand0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                for Target in Globals.AnimationData[AnimationID]["Targets"]:
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(0.15)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage('''Resources/CombatResources/Buff1.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "Preparation0":
            ""


        elif Data["AttackID"] == "FearsomeGaze0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))

                Globals.Threads[ID]["Thread"].start()

            elif Cast == 1:
                Globals.AnimationData[AnimationID]["Thread"].ping.emit()
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage("Resources/CombatResources/Gaze1.png")
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "Guillotine0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                AnimationList = Globals.AnimationData[AnimationID]["Animation"]
                for Animation in AnimationList:
                    Target = Animation["Target"]
                    ImgName = Animation["ImgName"]
                    Sleep = Animation["Sleep"]
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["ImgName"] = ImgName
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(Sleep)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage(f'''Resources/CombatResources/{Globals.AnimationData[AnimationID]["ImgName"]}.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "ShowOfMight0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                AnimationList = Globals.AnimationData[AnimationID]["Animation"]
                for Animation in AnimationList:
                    Target = Animation["Target"]
                    ImgName = Animation["ImgName"]
                    Sleep = Animation["Sleep"]
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["ImgName"] = ImgName
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(Sleep)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage(f'''Resources/CombatResources/{Globals.AnimationData[AnimationID]["ImgName"]}.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "Terrify0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                AnimationList = Globals.AnimationData[AnimationID]["Animation"]
                for Animation in AnimationList:
                    Target = Animation["Target"]
                    ImgName = Animation["ImgName"]
                    Sleep = Animation["Sleep"]
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["ImgName"] = ImgName
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(Sleep)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage(f'''Resources/CombatResources/{Globals.AnimationData[AnimationID]["ImgName"]}.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "CripplingHorror0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))

                Globals.Threads[ID]["Thread"].start()

            elif Cast == 1:
                Globals.AnimationData[AnimationID]["Thread"].ping.emit()
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage("Resources/CombatResources/DeBuff2.png")
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "Overkill0":
            ""
        elif Data["AttackID"] == "MassPanic0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                AnimationList = Globals.AnimationData[AnimationID]["Animation"]
                for Target in Globals.AnimationData[AnimationID]["Targets"]:
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(0.15)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage('''Resources/CombatResources/Fear1.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "LongHunt0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))

                Globals.Threads[ID]["Thread"].start()

            elif Cast == 1:
                Globals.AnimationData[AnimationID]["Thread"].ping.emit()
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage("Resources/CombatResources/DeBuff2.png")
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "ShakySteps0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                AnimationList = Globals.AnimationData[AnimationID]["Animation"]
                for Animation in AnimationList:
                    Target = Animation["Target"]
                    ImgName = Animation["ImgName"]
                    Sleep = Animation["Sleep"]
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["ImgName"] = ImgName
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(Sleep)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage(f'''Resources/CombatResources/{Globals.AnimationData[AnimationID]["ImgName"]}.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "BloodyHorror0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))

                Globals.Threads[ID]["Thread"].start()

            elif Cast == 1:
                Globals.AnimationData[AnimationID]["Thread"].ping.emit()
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage("Resources/CombatResources/Fear1.png")
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "Unyielding0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))

                Globals.Threads[ID]["Thread"].start()

            elif Cast == 1:
                Globals.AnimationData[AnimationID]["Thread"].ping.emit()
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage("Resources/CombatResources/Buff1.png")
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "Nightmares0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))

                Globals.Threads[ID]["Thread"].start()

            elif Cast == 1:
                Globals.AnimationData[AnimationID]["Thread"].ping.emit()
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage("Resources/CombatResources/DeBuff2.png")
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "PreyInstincts0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))
                Globals.Threads[ID]["Thread"].start()
            elif Cast == 1:
                AnimationList = Globals.AnimationData[AnimationID]["Animation"]
                for Target in Globals.AnimationData[AnimationID]["Targets"]:
                    Globals.AnimationData[AnimationID]["Target"] = Target
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                    sleep(0.15)
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage('''Resources/CombatResources/Buff1.png''')
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "Intimidate0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))

                Globals.Threads[ID]["Thread"].start()

            elif Cast == 1:
                Globals.AnimationData[AnimationID]["Thread"].ping.emit()
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage("Resources/CombatResources/Gaze1.png")
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["AttackID"] == "PainfullFear0":
            if Cast == 0:
                try:
                    ID = max(list(Globals.Threads.keys()))
                    ID += 1
                except:
                    ID = 0
                Globals.AnimationData[AnimationID]["ThreadID"] = ID
                Cast = 1
                Globals.Threads[ID] = {}
                Globals.Threads[ID]["Thread"] = QThread()
                Globals.Threads[ID]["Worker"] = Worker(AttackAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: AttackAnimation(self, AnimationID, Cast))

                Globals.Threads[ID]["Thread"].start()

            elif Cast == 1:
                Globals.AnimationData[AnimationID]["Thread"].ping.emit()
            elif Cast == 2:
                Target = Globals.AnimationData[AnimationID]["Target"]
                Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                BRX = TLX + Width - 100
                BRY = TLY + Height - 100

                RN1 = random.randint(TLX, BRX)
                RN2 = random.randint(TLY, BRY)
                widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage("Resources/CombatResources/DeBuff2.png")
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)



    except Exception as e:
        if Data["Target"] == '' or Data["Targets"] == []:
            Log(0, "ERROR ATTACK ANIMATION NO TARGET", e, Data)
        else:
            Log(2, "ERROR ATTACK ANIMATION", e, Data)

def AttackTrigger(Card):
    Button = Card[0]
    Attack = Card[1]
    try:
        Move = Attack["AttackID"]
        self = Globals.Layouts["BattleMenu"]
        Parent = Attack["Parent"]
        Source = Globals.Decks[os.path.basename(__file__)[:-3]]

        # FOR EASE OF MAKING THE ATTACKS
        try:
            SR1 = 0
            SR2 = 0
            SR3 = 0
            SR4 = 0
            SR5 = 0
            SR6 = 0
            SR7 = 0
            SR8 = 0
            SR9 = 0
            SR1 = Globals.SkillRolls[Globals.BattleInfo["SR"][0]].Total
            SR2 = Globals.SkillRolls[Globals.BattleInfo["SR"][1]].Total
            SR3 = Globals.SkillRolls[Globals.BattleInfo["SR"][2]].Total
            SR4 = Globals.SkillRolls[Globals.BattleInfo["SR"][3]].Total
            SR5 = Globals.SkillRolls[Globals.BattleInfo["SR"][4]].Total
            SR6 = Globals.SkillRolls[Globals.BattleInfo["SR"][5]].Total
            SR7 = Globals.SkillRolls[Globals.BattleInfo["SR"][6]].Total
            SR8 = Globals.SkillRolls[Globals.BattleInfo["SR"][7]].Total
            SR9 = Globals.SkillRolls[Globals.BattleInfo["SR"][8]].Total
        except:
            ""

        AvailableTargets = []
        for EnemyID in Globals.BattleObjects["Enemies"]:
            Enemy = Globals.BattleObjects["Enemies"][EnemyID]["Object"]
            if Enemy.Status == "Alive":
                AvailableTargets.append(EnemyID)

        AvailableAllies = []
        for AllyID in Globals.BattleObjects["Allies"]:
            Ally = Globals.BattleObjects["Allies"][AllyID]["Object"]
            if Ally.Status == "Alive":
                AvailableAllies.append(AllyID)
        if Move == "Strike0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Target = list(Globals.BattleInfo["Enemies"].keys())[0]
            AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":50, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "HeavyStrike0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Damage = SR1 + SR2
            Target = list(Globals.BattleInfo["Enemies"].keys())[0]
            AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":Damage, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            if len(Globals.BattleInfo["SR"]) >= 2:
                Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0], Globals.BattleInfo["SR"][1] ])
            else:
                Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "Bloodlust0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Damage = SR1 + SR2
            Times = int((SR3 / 2)//1)
            try:
                for i in range(Times):
                    Target = random.choice(AvailableTargets)
                    AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":Damage, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
                    Globals.Layouts["BattleMenu"].CastAttack( AttackData )
            except Exception as e:
                ""
            Healing = int((Globals.AnimationData[AnimationID]["DmgDealt"] / 2)//1)
            AttackData = { "Target":Parent, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1, "HealingEffect":1 }, "Source":Source, "Damage":0, "Healing":Healing, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0], Globals.BattleInfo["SR"][1], Globals.BattleInfo["SR"][2] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "ShowOfForce0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Target = list(Globals.BattleInfo["Enemies"].keys())[0]
            Damage = SR1
            AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":Damage, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "FlurryOfBlows0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Damage = SR1
            Times = SR2
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move}
            for i in range(Times):
                Target = list(Globals.BattleInfo["Enemies"].keys())[0]
                AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":Damage, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
                Globals.Layouts["BattleMenu"].CastAttack( AttackData )


            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0], Globals.BattleInfo["SR"][1], Globals.BattleInfo["SR"][2] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "TauntingBlow0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Target = list(Globals.BattleInfo["Enemies"].keys())[0]
            Damage = SR1
            # Globals.Layouts["BattleMenu"].CastAttack( Attack, Button, { "Damage":Damage, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Target":Target, "Effects":{}, "Flags":{"Confirmation":1}, "AnimationID":AnimationID } )
            AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":Damage, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "CheapStrike0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Target = list(Globals.BattleInfo["Enemies"].keys())[0]
            VulnerableEffect = {"ID":"Vulnerable","Level":1,"Data":{}}
            AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":4, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"Vulnerable":VulnerableEffect}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "BrokenGuard0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Target = list(Globals.BattleInfo["Enemies"].keys())[0]
            try:
                Vulnerable = Globals.BattleObjects["Enemies"][Target]["Object"].Effects["Vulnerable"]["Level"]
            except:
                Vulnerable = 0
            Damage = (Vulnerable * 4)
            AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1, "Attack":1 }, "Source":Source, "Damage":Damage, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            VulnerableEffect = {"ID":"Vulnerable","Level":Vulnerable,"Data":{}}
            AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "Effect":1, "EffectsTrigger":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"Vulnerable":VulnerableEffect}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0], Globals.BattleInfo["SR"][1] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "DisarmingStrike0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Target = list(Globals.BattleInfo["Enemies"].keys())[0]
            WeakEffect = {"ID":"Weak","Level":1,"Data":{}}
            AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":5, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"Weak":WeakEffect}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "Jab0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Target = list(Globals.BattleInfo["Enemies"].keys())[0]
            AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":4, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            # Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # EXHAUST OF THE CARD
            Globals.Layouts["BattleMenu"].ExhaustCard(Attack, Button)

            # SUMMONS THE NEW CARD ON TOP OF THE DRAWDECK
            Globals.Layouts["BattleMenu"].SummonCard(Attack, "DrawDeck", "Random")
        elif Move == "FullCombo0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Damage = 8
            Times = 3
            Target = list(Globals.BattleInfo["Enemies"].keys())[0]
            for i in range(Times):
                AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":Damage, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
                Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0], Globals.BattleInfo["SR"][1], Globals.BattleInfo["SR"][2] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "Swipe0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Damage = SR1
            if AvailableTargets != []:
                for Target in AvailableTargets:
                    AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":Damage, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
                    Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0], Globals.BattleInfo["SR"][1] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "ShieldBreaker0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Target = list(Globals.BattleInfo["Enemies"].keys())[0]
            EnemyShield = Globals.BattleObjects["Enemies"][Target]["Object"].Shield
            AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1, "ShieldBreak":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":EnemyShield, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0], Globals.BattleInfo["SR"][1] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "ScorchedLand0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            for Target in AvailableTargets:
                AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":25, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
                Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            for Ally in AvailableAllies:
                AttackData = { "Target":Ally, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":8, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
                Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0], Globals.BattleInfo["SR"][1] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "Charge0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            try:
                Shield = Globals.BattleObjects["Allies"][Parent]["Object"].Shield
            except Exception as e:
                Shield = 0
            Target = list(Globals.BattleInfo["Enemies"].keys())[0]
            # Globals.Layouts["BattleMenu"].CastAttack( Attack, Button, { "Damage":Shield, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Target":Target, "Effects":{}, "Flags":{"Confirmation":1}, "AnimationID":AnimationID } )
            AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":Shield, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")


        elif Move == "Defend0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Target = list(Globals.BattleInfo["Allies"].keys())[0]
            AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":5, "MentalDamage":0, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )


            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "Parry0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Parry = SR1 + SR2
            Target = list(Globals.BattleInfo["Allies"].keys())[0]
            ParryEffect = {"ID":"Parry","Level":Parry,"Data":{}}
            AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"Parry":ParryEffect}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            if len(Globals.BattleInfo["SR"]) >= 2:
                Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0], Globals.BattleInfo["SR"][1] ])
            else:
                Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "Counter0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Counter = int((SR1 / 2)//1)
            Target = list(Globals.BattleInfo["Allies"].keys())[0]
            CounterEffect = {"ID":"Counter","Level":Counter,"Data":{}}
            AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":0,"Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"Counter":CounterEffect}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "Concentrate0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            try:
                Target = list(Globals.BattleInfo["Allies"].keys())[0]
            except:
                Target = AvailableAllies[0]
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":Target, "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Bonus = int((SR1 / 2)//1)
            for SR in Globals.SkillRolls:
                Globals.SkillRolls[SR].Bonus += Bonus
                Globals.SkillRolls[SR].Update()

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "HunkerDown0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Target = list(Globals.BattleInfo["Allies"].keys())[0]
            HunkeredEffect = {"ID":"Hunkered","Level":1,"Data":{}}
            AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"Hunkered":HunkeredEffect}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )


            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0], Globals.BattleInfo["SR"][1] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "Barricade0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Shield = SR1
            for Ally in AvailableAllies:
                # Target = list(Globals.BattleInfo["Allies"].keys())[0]
                AttackData = { "Target":Ally, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":Shield, "MentalDamage":0, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
                Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0], Globals.BattleInfo["SR"][1] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "Feint0":
            # TRIGGERING THE ATTACK
            if len(Globals.BattleInfo["Deck"]["CurrentHand"].keys()) >= 2:
                while True:
                    CardID = random.choice(list(Globals.BattleInfo["Deck"]["CurrentHand"].keys()))
                    CardNew = Globals.BattleInfo["Deck"]["CurrentHand"][CardID]
                    if CardNew != Card:
                        Globals.Layouts["BattleMenu"].discardCard(CardNew, "CurrentHand")
                        break

            Bonus = int((SR1 / 3)//1)
            for i in range(Bonus):
                Globals.Layouts["BattleMenu"].drawCard(9)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "ThrillOfBattle0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            ThrillEffect = {"ID":"Thrill","Level":1,"Data":{}}
            for Ally in AvailableAllies:
                AttackData = { "Target":Ally, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"Thrill":ThrillEffect}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
                Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0], Globals.BattleInfo["SR"][1] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "RelentlessForce0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Parent, "ImgName":"Buff1","Sleep":0.15 })
            Roll = {"Upper":7, "Lower":3, "Bonus":0, "Minus":0}
            for i in range(2):
                # SR = random.randint(3,8)
                ID = max(list(Globals.SkillRolls.keys())) + 1
                RN = random.randint(Roll["Lower"], Roll["Upper"])
                SkillObject = SRObject(0, RN, Roll["Lower"], Roll["Upper"], Roll["Bonus"], Roll["Minus"], 0, ID)
                SkillObject.Update()
                Globals.SkillRolls[ID] = SkillObject

            ExhaustedEffect = {"ID":"Exhausted","Level":1,"Data":{}}
            AttackData = { "Target":Parent, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"Exhausted":ExhaustedEffect}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )


            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "SupressionAssault0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            VulnerableEffect = {"ID":"Vulnerable","Level":1,"Data":{}}
            WeakEffect = {"ID":"Weak","Level":1,"Data":{}}
            for Enemy in AvailableTargets:
                AttackData = { "Target":Enemy, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"Vulnerable":VulnerableEffect, "Weak":WeakEffect}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
                Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0], Globals.BattleInfo["SR"][1] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "EndlessCombat0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            EndlessEffect = {"ID":"Endless","Level":1,"Data":{}}
            for AllyID in AvailableAllies:
                AttackData = { "Target":AllyID, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"Endless":EndlessEffect}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
                Globals.Layouts["BattleMenu"].CastAttack( AttackData )


            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "FinalStand0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Roll = {"Upper":9, "Lower":5, "Bonus":0, "Minus":0}
            for i in range(2):
                # SR = random.randint(3,8)
                ID = max(list(Globals.SkillRolls.keys())) + 1
                RN = random.randint(Roll["Lower"], Roll["Upper"])
                SkillObject = SRObject(0, RN, Roll["Lower"], Roll["Upper"], Roll["Bonus"], Roll["Minus"], 0, ID)
                SkillObject.Update()
                Globals.SkillRolls[ID] = SkillObject

            LastStandEffect = {"ID":"LastStand","Level":1,"Data":{}}
            for AllyID in AvailableAllies:
                AttackData = { "Target":AllyID, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"LastStand":LastStandEffect}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
                Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            # Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "Preparation0":
            # TRIGGERING THE ATTACK
            for i in range(2):
                Globals.Layouts["BattleMenu"].drawCard(9)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")


        elif Move == "FearsomeGaze0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Damage = SR1
            Target = list(Globals.BattleInfo["Enemies"].keys())[0]
            AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":Damage, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "Guillotine0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Damage = SR1 + SR2 + SR3
            Target = list(Globals.BattleInfo["Enemies"].keys())[0]
            AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":Damage, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0], Globals.BattleInfo["SR"][1], Globals.BattleInfo["SR"][2] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "ShowOfMight0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Damage = SR1 + SR2 - 5
            if Damage < 0: Damage = 0
            Target = list(Globals.BattleInfo["Enemies"].keys())[0]

            for i in range(2):
                # Globals.Layouts["BattleMenu"].CastAttack( Attack, Button, { "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":Damage, "MentalHealing":0, "Target":Target, "Effects":{}, "Flags":{"Confirmation":1}, "AnimationID":AnimationID } )
                AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":Damage, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
                Globals.Layouts["BattleMenu"].CastAttack( AttackData )


            Fear = int((SR1 / 2)//1)
            FearEffect = {"ID":"Fear","Level":Fear,"Data":{}}
            # Globals.Layouts["BattleMenu"].CastAttack( Attack, Button, { "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Target":Target, "Effects":{"Fear":FearEffect}, "Flags":{"Confirmation":1, "Fear":1}, "AnimationID":AnimationID } )

            AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1, "Fear":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"Fear":FearEffect}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            if len(Globals.BattleInfo["SR"]) >= 2:
                Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0], Globals.BattleInfo["SR"][1] ])
            else:
                Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "Terrify0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Damage = SR1
            Target = list(Globals.BattleInfo["Enemies"].keys())[0]
            AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1, "Mental":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":Damage, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "CripplingHorror0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Damage = int((SR1 + SR2) * 1.5)
            Target = list(Globals.BattleInfo["Enemies"].keys())[0]
            if Globals.BattleObjects["Enemies"][Target]["Object"].Mental <= Damage:
                StunEffect = {"ID":"Stun","Level":1,"Data":{}}
                AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"Stun":StunEffect}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
                Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            if len(Globals.BattleInfo["SR"]) >= 2:
                Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0], Globals.BattleInfo["SR"][1] ])
            else:
                Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "Overkill0":
            ""
            # TODO
            # Target = Globals.BattleInfo["Enemies"][0]
            # Globals.Layouts["BattleMenu"].CastAttack( Attack, Button, { "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Target":Target, "Effects":[("Overkill",1)], "Flags":{"Confirmation":1} } )
        elif Move == "MassPanic0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Target = list(Globals.BattleInfo["Enemies"].keys())[0]
            Effects = Globals.BattleObjects["Enemies"][Target]["Object"].Effects
            try:
                if Effects["Fear"]["Level"] > 0:
                    for Target2 in AvailableTargets:
                        if Target2 != Target:
                            FearEffect = {"ID":"Fear","Level":1,"Data":{}}
                            # Globals.Layouts["BattleMenu"].CastAttack( Attack, Button, { "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Target":Target2, "Effects":{"Fear":FearEffect}, "Flags":{"Confirmation":1}, "AnimationID":AnimationID } )

                            AttackData = { "Target":Target2, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"Fear":FearEffect}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
                            Globals.Layouts["BattleMenu"].CastAttack( AttackData )
            except:
                ""

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "LongHunt0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Damage = SR1
            Target = list(Globals.BattleInfo["Enemies"].keys())[0]
            PreyEffect = {"ID":"Prey","Level":4,"Data":{}}
            AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":Damage, "MentalHealing":0, "Effects":{"Prey":PreyEffect}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "ShakySteps0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Target = list(Globals.BattleInfo["Enemies"].keys())[0]
            Effects = Globals.BattleObjects["Enemies"][Target]["Object"].Effects
            try:
                if Effects["Fear"]["Level"] > 0:
                    VulnerableEffect = {"ID":"Vulnerable","Level":1,"Data":{}}
                    WeakEffect = {"ID":"Weak","Level":1,"Data":{}}
                    AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"Weak":WeakEffect, "Vulnerable":VulnerableEffect}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
                    Globals.Layouts["BattleMenu"].CastAttack( AttackData )
            except:
                ""

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "BloodyHorror0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Target = list(Globals.BattleInfo["Enemies"].keys())[0]
            HP = Globals.BattleObjects["Allies"][Parent]["Object"].HP
            MaxHP = Globals.BattleObjects["Allies"][Parent]["Object"].MaxHP
            Damage = MaxHP - HP
            AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":Damage, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0], Globals.BattleInfo["SR"][1] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "Unyielding0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Target = list(Globals.BattleInfo["Allies"].keys())[0]
            UnyieldingEffect = {"ID":"Unyielding","Level":3,"Data":{}}
            AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"Unyielding":UnyieldingEffect}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "Nightmares0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            for i in range(2):
                Globals.Layouts["BattleMenu"].drawCard(9)
            Target = list(Globals.BattleInfo["Enemies"].keys())[0]
            Effects = Globals.BattleObjects["Enemies"][Target]["Object"].Effects
            try:
                if Effects["Fear"]["Level"] > 0:
                    Roll = {"Upper":7, "Lower":3, "Bonus":0, "Minus":0}
                    ID = max(list(Globals.SkillRolls.keys())) + 1
                    RN = random.randint(Roll["Lower"], Roll["Upper"])
                    SkillObject = SRObject(0, RN, Roll["Lower"], Roll["Upper"], Roll["Bonus"], Roll["Minus"], 0, ID)
                    SkillObject.Update()
                    Globals.SkillRolls[ID] = SkillObject
                    Globals.AnimationData[AnimationID]["Target"] = Target

                    # CALLING FOR THE ANIMATION
                    self = Globals.Layouts["BattleMenu"]
                    AttackAnimation(self, AnimationID, 0)
            except:
                ""

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "PreyInstincts0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            HuntingEffect = {"ID":"Hunting","Level":1,"Data":{}}
            Target = list(Globals.BattleInfo["Allies"].keys())[0]
            AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"Hunting":HuntingEffect}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "Intimidate0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Enemy = list(Globals.BattleInfo["Enemies"].keys())[0]
            CurrentTarget = Globals.BattleObjects["Enemies"][Enemy]["Object"].Target
            if len(AvailableAllies) > 1:
                NewList = AvailableAllies
                NewList.remove(CurrentTarget)
                NewTarget = random.choice(NewList)
                Globals.BattleObjects["Enemies"][Enemy]["Object"].Target = NewTarget

                Globals.AnimationData[AnimationID]["Target"] = Enemy

                # CALLING FOR THE ANIMATION
                self = Globals.Layouts["BattleMenu"]
                AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")
        elif Move == "PainfullFear0":
            # SETTING INITIAL DATA FOR THE ANIMATIONS
            AnimationID = getAnimationID()
            Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
            Globals.AnimationData[AnimationID] = Data

            # TRIGGERING THE ATTACK
            Damage = int(((SR1 + SR2) / 2)//1)
            Target = list(Globals.BattleInfo["Enemies"].keys())[0]
            PainfulMindEffect = {"ID":"PainfulMind","Level":Damage,"Data":{}}
            # Globals.Layouts["BattleMenu"].CastAttack( Attack, Button, { "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Target":Target, "Effects":{"PainfulMind":PainfulMindEffect}, "Flags":{"Confirmation":1}, "AnimationID":AnimationID } )

            AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"PainfulMind":PainfulMindEffect}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
            Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            # CALLING FOR THE ANIMATION
            self = Globals.Layouts["BattleMenu"]
            AttackAnimation(self, AnimationID, 0)

            # EXHAUSTING THE SR USED
            if len(Globals.BattleInfo["SR"]) >= 2:
                Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0], Globals.BattleInfo["SR"][1] ])
            else:
                Globals.Layouts["BattleMenu"].ExhaustSR([ Globals.BattleInfo["SR"][0] ])

            # DISCARDING THE CARD
            Globals.Layouts["BattleMenu"].discardCard(Card, "CurrentHand")

        else:
            print("NAFA", Move)
        Globals.Layouts["BattleMenu"].Refresh()

    except Exception as e:
        Log(4, "ERROR ATTACK TRIGGER,", e, Attack)
def AttackConfirmed(OriginalData, FinalData, Results):
    Move = FinalData["AttackID"]
    Attack = FinalData["OtherData"]["Attack"]
    Button = FinalData["OtherData"]["Button"]
    Source = FinalData["Source"]
    Parent = Attack["Parent"]

    try:
        if Move == "Strike0":
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]
            if Results["DamageDealt"] > 0 or Results["ShieldDamage"] > 0:
                Globals.AnimationData[AnimationID]["Target"] = Target
        elif Move == "HeavyStrike0":
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]
            if Results["DamageDealt"] > 0 or Results["ShieldDamage"] > 0:
                Globals.AnimationData[AnimationID]["Target"] = Target
        elif Move == "Bloodlust0":
            Target = Results["Target"]
            Parent = FinalData["Parent"]
            AnimationID = FinalData["AnimationID"]
            if "HealingEffect" in list(Results["Flags"].keys()):
                if Results["Flags"]["HealingEffect"] == 1:
                    if Results["HealingDealt"] > 0:
                        Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"HealEffect1","Sleep":0.15 })
            else:
                Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"AttackEffect1","Sleep":0.15 })
                Globals.AnimationData[AnimationID]["DmgDealt"] += Results["DamageDealt"]
        elif Move == "ShowOfForce0":
            Target = Results["Target"]
            Parent = FinalData["Parent"]

            AnimationID = FinalData["AnimationID"]
            if "VulnerableEffect" in list(FinalData["Flags"].keys()) and "Vulnerable" in list(Results["EffectsApplied"].keys()):
                if Results["Flags"]["VulnerableEffect"] > 0 and Results["EffectsApplied"]["Vulnerable"]["Level"] > 0:
                    # FLAVOR TEXT FOR APPLYING VULNERABLE
                    Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"Vulnerable","Sleep":0.15 })
                else:
                    ""
            elif "VulnerableEffect" not in list(Results["Flags"].keys()):
                # FLAVOR TEXT FOR DAMAGE
                Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"AttackEffect1","Sleep":0.15 })
                DamageDealt = Results["DamageDealt"]
                Vulnerable = int((Results["DamageDealt"] / 3)//1)
                VulnerableEffect = {"ID":"Vulnerable","Level":Vulnerable,"Data":{}}
                AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1, "VulnerableEffect":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"Vulnerable":VulnerableEffect}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
                Globals.Layouts["BattleMenu"].CastAttack( AttackData )
        elif Move == "FlurryOfBlows0":
            # FLAVOR TEXT FOR DAMAGE
            AnimationID = FinalData["AnimationID"]
            if Results["DamageDealt"] > 0:
                Target = Results["Target"]
                Globals.AnimationData[AnimationID]["Targets"].append(Target)
        elif Move == "TauntingBlow0":
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]

            # FOR DAMAGE
            Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"AttackEffect1","Sleep":0.15 })

            # FOR TAUNT
            if Results["DamageDealt"] > 0 or Results["ShieldDamage"] > 0:
                AttackSource = FinalData["Parent"]
                Enemy = Results["Target"]
                Globals.BattleObjects["Enemies"][Enemy]["Object"].Target = AttackSource
                Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"Taunt","Sleep":0.15 })
        elif Move == "CheapStrike0":
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]

            Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"AttackEffect1","Sleep":0.15 })

            if "Vulnerable" in list(Results["EffectsApplied"].keys()):
                if Results["EffectsApplied"]["Vulnerable"]["Level"] > 0:
                    Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"Vulnerable","Sleep":0.15 })
        elif Move == "BrokenGuard0":
            # FLAVOR TEXT FOR DAMAGE
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]
            if "Attack" in list(Results["Flags"].keys()) and Results["DamageDealt"] > 0:
                Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"AttackEffect5","Sleep":0.15 })
            elif "Effect" in list(Results["Flags"].keys()) and "Vulnerable" in list(Results["EffectsApplied"].keys()):
                if Results["EffectsApplied"]["Vulnerable"]["Level"] > 0:
                    Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"Vulnerable","Sleep":0.15 })
        elif Move == "DisarmingStrike0":
            # FLAVOR TEXT FOR DAMAGE
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]

            if Results["DamageDealt"] > 0 or Results["ShieldDamage"] > 0:
                Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"AttackEffect1","Sleep":0.15 })
            if Results["EffectsApplied"]["Weak"]["Level"] > 0:
                Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"Weak","Sleep":0.15 })
        elif Move == "Jab0":
            # FLAVOR TEXT FOR DAMAGE
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]
            if Results["DamageDealt"] > 0 or Results["ShieldDamage"] > 0:
                Globals.AnimationData[AnimationID]["Target"] = Target
        elif Move == "FullCombo0":
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]
            if Results["DamageDealt"] > 0 or Results["ShieldDamage"] > 0:
                Globals.AnimationData[AnimationID]["Targets"] .append(Target)
        elif Move == "Swipe0":
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]
            if Results["DamageDealt"] > 0 or Results["ShieldDamage"] > 0:
                Globals.AnimationData[AnimationID]["Targets"].append(Target)
        elif Move == "ShieldBreaker0":
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]
            if "ShieldBreak" in  list(Results["Flags"].keys()):
                if Globals.BattleObjects["Enemies"][Target]["Object"].Shield > 0:
                    Globals.BattleObjects["Enemies"][Target]["Object"].Shield = 0

                Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"Vulnerable","Sleep":0.15 })

                Parent = FinalData["Parent"]
                Source = FinalData["Source"]
                Attack = FinalData["OtherData"]["Attack"]
                Button = FinalData["OtherData"]["Button"]
                Damage = Globals.SkillRolls[Globals.BattleInfo["SR"][0]].Total
                AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":Damage, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
                Globals.Layouts["BattleMenu"].CastAttack( AttackData )
            else:
                if Results["DamageDealt"] > 0 or Results["ShieldDamage"] > 0:
                    Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"AttackEffect1","Sleep":0.15 })
        elif Move == "ScorchedLand0":
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]
            if Results["DamageDealt"] > 0 or Results["ShieldDamage"] > 0:
                Globals.AnimationData[AnimationID]["Targets"].append(Target)
        elif Move == "Charge0":
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]
            if Results["DamageDealt"] > 0 or Results["ShieldDamage"] > 0:
                Globals.AnimationData[AnimationID]["Target"] = Target


        elif Move == "Defend0":
            if Results["ShieldApplied"] > 0:
                AnimationID = FinalData["AnimationID"]
                Target = Results["Target"]
                Globals.AnimationData[AnimationID]["Target"] = Target
        elif Move == "Parry0":
            # FLAVOR TEXT FOR DAMAGE
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]

            if Results["EffectsApplied"]["Parry"]["Level"] > 0:
                Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"Parry","Sleep":0.15 })
        elif Move == "Counter0":
            # FLAVOR TEXT FOR DAMAGE
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]

            if Results["EffectsApplied"]["Counter"]["Level"] > 0:
                Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"Thorns","Sleep":0.15 })
        elif Move == "Concentrate0":
            ""
        elif Move == "HunkerDown0":
            # FLAVOR TEXT FOR DAMAGE
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]

            if Results["EffectsApplied"]["Hunkered"]["Level"] > 0:
                Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"Hunker","Sleep":0.15 })
        elif Move == "Barricade0":
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]
            if Results["ShieldApplied"] > 0:
                Globals.AnimationData[AnimationID]["Targets"].append(Target)
        elif Move == "Feint0":
            ""
        elif Move == "ThrillOfBattle0":
            # FLAVOR TEXT FOR DAMAGE
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]

            if Results["EffectsApplied"]["Thrill"]["Level"] > 0:
                Globals.AnimationData[AnimationID]["Targets"].append(Target)
        elif Move == "RelentlessForce0":
            # FLAVOR TEXT FOR DAMAGE
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]

            if Results["EffectsApplied"]["Exhausted"]["Level"] > 0:
                Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"DeBuff2","Sleep":0.15 })
        elif Move == "SupressionAssault0":
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]
            if Results["EffectsApplied"]["Vulnerable"]["Level"] > 0:
                Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"Vulnerable","Sleep":0.15 })
            if Results["EffectsApplied"]["Weak"]["Level"] > 0:
                Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"Weak","Sleep":0.15 })
        elif Move == "EndlessCombat0":
            # FLAVOR TEXT FOR DAMAGE
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]
            try:
                if Results["EffectsApplied"]["Endless"]["Level"] > 0:
                    Globals.AnimationData[AnimationID]["Targets"].append(Target)

                    Parent = Attack["Parent"]
                    Data = {"Parent":Parent, "Effects":{"Endless":{ "ID":"Endless","Level":1,"Data":{} } }, "Flags":{"EffectsTrigger":1}}
                    Globals.Layouts["BattleMenu"].CastUniversalEffect(Data)
            except Exception as e:
                ""
        elif Move == "FinalStand0":
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]
            try:
                if Results["EffectsApplied"]["LastStand"]["Level"] > 0:
                    Globals.AnimationData[AnimationID]["Targets"].append(Target)
            except:
                ""
        elif Move == "Preparation0":
            # FLAVOR TEXT FOR DAMAGE
            ""


        elif Move == "FearsomeGaze0":
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]
            if Results["MentalDealt"] > 0:
                Globals.AnimationData[AnimationID]["Target"] = Target
        elif Move == "Guillotine0":
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]

            if "Fear" not in list(Results["Flags"].keys()):
                Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"AttackEffect5","Sleep":0.15 })
                if Globals.BattleObjects["Enemies"][Target]["Object"].Status == "Dead":
                    Damage = Globals.BattleObjects["Enemies"][Target]["Object"].MaxHP
                    for EnemyID in Globals.BattleObjects["Enemies"]:
                        if Globals.BattleObjects["Enemies"][EnemyID]["Object"].Status == "Alive":
                            Parent = Attack["Parent"]
                            AttackData = { "Target":EnemyID, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1, "Fear":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":Damage, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
                            Globals.Layouts["BattleMenu"].CastAttack( AttackData )



            else:
                Target = Results["Target"]
                if Results["MentalDealt"] > 0:
                    Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"Fear1","Sleep":0.15 })
        elif Move == "ShowOfMight0":
            AnimationID = FinalData["AnimationID"]
            if "Fear" not in list(Results["Flags"].keys()):
                Target = Results["Target"]
                Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"Gaze1","Sleep":0.15 })
            else:
                Target = Results["Target"]
                Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"Fear1","Sleep":0.15 })
        elif Move == "Terrify0":
            AnimationID = FinalData["AnimationID"]
            if "Mental" in list(Results["Flags"].keys()):
                if Results["MentalDealt"] > 0:
                    Target = Results["Target"]
                    Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"Fear1","Sleep":0.15 })
                    FearEffect = {"ID":"Fear","Level":2,"Data":{}}
                    AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"Fear":FearEffect}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack, "Button":Button} }
                    Globals.Layouts["BattleMenu"].CastAttack( AttackData )

            elif "Mental" not in list(Results["Flags"].keys()):
                try:
                    if Results["EffectsApplied"]["Fear"]["Level"] > 0:
                        Target = Results["Target"]
                        Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"Gaze1","Sleep":0.15 })
                except:
                    ""
        elif Move == "CripplingHorror0":
            try:
                if Results["EffectsApplied"]["Stun"]["Level"] > 0:
                    AnimationID = FinalData["AnimationID"]
                    Target = Results["Target"]
                    Globals.AnimationData[AnimationID]["Target"] = Target
            except:
                ""
        elif Move == "Overkill0":
            # FLAVOR TEXT FOR DAMAGE
            ""
        elif Move == "MassPanic0":
            try:
                if Results["EffectsApplied"]["Fear"]["Level"] > 0:
                    AnimationID = FinalData["AnimationID"]
                    Target = Results["Target"]
                    Globals.AnimationData[AnimationID]["Targets"].append(Target)
            except:
                ""
        elif Move == "LongHunt0":
            try:
                if Results["EffectsApplied"]["Prey"]["Level"] > 0:
                    AnimationID = FinalData["AnimationID"]
                    Target = Results["Target"]
                    Globals.AnimationData[AnimationID]["Target"] = Target
            except:
                ""
        elif Move == "ShakySteps0":
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]
            if Results["EffectsApplied"]["Vulnerable"]["Level"] > 0:
                Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"Vulnerable","Sleep":0.15 })
            if Results["EffectsApplied"]["Weak"]["Level"] > 0:
                Globals.AnimationData[AnimationID]["Animation"].append({ "Target":Target, "ImgName":"Weak","Sleep":0.15 })
        elif Move == "BloodyHorror0":
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]
            if Results["MentalDealt"] > 0:
                Globals.AnimationData[AnimationID]["Target"] = Target
        elif Move == "Unyielding0":
            AnimationID = FinalData["AnimationID"]
            Target = Results["Target"]
            if Results["EffectsApplied"]["Unyielding"]["Level"] > 0:
                Globals.AnimationData[AnimationID]["Target"] = Target
        elif Move == "Nightmares0":
            # FLAVOR TEXT FOR DAMAGE
            ""
        elif Move == "PreyInstincts0":
            try:
                if Results["EffectsApplied"]["Hunting"]["Level"] > 0:
                    Target = Results["Target"]
                    AnimationID = FinalData["AnimationID"]
                    Globals.AnimationData[AnimationID]["Targets"].append(Target)
            except:
                ""
        elif Move == "Intimidate":
            # FLAVOR TEXT FOR DAMAGE
            ""
        elif Move == "PainfullFear0":
            try:
                if Results["EffectsApplied"]["PainfulMind"]["Level"] > 0:
                    Target = Results["Target"]
                    AnimationID = FinalData["AnimationID"]
                    Globals.AnimationData[AnimationID]["Target"] = Target
            except:
                ""




    except Exception as e:
        Log(4,"ERROR ATTACK CONFIRMED,", e, Attack)
    return OriginalData, FinalData, Results


    ""

def checkStatus(Attack, Button):
    Move = Attack["AttackID"]
    Parent = Attack["Parent"]
    # AmountOfAllies    len(Globals.BattleInfo["Allies"]) == 0
    # AmountOfEnemis    len(Globals.BattleInfo["Enemies"]) == 0
    # TargetSelf        Globals.BattleInfo["Allies"][0] == Parent
    # SRList = Globals.SkillRolls[Globals.BattleInfo["SR"][2]]
    SRList = []
    for SR in Globals.BattleInfo["SR"]:
        SRList.append(Globals.SkillRolls[SR])
    EnemiesAmount = len(list(Globals.BattleInfo["Enemies"].keys()) )
    AlliesAmount = len(Globals.BattleInfo["Allies"])
    SRAmount = len(SRList)
    AlliesList = list(Globals.BattleInfo["Allies"].keys())

    try:
        if Move == "Strike0":
            if SRAmount > 0 and EnemiesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "HeavyStrike0":
            if SRList[0].Total >= 5 and EnemiesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "Bloodlust0":
            if SRAmount >= 3: Button.Available = 1
            else: Button.Available = 0
        elif Move == "ShowOfForce0":
            if SRList[0].Total >= 7 and EnemiesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "FlurryOfBlows0":
            if SRList[2].Total >= 4 and SRAmount >= 3 and EnemiesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "TauntingBlow0":
            if SRAmount > 0 and EnemiesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "CheapStrike0":
            if SRAmount > 0 and EnemiesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "BrokenGuard0":
            if SRAmount >= 2 and SRList[0].Total >= 5 and EnemiesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "DisarmingStrike0":
            if SRList[0].Total > 0 and EnemiesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "Jab0":
            if EnemiesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "FullCombo0":
            if SRAmount >= 3 and EnemiesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "Swipe0":
            if SRAmount >= 2: Button.Available = 1
            else: Button.Available = 0
        elif Move == "ShieldBreaker0":
            if SRAmount >= 2 and SRList[0].Total >= 5 and EnemiesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "ScorchedLand0":
            if SRAmount >= 2: Button.Available = 1
            else: Button.Available = 0
        elif Move == "Charge0":
            if SRList[0].Total >= 5 and EnemiesAmount == 1: Button.Available = 1
            else: Button.Available = 0


        elif Move == "Defend0":
            if SRList[0].Total > 0 and AlliesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "Parry0":
            if SRList[0].Total > 0 and AlliesAmount == 1 and AlliesList[0] == Parent: Button.Available = 1
            else: Button.Available = 0
        elif Move == "Counter0":
            if SRList[0].Total > 0 and AlliesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "Concentrate0":
            if SRList[0].Total > 0: Button.Available = 1
            else: Button.Available = 0
        elif Move == "HunkerDown0":
            if SRAmount >= 2 and AlliesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "Barricade0":
            if SRAmount >= 2 and AlliesAmount == 0: Button.Available = 1
            else: Button.Available = 0
        elif Move == "Feint0":
            if SRList[0].Total > 0: Button.Available = 1
            else: Button.Available = 0
        elif Move == "ThrillOfBattle0":
            if SRAmount >= 2 and SRList[0].Total >= 5: Button.Available = 1
            else: Button.Available = 0
        elif Move == "RelentlessForce0":
            if SRList[0].Total > 0 and AlliesAmount == 0: Button.Available = 1
            else: Button.Available = 0
        elif Move == "SupressionAssault0":
            if SRAmount >= 2: Button.Available = 1
            else: Button.Available = 0
        elif Move == "EndlessCombat0":
            if SRList[0].Total > 0: Button.Available = 1
            else: Button.Available = 0
        elif Move == "FinalStand0":
            if True: Button.Available = 1
            else: Button.Available = 0
        elif Move == "Preparation0":
            if SRList[0].Total > 0: Button.Available = 1
            else: Button.Available = 0


        elif Move == "Guillotine0":
            if SRAmount >= 3 and EnemiesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "ShowOfMight0":
            if SRList[0].Total > 0 and EnemiesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "FearsomeGaze0":
            if SRList[0].Total > 0 and EnemiesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "Terrify0":
            if SRList[0].Total > 0 and EnemiesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "LongHunt0":
            if SRList[0].Total > 0 and EnemiesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "BloodyHorror0":
            if SRAmount >= 2 and EnemiesAmount == 1 and AlliesAmount == 0: Button.Available = 1
            else: Button.Available = 0
        elif Move == "PainfullFear0":
            if SRList[0].Total > 0 and EnemiesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "CripplingHorror0":
            if SRList[0].Total > 0 and EnemiesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "MassPanic0":
            if SRList[0].Total > 0 and EnemiesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "ShakySteps0":
            if SRList[0].Total > 0 and EnemiesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "Unyielding0":
            if SRList[0].Total > 0 and AlliesAmount == 1: Button.Available = 1
            else:
                Button.Available = 0
        elif Move == "Nightmares0":
            if SRList[0].Total > 0 and EnemiesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "PreyInstincts0":
            if SRList[0].Total >= 5 and AlliesAmount == 1: Button.Available = 1
            else: Button.Available = 0
        elif Move == "Intimidate0":
            if SRList[0].Total > 0 and EnemiesAmount == 1: Button.Available = 1
            else: Button.Available = 0


    except Exception as e:
        Button.Available = 0
        ""
    # if Button.Status == "Available":
    #     Button.Available = 0
    # elif Button.Status == "Disabled":
    #     Button.Available = 1
def getButtonText(self, Move):
    if Move == "Strike0":
        return "Strike"
    elif Move == "HeavyStrike0":
        return "HeavyStrike"
    elif Move == "Defend0":
        return "Defend"
    elif Move == "Bloodlust0":
        return "Bloodlust"
    elif Move == "ShowOfForce0":
        return "Show Of Force"
    elif Move == "FlurryOfBlows0":
        return "Flurry Of Blows"
    elif Move == "TauntingBlow0":
        return "Taunting Blow"
    elif Move == "CheapStrike0":
        return "Cheap Strike"
    elif Move == "BrokenGuard0":
        return "Broken Guard"
    elif Move == "DisarmingStrike0":
        return "Disarming Strike"
    elif Move == "Jab0":
        return "Jab"
    elif Move == "FullCombo0":
        return "Full Combo"
    elif Move == "Swipe0":
        return "Swipe"
    elif Move == "ShieldBreaker0":
        return "Shield Breaker"
    elif Move == "ScorchedLand0":
        return "Scorched Land"
    elif Move == "Charge0":
        return "Charge"

    elif Move == "Defend0":
        return "Defend"
    elif Move == "Parry0":
        return "Parry"
    elif Move == "Counter0":
        return "Counter"
    elif Move == "Concentrate0":
        return "Concentrate"
    elif Move == "HunkerDown0":
        return "Hunker Down"
    elif Move == "Barricade0":
        return "Barricade"
    elif Move == "Feint0":
        return "Feint"
    elif Move == "ThrillOfBattle0":
        return "Thrill Of Battle"
    elif Move == "RelentlessForce0":
        return "Relentless Force"
    elif Move == "SupressionAssault0":
        return "Supression Assault"
    elif Move == "EndlessCombat0":
        return "Endless Combat"
    elif Move == "FinalStand0":
        return "Final Stand"
    elif Move == "Preparation0":
        return "Preparation"


    elif Move == "Guillotine0":
        return "Guillotine"
    elif Move == "ShowOfMight0":
        return "Show Of Might"
    elif Move == "FearsomeGaze0":
        return "Fearsome Gaze"
    elif Move == "Terrify0":
        return "Terrify"
    elif Move == "LongHunt0":
        return "Long Hunt"
    elif Move == "BloodyHorror0":
        return "Bloody Horror"
    elif Move == "PainfullFear0":
        return "Painfull Fear"

    elif Move == "CripplingHorror0":
        return "Crippling Horror"
    elif Move == "MassPanic0":
        return "Mass Panic"
    elif Move == "ShakySteps0":
        return "Shaky Steps"
    elif Move == "Unyielding0":
        return "Unyielding"
    elif Move == "Nightmares0":
        return "Nightmares"
    elif Move == "PreyInstincts0":
        return "Prey Instincts"
    elif Move == "Intimidate0":
        return "Intimidate"
