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
Log = Globals.Layouts["MainF"].Log

class UiLayoutEnhanceMenu:
    def __init__(self):
        Globals.Layouts["EnhanceUI"] = self
        Globals.LayoutsData["EnhanceUI"] = {"Source":"enhanceMenuUI", "Initialized":0, "TargetID":None, "ActorID":None}

    def UI(self):
        MainWindow = Globals.Layouts["MainF"]
        self.GUI = QWidget(MainWindow)

        self.LabelBack = QLabel(self.GUI)
        self.LabelBack.setGeometry(288,5,1024,954)
        self.LabelBack.setProperty("Color","Dark")

        self.MainScroll = QScrollArea(self.GUI)
        self.MainScroll.setGeometry(288,10,1024,944)
        self.MainScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.MainScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.MainForm = QVBoxLayout()
        self.MainBox = QGroupBox()
        self.MainBox.setLayout(self.MainForm)
        self.MainBox.setMinimumWidth(1024)
        self.MainScroll.setWidget(self.MainBox)
        self.MainForm.setContentsMargins(0, 0, 0, 5)
        self.MainForm.WidgetsList = []


        self.LabelControl = QLabel(self.GUI)
        self.LabelControl.setGeometry(5,964,1592,55)
        self.LabelControl.setProperty("Color","Dark")

        self.ButtonMenu = QPushButton("Back", self.GUI, clicked = lambda: MainWindow.gotoPreviousLayout())
        self.ButtonMenu.setGeometry(15,970,200,45)
        self.ButtonMenu.setProperty("Color","Light")
        # Globals.LayoutsData["EnhanceUI"]["TargetID"] = "02"
        # Globals.LayoutsData["EnhanceUI"]["ActorID"] = "0"
        # print(Globals.SoLNPCData["0"]["Relations"])

    def Refresh(self):
        if Globals.LayoutsData["EnhanceUI"]["TargetID"] != None and Globals.LayoutsData["EnhanceUI"]["ActorID"] != None:
            # Globals.LayoutsData["EnhanceUI"] = {"Source":"enhanceMenuUI", "Initialized":0, "TargetID":None, "ActorID":None}
            Target = Globals.LayoutsData["EnhanceUI"]["TargetID"]
            Actor = Globals.LayoutsData["EnhanceUI"]["ActorID"]

            TargetData = Globals.SoLNPCData[Target]
            ActorData = Globals.SoLNPCData[Actor]

            TARelation = TargetData["Relations"][Actor]
            ATRelation = ActorData["Relations"][Target]


            for Widget in self.MainForm.WidgetsList:
                try:
                    Widget.hide()
                    self.MainForm.WidgetsList.removeWidget(Widget)
                except:
                    ""
            self.MainForm.WidgetsList = []

            def setPermanent(self):
                self.PWidget = QWidget(objectName = "Transparent")
                self.PWidget.Status = "Open"

                self.PLabel = QLabel("Permanent Values", self.PWidget, objectName = "SubTitle")
                self.PLabel.setProperty("Color","Light")
                self.PLabel.setGeometry(15,0,979,40)
                self.PLabel.setAlignment(Qt.AlignCenter)

                def POpenClose():
                    if self.PWidget.Status == "Open":
                        TotalHeight = 45
                        self.PWidget.setMaximumHeight(TotalHeight)
                        self.PWidget.setMinimumHeight(TotalHeight)

                        Height = self.MainBox.height() - self.PWidget.height() + TotalHeight
                        self.MainBox.setMinimumHeight(Height)
                        self.MainBox.setMaximumHeight(Height)

                        self.PCloser.setStyleSheet("border-image: url(images/SoLResources/Down.png); ")
                        self.PWidget.Status = "Closed"
                    elif self.PWidget.Status == "Closed":
                        TotalHeight = self.PWidget.TotalHeight
                        self.PWidget.setMaximumHeight(TotalHeight)
                        self.PWidget.setMinimumHeight(TotalHeight)

                        Height = self.MainBox.height() - 45 + TotalHeight
                        self.MainBox.setMinimumHeight(Height)
                        self.MainBox.setMaximumHeight(Height)

                        self.PCloser.setStyleSheet("border-image: url(images/SoLResources/Up.png); ")
                        self.PWidget.Status = "Open"
                self.PCloser = QPushButton(self.PWidget, clicked = lambda: POpenClose())
                self.PCloser.setProperty("Color","Light")
                self.PCloser.setGeometry(950,5,30,30)
                self.PCloser.setStyleSheet("border-image: url(images/SoLResources/Up.png); ")


                self.PLayout = QGridLayout()
                self.PLayout.setContentsMargins(5, 5, 5, 5)
                self.PLayout.WidgetsList = []
                self.PHolder = QWidget(self.PWidget, objectName = "Transparent")
                self.PHolder.setLayout(self.PLayout)

                FullPValuesList = list(set( list(Globals.SoLPValues.keys()) + list(TARelation["Permanent"].keys()) ))

                WidgetsDict = {}
                for PermanentID in FullPValuesList:
                    try:
                        if PermanentID in Globals.SoLPValues:
                            Value = None
                            if PermanentID in TARelation["Permanent"]:
                                Value = TARelation["Permanent"][PermanentID]
                            Widget = Globals.SoLPValues[PermanentID]["Reference"].GetPValueStaticWidget(PermanentID, Value)
                        else:
                            Value = None
                            if PermanentID in TARelation["Permanent"]:
                                Value = TARelation["Permanent"][PermanentID]
                            Widget = Globals.References["SoLFunctions"].GetPValueStaticWidget(PermanentID, Value)

                        if Widget != None:
                            WidgetsDict[PermanentID] = Widget
                    except:
                        ""
                MaxWidth = 994
                Width, Height = Globals.References["SoLFunctions"].GridLayoutMaker(self, self.PLayout, WidgetsDict, MaxWidth, 5)

                self.PHolder.setGeometry(15,45,Width,Height)
                TotalHeight = Height + 45
                self.PWidget.TotalHeight = TotalHeight
                self.PWidget.setMaximumHeight(TotalHeight)
                self.PWidget.setMinimumHeight(TotalHeight)
                self.PWidget.setMaximumWidth(MaxWidth)
                self.PWidget.setMinimumWidth(MaxWidth)

                self.MainForm.addWidget(self.PWidget)
                self.MainForm.WidgetsList.append(self.PWidget)

                Height = self.MainBox.height() + self.PWidget.height()+10
                self.MainBox.setMinimumHeight(Height)
                self.MainBox.setMaximumHeight(Height)

                # if len(WidgetsDict) > 0:
                #     Height = 0
                #     MaxWidth = 1014
                #
                #     TotalWidth = 0
                #     TotalHeight = 0
                #
                #     TempHeight = 0
                #     TempWidth = 5
                #
                #     Row, Layer = 0, 0
                #     for ValueID in WidgetsDict:
                #         TempWidth += 5
                #         ObjectWidth = WidgetsDict[ValueID].width()
                #         ObjectHeight = WidgetsDict[ValueID].height()
                #
                #         if ObjectHeight > TempHeight:
                #             TempHeight = ObjectHeight
                #
                #         if TempWidth + ObjectWidth < MaxWidth:
                #             self.PLayout.addWidget(WidgetsDict[ValueID], Layer, Row)
                #             TempWidth += ObjectWidth
                #             Row += 1
                #         else:
                #             Layer += 1
                #             Row = 0
                #             self.PLayout.addWidget(WidgetsDict[ValueID], Layer, Row)
                #
                #             TempWidth = 5
                #             TotalHeight += TempHeight
                #             TempWidth += ObjectWidth
                #             Row += 1
                #     else:
                #         TotalHeight += TempHeight
                #
                #     if Layer >= 1:
                #         Width = MaxWidth
                #         Height = TotalHeight
                #     else:
                #         Width = TempWidth + 5
                #         Height = TempHeight
                #
                #     self.PHolder.setGeometry(5,45,Width,Height)
                #     TotalHeight = Height + 45
                #     self.PWidget.setMaximumHeight(TotalHeight)
                #     self.PWidget.setMinimumHeight(TotalHeight)
                #     self.PWidget.setMaximumWidth(MaxWidth)
                #     self.PWidget.setMinimumWidth(MaxWidth)
                #
                #
                #     self.MainForm.addWidget(self.PWidget)
                #     self.MainForm.WidgetsList.append(self.PWidget)
                #
                #     Height = self.MainBox.height() + self.PWidget.height() + 10
                #     self.MainBox.setMinimumHeight(Height)
                #     self.MainBox.setMaximumHeight(Height)

            def setTemporal(self):
                self.TWidget = QWidget(objectName = "Transparent")
                self.TWidget.Status = "Open"

                self.TLabel = QLabel("Temporal Values", self.TWidget, objectName = "SubTitle")
                self.TLabel.setProperty("Color","Light")
                self.TLabel.setGeometry(15,0,979,40)
                self.TLabel.setAlignment(Qt.AlignCenter)

                def TOpenClose():
                    if self.TWidget.Status == "Open":
                        TotalHeight = 45
                        self.TWidget.setMaximumHeight(TotalHeight)
                        self.TWidget.setMinimumHeight(TotalHeight)

                        Height = self.MainBox.height() - self.TWidget.height() + TotalHeight
                        self.MainBox.setMinimumHeight(Height)
                        self.MainBox.setMaximumHeight(Height)

                        self.TCloser.setStyleSheet("border-image: url(images/SoLResources/Down.png); ")
                        self.TWidget.Status = "Closed"
                    elif self.TWidget.Status == "Closed":
                        TotalHeight = self.TWidget.TotalHeight
                        self.TWidget.setMaximumHeight(TotalHeight)
                        self.TWidget.setMinimumHeight(TotalHeight)

                        Height = self.MainBox.height() - 45 + TotalHeight
                        self.MainBox.setMinimumHeight(Height)
                        self.MainBox.setMaximumHeight(Height)

                        self.TCloser.setStyleSheet("border-image: url(images/SoLResources/Up.png); ")
                        self.TWidget.Status = "Open"
                self.TCloser = QPushButton(self.TWidget, clicked = lambda: TOpenClose())
                self.TCloser.setProperty("Color","Light")
                self.TCloser.setGeometry(950,5,30,30)
                self.TCloser.setStyleSheet("border-image: url(images/SoLResources/Up.png); ")



                self.TLayout = QGridLayout()
                self.TLayout.setContentsMargins(5, 5, 5, 5)
                self.TLayout.WidgetsList = []
                self.THolder = QWidget(self.TWidget, objectName = "Transparent")
                self.THolder.setLayout(self.TLayout)

                FullTValuesList = list(set( list(Globals.SoLTValues.keys()) + list(TARelation["Temporal"].keys()) ))

                WidgetsDict = {}
                for TemporalID in FullTValuesList:
                    try:
                        if TemporalID in Globals.SoLTValues:
                            Value = None
                            if TemporalID in TARelation["Temporal"]:
                                Value = TARelation["Temporal"][TemporalID]
                            Widget = Globals.SoLTValues[TemporalID]["Reference"].GetTValueStaticWidget(TemporalID, Value)
                        else:
                            Value = None
                            if TemporalID in TARelation["Temporal"]:
                                Value = TARelation["Temporal"][TemporalID]
                            Widget = Globals.References["SoLFunctions"].GetTValueStaticWidget(TemporalID, Value)

                        if Widget != None:
                            WidgetsDict[TemporalID] = Widget
                    except Exception as e:
                        ""

                MaxWidth = 994
                Width, Height = Globals.References["SoLFunctions"].GridLayoutMaker(self, self.TLayout, WidgetsDict, MaxWidth, 5)

                self.THolder.setGeometry(15,45,Width,Height)
                TotalHeight = Height + 45
                self.TWidget.TotalHeight = TotalHeight
                self.TWidget.setMaximumHeight(TotalHeight)
                self.TWidget.setMinimumHeight(TotalHeight)
                self.TWidget.setMaximumWidth(MaxWidth)
                self.TWidget.setMinimumWidth(MaxWidth)

                self.MainForm.addWidget(self.TWidget)
                self.MainForm.WidgetsList.append(self.TWidget)

                Height = self.MainBox.height() + self.TWidget.height()+10
                self.MainBox.setMinimumHeight(Height)
                self.MainBox.setMaximumHeight(Height)

            def setGems(self):
                self.GWidget = QWidget(objectName = "Transparent")
                self.GWidget.Status = "Open"

                self.GLabel = QLabel("Gems", self.GWidget, objectName = "SubTitle")
                self.GLabel.setProperty("Color","Light")
                self.GLabel.setGeometry(15,0,979,40)
                self.GLabel.setAlignment(Qt.AlignCenter)

                def GOpenClose():
                    if self.GWidget.Status == "Open":
                        TotalHeight = 45
                        self.GWidget.setMaximumHeight(TotalHeight)
                        self.GWidget.setMinimumHeight(TotalHeight)

                        Height = self.MainBox.height() - self.GWidget.height() + TotalHeight
                        self.MainBox.setMinimumHeight(Height)
                        self.MainBox.setMaximumHeight(Height)

                        self.GCloser.setStyleSheet("border-image: url(images/SoLResources/Down.png); ")
                        self.GWidget.Status = "Closed"
                    elif self.GWidget.Status == "Closed":
                        TotalHeight = self.GWidget.TotalHeight
                        self.GWidget.setMaximumHeight(TotalHeight)
                        self.GWidget.setMinimumHeight(TotalHeight)

                        Height = self.MainBox.height() - 45 + TotalHeight
                        self.MainBox.setMinimumHeight(Height)
                        self.MainBox.setMaximumHeight(Height)

                        self.GCloser.setStyleSheet("border-image: url(images/SoLResources/Up.png); ")
                        self.GWidget.Status = "Open"
                self.GCloser = QPushButton(self.GWidget, clicked = lambda: GOpenClose())
                self.GCloser.setProperty("Color","Light")
                self.GCloser.setGeometry(950,5,30,30)
                self.GCloser.setStyleSheet("border-image: url(images/SoLResources/Up.png); ")

                self.GLayout = QGridLayout()
                self.GLayout.setContentsMargins(5, 5, 5, 5)
                self.GLayout.WidgetsList = []
                self.GHolder = QWidget(self.GWidget, objectName = "Transparent")
                self.GHolder.setLayout(self.GLayout)

                FullGValuesList = list(set( list(Globals.SoLGValues.keys()) + list(TARelation["Gems"].keys()) ))

                WidgetsDict = {}
                for GemsID in FullGValuesList:
                    try:
                        if GemsID in Globals.SoLGValues:
                            Value = None
                            if GemsID in TARelation["Gems"]:
                                Value = TARelation["Gems"][GemsID]
                            Widget = Globals.SoLGValues[GemsID]["Reference"].GetGValueStaticWidget(GemsID, Value)
                        else:
                            Value = None
                            if GemsID in TARelation["Gems"]:
                                Value = TARelation["Gems"][GemsID]
                            Widget = Globals.References["SoLFunctions"].GetGValueStaticWidget(GemsID, Value)

                        if Widget != None:
                            WidgetsDict[GemsID] = Widget
                    except Exception as e:
                        ""

                MaxWidth = 994
                Width, Height = Globals.References["SoLFunctions"].GridLayoutMaker(self, self.GLayout, WidgetsDict, MaxWidth, 5)

                self.GHolder.setGeometry(15,45,Width,Height)
                TotalHeight = Height + 45
                self.GWidget.TotalHeight = TotalHeight
                self.GWidget.setMaximumHeight(TotalHeight)
                self.GWidget.setMinimumHeight(TotalHeight)
                self.GWidget.setMaximumWidth(MaxWidth)
                self.GWidget.setMinimumWidth(MaxWidth)

                self.MainForm.addWidget(self.GWidget)
                self.MainForm.WidgetsList.append(self.GWidget)

                Height = self.MainBox.height() + self.GWidget.height()+10
                self.MainBox.setMinimumHeight(Height)
                self.MainBox.setMaximumHeight(Height)

            def setAbilities(self):
                self.AWidget = QWidget(objectName = "Transparent")
                self.AWidget.Status = "Open"

                self.ALabel = QLabel("Abilities", self.AWidget, objectName = "SubTitle")
                self.ALabel.setProperty("Color","Light")
                self.ALabel.setGeometry(15,0,979,40)
                self.ALabel.setAlignment(Qt.AlignCenter)

                def AOpenClose():
                    if self.AWidget.Status == "Open":
                        TotalHeight = 45
                        self.AWidget.setMaximumHeight(TotalHeight)
                        self.AWidget.setMinimumHeight(TotalHeight)

                        Height = self.MainBox.height() - self.AWidget.height() + TotalHeight
                        self.MainBox.setMinimumHeight(Height)
                        self.MainBox.setMaximumHeight(Height)

                        self.ACloser.setStyleSheet("border-image: url(images/SoLResources/Down.png); ")
                        self.AWidget.Status = "Closed"
                    elif self.AWidget.Status == "Closed":
                        TotalHeight = self.AWidget.TotalHeight
                        self.AWidget.setMaximumHeight(TotalHeight)
                        self.AWidget.setMinimumHeight(TotalHeight)

                        Height = self.MainBox.height() - 45 + TotalHeight
                        self.MainBox.setMinimumHeight(Height)
                        self.MainBox.setMaximumHeight(Height)

                        self.ACloser.setStyleSheet("border-image: url(images/SoLResources/Up.png); ")
                        self.AWidget.Status = "Open"
                self.ACloser = QPushButton(self.AWidget, clicked = lambda: AOpenClose())
                self.ACloser.setProperty("Color","Light")
                self.ACloser.setGeometry(950,5,30,30)
                self.ACloser.setStyleSheet("border-image: url(images/SoLResources/Up.png); ")

                self.ALayout = QGridLayout()
                self.ALayout.setContentsMargins(5, 5, 5, 5)
                self.ALayout.WidgetsList = []
                self.AHolder = QWidget(self.AWidget, objectName = "Transparent")
                self.AHolder.setLayout(self.ALayout)

                FullAValuesList = list( Globals.SoLAbilities.keys() )

                WidgetsDict = {}
                for AbilityID in Globals.SoLAbilities:
                    try:
                        Data = None
                        if AbilityID in TARelation["Abilities"]:
                            Data = TARelation["Abilities"][AbilityID]
                        Widget = Globals.SoLAbilities[AbilityID]["Reference"].GetAbilityDynamicWidget(AbilityID, Data, Target, Actor, {"UpgradeForceAvailable":1, "DowngradeForceAvailable":1})
                        if Widget != None:
                            WidgetsDict[AbilityID] = Widget
                    except Exception as e:
                        print(e)
                        ""

                MaxWidth = 994
                Width, Height = Globals.References["SoLFunctions"].GridLayoutMaker(self, self.ALayout, WidgetsDict, MaxWidth, 10)

                self.AHolder.setGeometry(5,45,Width,Height)
                TotalHeight = Height + 45
                self.AWidget.TotalHeight = TotalHeight
                self.AWidget.setMaximumHeight(TotalHeight)
                self.AWidget.setMinimumHeight(TotalHeight)
                self.AWidget.setMaximumWidth(MaxWidth)
                self.AWidget.setMinimumWidth(MaxWidth)

                self.MainForm.addWidget(self.AWidget)
                self.MainForm.WidgetsList.append(self.AWidget)

                Height = self.MainBox.height() + self.AWidget.height()+10
                self.MainBox.setMinimumHeight(Height)
                self.MainBox.setMaximumHeight(Height)

            def setTraits(self):
                self.TTWidget = QWidget(objectName = "Transparent")
                self.TTWidget.Status = "Open"

                self.TTLabel = QLabel("Traits", self.TTWidget, objectName = "SubTitle")
                self.TTLabel.setProperty("Color","Light")
                self.TTLabel.setGeometry(15,0,979,40)
                self.TTLabel.setAlignment(Qt.AlignCenter)

                def TTOpenClose():
                    if self.TTWidget.Status == "Open":
                        TotalHeight = 45
                        self.TTWidget.setMaximumHeight(TotalHeight)
                        self.TTWidget.setMinimumHeight(TotalHeight)

                        Height = self.MainBox.height() - self.TTWidget.height() + TotalHeight
                        self.MainBox.setMinimumHeight(Height)
                        self.MainBox.setMaximumHeight(Height)

                        self.TTCloser.setStyleSheet("border-image: url(images/SoLResources/Down.png); ")
                        self.TTWidget.Status = "Closed"
                    elif self.TTWidget.Status == "Closed":
                        TotalHeight = self.TTWidget.TotalHeight
                        self.TTWidget.setMaximumHeight(TotalHeight)
                        self.TTWidget.setMinimumHeight(TotalHeight)

                        Height = self.MainBox.height() - 45 + TotalHeight
                        self.MainBox.setMinimumHeight(Height)
                        self.MainBox.setMaximumHeight(Height)

                        self.TTCloser.setStyleSheet("border-image: url(images/SoLResources/Up.png); ")
                        self.TTWidget.Status = "Open"
                self.TTCloser = QPushButton(self.TTWidget, clicked = lambda: TTOpenClose())
                self.TTCloser.setProperty("Color","Light")
                self.TTCloser.setGeometry(950,5,30,30)
                self.TTCloser.setStyleSheet("border-image: url(images/SoLResources/Up.png); ")

                self.TTLayout = QGridLayout()
                self.TTLayout.setContentsMargins(0, 0, 0, 0)
                self.TTLayout.WidgetsList = []
                self.TTHolder = QWidget(self.TTWidget, objectName = "Transparent")
                self.TTHolder.setLayout(self.TTLayout)

                FullAValuesList = list( Globals.SoLAbilities.keys() )

                WidgetsDict = {}
                for TraitID in Globals.SoLTraits:
                    try:
                        Data = None
                        if TraitID in TargetData["Traits"]:
                            Data = TargetData["Traits"][TraitID]
                        Widget = Globals.SoLTraits[TraitID]["Reference"].GetTraitDynamicWidget(TraitID, Data, Target, Actor, {"ForceAvailable":1})
                        if Widget != None:
                            WidgetsDict[TraitID] = Widget
                    except Exception as e:
                        print("Error", e)

                MaxWidth = 994
                Width, Height = Globals.References["SoLFunctions"].GridLayoutMaker(self, self.TTLayout, WidgetsDict, MaxWidth, 10)

                self.TTHolder.setGeometry(15,45,Width,Height)
                TotalHeight = Height + 45
                self.TTWidget.TotalHeight = TotalHeight
                self.TTWidget.setMaximumHeight(TotalHeight)
                self.TTWidget.setMinimumHeight(TotalHeight)
                self.TTWidget.setMaximumWidth(MaxWidth)
                self.TTWidget.setMinimumWidth(MaxWidth)

                self.MainForm.addWidget(self.TTWidget)
                self.MainForm.WidgetsList.append(self.TTWidget)

                Height = self.MainBox.height() + self.TTWidget.height()+10
                self.MainBox.setMinimumHeight(Height)
                self.MainBox.setMaximumHeight(Height)

            def setFallenStates(self):
                self.FWidget = QWidget(objectName = "Transparent")
                self.FWidget.Status = "Open"

                self.FLabel = QLabel("Fallen States", self.FWidget, objectName = "SubTitle")
                self.FLabel.setProperty("Color","Light")
                self.FLabel.setGeometry(15,0,979,40)
                self.FLabel.setAlignment(Qt.AlignCenter)

                def FOpenClose():
                    if self.FWidget.Status == "Open":
                        TotalHeight = 45
                        self.FWidget.setMaximumHeight(TotalHeight)
                        self.FWidget.setMinimumHeight(TotalHeight)

                        Height = self.MainBox.height() - self.FWidget.height() + TotalHeight
                        self.MainBox.setMinimumHeight(Height)
                        self.MainBox.setMaximumHeight(Height)

                        self.FCloser.setStyleSheet("border-image: url(images/SoLResources/Down.png); ")
                        self.FWidget.Status = "Closed"
                    elif self.FWidget.Status == "Closed":
                        TotalHeight = self.FWidget.TotalHeight
                        self.FWidget.setMaximumHeight(TotalHeight)
                        self.FWidget.setMinimumHeight(TotalHeight)

                        Height = self.MainBox.height() - 45 + TotalHeight
                        self.MainBox.setMinimumHeight(Height)
                        self.MainBox.setMaximumHeight(Height)

                        self.FCloser.setStyleSheet("border-image: url(images/SoLResources/Up.png); ")
                        self.FWidget.Status = "Open"
                self.FCloser = QPushButton(self.FWidget, clicked = lambda: FOpenClose())
                self.FCloser.setProperty("Color","Light")
                self.FCloser.setGeometry(950,5,30,30)
                self.FCloser.setStyleSheet("border-image: url(images/SoLResources/Up.png); ")

                self.FLayout = QGridLayout()
                self.FLayout.setContentsMargins(0, 0, 0, 0)
                self.FLayout.WidgetsList = []
                self.FHolder = QWidget(self.FWidget, objectName = "Transparent")
                self.FHolder.setLayout(self.FLayout)

                FullAValuesList = list( Globals.SoLAbilities.keys() )

                WidgetsDict = {}
                for FallenID in Globals.SoLFallenStates:
                    try:
                        Data = None
                        if FallenID in TARelation["FallenData"]:
                            Data = TARelation["FallenData"][FallenID]
                        Widget = Globals.SoLFallenStates[FallenID]["Reference"].GetFallenDynamicWidget(FallenID, Data, Target, Actor, {"ForceAvailable":1})
                        if Widget != None:
                            WidgetsDict[FallenID] = Widget
                    except Exception as e:
                        ""

                MaxWidth = 994
                Width, Height = Globals.References["SoLFunctions"].GridLayoutMaker(self, self.FLayout, WidgetsDict, MaxWidth, 10)

                self.FHolder.setGeometry(15,45,Width,Height)
                TotalHeight = Height + 45
                self.FWidget.TotalHeight = TotalHeight
                self.FWidget.setMaximumHeight(TotalHeight)
                self.FWidget.setMinimumHeight(TotalHeight)
                self.FWidget.setMaximumWidth(MaxWidth)
                self.FWidget.setMinimumWidth(MaxWidth)

                self.MainForm.addWidget(self.FWidget)
                self.MainForm.WidgetsList.append(self.FWidget)

                Height = self.MainBox.height() + self.FWidget.height()+10
                self.MainBox.setMinimumHeight(Height)
                self.MainBox.setMaximumHeight(Height)

            #####
            NameWidget = QWidget(objectName = "Transparent")
            NameWidget.setMinimumHeight(45)
            NameWidget.setMaximumHeight(45)
            NameWidget.setMinimumWidth(1024)
            NameWidget.setMaximumWidth(1024)

            LabelName = QLabel("TEST TEXT", NameWidget, objectName = "Title")
            LabelName.setText(Globals.SoLNPCData[Target]["BodyData"]["FullName"])
            LabelName.setAlignment(Qt.AlignCenter)
            LabelName.setGeometry(15,0,980,45)
            LabelName.setProperty("Color","Light")

            self.MainForm.addWidget(NameWidget)
            self.MainForm.WidgetsList.append(NameWidget)

            Height = NameWidget.height()+10
            self.MainBox.setMinimumHeight(Height)
            self.MainBox.setMaximumHeight(Height)
            self.MainBox.setMinimumWidth(1024)
            self.MainBox.setMaximumWidth(1024)
            setTemporal(self)
            setPermanent(self)
            setGems(self)
            setAbilities(self)
            setTraits(self)
            setFallenStates(self)



def Initialize(self, Reference):
    if "EnhanceUI" not in Globals.Layouts:
        Object = UiLayoutEnhanceMenu()
