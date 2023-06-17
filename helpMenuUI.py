
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import Globals


class UiLayoutHelpMenu:
    def __init__(self):
        Globals.Layouts["HelpUI"] = self
        Globals.LayoutsData["HelpUI"] = {"Source":"helpMenuUI", "Initialized":0}

    def UI(self):
        MainWindow = Globals.Layouts["MainF"]
        self.GUI = QWidget(MainWindow)

        self.LabelBack = QLabel(self.GUI)
        self.LabelBack.setGeometry(288,5,1024,954)
        self.LabelBack.setProperty("Color", "Dark")

        self.MainScroll = QScrollArea(self.GUI)
        self.MainScroll.setGeometry(293,5,1014,954)
        self.MainScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.MainScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.MainForm = QVBoxLayout()
        self.MainBox = QGroupBox()
        self.MainBox.setLayout(self.MainForm)
        self.MainBox.setMinimumWidth(1014)
        self.MainScroll.setWidget(self.MainBox)
        self.MainForm.setContentsMargins(0, 0, 0, 0)
        # self.MainBox.setStyleSheet('''background-color:rgb(255,0,0)''')

        ###
        NPCImportWidget = QWidget(objectName = "Transparent")

        NPCImportQuestion = QLabel(NPCImportWidget, objectName = "Title")
        NPCImportQuestion.setGeometry(0,0,1014,35)
        NPCImportQuestion.setText('''I just started the game and i can't see anyone''')
        NPCImportQuestion.setProperty("Color","None")
        NPCImportQuestion.setWordWrap(True)

        NPCImportAnswer = QLabel(NPCImportWidget, objectName = "SubTitle")
        NPCImportAnswer.setText('''If you are just starting the game, please make sure to go to the 'Manage Characters' menu and import any desired NPC into the game. Or make sure that in the 'Options' menu the random NPCs are enabled''')
        NPCImportAnswer.setGeometry(0,40,1014,50)
        NPCImportAnswer.setProperty("Color","None")
        NPCImportAnswer.setWordWrap(True)

        NPCImportWidget.setMaximumWidth(1014)
        NPCImportWidget.setMinimumWidth(1014)
        NPCImportWidget.setMinimumHeight(90)
        NPCImportWidget.setMaximumHeight(90)

        self.MainForm.addWidget(NPCImportWidget)
        self.MainBox.setMinimumHeight(self.MainBox.height() + NPCImportWidget.height()+10)
        self.MainBox.setMaximumHeight(self.MainBox.height() + NPCImportWidget.height()+10)
        # NPCImportWidget.setStyleSheet('''background-color:rgb(0,255,0)''')
        ###


        ###
        NPCLocationWidget = QWidget(objectName = "Transparent")

        NPCLocationQuestion = QLabel(NPCLocationWidget, objectName = "Title")
        NPCLocationQuestion.setGeometry(0,0,1014,35)
        NPCLocationQuestion.setText("I already imported NPCs but i can't find any")
        NPCLocationQuestion.setProperty("Color","None")
        NPCLocationQuestion.setWordWrap(True)

        NPCLocationAnswer = QLabel(NPCLocationWidget, objectName = "SubTitle")
        NPCLocationAnswer.setText("Most NPCs when imported start at the Residential Area, which can be accessed going first to the Eastern Street")
        NPCLocationAnswer.setGeometry(0,40,1014,35)
        NPCLocationAnswer.setProperty("Color","None")
        NPCLocationAnswer.setWordWrap(True)

        NPCLocationWidget.setMaximumWidth(1014)
        NPCLocationWidget.setMinimumWidth(1014)
        NPCLocationWidget.setMinimumHeight(75)
        NPCLocationWidget.setMaximumHeight(75)

        self.MainForm.addWidget(NPCLocationWidget)
        self.MainBox.setMinimumHeight(self.MainBox.height() + NPCLocationWidget.height()+10)
        self.MainBox.setMaximumHeight(self.MainBox.height() + NPCLocationWidget.height()+10)
        # NPCLocationWidget.setStyleSheet('''background-color:rgb(0,0,255)''')
        ###

        ###
        NPCSymbolWidget = QWidget(objectName = "Transparent")

        NPCSymbolQuestion = QLabel(NPCSymbolWidget, objectName = "Title")
        NPCSymbolQuestion.setGeometry(0,0,1014,35)
        NPCSymbolQuestion.setText("What do the symbols on the NPC represent?")
        NPCSymbolQuestion.setProperty("Color","None")
        NPCSymbolQuestion.setWordWrap(True)

        NPCSymbolAnswer = QLabel(NPCSymbolWidget, objectName = "SubTitle")
        NPCSymbolAnswer.setText("The heart's at the top represent a character arousal. The lighting bolt's in the middle represents a charcter energy. The diamonds at the bottom represent a character mood, blue for positive mood, red for negative mood.")
        NPCSymbolAnswer.setGeometry(0,40,1014,50)
        NPCSymbolAnswer.setProperty("Color","None")
        NPCSymbolAnswer.setWordWrap(True)

        NPCSymbolWidget.setMaximumWidth(1014)
        NPCSymbolWidget.setMinimumWidth(1014)
        NPCSymbolWidget.setMinimumHeight(90)
        NPCSymbolWidget.setMaximumHeight(90)

        self.MainForm.addWidget(NPCSymbolWidget)
        self.MainBox.setMinimumHeight(self.MainBox.height() + NPCSymbolWidget.height()+10)
        self.MainBox.setMaximumHeight(self.MainBox.height() + NPCSymbolWidget.height()+10)
        # NPCLocationWidget.setStyleSheet('''background-color:rgb(0,0,255)''')
        ###

        ###
        NPCDisappearWidget = QWidget(objectName = "Transparent")

        NPCDisappearQuestion = QLabel(NPCDisappearWidget, objectName = "Title")
        NPCDisappearQuestion.setGeometry(0,0,1014,35)
        NPCDisappearQuestion.setText("The characters keep disappearing")
        NPCDisappearQuestion.setProperty("Color","None")
        NPCDisappearQuestion.setWordWrap(True)

        NPCDisappearAnswer = QLabel(NPCDisappearWidget, objectName = "SubTitle")
        NPCDisappearAnswer.setText("If you haven't interacted, or failed to interact, with a cahracter for three or more actions, there is a chance that they will randomly wander away. And if a character is low on energy they will go to sleep and be away for 8 hours.")
        NPCDisappearAnswer.setGeometry(0,40,1014,50)
        NPCDisappearAnswer.setProperty("Color","None")
        NPCDisappearAnswer.setWordWrap(True)

        NPCDisappearWidget.setMaximumWidth(1014)
        NPCDisappearWidget.setMinimumWidth(1014)
        NPCDisappearWidget.setMinimumHeight(90)
        NPCDisappearWidget.setMaximumHeight(90)

        self.MainForm.addWidget(NPCDisappearWidget)
        self.MainBox.setMinimumHeight(self.MainBox.height() + NPCDisappearWidget.height()+10)
        self.MainBox.setMaximumHeight(self.MainBox.height() + NPCDisappearWidget.height()+10)
        # NPCLocationWidget.setStyleSheet('''background-color:rgb(0,0,255)''')
        ###

        ###
        NPCAfterWidget = QWidget(objectName = "Transparent")

        NPCAfterQuestion = QLabel(NPCAfterWidget, objectName = "Title")
        NPCAfterQuestion.setGeometry(0,0,1014,35)
        NPCAfterQuestion.setText("I already interacted with the characters, what to do next?")
        NPCAfterQuestion.setProperty("Color","None")
        NPCAfterQuestion.setWordWrap(True)

        NPCAfterAnswer = QLabel(NPCAfterWidget, objectName = "SubTitle")
        NPCAfterAnswer.setText("After having interactied with the characters for some time, you can go back to 'Home' and sleep, in there to the left you'll see a list of the characters you have a relationship with, and clicking on any will lead you to the menu to improve your raltionship with them")
        NPCAfterAnswer.setGeometry(0,40,1014,75)
        NPCAfterAnswer.setProperty("Color","None")
        NPCAfterAnswer.setWordWrap(True)

        NPCAfterWidget.setMaximumWidth(1014)
        NPCAfterWidget.setMinimumWidth(1014)
        NPCAfterWidget.setMinimumHeight(115)
        NPCAfterWidget.setMaximumHeight(115)

        self.MainForm.addWidget(NPCAfterWidget)
        self.MainBox.setMinimumHeight(self.MainBox.height() + NPCAfterWidget.height()+10)
        self.MainBox.setMaximumHeight(self.MainBox.height() + NPCAfterWidget.height()+10)
        # NPCRejectWidget.setStyleSheet('''background-color:rgb(0,0,255)''')
        ###

        ###
        NPCRejectWidget = QWidget(objectName = "Transparent")

        NPCRejectQuestion = QLabel(NPCRejectWidget, objectName = "Title")
        NPCRejectQuestion.setGeometry(0,0,1014,35)
        NPCRejectQuestion.setText("The characters keep rejecting my actions")
        NPCRejectQuestion.setProperty("Color","None")
        NPCRejectQuestion.setWordWrap(True)

        NPCRejectAnswer = QLabel(NPCRejectWidget, objectName = "SubTitle")
        NPCRejectAnswer.setText("If you are trying to do something the character doesn't like, they will try to reject said interaction, to counteract this you can improve your relationship with the character using gems")
        NPCRejectAnswer.setGeometry(0,40,1014,50)
        NPCRejectAnswer.setProperty("Color","None")
        NPCRejectAnswer.setWordWrap(True)

        NPCRejectWidget.setMaximumWidth(1014)
        NPCRejectWidget.setMinimumWidth(1014)
        NPCRejectWidget.setMinimumHeight(90)
        NPCRejectWidget.setMaximumHeight(90)

        self.MainForm.addWidget(NPCRejectWidget)
        self.MainBox.setMinimumHeight(self.MainBox.height() + NPCRejectWidget.height()+10)
        self.MainBox.setMaximumHeight(self.MainBox.height() + NPCRejectWidget.height()+10)
        # NPCLocationWidget.setStyleSheet('''background-color:rgb(0,0,255)''')
        ###

        ###
        NPCGemsWidget = QWidget(objectName = "Transparent")

        NPCGemsQuestion = QLabel(NPCGemsWidget, objectName = "Title")
        NPCGemsQuestion.setGeometry(0,0,1014,35)
        NPCGemsQuestion.setText("How do i obtain gems?")
        NPCGemsQuestion.setProperty("Color","None")
        NPCGemsQuestion.setWordWrap(True)

        NPCGemsAnswer = QLabel(NPCGemsWidget, objectName = "SubTitle")
        NPCGemsAnswer.setText("For every value you give such as favor or submission, you'll earn gems equal to that amount/10, rounded down, such as 3000 of a value turn into 100 gems, or 15000 of the value turn into 1000 gems")
        NPCGemsAnswer.setGeometry(0,40,1014,50)
        NPCGemsAnswer.setProperty("Color","None")
        NPCGemsAnswer.setWordWrap(True)

        NPCGemsWidget.setMaximumWidth(1014)
        NPCGemsWidget.setMinimumWidth(1014)
        NPCGemsWidget.setMinimumHeight(90)
        NPCGemsWidget.setMaximumHeight(90)

        self.MainForm.addWidget(NPCGemsWidget)
        self.MainBox.setMinimumHeight(self.MainBox.height() + NPCGemsWidget.height()+10)
        self.MainBox.setMaximumHeight(self.MainBox.height() + NPCGemsWidget.height()+10)
        # NPCLocationWidget.setStyleSheet('''background-color:rgb(0,0,255)''')
        ###

        ###
        IssuesWidget = QWidget(objectName = "Transparent")

        IssuesQuestion = QLabel(IssuesWidget, objectName = "Title")
        IssuesQuestion.setGeometry(0,0,1014,35)
        IssuesQuestion.setText("Some text doesn't make any sense or i just found a bug")
        IssuesQuestion.setProperty("Color","None")
        IssuesQuestion.setWordWrap(True)

        IssuesAnswer = QLabel(IssuesWidget, objectName = "SubTitle")
        IssuesAnswer.setText("Please make sure to report any odd behaivor, issues, and typos on the discord, include as much information as you can regarding the issue, like what the text says, or what you were doing when you found the bug")
        IssuesAnswer.setGeometry(0,40,1014,50)
        IssuesAnswer.setProperty("Color","None")
        IssuesAnswer.setWordWrap(True)

        IssuesWidget.setMaximumWidth(1014)
        IssuesWidget.setMinimumWidth(1014)
        IssuesWidget.setMinimumHeight(90)
        IssuesWidget.setMaximumHeight(90)

        self.MainForm.addWidget(IssuesWidget)
        self.MainBox.setMinimumHeight(self.MainBox.height() + IssuesWidget.height()+10)
        self.MainBox.setMaximumHeight(self.MainBox.height() + IssuesWidget.height()+10)
        # NPCLocationWidget.setStyleSheet('''background-color:rgb(0,0,255)''')
        ###

        ###
        SuggestionsWidget = QWidget(objectName = "Transparent")

        SuggestionsQuestion = QLabel(SuggestionsWidget, objectName = "Title")
        SuggestionsQuestion.setGeometry(0,0,1014,35)
        SuggestionsQuestion.setText("I've thought of an idea for the game or a quality of life feature")
        SuggestionsQuestion.setProperty("Color","None")
        SuggestionsQuestion.setWordWrap(True)

        SuggestionsAnswer = QLabel(SuggestionsWidget, objectName = "SubTitle")
        SuggestionsAnswer.setText("You can submit any idea or request on the discord, please use the appropiate channel for that")
        SuggestionsAnswer.setGeometry(0,40,1014,35)
        SuggestionsAnswer.setProperty("Color","None")
        SuggestionsAnswer.setWordWrap(True)

        SuggestionsWidget.setMaximumWidth(1014)
        SuggestionsWidget.setMinimumWidth(1014)
        SuggestionsWidget.setMinimumHeight(75)
        SuggestionsWidget.setMaximumHeight(75)

        self.MainForm.addWidget(SuggestionsWidget)
        self.MainBox.setMinimumHeight(self.MainBox.height() + SuggestionsWidget.height()+10)
        self.MainBox.setMaximumHeight(self.MainBox.height() + SuggestionsWidget.height()+10)
        # NPCLocationWidget.setStyleSheet('''background-color:rgb(0,0,255)''')
        ###


        self.LabelControl = QLabel(self.GUI)
        self.LabelControl.setGeometry(5,964,1592,55)
        self.LabelControl.setProperty("Color","Dark")

        self.ButtonMenu = QPushButton("Back", self.GUI, clicked = lambda: MainWindow.gotoPreviousLayout())
        self.ButtonMenu.setGeometry(15,970,200,45)

    def Refresh(self):
        ""

def Initialize(self, Reference):
    if "HelpUI" not in Globals.Layouts:
        Object = UiLayoutHelpMenu()
