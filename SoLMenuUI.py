
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QTextCursor
import Globals
# from UiStyle import *
# from SoLMenuFunctions import *
from time import sleep
import os
Log = Globals.Layouts["MainF"].Log

class UiLayoutSoLMenu(QWidget):
    RefreshSignal1 = pyqtSignal()
    RefreshSignal2 = pyqtSignal()
    RefreshSignal3 = pyqtSignal()

    CTS1 = pyqtSignal()
    CTS2 = pyqtSignal()
    CTS3 = pyqtSignal()

    CommandCheckSignal = pyqtSignal()

    def __init__(self):
        try:
            super().__init__()
            Globals.Layouts["SoLUI"] = self
            Globals.LayoutsData["SoLUI"] = {"Source":"SoLMenuUI", "Initialized":0}

        except Exception as e:
            Log(4, "ERROR SOL UI INITIALIZE", e)


    def UI(self):
        MainWindow = Globals.Layouts["MainF"]
        self.GUI = QWidget(MainWindow)

        # STATUS LABEL AT THE TOP
        self.labelStatus = QLabel(self.GUI)
        self.labelStatus.setGeometry(365,5,875,30)
        self.labelStatus.setWordWrap(True)
        self.labelStatus.setFont(QFont('Segoe UI', 11))
        self.labelStatus.setText("10:40        18 June 2050        Temple       Get some slime        Defeat the bees.")
        self.labelStatus.setAlignment(Qt.AlignCenter)
        self.labelStatus.setProperty("Color","Dark")

        # MAIN LABEL AT THE CENTRE
        self.labelMain = QLabel(self.GUI)
        self.labelMain.setWordWrap(True)
        self.labelMain.setFont(QFont('Segoe UI', 13))
        self.labelMain.setAlignment(Qt.AlignLeft)
        self.labelMain.setIndent(9)
        self.labelMain.setProperty("Color","Dark")

        self.scrollMain = QScrollArea(self.GUI)
        self.scrollMain.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollMain.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollMain.setGeometry(365,40,875,580)
        self.scrollMain.setWidgetResizable(True)
        self.scrollMain.setWidget(self.labelMain)


        self.BackNPCLabel = QLabel(self.GUI)
        self.BackNPCLabel.setGeometry(1245,5,355,1015)
        self.BackNPCLabel.setProperty("Color","Dark")

        self.FormNPC = QVBoxLayout()
        self.ScrollNPC = QScrollArea(self.GUI)
        self.ScrollNPC.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollNPC.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollNPC.setGeometry(1245,5,355,1015)

        self.GroupBoxNPC = QGroupBox()
        self.GroupBoxNPC.setLayout(self.FormNPC)
        self.GroupBoxNPC.setMinimumWidth(350)
        self.ScrollNPC.setWidget(self.GroupBoxNPC)
        self.FormNPC.setContentsMargins(0, 0, 0, 5)
        self.FormNPC.WigetsDict = {}

        self.ScrollPC = QScrollArea(self.GUI)
        self.ScrollPC.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollPC.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollPC.setGeometry(5,5,355,1015)
        self.ScrollPC.setProperty("Color","Dark")

        self.FormPC = QVBoxLayout()
        self.GroupBoxPC = QGroupBox()
        self.GroupBoxPC.setLayout(self.FormPC)
        self.ScrollPC.setWidget(self.GroupBoxPC)
        self.ScrollPC.setMinimumWidth(355)
        self.ScrollPC.setMaximumWidth(355)
        self.ScrollPC.setMinimumHeight(1015)
        self.ScrollPC.setMaximumHeight(1015)
        self.GroupBoxPC.setMinimumWidth(355)
        self.GroupBoxPC.setMaximumWidth(355)
        self.FormPC.setContentsMargins(3, 5, 3, 5)
        self.FormPC.WidgetsList = []

        self.labelButtons = QLabel(self.GUI)
        self.labelButtons.setGeometry(365,625,875,395)
        self.labelButtons.setProperty("Color","Dark")


        self.ScrollSoLButtons = QScrollArea(self.GUI)
        self.ScrollSoLButtons.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollSoLButtons.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollSoLButtons.setGeometry(370,630,870,245)

        self.FormSoLButtons = QGridLayout()
        self.FormSoLButtons.setContentsMargins(0, 0, 0, 0)
        self.GroupBoxSoLButtons = QGroupBox()
        self.GroupBoxSoLButtons.setLayout(self.FormSoLButtons)
        self.ScrollSoLButtons.setWidget(self.GroupBoxSoLButtons)
        self.GroupBoxSoLButtons.setMinimumWidth(870)
        self.FormSoLButtons.WidgetsList = []

        self.ScrollSoLEventButtons = QScrollArea(self.GUI)
        self.ScrollSoLEventButtons.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollSoLEventButtons.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollSoLEventButtons.setGeometry(370,885,870,80)

        self.FormSOLEventButtons = QGridLayout()
        self.FormSOLEventButtons.setContentsMargins(0, 0, 0, 0)
        self.GroupBoxSolEventButtons = QGroupBox()
        self.GroupBoxSolEventButtons.setLayout(self.FormSOLEventButtons)
        self.ScrollSoLEventButtons.setWidget(self.GroupBoxSolEventButtons)
        self.GroupBoxSolEventButtons.setMinimumWidth(870)
        self.FormSOLEventButtons.WidgetsList = []

        self.ScrollControlCommands = QScrollArea(self.GUI)
        self.ScrollControlCommands.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollControlCommands.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollControlCommands.setGeometry(370,970,870,50)

        self.FormControlCommands = QGridLayout()
        self.FormControlCommands.setContentsMargins(0, 0, 0, 0)
        self.GroupBoxControlCommands = QGroupBox()
        self.GroupBoxControlCommands.setLayout(self.FormControlCommands)
        self.ScrollControlCommands.setWidget(self.GroupBoxControlCommands)
        self.GroupBoxControlCommands.setMinimumWidth(870)
        self.FormControlCommands.WidgetsList = []


        self.Refresh()

    def Refresh(self):
        Globals.References["SoLFunctions"].Refresh(self)


    def OldUI(self):
        MainWindow = Globals.Layouts["MainF"]
        self.GUI = QWidget(MainWindow)
        # MainWindow.setWindowIcon(QtGui.QIcon('PhotoIcon.png'))

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
         ''')

        # THE LABEL BEHIND  THE PLAYER ELEMENTS
        self.labelPStatusHolder = QLabel(self.GUI)
        self.labelPStatusHolder.setGeometry(10,10,202,565)
        self.labelPStatusHolder.setWordWrap(True)

        # THE LABEL BEHIND THE TARGET ELEMENTS
        self.labelTStatusHolder = QLabel(self.GUI)
        self.labelTStatusHolder.setGeometry(1070,10,202,565)
        self.labelTStatusHolder.setWordWrap(True)

        # STATUS LABEL AT THE TOP
        self.labelStatus = QLabel(self.GUI)
        self.labelStatus.setGeometry(222,10,838,20)
        self.labelStatus.setWordWrap(True)
        self.labelStatus.setFont(QFont('Segoe UI', 9))
        self.labelStatus.setText("10:40        18 June 2050        Temple       Get some slime        Defeat the bees.")
        self.labelStatus.setAlignment(Qt.AlignCenter)

        # MAIN LABEL AT THE CENTRE
        self.labelMain = QLabel(self.GUI)
        self.labelMain.setGeometry(222,40,838,535)
        self.labelMain.setWordWrap(True)
        self.labelMain.setFont(QFont('Segoe UI', 12))
        self.labelMain.setText('''_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ \nYou are at the temple, it's filled with people and priests alike, prayng or sating their spiritual needs in here \nIt's currently a bit early in the morning, and as such streets are somewhat busy \nYou are talking with "3" who stares at you with that overly cheerful smile that relieve you just by looking at it''')
        self.labelMain.setAlignment(Qt.AlignLeft)
        self.labelMain.setIndent(9)

        # LABEL HOLDING THE COMMANDS AT THE BOTTOM
        self.labelCommands = QLabel(self.GUI)
        self.labelCommands.setGeometry(5,583,1270,205)
        self.labelCommands.setWordWrap(True)

            ##### STARTING TO BUILD UP THE TARGET STATUS ITEMS

        # LABEL HOLDING THE TARGET IMAGE
        self.labelTImage = QLabel(self.GUI)
        self.labelTImage.setGeometry(1080,20,120,120)
        self.labelTImage.setAlignment(Qt.AlignCenter)
        self.labelTImage.setScaledContents(True)
        self.labelTImage.setPixmap(QPixmap("/images/None.png"))


        # BUTTONS TO THE RIGHT OF THE TARGET IMAGE
        self.statusTButton1 = QPushButton(self.GUI, clicked = lambda: DescriptionCheck(self, "Target"))
        self.statusTButton1.setGeometry(1206,20,60,35)
        self.statusTButton1.setText("Description")
        self.statusTButton1.setFont(QFont('Segoe UI', 9))
        self.statusTButton1.show()

        self.statusTButton2 = QPushButton(self.GUI)
        self.statusTButton2.setGeometry(1206,60,60,35)
        self.statusTButton2.setText("Switch")
        self.statusTButton2.setFont(QFont('Segoe UI', 9))
        self.statusTButton2.clicked.connect(self.statusTButtonAction2)
        self.statusTButton2.show()

        self.statusTButton3 = QPushButton(self.GUI)
        self.statusTButton3.setGeometry(1206,100,60,35)
        self.statusTButton3.setText("Portrait")
        self.statusTButton3.setFont(QFont('Segoe UI', 9))
        self.statusTButton3.show()
        self.statusTButton3.clicked.connect(self.statusTButtonAction3)


        #### ENERGY STATUS
        self.labelTEnergy = QLabel(self.GUI)
        self.labelTEnergy.setGeometry(1080,143,206,50)
        self.labelTEnergy.setText("Energy: 930")
        self.labelTEnergy.setFont(QFont('Segoe UI', 9))
        self.labelTEnergy.setAlignment(Qt.AlignHCenter)

        #### ENERGY INDICATORS
        self.labelTEnergy1 = QLabel(self.GUI)
        self.labelTEnergy1.setGeometry(1083,168,20,25)
        self.labelTEnergy1.setStyleSheet('''QLabel{background-color:rgb(222, 222, 110) }''')
        self.labelTEnergy2 = QLabel(self.GUI)
        self.labelTEnergy2.setGeometry(1103,168,20,25)
        self.labelTEnergy2.setStyleSheet('''QLabel{background-color:rgb(222, 222, 110) }''')
        self.labelTEnergy3 = QLabel(self.GUI)
        self.labelTEnergy3.setGeometry(1123,168,20,25)
        self.labelTEnergy3.setStyleSheet('''QLabel{background-color:rgb(222, 222, 110) }''')
        self.labelTEnergy4 = QLabel(self.GUI)
        self.labelTEnergy4.setGeometry(1143,168,20,25)
        self.labelTEnergy4.setStyleSheet('''QLabel{background-color:rgb(222, 222, 110) }''')
        self.labelTEnergy5 = QLabel(self.GUI)
        self.labelTEnergy5.setGeometry(1163,168,20,25)
        self.labelTEnergy5.setStyleSheet('''QLabel{background-color:rgb(222, 222, 110) }''')
        self.labelTEnergy6 = QLabel(self.GUI)
        self.labelTEnergy6.setGeometry(1183,168,20,25)
        self.labelTEnergy6.setStyleSheet('''QLabel{background-color:rgb(222, 222, 110) }''')
        self.labelTEnergy7 = QLabel(self.GUI)
        self.labelTEnergy7.setGeometry(1203,168,20,25)
        self.labelTEnergy7.setStyleSheet('''QLabel{background-color:rgb(222, 222, 110) }''')
        self.labelTEnergy8 = QLabel(self.GUI)
        self.labelTEnergy8.setGeometry(1223,168,20,25)
        self.labelTEnergy8.setStyleSheet('''QLabel{background-color:rgb(222, 222, 110) }''')
        self.labelTEnergy9 = QLabel(self.GUI)
        self.labelTEnergy9.setGeometry(1242,168,20,25)
        self.labelTEnergy9.setStyleSheet('''QLabel{background-color:rgb(222, 222, 110) }''')
        self.labelTEnergy10 = QLabel(self.GUI)
        self.labelTEnergy10.setGeometry(1263,168,20,25)
        self.labelTEnergy10.setStyleSheet('''QLabel{background-color:rgb(222, 222, 110) }''')


        #### BUTTONS TO SWITCH TARGETS


        self.npcButton1 = QPushButton(self.GUI)
        self.npcButton1.setGeometry(1080,196,186,30)
        # self.npcButton1.setText("1")
        self.npcButton1.setFont(QFont('Segoe UI', 11))
        self.npcButton1.clicked.connect(self.NPCButton1)

        self.npcButton2 = QPushButton(self.GUI)
        self.npcButton2.setGeometry(1080,232,186,30)
        # self.npcButton2.setText("2")
        self.npcButton2.setFont(QFont('Segoe UI', 11))
        self.npcButton2.clicked.connect(self.NPCButton2)

        self.npcButton3 = QPushButton(self.GUI)
        self.npcButton3.setGeometry(1080,268,186,30)
        # self.npcButton3.setText("4")
        self.npcButton3.setFont(QFont('Segoe UI', 11))
        self.npcButton3.clicked.connect(self.NPCButton3)

        self.npcButton4 = QPushButton(self.GUI)
        self.npcButton4.setGeometry(1080,304,186,30)
        # self.npcButton4.setText("5")
        self.npcButton4.setFont(QFont('Segoe UI', 11))
        self.npcButton4.clicked.connect(self.NPCButton4)

        self.npcButton5 = QPushButton(self.GUI)
        self.npcButton5.setGeometry(1080,340,186,30)
        # self.npcButton5.setText("6")
        self.npcButton5.setFont(QFont('Segoe UI', 11))
        self.npcButton5.clicked.connect(self.NPCButton5)
        # self.CoverLabel = QLabel(self.GUI)
        # self.CoverLabel.setGeometry(1080,196,186,204)

        #### BUTTONS TO SWITCH NPC PAGE
        self.npcButtonLeft = QPushButton(self.GUI)
        self.npcButtonLeft.setGeometry(1080,376,90,30)
        self.npcButtonLeft.setText("<--")
        self.npcButtonLeft.setFont(QFont('Segoe UI', 11))
        self.npcButtonLeft.clicked.connect(self.NPCButtonLeft)
        self.npcButtonRight = QPushButton(self.GUI)
        self.npcButtonRight.setGeometry(1176,376,90,30)
        self.npcButtonRight.setText("-->")
        self.npcButtonRight.setFont(QFont('Segoe UI', 11))
        self.npcButtonRight.clicked.connect(self.NPCButtonRight)




        self.ScrollNPC = QScrollArea(self.GUI)
        self.ScrollNPC.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollNPC.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollNPC.setGeometry(1240,5,356,1015)
        self.ScrollNPC.setStyleSheet('''
        .QScrollArea{
        border: none;
        background-color:rgb(23, 23, 23);
        }
        QGroupBox{
        border: none;
        }
        ''')

        # self.ScrollSoLButtons = QScrollArea(self.GUI)
        # self.ScrollSoLButtons.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.ScrollSoLButtons.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        # self.ScrollSoLButtons.setGeometry(365,805,870,215)
        # self.ScrollSoLButtons.setStyleSheet('''
        # .QScrollArea{
        # border: 1px solid black;
        # background-color:rgb(23, 23, 23);
        # }
        # QGroupBox{
        # border: none;
        # background:none;
        # }
        # ''')


        #### LABEL SHOWING CURRENT STATUS OF TARGET
        self.object = QLabel()
        boldFont=QtGui.QFont('Segoe UI', 9)
        boldFont.setBold(True)
        # object.setFont(boldFont)
        self.object.setText("Text")
        self.object.setWordWrap(True)
        self.object.setAlignment(Qt.AlignLeft | Qt.AlignTop)

        self.scroll = QScrollArea(self.GUI)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setGeometry(1080,416,186,150)
        self.scroll.setWidgetResizable(True)
        self.scroll.setStyleSheet('''
        QScrollArea{
        border: 1px solid black;
        background-color:rgb(35, 35, 35);
        }

        ''')
        # BUILD WITHING THE SoLMenuFunctions FILE, SO IT CAN BE CHANGED AT EASE
        self.scroll.setWidget(self.object)
        setScrollStatus(self, '''Mood: Really Happy (8) \nDiscomfort:345 \nFavor: 1823 \nDisgust: 30 \nShame: 10 \n ''')
        # def setScrollStatus(self, object):
        #     self.scroll.setWidget(QWidget)




            ##### STARTING TO BUILD UP THE PLAYER STATUS ITEMS

        # LABEL HOLDING THE PLAYER IMAGE
        self.labelPImage = QLabel(self.GUI)
        self.labelPImage.setGeometry(20,20,200,200)
        self.labelPImage.setAlignment(Qt.AlignCenter)
        self.labelPImage.setScaledContents(True)
        self.labelPImage.setPixmap(QPixmap("C:/Users/PC/Downloads/FHuman_2_2_2_0_3_White_Black_4.jpg"))


        # BUTTONS TO THE RIGHT OF THE PLAYER IMAGE
        self.statusPButton1 = QPushButton(self.GUI, clicked = lambda: DescriptionCheck(self, "Self"))
        self.statusPButton1.setGeometry(146,20,60,35)
        self.statusPButton1.setText("Description")
        self.statusPButton1.setFont(QFont('Segoe UI', 9))
        self.statusPButton1.show()

        self.statusPButton2 = QPushButton(self.GUI)
        self.statusPButton2.setGeometry(146,60,60,35)
        self.statusPButton2.setText("Combat")
        self.statusPButton2.setFont(QFont('Segoe UI', 9))
        self.statusPButton2.show()

        self.statusPButton3 = QPushButton(self.GUI)
        self.statusPButton3.setGeometry(146,100,60,35)
        self.statusPButton3.setText("Portrait")
        self.statusPButton3.setFont(QFont('Segoe UI', 9))
        self.statusPButton3.clicked.connect(self.statusPButtonAction3)
        self.statusPButton3.show()


        #### ENERGY STATUS
        self.labelPEnergy = QLabel(self.GUI)
        self.labelPEnergy.setGeometry(20,143,206,50)
        self.labelPEnergy.setText("Energy: 1270")
        self.labelPEnergy.setFont(QFont('Segoe UI', 9))
        self.labelPEnergy.setAlignment(Qt.AlignHCenter)

        #### ENERGY INDICATORS
        self.labelPEnergy1 = QLabel(self.GUI)
        self.labelPEnergy1.setGeometry(22,168,20,25)
        self.labelPEnergy1.setStyleSheet('''QLabel{background-color:rgb(222, 222, 110) }''')
        self.labelPEnergy2 = QLabel(self.GUI)
        self.labelPEnergy2.setGeometry(42,168,20,25)
        self.labelPEnergy2.setStyleSheet('''QLabel{background-color:rgb(222, 222, 110) }''')
        self.labelPEnergy3 = QLabel(self.GUI)
        self.labelPEnergy3.setGeometry(62,168,20,25)
        self.labelPEnergy3.setStyleSheet('''QLabel{background-color:rgb(222, 222, 110) }''')
        self.labelPEnergy4 = QLabel(self.GUI)
        self.labelPEnergy4.setGeometry(82,168,20,25)
        self.labelPEnergy4.setStyleSheet('''QLabel{background-color:rgb(222, 222, 110) }''')
        self.labelPEnergy5 = QLabel(self.GUI)
        self.labelPEnergy5.setGeometry(102,168,20,25)
        self.labelPEnergy5.setStyleSheet('''QLabel{background-color:rgb(222, 222, 110) }''')
        self.labelPEnergy6 = QLabel(self.GUI)
        self.labelPEnergy6.setGeometry(122,168,20,25)
        self.labelPEnergy6.setStyleSheet('''QLabel{background-color:rgb(222, 222, 110) }''')
        self.labelPEnergy7 = QLabel(self.GUI)
        self.labelPEnergy7.setGeometry(142,168,20,25)
        self.labelPEnergy7.setStyleSheet('''QLabel{background-color:rgb(222, 222, 110) }''')
        self.labelPEnergy8 = QLabel(self.GUI)
        self.labelPEnergy8.setGeometry(162,168,20,25)
        self.labelPEnergy8.setStyleSheet('''QLabel{background-color:rgb(222, 222, 110) }''')
        self.labelPEnergy9 = QLabel(self.GUI)
        self.labelPEnergy9.setGeometry(182,168,20,25)
        self.labelPEnergy9.setStyleSheet('''QLabel{background-color:rgb(222, 222, 110) }''')
        self.labelPEnergy10 = QLabel(self.GUI)
        self.labelPEnergy10.setGeometry(202,168,20,25)
        self.labelPEnergy10.setStyleSheet('''QLabel{background-color:rgb(222, 222, 110 }''')





        #### STAMINA STATUS
        self.labelPStamina = QLabel(self.GUI)
        self.labelPStamina.setGeometry(20,208,186,50)
        self.labelPStamina.setText("Stamina: 760")
        self.labelPStamina.setFont(QFont('Segoe UI', 9))
        self.labelPStamina.setAlignment(Qt.AlignHCenter)

        #### STAMINA INDICATORS
        self.labelPStamina1 = QLabel(self.GUI)
        self.labelPStamina1.setGeometry(22,233,18,25)
        self.labelPStamina1.setStyleSheet('''QLabel{background-color:rgb(0, 170, 0) }''')
        self.labelPStamina2 = QLabel(self.GUI)
        self.labelPStamina2.setGeometry(40,233,18,25)
        self.labelPStamina2.setStyleSheet('''QLabel{background-color:rgb(0, 170, 0) }''')
        self.labelPStamina3 = QLabel(self.GUI)
        self.labelPStamina3.setGeometry(58,233,18,25)
        self.labelPStamina3.setStyleSheet('''QLabel{background-color:rgb(0, 170, 0) }''')
        self.labelPStamina4 = QLabel(self.GUI)
        self.labelPStamina4.setGeometry(76,233,18,25)
        self.labelPStamina4.setStyleSheet('''QLabel{background-color:rgb(0, 170, 0) }''')
        self.labelPStamina5 = QLabel(self.GUI)
        self.labelPStamina5.setGeometry(94,233,18,25)
        self.labelPStamina5.setStyleSheet('''QLabel{background-color:rgb(0, 170, 0) }''')
        self.labelPStamina6 = QLabel(self.GUI)
        self.labelPStamina6.setGeometry(112,233,18,25)
        self.labelPStamina6.setStyleSheet('''QLabel{background-color:rgb(0, 170, 0) }''')
        self.labelPStamina7 = QLabel(self.GUI)
        self.labelPStamina7.setGeometry(130,233,18,25)
        self.labelPStamina7.setStyleSheet('''QLabel{background-color:rgb(0, 170, 0) }''')
        self.labelPStamina8 = QLabel(self.GUI)
        self.labelPStamina8.setGeometry(148,233,18,25)
        self.labelPStamina8.setStyleSheet('''QLabel{background-color:rgb(0, 170, 0) }''')
        self.labelPStamina9 = QLabel(self.GUI)
        self.labelPStamina9.setGeometry(166,233,18,25)
        self.labelPStamina9.setStyleSheet('''QLabel{background-color:rgb(0, 170, 0) }''')
        self.labelPStamina10 = QLabel(self.GUI)
        self.labelPStamina10.setGeometry(184,233,18,25)
        self.labelPStamina10.setStyleSheet('''QLabel{background-color:rgb(0, 170, 0) }''')




        #### VITALITY STATUS
        self.labelPVitality = QLabel(self.GUI)
        self.labelPVitality.setGeometry(20,263,186,50)
        self.labelPVitality.setText("Vitality: 1500")
        self.labelPVitality.setFont(QFont('Segoe UI', 9))
        self.labelPVitality.setAlignment(Qt.AlignHCenter)

        #### VITALITY INDICATORS
        self.labelPVitality1 = QLabel(self.GUI)
        self.labelPVitality1.setGeometry(22,288,18,25)
        self.labelPVitality1.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')
        self.labelPVitality2 = QLabel(self.GUI)
        self.labelPVitality2.setGeometry(40,288,18,25)
        self.labelPVitality2.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')
        self.labelPVitality3 = QLabel(self.GUI)
        self.labelPVitality3.setGeometry(58,288,18,25)
        self.labelPVitality3.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')
        self.labelPVitality4 = QLabel(self.GUI)
        self.labelPVitality4.setGeometry(76,288,18,25)
        self.labelPVitality4.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')
        self.labelPVitality5 = QLabel(self.GUI)
        self.labelPVitality5.setGeometry(94,288,18,25)
        self.labelPVitality5.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')
        self.labelPVitality6 = QLabel(self.GUI)
        self.labelPVitality6.setGeometry(112,288,18,25)
        self.labelPVitality6.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')
        self.labelPVitality7 = QLabel(self.GUI)
        self.labelPVitality7.setGeometry(130,288,18,25)
        self.labelPVitality7.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')
        self.labelPVitality8 = QLabel(self.GUI)
        self.labelPVitality8.setGeometry(148,288,18,25)
        self.labelPVitality8.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')
        self.labelPVitality9 = QLabel(self.GUI)
        self.labelPVitality9.setGeometry(166,288,18,25)
        self.labelPVitality9.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')
        self.labelPVitality10 = QLabel(self.GUI)
        self.labelPVitality10.setGeometry(184,288,18,25)
        self.labelPVitality10.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')





        #### MANA STATUS
        self.labelPMana = QLabel(self.GUI)
        self.labelPMana.setGeometry(20,318,186,50)
        self.labelPMana.setText("Mana: 360")
        self.labelPMana.setFont(QFont('Segoe UI', 9))
        self.labelPMana.setAlignment(Qt.AlignHCenter)

        #### MANA INDICATORS
        self.labelPMana1 = QLabel(self.GUI)
        self.labelPMana1.setGeometry(22,343,18,25)
        self.labelPMana1.setStyleSheet('''QLabel{background-color:rgb(0, 100, 255) }''')
        self.labelPMana2 = QLabel(self.GUI)
        self.labelPMana2.setGeometry(40,343,18,25)
        self.labelPMana2.setStyleSheet('''QLabel{background-color:rgb(0, 100, 255) }''')
        self.labelPMana3 = QLabel(self.GUI)
        self.labelPMana3.setGeometry(58,343,18,25)
        self.labelPMana3.setStyleSheet('''QLabel{background-color:rgb(0, 100, 255) }''')
        self.labelPMana4 = QLabel(self.GUI)
        self.labelPMana4.setGeometry(76,343,18,25)
        self.labelPMana4.setStyleSheet('''QLabel{background-color:rgb(0, 100, 255) }''')
        self.labelPMana5 = QLabel(self.GUI)
        self.labelPMana5.setGeometry(94,343,18,25)
        self.labelPMana5.setStyleSheet('''QLabel{background-color:rgb(0, 100, 255) }''')
        self.labelPMana6 = QLabel(self.GUI)
        self.labelPMana6.setGeometry(112,343,18,25)
        self.labelPMana6.setStyleSheet('''QLabel{background-color:rgb(0, 100, 255) }''')
        self.labelPMana7 = QLabel(self.GUI)
        self.labelPMana7.setGeometry(130,343,18,25)
        self.labelPMana7.setStyleSheet('''QLabel{background-color:rgb(0, 100, 255) }''')
        self.labelPMana8 = QLabel(self.GUI)
        self.labelPMana8.setGeometry(148,343,18,25)
        self.labelPMana8.setStyleSheet('''QLabel{background-color:rgb(0, 100, 255) }''')
        self.labelPMana9 = QLabel(self.GUI)
        self.labelPMana9.setGeometry(166,343,18,25)
        self.labelPMana9.setStyleSheet('''QLabel{background-color:rgb(0, 100, 255) }''')
        self.labelPMana10 = QLabel(self.GUI)
        self.labelPMana10.setGeometry(184,343,18,25)
        self.labelPMana10.setStyleSheet('''QLabel{background-color:rgb(0, 100, 255) }''')





        #### LABEL FOR THE MAP
        self.labelMap = QLabel(self.GUI)
        self.labelMap.setGeometry(20,380,186,186)
        self.labelMap.setAlignment(Qt.AlignCenter)
        self.labelMap.setPixmap(QPixmap("C:/Users/PC/Downloads/Map.png"))
        self.labelMap.setScaledContents(True)




        #### INTERACT BUTTONS AT THE TOP 3 ROWS OF THE BOTTOM LABEL
        self.mainButton1 = QPushButton('-10 hour', self.GUI)
        self.mainButton1.setGeometry(12, 592, 152, 30)
        self.mainButton1.setFont(QFont('Segoe UI', 11))
        self.mainButton1.clicked.connect(self.mainButtonAction1)

        self.mainButton2 = QPushButton('-10 hour', self.GUI)
        self.mainButton2.setGeometry(170, 592, 152, 30)
        self.mainButton2.setFont(QFont('Segoe UI', 11))
        self.mainButton2.clicked.connect(self.mainButtonAction2)

        self.mainButton3 = QPushButton('-10 hour', self.GUI)
        self.mainButton3.setGeometry(328, 592, 152, 30)
        self.mainButton3.setFont(QFont('Segoe UI', 11))
        self.mainButton3.clicked.connect(self.mainButtonAction3)

        self.mainButton4 = QPushButton('-10 hour', self.GUI)
        self.mainButton4.setGeometry(486, 592, 152, 30)
        self.mainButton4.setFont(QFont('Segoe UI', 11))
        self.mainButton4.clicked.connect(self.mainButtonAction4)

        self.mainButton5 = QPushButton('-10 hour', self.GUI)
        self.mainButton5.setGeometry(644, 592, 152, 30)
        self.mainButton5.setFont(QFont('Segoe UI', 11))
        self.mainButton5.clicked.connect(self.mainButtonAction5)

        self.mainButton6 = QPushButton('-10 hour', self.GUI)
        self.mainButton6.setGeometry(802, 592, 152, 30)
        self.mainButton6.setFont(QFont('Segoe UI', 11))
        self.mainButton6.clicked.connect(self.mainButtonAction6)

        self.mainButton7 = QPushButton('-10 hour', self.GUI)
        self.mainButton7.setGeometry(960, 592, 152, 30)
        self.mainButton7.setFont(QFont('Segoe UI', 11))
        self.mainButton7.clicked.connect(self.mainButtonAction7)

        self.mainButton8 = QPushButton('-10 hour', self.GUI)
        self.mainButton8.setGeometry(1118, 592, 152, 30)
        self.mainButton8.setFont(QFont('Segoe UI', 11))
        self.mainButton8.clicked.connect(self.mainButtonAction8)

        self.mainButton9 = QPushButton('-10 hour', self.GUI)
        self.mainButton9.setGeometry(12, 628, 152, 30)
        self.mainButton9.setFont(QFont('Segoe UI', 11))
        self.mainButton9.clicked.connect(self.mainButtonAction9)

        self.mainButton10 = QPushButton('-10 hour', self.GUI)
        self.mainButton10.setGeometry(170, 628, 152, 30)
        self.mainButton10.setFont(QFont('Segoe UI', 11))
        self.mainButton10.clicked.connect(self.mainButtonAction10)

        self.mainButton11 = QPushButton('-10 hour', self.GUI)
        self.mainButton11.setGeometry(328, 628, 152, 30)
        self.mainButton11.setFont(QFont('Segoe UI', 11))
        self.mainButton11.clicked.connect(self.mainButtonAction11)

        self.mainButton12 = QPushButton('-10 hour', self.GUI)
        self.mainButton12.setGeometry(486, 628, 152, 30)
        self.mainButton12.setFont(QFont('Segoe UI', 11))
        self.mainButton12.clicked.connect(self.mainButtonAction12)

        self.mainButton13 = QPushButton('-10 hour', self.GUI)
        self.mainButton13.setGeometry(644, 628, 152, 30)
        self.mainButton13.setFont(QFont('Segoe UI', 11))
        self.mainButton13.clicked.connect(self.mainButtonAction13)

        self.mainButton14 = QPushButton('-10 hour', self.GUI)
        self.mainButton14.setGeometry(802, 628, 152, 30)
        self.mainButton14.setFont(QFont('Segoe UI', 11))
        self.mainButton14.clicked.connect(self.mainButtonAction14)

        self.mainButton15 = QPushButton('-10 hour', self.GUI)
        self.mainButton15.setGeometry(960, 628, 152, 30)
        self.mainButton15.setFont(QFont('Segoe UI', 11))
        self.mainButton15.clicked.connect(self.mainButtonAction15)

        self.mainButton16 = QPushButton('-10 hour', self.GUI)
        self.mainButton16.setGeometry(1118, 628, 152, 30)
        self.mainButton16.setFont(QFont('Segoe UI', 11))
        self.mainButton16.clicked.connect(self.mainButtonAction16)

        self.mainButton17 = QPushButton('-10 hour', self.GUI)
        self.mainButton17.setGeometry(12, 664, 152, 30)
        self.mainButton17.setFont(QFont('Segoe UI', 11))
        self.mainButton17.clicked.connect(self.mainButtonAction17)

        self.mainButton18 = QPushButton('-10 hour', self.GUI)
        self.mainButton18.setGeometry(170, 664, 152, 30)
        self.mainButton18.setFont(QFont('Segoe UI', 11))
        self.mainButton18.clicked.connect(self.mainButtonAction18)

        self.mainButton19 = QPushButton('-10 hour', self.GUI)
        self.mainButton19.setGeometry(328, 664, 152, 30)
        self.mainButton19.setFont(QFont('Segoe UI', 11))
        self.mainButton19.clicked.connect(self.mainButtonAction19)

        self.mainButton20 = QPushButton('-10 hour', self.GUI)
        self.mainButton20.setGeometry(486, 664, 152, 30)
        self.mainButton20.setFont(QFont('Segoe UI', 11))
        self.mainButton20.clicked.connect(self.mainButtonAction20)

        self.mainButton21 = QPushButton('-10 hour', self.GUI)
        self.mainButton21.setGeometry(644, 664, 152, 30)
        self.mainButton21.setFont(QFont('Segoe UI', 11))
        self.mainButton21.clicked.connect(self.mainButtonAction21)

        self.mainButton22 = QPushButton('-10 hour', self.GUI)
        self.mainButton22.setGeometry(802, 664, 152, 30)
        self.mainButton22.setFont(QFont('Segoe UI', 11))
        self.mainButton22.clicked.connect(self.mainButtonAction22)

        self.mainButton23 = QPushButton('-10 hour', self.GUI)
        self.mainButton23.setGeometry(960, 664, 152, 30)
        self.mainButton23.setFont(QFont('Segoe UI', 11))
        self.mainButton23.clicked.connect(self.mainButtonAction23)

        self.mainButton24 = QPushButton('-asdur', self.GUI)
        self.mainButton24.setGeometry(1118, 664, 152, 30)
        self.mainButton24.setFont(QFont('Segoe UI', 11))
        self.mainButton24.clicked.connect(self.mainButtonAction24)
        self.mainButton24.hide()

        self.mainButtonLeft = QPushButton('<--', self.GUI)
        self.mainButtonLeft.setGeometry(1118, 664, 73, 30)
        self.mainButtonLeft.setFont(QFont('Segoe UI', 11))
        self.mainButtonLeft.clicked.connect(self.mainButtonActionLeft)

        self.mainButtonRight = QPushButton('-->', self.GUI)
        self.mainButtonRight.setGeometry(1197, 664, 73, 30)
        self.mainButtonRight.setFont(QFont('Segoe UI', 11))
        self.mainButtonRight.clicked.connect(self.mainButtonActionRight)

        #### OTHER BUTTONS ON THE LAST TWO ROWS OF THE BOTTOM LABEL

        self.mainButton25 = QPushButton('-10 hour', self.GUI)
        self.mainButton25.setGeometry(12, 704, 152, 30)
        self.mainButton25.setFont(QFont('Segoe UI', 11))
        self.mainButton25.clicked.connect(self.mainButtonAction25)

        self.mainButton26 = QPushButton('-10 hour', self.GUI)
        self.mainButton26.setGeometry(170, 704, 152, 30)
        self.mainButton26.setFont(QFont('Segoe UI', 11))
        self.mainButton26.clicked.connect(self.mainButtonAction26)

        self.mainButton27 = QPushButton('-10 hour', self.GUI)
        self.mainButton27.setGeometry(328, 704, 152, 30)
        self.mainButton27.setFont(QFont('Segoe UI', 11))
        self.mainButton27.clicked.connect(self.mainButtonAction27)

        self.mainButton28 = QPushButton('-10 hour', self.GUI)
        self.mainButton28.setGeometry(486, 704, 152, 30)
        self.mainButton28.setFont(QFont('Segoe UI', 11))
        self.mainButton28.clicked.connect(self.mainButtonAction28)

        self.mainButton29 = QPushButton('-10 hour', self.GUI)
        self.mainButton29.setGeometry(644, 704, 152, 30)
        self.mainButton29.setFont(QFont('Segoe UI', 11))
        self.mainButton29.clicked.connect(self.mainButtonAction29)

        self.mainButton30 = QPushButton('-10 hour', self.GUI)
        self.mainButton30.setGeometry(802, 704, 152, 30)
        self.mainButton30.setFont(QFont('Segoe UI', 11))
        self.mainButton30.clicked.connect(self.mainButtonAction30)

        self.mainButton31 = QPushButton('-10 hour', self.GUI)
        self.mainButton31.setGeometry(960, 704, 152, 30)
        self.mainButton31.setFont(QFont('Segoe UI', 11))
        self.mainButton31.clicked.connect(self.mainButtonAction31)

        self.mainButton32 = QPushButton('-10 hour', self.GUI)
        self.mainButton32.setGeometry(1118, 704, 152, 30)
        self.mainButton32.setFont(QFont('Segoe UI', 11))
        self.mainButton32.clicked.connect(self.mainButtonAction32)

        self.mainButton33 = QPushButton('-10 hour', self.GUI)
        self.mainButton33.setGeometry(12, 740, 152, 30)
        self.mainButton33.setFont(QFont('Segoe UI', 11))
        self.mainButton33.clicked.connect(self.mainButtonAction33)

        self.mainButton34 = QPushButton('-10 hour', self.GUI)
        self.mainButton34.setGeometry(170, 740, 152, 30)
        self.mainButton34.setFont(QFont('Segoe UI', 11))
        self.mainButton34.clicked.connect(self.mainButtonAction34)

        self.mainButton35 = QPushButton('-10 hour', self.GUI)
        self.mainButton35.setGeometry(328, 740, 152, 30)
        self.mainButton35.setFont(QFont('Segoe UI', 11))
        self.mainButton35.clicked.connect(self.mainButtonAction35)

        self.mainButton36 = QPushButton('-10 hour', self.GUI)
        self.mainButton36.setGeometry(486, 740, 152, 30)
        self.mainButton36.setFont(QFont('Segoe UI', 11))
        self.mainButton36.clicked.connect(self.mainButtonAction36)

        self.mainButton37 = QPushButton('-10 hour', self.GUI)
        self.mainButton37.setGeometry(644, 740, 152, 30)
        self.mainButton37.setFont(QFont('Segoe UI', 11))
        self.mainButton37.clicked.connect(self.mainButtonAction37)

        self.mainButton38 = QPushButton('-10 hour', self.GUI)
        self.mainButton38.setGeometry(802, 740, 152, 30)
        self.mainButton38.setFont(QFont('Segoe UI', 11))
        self.mainButton38.clicked.connect(self.mainButtonAction38)

        # self.mainButton39 = QPushButton('-10 hour', self.GUI)
        # self.mainButton39.setGeometry(960, 740, 152, 30)
        # self.mainButton39.setFont(QFont('Segoe UI', 11))
        # self.mainButton39.clicked.connect(self.mainButtonAction39)
        #
        # self.mainButton40 = QPushButton('-10 hour', self.GUI)
        # self.mainButton40.setGeometry(1118, 740, 152, 30)
        # self.mainButton40.setFont(QFont('Segoe UI', 11))
        # self.mainButton40.clicked.connect(self.mainButtonAction40)
        resetTarget()
        resetSelf()
        updateGlobal(self)
        # interactCommands(self)
        updateImage(self,"Target")
        updateImage(self,"Self")
        Initialize(self)

        self.nextButton = QPushButton('Next', self.GUI)
        self.nextButton.setGeometry(1200, 700, 80, 80)
        self.nextButton.hide()

        self.InteractButton = QPushButton('Interact Button', self.GUI)
        self.InteractButton.setGeometry(1076, 259, 200,25)
        self.InteractButton.setFont(QFont('Arial', 9))
        self.InteractButton.hide()

        self.AbilitiesButton = QPushButton('Abilities', self.GUI)
        self.AbilitiesButton.setGeometry(960, 740, 152, 30)
        self.AbilitiesButton.setFont(QFont('Segoe UI', 11))
        self.AbilitiesButton.hide()

        self.MenuButton = QPushButton('Menu', self.GUI)
        self.MenuButton.setGeometry(1118, 740, 152, 30)
        self.MenuButton.setFont(QFont('Segoe UI', 11))


        # self.ReduceButton = QPushButton(self.GUI, clicked = lambda: self.ReduceFunc())
        # self.ReduceButton.setGeometry(1406,20,60,35)
        # self.ReduceButton.setText("Reduce")
        # self.ReduceButton.setFont(QFont('Segoe UI', 9))
        # self.ReduceButton.show()
        #
        #
        # self.IncreaseButton = QPushButton(self.GUI, clicked = lambda: self.IncreaseFunc())
        # self.IncreaseButton.setGeometry(1466,20,60,35)
        # self.IncreaseButton.setText("Increase")
        # self.IncreaseButton.setFont(QFont('Segoe UI', 9))
        # self.IncreaseButton.show()
        #
        # self.ToReduce = QLabel("Example Text", self.GUI)
        # self.ToReduce.setGeometry(1406,90,60,35)
        # self.ToReduce.setStyleSheet('''QWidget{background-color:red} ''')
        # # self.ToReduce.setFont(QFont('Segoe UI', 11))

        def hourMas(self):
            hourChange(self, 15)

        def hourMenos(self):
            hourChange(self, -15)

        def mainButtonAction1(self):
            commandActions(self,"button1")
        def mainButtonAction2(self):
            commandActions(self,"button2")
        def mainButtonAction3(self):
            commandActions(self,"button3")
        def mainButtonAction4(self):
            commandActions(self,"button4")
        def mainButtonAction5(self):
            commandActions(self,"button5")
        def mainButtonAction6(self):
            commandActions(self,"button6")
        def mainButtonAction7(self):
            commandActions(self,"button7")
        def mainButtonAction8(self):
            commandActions(self,"button8")
        def mainButtonAction9(self):
            commandActions(self,"button9")
        def mainButtonAction10(self):
            commandActions(self,"button10")
        def mainButtonAction11(self):
            commandActions(self,"button11")
        def mainButtonAction12(self):
            commandActions(self,"button12")
        def mainButtonAction13(self):
            commandActions(self,"button13")
        def mainButtonAction14(self):
            commandActions(self,"button14")
        def mainButtonAction15(self):
            commandActions(self,"button15")
        def mainButtonAction16(self):
            commandActions(self,"button16")
        def mainButtonAction17(self):
            commandActions(self,"button17")
        def mainButtonAction18(self):
            commandActions(self,"button18")
        def mainButtonAction19(self):
            commandActions(self,"button19")
        def mainButtonAction20(self):
            commandActions(self,"button20")
        def mainButtonAction21(self):
            commandActions(self,"button21")
        def mainButtonAction22(self):
            commandActions(self,"button22")
        def mainButtonAction23(self):
            commandActions(self,"button23")
        def mainButtonAction24(self):
            commandActions(self,"button24")
        def mainButtonAction25(self):
            commandActions(self,"button25")
        def mainButtonAction26(self):
            commandActions(self,"button26")
        def mainButtonAction27(self):
            commandActions(self,"button27")
        def mainButtonAction28(self):
            commandActions(self,"button28")
        def mainButtonAction29(self):
            commandActions(self,"button29")
        def mainButtonAction30(self):
            commandActions(self,"button30")
        def mainButtonAction31(self):
            commandActions(self,"button31")
        def mainButtonAction32(self):
            commandActions(self,"button32")
        def mainButtonAction33(self):
            commandActions(self,"button33")
        def mainButtonAction34(self):
            commandActions(self,"button34")
        def mainButtonAction35(self):
            commandActions(self,"button35")
        def mainButtonAction36(self):
            commandActions(self,"button36")
        def mainButtonAction37(self):
            commandActions(self,"button37")
        def mainButtonAction38(self):
            commandActions(self,"button38")
        def mainButtonAction39(self):
            commandActions(self,"button39")
        def mainButtonAction40(self):
            commandActions(self,"button40")
        def mainButtonAction41(self):
            commandActions(self,"button41")
        def mainButtonAction42(self):
            commandActions(self,"button42")
        def mainButtonAction43(self):
            commandActions(self,"button43")
        def mainButtonAction44(self):
            commandActions(self,"button44")
        def mainButtonAction45(self):
            commandActions(self,"button45")
        def mainButtonAction46(self):
            commandActions(self,"button46")
        def mainButtonAction47(self):
            commandActions(self,"button47")
        def mainButtonAction48(self):
            commandActions(self,"button48")
        def mainButtonAction49(self):
            commandActions(self,"button49")
        def mainButtonAction50(self):
            commandActions(self,"button50")
        def mainButtonAction51(self):
            commandActions(self,"button51")
        def mainButtonAction52(self):
            commandActions(self,"button52")
        def mainButtonAction53(self):
            commandActions(self,"button53")
        def mainButtonAction54(self):
            commandActions(self,"button54")
        def mainButtonAction55(self):
            commandActions(self,"button55")
        def mainButtonAction56(self):
            commandActions(self,"button56")
        def mainButtonAction57(self):
            commandActions(self,"button57")
        def mainButtonAction58(self):
            commandActions(self,"button58")
        def mainButtonAction59(self):
            # import InteractUI
            # InteractUI.MainWindow.gotoBattlesWindow()
            commandActions(self,"button59")
        def mainButtonAction60(self):
            commandActions(self,"button60")
        def mainButtonActionLeft(self):
            commandActions(self,"buttonLeft")
        def mainButtonActionRight(self):
            commandActions(self,"buttonRight")

        def NPCButton1(self):
            switchTarget(self, "NPCbutton1")
        def NPCButton2(self):
            switchTarget(self, "NPCbutton2")
        def NPCButton3(self):
            switchTarget(self, "NPCbutton3")
        def NPCButton4(self):
            switchTarget(self, "NPCbutton4")
        def NPCButton5(self):
            switchTarget(self, "NPCbutton5")

        def NPCButtonLeft(self):
            switchNPCpage(self, "Left")
        def NPCButtonRight(self):
            switchNPCpage(self, "Right")

        def statusTButtonAction3(self):
            switchTypeOfImage(self, "Target")
        def statusTButtonAction2(self):
            switchSelf(self)

        def statusPButtonAction3(self):
            switchTypeOfImage(self, "Self")


class UiLayoutBattleWindow(QWidget):
    def Ui(self, MainWindow):

        self.GUI = QWidget(MainWindow)
        self.backButton = QPushButton("Back", self.GUI)
        MainWindow.setCentralWidget(self.GUI)

def Initialize(self, Reference):
    if "SoLUI" not in Globals.Layouts:
        Object = UiLayoutSoLMenu()
