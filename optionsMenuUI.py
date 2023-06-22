import json

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import *

import Globals


class UiLayoutOptionsMenuOld:
    def Ui(self, MainWindow):
        self.optionsMenuUI = QWidget(MainWindow)
        # mainwindow.setWindowIcon(QtGui.QIcon('PhotoIcon.png'))
        self.optionsMenuUI.setStyleSheet('''
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
        QPushButton{
        	color:rgb(255, 255, 255)
        }
        QPushButton:hover{
        	color:rgb(255, 255, 0)
        }
        QLabel{
         border: 1px solid black;
         background : rgb(35, 35, 35);
         color:rgb(255, 255, 255)
        }
        QLineEdit{
		border: 1px solid black;
        color:rgb(255, 255, 255)
        }
        QGroupBox:title{
        color:rgb(255, 255, 255);
        subcontrol-position: top center;
        }
        QGroupBox{
        border: 1px solid black;
        background-color:rgb(35, 35, 35);
        }
        QScrollArea{
        border: 1px solid black;
        background-color:rgb(35, 35, 35);
        }
         ''')
        MainWindow.setCentralWidget(self.optionsMenuUI)
        MainWindow.setFixedSize(1280, 800)


        self.labelBack = QLabel(self.optionsMenuUI)
        self.labelBack.setGeometry(230,10,820,780)
        self.labelBack.setStyleSheet('''
                QLabel{
         border: 1px solid black;
         background : rgb(23, 23, 23);
         color:rgb(255, 255, 255);
        }
        ''')
        self.labelBack.setFont(QFont('Segoe UI', 14))

        self.buttonBack = QPushButton("Back To Menu", self.optionsMenuUI)
        self.buttonBack.setFont(QFont('Segoe UI', 14))
        self.buttonBack.setGeometry(20,670,160,35)

        self.buttonSave = QPushButton("Save", self.optionsMenuUI)
        self.buttonSave.setFont(QFont('Segoe UI', 14))
        self.buttonSave.setGeometry(1100,670,160,35)
        self.buttonSave.clicked.connect(self.saveCheck)

        ############

        self.scroll = QScrollArea(self.optionsMenuUI)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setGeometry(230,10,820,780)
        self.scroll.setStyleSheet('''
        QScrollArea{
        background-color:rgb(23, 23, 23);
        }
        ''')


        # object = QLabel()
        # object.setText('''Credits ''')
        # object.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        # object.setFont(QFont('Segoe UI', 14))
        # object.setStyleSheet('''
        #         QLabel{
        #  border: 1px solid black;
        #  background : rgb(23, 23, 23);
        #  color:rgb(255, 255, 255);
        # }
        # ''')


        myform = QVBoxLayout()

        #### NPC OPTIONS
        self.InteractWidget = QWidget()
        self.InteractWidget.setFixedSize(800,250)
        self.InteractWidget.setStyleSheet('''
        QWidget{
    	background-color:rgb(23, 23, 23);
        }
        QPushButton{
        background-color:rgb(35, 35, 35)
        }
        ''')

        self.labelNPCinteractions = QLabel("NPC Interactions", self.InteractWidget)
        self.labelNPCinteractions.setFont(QFont('Segoe UI', 16))
        self.labelNPCinteractions.setGeometry(10,10,780,40)
        self.labelNPCinteractions.setAlignment(Qt.AlignVCenter)
        self.labelNPCinteractions.setAlignment(Qt.AlignHCenter)
        self.labelNPCinteractions.setStyleSheet('''
        QLabel{
        border: 1px solid black;
        background : rgb(35, 35, 35);
        color:rgb(255, 255, 255)
        }
        ''')
        self.labelNPCinteract = QLabel("NPC Can Interact With One Another", self.InteractWidget)
        self.labelNPCinteract.setFont(QFont('Segoe UI', 14))
        self.labelNPCinteract.setGeometry(20,60,390,40)
        self.labelNPCinteract.setAlignment(Qt.AlignVCenter)
        self.labelNPCinteract.setAlignment(Qt.AlignHCenter)
        self.buttonNPCinteractCan = QPushButton("Can", self.InteractWidget)
        self.buttonNPCinteractCan.setFont(QFont('Segoe UI', 14))
        self.buttonNPCinteractCan.setGeometry(100,100,90,35)
        self.buttonNPCinteractCan.setCheckable(True)
        self.buttonNPCinteractCan.clicked.connect(self.buttonNPCinteractCanAction)
        self.buttonNPCinteractCant = QPushButton("Can't", self.InteractWidget)
        self.buttonNPCinteractCant.setFont(QFont('Segoe UI', 14))
        self.buttonNPCinteractCant.setGeometry(210,100,90,35)
        self.buttonNPCinteractCant.setCheckable(True)
        self.buttonNPCinteractCant.clicked.connect(self.buttonNPCinteractCantAction)

        self.labelNPCrelations = QLabel("NPC Can Form Relationships", self.InteractWidget)
        self.labelNPCrelations.setFont(QFont('Segoe UI', 14))
        self.labelNPCrelations.setGeometry(420,60,390,40)
        self.labelNPCrelations.setAlignment(Qt.AlignVCenter)
        self.labelNPCrelations.setAlignment(Qt.AlignHCenter)
        self.buttonNPCrelationsCan = QPushButton("Can", self.InteractWidget)
        self.buttonNPCrelationsCan.setFont(QFont('Segoe UI', 14))
        self.buttonNPCrelationsCan.setGeometry(500,100,90,35)
        self.buttonNPCrelationsCan.setCheckable(True)
        self.buttonNPCrelationsCan.clicked.connect(self.buttonNPCrelationsCanAction)
        self.buttonNPCrelationsCant = QPushButton("Can't", self.InteractWidget)
        self.buttonNPCrelationsCant.setFont(QFont('Segoe UI', 14))
        self.buttonNPCrelationsCant.setGeometry(610,100,90,35)
        self.buttonNPCrelationsCant.setCheckable(True)
        self.buttonNPCrelationsCant.clicked.connect(self.buttonNPCrelationsCantAction)

        self.labelNPCviolence = QLabel("Violent interactions between NPC", self.InteractWidget)
        self.labelNPCviolence.setFont(QFont('Segoe UI', 14))
        self.labelNPCviolence.setGeometry(20,150,390,40)
        self.labelNPCviolence.setAlignment(Qt.AlignVCenter)
        self.labelNPCviolence.setAlignment(Qt.AlignHCenter)
        self.buttonNPCviolenceCan = QPushButton("Can", self.InteractWidget)
        self.buttonNPCviolenceCan.setFont(QFont('Segoe UI', 14))
        self.buttonNPCviolenceCan.setGeometry(100,190,90,35)
        self.buttonNPCviolenceCan.setCheckable(True)
        self.buttonNPCviolenceCan.clicked.connect(self.buttonNPCviolenceCanAction)
        self.buttonNPCviolenceCant = QPushButton("Can't", self.InteractWidget)
        self.buttonNPCviolenceCant.setFont(QFont('Segoe UI', 14))
        self.buttonNPCviolenceCant.setGeometry(210,190,90,35)
        self.buttonNPCviolenceCant.setCheckable(True)
        self.buttonNPCviolenceCant.clicked.connect(self.buttonNPCviolenceCantAction)

        self.labelNPCerotic = QLabel("Erotic interactions between NPC", self.InteractWidget)
        self.labelNPCerotic.setFont(QFont('Segoe UI', 14))
        self.labelNPCerotic.setGeometry(420,150,390,40)
        self.labelNPCerotic.setAlignment(Qt.AlignVCenter)
        self.labelNPCerotic.setAlignment(Qt.AlignHCenter)
        self.buttonNPCeroticCan = QPushButton("Can", self.InteractWidget)
        self.buttonNPCeroticCan.setFont(QFont('Segoe UI', 14))
        self.buttonNPCeroticCan.setGeometry(500,190,90,35)
        self.buttonNPCeroticCan.setCheckable(True)
        self.buttonNPCeroticCan.clicked.connect(self.buttonNPCeroticCanAction)
        self.buttonNPCeroticCant = QPushButton("Can't", self.InteractWidget)
        self.buttonNPCeroticCant.setFont(QFont('Segoe UI', 14))
        self.buttonNPCeroticCant.setGeometry(610,190,90,35)
        self.buttonNPCeroticCant.setCheckable(True)
        self.buttonNPCeroticCant.clicked.connect(self.buttonNPCeroticCantAction)

        myform.addWidget(self.InteractWidget)
        ####

        #### NPC OPTIONS
        self.FetishesWidget = QWidget()
        self.FetishesWidget.setFixedSize(800,170)
        self.FetishesWidget.setStyleSheet('''
        QWidget{
    	background-color:rgb(23, 23, 23);
        }
        QPushButton{
        background-color:rgb(35, 35, 35)
        }
        ''')
        self.labelFetishes = QLabel("Fetishes", self.FetishesWidget)
        self.labelFetishes.setFont(QFont('Segoe UI', 16))
        self.labelFetishes.setGeometry(10,10,780,40)
        self.labelFetishes.setAlignment(Qt.AlignVCenter)
        self.labelFetishes.setAlignment(Qt.AlignHCenter)
        self.labelFetishes.setStyleSheet('''
        QLabel{
        border: 1px solid black;
        background : rgb(35, 35, 35);
        color:rgb(255, 255, 255)
        }
        ''')

        self.labelFetishWatersports = QLabel("Watersports", self.FetishesWidget)
        self.labelFetishWatersports.setFont(QFont('Segoe UI', 14))
        self.labelFetishWatersports.setGeometry(10,60,280,40)
        self.labelFetishWatersports.setAlignment(Qt.AlignVCenter)
        self.labelFetishWatersports.setAlignment(Qt.AlignHCenter)
        self.buttonFetishWatersports = QPushButton("Enabled", self.FetishesWidget)
        self.buttonFetishWatersports.setFont(QFont('Segoe UI', 14))
        self.buttonFetishWatersports.setGeometry(300,60,90,40)
        self.buttonFetishWatersports.setCheckable(True)
        self.buttonFetishWatersports.clicked.connect(self.buttonFetishWatersportsAction)

        self.labelFetishPregnancy = QLabel("Pregnancy", self.FetishesWidget)
        self.labelFetishPregnancy.setFont(QFont('Segoe UI', 14))
        self.labelFetishPregnancy.setGeometry(410,60,280,40)
        self.labelFetishPregnancy.setAlignment(Qt.AlignVCenter)
        self.labelFetishPregnancy.setAlignment(Qt.AlignHCenter)
        self.buttonFetishPregnancy = QPushButton("Enabled", self.FetishesWidget)
        self.buttonFetishPregnancy.setFont(QFont('Segoe UI', 14))
        self.buttonFetishPregnancy.setGeometry(700,60,90,40)
        self.buttonFetishPregnancy.setCheckable(True)
        self.buttonFetishPregnancy.clicked.connect(self.buttonFetishPregnancyAction)

        self.labelFetishNetorare = QLabel("Netorare", self.FetishesWidget)
        self.labelFetishNetorare.setFont(QFont('Segoe UI', 14))
        self.labelFetishNetorare.setGeometry(10,110,280,40)
        self.labelFetishNetorare.setAlignment(Qt.AlignVCenter)
        self.labelFetishNetorare.setAlignment(Qt.AlignHCenter)
        self.buttonFetishNetorare = QPushButton("Enabled", self.FetishesWidget)
        self.buttonFetishNetorare.setFont(QFont('Segoe UI', 14))
        self.buttonFetishNetorare.setGeometry(300,110,90,40)
        self.buttonFetishNetorare.setCheckable(True)
        self.buttonFetishNetorare.clicked.connect(self.buttonFetishNetorareAction)

        self.labelFetishRyona = QLabel("Ryona", self.FetishesWidget)
        self.labelFetishRyona.setFont(QFont('Segoe UI', 14))
        self.labelFetishRyona.setGeometry(410,110,280,40)
        self.labelFetishRyona.setAlignment(Qt.AlignVCenter)
        self.labelFetishRyona.setAlignment(Qt.AlignHCenter)
        self.buttonFetishRyona = QPushButton("Enabled", self.FetishesWidget)
        self.buttonFetishRyona.setFont(QFont('Segoe UI', 14))
        self.buttonFetishRyona.setGeometry(700,110,90,40)
        self.buttonFetishRyona.setCheckable(True)
        self.buttonFetishRyona.clicked.connect(self.buttonFetishRyonaAction)

        myform.addWidget(self.FetishesWidget)
        ####



        # object = QWidget()
        # object.setFixedSize(500,500)
        # object.setStyleSheet('''background-color: rgb(255,0,0); margin:5px; border:1px solid rgb(0, 255, 0);''')
        # label = QLabel("Hey", object)
        # label.setGeometry(50,50,200,200)
        # myform.addWidget(object)
        #
        #
        # object = QWidget()
        # object.setFixedSize(500,500)
        # object.setStyleSheet('''background-color: rgb(0,255,0); margin:5px; border:1px solid rgb(0, 0, 255);''')
        # label = QLabel("Hey", object)
        # label.setGeometry(50,50,200,200)
        # myform.addWidget(object)
        #
        # object2 = QWidget()
        # object2.setFixedSize(500,500)
        # object2.setStyleSheet('''background-color: rgb(0,0,255); margin:5px; border:1px solid rgb(255, 0, 0);''')
        # label2 = QLabel("Hey", object2)
        # label2.setGeometry(50,50,200,200)
        # myform.addWidget(object2)


        mygroupbox = QGroupBox()
        # mygroupbox.setFont(QFont('Segoe UI', 14))
        mygroupbox.setLayout(myform)
        self.scroll.setWidget(mygroupbox)

        self.startCheck()

        ##################


    def checkPage(self):
        page = 1
        if page == 1:
            self.labelNPCinteractions.show()

            self.labelNPCinteract.show()
            self.buttonNPCinteractCan.show()
            self.buttonNPCinteractCant.show()

            self.labelNPCrelations.show()
            self.buttonNPCrelationsCan.show()
            self.buttonNPCrelationsCant.show()

            self.labelNPCviolence.show()
            self.buttonNPCviolenceCan.show()
            self.buttonNPCviolenceCant.show()

            self.labelNPCerotic.show()
            self.buttonNPCeroticCan.show()
            self.buttonNPCeroticCant.show()


            self.labelFetishes.show()

            self.labelFetishWatersports.show()
            self.buttonFetishWatersports.show()

            self.labelFetishPregnancy.show()
            buttonFetishPregnancy.show()

            self.labelFetishNetorare.show()
            self.buttonFetishNetorare.show()

            self.labelFetishRyona.show()
            self.buttonFetishRyona.show()
        else:
            self.labelNPCinteractions.hide()

            self.labelNPCinteract.hide()
            self.buttonNPCinteractCan.hide()
            self.buttonNPCinteractCant.hide()

            self.labelNPCrelations.hide()
            self.buttonNPCrelationsCan.hide()
            self.buttonNPCrelationsCant.hide()

            self.labelNPCviolence.hide()
            self.buttonNPCviolenceCan.hide()
            self.buttonNPCviolenceCant.hide()

            self.labelNPCerotic.hide()
            self.buttonNPCeroticCan.hide()
            self.buttonNPCeroticCant.hide()


            self.labelFetishes.hide()

            self.labelFetishWatersports.hide()
            self.buttonFetishWatersports.hide()

            self.labelFetishPregnancy.hide()
            buttonFetishPregnancy.hide()

            self.labelFetishNetorare.hide()
            self.buttonFetishNetorare.hide()

            self.labelFetishRyona.hide()
            self.buttonFetishRyona.hide()

    def previousPage(self):
        page = self.labelPage.text()
        length = len(page)
        page = page[6:length]
        page = int(page) - 1
        self.labelPage.setText("Page: "+str(page))

    def nextPage(self):
        page = self.labelPage.text()
        length = len(page)
        page = page[6:length]
        page = int(page) + 1
        self.labelPage.setText("Page: "+str(page))

    def startCheck(self):
        with pathlib.Path.open('playerConfig.json', 'rb') as f:
            configurations = json.load(f)
        if configurations["Interact"]: self.buttonNPCinteractCan.setChecked(1); self.buttonNPCinteractCant.setChecked(0)
        else: self.buttonNPCinteractCan.setChecked(0); self.buttonNPCinteractCant.setChecked(1)
        if configurations["Relations"]: self.buttonNPCrelationsCan.setChecked(1); self.buttonNPCrelationsCant.setChecked(0)
        else: self.buttonNPCrelationsCan.setChecked(0); self.buttonNPCrelationsCant.setChecked(1)
        if configurations["Violence"]: self.buttonNPCviolenceCan.setChecked(1); self.buttonNPCviolenceCant.setChecked(0)
        else: self.buttonNPCviolenceCan.setChecked(0); self.buttonNPCviolenceCant.setChecked(1)
        if configurations["Erotic"]: self.buttonNPCeroticCan.setChecked(1); self.buttonNPCeroticCant.setChecked(0)
        else: self.buttonNPCeroticCan.setChecked(0); self.buttonNPCeroticCant.setChecked(1)

        if configurations["Watersports"]: self.buttonFetishWatersports.setChecked(1); self.buttonFetishWatersports.setText("Enabled")
        else: self.buttonFetishWatersports.setChecked(0); self.buttonFetishWatersports.setText("Disabled")
        if configurations["Pregnancy"]: self.buttonFetishPregnancy.setChecked(1); self.buttonFetishPregnancy.setText("Enabled")
        else: self.buttonFetishPregnancy.setChecked(0); self.buttonFetishPregnancy.setText("Disabled")
        if configurations["Netorare"]: self.buttonFetishNetorare.setChecked(1); self.buttonFetishNetorare.setText("Enabled")
        else: self.buttonFetishNetorare.setChecked(0); self.buttonFetishNetorare.setText("Disabled")
        if configurations["Ryona"]: self.buttonFetishRyona.setChecked(1); self.buttonFetishRyona.setText("Enabled")
        else: self.buttonFetishRyona.setChecked(0); self.buttonFetishRyona.setText("Disabled")
        ""

    def saveCheck(self):
        interact = 1 if self.buttonNPCinteractCan.isChecked() else 0
        relations = 1 if self.buttonNPCrelationsCan.isChecked() else 0
        violence = 1 if self.buttonNPCviolenceCan.isChecked() else 0
        erotic = 1 if self.buttonNPCeroticCan.isChecked() else 0


        watersports = 1 if self.buttonFetishWatersports.isChecked() else 0
        pregnancy = 1 if self.buttonFetishPregnancy.isChecked() else 0
        netorare = 1 if self.buttonFetishNetorare.isChecked() else 0
        ryona = 1 if self.buttonFetishRyona.isChecked() else 0

        configurations = {"Interact":interact, "Relations":relations, "Violence":violence, "Erotic":erotic, "Watersports":watersports, "Pregnancy":pregnancy, "Netorare":netorare, "Ryona":ryona}
        with pathlib.Path.open("playerConfig.json", 'w') as f:
            json.dump(configurations, f)

    ####### NPC Interactions
    def buttonNPCinteractCanAction(self):
        self.buttonNPCinteractCant.setChecked(0)
        ""
    def buttonNPCinteractCantAction(self):
        self.buttonNPCinteractCan.setChecked(0)
        ""

    def buttonNPCrelationsCanAction(self):
        self.buttonNPCrelationsCant.setChecked(0)
        ""
    def buttonNPCrelationsCantAction(self):
        self.buttonNPCrelationsCan.setChecked(0)
        ""

    def buttonNPCviolenceCanAction(self):
        self.buttonNPCviolenceCant.setChecked(0)
        ""
    def buttonNPCviolenceCantAction(self):
        self.buttonNPCviolenceCan.setChecked(0)
        ""

    def buttonNPCeroticCanAction(self):
        self.buttonNPCeroticCant.setChecked(0)
        ""
    def buttonNPCeroticCantAction(self):
        self.buttonNPCeroticCan.setChecked(0)
        ""


    ####### Fetishes
    def buttonFetishWatersportsAction(self):
        if self.buttonFetishWatersports.isChecked(): self.buttonFetishWatersports.setText("Enabled")
        else: self.buttonFetishWatersports.setText("Disabled")
    def buttonFetishPregnancyAction(self):
        if self.buttonFetishPregnancy.isChecked(): self.buttonFetishPregnancy.setText("Enabled")
        else: self.buttonFetishPregnancy.setText("Disabled")
    def buttonFetishNetorareAction(self):
        if self.buttonFetishNetorare.isChecked(): self.buttonFetishNetorare.setText("Enabled")
        else: self.buttonFetishNetorare.setText("Disabled")
    def buttonFetishRyonaAction(self):
        if self.buttonFetishRyona.isChecked(): self.buttonFetishRyona.setText("Enabled")
        else: self.buttonFetishRyona.setText("Disabled")

class UiLayoutOptionsMenu:
    def __init__(self):
        Globals.Layouts["OptionsUI"] = self
        Globals.LayoutsData["OptionsUI"] = {"Source":"optionsMenuUI", "Initialized":0}

    def UI(self):
        MainWindow = Globals.Layouts["MainF"]
        self.GUI = QWidget(MainWindow)

        self.OptionsScroll = QScrollArea(self.GUI)
        self.OptionsScroll.setGeometry(288,5,1024,954)
        self.OptionsScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.OptionsScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.OptionsScroll.setProperty("Color","Dark")

        self.OptionsForm = QGridLayout()
        self.OptionsBox = QGroupBox()
        self.OptionsBox.setLayout(self.OptionsForm)
        self.OptionsBox.setMinimumWidth(1024)
        self.OptionsBox.setMaximumWidth(1024)
        self.OptionsScroll.setWidget(self.OptionsBox)
        self.OptionsForm.setContentsMargins(5, 5, 0, 0)
        self.OptionsForm.WidgetsDict = {}

        ###
        self.InteractWidget = QWidget(objectName = "Transparent")

        self.InteractLabel = QLabel(self.InteractWidget, objectName = "Title")
        self.InteractLabel.setText("NPC Interaction Options")
        self.InteractLabel.setGeometry(0,0,500,45)
        self.InteractLabel.setProperty("Color","Light")
        self.InteractLabel.setAlignment(Qt.AlignCenter)

        #
        self.NPCInteractLabel = QLabel(self.InteractWidget, objectName = "SubTitle")
        self.NPCInteractLabel.setText("NPC Interactions")
        self.NPCInteractLabel.setGeometry(0,50,290,40)
        self.NPCInteractLabel.setProperty("Color","Dark")
        self.NPCInteractLabel.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.NPCInteractButtonOFF = QPushButton("Disabled", self.InteractWidget)
        self.NPCInteractButtonOFF.setGeometry(295,50,100,40)
        self.NPCInteractButtonOFF.setProperty("Color","Light")
        self.NPCInteractButtonOFF.setCheckable(True)

        self.NPCInteractButtonON = QPushButton("Enabled", self.InteractWidget)
        self.NPCInteractButtonON.setGeometry(400,50,100,40)
        self.NPCInteractButtonON.setProperty("Color","Light")
        self.NPCInteractButtonON.setCheckable(True)

        InteractButtonGroup = QButtonGroup(self.InteractWidget)
        InteractButtonGroup.addButton(self.NPCInteractButtonOFF)
        InteractButtonGroup.addButton(self.NPCInteractButtonON)
        InteractButtonGroup.setExclusive(True)
        self.NPCInteractButtonON.setChecked(True)
        #

        #
        self.NPCInteractOtherLabel = QLabel(self.InteractWidget, objectName = "SubTitle")
        self.NPCInteractOtherLabel.setText("Interactions between NPC")
        self.NPCInteractOtherLabel.setGeometry(0,100,290,40)
        self.NPCInteractOtherLabel.setProperty("Color","Dark")
        self.NPCInteractOtherLabel.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.NPCInteractButtonOtherOFF = QPushButton("Disabled", self.InteractWidget)
        self.NPCInteractButtonOtherOFF.setGeometry(295,100,100,40)
        self.NPCInteractButtonOtherOFF.setProperty("Color","Light")
        self.NPCInteractButtonOtherOFF.setCheckable(True)

        self.NPCInteractButtonOtherON = QPushButton("Enabled", self.InteractWidget)
        self.NPCInteractButtonOtherON.setGeometry(400,100,100,40)
        self.NPCInteractButtonOtherON.setProperty("Color","Light")
        self.NPCInteractButtonOtherON.setCheckable(True)

        InteractButtonOtherGroup = QButtonGroup(self.InteractWidget)
        InteractButtonOtherGroup.addButton(self.NPCInteractButtonOtherOFF)
        InteractButtonOtherGroup.addButton(self.NPCInteractButtonOtherON)
        InteractButtonOtherGroup.setExclusive(True)
        self.NPCInteractButtonOtherON.setChecked(True)
        #

        #
        self.NPCInteractPlayerLabel = QLabel(self.InteractWidget, objectName = "SubTitle")
        self.NPCInteractPlayerLabel.setText("NPC interactions with the player")
        self.NPCInteractPlayerLabel.setGeometry(0,150,290,40)
        self.NPCInteractPlayerLabel.setProperty("Color","Dark")
        self.NPCInteractPlayerLabel.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)


        self.NPCInteractButtonPlayerOFF = QPushButton("Disabled", self.InteractWidget)
        self.NPCInteractButtonPlayerOFF.setGeometry(295,150,100,40)
        self.NPCInteractButtonPlayerOFF.setProperty("Color","Light")
        self.NPCInteractButtonPlayerOFF.setCheckable(True)

        self.NPCInteractButtonPlayerON = QPushButton("Enabled", self.InteractWidget)
        self.NPCInteractButtonPlayerON.setGeometry(400,150,100,40)
        self.NPCInteractButtonPlayerON.setProperty("Color","Light")
        self.NPCInteractButtonPlayerON.setCheckable(True)

        InteractButtonPlayerGroup = QButtonGroup(self.InteractWidget)
        InteractButtonPlayerGroup.addButton(self.NPCInteractButtonPlayerOFF)
        InteractButtonPlayerGroup.addButton(self.NPCInteractButtonPlayerON)
        InteractButtonPlayerGroup.setExclusive(True)
        self.NPCInteractButtonPlayerOFF.setChecked(True)
        #


        self.InteractWidget.setMinimumWidth(500)
        self.InteractWidget.setMaximumWidth(500)
        self.InteractWidget.Height = 200
        self.OptionsForm.addWidget(self.InteractWidget, 0, 1)
        ###


        ###
        self.RandomWidget = QWidget(objectName = "Transparent")

        self.RandomLabel = QLabel(self.RandomWidget, objectName = "Title")
        self.RandomLabel.setText("Random NPC Options")
        self.RandomLabel.setGeometry(0,0,500,45)
        self.RandomLabel.setProperty("Color","Light")
        self.RandomLabel.setAlignment(Qt.AlignCenter)

        #
        self.RandomNPCLabel = QLabel(self.RandomWidget, objectName = "SubTitle")
        self.RandomNPCLabel.setText("NPC Interactions")
        self.RandomNPCLabel.setGeometry(0,50,290,40)
        self.RandomNPCLabel.setProperty("Color","Dark")
        self.RandomNPCLabel.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.RandomNPCButtonOFF = QPushButton("Disabled", self.RandomWidget)
        self.RandomNPCButtonOFF.setGeometry(295,50,100,40)
        self.RandomNPCButtonOFF.setProperty("Color","Light")
        self.RandomNPCButtonOFF.setCheckable(True)

        self.RandomNPCButtonON = QPushButton("Enabled", self.RandomWidget)
        self.RandomNPCButtonON.setGeometry(400,50,100,40)
        self.RandomNPCButtonON.setProperty("Color","Light")
        self.RandomNPCButtonON.setCheckable(True)

        RandomNPCButtonGroup = QButtonGroup(self.RandomWidget)
        RandomNPCButtonGroup.addButton(self.RandomNPCButtonOFF)
        RandomNPCButtonGroup.addButton(self.RandomNPCButtonON)
        RandomNPCButtonGroup.setExclusive(True)
        self.RandomNPCButtonON.setChecked(True)
        #

        #
        self.RandomAmountLabel = QLabel(self.RandomWidget, objectName = "SubTitle")
        self.RandomAmountLabel.setText("Amount of random NPC's")
        self.RandomAmountLabel.setGeometry(0,100,290,40)
        self.RandomAmountLabel.setProperty("Color","Dark")
        self.RandomAmountLabel.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        self.RandomAmountLine = QLineEdit(self.RandomWidget)
        self.RandomAmountLine.setText("15")
        self.RandomAmountLine.setGeometry(295,100,290,40)
        self.RandomAmountLine.setProperty("Color","Light")
        self.RandomAmountLine.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.RandomAmountLine.setValidator(QIntValidator(0,99))
        #

        #
        self.RandomSexLabel = QLabel(self.RandomWidget, objectName = "SubTitle")
        self.RandomSexLabel.setText("Sex ratio of random NPC's")
        self.RandomSexLabel.setGeometry(0,150,290,40)
        self.RandomSexLabel.setProperty("Color","Dark")
        self.RandomSexLabel.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)

        def SexLinesRefresh(self):
            try:
                if self.Lines[0] == "Male" and int(self.RandomSexMaleLine.text()) >= 100:
                    self.RandomSexMaleLine.setText(100)
                    self.RandomSexFemaleLine.setText(0)
                    self.RandomSexFutanariLine.setText(0)
                elif self.Lines[0] == "Female" and int(self.RandomSexFemaleLine.text()) >= 100:
                    self.RandomSexMaleLine.setText(0)
                    self.RandomSexFemaleLine.setText(100)
                    self.RandomSexFutanariLine.setText(0)
                elif self.Lines[0] == "Futanari" and int(self.RandomSexFutanariLine.text()) >= 100:
                    self.RandomSexMaleLine.setText(0)
                    self.RandomSexFemaleLine.setText(0)
                    self.RandomSexFutanariLine.setText(100)
                else:
                    FutaValue = int(self.RandomSexFutanariLine.text())
                    FemaleValue = int(self.RandomSexFemaleLine.text())
                    MaleValue = int(self.RandomSexMaleLine.text())

                    if self.Lines[1] == 0:
                        if FutaValue + FemaleValue + MaleValue > 100:
                            Extra = FutaValue + FemaleValue + MaleValue - 100
                            if self.Lines[0] == "Male":
                                for i in range(Extra):
                                    if FemaleValue < FutaValue:
                                        FutaValue -= 1
                                    else:
                                        FemaleValue -= 1
                            elif self.Lines[0] == "Female":
                                for i in range(Extra):
                                    if FutaValue < MaleValue:
                                        MaleValue -= 1
                                    else:
                                        FutaValue -= 1
                            elif self.Lines[0] == "Futanari":
                                for i in range(Extra):
                                    if FemaleValue < MaleValue:
                                        MaleValue -= 1
                                    else:
                                        FemaleValue -= 1
                        elif FutaValue + FemaleValue + MaleValue < 100:
                            Remaining = 100 - FutaValue + FemaleValue + MaleValue
                            if self.Lines[0] == "Male":
                                for i in range(Remaining):
                                    if FemaleValue > FutaValue:
                                        FutaValue += 1
                                    else:
                                        FemaleValue += 1
                            elif self.Lines[0] == "Female":
                                for i in range(Remaining):
                                    if FutaValue > MaleValue:
                                        MaleValue += 1
                                    else:
                                        FutaValue += 1
                            elif self.Lines[0] == "Futanari":
                                for i in range(Remaining):
                                    if FemaleValue > MaleValue:
                                        MaleValue += 1
                                    else:
                                        FemaleValue += 1

                        self.RandomSexMaleLine.setText(str(MaleValue))
                        self.RandomSexFemaleLine.setText(str(FemaleValue))
                        self.RandomSexFutanariLine.setText(str(FutaValue))
                    else:
                        if (self.Lines[0] == "Male" and self.Lines[1] == "Female") and MaleValue + FemaleValue > 100:
                            FemaleValue = 100 - MaleValue
                        elif (self.Lines[0] == "Female" and self.Lines[1] == "Male") and MaleValue + FemaleValue > 100:
                            MaleValue = 100 - FemaleValue

                        elif (self.Lines[0] == "Futanari" and self.Lines[1] == "Female") and FutaValue + FemaleValue > 100:
                            FemaleValue = 100 - FutaValue
                        elif (self.Lines[0] == "Female" and self.Lines[1] == "Futanari") and FutaValue + FemaleValue > 100:
                            FutaValue = 100 - FemaleValue

                        elif (self.Lines[0] == "Futanari" and self.Lines[1] == "Male") and FutaValue + MaleValue > 100:
                            MaleValue = 100 - FutaValue
                        elif (self.Lines[0] == "Male" and self.Lines[1] == "Futanari") and FutaValue + MaleValue > 100:
                            FutaValue = 100 - MaleValue

                        else:
                            # if FutaValue + FemaleValue + MaleValue < 100:
                            if (self.Lines[0] == "Male" and self.Lines[1] == "Female") or (self.Lines[0] == "Female" and self.Lines[1] == "Male"):
                                FutaValue = 100 - (MaleValue + FemaleValue)
                            elif (self.Lines[0] == "Futanari" and self.Lines[1] == "Female") or (self.Lines[0] == "Female" and self.Lines[1] == "Futanari"):
                                MaleValue = 100 - (FutaValue + FemaleValue)
                            elif (self.Lines[0] == "Male" and self.Lines[1] == "Futanari") or (self.Lines[0] == "Futanari" and self.Lines[1] == "Male"):
                                FemaleValue = 100 - (MaleValue + FutaValue)

                    self.RandomSexMaleLine.setText(str(MaleValue))
                    self.RandomSexFemaleLine.setText(str(FemaleValue))
                    self.RandomSexFutanariLine.setText(str(FutaValue))
            except Exception as e:
                print(e)
        self.Lines = [0,0]
        self.RandomSexMaleLabel = QLabel(self.RandomWidget, objectName = "SmallText")
        self.RandomSexMaleLabel.setText("Male")
        self.RandomSexMaleLabel.setGeometry(300,130,60,20)
        self.RandomSexMaleLabel.setProperty("Color", "None")
        self.RandomSexMaleLabel.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.RandomSexMaleLine = QLineEdit(self.RandomWidget)
        self.RandomSexMaleLine.setText("45")
        self.RandomSexMaleLine.setGeometry(295,150,65,40)
        self.RandomSexMaleLine.setProperty("Color","Light")
        self.RandomSexMaleLine.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        def MaleFinished(self):
            self.Lines[1] = self.Lines[0]
            self.Lines[0] = "Male"
            SexLinesRefresh(self)

        self.RandomSexMaleLine.editingFinished.connect(lambda: MaleFinished(self))


        self.RandomSexFemaleLabel = QLabel(self.RandomWidget, objectName = "SmallText")
        self.RandomSexFemaleLabel.setText("Female")
        self.RandomSexFemaleLabel.setGeometry(370,130,60,20)
        self.RandomSexFemaleLabel.setProperty("Color", "None")
        self.RandomSexFemaleLabel.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.RandomSexFemaleLine = QLineEdit(self.RandomWidget)
        self.RandomSexFemaleLine.setText("45")
        self.RandomSexFemaleLine.setGeometry(365,150,65,40)
        self.RandomSexFemaleLine.setProperty("Color","Light")
        self.RandomSexFemaleLine.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        def FemaleFinished(self):
            self.Lines[1] = self.Lines[0]
            self.Lines[0] = "Female"
            SexLinesRefresh(self)

        self.RandomSexFemaleLine.editingFinished.connect(lambda: FemaleFinished(self))


        self.RandomSexFutanariLabel = QLabel(self.RandomWidget, objectName = "SmallText")
        self.RandomSexFutanariLabel.setText("Futanari")
        self.RandomSexFutanariLabel.setGeometry(440,130,60,20)
        self.RandomSexFutanariLabel.setProperty("Color", "None")
        self.RandomSexFutanariLabel.setAlignment(Qt.AlignTop | Qt.AlignHCenter)
        self.RandomSexFutanariLine = QLineEdit(self.RandomWidget)
        self.RandomSexFutanariLine.setText("10")
        self.RandomSexFutanariLine.setGeometry(435,150,65,40)
        self.RandomSexFutanariLine.setProperty("Color","Light")
        self.RandomSexFutanariLine.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        def FutaFinished(self):
            self.Lines[1] = self.Lines[0]
            self.Lines[0] = "Futanari"
            SexLinesRefresh(self)

        self.RandomSexFutanariLine.editingFinished.connect(lambda: FutaFinished(self))


        self.RandomWidget.setMinimumWidth(500)
        self.RandomWidget.setMaximumWidth(500)
        self.RandomWidget.Height = 200
        self.OptionsForm.addWidget(self.RandomWidget, 0, 2)
        ###



        self.ControlWidget = QWidget(self.GUI)
        self.ControlWidget.setGeometry(5,964,1592,55)
        self.ControlWidget.setProperty("Color","Dark")

        self.ButtonMenu = QPushButton("Back", self.ControlWidget, clicked = lambda: MainWindow.gotoPreviousLayout())
        self.ButtonMenu.setGeometry(10,6,200,45)

        self.ButtonSave = QPushButton("Save", self.ControlWidget, clicked = lambda: self.Save())
        self.ButtonSave.setGeometry(220,6,200,45)


    def Refresh(self):
        self.InteractWidget.setMinimumHeight(self.InteractWidget.Height)
        self.InteractWidget.setMaximumHeight(self.InteractWidget.Height)

        self.RandomWidget.setMinimumHeight(self.RandomWidget.Height)
        self.RandomWidget.setMaximumHeight(self.RandomWidget.Height)


        # Width = self.InteractWidget.width() + self.RandomWidget.width()
        self.OptionsBox.setMinimumWidth(1020)
        self.OptionsBox.setMaximumWidth(1020)
        self.OptionsBox.setMinimumHeight(self.InteractWidget.Height)
        self.OptionsBox.setMaximumHeight(self.InteractWidget.Height)

        Interactions = Globals.PlayerConfig["Interactions"]
        BetweenNPC = Globals.PlayerConfig["BetweenNPC"]
        NPCtoPC = Globals.PlayerConfig["NPCtoPC"]

        RandomNPC = Globals.PlayerConfig["RandomNPC"]

        RandomAmount = Globals.PlayerConfig["RandomAmount"]

        MaleRatio = Globals.PlayerConfig["RandomRatio"]["Male"]
        FemaleRatio = Globals.PlayerConfig["RandomRatio"]["Female"]
        FutaRatio = Globals.PlayerConfig["RandomRatio"]["FutaRatio"]


        if Interactions == 1: self.NPCInteractButtonON.setChecked(True)
        else: self.NPCInteractButtonOFF.setChecked(True)

        if BetweenNPC == 1: self.NPCInteractButtonOtherON.setChecked(True)
        else: self.NPCInteractButtonOtherOFF.setChecked(True)

        if NPCtoPC == 1: self.NPCInteractButtonPlayerON.setChecked(True)
        else: self.NPCInteractButtonPlayerOFF.setChecked(True)

        if RandomNPC == 1: self.RandomNPCButtonON.setChecked(True)
        else: self.RandomNPCButtonOFF.setChecked(True)

        self.RandomAmountLine.setText(str(RandomAmount))

        self.RandomSexMaleLine.setText(str(MaleRatio))
        self.RandomSexFemaleLine.setText(str(FemaleRatio))
        self.RandomSexFutanariLine.setText(str(FutaRatio))

        # Globals.PlayerConfig["RandomRatio"] = {"Male":MaleRatio, "Female":FemaleRatio, "FutaRatio":FutaRatio}


    def Save(self):
        print(Globals.PlayerConfig)
        if self.NPCInteractButtonOFF.isChecked: Interactions = 0
        if self.NPCInteractButtonON.isChecked: Interactions = 1

        if self.NPCInteractButtonOtherOFF.isChecked: BetweenNPC = 0
        if self.NPCInteractButtonOtherON.isChecked: BetweenNPC = 1

        if self.NPCInteractButtonPlayerOFF.isChecked: NPCtoPC = 0
        if self.NPCInteractButtonPlayerON.isChecked: NPCtoPC = 1

        if self.RandomNPCButtonOFF.isChecked: RandomNPC = 0
        if self.RandomNPCButtonON.isChecked: RandomNPC = 1

        RandomAmount = int(self.RandomAmountLine.text())
        MaleRatio = int(self.RandomSexMaleLine.text())
        FemaleRatio = int(self.RandomSexFemaleLine.text())
        FutaRatio = int(self.RandomSexFutanariLine.text())

        Globals.PlayerConfig["Interactions"] = Interactions
        Globals.PlayerConfig["BetweenNPC"] = BetweenNPC
        Globals.PlayerConfig["NPCtoPC"] = NPCtoPC
        Globals.PlayerConfig["RandomNPC"] = RandomNPC
        Globals.PlayerConfig["RandomAmount"] = RandomAmount
        Globals.PlayerConfig["RandomRatio"] = {"Male":MaleRatio, "Female":FemaleRatio, "FutaRatio":FutaRatio}
        print(Globals.PlayerConfig)

    def ResizeEvent(self):
        Width = Globals.Layouts["MainF"].width()
        Height = Globals.Layouts["MainF"].height()
        Diff = 1024 - Height

        self.OptionsScroll.setGeometry(288,5,1024,954-Diff)
        self.ControlWidget.setGeometry(5,964-Diff,1592,55)



def Initialize(self, Reference):
    if "OptionsUI" not in Globals.Layouts:
        Object = UiLayoutOptionsMenu()
