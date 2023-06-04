import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QTextCursor
import json
import os


class UiLayoutOptionsMenu(object):
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
        self.NPCWidget = QWidget()
        self.NPCWidget.setFixedSize(800,250)
        self.NPCWidget.setStyleSheet('''
        QWidget{
    	background-color:rgb(23, 23, 23);
        }
        QPushButton{
        background-color:rgb(35, 35, 35)
        }
        ''')

        self.labelNPCinteractions = QLabel("NPC Interactions", self.NPCWidget)
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
        self.labelNPCinteract = QLabel("NPC Can Interact With One Another", self.NPCWidget)
        self.labelNPCinteract.setFont(QFont('Segoe UI', 14))
        self.labelNPCinteract.setGeometry(20,60,390,40)
        self.labelNPCinteract.setAlignment(Qt.AlignVCenter)
        self.labelNPCinteract.setAlignment(Qt.AlignHCenter)
        self.buttonNPCinteractCan = QPushButton("Can", self.NPCWidget)
        self.buttonNPCinteractCan.setFont(QFont('Segoe UI', 14))
        self.buttonNPCinteractCan.setGeometry(100,100,90,35)
        self.buttonNPCinteractCan.setCheckable(True)
        self.buttonNPCinteractCan.clicked.connect(self.buttonNPCinteractCanAction)
        self.buttonNPCinteractCant = QPushButton("Can't", self.NPCWidget)
        self.buttonNPCinteractCant.setFont(QFont('Segoe UI', 14))
        self.buttonNPCinteractCant.setGeometry(210,100,90,35)
        self.buttonNPCinteractCant.setCheckable(True)
        self.buttonNPCinteractCant.clicked.connect(self.buttonNPCinteractCantAction)

        self.labelNPCrelations = QLabel("NPC Can Form Relationships", self.NPCWidget)
        self.labelNPCrelations.setFont(QFont('Segoe UI', 14))
        self.labelNPCrelations.setGeometry(420,60,390,40)
        self.labelNPCrelations.setAlignment(Qt.AlignVCenter)
        self.labelNPCrelations.setAlignment(Qt.AlignHCenter)
        self.buttonNPCrelationsCan = QPushButton("Can", self.NPCWidget)
        self.buttonNPCrelationsCan.setFont(QFont('Segoe UI', 14))
        self.buttonNPCrelationsCan.setGeometry(500,100,90,35)
        self.buttonNPCrelationsCan.setCheckable(True)
        self.buttonNPCrelationsCan.clicked.connect(self.buttonNPCrelationsCanAction)
        self.buttonNPCrelationsCant = QPushButton("Can't", self.NPCWidget)
        self.buttonNPCrelationsCant.setFont(QFont('Segoe UI', 14))
        self.buttonNPCrelationsCant.setGeometry(610,100,90,35)
        self.buttonNPCrelationsCant.setCheckable(True)
        self.buttonNPCrelationsCant.clicked.connect(self.buttonNPCrelationsCantAction)

        self.labelNPCviolence = QLabel("Violent interactions between NPC", self.NPCWidget)
        self.labelNPCviolence.setFont(QFont('Segoe UI', 14))
        self.labelNPCviolence.setGeometry(20,150,390,40)
        self.labelNPCviolence.setAlignment(Qt.AlignVCenter)
        self.labelNPCviolence.setAlignment(Qt.AlignHCenter)
        self.buttonNPCviolenceCan = QPushButton("Can", self.NPCWidget)
        self.buttonNPCviolenceCan.setFont(QFont('Segoe UI', 14))
        self.buttonNPCviolenceCan.setGeometry(100,190,90,35)
        self.buttonNPCviolenceCan.setCheckable(True)
        self.buttonNPCviolenceCan.clicked.connect(self.buttonNPCviolenceCanAction)
        self.buttonNPCviolenceCant = QPushButton("Can't", self.NPCWidget)
        self.buttonNPCviolenceCant.setFont(QFont('Segoe UI', 14))
        self.buttonNPCviolenceCant.setGeometry(210,190,90,35)
        self.buttonNPCviolenceCant.setCheckable(True)
        self.buttonNPCviolenceCant.clicked.connect(self.buttonNPCviolenceCantAction)

        self.labelNPCerotic = QLabel("Erotic interactions between NPC", self.NPCWidget)
        self.labelNPCerotic.setFont(QFont('Segoe UI', 14))
        self.labelNPCerotic.setGeometry(420,150,390,40)
        self.labelNPCerotic.setAlignment(Qt.AlignVCenter)
        self.labelNPCerotic.setAlignment(Qt.AlignHCenter)
        self.buttonNPCeroticCan = QPushButton("Can", self.NPCWidget)
        self.buttonNPCeroticCan.setFont(QFont('Segoe UI', 14))
        self.buttonNPCeroticCan.setGeometry(500,190,90,35)
        self.buttonNPCeroticCan.setCheckable(True)
        self.buttonNPCeroticCan.clicked.connect(self.buttonNPCeroticCanAction)
        self.buttonNPCeroticCant = QPushButton("Can't", self.NPCWidget)
        self.buttonNPCeroticCant.setFont(QFont('Segoe UI', 14))
        self.buttonNPCeroticCant.setGeometry(610,190,90,35)
        self.buttonNPCeroticCant.setCheckable(True)
        self.buttonNPCeroticCant.clicked.connect(self.buttonNPCeroticCantAction)

        myform.addWidget(self.NPCWidget)
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
        with open('playerConfig.json', 'rb') as f:
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
        if self.buttonNPCinteractCan.isChecked(): interact = 1
        else: interact = 0
        if self.buttonNPCrelationsCan.isChecked(): relations = 1
        else: relations = 0
        if self.buttonNPCviolenceCan.isChecked(): violence = 1
        else: violence = 0
        if self.buttonNPCeroticCan.isChecked(): erotic = 1
        else: erotic = 0


        if self.buttonFetishWatersports.isChecked(): watersports = 1
        else: watersports = 0
        if self.buttonFetishPregnancy.isChecked(): pregnancy = 1
        else: pregnancy = 0
        if self.buttonFetishNetorare.isChecked(): netorare = 1
        else: netorare = 0
        if self.buttonFetishRyona.isChecked(): ryona = 1
        else: ryona = 0

        configurations = {"Interact":interact, "Relations":relations, "Violence":violence, "Erotic":erotic, "Watersports":watersports, "Pregnancy":pregnancy, "Netorare":netorare, "Ryona":ryona}
        with open("playerConfig.json", 'w') as f:
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

def Initialize(self, Reference):
    ""
