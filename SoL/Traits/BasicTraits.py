import os
import pathlib
import random

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import Globals

Log = Globals.Layouts["MainF"].Log

def Initialize(self, Reference):


    List = ["Courage0", "Attitude0", "Pride0", "Dere0", "SelfControl0", "Cheerfulness0", "Shyness0", 'Gullible0', "Charm0", "SubstanceResistance0", "SexualInterest0", "Virtue0", "Chastity0", "Openess0", "PainResistance0", "ArousalEase0", "ResponseToPleasure0", "Perversion0", "Dominance0", "Forceful0", "Loyalty0", "Violence0", "Beauty0", "Shame0", "Will0", "Influence0", "Fertility0", "LewdBody0"]
    for TraitID in List:
        Globals.SoLTraits[TraitID] = {"ID":TraitID, "Reference":Reference, "OtherData":{}}

    try:
        Globals.Layouts["SoLUI"].CommandCheckSignal.connect(lambda: TriggerTrait(self, "Chastity0", "CommandCheckSignal"))
    except:
        ""

    Globals.References["SoLFunctions"].Connect("CAS2", CASHandling2)
    # Globals.SignalData["CAS2"] = {"CommandID":CommandID, "ID":ID, "NPCID":NPCID, "Flags":{"Succes":0}, "TargetConnotations":TargetConnotations, "ActorConnotations":ActorConnotations}



# def ProcessingTrait(self, TargetDict, ActorDict, CommandID, Actor, Target, TraitID, Who):
#     return TargetDict, ActorDict
def CASHandling2():
    ""
    # Globals.SignalData["CAS2"] = {"CommandID":CommandID, "ID":ID, "NPCID":NPCID, "Flags":{"Succes":0}, "TargetConnotations":TargetConnotations, "ActorConnotations":ActorConnotations}
    # Actor = Globals.SignalData["CAS2"]["ID"]
    # Target = Globals.SignalData["CAS2"]["NPCID"]
    # if "Courage0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["Courage0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["Courage0"]["Level"] == 1:
    #         print("Brave")
    #         ""
    #     elif Globals.SoLNPCData[Target]["Traits"]["Courage0"]["Level"] == 2:
    #         print("Timid")
    # if "Attitude0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["Attitude0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["Attitude0"]["Level"] == 1:
    #         print("Defiant")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Attitude0"]["Level"] == 2:
    #         print("Docile")
    # if "Pride0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["Pride0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["Pride0"]["Level"] == 1:
    #         print("Prideful")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Pride0"]["Level"] == 2:
    #         print("Humble")
    # if "Dere0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["Dere0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["Dere0"]["Level"] == 1:
    #         print("Tsundere")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Dere0"]["Level"] == 2:
    #         print("Dandere")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Dere0"]["Level"] == 2:
    #         print("Kuudere")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Dere0"]["Level"] == 2:
    #         print("Yandere")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Dere0"]["Level"] == 2:
    #         print("Deredere")
    # if "SelfControl0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["SelfControl0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["SelfControl0"]["Level"] == 1:
    #         print("High")
    #     elif Globals.SoLNPCData[Target]["Traits"]["SelfControl0"]["Level"] == 2:
    #         print("Low")
    # if "Cheerfulness0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["Cheerfulness0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["Cheerfulness0"]["Level"] == 1:
    #         print("Cheerful")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Cheerfulness0"]["Level"] == 2:
    #         print("Gloomy")
    # if "Shyness0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["Shyness0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["Shyness0"]["Level"] == 1:
    #         print("Shy")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Shyness0"]["Level"] == 2:
    #         print("Outgoing")
    # if "Gullible0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["Gullible0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["Gullible0"]["Level"] == 1:
    #         print("Gullible")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Gullible0"]["Level"] == 2:
    #         print("Untrusting")
    # if "Charm0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["Charm0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["Charm0"]["Level"] == 1:
    #         print("Charming")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Charm0"]["Level"] == 2:
    #         print("Charmless")
    # if "SubstanceResistance0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["SubstanceResistance0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["SubstanceResistance0"]["Level"] == 1:
    #         print("Resistant")
    #     elif Globals.SoLNPCData[Target]["Traits"]["SubstanceResistance0"]["Level"] == 2:
    #         print("Weak")
    # if "SexualInterest0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["SexualInterest0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["SexualInterest0"]["Level"] == 1:
    #         print("Curious")
    #     elif Globals.SoLNPCData[Target]["Traits"]["SexualInterest0"]["Level"] == 2:
    #         print("Conservative")
    # if "Virtue0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["Virtue0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["Virtue0"]["Level"] == 1:
    #         print("Virtuous")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Virtue0"]["Level"] == 2:
    #         print("Depraved")
    # if "Chastity0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["Chastity0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["Chastity0"]["Level"] == 1:
    #         print("Not for Lewding")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Chastity0"]["Level"] == 2:
    #         print("Chaste")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Chastity0"]["Level"] == 2:
    #         print("Unchaste")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Chastity0"]["Level"] == 2:
    #         print("Slutty")
    # if "Openess" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["Openess"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["Openess"]["Level"] == 1:
    #         print("Liberated")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Openess"]["Level"] == 2:
    #         print("Repressed")
    # if "PainResistance0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["PainResistance0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["PainResistance0"]["Level"] == 1:
    #         print("High")
    #     elif Globals.SoLNPCData[Target]["Traits"]["PainResistance0"]["Level"] == 2:
    #         print("Low")
    # if "ArousalEase0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["ArousalEase0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["ArousalEase0"]["Level"] == 1:
    #         print("Easy")
    #     elif Globals.SoLNPCData[Target]["Traits"]["ArousalEase0"]["Level"] == 2:
    #         print("Hard")
    # if "ResponseToPleasure0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["ResponseToPleasure0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["ResponseToPleasure0"]["Level"] == 1:
    #         print("Enjoys")
    #     elif Globals.SoLNPCData[Target]["Traits"]["ResponseToPleasure0"]["Level"] == 2:
    #         print("Denies")
    # if "Perversion0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["Perversion0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["Perversion0"]["Level"] == 1:
    #         print("Perverted")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Perversion0"]["Level"] == 2:
    #         print("Pure")
    # if "Dominance0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["Dominance0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["Dominance0"]["Level"] == 1:
    #         print("Submissive")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Dominance0"]["Level"] == 2:
    #         print("Dominant")
    # if "Forceful0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["Forceful0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["Forceful0"]["Level"] == 1:
    #         print("Forceful")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Forceful0"]["Level"] == 2:
    #         print("Exploitable")
    # if "Loyalty0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["Loyalty0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["Loyalty0"]["Level"] == 1:
    #         print("Loyal")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Loyalty0"]["Level"] == 2:
    #         print("Disloyal")
    # if "Violence0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["Violence0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["Violence0"]["Level"] == 1:
    #         print("Violent")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Violence0"]["Level"] == 2:
    #         print("Meek")
    # if "Beauty0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["Beauty0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["Beauty0"]["Level"] == 1:
    #         print("Gorgeous")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Beauty0"]["Level"] == 2:
    #         print("Beautiful")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Beauty0"]["Level"] == 2:
    #         print("Ugly")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Beauty0"]["Level"] == 2:
    #         print("Disfigured")
    # if "Shame0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["Shame0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["Shame0"]["Level"] == 1:
    #         print("Shameful")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Shame0"]["Level"] == 2:
    #         print("Shameless")
    # if "Will0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["Will0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["Will0"]["Level"] == 1:
    #         print("Strong Willed")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Will0"]["Level"] == 2:
    #         print("Weak Willed")
    # if "Influence0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["Influence0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["Influence0"]["Level"] == 1:
    #         print("Corruptor")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Influence0"]["Level"] == 2:
    #         print("Purificator")
    # if "Fertility0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["Fertility0"]["Level"] != 0:
    #     if Globals.SoLNPCData[Target]["Traits"]["Fertility0"]["Level"] == 1:
    #         print("Hyper Fertile")
    #     elif Globals.SoLNPCData[Target]["Traits"]["Fertility0"]["Level"] == 2:
    #         print("Infertile")
    # if "LewdBody0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["Courage0"]["Level"] != 0:
    #     ""
    #     # if Globals.SoLNPCData[Target]["Traits"]["Courage0"]["Level"] == 1:
    #     #     print("Brave")
    #     # elif Globals.SoLNPCData[Target]["Traits"]["Courage0"]["Level"] == 2:
    #     #     print("Timid")



def TraitChange(TraitID, NPCID, Data, Value):
    Data["Level"] = Value
    Globals.SoLNPCData[NPCID]["Traits"][TraitID] = Data

    # if TraitID == "Courage0":
    #     ""

    Globals.LayoutsData["Active"].Refresh()

def GetTraitSelection(self, TraitID):
    # if TraitID == "Shy0":
    #     Label = QLabel()
    #     Label.setText("Shyness")
    #     Label.setMinimumWidth(250)
    #     Label.setMaximumWidth(250)
    #     Label.setMinimumHeight(50)
    #     Label.setMaximumHeight(50)
    #     return Label
    try:
        if TraitID == "Courage0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Courage", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Brave")
            TraitWidget.TraitBox.addItem("Timid")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)

            TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')


            return TraitWidget
        elif TraitID == "Attitude0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Attitude", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Defiant")
            TraitWidget.TraitBox.addItem("Docile")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "Pride0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Pride", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Prideful")
            TraitWidget.TraitBox.addItem("Humble")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "Dere0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Dere", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Tsundere")
            TraitWidget.TraitBox.addItem("Dandere")
            TraitWidget.TraitBox.addItem("Kuudere")
            TraitWidget.TraitBox.addItem("Yandere")
            TraitWidget.TraitBox.addItem("Deredere")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "SelfControl0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Self Control", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("High")
            TraitWidget.TraitBox.addItem("Low")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "Cheerfulness0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Cheerfulness", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Cheerful")
            TraitWidget.TraitBox.addItem("Gloomy")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "Shyness0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Shyness", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Shy")
            TraitWidget.TraitBox.addItem("Outgoing")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "Gullible0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Gullible", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Gullible")
            TraitWidget.TraitBox.addItem("Untrusting")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "Charm0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Charm", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Charming")
            TraitWidget.TraitBox.addItem("Charmless")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "SubstanceResistance0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Substance Resistance", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Resistant")
            TraitWidget.TraitBox.addItem("Weak")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "SexualInterest0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Sexual Interest", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Curious")
            TraitWidget.TraitBox.addItem("Conservative")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "Virtue0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Virtue", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Virtuous")
            TraitWidget.TraitBox.addItem("Depraved")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "Chastity0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Chastity", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Not for Lewding")
            TraitWidget.TraitBox.addItem("Chaste")
            TraitWidget.TraitBox.addItem("Unchaste")
            TraitWidget.TraitBox.addItem("Slutty")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "Openess0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Openess", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Liberated")
            TraitWidget.TraitBox.addItem("Repressed")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "PainResistance0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Pain Resistance", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("High")
            TraitWidget.TraitBox.addItem("Low")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "ArousalEase0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Arousal Ease", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Easy")
            TraitWidget.TraitBox.addItem("Hard")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "ResponseToPleasure0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Response To Pleasure", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Enjoys")
            TraitWidget.TraitBox.addItem("Denies")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "Perversion0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Perversion", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Perverted")
            TraitWidget.TraitBox.addItem("Pure")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "Dominance0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Dominance", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Submissive")
            TraitWidget.TraitBox.addItem("Dominant")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "Forceful0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Forceful", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Forceful")
            TraitWidget.TraitBox.addItem("Exploitable")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "Loyalty0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Loyalty", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Loyal")
            TraitWidget.TraitBox.addItem("Disloyal")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "Violence0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Violence", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Violent")
            TraitWidget.TraitBox.addItem("Meek")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "Beauty0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Beauty", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Gorgeous")
            TraitWidget.TraitBox.addItem("Beautiful")
            TraitWidget.TraitBox.addItem("Ugly")
            TraitWidget.TraitBox.addItem("Disfigured")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "Shame0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Shame", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Shameful")
            TraitWidget.TraitBox.addItem("Shameless")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "Will0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Will", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Strong Willed")
            TraitWidget.TraitBox.addItem("Weak Willed")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "Influence0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Influence", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Corruptor")
            TraitWidget.TraitBox.addItem("Purificator")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "Fertility0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Fertility", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitBox = QComboBox(TraitWidget)
            TraitWidget.TraitBox.setGeometry(0, 40, 200, 35)
            TraitWidget.TraitBox.addItem("---")
            TraitWidget.TraitBox.addItem("Hyper Fertile")
            TraitWidget.TraitBox.addItem("Infertile")

            def FuncReturnValue(Widget):
                Value = Widget.TraitBox.currentIndex()
                Data = {"ID":TraitID, "Level":Value,"OtherData":{}}
                return Data
            def FuncLoadValue(Widget, Data):
                Value = Data["Level"]
                Widget.TraitBox.setCurrentIndex(Value)

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget
        elif TraitID == "LewdBody0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Lewd Body Parts", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)

            TraitWidget.VLewdLabel = QLabel("V", TraitWidget)
            TraitWidget.VLewdLabel.setGeometry(25,40,25,25)
            TraitWidget.VLewdBox = QCheckBox(TraitWidget)
            TraitWidget.VLewdBox.setGeometry(30,65,15,15)
            TraitWidget.VLewdBox.setChecked(False)

            TraitWidget.ALewdLabel = QLabel("A", TraitWidget)
            TraitWidget.ALewdLabel.setGeometry(55,40,25,25)
            TraitWidget.ALewdBox = QCheckBox(TraitWidget)
            TraitWidget.ALewdBox.setGeometry(60,65,15,15)
            TraitWidget.ALewdBox.setChecked(False)

            TraitWidget.BLewdLabel = QLabel("B", TraitWidget)
            TraitWidget.BLewdLabel.setGeometry(85,40,25,25)
            TraitWidget.BLewdBox = QCheckBox(TraitWidget)
            TraitWidget.BLewdBox.setGeometry(90,65,15,15)
            TraitWidget.BLewdBox.setChecked(False)

            TraitWidget.PLewdLabel = QLabel("P", TraitWidget)
            TraitWidget.PLewdLabel.setGeometry(115,40,25,25)
            TraitWidget.PLewdBox = QCheckBox(TraitWidget)
            TraitWidget.PLewdBox.setGeometry(120,65,15,15)
            TraitWidget.PLewdBox.setChecked(False)

            TraitWidget.MLewdLabel = QLabel("M", TraitWidget)
            TraitWidget.MLewdLabel.setGeometry(145,40,25,25)
            TraitWidget.MLewdBox = QCheckBox(TraitWidget)
            TraitWidget.MLewdBox.setGeometry(150,65,15,15)
            TraitWidget.MLewdBox.setChecked(False)
            TraitWidget.setGeometry(1025,230,202,82)



            def FuncReturnValue(Widget):
                V = TraitWidget.VLewdBox.isChecked()
                A = TraitWidget.ALewdBox.isChecked()
                B = TraitWidget.BLewdBox.isChecked()
                P = TraitWidget.PLewdBox.isChecked()
                M = TraitWidget.MLewdBox.isChecked()
                Dict = {"ID":TraitID, "V":V, "A":A, "B":B, "P":P, "M":M, "OtherData":{}}
                return Dict
            def FuncLoadValue(Widget, Dict):
                Widget.VLewdBox.setChecked(Dict["V"])
                Widget.ALewdBox.setChecked(Dict["A"])
                Widget.BLewdBox.setChecked(Dict["B"])
                Widget.PLewdBox.setChecked(Dict["P"])
                Widget.MLewdBox.setChecked(Dict["M"])

            TraitWidget.ReturnValue = FuncReturnValue
            TraitWidget.LoadValue = FuncLoadValue

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget

    except Exception as e:
        print("Error", e)


def TriggerTrait(self, TraitID, Source):
    try:
        if Source == "CommandCheckSignal":
            CommandID = Globals.SignalData["CommandCheckSignal"]["CommandID"]
            Status = Globals.SignalData["CommandCheckSignal"]["Status"]
            Actor = Globals.SignalData["CommandCheckSignal"]["Actor"]
            Target = Globals.SignalData["CommandCheckSignal"]["Target"]
            if TraitID == "Chastity0":
                if "Chastity0" in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"]["Chastity0"] == 1:
                    TargetConnotations, ActorConnotations = Globals.Commands[CommandID]["Reference"].GetConnotations(self, CommandID, Actor, Target, {"Success":2})
                    if "Sexual" in TargetConnotations or "SHarassement" in TargetConnotations: Globals.SignalData["CommandCheckSignal"]["Status"] = 0
    except Exception as e:
        Log(3, "ERROR TRIGGERING TRAIT", e, __name__, TraitID, Source)

def GetTraitStaticWidget(self, TraitID, NPCData):
    try:
        try:
            Value = NPCData["Traits"][TraitID]["Level"]
        except:
            Value = 0
        if TraitID == "Courage0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Courage", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Brave")
            elif Value == 2:
                TraitValue.setText("Timid")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "Attitude0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Attitude", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Defiant")
            elif Value == 2:
                TraitValue.setText("Docile")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "Pride0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Pride", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Prideful")
            elif Value == 2:
                TraitValue.setText("Humble")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "Dere0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Dere", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Tsundere")
            elif Value == 2:
                TraitValue.setText("Dandere")
            elif Value == 3:
                TraitValue.setText("Kuudere")
            elif Value == 4:
                TraitValue.setText("Yandere")
            elif Value == 5:
                TraitValue.setText("Deredere")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "SelfControl0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Self Control", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("High")
            elif Value == 2:
                TraitValue.setText("Low")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "Cheerfulness0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Cheerfulness", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Cheerful")
            elif Value == 2:
                TraitValue.setText("Gloomy")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "Shyness0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Shyness", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Shy")
            elif Value == 2:
                TraitValue.setText("Outgoing")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "Gullible0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Gullible", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Gullible")
            elif Value == 2:
                TraitValue.setText("Untrusting")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "Charm0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Charm", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Charming")
            elif Value == 2:
                TraitValue.setText("Charmless")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "SubstanceResistance0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Substance Resistance", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Resistant")
            elif Value == 2:
                TraitValue.setText("Weak")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "SexualInterest0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Sexual Interest", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Curious")
            elif Value == 2:
                TraitValue.setText("Conservative")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "Virtue0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Virtue", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Virtuous")
            elif Value == 2:
                TraitValue.setText("Depraved")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "Chastity0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Chastity", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Not for Lewding")
            elif Value == 2:
                TraitValue.setText("Chaste")
            elif Value == 3:
                TraitValue.setText("Unchaste")
            elif Value == 4:
                TraitValue.setText("Slutty")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "Openess0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Openess", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Liberated")
            elif Value == 2:
                TraitValue.setText("Repressed")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "PainResistance0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Pain Resistance", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("High")
            elif Value == 2:
                TraitValue.setText("Low")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "ArousalEase0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Arousal Ease", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Easy")
            elif Value == 2:
                TraitValue.setText("Hard")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "ResponseToPleasure0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Response To Pleasure", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Enjoys")
            elif Value == 2:
                TraitValue.setText("Denies")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "Perversion0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Perversion", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Perverted")
            elif Value == 2:
                TraitValue.setText("Pure")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "Dominance0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Dominance", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Submissive")
            elif Value == 2:
                TraitValue.setText("Dominant")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "Forceful0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Forceful", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Forceful")
            elif Value == 2:
                TraitValue.setText("Exploitable")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "Loyalty0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Loyalty", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Loyal")
            elif Value == 2:
                TraitValue.setText("Disloyal")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "Violence0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Violence", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Violent")
            elif Value == 2:
                TraitValue.setText("Meek")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "Beauty0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Beauty", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Gorgeous")
            elif Value == 2:
                TraitValue.setText("Beautiful")
            elif Value == 3:
                TraitValue.setText("Ugly")
            elif Value == 4:
                TraitValue.setText("Disfigured")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "Shame0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Shame", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Shameful")
            elif Value == 2:
                TraitValue.setText("Shameless")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "Will0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Will", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Strong Willed")
            elif Value == 2:
                TraitValue.setText("Weak Willed")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "Influence0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Influence", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Corruptor")
            elif Value == 2:
                TraitValue.setText("Purificator")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "Fertility0":
            TraitWidget = QWidget()

            TraitLabel = QLabel("Fertility", TraitWidget)
            TraitLabel.setGeometry(0, 0, 200, 35)
            TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitLabel.setFont(QFont('Segoe UI', 14))
            TraitValue = QLabel(TraitWidget)
            TraitValue.setGeometry(0, 40, 200, 35)
            TraitValue.setFont(QFont('Segoe UI', 12))

            if Value == 1:
                TraitValue.setText("Hyper Fertile")
            elif Value == 2:
                TraitValue.setText("Infertile")

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            # TraitWidget.setToolTip('Courage, affects the Resistance and Discomfort values.')
            return TraitWidget
        elif TraitID == "LewdBody0":
            TraitWidget = QWidget()

            TraitWidget.TraitLabel = QLabel("Lewd Body Parts", TraitWidget)
            TraitWidget.TraitLabel.setGeometry(0, 0, 200, 35)
            TraitWidget.TraitLabel.setAlignment(QtCore.Qt.AlignCenter)
            TraitWidget.TraitLabel.setFont(QFont('Segoe UI', 14))

            TraitWidget.VLewdLabel = QLabel("V", TraitWidget)
            TraitWidget.VLewdLabel.setGeometry(25,40,25,25)
            TraitWidget.VLewdLabel.setFont(QFont('Segoe UI', 12))
            TraitWidget.VLewdLabel.setAlignment(Qt.AlignCenter)
            TraitWidget.VLewdBox = QCheckBox(TraitWidget)
            TraitWidget.VLewdBox.setGeometry(30,65,15,15)
            if NPCData["Traits"]["LewdBody0"]["V"] == 1:
                TraitWidget.VLewdBox.setChecked(True)
            else:
                TraitWidget.VLewdBox.setChecked(False)

            TraitWidget.ALewdLabel = QLabel("A", TraitWidget)
            TraitWidget.ALewdLabel.setGeometry(55,40,25,25)
            TraitWidget.ALewdLabel.setFont(QFont('Segoe UI', 12))
            TraitWidget.ALewdLabel.setAlignment(Qt.AlignCenter)
            TraitWidget.ALewdBox = QCheckBox(TraitWidget)
            TraitWidget.ALewdBox.setGeometry(60,65,15,15)
            TraitWidget.ALewdBox.setChecked(False)
            if NPCData["Traits"]["LewdBody0"]["A"] == 1:
                TraitWidget.ALewdBox.setChecked(True)
            else:
                TraitWidget.ALewdBox.setChecked(False)

            TraitWidget.BLewdLabel = QLabel("B", TraitWidget)
            TraitWidget.BLewdLabel.setGeometry(85,40,25,25)
            TraitWidget.BLewdLabel.setFont(QFont('Segoe UI', 12))
            TraitWidget.BLewdLabel.setAlignment(Qt.AlignCenter)
            TraitWidget.BLewdBox = QCheckBox(TraitWidget)
            TraitWidget.BLewdBox.setGeometry(90,65,15,15)
            TraitWidget.BLewdBox.setChecked(False)
            if NPCData["Traits"]["LewdBody0"]["B"] == 1:
                TraitWidget.BLewdBox.setChecked(True)
            else:
                TraitWidget.BLewdBox.setChecked(False)

            TraitWidget.PLewdLabel = QLabel("P", TraitWidget)
            TraitWidget.PLewdLabel.setGeometry(115,40,25,25)
            TraitWidget.PLewdLabel.setFont(QFont('Segoe UI', 12))
            TraitWidget.PLewdLabel.setAlignment(Qt.AlignCenter)
            TraitWidget.PLewdBox = QCheckBox(TraitWidget)
            TraitWidget.PLewdBox.setGeometry(120,65,15,15)
            TraitWidget.PLewdBox.setChecked(False)
            if NPCData["Traits"]["LewdBody0"]["P"] == 1:
                TraitWidget.PLewdBox.setChecked(True)
            else:
                TraitWidget.PLewdBox.setChecked(False)

            TraitWidget.MLewdLabel = QLabel("M", TraitWidget)
            TraitWidget.MLewdLabel.setGeometry(145,40,25,25)
            TraitWidget.MLewdLabel.setFont(QFont('Segoe UI', 12))
            TraitWidget.MLewdLabel.setAlignment(Qt.AlignCenter)
            TraitWidget.MLewdBox = QCheckBox(TraitWidget)
            TraitWidget.MLewdBox.setGeometry(150,65,15,15)
            TraitWidget.MLewdBox.setChecked(False)
            if NPCData["Traits"]["LewdBody0"]["M"] == 1:
                TraitWidget.MLewdBox.setChecked(True)
            else:
                TraitWidget.MLewdBox.setChecked(False)

            def Oh():
                if NPCData["Traits"]["LewdBody0"]["V"] == 0: TraitWidget.VLewdBox.setChecked(0)
                else: TraitWidget.VLewdBox.setChecked(2)
                if NPCData["Traits"]["LewdBody0"]["A"] == 0: TraitWidget.ALewdBox.setChecked(0)
                else: TraitWidget.ALewdBox.setChecked(2)
                if NPCData["Traits"]["LewdBody0"]["B"] == 0: TraitWidget.BLewdBox.setChecked(0)
                else: TraitWidget.BLewdBox.setChecked(2)
                if NPCData["Traits"]["LewdBody0"]["P"] == 0: TraitWidget.PLewdBox.setChecked(0)
                else: TraitWidget.PLewdBox.setChecked(2)
                if NPCData["Traits"]["LewdBody0"]["M"] == 0: TraitWidget.MLewdBox.setChecked(0)
                else: TraitWidget.MLewdBox.setChecked(2)


            TraitWidget.VLewdBox.clicked.connect(Oh)
            TraitWidget.ALewdBox.clicked.connect(Oh)
            TraitWidget.BLewdBox.clicked.connect(Oh)
            TraitWidget.PLewdBox.clicked.connect(Oh)
            TraitWidget.MLewdBox.clicked.connect(Oh)

            TraitWidget.setGeometry(1025,230,202,82)

            TraitWidget.setMinimumWidth(200)
            TraitWidget.setMaximumWidth(200)
            TraitWidget.setMinimumHeight(80)
            TraitWidget.setMaximumHeight(80)
            return TraitWidget

    except Exception as e:
        print("Error", e)

    return None

def GetTraitConditions(TraitID, NPCID, OtherID, Flags):
    Gems = Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]
    # AbilitiesList = ["Obedience", "Lust", "Intimacy", "Submission", "Superiority", "CSense", "VSense", "ASense", "PSense", "MSense", "Service", "Sadism", "Masochism", "Exhibitionism"]

    # GemsList = ["Favor", "Loyalty", "Hate", "Submission", "Superiority", "PPlea", "Service", "Pain", "Shame", "Fear", "Desire", "APlea", "VPlea", "CPlea", "BPlea", "MPlea"]
    # "Temporal":{ "Favor": 15, "Loyalty": 5, "Desire": 0, "Obedience": 0, "Superiority": 0, "Submission": 0, "Servicing": 0, "Shame": 0, "MPlea": 0, "CPlea": 0, "APlea": 0, "VPlea": 0, "PPlea": 0, "Pain": 0, "Fear": 0, "Discomfort": 5, "Hate": 0,},
    Dict = {}
    try:
        Value = 0
        try:
            Value = Globals.SoLNPCData[NPCID]["Traits"][TraitID]["Level"]
        except:
            ""
        if TraitID == "Courage0":
            # 1: Brave
                # Gain: 1500 Superiority Gems
                # Lose: 1500 Fear Gems
            # 2: Timid
                # Gain: 1500 Fear Gems
                # Lose: 1500 Superiority Gems
            Dict[0] = {"Level":0, "Title":"---", "Text":"", "Available":0}

            Dict[1] = {"Level":1, "Title":"Brave", "Text":"1500 Superiority Gems", "Available":0}
            if (("Superiority" in Gems and Gems["Superiority"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[1]["Available"] = 1

            Dict[2] = {"Level":2, "Title":"Timid", "Text":"1500 Fear Gems", "Available":0}
            if (("Fear" in Gems and Gems["Fear"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[2]["Available"] = 1

            if Value != 0:
                if Value == 1:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Fear Gems", "Available":0}
                    if ("Fear" in Gems and Gems["Fear"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
                elif Value == 2:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Superiority Gems", "Available":0}
                    if ("Superiority" in Gems and Gems["Superiority"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
        elif TraitID == "Attitude0":
            # 1: Defiant
                # Gain: 1500 Superiority Gems + Sadism Gems
                # Lose: 1500 Obedience
            # 2: Docile
                # Gain: 2500 Obedience Gems + Submission Gems
                # Lose: 1500 Superioirty + Sadism gems
            Dict[0] = {"Level":0, "Title":"---", "Text":"", "Available":0}

            Sum = 0
            if  "Superiority" in Gems: Sum += Gems["Superiority"]["Amount"]
            if "Sadism" in Gems: Sum += Gems["Saidsm"]["Amount"]
            Dict[1] = {"Level":1, "Title":"Defiant", "Text":"1500 Superiority Gems + Sadism Gems", "Available":0}
            if ((Sum >= 1500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[1]["Available"] = 1

            Sum = 0
            if  "Obedience" in Gems: Sum += Gems["Obedience"]["Amount"]
            if "Submission" in Gems: Sum += Gems["Submission"]["Amount"]
            Dict[2] = {"Level":2, "Title":"Docile", "Text":"2500 Obedience Gems + Submission Gems", "Available":0}
            if ((Sum >= 1500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[2]["Available"] = 1

            if Value != 0:
                if Value == 1:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Obedience Gems", "Available":0}
                    if ("Obedience" in Gems and Gems["Obedience"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1

                elif Value == 2:
                    Sum = 0
                    if  "Superioirty" in Gems: Sum += Gems["Superioirty"]["Amount"]
                    if "Sadism" in Gems: Sum += Gems["Sadism"]["Amount"]
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Superioirty + Sadism Gems", "Available":0}
                    if Sum >= 1500 or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
        elif TraitID == "Pride0":
            # 1: Prideful
                # Gain: 1500 Superiority
                # Lose: 2500 Submission Gems + Obedience Gems
            # 2: Humble
                # Gain: 2500 Obedience + Submission Gems
                # Lose: 1500 Superiority
            Dict[0] = {"Level":0, "Title":"---", "Text":"", "Available":0}

            Dict[1] = {"Level":1, "Title":"Prideful", "Text":"1500 Superiority Gems", "Available":0}
            if (("Superiority" in Gems and Gems["Superiority"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[1]["Available"] = 1

            Sum = 0
            if  "Obedience" in Gems: Sum += Gems["Obedience"]["Amount"]
            if "Submission" in Gems: Sum += Gems["Submission"]["Amount"]
            Dict[2] = {"Level":2, "Title":"Humble", "Text":"2500 Obedience + Submission Gems", "Available":0}
            if ((Sum >= 1500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[2]["Available"] = 1

            if Value != 0:
                if Value == 1:
                    Sum = 0
                    if  "Obedience" in Gems: Sum += Gems["Obedience"]["Amount"]
                    if "Submission" in Gems: Sum += Gems["Submission"]["Amount"]
                    Dict[0] = {"Level":0, "Title":"---", "Text":"2500 Submission Gems + Obedience Gems", "Available":0}
                    if (Sum >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
                elif Value == 2:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Superiority Gems", "Available":0}
                    if ("Superiority" in Gems and Gems["Superiority"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
        elif TraitID == "Dere0":
            # 1: Tsundere
                # Gain: 1000 Superiority Gems / 500 Favor Gems
                # Lose: 500 loyalty Gems / 1000 Favor Gems
            # 2: Dandere
                # Gain: 1000 Fear Gems / 500 Pain Gems
                # Lose: 1000 Superiority Gems / 500 Shame Gems
            # 3: Kuudere
                # Gain: 1000 Fear Gems / 1000 Shame Gems
                # Lose: 1500 Favor Gems / 500 Reliability Gems
            # 4: Yandere
                # Gain: 500 Favor Gems / 1000 Lust Gems
                # Lose: Lvl 5 Sumbission / Lvl 5 Intimacy
            # 5: Deredere
                # Gain: 2000 Favor Gems
                # Lose: 1000 Pain Gems / 500 Fear Gems
            Dict[0] = {"Level":0, "Title":"---", "Text":"Not A Dere", "Available":0}
            Dict[1] = {"Level":1, "Title":"Tsundere", "Text":"1000 Superiority Gems / 500 Favor Gems", "Available":0}
            if (("Superiority" in Gems and Gems["Superiority"]["Amount"] >= 1000 and "Favor" in Gems and Gems["Favor"]["Amount"] >= 500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[1]["Available"] = 1

            Dict[2] = {"Level":2, "Title":"Dandere", "Text":"1000 Fear Gems / 500 Pain Gems", "Available":0}
            if (("Fear" in Gems and Gems["Fear"]["Amount"] >= 1000 and "Pain" in Gems and Gems["Pain"]["Amount"] >= 500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[2]["Available"] = 1

            Dict[3] = {"Level":3, "Title":"Kuudere", "Text":"1000 Fear Gems / 1000 Shame Gems", "Available":0}
            if (("Fear" in Gems and Gems["Fear"]["Amount"] >= 1000 and "Shame" in Gems and Gems["Shame"]["Amount"] >= 1000) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[3]["Available"] = 1

            Dict[4] = {"Level":4, "Title":"Yandere", "Text":"500 Favor Gems / 1000 Lust Gems", "Available":0}
            if (("Favor" in Gems and Gems["Favor"]["Amount"] >= 500 and "Lust" in Gems and Gems["Lust"] >= 1000) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[4]["Available"] = 1

            Dict[5] = {"Level":5, "Title":"Deredere", "Text":"2000 Favor Gems", "Available":0}
            if (("Favor" in Gems and Gems["Favor"]["Amount"] >= 2000) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[5]["Available"] = 1

            if Value != 0:
                if Globals.SoLNPCData[NPCID]["Traits"][TraitID]["Level"] == 1:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"500 Loyalty Gems / 1000 Favor Gems", "Available":0}
                    if ("Loyalty" in Gems and Gems["Loyalty"]["Amount"] >  500 and "Favor" in Gems and Gems["Favor"]["Amount"] >  1000) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
                elif Globals.SoLNPCData[NPCID]["Traits"][TraitID]["Level"] == 2:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1000 Superiority Gems / 500 Shame Gems", "Available":0}
                    if ("Superiority" in Gems and Gems["Superiority"]["Amount"] >  1000 and "Shame" in Gems and Gems["Shame"]["Amount"] >  500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
                elif Globals.SoLNPCData[NPCID]["Traits"][TraitID]["Level"] == 3:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Favor Gems / 500 Reliability Gems", "Available":0}
                    if ("Favor" in Gems and Gems["Favor"]["Amount"] >  1500 and "Reliability" in Gems and Gems["Reliability"] > 500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
                elif Globals.SoLNPCData[NPCID]["Traits"][TraitID]["Level"] == 4:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"< Lvl 5 Sumbission / < Lvl 5 Intimacy", "Available":0}
                    if ("Sumbission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Abilities"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Abilities"]["Submission"]["Level"] >= 5 and "Intimacy" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Abilities"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Abilities"]["Intimacy"]["Level"] >= 5) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
                elif Globals.SoLNPCData[NPCID]["Traits"][TraitID]["Level"] == 5:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1000 Pain Gems / 500 Fear Gems", "Available":0}
                    if ("Pain" in Gems and Gems["Pain"]["Amount"] >  1000 and "Fear" in Gems and Gems["Fear"]["Amount"] >  500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1


            return Dict
        elif TraitID == "SelfControl0":
            # 1 High
                # Gain: 2000 Shame Gems
                # Lose: 2500 Desire Gems
            # 2 Low
                # Gain: 2000 Desire Gems
                # Lose: 2500 Shame Gems
            Dict[0] = {"Level":0, "Title":"---", "Text":"", "Available":0}

            Dict[1] = {"Level":1, "Title":"High", "Text":"2000 Shame Gems", "Available":0}
            if (("Shame" in Gems and Gems["Shame"]["Amount"] >= 2000) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[1]["Available"] = 1

            Dict[2] = {"Level":2, "Title":"Low", "Text":"2000 Desire Gems", "Available":0}
            if (("Desire" in Gems and Gems["Desire"]["Amount"] >= 2000) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[2]["Available"] = 1

            if Value != 0:
                if Value == 1:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"2500 Desire Gems", "Available":0}
                    if ("Desire" in Gems and Gems["Desire"]["Amount"] >= 2500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
                elif Value == 2:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"2500 Shame Gems", "Available":0}
                    if ("Shame" in Gems and Gems["Shame"]["Amount"] >= 2500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
        elif TraitID == "Cheerfulness0":
            # 1 Cheerful
                # Gain: 1500 Favor Gems
                # Lose: 2500 Fear Gems + Pain Gems
            # 2 Gloomy
                # Gain: 2500 Fear Gems + Pain Gems
                # Lose: 2500 Favor Gems
            Dict[0] = {"Level":0, "Title":"---", "Text":"", "Available":0}

            Dict[1] = {"Level":1, "Title":"Cheerful", "Text":"1500 Favor Gems", "Available":0}
            if (("Favor" in Gems and Gems["Favor"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[1]["Available"] = 1

            Sum = 0
            if  "Fear" in Gems: Sum += Gems["Fear"]
            if "Pain" in Gems: Sum += Gems["Pain"]
            Dict[2] = {"Level":2, "Title":"Gloomy", "Text":"2500 Fear Gems + Pain Gems", "Available":0}
            if ((Sum >= 2500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[2]["Available"] = 1

            if Value != 0:
                if Value == 1:
                    Sum = 0
                    if  "Fear" in Gems: Sum += Gems["Fear"]
                    if "Pain" in Gems: Sum += Gems["Pain"]
                    Dict[0] = {"Level":0, "Title":"---", "Text":"2500 Fear Gems + Pain Gems", "Available":0}
                    if Sum >= 2500 or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
                elif Value == 2:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"2500 Favor Gems", "Available":0}
                    if ("Favor" in Gems and Gems["Favor"]["Amount"] >= 2500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
        elif TraitID == "Shyness0":
            # 1: Shy
                # Gain: 1500 Fear Gems
                # Lose: 1500 Shame Gems
            # 2: Outgoing
                # Gain: 1500 Shame Gems
                # Lose: 1500 Fear Gems
            Dict[0] = {"Level":0, "Title":"---", "Text":"", "Available":0}

            Dict[1] = {"Level":1, "Title":"Shy", "Text":"1500 Fear Gems", "Available":0}
            if (("Fear" in Gems and Gems["Fear"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[1]["Available"] = 1

            Dict[2] = {"Level":2, "Title":"Outgoing", "Text":"1500 Shame Gems", "Available":0}
            if (("Shame" in Gems and Gems["Shame"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[2]["Available"] = 1

            if Value != 0:
                if Value == 1:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Shame Gems", "Available":0}
                    if ("Shame" in Gems and Gems["Shame"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
                elif Value == 2:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Fear Gems", "Available":0}
                    if ("Fear" in Gems and Gems["Fear"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
        elif TraitID == "Gullible0":
            # 1: Gullible
                # Gain: 2500 Favor
                # Lose: 1500 Pain
            # 2: Untrusting
                # Gain: 1500 Pain
                # Lose: 2500 Favor
            Dict[0] = {"Level":0, "Title":"---", "Text":"", "Available":0}

            Dict[1] = {"Level":1, "Title":"Gullible", "Text":"2500 Favor Gems", "Available":0}
            if (("Favor" in Gems and Gems["Favor"]["Amount"] >= 2500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[1]["Available"] = 1

            Dict[2] = {"Level":2, "Title":"Untrusting", "Text":"1500 Pain Gems", "Available":0}
            if (("Pain" in Gems and Gems["Pain"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[2]["Available"] = 1

            if Value != 0:
                if Value == 1:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Pain Gems", "Available":0}
                    if ("Pain" in Gems and Gems["Pain"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
                elif Value == 2:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"2500 Favor Gems", "Available":0}
                    if ("Favor" in Gems and Gems["Favor"]["Amount"] >= 2500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
        # elif TraitID == "Charm0":
        #     ""
        #     # TraitWidget.TraitBox.addItem("---")
        #     # TraitWidget.TraitBox.addItem("Charming")
        #     # TraitWidget.TraitBox.addItem("Charmless")
        # elif TraitID == "SubstanceResistance0":
        #     ""
        #     # TraitWidget.TraitBox.addItem("---")
        #     # TraitWidget.TraitBox.addItem("Resistant")
        #     # TraitWidget.TraitBox.addItem("Weak")
        elif TraitID == "SexualInterest0":
            #1: Curious
                # Gain: 2500 Desire
                # Lose: 1500 Service
            #2: Conservative
                # Gain: 1500 Service
                # Lose: 2500 Desire
            Dict[0] = {"Level":0, "Title":"---", "Text":"", "Available":0}

            Dict[1] = {"Level":1, "Title":"Curious", "Text":"2500 Desire Gems", "Available":0}
            if (("Desire" in Gems and Gems["Desire"]["Amount"] >= 2500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[1]["Available"] = 1

            Dict[2] = {"Level":2, "Title":"Conservative", "Text":"1500 Service Gems", "Available":0}
            if (("Service" in Gems and Gems["Service"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[2]["Available"] = 1

            if Value != 0:
                if Value == 1:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Service Gems", "Available":0}
                    if ("Service" in Gems and Gems["Service"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
                elif Value == 2:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"2500 Desire Gems", "Available":0}
                    if ("Desire" in Gems and Gems["Desire"]["Amount"] >= 2500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
        elif TraitID == "Virtue0":
            # 1: Virtuous
                # Gain: 2500 Loyalty Gems
                # Lose: 1500 Desire Gems
            # 2: Depraved
                # Gain: 1500 Desire Gems
                # Lose: 2500 Loyalty Gems
            Dict[0] = {"Level":0, "Title":"---", "Text":"", "Available":0}

            Dict[1] = {"Level":1, "Title":"Virtuous", "Text":"2500 Loyalty Gems", "Available":0}
            if (("Loyalty" in Gems and Gems["Loyalty"]["Amount"] >= 2500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[1]["Available"] = 1

            Dict[2] = {"Level":2, "Title":"Depraved", "Text":"1500 Desire Gems", "Available":0}
            if (("Desire" in Gems and Gems["Desire"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[2]["Available"] = 1

            if Value != 0:
                if Value == 1:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Desire Gems", "Available":0}
                    if ("Desire" in Gems and Gems["Desire"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
                elif Value == 2:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"2500 Loyalty Gems", "Available":0}
                    if ("Loyalty" in Gems and Gems["Loyalty"]["Amount"] >= 2500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
        # elif TraitID == "Chastity0":
        #     ""
        #     # TraitWidget.TraitBox.addItem("---")
        #     # TraitWidget.TraitBox.addItem("Not for Lewding")
        #     # TraitWidget.TraitBox.addItem("Chaste")
        #     # TraitWidget.TraitBox.addItem("Unchaste")
        #     # TraitWidget.TraitBox.addItem("Slutty")
        elif TraitID == "Openess0":
            #1: Liberated
                # Gain: 1500 Desire Gems
                # Lose: 1500 Shame Gems
            #2: Repressed
                # Gain: 1500 Shame Gems
                # Lose: 1500 Desire Gems
            Dict[0] = {"Level":0, "Title":"---", "Text":"", "Available":0}

            Dict[1] = {"Level":1, "Title":"Liberated", "Text":"1500 Desire Gems", "Available":0}
            if (("Desire" in Gems and Gems["Desire"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[1]["Available"] = 1

            Dict[2] = {"Level":2, "Title":"Repressed", "Text":"1500 Shame Gems", "Available":0}
            if (("Shame" in Gems and Gems["Shame"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[2]["Available"] = 1

            if Value != 0:
                if Value == 1:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Shame Gems", "Available":0}
                    if ("Shame" in Gems and Gems["Shame"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
                elif Value == 2:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Desire Gems", "Available":0}
                    if ("Desire" in Gems and Gems["Desire"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
        elif TraitID == "PainResistance0":
            #1: High
                # Gain: 1500 Pain Gems
                # Lose: 1500 Pain Gems
            #2: Low
                # Gain: 1500 Pain Gems
                # Lose: 1500 Pain Gems
            Dict[0] = {"Level":0, "Title":"---", "Text":"", "Available":0}

            Dict[1] = {"Level":1, "Title":"High", "Text":"1500 Pain Gems", "Available":0}
            if (("Pain" in Gems and Gems["Pain"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[1]["Available"] = 1

            Dict[2] = {"Level":2, "Title":"Low", "Text":"1500 Pain Gems", "Available":0}
            if (("Pain" in Gems and Gems["Pain"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[2]["Available"] = 1

            if Value != 0:
                if Value == 1:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Pain Gems", "Available":0}
                    if ("Pain" in Gems and Gems["Pain"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
                elif Value == 2:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Pain Gems", "Available":0}
                    if ("Pain" in Gems and Gems["Pain"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
        elif TraitID == "ArousalEase0":
            #1: Easy
                # Gain: 1500 Desire Gems
                # Lose: 1500 Pain Gems
            #2: Hard
                # Gain: 1500 Pain Gems
                # Lose: 1500 Desire Gems
            Dict[0] = {"Level":0, "Title":"---", "Text":"", "Available":0}

            Dict[1] = {"Level":1, "Title":"Easy", "Text":"1500 Desire Gems", "Available":0}
            if (("Desire" in Gems and Gems["Desire"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[1]["Available"] = 1

            Dict[2] = {"Level":2, "Title":"Hard", "Text":"1500 Pain Gems", "Available":0}
            if (("Pain" in Gems and Gems["Pain"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[2]["Available"] = 1

            if Value != 0:
                if Value == 1:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Pain Gems", "Available":0}
                    if ("Pain" in Gems and Gems["Pain"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
                elif Value == 2:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Desire Gems", "Available":0}
                    if ("Desire" in Gems and Gems["Desire"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
        elif TraitID == "ResponseToPleasure0":
            #1: Enjoys
                # Gain: 1500 Desire Gems
                # Lose: 1500 Shame Gems
            #2: Denies
                # Gain: 1500 Shame Gems
                # Lose: 1500 Desire Gems
            Dict[0] = {"Level":0, "Title":"---", "Text":"", "Available":0}

            Dict[1] = {"Level":1, "Title":"Enjoys", "Text":"1500 Desire Gems", "Available":0}
            if (("Desire" in Gems and Gems["Desire"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[1]["Available"] = 1

            Dict[2] = {"Level":2, "Title":"Denies", "Text":"1500 Shame Gems", "Available":0}
            if (("Shame" in Gems and Gems["Shame"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[2]["Available"] = 1

            if Value != 0:
                if Value == 1:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Shame Gems", "Available":0}
                    if ("Shame" in Gems and Gems["Shame"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
                elif Value == 2:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Desire Gems", "Available":0}
                    if ("Desire" in Gems and Gems["Desire"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
        elif TraitID == "Perversion0":
            #1: Perverted
                # Gain: 1500 Desire Gems
                # Lose: 1500 Loyalty Gems
            #2: Pure
                # Gain: 1500 Loyalty Gems
                # Lose: 1500 Desire Gems
            Dict[0] = {"Level":0, "Title":"---", "Text":"", "Available":0}

            Dict[1] = {"Level":1, "Title":"Perverted", "Text":"1500 Desire Gems", "Available":0}
            if (("Desire" in Gems and Gems["Desire"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[1]["Available"] = 1

            Dict[2] = {"Level":2, "Title":"Pure", "Text":"1500 Loyalty Gems", "Available":0}
            if (("Loyalty" in Gems and Gems["Loyalty"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[2]["Available"] = 1

            if Value != 0:
                if Value == 1:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Loyalty Gems", "Available":0}
                    if ("Loyalty" in Gems and Gems["Loyalty"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
                elif Value == 2:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Desire Gems", "Available":0}
                    if ("Desire" in Gems and Gems["Desire"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
        elif TraitID == "Dominance0":
            # 1: Submissive
                # Gain: 2500 Submission Gems
                # Lose: 1500 Superiority Gems
            # 2: Dominant
                # Gain 2500 Superiority Gems
                # Lose 1500 Submission gems
            Dict[0] = {"Level":0, "Title":"---", "Text":"", "Available":0}

            Dict[1] = {"Level":1, "Title":"Submissive", "Text":"2500 Submission Gems", "Available":0}
            if (("Submission" in Gems and Gems["Submission"]["Amount"] >= 2500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[1]["Available"] = 1

            Dict[2] = {"Level":2, "Title":"Dominant", "Text":"2500 Superiority Gems", "Available":0}
            if (("Superiority" in Gems and Gems["Superiority"]["Amount"] >= 2500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[2]["Available"] = 1

            if Value != 0:
                if Value == 1:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Superiority Gems", "Available":0}
                    if ("Superiority" in Gems and Gems["Superiority"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
                elif Value == 2:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Submission gems", "Available":0}
                    if ("Submission" in Gems and Gems["Submission"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
        elif TraitID == "Forceful0":
            # 1: Forceful
            #     Gain: 2500 Superiority Gems
            #     Lose: 1500 Pain Gems
            # 2: Exploitable
            #     Gain 2500 Pain Gems
            #     Lose 1500 Superiority gems
            Dict[0] = {"Level":0, "Title":"---", "Text":"", "Available":0}

            Dict[1] = {"Level":1, "Title":"Forceful", "Text":"2500 Superiority Gems", "Available":0}
            if (("Superiority" in Gems and Gems["Superiority"]["Amount"] >= 2500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[1]["Available"] = 1

            Dict[2] = {"Level":2, "Title":"Exploitable", "Text":"2500 Pain Gems", "Available":0}
            if (("Pain" in Gems and Gems["Pain"]["Amount"] >= 2500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[2]["Available"] = 1

            if Value != 0:
                if Value == 1:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Pain Gems", "Available":0}
                    if ("Pain" in Gems and Gems["Pain"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
                elif Value == 2:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Superiority gems", "Available":0}
                    if ("Superiority" in Gems and Gems["Superiority"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
        elif TraitID == "Loyalty0":
            # 1: Loyal
            #     Gain: 2500 Loyalty Gems
            #     Lose: 2500 Desire Gems
            # 2: Disloyal
            #     Gain 1500 Desire Gems
            #     Lose 1500 Loyalty gems
            Dict[0] = {"Level":0, "Title":"---", "Text":"", "Available":0}

            Dict[1] = {"Level":1, "Title":"Loyal", "Text":"2500 Loyalty Gems", "Available":0}
            if (("Loyalty" in Gems and Gems["Loyalty"]["Amount"] >= 2500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[1]["Available"] = 1

            Dict[2] = {"Level":2, "Title":"Disloyal", "Text":"1500 Desire Gems", "Available":0}
            if (("Desire" in Gems and Gems["Desire"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[2]["Available"] = 1

            if Value != 0:
                if Value == 1:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"2500 Desire Gems", "Available":0}
                    if ("Desire" in Gems and Gems["Desire"]["Amount"] >= 2500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
                elif Value == 2:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Loyalty gems", "Available":0}
                    if ("Loyalty" in Gems and Gems["Loyalty"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
        elif TraitID == "Violence0":
            # 1: Violent
            #     Gain: 2500 Superiority Gems
            #     Lose: 1500 Pain Gems
            # 2: Meek
            #     Gain 2500 Pain Gems
            #     Lose 1500 Superiority gems
            Dict[0] = {"Level":0, "Title":"---", "Text":"", "Available":0}

            Dict[1] = {"Level":1, "Title":"Violent", "Text":"2500 Superiority Gems", "Available":0}
            if (("Superiority" in Gems and Gems["Superiority"]["Amount"] >= 2500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[1]["Available"] = 1

            Dict[2] = {"Level":2, "Title":"Meek", "Text":"2500 Pain Gems", "Available":0}
            if (("Pain" in Gems and Gems["Pain"]["Amount"] >= 2500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[2]["Available"] = 1

            if Value != 0:
                if Value == 1:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Pain Gems", "Available":0}
                    if ("Pain" in Gems and Gems["Pain"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
                elif Value == 2:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Superiority gems", "Available":0}
                    if ("Superiority" in Gems and Gems["Superiority"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
        # elif TraitID == "Beauty0":
        #     ""
        #     # TraitWidget.TraitBox.addItem("---")
        #     # TraitWidget.TraitBox.addItem("Gorgeous")
        #     # TraitWidget.TraitBox.addItem("Beautiful")
        #     # TraitWidget.TraitBox.addItem("Ugly")
        #     # TraitWidget.TraitBox.addItem("Disfigured")
        elif TraitID == "Shame0":
            # 1: Shameful
            #     Gain: 2500 Shame Gems
            #     Lose: 1500 Desire Gems
            # 2: Shameless
            #     Gain 2500 Desire Gems
            #     Lose 1500 Shame gems
            Dict[0] = {"Level":0, "Title":"---", "Text":"", "Available":0}

            Dict[1] = {"Level":1, "Title":"Shameful", "Text":"2500 Shame Gems", "Available":0}
            if (("Shame" in Gems and Gems["Shame"]["Amount"] >= 2500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[1]["Available"] = 1

            Dict[2] = {"Level":2, "Title":"Shameless", "Text":"2500 Desire Gems", "Available":0}
            if (("Desire" in Gems and Gems["Desire"]["Amount"] >= 2500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[2]["Available"] = 1

            if Value != 0:
                if Value == 1:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Desire Gems", "Available":0}
                    if ("Desire" in Gems and Gems["Desire"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
                elif Value == 2:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Shame gems", "Available":0}
                    if ("Shame" in Gems and Gems["Shame"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
        elif TraitID == "Will0":
            # 1: Strong Willed
            #     Gain: 1500 Loyalty Gems
            #     Lose: 2500 Desire Gems
            # 2: Weak Willed
            #     Gain 2500 Desire Gems
            #     Lose 1500 Loyalty gems
            Dict[0] = {"Level":0, "Title":"---", "Text":"", "Available":0}

            Dict[1] = {"Level":1, "Title":"Strong Willed", "Text":"1500 Loyalty Gems", "Available":0}
            if (("Loyalty" in Gems and Gems["Loyalty"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[1]["Available"] = 1

            Dict[2] = {"Level":2, "Title":"Weak Willed", "Text":"2500 Desire Gems", "Available":0}
            if (("Desire" in Gems and Gems["Desire"]["Amount"] >= 2500) or Flags["ForceAvailable"] == 1) and Value == 0: Dict[2]["Available"] = 1

            if Value != 0:
                if Value == 1:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"2500 Desire Gems", "Available":0}
                    if ("Desire" in Gems and Gems["Desire"]["Amount"] >= 2500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
                elif Value == 2:
                    Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Loyalty gems", "Available":0}
                    if ("Loyalty" in Gems and Gems["Loyalty"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
        # elif TraitID == "Influence0":
        #     ""
        #     # TraitWidget.TraitBox.addItem("---")
        #     # TraitWidget.TraitBox.addItem("Corruptor")
        #     # TraitWidget.TraitBox.addItem("Purificator")
        # elif TraitID == "Fertility0":
        #     ""
        #     # TraitWidget.TraitBox.addItem("---")
        #     # TraitWidget.TraitBox.addItem("Hyper Fertile")
        #     # TraitWidget.TraitBox.addItem("Infertile")
        # elif TraitID == "LewdBody0":
        #         ""
        #     	# V
        #     	# A
        #     	# B
        #     	# P
        #     	# M
    except Exception as e:
        Log(3, "ERROR RETRIEVING TRAIT CONDITIONS", e, TraitID)

    return Dict


def GetTraitDynamicWidget(TraitID, Data, NPCID, OtherID, Flags):
    try:
        if TraitID != "LewdBody0" and TraitID != "Dere0":
            Value = Data["Level"]

            Conditions = GetTraitConditions(TraitID, NPCID, OtherID, Flags)
            if len(list(Conditions.keys())) > 0:
                WidgetsList = []
                Widget = QWidget(objectName = "Transparent")

                TitleLabel = QLabel(f"{TraitID[:-1]}", Widget, objectName = "SubTitle")
                TitleLabel.setProperty("Color","Light")
                TitleLabel.setGeometry(0,0,250,40)
                TitleLabel.setMinimumHeight(40)
                TitleLabel.setMaximumHeight(40)
                TitleLabel.setAlignment(QtCore.Qt.AlignCenter)

                Holder = QWidget(Widget)
                Holder.setGeometry(0,45,250,0)

                Layout = QVBoxLayout()
                Layout.setSpacing(0)
                Layout.setContentsMargins(0, 0, 0, 0)
                Widget.setContentsMargins(0, 0, 0, 0)
                Holder.setLayout(Layout)

                Height = 0

                Conditions = GetTraitConditions(TraitID, NPCID, OtherID, Flags)
                if 0 in Conditions:
                    Widget0 = QWidget()

                    BackLabel0 = QLabel(Widget0)
                    BackLabel0.setProperty("Color","Dark")
                    Label0 = QLabel(Widget0, objectName = "SmallText")
                    Label0.setProperty("Color","Dark")
                    Label0.setProperty("Border","None")
                    Label0.setGeometry(0,0,215,35)
                    Label0.setWordWrap(True)

                    Available = Conditions[0]["Available"]
                    if Available == 1:
                        def Click0():
                            if Button0.Available == 1:
                                TraitChange(TraitID, NPCID, Data, 0)
                        # Button0 = QPushButton(Widget0, clicked = lambda: Click0())
                        # Button0.setStyleSheet("border-image: url(Resources/SoLResources/Cycle.png); ")
                        # Button0.setGeometry(215,1,33,33)
                        # Button0.setProperty("Color","Dark")
                        # Button0.Available = Available

                        Button0 = QLabel(Widget0)
                        Button0.setGeometry(215,1,33,33)
                        Button0.mouseReleaseEvent = lambda event: Click0()
                        Button0.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "Cycle.png" ) ))
                        # Button0.setStyleSheet("border:none; background:none;")
                        Button0.setProperty("Color","None")
                        Button0.setScaledContents(True)
                        Button0.Available = Available


                        if Value != 0:
                            Label0.setProperty("Selected",1)

                    if Value != 0:
                        Label0.setText(f'''{Conditions[0]["Title"]}: {Conditions[0]["Text"]}''')
                    else:
                        Label0.setText(f'''{Conditions[0]["Title"]}: Current Level''')

                    LabelHeight = Globals.References["SoLFunctions"].AdjustSize(Label0)
                    Label0.setGeometry(1,1,214,LabelHeight)
                    BackLabel0.setGeometry(0,0,250,LabelHeight+2)

                    Widget0.setMinimumHeight(BackLabel0.height())
                    Widget0.setMaximumHeight(BackLabel0.height())

                    Layout.addWidget(Widget0)
                    Height += Widget0.height()

                if 1 in Conditions:
                    Widget1 = QWidget()

                    BackLabel1 = QLabel(Widget1)
                    BackLabel1.setProperty("Color","Dark")
                    Label1 = QLabel(Widget1, objectName = "SmallText")
                    Label1.setProperty("Color","Dark")
                    Label1.setProperty("Border","None")
                    Label1.setGeometry(0,0,215,35)
                    Label1.setWordWrap(True)

                    Available = Conditions[1]["Available"]
                    if Available == 1:
                        def Click1():
                            if Button1.Available == 1:
                                TraitChange(TraitID, NPCID, Data, 1)
                        # Button1 = QPushButton(Widget1, clicked = lambda: Click1())
                        # Button1.setStyleSheet("border-image: url(Resources/SoLResources/Cycle.png); ")
                        # Button1.setGeometry(215,1,33,33)
                        # Button1.setProperty("Color","Dark")
                        # Button1.Available = Available

                        Button1 = QLabel(Widget1)
                        Button1.setGeometry(215,1,33,33)
                        Button1.mouseReleaseEvent = lambda event: Click2()
                        Button1.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "Cycle.png" ) ))
                        # Button1.setStyleSheet("border:none; background:none;")
                        Button1.setProperty("Color","None")
                        Button1.setScaledContents(True)
                        Button1.Available = Available


                        if Value != 1:
                            Label1.setProperty("Selected",1)
                    elif Value != 0 and Value != 1:
                        Label1.setProperty("Selected",-1)
                    if Value != 1:
                        Label1.setText(f'''{Conditions[1]["Title"]}: {Conditions[1]["Text"]}''')
                    else:
                        Label1.setText(f'''{Conditions[1]["Title"]}: Current Level''')

                    LabelHeight = Globals.References["SoLFunctions"].AdjustSize(Label1)
                    Label1.setGeometry(1,1,214,LabelHeight)
                    BackLabel1.setGeometry(0,0,250,LabelHeight+2)

                    Widget1.setMinimumHeight(BackLabel1.height())
                    Widget1.setMaximumHeight(BackLabel1.height())

                    Layout.addWidget(Widget1)
                    Height += Widget1.height()

                if 2 in Conditions:
                    Widget2 = QWidget()

                    BackLabel2 = QLabel(Widget2)
                    BackLabel2.setProperty("Color","Dark")
                    Label2 = QLabel(Widget2, objectName = "SmallText")
                    Label2.setProperty("Color","Dark")
                    Label2.setProperty("Border","None")
                    Label2.setGeometry(0,0,215,35)
                    Label2.setWordWrap(True)

                    Available = Conditions[2]["Available"]
                    if Available == 1:
                        def Click2():
                            if Button2.Available == 1:
                                TraitChange(TraitID, NPCID, Data, 2)
                        # Button2 = QPushButton(Widget2, clicked = lambda: Click2())
                        # Button2.setStyleSheet("border-image: url(Resources/SoLResources/Cycle.png); ")
                        # Button2.setGeometry(215,1,33,33)
                        # Button2.setProperty("Color","Dark")
                        # Button2.Available = Available

                        Button2 = QLabel(Widget2)
                        Button2.setGeometry(215,1,33,33)
                        Button2.mouseReleaseEvent = lambda event: Click2()
                        Button2.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "Cycle.png" ) ))
                        # Button2.setStyleSheet("border:none; background:none;")
                        Button2.setProperty("Color","None")
                        Button2.setScaledContents(True)
                        Button2.Available = Available



                        if Value != 2:
                            Label2.setProperty("Selected",1)
                    elif Value != 0 and Value != 2:
                        Label2.setProperty("Selected",-1)
                    if Value != 2:
                        Label2.setText(f'''{Conditions[2]["Title"]}: {Conditions[2]["Text"]}''')
                    else:
                        Label2.setText(f'''{Conditions[2]["Title"]}: Current Level''')

                    LabelHeight = Globals.References["SoLFunctions"].AdjustSize(Label2)
                    Label2.setGeometry(1,1,214,LabelHeight)
                    BackLabel2.setGeometry(0,0,250,LabelHeight+2)

                    Widget2.setMinimumHeight(BackLabel2.height())
                    Widget2.setMaximumHeight(BackLabel2.height())

                    Layout.addWidget(Widget2)
                    Height += Widget2.height()

                Holder.setMinimumHeight(Height)
                Holder.setMaximumHeight(Height)

                Widget.setMinimumHeight(Height+45)
                Widget.setMaximumHeight(Height+45)

                Widget.setMinimumWidth(250)
                Widget.setMaximumWidth(250)

                return Widget

        elif TraitID == "Dere0":
            Value = Data["Level"]

            WidgetsList = []
            Widget = QWidget(objectName = "Transparent")

            TitleLabel = QLabel("Dere", Widget, objectName = "SubTitle")
            TitleLabel.setProperty("Color","Light")
            TitleLabel.setGeometry(0,0,250,40)
            TitleLabel.setMinimumHeight(40)
            TitleLabel.setMaximumHeight(40)
            TitleLabel.setAlignment(QtCore.Qt.AlignCenter)

            Holder = QWidget(Widget)
            Holder.setGeometry(0,45,250,0)

            Layout = QVBoxLayout()
            Layout.setSpacing(0)
            Layout.setContentsMargins(0, 0, 0, 0)
            Widget.setContentsMargins(0, 0, 0, 0)
            Holder.setLayout(Layout)

            Height = 0

            Conditions = GetTraitConditions(TraitID, NPCID, OtherID, Flags)
            # NOT A DERE
            if 0 in Conditions:
                NaDWidget = QWidget()

                NaDBackLabel = QLabel(NaDWidget)
                NaDBackLabel.setProperty("Color","Dark")
                NaDLabel = QLabel(NaDWidget, objectName = "SmallText")
                NaDLabel.setProperty("Color","Dark")
                NaDLabel.setProperty("Border","None")
                NaDLabel.setGeometry(0,0,215,35)
                NaDLabel.setWordWrap(True)

                Available = Conditions[0]["Available"]
                if Available == 1:
                    def NaDClick():
                        if NaDButton.Available == 1:
                            TraitChange(TraitID, NPCID, Data, 0)
                    # NaDButton = QPushButton(NaDWidget, clicked = lambda: NaDClick())
                    # NaDButton.setStyleSheet("border-image: url(Resources/SoLResources/Cycle.png); ")
                    # NaDButton.setGeometry(215,1,33,33)
                    # NaDButton.setProperty("Color","Dark")
                    # NaDButton.Available = Available

                    NaDButton = QLabel(NaDWidget)
                    NaDButton.setGeometry(215,1,33,33)
                    NaDButton.mouseReleaseEvent = lambda event: NaDClick()
                    NaDButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "Cycle.png" ) ))
                    # NaDButton.setStyleSheet("border:none; background:none;")
                    NaDButton.setProperty("Color","None")
                    NaDButton.setScaledContents(True)
                    NaDButton.Available = Available


                    if Value != 0:
                        NaDLabel.setProperty("Selected",1)

                if Value != 0:
                    NaDLabel.setText(f'''{Conditions[0]["Title"]}: {Conditions[0]["Text"]}''')
                else:
                    NaDLabel.setText(f'''{Conditions[0]["Title"]}: Current Level''')

                LabelHeight = Globals.References["SoLFunctions"].AdjustSize(NaDLabel)
                NaDLabel.setGeometry(1,1,214,LabelHeight)
                NaDBackLabel.setGeometry(0,0,250,LabelHeight+2)

                NaDWidget.setMinimumHeight(NaDBackLabel.height())
                NaDWidget.setMaximumHeight(NaDBackLabel.height())

                Layout.addWidget(NaDWidget)
                Height += NaDWidget.height()
            # TSUNDERE
            if 1 in Conditions:
                TsunWidget = QWidget()

                TsunBackLabel = QLabel(TsunWidget)
                TsunBackLabel.setProperty("Color","Dark")
                TsunLabel = QLabel(TsunWidget, objectName = "SmallText")
                TsunLabel.setProperty("Color","Dark")
                TsunLabel.setProperty("Border","None")
                TsunLabel.setGeometry(0,0,215,35)
                TsunLabel.setWordWrap(True)

                Available = Conditions[1]["Available"]
                if Available == 1:
                    def TsunClick():
                        if TsunButton.Available == 1:
                            TraitChange(TraitID, NPCID, Data, 1)
                    # TsunButton = QPushButton(TsunWidget, clicked = lambda: TsunClick())
                    # TsunButton.setStyleSheet("border-image: url(Resources/SoLResources/Cycle.png); ")
                    # TsunButton.setGeometry(215,1,33,33)
                    # TsunButton.setProperty("Color","Dark")
                    # TsunButton.Available = Available

                    TsunButton = QLabel(TsunWidget)
                    TsunButton.setGeometry(215,1,33,33)
                    TsunButton.mouseReleaseEvent = lambda event: TsunClick()
                    TsunButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "Cycle.png" ) ))
                    # TsunButton.setStyleSheet("border:none; background:none;")
                    TsunButton.setProperty("Color","None")
                    TsunButton.setScaledContents(True)
                    TsunButton.Available = Available


                    if Value != 1:
                        TsunLabel.setProperty("Selected",1)
                elif Value != 0 and Value != 1:
                    TsunLabel.setProperty("Selected",-1)
                if Value != 1:
                    TsunLabel.setText(f'''{Conditions[1]["Title"]}: {Conditions[1]["Text"]}''')
                else:
                    TsunLabel.setText(f'''{Conditions[1]["Title"]}: Current Level''')

                LabelHeight = Globals.References["SoLFunctions"].AdjustSize(TsunLabel)
                TsunLabel.setGeometry(1,1,214,LabelHeight)
                TsunBackLabel.setGeometry(0,0,250,LabelHeight+2)

                TsunWidget.setMinimumHeight(TsunBackLabel.height())
                TsunWidget.setMaximumHeight(TsunBackLabel.height())

                Layout.addWidget(TsunWidget)
                Height += TsunWidget.height()
            # DANDERE
            if 2 in Conditions:
                DanWidget = QWidget()

                DanBackLabel = QLabel(DanWidget)
                DanBackLabel.setProperty("Color","Dark")
                DanLabel = QLabel(DanWidget, objectName = "SmallText")
                DanLabel.setProperty("Color","Dark")
                DanLabel.setProperty("Border","None")
                DanLabel.setGeometry(0,0,215,35)
                DanLabel.setWordWrap(True)

                Available = Conditions[2]["Available"]
                if Available == 1:
                    def DanClick():
                        if DanButton.Available == 1:
                            TraitChange(TraitID, NPCID, Data, 2)
                    # DanButton = QPushButton(DanWidget, clicked = lambda: DanClick())
                    # DanButton.setStyleSheet("border-image: url(Resources/SoLResources/Cycle.png); ")
                    # DanButton.setGeometry(215,1,33,33)
                    # DanButton.setProperty("Color","Dark")
                    # DanButton.Available = Available

                    DanButton = QLabel(DanWidget)
                    DanButton.setGeometry(215,1,33,33)
                    DanButton.mouseReleaseEvent = lambda event: DanClick()
                    DanButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "Cycle.png" ) ))
                    # DanButton.setStyleSheet("border:none; background:none;")
                    DanButton.setProperty("Color","None")
                    DanButton.setScaledContents(True)
                    DanButton.Available = Available


                    if Value != 2:
                        DanLabel.setProperty("Selected",1)
                elif Value != 0 and Value != 2:
                    DanLabel.setProperty("Selected",-1)
                if Value != 2:
                    DanLabel.setText(f'''{Conditions[2]["Title"]}: {Conditions[2]["Text"]}''')
                else:
                    DanLabel.setText(f'''{Conditions[2]["Title"]}: Current Level''')

                LabelHeight = Globals.References["SoLFunctions"].AdjustSize(DanLabel)
                DanLabel.setGeometry(1,1,214,LabelHeight)
                DanBackLabel.setGeometry(0,0,250,LabelHeight+2)

                DanWidget.setMinimumHeight(DanBackLabel.height())
                DanWidget.setMaximumHeight(DanBackLabel.height())

                Layout.addWidget(DanWidget)
                Height += DanWidget.height()
            # KUUDERE
            if 3 in Conditions:
                KuuWidget = QWidget()

                KuuBackLabel = QLabel(KuuWidget)
                KuuBackLabel.setProperty("Color","Dark")
                KuuLabel = QLabel(KuuWidget, objectName = "SmallText")
                KuuLabel.setProperty("Color","Dark")
                KuuLabel.setProperty("Border","None")
                KuuLabel.setGeometry(0,0,215,35)
                KuuLabel.setWordWrap(True)

                Available = Conditions[3]["Available"]
                if Available == 1:
                    def KuuClick():
                        if KuuButton.Available == 1:
                            TraitChange(TraitID, NPCID, Data, 3)
                    # KuuButton = QPushButton(KuuWidget, clicked = lambda: KuuClick())
                    # KuuButton.setStyleSheet("border-image: url(Resources/SoLResources/Cycle.png); ")
                    # KuuButton.setGeometry(215,1,33,33)
                    # KuuButton.setProperty("Color","Dark")
                    # KuuButton.Available = Available

                    KuuButton = QLabel(KuuWidget)
                    KuuButton.setGeometry(215,1,33,33)
                    KuuButton.mouseReleaseEvent = lambda event: KuuClick()
                    KuuButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "Cycle.png" ) ))
                    # KuuButton.setStyleSheet("border:none; background:none;")
                    KuuButton.setProperty("Color","None")
                    KuuButton.setScaledContents(True)
                    KuuButton.Available = Available

                    if Value != 3:
                        KuuLabel.setProperty("Selected",1)
                elif Value != 0 and Value != 3:
                    KuuLabel.setProperty("Selected",-1)
                if Value != 3:
                    KuuLabel.setText(f'''{Conditions[3]["Title"]}: {Conditions[3]["Text"]}''')
                else:
                    KuuLabel.setText(f'''{Conditions[3]["Title"]}: Current Level''')

                LabelHeight = Globals.References["SoLFunctions"].AdjustSize(KuuLabel)
                KuuLabel.setGeometry(1,1,214,LabelHeight)
                KuuBackLabel.setGeometry(0,0,250,LabelHeight+2)

                KuuWidget.setMinimumHeight(KuuBackLabel.height())
                KuuWidget.setMaximumHeight(KuuBackLabel.height())

                Layout.addWidget(KuuWidget)
                Height += KuuWidget.height()
            # YANDERE
            if 4 in Conditions:
                YanWidget = QWidget()

                YanBackLabel = QLabel(YanWidget)
                YanBackLabel.setProperty("Color","Dark")
                YanLabel = QLabel(YanWidget, objectName = "SmallText")
                YanLabel.setProperty("Color","Dark")
                YanLabel.setProperty("Border","None")
                YanLabel.setGeometry(0,0,215,35)
                YanLabel.setWordWrap(True)

                Available = Conditions[4]["Available"]
                if Available == 1:
                    def YanClick():
                        if YanButton.Available == 1:
                            TraitChange(TraitID, NPCID, Data, 4)
                    # YanButton = QPushButton(YanWidget, clicked = lambda: YanClick())
                    # YanButton.setStyleSheet("border-image: url(Resources/SoLResources/Cycle.png); ")
                    # YanButton.setGeometry(215,1,33,33)
                    # YanButton.setProperty("Color","Dark")
                    # YanButton.Available = Available

                    YanButton = QLabel(YanWidget)
                    YanButton.setGeometry(215,1,33,33)
                    YanButton.mouseReleaseEvent = lambda event: YanClick()
                    YanButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "Cycle.png" ) ))
                    # YanButton.setStyleSheet("border:none; background:none;")
                    YanButton.setProperty("Color","None")
                    YanButton.setScaledContents(True)
                    YanButton.Available = Available

                    if Value != 4:
                        YanLabel.setProperty("Selected",1)
                elif Value != 0 and Value != 4:
                    YanLabel.setProperty("Selected",-1)
                if Value != 4:
                    YanLabel.setText(f'''{Conditions[4]["Title"]}: {Conditions[4]["Text"]}''')
                else:
                    YanLabel.setText(f'''{Conditions[4]["Title"]}: Current Level''')

                LabelHeight = Globals.References["SoLFunctions"].AdjustSize(YanLabel)
                YanLabel.setGeometry(1,1,214,LabelHeight)
                YanBackLabel.setGeometry(0,0,250,LabelHeight+2)

                YanWidget.setMinimumHeight(YanBackLabel.height())
                YanWidget.setMaximumHeight(YanBackLabel.height())

                Layout.addWidget(YanWidget)
                Height += YanWidget.height()
            # DEREDERE
            if 5 in Conditions:
                DereWidget = QWidget()

                DereBackLabel = QLabel(DereWidget)
                DereBackLabel.setProperty("Color","Dark")
                DereLabel = QLabel(DereWidget, objectName = "SmallText")
                DereLabel.setProperty("Color","Dark")
                DereLabel.setProperty("Border","None")
                DereLabel.setGeometry(0,0,215,35)
                DereLabel.setWordWrap(True)

                Available = Conditions[5]["Available"]
                if Available == 1:
                    def DereClick():
                        if DereButton.Available == 1:
                            TraitChange(TraitID, NPCID, Data, 5)
                    # DereButton = QPushButton(DereWidget, clicked = lambda: DereClick())
                    # DereButton.setStyleSheet("border-image: url(Resources/SoLResources/Cycle.png); ")
                    # DereButton.setGeometry(215,1,33,33)
                    # DereButton.setProperty("Color","Dark")
                    # DereButton.Available = Available

                    DereButton = QLabel(DereWidget)
                    DereButton.setGeometry(215,1,33,33)
                    DereButton.mouseReleaseEvent = lambda event: DereClick()
                    DereButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "Cycle.png" ) ))
                    # DereButton.setStyleSheet("border:none; background:none;")
                    DereButton.setProperty("Color","None")
                    DereButton.setScaledContents(True)
                    DereButton.Available = Available

                    if Value != 5:
                        DereLabel.setProperty("Selected",1)
                elif Value != 0 and Value != 5:
                    DereLabel.setProperty("Selected",-1)
                if Value != 5:
                    DereLabel.setText(f'''{Conditions[5]["Title"]}: {Conditions[5]["Text"]}''')
                else:
                    DereLabel.setText(f'''{Conditions[5]["Title"]}: Current Level''')

                LabelHeight = Globals.References["SoLFunctions"].AdjustSize(DereLabel)
                DereLabel.setGeometry(1,1,214,LabelHeight)
                DereBackLabel.setGeometry(0,0,250,LabelHeight+2)

                DereWidget.setMinimumHeight(DereBackLabel.height())
                DereWidget.setMaximumHeight(DereBackLabel.height())

                Layout.addWidget(DereWidget)
                Height += DereWidget.height()

            Holder.setMinimumHeight(Height)
            Holder.setMaximumHeight(Height)

            Widget.setMinimumHeight(Height+45)
            Widget.setMaximumHeight(Height+45)

            Widget.setMinimumWidth(250)
            Widget.setMaximumWidth(250)

            return Widget

        return None
    except Exception as e:
        Log(3, "ERROR GetTraitDynamicWidget", e, TraitID, Data, NPCID, OtherID, Flags)


def CommandProcessTrait(self, OriginalData, FinalData, TraitID):
    Target = FinalData["Target"]
    Actor = FinalData["Actor"]
    Relation = 0
    try:
        if TraitID != "LewdBody0":
            Level = Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"]

        if TraitID == "Courage0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                # Level = Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"]
                if Level == 1:  # Brave
                    if "Submission" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Submission"] = int(FinalData["TargetDict"]["Temporal"]["Submission"] * 0.8)
                    if "Pain" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Pain"] = int(FinalData["TargetDict"]["Temporal"]["Pain"] * 0.9)
                    if "Shame" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Shame"] = int(FinalData["TargetDict"]["Temporal"]["Shame"] * 0.86)
                elif Level == 2: #Timid
                    ""
                    if "Submission" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Submission"] = int(FinalData["TargetDict"]["Temporal"]["Submission"] * 1.2)
                    if "Pain" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Pain"] = int(FinalData["TargetDict"]["Temporal"]["Pain"] * 1.1)
                    if "Shame" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Shame"] = int(FinalData["TargetDict"]["Temporal"]["Shame"] * 1.15)
        elif TraitID == "Attitude0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # Defiant
                    if "Submission" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Submission"] = int(FinalData["TargetDict"]["Temporal"]["Submission"] * 0.8)
                    if "Service" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Service"] = int(FinalData["TargetDict"]["Temporal"]["Service"] * 0.6)
                    if "Shame" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Shame"] = int(FinalData["TargetDict"]["Temporal"]["Shame"] * 1.2)
                    if "Discomfort" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Discomfort"] = int(FinalData["TargetDict"]["Temporal"]["Discomfort"] * 1.1)
                    if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Temporal"]["Submission"] = int(FinalData["TargetDict"]["Resistance"] * 1.1)
                elif Level == 2: # Docile
                    if "Submission" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Submission"] = int(FinalData["TargetDict"]["Temporal"]["Submission"] * 1.2)
                    if "Service" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Service"] = int(FinalData["TargetDict"]["Temporal"]["Service"] * 1.3)
                    if "Shame" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Shame"] = int(FinalData["TargetDict"]["Temporal"]["Shame"] * 0.85)
                    if "Discomfort" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Discomfort"] = int(FinalData["TargetDict"]["Temporal"]["Discomfort"] * 0.9)
                    if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 0.9)
        elif TraitID == "Pride0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # Prideful
                    if "Obedience" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Obedience"] = int(FinalData["TargetDict"]["Temporal"]["Obedience"] * 0.9)
                    if "Superiority" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Superiority"] = int(FinalData["TargetDict"]["Temporal"]["Superiority"] * 1.2)
                    if "Service" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Service"] = int(FinalData["TargetDict"]["Temporal"]["Service"] * 0.9)
                    if "Shame" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Shame"] = int(FinalData["TargetDict"]["Temporal"]["Shame"] * 1.1)
                    if "Discomfort" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Discomfort"] = int(FinalData["TargetDict"]["Temporal"]["Discomfort"] * 1.2)
                    if "Hate" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Hate"] = int(FinalData["TargetDict"]["Temporal"]["Hate"] * 1.2)
                elif Level == 2: # Humble
                    if "Obedience" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Obedience"] = int(FinalData["TargetDict"]["Temporal"]["Obedience"] * 1.1)
                    if "Submission" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Submission"] = int(FinalData["TargetDict"]["Temporal"]["Submission"] * 1.2)
                    if "Service" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Service"] = int(FinalData["TargetDict"]["Temporal"]["Service"] * 1.1)
                    if "Shame" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Shame"] = int(FinalData["TargetDict"]["Temporal"]["Shame"] * 0.9)
                    if "Discomfort" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Discomfort"] = int(FinalData["TargetDict"]["Temporal"]["Discomfort"] * 0.9)
                    if "Hate" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Hate"] = int(FinalData["TargetDict"]["Temporal"]["Hate"] * 0.9)
        elif TraitID == "Dere0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # Tsundere
                    ""
                    # 0 Aquitance
                    # 1 Familia
                    # 2 Affection
                    # 3 Love
                    # if Relation 1-2:
                    if True:
                        if "Favor" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Favor"] = int(FinalData["TargetDict"]["Temporal"]["Favor"] * 0.9)
                        if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 0.9)
                        if "Obedience" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Obedience"] = int(FinalData["TargetDict"]["Temporal"]["Obedience"] * 0.9)
                        if "Submission" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Submission"] = int(FinalData["TargetDict"]["Temporal"]["Submission"] * 0.9)
                        if "Shame" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Shame"] = int(FinalData["TargetDict"]["Temporal"]["Shame"] * 1.1)
                        if "Discomfort" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Discomfort"] = int(FinalData["TargetDict"]["Temporal"]["Discomfort"] * 1.1)
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 1.1)
                    # if Relation >= 3:
                    elif False:
                        if "Favor" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Favor"] = int(FinalData["TargetDict"]["Temporal"]["Favor"] * 1.2)
                        if "Loyalty" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Loyalty"] = int(FinalData["TargetDict"]["Temporal"]["Loyalty"] * 1.1)
                        if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 1.1)
                        if "Obedience" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Obedience"] = int(FinalData["TargetDict"]["Temporal"]["Obedience"] * 1.1)
                        if "Service" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Service"] = int(FinalData["TargetDict"]["Temporal"]["Service"] * 1.1)
                        if "Discomfort" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Discomfort"] = int(FinalData["TargetDict"]["Temporal"]["Discomfort"] * 0.8)
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 0.8)
                elif Level == 2: # Dandere
                    if "Submission" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Submission"] = int(FinalData["TargetDict"]["Temporal"]["Submission"] * 1.2)
                    if "Obedience" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Obedience"] = int(FinalData["TargetDict"]["Temporal"]["Obedience"] * 1.1)
                    if "Shame" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Shame"] = int(FinalData["TargetDict"]["Temporal"]["Shame"] * 1.1)
                    if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 0.9)
                    # if Relation >= 2:
                    if False:
                        if "Favor" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Favor"] = int(FinalData["TargetDict"]["Temporal"]["Favor"] * 1.2)
                elif Level == 3: # Kuudere
                    if "Favor" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Favor"] = int(FinalData["TargetDict"]["Temporal"]["Favor"] * 0.9)
                    if "Loyalty" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Loyalty"] = int(FinalData["TargetDict"]["Temporal"]["Loyalty"] * 0.9)
                    if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 0.9)
                    if "Shame" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Shame"] = int(FinalData["TargetDict"]["Temporal"]["Shame"] * 0.8)
                    if "Discomfort" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Discomfort"] = int(FinalData["TargetDict"]["Temporal"]["Discomfort"] * 0.8)
                    if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 0.9)
                    ""
                elif Level == 4: # Yandere
                    # if Relation >= 2:
                    if False:
                        if "Favor" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Favor"] = int(FinalData["TargetDict"]["Temporal"]["Favor"] * 1.1)
                        if "Loyalty" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Loyalty"] = int(FinalData["TargetDict"]["Temporal"]["Loyalty"] * 1.1)
                        if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 1.1)
                        if "Service" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Service"] = int(FinalData["TargetDict"]["Temporal"]["Service"] * 1.1)
                        if "Discomfort" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Discomfort"] = int(FinalData["TargetDict"]["Temporal"]["Discomfort"] * 0.9)
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 0.7)
                elif Level == 5: # Deredere
                    if "Favor" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Favor"] = int(FinalData["TargetDict"]["Temporal"]["Favor"] * 1.2)
                    if "Loyalty" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Loyalty"] = int(FinalData["TargetDict"]["Temporal"]["Loyalty"] * 1.1)
                    if "Obedience" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Obedience"] = int(FinalData["TargetDict"]["Temporal"]["Obedience"] * 1.1)
                    if "Service" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Service"] = int(FinalData["TargetDict"]["Temporal"]["Service"] * 1.1)
                    if "Fear" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Fear"] = int(FinalData["TargetDict"]["Temporal"]["Fear"] * 0.9)
                    if "Discomfort" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Discomfort"] = int(FinalData["TargetDict"]["Temporal"]["Discomfort"] * 0.9)
                    if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 0.9)
                    ""
        elif TraitID == "SelfControl0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # High
                    if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 0.8)
                    if "Arousal" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Arousal"] = int(FinalData["TargetDict"]["State"]["Arousal"] * 0.8)
                elif Level == 2: # Low
                    if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 1.2)
                    if "Arousal" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Arousal"] = int(FinalData["TargetDict"]["State"]["Arousal"] * 1.2)
        elif TraitID == "Cheerfulness0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # Cheerful
                    if "Mood" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Mood"] = int(FinalData["TargetDict"]["State"]["Mood"] * 1.2)
                    if "Favor" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Favor"] = int(FinalData["TargetDict"]["Temporal"]["Favor"] * 1.2)
                elif Level == 2: # Gloomy
                    if "Mood" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Mood"] = int(FinalData["TargetDict"]["State"]["Mood"] * 0.8)
                    if "Favor" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Favor"] = int(FinalData["TargetDict"]["Temporal"]["Favor"] * 0.8)
        elif TraitID == "Shyness0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # Shy
                    if "Submission" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Submission"] = int(FinalData["TargetDict"]["Temporal"]["Submission"] * 1.2)
                    if "Service" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Service"] = int(FinalData["TargetDict"]["Temporal"]["Service"] * 1.2)
                    if "Shame" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Shame"] = int(FinalData["TargetDict"]["Temporal"]["Shame"] * 1.2)
                    if "Fear" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Fear"] = int(FinalData["TargetDict"]["Temporal"]["Fear"] * 1.2)
                elif Level == 2: # Outgoing
                    if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 1.2)
                    if "Shame" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Shame"] = int(FinalData["TargetDict"]["Temporal"]["Shame"] * 0.8)
                    if "Discomfort" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Discomfort"] = int(FinalData["TargetDict"]["Temporal"]["Discomfort"] * 0.8)
                    if "Fear" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Fear"] = int(FinalData["TargetDict"]["Temporal"]["Fear"] * 0.8)
        elif TraitID == "Gullible0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # Gullible
                    # ""
                    if "Favor" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Favor"] = int(FinalData["TargetDict"]["Temporal"]["Favor"] * 1.2)
                    if "Obedience" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Obedience"] = int(FinalData["TargetDict"]["Temporal"]["Obedience"] * 1.2)
                    if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 0.8)
                elif Level == 2: # Untrusting
                    # ""
                    if "Favor" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Favor"] = int(FinalData["TargetDict"]["Temporal"]["Favor"] * 0.9)
                    if "Obedience" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Obedience"] = int(FinalData["TargetDict"]["Temporal"]["Obedience"] * 0.9)
                    if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 1.1)
        elif TraitID == "Charm0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # Charming
                    # ""
                    # if actor has it
                    if "Mood" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Mood"] = int(FinalData["TargetDict"]["State"]["Mood"] * 1.2)
                    if "Favor" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Favor"] = int(FinalData["TargetDict"]["Temporal"]["Favor"] * 1.2)
                    if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 1.2)
                    if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 0.8)
                    if "Discomfort" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Discomfort"] = int(FinalData["TargetDict"]["Temporal"]["Discomfort"] * 0.8)
                elif Level == 2: # Charmless
                    # ""
                    # if actor has it
                    if "Mood" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Mood"] = int(FinalData["TargetDict"]["State"]["Mood"] * 0.8)
                    if "Favor" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Favor"] = int(FinalData["TargetDict"]["Temporal"]["Favor"] * 0.8)
                    if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 0.8)
                    if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 1.2)
                    if "Discomfort" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Discomfort"] = int(FinalData["TargetDict"]["Temporal"]["Discomfort"] * 1.2)
        elif TraitID == "SubstanceResistance0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # Resistant
                    ""
                    if "Intoxication" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Intoxication"] = int(FinalData["TargetDict"]["State"]["Intoxication"] * 0.6)
                elif Level == 2: # Weak
                    if "Intoxication" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Intoxication"] = int(FinalData["TargetDict"]["State"]["Intoxication"] * 1.4)
                    ""
        elif TraitID == "SexualInterest0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # Curious
                    # ""
                    if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 1.2)
                    if "Shame" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Shame"] = int(FinalData["TargetDict"]["Temporal"]["Shame"] * 0.9)
                elif Level == 2: # Conservative
                    if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 0.8)
                    if "Shame" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Shame"] = int(FinalData["TargetDict"]["Temporal"]["Shame"] * 1.2)
        elif TraitID == "Virtue0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # Virtuous
                    if "Loyalty" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Loyalty"] = int(FinalData["TargetDict"]["Temporal"]["Loyalty"] * 1.2)
                    if "Shame" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Shame"] = int(FinalData["TargetDict"]["Temporal"]["Shame"] * 1.2)
                    if "Discomfort" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Discomfort"] = int(FinalData["TargetDict"]["Temporal"]["Discomfort"] * 1.2)
                    if "Arousal" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Arousal"] = int(FinalData["TargetDict"]["State"]["Arousal"] * 0.9)
                    if "Excitement" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Excitement"] = int(FinalData["TargetDict"]["State"]["Excitement"] * 0.9)
                    if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 0.7)
                elif Level == 2: # Depraved
                    if "Loyalty" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Loyalty"] = int(FinalData["TargetDict"]["Temporal"]["Loyalty"] * 0.8)
                    if "Shame" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Shame"] = int(FinalData["TargetDict"]["Temporal"]["Shame"] * 0.9)
                    if "Discomfort" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Discomfort"] = int(FinalData["TargetDict"]["Temporal"]["Discomfort"] * 0.8)
                    if "Arousal" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Arousal"] = int(FinalData["TargetDict"]["State"]["Arousal"] * 1.2)
                    if "Excitement" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Excitement"] = int(FinalData["TargetDict"]["State"]["Excitement"] * 1.2)
                    if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 1.2)
        elif TraitID == "Chastity0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # Not for Lewding
                    if "Excitement" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Excitement"] = int(FinalData["TargetDict"]["State"]["Excitement"] * 0)
                    if "Arousal" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Arousal"] = int(FinalData["TargetDict"]["State"]["Arousal"] * 0)
                    if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 0)
                    if "MPlea" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["MPlea"] = int(FinalData["TargetDict"]["Temporal"]["MPlea"] * 0)
                    if "CPlea" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["CPlea"] = int(FinalData["TargetDict"]["Temporal"]["CPlea"] * 0)
                    if "APlea" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["APlea"] = int(FinalData["TargetDict"]["Temporal"]["APlea"] * 0)
                    if "VPlea" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["VPlea"] = int(FinalData["TargetDict"]["Temporal"]["VPlea"] * 0)
                    if "PPlea" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["PPlea"] = int(FinalData["TargetDict"]["Temporal"]["PPlea"] * 0)
                elif Level == 2: # Chaste
                    if Relation < 2:
                        if "Excitement" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Excitement"] = int(FinalData["TargetDict"]["State"]["Excitement"] * 0.6)
                        if "Arousal" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Arousal"] = int(FinalData["TargetDict"]["State"]["Arousal"] * 0.6)
                        if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 0.6)
                        if "MPlea" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["MPlea"] = int(FinalData["TargetDict"]["Temporal"]["MPlea"] * 0.6)
                        if "CPlea" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["CPlea"] = int(FinalData["TargetDict"]["Temporal"]["CPlea"] * 0.6)
                        if "APlea" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["APlea"] = int(FinalData["TargetDict"]["Temporal"]["APlea"] * 0.6)
                        if "VPlea" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["VPlea"] = int(FinalData["TargetDict"]["Temporal"]["VPlea"] * 0.6)
                        if "PPlea" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["PPlea"] = int(FinalData["TargetDict"]["Temporal"]["PPlea"] * 0.6)
                elif Level == 3: # Unchaste
                    if Relation > 1:
                        if "Excitement" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Excitement"] = int(FinalData["TargetDict"]["State"]["Excitement"] * 1.3)
                        if "Arousal" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Arousal"] = int(FinalData["TargetDict"]["State"]["Arousal"] * 1.3)
                        if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 1.3)
                        if "MPlea" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["MPlea"] = int(FinalData["TargetDict"]["Temporal"]["MPlea"] * 1.3)
                        if "CPlea" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["CPlea"] = int(FinalData["TargetDict"]["Temporal"]["CPlea"] * 1.3)
                        if "APlea" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["APlea"] = int(FinalData["TargetDict"]["Temporal"]["APlea"] * 1.3)
                        if "VPlea" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["VPlea"] = int(FinalData["TargetDict"]["Temporal"]["VPlea"] * 1.3)
                        if "PPlea" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["PPlea"] = int(FinalData["TargetDict"]["Temporal"]["PPlea"] * 1.3)
                elif Level == 4: # Slutty
                    if "Excitement" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Excitement"] = int(FinalData["TargetDict"]["State"]["Excitement"] * 2.0)
                    if "Arousal" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Arousal"] = int(FinalData["TargetDict"]["State"]["Arousal"] * 2.0)
                    if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 2.0)
                    if "MPlea" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["MPlea"] = int(FinalData["TargetDict"]["Temporal"]["MPlea"] * 2.0)
                    if "CPlea" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["CPlea"] = int(FinalData["TargetDict"]["Temporal"]["CPlea"] * 2.0)
                    if "APlea" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["APlea"] = int(FinalData["TargetDict"]["Temporal"]["APlea"] * 2.0)
                    if "VPlea" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["VPlea"] = int(FinalData["TargetDict"]["Temporal"]["VPlea"] * 2.0)
                    if "PPlea" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["PPlea"] = int(FinalData["TargetDict"]["Temporal"]["PPlea"] * 2.0)
        elif TraitID == "Openess0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # Liberated
                    # ""
                    if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 1.2)
                    if "Shame" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Shame"] = int(FinalData["TargetDict"]["Temporal"]["Shame"] * 0.7)
                elif Level == 2: # Repressed
                    # ""
                    if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 0.8)
                    if "Shame" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Shame"] = int(FinalData["TargetDict"]["Temporal"]["Shame"] * 1.2)
        elif TraitID == "PainResistance0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # High
                    # ""
                    if "Pain" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Pain"] = int(FinalData["TargetDict"]["Temporal"]["Pain"] * 0.8)
                elif Level == 2: # Low
                    # ""
                    if "Pain" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Pain"] = int(FinalData["TargetDict"]["Temporal"]["Pain"] * 1.2)
        elif TraitID == "ArousalEase0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # Easy
                    if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 1.2)
                    if "Arousal" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Arousal"] = int(FinalData["TargetDict"]["State"]["Arousal"] * 1.2)
                    if "Excitement" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Excitement"] = int(FinalData["TargetDict"]["State"]["Excitement"] * 1.2)
                elif Level == 2: # Hard
                    if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 0.8)
                    if "Arousal" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Arousal"] = int(FinalData["TargetDict"]["State"]["Arousal"] * 0.8)
                    if "Excitement" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Excitement"] = int(FinalData["TargetDict"]["State"]["Excitement"] * 0.8)
        elif TraitID == "ResponseToPleasure0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # Enjoys
                    # ""
                    if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 1.1)
                    # # if Plea:
                    #     if "Favor" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Favor"] = int(FinalData["TargetDict"]["Temporal"]["Favor"] * 1.2)
                    #     if "Loyalty" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Loyalty"] = int(FinalData["TargetDict"]["Temporal"]["Loyalty"] * 1.1)
                    #     if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 0.9)
                elif Level == 2: # Denies
                    if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 0.8)
                    # # if Plea:
                    #     if "Favor" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Favor"] = int(FinalData["TargetDict"]["Temporal"]["Favor"] * 0.8)
                    #     if "Loyalty" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Loyalty"] = int(FinalData["TargetDict"]["Temporal"]["Loyalty"] * 0.9)
                    #     if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 1.2)
        elif TraitID == "Perversion0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # Perverted
                    if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 1.2)
                    if "Excitement" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Excitement"] = int(FinalData["TargetDict"]["State"]["Excitement"] * 1.2)
                    if "Arousal" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Arousal"] = int(FinalData["TargetDict"]["State"]["Arousal"] * 1.2)
                    if "Shame" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Shame"] = int(FinalData["TargetDict"]["Temporal"]["Shame"] * 1.2)
                elif Level == 2: # Pure
                    if "Desire" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Desire"] = int(FinalData["TargetDict"]["Temporal"]["Desire"] * 0.8)
                    if "Excitement" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Excitement"] = int(FinalData["TargetDict"]["State"]["Excitement"] * 0.8)
                    if "Arousal" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Arousal"] = int(FinalData["TargetDict"]["State"]["Arousal"] * 0.8)
                    if "Shame" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Shame"] = int(FinalData["TargetDict"]["Temporal"]["Shame"] * 0.8)
        elif TraitID == "Dominance0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # Submissive
                    if "Submission" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Submission"] = int(FinalData["TargetDict"]["Temporal"]["Submission"] * 1.1)
                    if "Superiority" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Superiority"] = int(FinalData["TargetDict"]["Temporal"]["Superiority"] * 0.8)
                    if "Service" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Service"] = int(FinalData["TargetDict"]["Temporal"]["Service"] * 1.2)
                    # # if submission:
                    #     if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 0.8)
                    # # if superiority:
                    #     if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 1.2)
                elif Level == 2: # Dominant
                    if "Submission" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Submission"] = int(FinalData["TargetDict"]["Temporal"]["Submission"] * 0.8)
                    if "Superiority" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Superiority"] = int(FinalData["TargetDict"]["Temporal"]["Superiority"] * 1.2)
                    if "Service" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Service"] = int(FinalData["TargetDict"]["Temporal"]["Service"] * 0.8)
                    # # if submission:
                    #     if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 1.2)
                    # # if superiority:
                    #     if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 0.8)
        elif TraitID == "Forceful0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # Forceful
                    # TODO
                    ""
                elif Level == 2: # Exploitable
                    # TODO
                    ""
        elif TraitID == "Loyalty0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # Loyal
                    if "Loyalty" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Loyalty"] = int(FinalData["TargetDict"]["Temporal"]["Loyalty"] * 1.2)
                    # TODO if sexual
                    ""
                elif Level == 2: # Disloyal
                    if "Loyalty" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Loyalty"] = int(FinalData["TargetDict"]["Temporal"]["Loyalty"] * 0.8)
                    # TODO if sexual
                    ""
        elif TraitID == "Violence0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # Violent
                    # TODO
                    ""
                elif Level == 2: # Meek
                    # TODO
                    ""
        elif TraitID == "Beauty0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # Gorgeous
                    # IF ACTOR:
                        if "Excitement" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Excitement"] = int(FinalData["TargetDict"]["State"]["Excitement"] * 1.2)
                        if "Arousal" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Arousal"] = int(FinalData["TargetDict"]["State"]["Arousal"] * 1.2)
                        if "Favor" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Favor"] = int(FinalData["TargetDict"]["Temporal"]["Favor"] * 1.2)
                        if "Discomfort" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Discomfort"] = int(FinalData["TargetDict"]["Temporal"]["Discomfort"] * 0.8)
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 0.8)
                    # if target:
                        if "Excitement" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Excitement"] = int(FinalData["TargetDict"]["State"]["Excitement"] * 1.2)
                        if "Arousal" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Arousal"] = int(FinalData["TargetDict"]["State"]["Arousal"] * 1.2)
                        if "Favor" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Favor"] = int(FinalData["TargetDict"]["Temporal"]["Favor"] * 1.2)
                        if "Discomfort" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Discomfort"] = int(FinalData["TargetDict"]["Temporal"]["Discomfort"] * 0.8)
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 0.8)
                elif Level == 2: # Beautiful
                    # IF ACTOR:
                        if "Excitement" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Excitement"] = int(FinalData["TargetDict"]["State"]["Excitement"] * 1.1)
                        if "Arousal" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Arousal"] = int(FinalData["TargetDict"]["State"]["Arousal"] * 1.1)
                        if "Favor" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Favor"] = int(FinalData["TargetDict"]["Temporal"]["Favor"] * 1.1)
                        if "Discomfort" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Discomfort"] = int(FinalData["TargetDict"]["Temporal"]["Discomfort"] * 0.9)
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 0.9)
                    # if target:
                        if "Excitement" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Excitement"] = int(FinalData["TargetDict"]["State"]["Excitement"] * 1.1)
                        if "Arousal" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Arousal"] = int(FinalData["TargetDict"]["State"]["Arousal"] * 1.1)
                        if "Favor" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Favor"] = int(FinalData["TargetDict"]["Temporal"]["Favor"] * 1.1)
                        if "Discomfort" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Discomfort"] = int(FinalData["TargetDict"]["Temporal"]["Discomfort"] * 0.9)
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 0.9)
                elif Level == 3: # Ugly
                    # IF ACTOR:
                        if "Excitement" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Excitement"] = int(FinalData["TargetDict"]["State"]["Excitement"] * 0.9)
                        if "Arousal" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Arousal"] = int(FinalData["TargetDict"]["State"]["Arousal"] * 0.9)
                        if "Favor" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Favor"] = int(FinalData["TargetDict"]["Temporal"]["Favor"] * 0.9)
                        if "Discomfort" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Discomfort"] = int(FinalData["TargetDict"]["Temporal"]["Discomfort"] * 1.1)
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 1.1)
                    # if target:
                        if "Excitement" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Excitement"] = int(FinalData["TargetDict"]["State"]["Excitement"] * 0.9)
                        if "Arousal" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Arousal"] = int(FinalData["TargetDict"]["State"]["Arousal"] * 0.9)
                        if "Favor" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Favor"] = int(FinalData["TargetDict"]["Temporal"]["Favor"] * 0.9)
                        if "Discomfort" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Discomfort"] = int(FinalData["TargetDict"]["Temporal"]["Discomfort"] * 1.1)
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 1.1)
                elif Level == 4: # Disfigured
                    # IF ACTOR:
                        if "Excitement" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Excitement"] = int(FinalData["TargetDict"]["State"]["Excitement"] * 0.8)
                        if "Arousal" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Arousal"] = int(FinalData["TargetDict"]["State"]["Arousal"] * 0.8)
                        if "Favor" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Favor"] = int(FinalData["TargetDict"]["Temporal"]["Favor"] * 0.8)
                        if "Discomfort" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Discomfort"] = int(FinalData["TargetDict"]["Temporal"]["Discomfort"] * 1.2)
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 1.2)
                    # if target:
                        if "Excitement" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Excitement"] = int(FinalData["TargetDict"]["State"]["Excitement"] * 0.8)
                        if "Arousal" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Arousal"] = int(FinalData["TargetDict"]["State"]["Arousal"] * 0.8)
                        if "Favor" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Favor"] = int(FinalData["TargetDict"]["Temporal"]["Favor"] * 0.8)
                        if "Discomfort" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Discomfort"] = int(FinalData["TargetDict"]["Temporal"]["Discomfort"] * 1.2)
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] = int(FinalData["TargetDict"]["Resistance"] * 1.2)
        elif TraitID == "Shame0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # Shameful
                    if "Shame" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Shame"] = int(FinalData["TargetDict"]["Temporal"]["Shame"] * 1.4)
                elif Level == 2: # Shameless
                    if "Shame" in FinalData["TargetDict"]["Temporal"]: FinalData["TargetDict"]["Temporal"]["Shame"] = int(FinalData["TargetDict"]["Temporal"]["Shame"] * 0.6)
        elif TraitID == "Will0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # Strong Willed
                    ""
                    # TODO
                elif Level == 2: # Weak Willed
                    ""
                    # TODO
        elif TraitID == "Influence0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # Corruptor
                    ""
                    # TODO
                elif Level == 2: # Purificator
                    ""
                    # TODO
        elif TraitID == "Fertility0":
            if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
                if Level == 1: # Hyper Fertile
                    ""
                    # TODO
                elif Level == 2: # Infertile
                    ""
                    # TODO
        elif TraitID == "LewdBody0":
            ""
            # if TraitID in Globals.SoLNPCData[Target]["Traits"] and Globals.SoLNPCData[Target]["Traits"][TraitID]["Level"] != 0:
            #     ""
            #     # PLEA+++

    except Exception as e:
        ""
        # Log(3, "ERROR CommandProcessTrait", e, TraitID, OriginalData, FinalData)

    return OriginalData, FinalData

def GetrandomTraitData(TraitID):
    try:
        Data = {"ID":TraitID, "Level":0,"OtherData":{}}
        if TraitID == "Courage0":
            Data["Level"] = random.randint(0,2)
        elif TraitID == "Attitude0":
            Data["Level"] = random.randint(0,2)
        elif TraitID == "Pride0":
            Data["Level"] = random.randint(0,2)
        elif TraitID == "Dere0":
            Data["Level"] = random.randint(0,5)
        elif TraitID == "SelfControl0":
            Data["Level"] = random.randint(0,2)
        elif TraitID == "Cheerfulness0":
            Data["Level"] = random.randint(0,2)
        elif TraitID == "Shyness0":
            Data["Level"] = random.randint(0,2)
        elif TraitID == "Gullible0":
            Data["Level"] = random.randint(0,2)
        elif TraitID == "Charm0":
            Data["Level"] = random.randint(0,2)
        elif TraitID == "SubstanceResistance0":
            Data["Level"] = random.randint(0,2)
        elif TraitID == "SexualInterest0":
            Data["Level"] = random.randint(0,2)
        elif TraitID == "Virtue0":
            Data["Level"] = random.randint(0,2)
        elif TraitID == "Chastity0":
            Data["Level"] = random.randint(0,4)
        elif TraitID == "Openess0":
            Data["Level"] = random.randint(0,2)
        elif TraitID == "PainResistance0":
            Data["Level"] = random.randint(0,2)
        elif TraitID == "ArousalEase0":
            Data["Level"] = random.randint(0,2)
        elif TraitID == "ResponseToPleasure0":
            Data["Level"] = random.randint(0,2)
        elif TraitID == "Perversion0":
            Data["Level"] = random.randint(0,2)
        elif TraitID == "Dominance0":
            Data["Level"] = random.randint(0,2)
        elif TraitID == "Forceful0":
            Data["Level"] = random.randint(0,2)
        elif TraitID == "Loyalty0":
            Data["Level"] = random.randint(0,2)
        elif TraitID == "Violence0":
            Data["Level"] = random.randint(0,2)
        elif TraitID == "Beauty0":
            Data["Level"] = random.randint(0,4)
        elif TraitID == "Shame0":
            Data["Level"] = random.randint(0,2)
        elif TraitID == "Will0":
            Data["Level"] = random.randint(0,2)
        elif TraitID == "Influence0":
            Data["Level"] = random.randint(0,2)
        elif TraitID == "Fertility0":
            Data["Level"] = random.randint(0,2)
        elif TraitID == "LewdBody0":
            Data["V"] = random.randint(0,1)
            Data["A"] = random.randint(0,1)
            Data["B"] = random.randint(0,1)
            Data["P"] = random.randint(0,1)
            Data["M"] = random.randint(0,1)
            Data.pop("Level")
        return Data
    except Exception as e:
        print(e)
