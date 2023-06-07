from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QTextCursor

import os
import sys

Enemies = {}

Allies = {}

DeadEnemies = {}

SelfStatus = {}
SelfStatus["DangerLevel"] = 1

MainWindow = {}

SkillRolls = {}

CurrentHand = {}

CurrentDeck = []

DiscardDeck = []

BattleInfo = {"Target":[], "Allies":{}, "Enemies":{},"SR":[],"Attack":'',"Deck":{"WholeDeck":[],"DrawDeck":[],"DiscardDeck":[],"CurrentHand":[], "ExhaustDeck":[]}, "CurrentCard":"", "IDCounter":0, "EffectStages":{"ProcessingStage1":{}, "ProcessingStage2":{}, "ProcessingStage3":{}, "ProcessingStageSOT":{}, "ProcessingStageEOT":{}, "ProcessingStageCRSR":{}, "ProcessingStageEXSR":{}, "ProcessingStageDRCARD":{}, "ProcessingStageDCCARD":{}, "ProcessingStageSMCARD":{}, "ProcessingStageEXCARD":{},  "UniversalEffects":{}, "ProcessingUniversalEffects":{}}, "EffectsDict":{}, "RelicsDict":{}, "Relics":{} }
# UniversalEffect = 'ID':[Level, Duration, Parent/Source]


Cards = {}

Decks = {}

Effects = {}

def retrieveEnemies():

    EnemiesPath = os.path.abspath(__file__)
    nameLength = len(os.path.basename(__file__))
    fullLength = len(EnemiesPath)
    EnemiesPath = EnemiesPath[0:fullLength-nameLength]
    EnemiesPath += "Combat\\Enemies"
    if EnemiesPath not in sys.path:
        sys.path.insert(0, EnemiesPath)

    x = os.listdir("Combat/Enemies")
    EnemyData = {}
    for file in x:
        if ".py" in file:
            file = file[0:len(file)-3]
            try:
                Enemy = __import__(file)
                BaseData = Enemy.Enemy.BaseData("Oh")
                EnemyData[file] = BaseData
            except:
                print("NOoo")
    return EnemyData

References = {}

PartyObjects = {}

Keys = {}

Layouts = {}

Animations = {}

BattleObjects = {"Allies":{}, "Enemies":{}}
# BattleObjects = {"Allies":{}, "Enemies":{"BanditThief0":{"Object":'', "Widget":''} }}

Threads = {}

FinishedThreads = []

BattleAniData = {}

AnimationData = {}

EffectsData = {}

EffectsDict = {}

EventData = {}

LayoutsData = {"ReturnToLayout":'', "Active":'', "Previous":''}


SoLNPCData = {}
SoLPCData = {}
SoLTempData = {}
SoLOtherData = {}
SoLEnviorementData = {}
SoLNPCSchedules = {}
Commands = {}
SoLTraits = {}
SoLAbilities = {}

### SETS UP THE GLOBAL DICTS
SoLPValues = {}
SoLTValues = {}
SoLGValues = {}
EventCommands = {}
SoLNPCFunctions = {}
ControlCommands = {}
SoLPersonalities = {}
SoLFallenStates = {}
Locations = {}
Signals = {}
SignalData = {"CommandCheckSignal":{"OtherData":{}},
    "RefreshSignal1":{"OtherData":{}},
    "RefreshSignal2":{"OtherData":{}},
    "RefreshSignal3":{"OtherData":{}},
    "CTS1":{ "Values":{"CommandID":"", "Target":"", "Actor":""}, "OtherData":{} },
    "CTS2":{ "Values":{"CommandID":"", "Modification":"", "Implementation":"", "Target":"", "Actor":"", "TargetData":{}, "ActorData":{}}, "OtherData":{} },
    "CTS3":{ "Values":{"Modification":"", "Implementation":"", "OriginalData":{}, "FinalData":{}}, "OtherData":{} },
    }


def Initialize(self, Reference):
    ""
