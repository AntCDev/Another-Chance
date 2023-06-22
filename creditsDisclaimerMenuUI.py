
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import Globals
import os
import pathlib

class UiLayoutDisclaimerMenu:
    def __init__(self):
        Globals.Layouts["DisclaimerUI"] = self
        Globals.LayoutsData["DisclaimerUI"] = {"Source":"creditsDisclaimerMenuUI", "Initialized":0}

    def UI(self):
        MainWindow = Globals.Layouts["MainF"]
        self.GUI = QWidget(MainWindow)

        # self.LabelBack = QLabel(self.GUI)
        # self.LabelBack.setGeometry(288,5,1024,1014)
        # self.LabelBack.setProperty("Color","Dark")

        self.LabelMain = QLabel(self.GUI, objectName = "SubTitle")
        self.LabelMain.setGeometry(288,5,1024,954)
        self.LabelMain.setProperty("Color","Dark")
        self.LabelMain.setWordWrap(True)
        self.LabelMain.setText('''
The contents of this computer software are entirely a work of fiction. Use of this game software or its files in any way is exclusively restricted to use by adults. You must be above 18 years old or older in order to use this computer software in any way, shape, or form. You must also meet the minimum requirement for adulthood in your nation and state of residence in order to use this software in any way, shape, or form. Usage or viewing of this computer software by minors is expressly prohibited.

This software contains artistic and written depictions of sexual conduct. All characters, or any human-like representation of characters, engaged in sexual conduct in any way, shape, or form, are all fictional human being and 18 years of age or older consenting to the actions represented. No actual or identifiable human being was used during the development of this computer software. Any similarities to real or imagined person(s), place(s), and/or group(s) are purely coincidental.

Please check to make sure this software doesn't violate your nation or estate's laws before using it. No part of this software is intended, nor to be interpreted for use in any real-life situation. By continuing beyond this point, the user agrees that they does not find such content offensive nor obscene and acknowledges that they will use this software with due legal diligence and in good and responsible conduct.

Any modification to the existing software, or implementation of new files, is responsibility of the user to corroborate that their contents or effects doesn't violate or go against their nation and state laws.
        ''')

        self.ControlWidget = QWidget(self.GUI)
        self.ControlWidget.setProperty("Color", "Dark")
        self.ControlWidget.setGeometry(288,959,1024,60)

        self.AcceptButton = QPushButton(self.ControlWidget, clicked = lambda: MainWindow.gotoLayout("MainMenuUI"))
        self.AcceptButton.setGeometry(5,5,250,50)
        self.AcceptButton.setProperty("Color","Light")
        self.AcceptButton.setText("I Accept")

    def Refresh(self):
        ""

    def ResizeEvent(self):
        Width = Globals.Layouts["MainF"].width()
        Height = Globals.Layouts["MainF"].height()

        self.ControlWidget.move(288,Height-65)

        self.LabelMain.setGeometry(288,5,1024,Height-75)

################################

class UiLayoutCreditsMenu:
    def __init__(self):
        Globals.Layouts["CreditsUI"] = self
        Globals.LayoutsData["CreditsUI"] = {"Source":"creditsDisclaimerMenuUI", "Initialized":0}

    def UI(self):
        MainWindow = Globals.Layouts["MainF"]
        self.GUI = QWidget(MainWindow)

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
        self.scroll.setProperty("Color","Dark")

        self.ControlWidget = QWidget(self.GUI)
        self.ControlWidget.setGeometry(5,964,1592,55)
        self.ControlWidget.setProperty("Color","Dark")

        self.ButtonMenu = QPushButton("Back", self.ControlWidget, clicked = lambda: MainWindow.gotoPreviousLayout())
        self.ButtonMenu.setGeometry(10,96,200,45)

        self.ButtonLicense = QPushButton("License", self.ControlWidget, clicked = lambda: MainWindow.gotoLayout("LicenseUI"))
        self.ButtonLicense.setGeometry(220,96,200,45)

        #
        # ##############
        # self.ClothesWidget = QWidget(self.GUI)
        # self.ClothesWidget.setGeometry(10,10,500,300)
        # # self.ClothesWidget.setStyleSheet('''background-color:rgb(255,0,0)''')
        #
        # self.ClothesLayout = QHBoxLayout()
        #
        # ####
        # self.ClothesLeftLayout = QVBoxLayout()
        # self.ClothesLeftLayout.setSpacing(0)
        # self.ClothesLeftLayout.setContentsMargins(0,0,0,0)
        #
        # ##
        # self.ClothesPickLayout = QHBoxLayout()
        # self.ClothesPicker = QListWidget()
        # self.ClothesPicker.addItem("Bra")
        # self.ClothesPicked = QListWidget()
        # self.ClothesPicked.addItem("Hat")
        # self.ClothesPicked.addItem("Glasses")
        # self.ClothesPicked.addItem("Dress")
        # self.ClothesPicked.addItem("Panties")
        # self.ClothesPicked.addItem("Shoes")
        # self.ClothesPickLayout.addWidget(self.ClothesPicker)
        # self.ClothesPickLayout.addWidget(self.ClothesPicked)
        #
        # self.ClothesPickHolder = QWidget()
        # self.ClothesPickHolder.setLayout(self.ClothesPickLayout)
        #
        # self.ClothesLeftLayout.addWidget(self.ClothesPickHolder)
        # ##
        #
        # ##
        # self.ClothesControlLayout = QHBoxLayout()
        #
        # self.ClothesControlPicker = QWidget()
        # self.ClothesControlPickerLeft = QPushButton(self.ClothesControlPicker)
        # self.ClothesControlPickerLeft.setText("<-")
        # self.ClothesControlPickerLeft.setGeometry(0,0,20,20)
        # self.ClothesControlPickerRight = QPushButton(self.ClothesControlPicker)
        # self.ClothesControlPickerRight.setText("->")
        # self.ClothesControlPickerRight.setGeometry(20,0,20,20)
        #
        # self.ClothesControlOrder = QWidget()
        # self.ClothesControlOrderUp = QPushButton(self.ClothesControlOrder)
        # self.ClothesControlOrderUp.setText("↑")
        # self.ClothesControlOrderUp.setGeometry(0,0,20,20)
        # self.ClothesControlOrderDown = QPushButton(self.ClothesControlOrder)
        # self.ClothesControlOrderDown.setText("↓")
        # self.ClothesControlOrderDown.setGeometry(20,0,20,20)
        #
        # self.ClothesControlLayout.addWidget(self.ClothesControlPicker)
        # self.ClothesControlLayout.addWidget(self.ClothesControlOrder)
        #
        # self.ClothesControlHolder = QWidget()
        # self.ClothesControlHolder.setLayout(self.ClothesControlLayout)
        # self.ClothesControlHolder.setMinimumSize(40,40)
        # self.ClothesLeftLayout.addWidget(self.ClothesControlHolder)
        # ##
        #
        # self.ClothesLeftHolder = QWidget()
        # self.ClothesLeftHolder.setLayout(self.ClothesLeftLayout)
        # self.ClothesLayout.addWidget(self.ClothesLeftHolder)
        # ####
        #
        #
        # ####
        # self.ClothesRightLayout = QVBoxLayout()
        # # self.ClothesRightLayout.setSpacing(0)
        # self.ClothesRightLayout.setContentsMargins(0,0,0,0)
        #
        # ##
        # self.ClothesHeadLayout = QHBoxLayout()
        # self.ClothesHeadLayout.setSpacing(0)
        # self.ClothesHeadLayout.setContentsMargins(0,0,0,0)
        #
        # self.BaseHead = QLabel("Head")
        # self.BaseHead.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "OtherResources" / "Head.png" ) ))
        # self.BaseHead.setScaledContents(True)
        # self.BaseHead.setMinimumSize(64,64)
        # self.BaseHead.setMaximumSize(64,64)
        # self.ClothesHeadLayout.addWidget(self.BaseHead)
        #
        # self.EmptyHead = QLabel("Empty")
        # self.EmptyHead.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "OtherResources" / "Hat.png" ) ))
        # self.EmptyHead.setScaledContents(True)
        # self.EmptyHead.setMinimumSize(64,64)
        # self.EmptyHead.setMaximumSize(64,64)
        # self.ClothesHeadLayout.addWidget(self.EmptyHead)
        #
        # self.EmptyHead2 = QLabel("Empty2")
        # self.EmptyHead2.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "OtherResources" / "Glasses.png" ) ))
        # self.EmptyHead2.setScaledContents(True)
        # self.EmptyHead2.setMinimumSize(64,64)
        # self.EmptyHead2.setMaximumSize(64,64)
        # self.ClothesHeadLayout.addWidget(self.EmptyHead2)
        #
        # self.ClothesHeadHolder =QWidget()
        # self.ClothesHeadHolder.setLayout(self.ClothesHeadLayout)
        # self.ClothesRightLayout.addWidget(self.ClothesHeadHolder)
        # ##
        #
        # ##
        # self.ClothesBodyLayout = QHBoxLayout()
        # self.ClothesBodyLayout.setSpacing(0)
        # self.ClothesBodyLayout.setContentsMargins(0,0,0,0)
        #
        # self.BaseBody = QLabel("Body")
        # self.BaseBody.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "OtherResources" / "Body.png" ) ))
        # self.BaseBody.setScaledContents(True)
        # self.BaseBody.setMinimumSize(64,64)
        # self.BaseBody.setMaximumSize(64,64)
        # self.ClothesBodyLayout.addWidget(self.BaseBody)
        #
        # self.EmptyBody = QLabel("Empty")
        # self.EmptyBody.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "OtherResources" / "Dress.png" ) ))
        # self.EmptyBody.setScaledContents(True)
        # self.EmptyBody.setMinimumSize(64,64)
        # self.EmptyBody.setMaximumSize(64,64)
        # self.ClothesBodyLayout.addWidget(self.EmptyBody)
        #
        # self.EmptyBody2 = QLabel()
        # self.EmptyBody2.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "OtherResources" / "No Target.png" ) ))
        # self.EmptyBody2.setScaledContents(True)
        # self.EmptyBody2.setMinimumSize(64,64)
        # self.EmptyBody2.setMaximumSize(64,64)
        # self.ClothesBodyLayout.addWidget(self.EmptyBody2)
        #
        #
        # self.ClothesBodyHolder =QWidget()
        # self.ClothesBodyHolder.setLayout(self.ClothesBodyLayout)
        # self.ClothesRightLayout.addWidget(self.ClothesBodyHolder)
        # ##
        #
        # ##
        # self.ClothesPantsLayout = QHBoxLayout()
        # self.ClothesPantsLayout.setSpacing(0)
        # self.ClothesPantsLayout.setContentsMargins(0,0,0,0)
        #
        # self.BasePants = QLabel("Pants")
        # self.BasePants.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "OtherResources" / "Pants.png" ) ))
        # self.BasePants.setScaledContents(True)
        # self.BasePants.setMinimumSize(64,64)
        # self.BasePants.setMaximumSize(64,64)
        # self.ClothesPantsLayout.addWidget(self.BasePants)
        #
        # self.EmptyPants = QLabel("Empty")
        # self.EmptyPants.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "OtherResources" / "Dress.png" ) ))
        # self.EmptyPants.setScaledContents(True)
        # self.EmptyPants.setMinimumSize(64,64)
        # self.EmptyPants.setMaximumSize(64,64)
        # self.ClothesPantsLayout.addWidget(self.EmptyPants)
        #
        # self.EmptyPants2 = QLabel()
        # self.EmptyPants2.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "OtherResources" / "Panties.png" ) ))
        # self.EmptyPants2.setScaledContents(True)
        # self.EmptyPants2.setMinimumSize(64,64)
        # self.EmptyPants2.setMaximumSize(64,64)
        # self.ClothesPantsLayout.addWidget(self.EmptyPants2)
        #
        # self.ClothesPantsHolder =QWidget()
        # self.ClothesPantsHolder.setLayout(self.ClothesPantsLayout)
        # self.ClothesRightLayout.addWidget(self.ClothesPantsHolder)
        # ##
        #
        # ##
        # self.ClothesShoesLayout = QHBoxLayout()
        # self.ClothesShoesLayout.setSpacing(0)
        # self.ClothesShoesLayout.setContentsMargins(0,0,0,0)
        #
        # self.BaseShoes = QLabel("Shoes")
        # self.BaseShoes.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "OtherResources" / "Feet.png" ) ))
        # self.BaseShoes.setScaledContents(True)
        # self.BaseShoes.setMinimumSize(64,64)
        # self.BaseShoes.setMaximumSize(64,64)
        # self.ClothesShoesLayout.addWidget(self.BaseShoes)
        #
        # self.EmptyShoes = QLabel("Empty")
        # self.EmptyShoes.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "OtherResources" / "Shoes.png" ) ))
        # self.EmptyShoes.setScaledContents(True)
        # self.EmptyShoes.setMinimumSize(64,64)
        # self.EmptyShoes.setMaximumSize(64,64)
        # self.ClothesShoesLayout.addWidget(self.EmptyShoes)
        #
        # self.EmptyShoes2 = QLabel()
        # self.EmptyShoes2.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "OtherResources" / "Socks.png" ) ))
        # self.EmptyShoes2.setScaledContents(True)
        # self.EmptyShoes2.setMinimumSize(64,64)
        # self.EmptyShoes2.setMaximumSize(64,64)
        # self.ClothesShoesLayout.addWidget(self.EmptyShoes2)
        #
        #
        # self.ClothesShoesHolder =QWidget()
        # self.ClothesShoesHolder.setLayout(self.ClothesShoesLayout)
        # self.ClothesRightLayout.addWidget(self.ClothesShoesHolder)
        # ##
        #
        # self.ClothesWidget.setLayout(self.ClothesRightLayout)
        #
        # self.ClothesRightHolder = QWidget()
        # self.ClothesRightHolder.setLayout(self.ClothesRightLayout)
        # self.ClothesLayout.addWidget(self.ClothesRightHolder)
        #
        # ####
        # 
        # # self.ClothesWidget.setLayout(self.ClothesRightLayout)
        # self.ClothesWidget.setLayout(self.ClothesLayout)

    def Refresh(self):
        ""

    def ResizeEvent(self):
        Width = Globals.Layouts["MainF"].width()
        Height = Globals.Layouts["MainF"].height()
        Diff = 1024 - Height

        self.scroll.setGeometry(288,5,1024,954-Diff)
        self.ControlWidget.setGeometry(5,964-Diff,1592,55)


class UiLayoutLicenseMenu:
    def __init__(self):
        Globals.Layouts["LicenseUI"] = self
        Globals.LayoutsData["LicenseUI"] = {"Source":"creditsDisclaimerMenuUI", "Initialized":0}

    def UI(self):
        MainWindow = Globals.Layouts["MainF"]
        self.GUI = QWidget(MainWindow)

        self.LabelContent = QLabel()
        self.LabelContent.setMaximumWidth(1024)
        self.LabelContent.setMinimumWidth(1024)
        self.LabelContent.setProperty("Color","Dark")
        self.LabelContent.setWordWrap(True)
        self.LabelContent.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        try:
            with pathlib.Path.open('License.txt', 'r', encoding='UTF-8') as file:
                LicenseText = file.read()
            self.LabelContent.setText(LicenseText)
        except Exception as e:
            print(e)

        self.scroll = QScrollArea(self.GUI)
        self.scroll.setGeometry(288,5,1024,954)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidget(self.LabelContent)
        self.scroll.setProperty("Color","Dark")

        self.ControlWidget = QWidget(self.GUI)
        self.ControlWidget.setGeometry(5,964,1592,55)
        self.ControlWidget.setProperty("Color","Dark")

        self.ButtonMenu = QPushButton("Back", self.ControlWidget, clicked = lambda: MainWindow.gotoPreviousLayout())
        self.ButtonMenu.setGeometry(10,6,200,45)

    def Refresh(self):
        ""

    def ResizeEvent(self):
        Width = Globals.Layouts["MainF"].width()
        Height = Globals.Layouts["MainF"].height()
        Diff = 1024 - Height

        self.scroll.setGeometry(288,5,1024,954-Diff)
        self.ControlWidget.setGeometry(5,964-Diff,1592,55)


def Initialize(self, Reference):
    if "CreditsUI" not in Globals.Layouts:
        Object = UiLayoutCreditsMenu()
    if "DisclaimerUI" not in Globals.Layouts:
        Object2 = UiLayoutDisclaimerMenu()
    if "LicenseUI" not in Globals.Layouts:
        Object2 = UiLayoutLicenseMenu()
