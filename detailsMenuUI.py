import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QTextCursor
import json
import os
import Globals
import random
import math
import re
import pathlib
Log = Globals.Layouts["MainF"].Log
class ValueWidget:
    def __init__(self, ID, Value):
        self.ID = ID
        self.Value = Value

    def GetWidget(self):
        ID = self.ID
        Value = self.Value

        ValueLabel = QLabel()
        ValueLabel.setText(f'''{ID}: {Value}''')
        ValueLabel.setGeometry(0, 40, 150, 35)
        ValueLabel.setFont(QFont('Segoe UI', 12))
        ValueLabel.setStyleSheet('''
        background-color:rgba(23,23,23,0);
        border:none;
        ''')

        return ValueLabel


class UiLayoutDetailsMenu:
    def __init__(self):
        Globals.Layouts["DetailsUI"] = self
        if "DetailsUI" not in Globals.LayoutsData:
            Globals.LayoutsData["DetailsUI"] = {"Source":"detailsMenuUI", "Initialized":0, "ID":None, "Name":None, "Type":0}
        else:
            Globals.LayoutsData["DetailsUI"]["Source"] = "detailsMenuUI"


    def UI(self):
        MainWindow = Globals.Layouts["MainF"]
        self.GUI = QWidget(MainWindow)
        # mainwindow.setWindowIcon(QtGui.QIcon('PhotoIcon.png'))
        # self.GUI.setStyleSheet('''
        # QWidget{
        # background-color:rgb(35,35,35);
        # }
        # .QGroupBox{
        # border:none;
        # background:none;
        # }
        #
        # .QScrollArea{
        # border:none;
        # background-color:rgba(23,23,23,0)
        # }
        #
        # QPushButton{
        # color:rgb(255, 255, 255);
        # font-size: 14pt;
        # font-family: Segoe UI;
        # }
        # QPushButton:hover{
        # color:rgb(255, 255, 0);
        # }
        #
        # QLabel{
        # color:rgb(255, 255, 255);
        # border:1px solid black;
        # }
        # QLabel:hover{
        # color:rgb(255, 255, 0);
        # }
        #
        # QLabel#MainTitle{
        # color:rgb(255, 255, 255);
        # border:1px solid black;
        # }
        #
        # QLabel#SubTitle{
        # color:rgb(255, 255, 255);
        # border:1px solid black;
        # }
        # QLabel#SubTitle:hover{
        # color:rgb(255, 255, 0);
        # }
        #
        # QLineEdit{
        # color:rgb(255, 255, 255);
        # border:1px solid black;
        # background-color:rgb(35,35,35);
        # }
        #
        # QTextEdit{
        # color:rgb(255, 255, 255);
        # border:1px solid black;
        # background-color:rgb(35,35,35);
        # }
        #
        # QComboBox{
        # background-color:rgb(23,23,23);
        # color:rgb(255, 255, 255);
        # }
        # QComboBox:hover{
        # color:rgb(255, 255, 0);
        # }
		# QComboBox QAbstractItemView {
        # border: 1px solid grey;
        # color: white;
        # selection-color: yellow;
		# }
        #
        # QRadioButton{
        # color:rgb(255, 255, 255);
        # }
        # QRadioButton:hover{
        # color:rgb(255, 255, 0);
        # }
        #
        # QToolTip{
        # background-color: rgb(23,23,23);
        # color: white;
        # border: 1px solid black;
        #
        #
        # }
        #
        # ''')

        self.MainScroll = QScrollArea(self.GUI)
        self.MainScroll.setGeometry(288,5,1024,954)
        self.MainScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.MainScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.MainScroll.setStyleSheet('''
        .QScrollArea{
        border: none;
        background-color:rgb(23, 23, 23);
        }
        QGroupBox{
        border: none;
        }
        ''')
        self.MainForm = QVBoxLayout()
        self.MainBox = QGroupBox()
        self.MainBox.setLayout(self.MainForm)
        self.MainBox.setMinimumWidth(1024)
        self.MainScroll.setWidget(self.MainBox)
        self.MainForm.setContentsMargins(0, 0, 0, 5)
        self.MainForm.WidgetsList = []


        self.LabelControl = QLabel(self.GUI)
        self.LabelControl.setGeometry(5,964,1592,55)
        self.LabelControl.setStyleSheet('''
        QLabel{
        background-color:rgb(23,23,23);
        }
        ''')

        self.ButtonMenu = QPushButton("Back", self.GUI, clicked = lambda: MainWindow.gotoPreviousLayout())
        self.ButtonMenu.setGeometry(15,970,200,45)

        # Globals.LayoutsData["DetailsUI"]["ID"] = "02"
        # Globals.LayoutsData["DetailsUI"]["Name"] = "Valerie"
        # Globals.LayoutsData["DetailsUI"]["Type"] = 1

    def Initialize(self):
        ""
    def Refresh(self):
        for Widget in self.MainForm.WidgetsList:
            self.MainForm.removeWidget(Widget)

        if Globals.LayoutsData["DetailsUI"]["ID"] != None and Globals.LayoutsData["DetailsUI"]["Name"] != None:
            Type = Globals.LayoutsData["DetailsUI"]["Type"]
            # 0 = DEFAULT DATA/ 1 = CURRENT DATA/ 2 = RANDOMIZED NPC
            ### GATHERING THE NPC DATA
            if Type == 0:
                ID = Globals.LayoutsData["DetailsUI"]["ID"]
                Name = Globals.LayoutsData["DetailsUI"]["Name"]

                with open(pathlib.Path() / "NPCData" / f"{Name}{ID}" / f"{Name}{ID}Data.json" , 'rb') as f:
                    NPCData = json.load(f)

                Files = os.listdir( os.path.abspath( pathlib.Path() / "NPCData" / f"{Name}{ID}" ) )
                # Files = os.listdir(f'''NPCData/{Name}{ID}''')
                ImageType = "Portrait"
                list = [File for File in Files if File.endswith((".png")) or File.endswith((".jpg")) or File.endswith((".jpeg"))]
                ListPortraits, ListFullBody = [], []
                ListPortraits = [File for File in list if File.startswith("Portrait")]
                ListFullBody = [File for File in list if File.startswith("FullBody")]
                ImageName = ""
                if (ImageType == "Portrait" or ListFullBody == []) and ListPortraits != []:
                    ImageName = random.choice(ListPortraits)
                if (ImageType == "FullBody" or ListPortraits == []) and  ListFullBody != []:
                    ImageName = random.choice(ListFullBody)
            elif Type == 1:
                ID = Globals.LayoutsData["DetailsUI"]["ID"]
                Name = Globals.LayoutsData["DetailsUI"]["Name"]

                NPCData = Globals.SoLNPCData[ID]

                ImageName = ""
                try:
                    Files = os.listdir( os.path.abspath( pathlib.Path() / "NPCData" / f"{Name}{ID}" ) )
                    ImageType = "Portrait"
                    list = [File for File in Files if File.endswith((".png")) or File.endswith((".jpg")) or File.endswith((".jpeg"))]
                    ListPortraits, ListFullBody = [], []
                    ListPortraits = [File for File in list if File.startswith("Portrait")]
                    ListFullBody = [File for File in list if File.startswith("FullBody")]
                    if (ImageType == "Portrait" or ListFullBody == []) and ListPortraits != []:
                        ImageName = random.choice(ListPortraits)
                    if (ImageType == "FullBody" or ListPortraits == []) and  ListFullBody != []:
                        ImageName = random.choice(ListFullBody)
                except:
                    ""

            self.setDescriptions(NPCData, ImageName)
            self.setTraits(NPCData, ImageName)
            self.setRelationships(NPCData, ImageName)

            self.MainBox.setMinimumHeight(self.GeneralWidget.height() + self.TraitsWidget.height() + self.RelationshipsWidget.height() + 20)
            self.MainBox.setMaximumHeight(self.GeneralWidget.height() + self.TraitsWidget.height() + self.RelationshipsWidget.height() + 20)

    def setDescriptions(self, NPCData, ImageName):
        ID = NPCData["ID"]
        Name = NPCData["Name"]
        Desc = Globals.References["SoLFunctions"].GetDescription
        # PSub = She He
        # PObj = Her Him
        # PPos = Her His
        # PIPos = Hers His

        ### SETTING UP THE WIDGETS
        self.GeneralWidget = QWidget()
        self.GeneralWidget.setStyleSheet('''
        .QWidget{
        background-color:rgb(23,23,23);
        }
        ''')

        self.NameLabel = QLabel(self.GeneralWidget)
        self.NameLabel.setGeometry(5,10,1014,45)
        self.NameLabel.setFont(QFont('Segoe UI', 16))
        self.NameLabel.setAlignment(Qt.AlignCenter)
        self.NameLabel.setText(NPCData["BodyData"]["FullName"])

        self.DescriptionLabel = QLabel(self.GeneralWidget)
        self.DescriptionLabel.setGeometry(5,60,1014,500)
        self.DescriptionLabel.setFont(QFont('Segoe UI', 12))
        self.DescriptionLabel.setAlignment(Qt.AlignTop)

        TotalText = ""
        if ImageName != "":
            NoPath = os.path.abspath( pathlib.Path() / "Resources" / "OtherResources" / "35.png" )

            TotalText += f'''<img src="{NoPath}" width="205" height="200" style="float: left; padding: 15px 15px;" />'''
            self.ImageLabel = QLabel(self.GeneralWidget)
            self.ImageLabel.setGeometry(10,60,200,200)
            self.ImageLabel.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "NPCData" / f"{Name}{ID}" / ImageName ) ))
            self.ImageLabel.setScaledContents(True)
            # self.ImageLabel.setText(f'''<img src="NPCData/{Name}{ID}/{ImageName}" width="200" height="200" />''')


        ### SETTING UP THE FLAVOR TEXT
        PSub, PObj, PPos, PIPos = NPCData["BodyData"]["Pronouns"]["PSub"].lower(), NPCData["BodyData"]["Pronouns"]["PObj"].lower(), NPCData["BodyData"]["Pronouns"]["PPos"].lower(), NPCData["BodyData"]["Pronouns"]["PIPos"].lower()

        FlavorText = ""
        if NPCData["Descriptions"]["Backstory"] != "":
            if FlavorText != "": FlavorText += "<br/><br/>"
            FlavorText +=  NPCData["Descriptions"]["Backstory"]

        if NPCData["Descriptions"]["Core"] != "":
            if FlavorText != "": FlavorText += "<br/><br/>"
            FlavorText += NPCData["Descriptions"]["Core"] + ". "
        FlavorText += f'''{Name} is a {Desc("Age", NPCData, "D")} {NPCData["BodyData"]["Race"].lower()} with {Desc("Skin", NPCData, "DP")}. {PSub.capitalize()} is {Desc("Height", NPCData, "D")}, with a {Desc("Complexion", NPCData, "DP")}.<br/>'''

        if NPCData["Descriptions"]["Head"] != "":
            FlavorText += NPCData["Descriptions"]["Head"] + ". "
        FlavorText += f'''{PPos.capitalize()} {Desc("FaceType", NPCData, "P")} is {Desc("FaceType", NPCData, "D")}, having {Desc("LipsSize", NPCData, "DP")} and {Desc("Eyes", NPCData, "DP")}. {PSub.capitalize()} has {Desc("Hair", NPCData, "DP")}.<br/>'''

        if NPCData["Descriptions"]["Arms"] != "":
            FlavorText += NPCData["Descriptions"]["Arms"] + ". "
        if NPCData["Descriptions"]["Legs"] != "":
            FlavorText += NPCData["Descriptions"]["Legs"] + ". "
        FlavorText += f'''{PSub.capitalize()} has {Desc("HipsSize", NPCData, "DP")} complimented by a {Desc("AssSize", NPCData, "DP")}.<br/>'''

        if NPCData["Descriptions"]["Genitals"] != "":
            FlavorText += NPCData["Descriptions"]["Genitals"] + ". "
        FlavorText += f'''{PPos.capitalize()} {Desc("ChestSize", NPCData, "P")} '''
        if NPCData["BodyData"]["Chest"] <= 1:
            FlavorText += "is"
        else:
            FlavorText += "are"
        FlavorText += f''' {Desc("ChestSize", NPCData, "D")}.  '''
        if NPCData["BodyData"]["VTightness"] > 0:
            FlavorText += f'''{PSub.capitalize()} has a '''
            if NPCData["BodyData"]["VVirgin"] == 1:
                FlavorText += f'''virgin '''
            FlavorText += f'''{Desc("VTightness", NPCData, "DP")}. '''
        if NPCData["BodyData"]["PenisSize"] > 0:
            FlavorText += f'''{PSub.capitalize()} has a '''
            if NPCData["BodyData"]["PVirgin"] == 1:
                FlavorText += f'''virgin '''
            FlavorText += f'''{Desc("PenisSize", NPCData, "DP")}. '''
        if NPCData["BodyData"]["BallsSize"] > 0:
            FlavorText += f'''{PSub.capitalize()} has {Desc("BallsSize", NPCData, "DP")}. '''

        if NPCData["BodyData"]["ATightness"] > 0:
            FlavorText += f'''{PSub.capitalize()} has a '''
            if NPCData["BodyData"]["AVirgin"] == 1:
                FlavorText += f'''virgin '''
            FlavorText += f'''{Desc("ATightness", NPCData, "DP")}. '''

        self.DescriptionLabel.setText(FlavorText)
        self.DescriptionLabel.setWordWrap(True)


        ### CLEANING THE TEXT
        OpIndices = [m.start() for m in re.finditer("<", FlavorText)]
        ClIndices = [m.start() for m in re.finditer(">", FlavorText)]
        CleanText = ""
        for i in range(len(OpIndices)):
            if i == 0:
                CleanText =  FlavorText[0:OpIndices[0]]
            else:
                try:
                    CleanText += FlavorText[ClIndices[i-1]+1:OpIndices[i]]
                except:
                    ""
        else:
            CleanText += FlavorText[ClIndices[-1]+1:]

        TempText = "" + FlavorText
        TempText = TempText.replace("<br/>", r"/n")
        OpIndices = [m.start() for m in re.finditer("<", TempText)]
        ClIndices = [m.start() for m in re.finditer(">", TempText)]
        SemiCleanText = ""
        for i in range(len(OpIndices)):
            if i == 0:
                SemiCleanText =  TempText[0:OpIndices[0]]
            else:
                try:
                    SemiCleanText += TempText[ClIndices[i-1]+1:OpIndices[i]]
                except:
                    ""
        if SemiCleanText == "":
            SemiCleanText = TempText
        BreakIndices = [m.start() for m in re.finditer(r"/n", SemiCleanText)]


        ### CALCULATING THE HEIGHT OF THE WIDGET
        MaxWidth = 802
        text = self.DescriptionLabel.text()
        f_metrics = self.DescriptionLabel.fontMetrics()
        BoundingRect = f_metrics.boundingRect(CleanText)
        FontWidth = BoundingRect.width()
        FontHeight = BoundingRect.height()
        LetterWidth = FontWidth / len(CleanText)
        PerLineS = math.floor(MaxWidth / LetterWidth)
        PerLineL = math.floor((MaxWidth + 200) / LetterWidth)
        if ImageName != "":
            PerLine = PerLineS
        else:
            PerLine = PerLineL

        Count = 0
        Lines = 0
        while True:
            if ImageName != "" and Lines * FontHeight > 200:
                PerLine = PerLineL
            if Count > len(SemiCleanText):
                break
            if len(BreakIndices) > 0 and Count + PerLine > BreakIndices[0]:
                # print(SemiCleanText[Count:BreakIndices[0]])
                Count = BreakIndices[0]
                BreakIndices.pop(0)
                Lines += 1
            else:
                # print(SemiCleanText[Count:Count+PerLine])
                Count += PerLine
                Lines += 1
        Height = (Lines+1) * FontHeight
        TotalText += FlavorText
        if Height < 200:
            Height = 200

        self.DescriptionLabel.setText(TotalText)
        self.DescriptionLabel.setMinimumHeight(Height)
        self.DescriptionLabel.setMaximumHeight(Height)

        self.GeneralWidget.setMinimumHeight(Height+50)
        self.GeneralWidget.setMaximumHeight(Height+50)

        self.MainForm.WidgetsList.append(self.GeneralWidget)
        self.MainForm.addWidget(self.GeneralWidget)

    def setTraits(self, NPCData, ImageName):
        self.TraitsWidget = QWidget()
        self.TraitsWidget.setStyleSheet('''
        .QWidget{
        background-color:rgb(23,23,23);
        }
        ''')

        self.TraitsLabel = QLabel(self.TraitsWidget)
        self.TraitsLabel.setGeometry(5,10,1014,45)
        self.TraitsLabel.setFont(QFont('Segoe UI', 16))
        self.TraitsLabel.setAlignment(Qt.AlignCenter)
        self.TraitsLabel.setText("Traits")

        TraitWidgetsDict = {}
        for TraitID in NPCData["Traits"]:
            try:
                TraitWidget = Globals.SoLTraits[TraitID]["Reference"].GetTraitStaticWidget(self, TraitID, NPCData)
                if TraitWidget == None:
                    Log(1, "ERROR RETRIEVING TRAIT STATIC WIDGET", "No widget available", TraitID, Globals.SoLTraits[TraitID]["Reference"])
                    continue
                    # raise "No widget available"
                TraitWidgetsDict[TraitID] = TraitWidget
            except Exception as e:
                Log(1, "ERROR RETRIEVING TRAIT STATIC WIDGET", e, TraitID, NPCData)


        MaxWidth = 1014
        TraitsLayout = QGridLayout()

        # Height = 0

        # TotalWidth = 0
        # TotalHeight = 0
        #
        # TempHeight = 0
        # TempWidth = 5
        #
        # Row, Layer = 0, 0
        # # self.TraitsLayout.setGeometry(QRect(5,600,1014,45))
        # for TraitID in TraitWidgetsDict:
        #     TempWidth += 5
        #     ObjectWidth = TraitWidgetsDict[TraitID].width()
        #     ObjectHeight = TraitWidgetsDict[TraitID].height()
        #
        #     if ObjectHeight > TempHeight:
        #         TempHeight = ObjectHeight
        #
        #     if TempWidth + ObjectWidth < MaxWidth:
        #         TraitsLayout.addWidget(TraitWidgetsDict[TraitID], Layer, Row)
        #         TempWidth += ObjectWidth
        #         Row += 1
        #     else:
        #         Layer += 1
        #         Row = 0
        #         TraitsLayout.addWidget(TraitWidgetsDict[TraitID], Layer, Row)
        #
        #         TempWidth = 5
        #         TotalHeight += TempHeight
        #         TempWidth += ObjectWidth
        #         Row += 1
        # else:
        #     TotalHeight += TempHeight
        #
        # if len(TraitWidgetsDict) > 0:
        #     if Layer >= 1:
        #         Width = MaxWidth
        #         Height = TotalHeight + 20
        #     else:
        #         Width = TotalWidth + 5
        #         Height = TempHeight + 20

        TraitsLayout.setContentsMargins(0, 0, 0, 0)
        Width, Height = Globals.References["SoLFunctions"].GridLayoutMaker(self, TraitsLayout, TraitWidgetsDict, MaxWidth, 10)

        self.TraitsHolder = QWidget(self.TraitsWidget)
        self.TraitsHolder.setGeometry(5,55,1014,45)
        self.TraitsHolder.setLayout(TraitsLayout)
        self.TraitsHolder.setMinimumHeight(Height)
        self.TraitsHolder.setMaximumHeight(Height)

        # self.TraitsLayout.setMinimumHeight(Height)
        # self.TraitsLayout.setMaximumHeight(Height)


        self.TraitsWidget.setMinimumHeight(Height + 60)
        self.TraitsWidget.setMaximumHeight(Height + 60)

        self.MainForm.WidgetsList.append(self.TraitsWidget)
        self.MainForm.addWidget(self.TraitsWidget)

    def setRelationships(self, NPCData, ImageName):
        try:
            self.RelationshipsWidget = QWidget()
            self.RelationshipsWidget.setProperty("Color", "Dark")

            self.RelationshipsLabel = QLabel("Relations", self.RelationshipsWidget, objectName = "Title")
            self.RelationshipsLabel.setGeometry(5,0,1014,45)
            self.RelationshipsLabel.setProperty("Color", "Light")
            self.RelationshipsLabel.setAlignment(Qt.AlignCenter)

            self.RelationLayout = QVBoxLayout()
            self.RelationHolder = QWidget(self.RelationshipsWidget, objectName = "Transparent")
            self.RelationHolder.setLayout(self.RelationLayout)
            self.RelationHolder.setGeometry(5,50,1014,0)
            self.RelationLayout.setContentsMargins(0,0,0,0)

            self.GlobalWidget = QWidget(objectName = "Transparent")
            self.GlobalLayout = QGridLayout()
            self.GlobalLayout.setContentsMargins(0,0,0,0)
            self.GlobalHolder = QWidget(self.GlobalWidget, objectName = "Transparent")
            self.GlobalHolder.setLayout(self.GlobalLayout)
            self.GlobalHolder.setGeometry(0,0,1014,0)

            self.RelationHolder.setMinimumHeight(0)
            self.RelationHolder.setMaximumHeight(0)

            if True:
                # Sets up the global values
                try:
                    GlobalsDict = {}
                    for Relation in NPCData["Relations"]:
                        for Key in NPCData["Relations"][Relation]["Permanent"]:
                            if Key not in GlobalsDict:
                                GlobalsDict[Key] = NPCData["Relations"][Relation]["Permanent"][Key]
                            else:
                                GlobalsDict[Key] += NPCData["Relations"][Relation]["Permanent"][Key]
                    if "Attraction" in GlobalsDict:
                        GlobalsDict.pop("Attraction")
                    if "Reliability" in GlobalsDict:
                        GlobalsDict.pop("Reliability")

                    GlobalWidgetsDict = {}
                    for ValueID in GlobalsDict:
                        Object = ValueWidget(ValueID, GlobalsDict[ValueID])
                        Widget = Object.GetWidget()
                        if Widget != None:
                            GlobalWidgetsDict[ValueID] = Widget

                    MaxWidth = 1014
                    Width, Height = Globals.References["SoLFunctions"].GridLayoutMaker(self, self.GlobalLayout, GlobalWidgetsDict, MaxWidth, 10)

                    self.GlobalHolder.setMinimumHeight(Height)
                    self.GlobalHolder.setMaximumHeight(Height)
                    self.GlobalHolder.setMinimumWidth(Width)
                    self.GlobalHolder.setMaximumWidth(Width)

                except Exception as e:
                    Log(2, "ERROR SETT UP GLOBAL PERMANENT VALUES", e)

            self.GlobalWidget.setMinimumHeight(self.GlobalHolder.height())
            self.GlobalWidget.setMaximumHeight(self.GlobalHolder.height())
            self.GlobalWidget.setMinimumWidth(1014)
            self.GlobalWidget.setMaximumWidth(1014)
            # self.GlobalWidget.setStyleSheet('''background-color:rgb(0,0,255)''')

            self.RelationHolder.setMinimumHeight(self.RelationHolder.height() + self.GlobalWidget.height() + 5)
            self.RelationHolder.setMaximumHeight(self.RelationHolder.height() + self.GlobalWidget.height() + 5)

            self.RelationLayout.addWidget(self.GlobalWidget)

            # GLOBALS
            # RELATION
            ## PERMANENT
            ## ABILITIES
            ## FALLEN STATE



            if len(NPCData["Relations"]) > 0:
                def setRelation():
                    self.RelationHolder.setMinimumHeight(50 + self.GlobalWidget.height() + 5)
                    self.RelationHolder.setMaximumHeight(50 + self.GlobalWidget.height() + 5)

                    Key = self.RelationPicker.currentText()
                    self.RelationNPCLabel.setText(f'''{Key}''')
                    RelationData = self.RelationPicker.Data[Key]

                    ### PERMANENT
                    try:
                        for Widget in self.PermanentLayout.WidgetsList:
                            self.PermanentLayout.removeWidget(Widget)
                    except:
                        ""
                    self.PermanentLayout.WidgetsList = []

                    PermanentDict = {}
                    for PermanentID in RelationData["Permanent"]:
                        PermanentDict[PermanentID] = RelationData["Permanent"][PermanentID]

                    PermanentWidgetsDict = {}
                    for ValueID in PermanentDict:
                        Object = ValueWidget(ValueID, PermanentDict[ValueID])
                        Widget = Object.GetWidget()
                        if Widget != None:
                            PermanentWidgetsDict[ValueID] = Widget
                            self.PermanentLayout.WidgetsList.append(Widget)

                    MaxWidth = 1014
                    Width, Height = Globals.References["SoLFunctions"].GridLayoutMaker(self, self.PermanentLayout, PermanentWidgetsDict, MaxWidth, 10)
                    self.PermanentHolder.setMinimumWidth(Width)
                    self.PermanentHolder.setMaximumWidth(Width)
                    self.PermanentHolder.setMinimumHeight(Height)
                    self.PermanentHolder.setMaximumHeight(Height)

                    self.PermanentWidget.setMinimumWidth(MaxWidth)
                    self.PermanentWidget.setMaximumWidth(MaxWidth)
                    self.PermanentWidget.setMinimumHeight(Height+45)
                    self.PermanentWidget.setMaximumHeight(Height+45)


                    ### ABILITIES
                    try:
                        for Widget in self.AbilitiesLayout.WidgetsList:
                            self.AbilitiesLayout.removeWidget(Widget)
                    except:
                        ""
                    self.AbilitiesLayout.WidgetsList = []


                    AbilitiesWidgetsDict = {}
                    for AbilityID in Globals.SoLAbilities:
                        if AbilityID in RelationData["Abilities"]:
                            Data = RelationData["Abilities"][AbilityID]
                        else:
                            Data = {}
                        Widget = Globals.SoLAbilities[AbilityID]["Reference"].GetAbilityStaticWidget(AbilityID, Data)
                        if Widget != None:
                            AbilitiesWidgetsDict[AbilityID] = Widget
                            self.AbilitiesLayout.WidgetsList.append(Widget)

                    MaxWidth = 1014
                    Width, Height = Globals.References["SoLFunctions"].GridLayoutMaker(self, self.AbilitiesLayout, AbilitiesWidgetsDict, MaxWidth, 10)
                    self.AbilitiesHolder.setMinimumWidth(Width)
                    self.AbilitiesHolder.setMaximumWidth(Width)
                    self.AbilitiesHolder.setMinimumHeight(Height)
                    self.AbilitiesHolder.setMaximumHeight(Height)

                    self.AbilitiesWidget.setMinimumWidth(MaxWidth)
                    self.AbilitiesWidget.setMaximumWidth(MaxWidth)
                    self.AbilitiesWidget.setMinimumHeight(Height+45)
                    self.AbilitiesWidget.setMaximumHeight(Height+45)
                    #
                    #
                    ### FALLEN STATES
                    try:
                        for Widget in self.FallenLayout.WidgetsList:
                            self.FallenLayout.removeWidget(Widget)
                    except:
                        ""
                    self.FallenLayout.WidgetsList = []

                    FallenWidgetsDict = {}
                    for FallenID in Globals.SoLFallenStates:
                        if FallenID in RelationData["FallenData"]:
                            FallenData = RelationData["FallenData"][FallenID]
                        else:
                            FallenData = {}
                        Widget = Globals.SoLFallenStates[FallenID]["Reference"].GetStaticFallenWidget(FallenID, FallenData, RelationData)
                        if Widget != None:
                            FallenWidgetsDict[FallenID] = Widget
                            self.AbilitiesLayout.WidgetsList.append(Widget)
                            # self.FallenLayout.WidgetList.append(Widget)

                    MaxWidth = 1014
                    Width, Height = Globals.References["SoLFunctions"].GridLayoutMaker(self, self.FallenLayout, FallenWidgetsDict, MaxWidth, 10)
                    self.FallenHolder.setMinimumWidth(Width)
                    self.FallenHolder.setMaximumWidth(Width)
                    self.FallenHolder.setMinimumHeight(Height)
                    self.FallenHolder.setMaximumHeight(Height)

                    self.FallenWidget.setMinimumWidth(MaxWidth)
                    self.FallenWidget.setMaximumWidth(MaxWidth)
                    self.FallenWidget.setMinimumHeight(Height+50)
                    self.FallenWidget.setMaximumHeight(Height+50)
                    #
                    #
                    #
                    #
                    #
                    #
                    if self.PermanentWidget.height() != 0:
                        self.RelationLayout.addWidget(self.PermanentWidget)
                        self.RelationHolder.setMinimumHeight(self.RelationHolder.height() + self.PermanentWidget.height() + 5)
                        self.RelationHolder.setMaximumHeight(self.RelationHolder.height() + self.PermanentWidget.height() + 5)
                    if self.AbilitiesWidget.height() != 0:
                        self.RelationLayout.addWidget(self.AbilitiesWidget)
                        self.RelationHolder.setMinimumHeight(self.RelationHolder.height() + self.AbilitiesWidget.height() + 5)
                        self.RelationHolder.setMaximumHeight(self.RelationHolder.height() + self.AbilitiesWidget.height() + 5)
                    if self.FallenWidget.height() != 0:
                        self.RelationLayout.addWidget(self.FallenWidget)
                        self.RelationHolder.setMinimumHeight(self.RelationHolder.height() + self.FallenWidget.height() + 5)
                        self.RelationHolder.setMaximumHeight(self.RelationHolder.height() + self.FallenWidget.height() + 5)
                    # Height = self.PermanentWidget.height() + self.AbilitiesWidget.height() + self.FallenWidget.height() + 50
                    # self.RelationLayout.setMinimumHeight(Height + 50)
                    # self.RelationLayout.setMaximumHeight(Height + 50)

                    # self.RelationshipsWidget.setMinimumHeight(self.RelationLayout.height() + 50)
                    # self.RelationshipsWidget.setMaximumHeight(self.RelationLayout.height() + 50)

                ##
                self.RelationPickerWidget = QWidget(objectName = "Transparent")
                self.RelationNPCLabel = QLabel(self.RelationPickerWidget, objectName = "SubTitle")
                self.RelationNPCLabel.setGeometry(0, 0, 1014, 45)
                self.RelationNPCLabel.setProperty("Color", "Light")
                self.RelationNPCLabel.setAlignment(Qt.AlignCenter)

                self.RelationPicker = QComboBox(self.RelationPickerWidget)
                self.RelationPicker.setGeometry(804,5,200,35)
                self.RelationPicker.setFont(QFont('Segoe UI', 12))
                self.RelationPicker.currentIndexChanged.connect(setRelation)
                self.RelationPicker.Data = {}

                self.RelationPickerWidget.setMinimumWidth(1014)
                self.RelationPickerWidget.setMaximumWidth(1014)
                self.RelationPickerWidget.setMinimumHeight(45)
                self.RelationPickerWidget.setMaximumHeight(45)

                self.RelationLayout.addWidget(self.RelationPickerWidget)
                self.RelationHolder.setMinimumHeight(self.RelationHolder.height() + self.RelationPickerWidget.height() + 5)
                self.RelationHolder.setMaximumHeight(self.RelationHolder.height() + self.RelationPickerWidget.height() + 5)
                # self.RelationPickerWidget.setStyleSheet('''background-color:rgb(255,255,0)''')
                ##

                self.PermanentWidget = QWidget(objectName = "Transparent")
                self.PermanentLabel = QLabel("Permanent", self.PermanentWidget, objectName = "SubTitle")
                self.PermanentLabel.setGeometry(0,0,1014,45)
                self.PermanentLabel.setProperty("Color", "Light")
                self.PermanentLabel.setAlignment(Qt.AlignCenter)
                self.PermanentLayout = QGridLayout()
                self.PermanentLayout.setContentsMargins(0,0,0,0)
                self.PermanentHolder = QWidget(self.PermanentWidget, objectName = "Transparent")
                self.PermanentHolder.setGeometry(0,45,1014,0)
                self.PermanentHolder.setLayout(self.PermanentLayout)
                # self.PermanentWidget.setStyleSheet('''background-color:rgb(255,0,255)''')
                #
                self.AbilitiesWidget = QWidget(objectName = "Transparent")
                self.AbilitiesLabel = QLabel("Abilities", self.AbilitiesWidget, objectName = "SubTitle")
                self.AbilitiesLabel.setGeometry(0,0,1014,45)
                self.AbilitiesLabel.setProperty("Color", "Light")
                self.AbilitiesLabel.setAlignment(Qt.AlignCenter)
                self.AbilitiesLayout = QGridLayout()
                self.AbilitiesLayout.setContentsMargins(0,0,0,0)
                self.AbilitiesHolder = QWidget(self.AbilitiesWidget, objectName = "Transparent")
                self.AbilitiesHolder.setGeometry(0,45,1014,0)
                self.AbilitiesHolder.setLayout(self.AbilitiesLayout)
                # self.AbilitiesWidget.setStyleSheet('''background-color:rgb(0,255,255)''')
                #
                self.FallenWidget = QWidget(objectName = "Transparent")
                self.FallenLabel = QLabel("Fallen", self.FallenWidget, objectName = "SubTitle")
                self.FallenLabel.setGeometry(0,0,1014,45)
                self.FallenLabel.setProperty("Color", "Light")
                self.FallenLabel.setAlignment(Qt.AlignCenter)
                self.FallenLayout = QGridLayout()
                self.FallenLayout.setContentsMargins(0,0,0,0)
                self.FallenHolder = QWidget(self.FallenWidget, objectName = "Transparent")
                self.FallenHolder.setGeometry(0,45,1014,0)
                self.FallenHolder.setLayout(self.FallenLayout)
                # self.FallenWidget.setStyleSheet('''background-color:rgb(255,255,255)''')

                for NPCID in NPCData["Relations"]:
                    RelationData = NPCData["Relations"][NPCID]
                    try:
                        OtherName = Globals.SoLNPCData[NPCID]["Name"]
                        OtherID = Globals.SoLNPCData[NPCID]["ID"]
                        self.RelationPicker.Data[f'''{OtherName} {OtherID}'''] = RelationData
                        self.RelationPicker.addItem(f'''{OtherName} {OtherID}''')
                    except Exception as e:
                        ""

            # self.RelationHolder.setStyleSheet('''background-color:rgb(0,255,0)''')
            # self.RelationshipsWidget.setStyleSheet('''background-color:rgb(255,0,0)''')

            self.RelationshipsWidget.setMinimumHeight(self.RelationHolder.height() + 50)
            self.RelationshipsWidget.setMaximumHeight(self.RelationHolder.height() + 50)
            # self.RelationshipsWidget.setMinimumHeight(self.RelationshipsWidget.height() + 500)
            # self.RelationshipsWidget.setMaximumHeight(self.RelationshipsWidget.height() + 500)

            self.MainForm.WidgetsList.append(self.RelationshipsWidget)
            self.MainForm.addWidget(self.RelationshipsWidget)

        except Exception as e:
            print("ERR", e)

    def setRelationships2(self, NPCData, ImageName):
        self.RelationshipsWidget = QWidget()
        self.RelationshipsWidget.setStyleSheet('''
        .QWidget{
        background-color:rgb(23,23,23);
        }
        ''')


        self.GlobalWidget = QWidget(self.RelationshipsWidget)
        self.RelationshipsLabel = QLabel(self.GlobalWidget)
        self.RelationshipsLabel.setGeometry(5,0,1014,45)
        self.RelationshipsLabel.setFont(QFont('Segoe UI', 16))
        self.RelationshipsLabel.setAlignment(Qt.AlignCenter)
        self.RelationshipsLabel.setText("Relations")

        self.RelationshipsWidget.GlobalHeight = 0
        PermanentDict = {}
        for NPCID in NPCData["Relations"]:
            for PermanentID in NPCData["Relations"][NPCID]["Permanent"]:
                if PermanentID not in PermanentDict:
                    PermanentDict[PermanentID] = NPCData["Relations"][NPCID]["Permanent"][PermanentID]
                else:
                    PermanentDict[PermanentID] += NPCData["Relations"][NPCID]["Permanent"][PermanentID]
        if "Attraction" in PermanentDict:
            PermanentDict.pop("Attraction")
        if "Reliability" in PermanentDict:
            PermanentDict.pop("Reliability")


        WidgetsDict = {}
        for ValueID in PermanentDict:
            Object = ValueWidget(ValueID, PermanentDict[ValueID])
            Widget = Object.GetWidget()
            if Widget != None:
                WidgetsDict[ValueID] = Widget


        MaxWidth = 1014

        self.GlobalLayout = QGridLayout()


        Width, Height = Globals.References["SoLFunctions"].GridLayoutMaker(self, self.GlobalLayout, WidgetsDict, MaxWidth, 10)

        self.GlobalValuesHolder = QWidget(self.GlobalWidget)
        self.GlobalValuesHolder.setGeometry(5,50,1014,45)
        self.GlobalValuesHolder.setLayout(self.GlobalLayout)
        self.GlobalValuesHolder.setMinimumHeight(Height)
        self.GlobalValuesHolder.setMaximumHeight(Height)
        self.GlobalValuesHolder.setMinimumWidth(Width)
        self.GlobalValuesHolder.setMaximumWidth(Width)


        Height += 50
        self.GlobalWidget.setMinimumHeight(Height)
        self.GlobalWidget.setMaximumHeight(Height)
        self.GlobalWidget.setMinimumWidth(MaxWidth)
        self.GlobalWidget.setMaximumWidth(MaxWidth)

        if len(NPCData["Relations"]) > 0:
            self.RelationWidget = QWidget()

            self.RelationLabel = QLabel(self.RelationshipsWidget, objectName = "Title")
            self.RelationLabel.setGeometry(0,0,1014,45)
            self.RelationLabel.setAlignment(Qt.AlignCenter)



            # self.RelationLabel = QLabel(self.RelationshipsWidget, objectName = "Title")
            # self.RelationLabel.setGeometry(5,Height+20,1014,45)
            # self.RelationLabel.setFont(QFont('Segoe UI', 16))
            # self.RelationLabel.setAlignment(Qt.AlignCenter)
            # self.RelationLabel.setText("NPCName")

            def setRelation():
                try:
                    ### PERMANENT VALUES
                    Key = self.RelationBox.currentText()
                    self.RelationLabel.setText(f'''{Key}''')

                    RelationData = self.RelationBox.Data[Key]
                    try:
                        for Widget in self.PartialValuesLayout.WidgetList:
                            self.PartialValuesLayout.removeWidget(Widget)
                    except Exception as e:
                        ""
                    self.PartialValuesLayout.WidgetList = []

                    PermanentDict = {}
                    for PermanentID in RelationData["Permanent"]:
                        PermanentDict[PermanentID] = RelationData["Permanent"][PermanentID]

                    WidgetsDict = {}
                    for ValueID in PermanentDict:
                        Object = ValueWidget(ValueID, PermanentDict[ValueID])
                        Widget = Object.GetWidget()
                        if Widget != None:
                            WidgetsDict[ValueID] = Widget
                            self.PartialValuesLayout.WidgetList.append(Widget)

                    MaxWidth = 1014
                    Width, Height = Globals.References["SoLFunctions"].GridLayoutMaker(self, self.PartialValuesLayout, WidgetsDict, MaxWidth, 10)

                    self.PartialValuesHolder.setMinimumHeight(Height)
                    self.PartialValuesHolder.setMaximumHeight(Height)
                    self.PartialValuesHolder.setMinimumWidth(Width)
                    self.PartialValuesHolder.setMaximumWidth(Width)

                    self.PermanentWidget.setMinimumHeight(Height+55)
                    self.PermanentWidget.setMaximumHeight(Height+55)
                    self.PermanentWidget.setMinimumWidth(MaxWidth)
                    self.PermanentWidget.setMaximumWidth(MaxWidth)

                    ### ABILITIES
                    try:
                        for Widget in self.PartialAbilitiesLayout.WidgetList:
                            self.PartialAbilitiesLayout.removeWidget(Widget)
                    except:
                        ""
                    self.PartialAbilitiesLayout.WidgetList = []
                    WidgetsDict = {}
                    for AbilityID in Globals.SoLAbilities:
                        try:
                            if AbilityID in RelationData["Abilities"]:
                                Data = RelationData["Abilities"][AbilityID]
                            else:
                                Data = {}
                            Widget = Globals.SoLAbilities[AbilityID]["Reference"].GetAbilityStaticWidget(AbilityID, Data)
                            if Widget != None:
                                WidgetsDict[AbilityID] = Widget
                                self.PartialAbilitiesLayout.WidgetList.append(Widget)
                            else:
                                Log(2, "UNABLE TO RETRIEVE ABILITY STATIC WIDGET", AbilityID, Data, NPCData)
                        except Exception as e:
                            Log(2, "ERROR RETRIEVING ABILITY STATIC WIDGET", e, AbilityID, NPCData)

                    MaxWidth = 1014
                    Width, Height = Globals.References["SoLFunctions"].GridLayoutMaker(self, self.PartialAbilitiesLayout, WidgetsDict, MaxWidth, 10)

                    self.PartialAbilitiesHolder.setMinimumHeight(Height)
                    self.PartialAbilitiesHolder.setMaximumHeight(Height)
                    self.PartialAbilitiesHolder.setMinimumWidth(Width)
                    self.PartialAbilitiesHolder.setMaximumWidth(Width)

                    self.AbilitiesWidget.setMinimumHeight(Height+55)
                    self.AbilitiesWidget.setMaximumHeight(Height+55)
                    self.AbilitiesWidget.setMinimumWidth(MaxWidth)
                    self.AbilitiesWidget.setMaximumWidth(MaxWidth)


                    ### FALLEN STATES
                    try:
                        for Widget in self.FallenLayout.WidgetList:
                            self.FallenLayout.removeWidget(Widget)
                    except:
                        ""
                    self.FallenLayout.WidgetList = []
                    WidgetsDict = {}
                    for FallenID in Globals.SoLFallenStates:
                        try:
                            # if FallenID in RelationData["FallenData"]:
                            if False:
                                FallenData = RelationData["FallenData"][FallenID]
                            else:
                                FallenData = {}
                            Widget = Globals.SoLFallenStates[FallenID]["Reference"].GetStaticFallenWidget(FallenID, FallenData, RelationData)
                            if Widget != None:
                                WidgetsDict[FallenID] = Widget
                                self.FallenLayout.WidgetList.append(Widget)
                            else:
                                Log(2, "UNABLE TO RETRIEVE FALLEN STATIC WIDGET", FallenID, FallenData, NPCData)
                        except Exception as e:
                            Log(2, "ERROR RETRIEVING FALLEN STATIC WIDGET", e, FallenID, NPCData)

                    MaxWidth = 1014
                    Width, Height = Globals.References["SoLFunctions"].GridLayoutMaker(self, self.FallenLayout, WidgetsDict, MaxWidth, 10)

                    self.FallenLayoutHolder.setMinimumHeight(Height)
                    self.FallenLayoutHolder.setMaximumHeight(Height)
                    self.FallenLayoutHolder.setMinimumWidth(Width)
                    self.FallenLayoutHolder.setMaximumWidth(Width)

                    self.FallenWidget.setMinimumHeight(Height+555)
                    self.FallenWidget.setMaximumHeight(Height+555)
                    self.FallenWidget.setMinimumWidth(MaxWidth)
                    self.FallenWidget.setMaximumWidth(MaxWidth)

                    self.FallenWidget.setStyleSheet('''background-color:rgb(255,0,0) ''')



                    YLocation = self.GlobalWidget.height() + 70
                    self.PermanentWidget.setGeometry(5,YLocation,0,0)

                    YLocation = self.GlobalWidget.height() + self.PermanentWidget.height() + 70
                    self.AbilitiesWidget.setGeometry(5,YLocation,0,0)

                    YLocation = self.GlobalWidget.height() + self.PermanentWidget.height() + self.AbilitiesWidget.height() + 70
                    self.FallenWidget.setGeometry(5,YLocation,0,0)

                    self.RelationshipsWidget.setMinimumHeight(self.GlobalWidget.height() + self.PermanentWidget.height() + self.AbilitiesWidget.height() + self.FallenWidget.height() + 630)
                    self.RelationshipsWidget.setMaximumHeight(self.GlobalWidget.height() + self.PermanentWidget.height() + self.AbilitiesWidget.height() + self.FallenWidget.height() + 630)
                    self.PermanentLabel.raise_()


                except Exception as e:
                    print("ERROR SET RELATION", e)
                    ""


            self.RelationBox = QComboBox(self.RelationshipsWidget)
            self.RelationBox.setGeometry(804,Height + 25,200,35)
            self.RelationBox.setFont(QFont('Segoe UI', 12))
            self.RelationBox.currentIndexChanged.connect(setRelation)
            self.RelationBox.Data = {}


            self.PermanentWidget = QWidget(self.RelationshipsWidget)

            self.PermanentLabel = QLabel(self.PermanentWidget)
            self.PermanentLabel.setGeometry(5,5,1004,35)
            self.PermanentLabel.setFont(QFont('Segoe UI', 14))
            self.PermanentLabel.setAlignment(Qt.AlignCenter)
            self.PermanentLabel.setText("Permanent")

            self.PartialValuesLayout = QGridLayout()
            self.PartialValuesHolder = QWidget(self.PermanentWidget)
            self.PartialValuesHolder.setLayout(self.PartialValuesLayout)
            self.PartialValuesHolder.setGeometry(0,40,0,0)


            self.AbilitiesWidget = QWidget(self.RelationshipsWidget)

            self.AbilitiesLabel = QLabel(self.AbilitiesWidget)
            self.AbilitiesLabel.setGeometry(5,5,1004,35)
            self.AbilitiesLabel.setFont(QFont('Segoe UI', 14))
            self.AbilitiesLabel.setAlignment(Qt.AlignCenter)
            self.AbilitiesLabel.setText("Abilities")

            self.PartialAbilitiesLayout = QGridLayout()
            self.PartialAbilitiesHolder = QWidget(self.AbilitiesWidget)
            self.PartialAbilitiesHolder.setLayout(self.PartialAbilitiesLayout)
            self.PartialAbilitiesHolder.setGeometry(0,40,0,0)


            self.FallenWidget = QWidget(self.RelationshipsWidget)

            self.FallenLabel = QLabel(self.FallenWidget)
            self.FallenLabel.setGeometry(5,5,1004,35)
            self.FallenLabel.setFont(QFont('Segoe UI', 14))
            self.FallenLabel.setAlignment(Qt.AlignCenter)
            self.FallenLabel.setText("Fallen States")

            self.FallenLayout = QGridLayout()
            self.FallenLayoutHolder = QWidget(self.FallenWidget)
            self.FallenLayoutHolder.setLayout(self.FallenLayout)
            self.FallenLayoutHolder.setGeometry(0,40,0,0)



            for NPCID in NPCData["Relations"]:
                RelationData = NPCData["Relations"][NPCID]
                try:
                    OtherName = Globals.SoLNPCData[NPCID]["Name"]
                    OtherID = Globals.SoLNPCData[NPCID]["ID"]
                    self.RelationBox.Data[f'''{OtherName} {OtherID}'''] = RelationData
                    self.RelationBox.addItem(f'''{OtherName} {OtherID}''')
                except Exception as e:
                    print(e)
                    OtherID = NPCID
                    self.RelationBox.addItem(f'''{OtherID}''')
                    self.RelationBox.Data[f'''{OtherID}'''] = RelationData



            Height = self.GlobalWidget.height() + self.PermanentWidget.height() + self.AbilitiesWidget.height()
            if Height != 0:
                print("oh", self.GlobalWidget.height(), self.PermanentWidget.height(), self.AbilitiesWidget.height())
                Height += 110
            self.RelationshipsWidget.setMinimumHeight(Height)
            self.RelationshipsWidget.setMaximumHeight(Height)
        else:
            self.RelationshipsWidget.setMaximumHeight(50)
            self.RelationshipsWidget.setMinimumHeight(50)
            # self.RelationshipsWidget.setStyleSheet('''background-color:rgb(255,0,0) ''')
        self.MainForm.WidgetsList.append(self.RelationshipsWidget)
        self.MainForm.addWidget(self.RelationshipsWidget)


def Initialize(self, Reference):
    if "DetailsUI" not in Globals.Layouts:
        Object = UiLayoutDetailsMenu()
