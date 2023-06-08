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
import copy
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
            Log(2, "ERROR THREAD TASK", e, self.Func, "BasicEffects")

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
        ""

def GetEffects(self, Reference):
    # STAGE 1
    EffectsList = ["Vulnerable", "Weak", "Parry", "Hunkered", "Strength", "Thrill", "Fear", "Stun"]
    for Effect in EffectsList:
        Globals.BattleInfo["EffectStages"]["ProcessingStage1"][Effect] = Reference
        Globals.BattleInfo["EffectsDict"][Effect] = Reference
    # STAGE 2
    EffectsList = []
    for Effect in EffectsList:
        Globals.BattleInfo["EffectStages"]["ProcessingStage2"][Effect] = Reference
        Globals.BattleInfo["EffectsDict"][Effect] = Reference
    # STAGE 3
    EffectsList = ["Counter", "LastStand", "Stun", "Prey", "Unyielding", "Hunting", "PainfulMind"]
    for Effect in EffectsList:
        Globals.BattleInfo["EffectStages"]["ProcessingStage3"][Effect] = Reference
        Globals.BattleInfo["EffectsDict"][Effect] = Reference

    # STAGE SOT
    EffectsList = ["Exhausted", "LastStand", "Stun"]
    for Effect in EffectsList:
        Globals.BattleInfo["EffectStages"]["ProcessingStageSOT"][Effect] = Reference
        Globals.BattleInfo["EffectsDict"][Effect] = Reference
    # STAGE EOT
    EffectsList = ["Parry", "Hunkered", "Thrill", "Counter"]
    for Effect in EffectsList:
        Globals.BattleInfo["EffectStages"]["ProcessingStageEOT"][Effect] = Reference
        Globals.BattleInfo["EffectsDict"][Effect] = Reference

    # STAGE DRCARD
    EffectsList = ["Stun"]
    for Effect in EffectsList:
        Globals.BattleInfo["EffectStages"]["ProcessingStageDRCARD"][Effect] = Reference
        Globals.BattleInfo["EffectsDict"][Effect] = Reference
    # STAGE DCCARD
    EffectsList = []
    for Effect in EffectsList:
        Globals.BattleInfo["EffectStages"]["ProcessingStageDCCARD"][Effect] = Reference
        Globals.BattleInfo["EffectsDict"][Effect] = Reference

    # STAGE EXCARD
    EffectsList = ["Endless"]
    for Effect in EffectsList:
        Globals.BattleInfo["EffectStages"]["ProcessingStageEXCARD"][Effect] = Reference
        Globals.BattleInfo["EffectsDict"][Effect] = Reference
    # STAGE SMCARD
    EffectsList = []
    for Effect in EffectsList:
        Globals.BattleInfo["EffectStages"]["ProcessingStageSMCARD"][Effect] = Reference
        Globals.BattleInfo["EffectsDict"][Effect] = Reference


    # STAGE CRSR
    EffectsList = ["Stun"]
    for Effect in EffectsList:
        Globals.BattleInfo["EffectStages"]["ProcessingStageCRSR"][Effect] = Reference
        Globals.BattleInfo["EffectsDict"][Effect] = Reference
    # STAGE EXSR
    EffectsList = []
    for Effect in EffectsList:
        Globals.BattleInfo["EffectStages"]["ProcessingStageEXSR"][Effect] = Reference
        Globals.BattleInfo["EffectsDict"][Effect] = Reference


    # STAGE ProcessingUniversalEffects
    EffectsList = []
    for Effect in EffectsList:
        Globals.BattleInfo["EffectStages"]["ProcessingUniversalEffects"][Effect] = Reference
        Globals.BattleInfo["EffectsDict"][Effect] = Reference


def getAnimationID():
    try:
        ID = max(Globals.AnimationData.keys()) + 1
    except:
        ID = 0
    Globals.AnimationData[ID] = {}
    return ID

def EffectAnimation(self, AnimationID, Cast):
    Data = Globals.AnimationData[AnimationID]
    try:
        try:
            if Data["Target"] in list(Globals.BattleObjects["Enemies"].keys()):
                Type = "Enemies"
            elif Data["Target"] in list(Globals.BattleObjects["Allies"].keys()):
                Type = "Allies"
        except:
            ""
        if Data["EffectID"] == "Parry":
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
                Globals.Threads[ID]["Worker"] = Worker(EffectAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: EffectAnimation(self, AnimationID, Cast))

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
                widget = QLabel(Globals.Layouts["BattleMenu"].battleMenuUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage("Resources/CombatResources/AttackEffect4.png")
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["EffectID"] == "Thrill":
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
                Globals.Threads[ID]["Worker"] = Worker(EffectAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: EffectAnimation(self, AnimationID, Cast))

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
                widget = QLabel(Globals.Layouts["BattleMenu"].battleMenuUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage("Resources/CombatResources/Strength.png")
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["EffectID"] == "Counter":
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
                Globals.Threads[ID]["Worker"] = Worker(EffectAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: EffectAnimation(self, AnimationID, Cast))

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
                widget = QLabel(Globals.Layouts["BattleMenu"].battleMenuUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage("Resources/CombatResources/AttackEffect4.png")
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["EffectID"] == "Prey":
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
                Globals.Threads[ID]["Worker"] = Worker(EffectAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: EffectAnimation(self, AnimationID, Cast))

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
                widget = QLabel(Globals.Layouts["BattleMenu"].battleMenuUI)
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
        elif Data["EffectID"] == "Unyielding":
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
                Globals.Threads[ID]["Worker"] = Worker(EffectAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: EffectAnimation(self, AnimationID, Cast))

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
                widget = QLabel(Globals.Layouts["BattleMenu"].battleMenuUI)
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
        elif Data["EffectID"] == "Hunting":
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
                Globals.Threads[ID]["Worker"] = Worker(EffectAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: EffectAnimation(self, AnimationID, Cast))

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
                widget = QLabel(Globals.Layouts["BattleMenu"].battleMenuUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage("Resources/CombatResources/Debuff2.png")
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)
        elif Data["EffectID"] == "PainfulMind":
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
                Globals.Threads[ID]["Worker"] = Worker(EffectAnimation, Data, AnimationID, Cast)

                Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                Cast = 2
                Globals.Threads[ID]["Worker"].ping.connect(lambda: EffectAnimation(self, AnimationID, Cast))

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
                widget = QLabel(Globals.Layouts["BattleMenu"].battleMenuUI)
                widget.setGeometry(RN1,RN2,100,100)
                widget.show()
                widget.raise_()
                widget.setScaledContents(True)
                widget.setStyleSheet('''
                border: 0px solid black;
                background-color: rgba(0,0,0,0%);
                ''')
                image = QImage("Resources/CombatResources/Debuff2.png")
                imagepix = QPixmap.fromImage(image)
                widget.setPixmap(imagepix)
                Globals.Layouts["BattleMenu"].Fade(widget)

    except Exception as e:
        Log(1, "ERROR EFFECT ANIMATION", e)
        ""

def EffectTrigger(self, Data):
    try:
        Target = Data["FinalData"]["Target"]
        Parent = Data["FinalData"]["Parent"]
        if Target in list(Globals.BattleObjects["Enemies"].keys()):
            TargetType = "Enemies"
        elif Target in list(Globals.BattleObjects["Allies"].keys()):
            TargetType = "Allies"
        if Parent in list(Globals.BattleObjects["Enemies"].keys()):
            ParentType = "Enemies"
        elif Parent in list(Globals.BattleObjects["Allies"].keys()):
            ParentType = "Allies"
    except:
        ""
    Source = Globals.References[os.path.basename(__file__)[:-3]]
    # Globals.References
    try:
        if Data["Stage"] == 1:
            # Data = {"Effect":Effect, "Attack":Attack, "Button":Button, "OriginalData":OriginalData, "FinalData":FinalData, "Results":Results, "Stage":1, "Who":"Target"}
            try:
                Target = Data["FinalData"]["Target"]
                Parent = Data["FinalData"]["Parent"]
                if Target in list(Globals.BattleObjects["Enemies"].keys()):
                    TargetType = "Enemies"
                elif Target in list(Globals.BattleObjects["Allies"].keys()):
                    TargetType = "Allies"
                if Parent in list(Globals.BattleObjects["Enemies"].keys()):
                    ParentType = "Enemies"
                elif Parent in list(Globals.BattleObjects["Allies"].keys()):
                    ParentType = "Allies"
            except:
                ""
            Reference = Globals.BattleInfo["EffectStages"]["ProcessingStage1"][Data["Effect"]]
            if Data["Who"] == "Target" or Data["Who"] == "Universal":
                if Data["Effect"] == "Vulnerable":
                    if Data["FinalData"]["Damage"] > 0:
                        Damage = Data["FinalData"]["Damage"]
                        Damage = int((Damage * 1.4)//1)
                        Data["FinalData"]["Damage"] = Damage
                        if Globals.BattleObjects[TargetType][Target]["Object"].Effects["Vulnerable"]["Level"] > 1:
                            Globals.BattleObjects[TargetType][Target]["Object"].Effects["Vulnerable"]["Level"] -= 1
                        else:
                            Globals.BattleObjects[TargetType][Target]["Object"].Effects.pop("Vulnerable")
                        return Data
                elif Data["Effect"] == "Parry":
                    if Data["FinalData"]["Type"] == "Attack":
                        Damage = Data["FinalData"]["Damage"]
                        Data["FinalData"]["Damage"] = 0
                        ParryLevel = Globals.BattleObjects[TargetType][Target]["Object"].Effects["Parry"]["Level"]
                        if Damage > ParryLevel:
                            ParryDamage = ParryLevel
                        else:
                            ParryDamage = Damage
                        Globals.BattleObjects[TargetType][Target]["Object"].Effects.pop("Parry")

                        # SETTING INITIAL DATA FOR THE ANIMATIONS
                        AnimationID = getAnimationID()
                        DataAni = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "EffectID":"Parry", "DmgDealt":0, "Animation":[]}
                        Globals.AnimationData[AnimationID] = DataAni

                        # TRIGGERING THE ATTACK
                        AttackData = { "Target":Parent, "Parent":Target, "AttackID":"Parry", "Type":"Effect", "Flags":{ "Confirmation":0, "EffectsTrigger":0 }, "Source":Source, "Damage":ParryDamage, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{} }
                        Globals.Layouts["BattleMenu"].CastAttack( AttackData )

                        # CALLING FOR THE ANIMATION
                        Globals.AnimationData[AnimationID]["Target"] = Parent
                        self = Globals.Layouts["BattleMenu"]
                        EffectAnimation(self, AnimationID, 0)

                        return Data
                elif Data["Effect"] == "Hunkered":
                    if Data["FinalData"]["Damage"] > 0:
                        Damage = Data["FinalData"]["Damage"]
                        Damage = int((Damage * 0.5)//1)
                        Data["FinalData"]["Damage"] = Damage
                        return Data
                elif Data["Effect"] == "Fear":
                    if Data["FinalData"]["MentalDamage"] > 0:
                        Damage = Data["FinalData"]["MentalDamage"]
                        Damage = int((Damage * 1.4)//1)
                        Data["FinalData"]["MentalDamage"] = Damage
                        if Globals.BattleObjects[TargetType][Target]["Object"].Effects["Fear"]["Level"] > 1:
                            Globals.BattleObjects[TargetType][Target]["Object"].Effects["Fear"]["Level"] -= 1
                        else:
                            Globals.BattleObjects[TargetType][Target]["Object"].Effects.pop("Fear")
                        return Data

            if Data["Who"] == "Caster" or Data["Who"] == "Universal":
                if Data["Effect"] == "Weak":
                    if Data["FinalData"]["Type"] == "Attack" and Data["FinalData"]["Damage"] > 0:
                        Damage = Data["FinalData"]["Damage"]
                        Damage = int((Damage * 0.75)//1)
                        Data["FinalData"]["Damage"] = Damage
                        return Data
                if Data["Effect"] == "Thrill":
                    if Data["FinalData"]["Type"] == "Attack" and Data["FinalData"]["Damage"] > 0:
                        ThrillLevel = Globals.BattleObjects[ParentType][Parent]["Object"].Effects["Thrill"]["Level"]

                        # SETTING INITIAL DATA FOR THE ANIMATIONS
                        AnimationID = getAnimationID()
                        DataAni = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "EffectID":"Thrill", "DmgDealt":0, "Animation":[]}
                        Globals.AnimationData[AnimationID] = DataAni

                        # TRIGGERING THE ATTACK
                        StrengthEffect = {"ID":"Strength","Level":ThrillLevel,"Data":{}}
                        AttackData = { "Target":Parent, "Parent":Parent, "AttackID":"Parry", "Type":"Effect", "Flags":{ "Confirmation":0, "EffectsTrigger":0 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"Strength":StrengthEffect}, "AnimationID":AnimationID, "OtherData":{} }
                        Globals.Layouts["BattleMenu"].CastAttack( AttackData )

                        # CALLING FOR THE ANIMATION
                        Globals.AnimationData[AnimationID]["Target"] = Parent
                        self = Globals.Layouts["BattleMenu"]
                        EffectAnimation(self, AnimationID, 0)
                elif Data["Effect"] == "Strength":
                    if Data["FinalData"]["Type"] == "Attack" and Data["FinalData"]["Damage"] > 0:
                        StrengthLevel = Globals.BattleObjects[ParentType][Parent]["Object"].Effects["Strength"]["Level"]
                        # StrengthLevel = Globals.BattleObjects[TargetType][Target]["Object"].Effects["Strength"]["Level"]
                        Damage = Data["FinalData"]["Damage"]
                        Damage += StrengthLevel
                        Data["FinalData"]["Damage"] = Damage
                        return Data

        elif Data["Stage"] == 2:
            # Data = {"Effect":Effect, "Attack":Attack, "Button":Button, "OriginalData":OriginalData, "FinalData":FinalData, "Results":Results, "Stage":2, "Who":"Target"}
            try:
                Target = Data["FinalData"]["Target"]
                Parent = Data["FinalData"]["Parent"]
                if Target in list(Globals.BattleObjects["Enemies"].keys()):
                    TargetType = "Enemies"
                elif Target in list(Globals.BattleObjects["Allies"].keys()):
                    TargetType = "Allies"
                if Parent in list(Globals.BattleObjects["Enemies"].keys()):
                    ParentType = "Enemies"
                elif Parent in list(Globals.BattleObjects["Allies"].keys()):
                    ParentType = "Allies"
            except:
                ""
        elif Data["Stage"] == 3:
            # Data = {"Effect":Effect, "Attack":Attack, "Button":Button, "OriginalData":OriginalData, "FinalData":FinalData, "Results":Results, "Stage":3, "Who":"Target"}
            try:
                Target = Data["FinalData"]["Target"]
                Parent = Data["FinalData"]["Parent"]
                if Target in list(Globals.BattleObjects["Enemies"].keys()):
                    TargetType = "Enemies"
                elif Target in list(Globals.BattleObjects["Allies"].keys()):
                    TargetType = "Allies"
                if Parent in list(Globals.BattleObjects["Enemies"].keys()):
                    ParentType = "Enemies"
                elif Parent in list(Globals.BattleObjects["Allies"].keys()):
                    ParentType = "Allies"
            except:
                ""
            if Data["Who"] == "Target" or Data["Who"] == "Universal":
                if Data["Effect"] == "Counter":
                    if Data["FinalData"]["Type"] == "Attack" and Data["FinalData"]["Damage"] > 0:
                        if Data["Results"]["ShieldDamage"] > 0 and Data["Results"]["DamageDealt"] <= 0:
                            CounterLevel = Globals.BattleObjects[TargetType][Target]["Object"].Effects["Counter"]["Level"]

                            # SETTING INITIAL DATA FOR THE ANIMATIONS
                            AnimationID = getAnimationID()
                            DataAni = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "EffectID":"Counter", "DmgDealt":0, "Animation":[]}
                            Globals.AnimationData[AnimationID] = DataAni

                            # TRIGGERING THE ATTACK
                            AttackData = { "Target":Parent, "Parent":Target, "AttackID":"Counter", "Type":"Effect", "Flags":{ "Confirmation":0, "EffectsTrigger":0 }, "Source":Source, "Damage":CounterLevel, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{} }
                            Globals.Layouts["BattleMenu"].CastAttack( AttackData )

                            # CALLING FOR THE ANIMATION
                            Globals.AnimationData[AnimationID]["Target"] = Parent
                            self = Globals.Layouts["BattleMenu"]
                            EffectAnimation(self, AnimationID, 0)

                            return Data
                elif Data["Effect"] == "Stun":
                    # TODO Enemy.Status == "Stunned"
                    ""
                elif Data["Effect"] == "Prey":
                    # TO PREVENT THE EFFECT FROM TRIGGERING ITSELF
                    PreyLevel = Globals.BattleObjects[TargetType][Target]["Object"].Effects["Prey"]["Level"]
                    try:
                        ResultsLevel = Data["Results"]["EffectsApplied"]["Prey"]["Level"]
                    except:
                        ResultsLevel = 0
                    if ResultsLevel != PreyLevel and Data["FinalData"]["Type"] == "Attack":
                        PreyLevel -= ResultsLevel
                        # SETTING INITIAL DATA FOR THE ANIMATIONS
                        AnimationID = getAnimationID()
                        DataAni = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "EffectID":"Prey", "DmgDealt":0, "Animation":[]}
                        Globals.AnimationData[AnimationID] = DataAni

                        # TRIGGERING THE ATTACK
                        AttackData = { "Target":Target, "Parent":Parent, "AttackID":"Prey", "Type":"Effect", "Flags":{ "Confirmation":0, "EffectsTrigger":0 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":PreyLevel, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{} }
                        Globals.Layouts["BattleMenu"].CastAttack( AttackData )

                        # CALLING FOR THE ANIMATION
                        Globals.AnimationData[AnimationID]["Target"] = Target
                        self = Globals.Layouts["BattleMenu"]
                        EffectAnimation(self, AnimationID, 0)

                        return Data
                elif Data["Effect"] == "Unyielding":
                    # TO PREVENT THE EFFECT FROM TRIGGERING ITSELF
                    UnyieldingLevel = Globals.BattleObjects[TargetType][Target]["Object"].Effects["Unyielding"]["Level"]
                    try:
                        ResultsLevel = Data["Results"]["EffectsApplied"]["Unyielding"]["Level"]
                    except:
                        ResultsLevel = 0
                    if ResultsLevel != UnyieldingLevel and Data["FinalData"]["Type"] == "Attack" and (Data["OriginalData"]["Damage"] > 0 or Data["OriginalData"]["MentalDamage"] > 0):
                        UnyieldingLevel -= ResultsLevel
                        # SETTING INITIAL DATA FOR THE ANIMATIONS
                        AnimationID = getAnimationID()
                        DataAni = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "EffectID":"Unyielding", "DmgDealt":0, "Animation":[]}
                        Globals.AnimationData[AnimationID] = DataAni

                        # TRIGGERING THE ATTACK
                        AttackData = { "Target":Parent, "Parent":Target, "AttackID":"Unyielding", "Type":"Effect", "Flags":{ "Confirmation":0, "EffectsTrigger":0 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":UnyieldingLevel, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{} }
                        Globals.Layouts["BattleMenu"].CastAttack( AttackData )

                        # CALLING FOR THE ANIMATION
                        Globals.AnimationData[AnimationID]["Target"] = Parent
                        self = Globals.Layouts["BattleMenu"]
                        EffectAnimation(self, AnimationID, 0)

                        return Data
                elif Data["Effect"] == "PainfulMind":
                    # TO PREVENT THE EFFECT FROM TRIGGERING ITSELF
                    PainfulMindLevel = Globals.BattleObjects[TargetType][Target]["Object"].Effects["PainfulMind"]["Level"]
                    try:
                        ResultsLevel = Data["Results"]["EffectsApplied"]["PainfulMind"]["Level"]
                    except:
                        ResultsLevel = 0
                    if ResultsLevel != PainfulMindLevel and Data["Results"]["DamageDealt"] > 0:
                        PainfulMindLevel -= ResultsLevel
                        # SETTING INITIAL DATA FOR THE ANIMATIONS
                        AnimationID = getAnimationID()
                        DataAni = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "EffectID":"PainfulMind", "DmgDealt":0, "Animation":[]}
                        Globals.AnimationData[AnimationID] = DataAni

                        # TRIGGERING THE ATTACK
                        AttackData = { "Target":Target, "Parent":Parent, "AttackID":"PainfulMind", "Type":"Effect", "Flags":{ "Confirmation":0, "EffectsTrigger":0 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":PainfulMindLevel, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{} }
                        Globals.Layouts["BattleMenu"].CastAttack( AttackData )

                        # CALLING FOR THE ANIMATION
                        Globals.AnimationData[AnimationID]["Target"] = Target
                        self = Globals.Layouts["BattleMenu"]
                        EffectAnimation(self, AnimationID, 0)


            if Data["Who"] == "Caster" or Data["Who"] == "Universal":
                if Data["Effect"] == "LastStand":
                    # SO THE EFFECT ISN'T TRIGGERED IN THE SAME ATTACK THAT ADDS IT
                    if "LastStand" in Data["Results"]["EffectsApplied"]:
                        if Data["Results"]["EffectsApplied"]["LastStand"]["Level"] == Globals.BattleObjects[ParentType][Parent]["Object"].Effects["LastStand"]["Level"]:
                            return Data

                    Attack = Data["FinalData"]["OtherData"]["Attack"]
                    Button = Data["FinalData"]["OtherData"]["Button"]
                    Globals.Layouts["BattleMenu"].ExhaustCard(Attack, Button)
                elif Data["Effect"] == "Hunting":
                    # SO THE EFFECT ISN'T TRIGGERED IN THE SAME ATTACK THAT ADDS IT
                    if "Hunting" in Data["Results"]["EffectsApplied"]:
                        if Data["Results"]["EffectsApplied"]["Hunting"]["Level"] == Globals.BattleObjects[ParentType][Parent]["Object"].Effects["Hunting"]["Level"]:
                            return Data
                    # TO PREVENT THE EFFECT FROM TRIGGERING ITSELF
                    HuntingLevel = Globals.BattleObjects[ParentType][Parent]["Object"].Effects["Hunting"]["Level"]
                    try:
                        ResultsLevel = Data["Results"]["EffectsApplied"]["Hunting"]["Level"]
                    except:
                        ResultsLevel = 0

                    if ResultsLevel != HuntingLevel and Data["FinalData"]["Type"] == "Attack":
                        HuntingLevel -= ResultsLevel
                        # SETTING INITIAL DATA FOR THE ANIMATIONS
                        AnimationID = getAnimationID()
                        DataAni = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "EffectID":"Hunting", "DmgDealt":0, "Animation":[]}
                        Globals.AnimationData[AnimationID] = DataAni

                        # TRIGGERING THE ATTACK
                        FearEffect = {"ID":"Fear","Level":HuntingLevel,"Data":{}}
                        AttackData = { "Target":Target, "Parent":Parent, "AttackID":"Hunting", "Type":"Effect", "Flags":{ "Confirmation":0, "EffectsTrigger":0 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"Fear":FearEffect}, "AnimationID":AnimationID, "OtherData":{} }
                        Globals.Layouts["BattleMenu"].CastAttack( AttackData )

                        print("oh")
                        # CALLING FOR THE ANIMATION
                        Globals.AnimationData[AnimationID]["Target"] = Target
                        self = Globals.Layouts["BattleMenu"]
                        EffectAnimation(self, AnimationID, 0)

                        return Data

        elif Data["Stage"] == "SOT":
            # Data = {"Effect":Effect, "Stage":"SOT", "Parent":Parent}
            try:
                Parent = Data["Parent"]
                if Parent in list(Globals.BattleObjects["Enemies"].keys()):
                    ParentType = "Enemies"
                elif Parent in list(Globals.BattleObjects["Allies"].keys()):
                    ParentType = "Allies"
            except:
                ""
            if Data["Effect"] == "Exhausted":
                # TODO Test this
                if Globals.BattleObjects[ParentType][Parent]["Object"].Effects["Exhausted"]["Level"] > 1:
                    Globals.BattleObjects[ParentType][Parent]["Object"].Effects["Exhausted"]["Level"] -= 1
                else:
                    Globals.BattleObjects[ParentType][Parent]["Object"].Effects.pop("Exhausted")

                # SETTING INITIAL DATA FOR THE ANIMATIONS
                AnimationID = getAnimationID()
                DataAni = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "EffectID":"Parry", "DmgDealt":0, "Animation":[]}
                Globals.AnimationData[AnimationID] = DataAni

                # TRIGGERING THE ATTACK
                StunEffect = {"ID":"Stun","Level":1,"Data":{}}
                AttackData = { "Target":Parent, "Parent":Parent, "AttackID":"Exhausted", "Type":"Effect", "Flags":{ "Confirmation":0, "EffectsTrigger":0 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"Stun":StunEffect}, "AnimationID":AnimationID, "OtherData":{} }
                Globals.Layouts["BattleMenu"].CastAttack( AttackData )

                # CALLING FOR THE ANIMATION
                Globals.AnimationData[AnimationID]["Target"] = Parent
                self = Globals.Layouts["BattleMenu"]
                EffectAnimation(self, AnimationID, 0)

                return Data
            if Data["Effect"] == "LastStand":
                # TODO Test this
                if Globals.BattleObjects[ParentType][Parent]["Object"].Effects["Exhausted"]["Level"] > 1:
                    Globals.BattleObjects[ParentType][Parent]["Object"].Effects["Exhausted"]["Level"] -= 1
                else:
                    Globals.BattleObjects[ParentType][Parent]["Object"].Effects.pop("Exhausted")

                # SETTING INITIAL DATA FOR THE ANIMATIONS
                AnimationID = getAnimationID()
                DataAni = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "EffectID":"Parry", "DmgDealt":0, "Animation":[]}
                Globals.AnimationData[AnimationID] = DataAni

                # TRIGGERING THE ATTACK
                VulnerableEffect = {"ID":"Vulnerable","Level":3,"Data":{}}
                WeakEffect = {"ID":"Weak","Level":3,"Data":{}}
                AttackData = { "Target":Parent, "Parent":Parent, "AttackID":"Exhausted", "Type":"Effect", "Flags":{ "Confirmation":0, "EffectsTrigger":0 }, "Source":Source, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{"Vulnerable":VulnerableEffect, "Weak":WeakEffect}, "AnimationID":AnimationID, "OtherData":{} }
                Globals.Layouts["BattleMenu"].CastAttack( AttackData )

                # CALLING FOR THE ANIMATION
                Globals.AnimationData[AnimationID]["Target"] = Parent
                self = Globals.Layouts["BattleMenu"]
                EffectAnimation(self, AnimationID, 0)

                return Data
        elif Data["Stage"] == "EOT":
            # Data = {"Effect":Effect, "Stage":"EOT", "Parent":Parent}
            try:
                Parent = Data["Parent"]
                if Parent in list(Globals.BattleObjects["Enemies"].keys()):
                    ParentType = "Enemies"
                elif Parent in list(Globals.BattleObjects["Allies"].keys()):
                    ParentType = "Allies"
            except:
                ""
            if Data["Effect"] == "Parry":
                Globals.BattleObjects[TargetType][Target]["Object"].Effects.pop("Parry")
            if Data["Effect"] == "Hunkered":
                if Globals.BattleObjects[TargetType][Target]["Object"].Effects["Hunkered"]["Level"] > 1:
                    Globals.BattleObjects[TargetType][Target]["Object"].Effects["Hunkered"]["Level"] -= 1
                else:
                    Globals.BattleObjects[TargetType][Target]["Object"].Effects.pop("Hunkered")
                return Data
            if Data["Effect"] == "Thrill":
                Globals.BattleObjects[TargetType][Target]["Object"].Effects.pop("Thrill")
            if Data["Effect"] == "Counter":
                Globals.BattleObjects[TargetType][Target]["Object"].Effects.pop("Counter")

        elif Data["Stage"] == "CRSR":
            # Roll = {'Upper': 7, 'Lower': 3, 'Bonus': 0, 'Minus': 0, 'Parent': '0'}
            # Data = {"Effect":Effect, "Stage":"CRSR", "SRList":SRList, "Parent":Parent, "Who":"Ally"}
            if Data["Effect"] == "Stun":
                if Data["Who"] == "Ally":
                    NewList = []
                    for Roll in Data["SRList"]:
                        if Roll["Parent"] == Data["Parent"]:
                            ''
                        else:
                            NewList.append(Roll)
                    Data["SRList"] = NewList
                    return Data
        elif Data["Stage"] == "EXSR":
            # Data = {"Effect":Effect, "Stage":"CRSR", "SR":SR, "SRList":SRList, "Parent": Parent}
            ""

        elif Data["Stage"] == "DRCARD":
            # Data = {"Effect":Effect, "Stage":"DRCARD", "Card":Card, "Parent":Parent}
            if Data["Effect"] == "Stun":
                if Data["Card"] != []:
                    Data["Card"][0].Status = "Disabled"
                    return Data
        elif Data["Stage"] == "DCCARD":
            # Data = {"Effect":Effect, "Stage":"DCCARD", "Card":Card, "Parent":Parent, "Deck":Deck}
            ""

        elif Data["Stage"] == "SMCARD":
            # Data = {"Effect":Effect, "Stage":"DRCARD", "Card":Card, "Parent":Parent}
            ""
        elif Data["Stage"] == "EXCARD":
            # Data = {"Effect":Effect, "Stage":"EXCARD", "Attack":Attack, "Button":Button, "EffectFull":EffectFull}
            if Data["Effect"] == "Endless":
                if Data["Attack"] != {}:
                    EndlessLevel = Data["EffectFull"]["Level"]
                    # print("EndlessLevel", EndlessLevel)
                    for i in range(EndlessLevel):
                        Globals.Layouts["BattleMenu"].drawCard()
            ""
    except Exception as e:
        Log(3, "ERROR EFFECT TRIGGER", Data["Stage"], Data["Effect"], e, Data)

    return Data

def EffectConfirmed(OriginalData, FinalData, Results):
    # print("EffectConfirmed")
    ""

def getIcon(Effect, Object):
    # EffectID = Object.Effects[Effect]["ID"]
    EffectID = Object.Effects[Effect]["ID"]
    Level = Object.Effects[Effect]["Level"]
    if EffectID == "Vulnerable":
        IconWidget = QLabel()
        IconWidget.setScaledContents(True)
        IconWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        IconWidget.setFont(QFont('Segoe UI', 14))
        IconWidget.setStyleSheet('''
        QLabel{
        background-color:rgb(35,35,35);
        border-image: url(Resources/CombatResources/Vulnerable.png);
        }
        QToolTip{
        background-color:rgb(255,255,255)
        }
        ''')

        if 16777248 in Globals.Keys:
            IconWidget.setText(str(Level))
        IconWidget.setToolTip(f'''Vulnerable {Level}, Recieve 40% more damage the next {Level} times''')

        return IconWidget
    elif EffectID == "Weak":
        IconWidget = QLabel()
        IconWidget.setScaledContents(True)
        IconWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        IconWidget.setFont(QFont('Segoe UI', 14))
        IconWidget.setStyleSheet('''
        QLabel{
        background-color:rgb(35,35,35);
        border-image: url(Resources/CombatResources/Weak.png);
        }
        QToolTip{
        background-color:rgb(255,255,255)
        }
        ''')

        if 16777248 in Globals.Keys:
            IconWidget.setText(str(Level))
        IconWidget.setToolTip(f'''Weak {Level}, Deal 25% less damage the next {Level} times''')

        return IconWidget
    elif EffectID == "Parry":
        IconWidget = QLabel()
        IconWidget.setScaledContents(True)
        IconWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        IconWidget.setFont(QFont('Segoe UI', 14))
        IconWidget.setStyleSheet('''
        QLabel{
        background-color:rgb(35,35,35);
        border-image: url(Resources/CombatResources/Parry.png);
        }
        QToolTip{
        background-color:rgb(255,255,255)
        }
        ''')

        if 16777248 in Globals.Keys:
            IconWidget.setText(str(Level))
        IconWidget.setToolTip(f'''Parry {Level}, Block the next attack and deflect up to {Level} damage''')

        return IconWidget
    elif EffectID == "Counter":
        IconWidget = QLabel()
        IconWidget.setScaledContents(True)
        IconWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        IconWidget.setFont(QFont('Segoe UI', 14))
        IconWidget.setStyleSheet('''
        QLabel{
        background-color:rgb(35,35,35);
        border-image: url(Resources/CombatResources/Thorns.png);
        }
        QToolTip{
        background-color:rgb(255,255,255)
        }
        ''')

        if 16777248 in Globals.Keys:
            IconWidget.setText(str(Level))
        IconWidget.setToolTip(f'''Counter {Level}, Deals {Level} damage back when an attack is blocked''')

        return IconWidget
    elif EffectID == "Hunkered":
        IconWidget = QLabel()
        IconWidget.setScaledContents(True)
        IconWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        IconWidget.setFont(QFont('Segoe UI', 14))
        IconWidget.setStyleSheet('''
        QLabel{
        background-color:rgb(35,35,35);
        border-image: url(Resources/CombatResources/Hunker.png);
        }
        QToolTip{
        background-color:rgb(255,255,255)
        }
        ''')

        if 16777248 in Globals.Keys:
            IconWidget.setText(str(Level))
        IconWidget.setToolTip(f'''Hunkered {Level}, Reduces incoming damage in 1/2 for the next {Level} turns''')

        return IconWidget
    elif EffectID == "Thrill":
        IconWidget = QLabel()
        IconWidget.setScaledContents(True)
        IconWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        IconWidget.setFont(QFont('Segoe UI', 14))
        IconWidget.setStyleSheet('''
        QLabel{
        background-color:rgb(35,35,35);
        border-image: url(Resources/CombatResources/Buff1.png);
        }
        QToolTip{
        background-color:rgb(255,255,255)
        }
        ''')

        if 16777248 in Globals.Keys:
            IconWidget.setText(str(Level))
        IconWidget.setToolTip(f'''Thrill {Level}, Grants {Level} Strength every attack this turn''')

        return IconWidget
    elif EffectID == "Strength":
        IconWidget = QLabel()
        IconWidget.setScaledContents(True)
        IconWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        IconWidget.setFont(QFont('Segoe UI', 14))
        IconWidget.setStyleSheet('''
        QLabel{
        background-color:rgb(35,35,35);
        border-image: url(Resources/CombatResources/Strength.png);
        }
        QToolTip{
        background-color:rgb(255,255,255)
        }
        ''')

        if 16777248 in Globals.Keys:
            IconWidget.setText(str(Level))
        IconWidget.setToolTip(f'''Strength {Level}, Every attack deals {Level} extra damage''')

        return IconWidget
    elif EffectID == "Exhausted":
        IconWidget = QLabel()
        IconWidget.setScaledContents(True)
        IconWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        IconWidget.setFont(QFont('Segoe UI', 14))
        IconWidget.setStyleSheet('''
        QLabel{
        background-color:rgb(35,35,35);
        border-image: url(Resources/CombatResources/Debuff2.png);
        }
        QToolTip{
        background-color:rgb(255,255,255)
        }
        ''')

        if 16777248 in Globals.Keys:
            IconWidget.setText(str(Level))
        IconWidget.setToolTip(f'''Exhausted {Level}, At he start of the next {Level} turns get Stun 1 ''')

        return IconWidget
    elif EffectID == "Endless":
        IconWidget = QLabel()
        IconWidget.setScaledContents(True)
        IconWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        IconWidget.setFont(QFont('Segoe UI', 14))
        IconWidget.setStyleSheet('''
        QLabel{
        background-color:rgb(35,35,35);
        border-image: url(Resources/CombatResources/Buff1.png);
        }
        QToolTip{
        background-color:rgb(255,255,255)
        }
        ''')

        if 16777248 in Globals.Keys:
            IconWidget.setText(str(Level))
        IconWidget.setToolTip(f'''Endless {Level}, Draw {Level} cards for every exhausted card this turn. ''')

        return IconWidget
    elif EffectID == "LastStand":
        IconWidget = QLabel()
        IconWidget.setScaledContents(True)
        IconWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        IconWidget.setFont(QFont('Segoe UI', 14))
        IconWidget.setStyleSheet('''
        QLabel{
        background-color:rgb(35,35,35);
        border-image: url(Resources/CombatResources/Buff2.png);
        }
        QToolTip{
        background-color:rgb(255,255,255)
        }
        ''')

        if 16777248 in Globals.Keys:
            IconWidget.setText(str(Level))
        IconWidget.setToolTip(f'''LastStand {Level}, EXhaust every card used this turn. At he start of the next {Level} turns get 3 Weak and 3 Wulnerable. ''')

        return IconWidget
    elif EffectID == "Fear":
        IconWidget = QLabel()
        IconWidget.setScaledContents(True)
        IconWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        IconWidget.setFont(QFont('Segoe UI', 14))
        IconWidget.setStyleSheet('''
        QLabel{
        background-color:rgb(35,35,35);
        border-image: url(Resources/CombatResources/Fear2.png);
        }
        QToolTip{
        background-color:rgb(255,255,255)
        }
        ''')

        if 16777248 in Globals.Keys:
            IconWidget.setText(str(Level))
        IconWidget.setToolTip(f'''Fear {Level}, Recieve 40% more mental damage the next {Level} times''')

        return IconWidget
    elif EffectID == "Stun":
        IconWidget = QLabel()
        IconWidget.setScaledContents(True)
        IconWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        IconWidget.setFont(QFont('Segoe UI', 14))
        IconWidget.setStyleSheet('''
        QLabel{
        background-color:rgb(35,35,35);
        border-image: url(Resources/CombatResources/Stun.png);
        }
        QToolTip{
        background-color:rgb(255,255,255)
        }
        ''')

        if 16777248 in Globals.Keys:
            IconWidget.setText(str(Level))
        IconWidget.setToolTip(f'''Stun {Level}, The next {Level} turns this character's attacks are disabled and won't provide SR's ''')

        return IconWidget
    elif EffectID == "Prey":
        IconWidget = QLabel()
        IconWidget.setScaledContents(True)
        IconWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        IconWidget.setFont(QFont('Segoe UI', 14))
        IconWidget.setStyleSheet('''
        QLabel{
        background-color:rgb(35,35,35);
        border-image: url(Resources/CombatResources/Prey.png);
        }
        QToolTip{
        background-color:rgb(255,255,255)
        }
        ''')

        if 16777248 in Globals.Keys:
            IconWidget.setText(str(Level))
        IconWidget.setToolTip(f'''Prey {Level}, Recieve {Level} mental damage every attack recieved ''')

        return IconWidget
    elif EffectID == "Unyielding":
        IconWidget = QLabel()
        IconWidget.setScaledContents(True)
        IconWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        IconWidget.setFont(QFont('Segoe UI', 14))
        IconWidget.setStyleSheet('''
        QLabel{
        background-color:rgb(35,35,35);
        border-image: url(Resources/CombatResources/Unyielding.png);
        }
        QToolTip{
        background-color:rgb(255,255,255)
        }
        ''')

        if 16777248 in Globals.Keys:
            IconWidget.setText(str(Level))
        IconWidget.setToolTip(f'''Unyielding {Level}, Deal {Level} mental damage upon being hit ''')

        return IconWidget
    elif EffectID == "Hunting":
        IconWidget = QLabel()
        IconWidget.setScaledContents(True)
        IconWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        IconWidget.setFont(QFont('Segoe UI', 14))
        IconWidget.setStyleSheet('''
        QLabel{
        background-color:rgb(35,35,35);
        border-image: url(Resources/CombatResources/Hunting.png);
        }
        QToolTip{
        background-color:rgb(255,255,255)
        }
        ''')

        if 16777248 in Globals.Keys:
            IconWidget.setText(str(Level))
        IconWidget.setToolTip(f'''Hunting {Level}, Applies {Level} fear every attack ''')

        return IconWidget
    elif EffectID == "PainfulMind":
        IconWidget = QLabel()
        IconWidget.setScaledContents(True)
        IconWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        IconWidget.setFont(QFont('Segoe UI', 14))
        IconWidget.setStyleSheet('''
        QLabel{
        background-color:rgb(35,35,35);
        border-image: url(Resources/CombatResources/PainfulMind.png);
        }
        QToolTip{
        background-color:rgb(255,255,255)
        }
        ''')

        if 16777248 in Globals.Keys:
            IconWidget.setText(str(Level))
        IconWidget.setToolTip(f'''Painful Mind {Level}, Deals {Level} metal damage every tiime they recive damage ''')

        return IconWidget
