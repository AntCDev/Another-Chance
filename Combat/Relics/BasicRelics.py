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
def getAnimationID():
    try:
        ID = max(Globals.AnimationData.keys()) + 1
    except:
        ID = 0
    Globals.AnimationData[ID] = {}
    return ID



def GetRelics(self, Reference):
    def ApllyRarity(Relic):
        MList = ["BandAid", "SharpeningStone", "ClothArmor"]
        NList = []
        RList = []
        SRList = []
        if Relic in NList:
            Globals.BattleInfo["RelicsDict"][Relic]["Rarity"] = "Normal"
        elif Relic in RList:
            Globals.BattleInfo["RelicsDict"][Relic]["Rarity"] = "Rare"
        elif Relic in SRList:
            Globals.BattleInfo["RelicsDict"][Relic]["Rarity"] = "SuperRare"
        else:
            Globals.BattleInfo["RelicsDict"][Relic]["Rarity"] = "Mundane"


    # STAGE 1
    RelicsList = ["BandAid", "SharpeningStone", "ClothArmor"]
    for Relic in RelicsList:
        Globals.BattleInfo["EffectStages"]["ProcessingStage1"][Relic] = Reference
        Globals.BattleInfo["RelicsDict"][Relic] = {"Reference":Reference, "Available":1}
        ApllyRarity(Relic)
    # STAGE 2
    RelicsList = []
    for Relic in RelicsList:
        Globals.BattleInfo["EffectStages"]["ProcessingStage2"][Relic] = Reference
        Globals.BattleInfo["RelicsDict"][Relic] = {"Reference":Reference, "Available":1}
        ApllyRarity(Relic)
    # STAGE 3
    RelicsList = []
    for Relic in RelicsList:
        Globals.BattleInfo["EffectStages"]["ProcessingStage3"][Relic] = Reference
        Globals.BattleInfo["RelicsDict"][Relic] = {"Reference":Reference, "Available":1}
        ApllyRarity(Relic)

    # STAGE SOT
    RelicsList = []
    for Relic in RelicsList:
        Globals.BattleInfo["EffectStages"]["ProcessingStageSOT"][Relic] = Reference
        Globals.BattleInfo["RelicsDict"][Relic] = {"Reference":Reference, "Available":1}
        ApllyRarity(Relic)
    # STAGE EOT
    RelicsList = []
    for Relic in RelicsList:
        Globals.BattleInfo["EffectStages"]["ProcessingStageEOT"][Relic] = Reference
        Globals.BattleInfo["RelicsDict"][Relic] = {"Reference":Reference, "Available":1}
        ApllyRarity(Relic)

    # STAGE DRCARD
    RelicsList = []
    for Relic in RelicsList:
        Globals.BattleInfo["EffectStages"]["ProcessingStageDRCARD"][Relic] = Reference
        Globals.BattleInfo["RelicsDict"][Relic] = {"Reference":Reference, "Available":1}
        ApllyRarity(Relic)
    # STAGE DCCARD
    RelicsList = []
    for Relic in RelicsList:
        Globals.BattleInfo["EffectStages"]["ProcessingStageDCCARD"][Relic] = Reference
        Globals.BattleInfo["RelicsDict"][Relic] = {"Reference":Reference, "Available":1}
        ApllyRarity(Relic)

    # STAGE EXCARD
    RelicsList = []
    for Relic in RelicsList:
        Globals.BattleInfo["EffectStages"]["ProcessingStageEXCARD"][Relic] = Reference
        Globals.BattleInfo["RelicsDict"][Relic] = {"Reference":Reference, "Available":1}
        ApllyRarity(Relic)
    # STAGE SMCARD
    RelicsList = []
    for Relic in RelicsList:
        Globals.BattleInfo["EffectStages"]["ProcessingStageSMCARD"][Relic] = Reference
        Globals.BattleInfo["RelicsDict"][Relic] = {"Reference":Reference, "Available":1}
        ApllyRarity(Relic)

    # STAGE CRSR
    RelicsList = []
    for Relic in RelicsList:
        Globals.BattleInfo["EffectStages"]["ProcessingStageCRSR"][Relic] = Reference
        Globals.BattleInfo["RelicsDict"][Relic] = {"Reference":Reference, "Available":1}
        ApllyRarity(Relic)
    # STAGE EXSR
    RelicsList = []
    for Relic in RelicsList:
        Globals.BattleInfo["EffectStages"]["ProcessingStageEXSR"][Relic] = Reference
        Globals.BattleInfo["RelicsDict"][Relic] = {"Reference":Reference, "Available":1}
        ApllyRarity(Relic)

    # STAGE ProcessingUniversalEffects
    RelicsList = []
    for Relic in RelicsList:
        Globals.BattleInfo["EffectStages"]["ProcessingUniversalEffects"][Relic] = Reference
        Globals.BattleInfo["RelicsDict"][Relic] = {"Reference":Reference, "Available":1}
        ApllyRarity(Relic)
def GetText(self, Relic):
    if Relic == "BandAid":
        return "Band Aid"
    elif Relic == "SharpeningStone":
        return "Sharpening Stone"
    elif Relic == "ClothArmor":
        return "Cloth Armor"
    else:
        return Relic

def GainRelic(self, Relic):
    Globals.BattleInfo["RelicsDict"][Relic]["Available"] = 0
    Globals.BattleInfo["Relics"][Relic] = {"Active":1, "OtherData":{}}
def LoseRelic(self, Relic):
    ""

def getIcon(self, Relic):
    if Relic == "BandAid":
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
        IconWidget.setToolTip(f'''Band Aid, Heal 1 more hp each healing action''')
    elif Relic == "SharpeningStone":
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
        IconWidget.setToolTip(f'''Sharpening Stone, Deal 1 more damage each damaging action''')
    elif Relic == "ClothArmor":
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
        IconWidget.setToolTip(f'''Cloth Armor, Start of combat gain 5 Shield. Gain 1 more shield each shielding action''')
    return IconWidget

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

    try:
        if Data["Effect"] == "BandAid":
            if Data["OriginalData"]["Healing"] > 0:
                Data["FinalData"]["Healing"] += 1
        elif Data["Effect"] == "SharpeningStone":
            if Data["OriginalData"]["Damage"] > 0:
                Data["FinalData"]["Damage"] += 1
        elif Data["Effect"] == "ClothArmor":
            if Data["OriginalData"]["Shield"] > 0:
                Data["FinalData"]["Shield"] += 1
    except Exception as e:
        Log(2, "ERROR RELIC TRIGGER", Data, Source)
        ""
    return Data
def EffectConfirmed(OriginalData, FinalData, Results):
    # print("EffectConfirmed")
    ""
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
    except:
        ""
