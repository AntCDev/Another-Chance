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
import Globals

import pathlib


class UiLayoutDisclaimerMenu(object):
    def __init__(self):
        Globals.Layouts["DisclaimerUI"] = self
        Globals.LayoutsData["DisclaimerUI"] = {"Source":"creditsDisclaimerMenuUI", "Initialized":0}

    def UI(self):
        MainWindow = Globals.Layouts["MainF"]
        self.GUI = QWidget(MainWindow)

        self.LabelBack = QLabel(self.GUI)
        self.LabelBack.setGeometry(288,5,1024,1014)
        self.LabelBack.setProperty("Color","Dark")

        self.LabelMain = QLabel(self.GUI, objectName = "SubTitle")
        self.LabelMain.setGeometry(288,5,1024,954)
        self.LabelMain.setProperty("Color","Dark")
        self.LabelMain.setWordWrap(True)
        self.LabelMain.setText(f'''
The contents of this computer software are entirely a work of fiction. Use of this game software or its files in any way is exclusively restricted to use by adults. You must be above 18 years old or older in order to use this computer software in any way, shape, or form. You must also meet the minimum requirement for adulthood in your nation and state of residence in order to use this software in any way, shape, or form. Usage or viewing of this computer software by minors is expressly prohibited.

This software contains artistic and written depictions of sexual conduct. All characters, or any human-like representation of characters, engaged in sexual conduct in any way, shape, or form, are all fictional human being and 18 years of age or older consenting to the actions represented. No actual or identifiable human being was used during the development of this computer software. Any similarities to real or imagined person(s), pace(s), and/or group(s) are purely coincidental.

Please check to make sure this software doesn't violate your nation or estate's laws before using it. No part of this software is intended, nor to be interpreted for use in any real-life situation. By continuing beyond this point, the user agrees that they does not find such content offensive nor obscene and acknowledges that they will use this software with due legal diligence and in good and responsible conduct.

Any modification to the existing software, or implementation of new files, is responsibility of the user to corroborate that their contents, or effects doesn't violate or go against their nation and state laws.
        ''')

        self.AcceptButton = QPushButton(self.GUI, clicked = lambda: MainWindow.gotoLayout("MainMenuUI"))
        self.AcceptButton.setGeometry(700,964,250,50)
        self.AcceptButton.setProperty("Color","Light")
        self.AcceptButton.setText("I Accept")

    def Refresh(self):
        ""

################################

class UiLayoutCreditsMenu(object):
    def __init__(self):
        Globals.Layouts["CreditsUI"] = self
        Globals.LayoutsData["CreditsUI"] = {"Source":"creditsDisclaimerMenuUI", "Initialized":0}

    def UI(self):
        MainWindow = Globals.Layouts["MainF"]
        self.GUI = QWidget(MainWindow)

        self.LabelBack = QLabel(self.GUI)
        self.LabelBack.setGeometry(288,5,1024,954)
        self.LabelBack.setProperty("Color","Dark")
        self.LabelBack.setWordWrap(True)

        self.LabelContent = QLabel()
        self.LabelContent.setMaximumWidth(1024)
        self.LabelContent.setMinimumWidth(1024)
        self.LabelContent.setProperty("Color","Dark")
        self.LabelContent.setWordWrap(True)
        self.LabelContent.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        Text = '''
Per the usage of PyQT, of which the Riverbank Computing is responsible, this software is created under the GPL 3 License. A full copy of which has been anexed in the files, and can be accesed by the 'License' button below

Source and credits for the icons used:
www.game-icons.net
www.flaticon.com
www.patreon.com
www.discord.com
        '''
        self.LabelContent.setText(Text)

        self.scroll = QScrollArea(self.GUI)
        self.scroll.setGeometry(288,5,1024,954)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidget(self.LabelContent)

        self.LabelControl = QLabel(self.GUI)
        self.LabelControl.setGeometry(5,964,1592,55)
        self.LabelControl.setProperty("Color","Dark")

        self.ButtonMenu = QPushButton("Back", self.GUI, clicked = lambda: MainWindow.gotoPreviousLayout())
        self.ButtonMenu.setGeometry(15,970,200,45)

        self.ButtonLicense = QPushButton("License", self.GUI, clicked = lambda: MainWindow.gotoLayout("LicenseUI"))
        self.ButtonLicense.setGeometry(225,970,200,45)


    def Refresh(self):
        ""

class UiLayoutLicenseMenu(object):
    def __init__(self):
        Globals.Layouts["LicenseUI"] = self
        Globals.LayoutsData["LicenseUI"] = {"Source":"creditsDisclaimerMenuUI", "Initialized":0}

    def UI(self):
        MainWindow = Globals.Layouts["MainF"]
        self.GUI = QWidget(MainWindow)

        self.LabelBack = QLabel(self.GUI)
        self.LabelBack.setGeometry(288,5,1024,954)
        self.LabelBack.setProperty("Color","Dark")
        self.LabelBack.setWordWrap(True)

        self.LabelContent = QLabel()
        self.LabelContent.setMaximumWidth(1024)
        self.LabelContent.setMinimumWidth(1024)
        self.LabelContent.setProperty("Color","Dark")
        self.LabelContent.setWordWrap(True)
        self.LabelContent.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        try:
            with open('License.txt', 'r', encoding='UTF-8') as file:
                LicenseText = file.read()
            self.LabelContent.setText(LicenseText)
        except Exception as e:
            print(e)

        self.scroll = QScrollArea(self.GUI)
        self.scroll.setGeometry(288,5,1024,954)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidget(self.LabelContent)

        self.LabelControl = QLabel(self.GUI)
        self.LabelControl.setGeometry(5,964,1592,55)
        self.LabelControl.setProperty("Color","Dark")

        self.ButtonMenu = QPushButton("Back", self.GUI, clicked = lambda: MainWindow.gotoPreviousLayout())
        self.ButtonMenu.setGeometry(15,970,200,45)


    def Refresh(self):
        ""

def Initialize(self, Reference):
    if "CreditsUI" not in Globals.Layouts:
        Object = UiLayoutCreditsMenu()
    if "DisclaimerUI" not in Globals.Layouts:
        Object2 = UiLayoutDisclaimerMenu()
    if "LicenseUI" not in Globals.Layouts:
        Object2 = UiLayoutLicenseMenu()