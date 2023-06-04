from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QTextCursor
import Globals
import random
import os
Log = Globals.Layouts["MainF"].Log

def Initialize(self, Reference):
    LocationsList = ['SouthernStreet', 'EasternStreet', 'NorthernStreet', 'WesternStreet', 'MainStreet', 'DefenseStreet', 'LibraryStreet', 'TempleStreet', 'UniversityStreet', 'Home', 'UpperShoppingArea', 'Garrison', 'TrainingArea', 'LowerShoppingArea', 'ResidentialArea', 'Temple', 'CommunalArea', 'SlaversCamp', 'MainPlaza', 'Academia', 'PaladinsArea', 'Library', 'University', 'Laboratory', 'YourRoom']
    for ID in LocationsList:
        Globals.Locations[ID] = {"ID":ID, "Reference":Reference, "OtherData":{}}


def GetLocationButtons(self, Location):
    ButtonsList = []
    if Location == "Home":
        def SleepFunc():
            PCID = Globals.SoLPCData["ID"]
            Globals.References["SoLFunctions"].Sleep(PCID)
            # Globals.References["SoLFunctions"].PassTime(Globals.Layouts["SoLUI"], 480)

        SleepButton = QPushButton(clicked = lambda: SleepFunc())
        SleepButton.setText("Sleep")
        SleepButton.setMinimumWidth(165)
        SleepButton.setMaximumWidth(165)
        SleepButton.setMinimumHeight(35)
        SleepButton.setMaximumHeight(35)
        ButtonsList.append(SleepButton)

    return ButtonsList
