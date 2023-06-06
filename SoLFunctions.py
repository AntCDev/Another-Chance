
import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QTextCursor
import json
import os
import random
import math
import Globals
Log = Globals.Layouts["MainF"].Log
import copy
import time
import inspect

class GenericNPCObject:
    def __init__(self, ID):
        self.ID = ID
        self.Data = Globals.SoLNPCData[self.ID]
        self.Name = self.Data["Name"]


    def GetWidget(self):
        self.NPCWidget = QWidget()
        self.NPCWidget.setMinimumWidth(350)
        self.NPCWidget.setMinimumHeight(200)
        self.NPCWidget.setMaximumWidth(350)
        self.NPCWidget.setMaximumHeight(200)
        # if Globals.SoLPCData["Targeting"] == self.ID:
        self.NPCWidget.setStyleSheet('''
        .QWidget{
        border: 1px solid black;
        background : rgb(23, 23, 23)
        }
        .QWidget[Selected = "1"]{
        border: 1px solid yellow;
        background : rgb(23, 23, 23)
        }
        QLabel{
        border: 1px solid black;
        background : rgb(35, 35, 35)
        }
        ''')
        # else:
        #     self.NPCWidget.setStyleSheet('''
        #     .QWidget{
        #     border: 1px solid black;
        #     background : rgb(23, 23, 23)
        #     }
        #     QLabel{
        #     border: 1px solid black;
        #     background : rgb(35, 35, 35)
        #     }
        #     ''')


        ImageName = ""
        try:
            ListPortraits, ListFullBody = GetImages(self.Data)
            ImageType = "Portrait"
            if ImageType == "Portrait" or ListFullBody == []:
                ImageName = random.choice(ListPortraits)
            if ImageType == "FullBody" or ListPortraits == []:
                ImageName = random.choice(ListFullBody)

            if ImageName == "":
                ListPortraits, ListFullBody = GetGenericImage(self.Data)

            self.LabelImage = QLabel(self.NPCWidget)
            self.LabelImage.setGeometry(5,5,130,130)
            self.LabelImage.setPixmap(QPixmap(f'''NPCdata/{self.Name}{self.ID}/{ImageName}'''))
            self.LabelImage.setScaledContents(True)
        except Exception as e:
            self.LabelImage = QLabel(self.NPCWidget)
            self.LabelImage.setGeometry(5,5,130,130)
            self.LabelImage.setStyleSheet('''
            QLabel{
            background : rgb(23, 23, 23)
            }
            ''')
        if ImageName == "":
            ImageName = GetGenericImage(self.Data)


        def FC():
            ToggleFavorite(self.ID)
            Globals.References["SoLFunctions"].Refresh(Globals.Layouts["SoLUI"])
        self.LabelFavorite = QLabel(self.NPCWidget)
        self.LabelFavorite.setGeometry(5,5,25,25)
        self.LabelFavorite.mouseReleaseEvent = lambda event: FC()

        self.LabelName = QLabel(self.NPCWidget)
        self.LabelName.setGeometry(140,5,205,40)
        self.LabelName.setText(self.Data["Name"])
        self.LabelName.setFont(QFont('Segoe UI', 14))
        self.LabelName.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        def GoToDetails():

            Globals.LayoutsData["DetailsUI"]["ID"] = self.ID
            Globals.LayoutsData["DetailsUI"]["Name"] = self.Name
            Globals.LayoutsData["DetailsUI"]["Type"] = 1
            Globals.Layouts["MainF"].gotoLayout("DetailsUI")

        self.ButtonDetails = QPushButton("Details", self.NPCWidget,clicked = lambda:GoToDetails())
        self.ButtonDetails.setGeometry(270,50,75,40)
        self.ButtonDetails.setFont(QFont('Segoe UI', 12))
        # self.buttonOptions = QPushButton('Options(Deta)', self.GUI, clicked = lambda: MainWindow.gotoLayout("DetailsUI", "detailsMenuUI"))

        def SwitchFunc(self):
            Globals.References["SoLFunctions"].Switch(Globals.Layouts["SoLUI"], self.ID)

        self.ButtonSwitch = QPushButton("Switch", self.NPCWidget, clicked = lambda: SwitchFunc(self))
        self.ButtonSwitch.setGeometry(270,95,75,40)
        self.ButtonSwitch.setFont(QFont('Segoe UI', 12))

        self.LabelAction = QLabel(self.NPCWidget)
        self.LabelAction.setGeometry(5,140,340,55)
        self.LabelAction.setText(f'''{self.Data["Name"]} angrily scolds Player''')
        self.LabelAction.setFont(QFont('Segoe UI', 12))
        self.LabelAction.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        self.LabelAction.setWordWrap(True)

        Fluff = Globals.SoLNPCData[self.ID]["Actions"]["CurrentTask"]["Task"][1]["BriefFluff"]
        self.LabelAction.setText(Fluff)

        def NG():
            try:
                PCID = Globals.SoLPCData["ID"]
                if self.ID != PCID:
                    Globals.SoLPCData["Targeting"] = self.ID
                    Globals.References["SoLFunctions"].Refresh(Globals.Layouts["SoLUI"])
            except Exception as e:
                Log(3, "ERROR SWITCHING TARGET", e)

        self.NPCWidget.mouseReleaseEvent = lambda event: NG()

        # FOR EASE OF CONTAINING THE REPEATED LABLES
        if True:
            self.LabelArousal1 = QLabel(self.NPCWidget)
            self.LabelArousal1.setGeometry(140,50,25,25)
            self.LabelArousal1.setScaledContents(True)
            self.LabelArousal1.setStyleSheet('''QLabel{background: none;}''')

            self.LabelArousal2 = QLabel(self.NPCWidget)
            self.LabelArousal2.setGeometry(165,50,25,25)
            self.LabelArousal2.setScaledContents(True)
            self.LabelArousal2.setStyleSheet('''QLabel{background: none;}''')

            self.LabelArousal3 = QLabel(self.NPCWidget)
            self.LabelArousal3.setGeometry(190,50,25,25)
            self.LabelArousal3.setScaledContents(True)
            self.LabelArousal3.setStyleSheet('''QLabel{background: none;}''')

            self.LabelArousal4 = QLabel(self.NPCWidget)
            self.LabelArousal4.setGeometry(215,50,25,25)
            self.LabelArousal4.setScaledContents(True)
            self.LabelArousal4.setStyleSheet('''QLabel{background: none;}''')

            self.LabelArousal5 = QLabel(self.NPCWidget)
            self.LabelArousal5.setGeometry(240,50,25,25)
            self.LabelArousal5.setScaledContents(True)
            self.LabelArousal5.setStyleSheet('''QLabel{background: none;}''')


        if True:
            self.LabelEnergy1 = QLabel(self.NPCWidget)
            self.LabelEnergy1.setGeometry(140,80,25,25)
            self.LabelEnergy1.setScaledContents(True)
            self.LabelEnergy1.setStyleSheet('''QLabel{background: none;}''')

            self.LabelEnergy2 = QLabel(self.NPCWidget)
            self.LabelEnergy2.setGeometry(165,80,25,25)
            self.LabelEnergy2.setScaledContents(True)
            self.LabelEnergy2.setStyleSheet('''QLabel{background: none;}''')

            self.LabelEnergy3 = QLabel(self.NPCWidget)
            self.LabelEnergy3.setGeometry(190,80,25,25)
            self.LabelEnergy3.setScaledContents(True)
            self.LabelEnergy3.setStyleSheet('''QLabel{background: none;}''')

            self.LabelEnergy4 = QLabel(self.NPCWidget)
            self.LabelEnergy4.setGeometry(215,80,25,25)
            self.LabelEnergy4.setScaledContents(True)
            self.LabelEnergy4.setStyleSheet('''QLabel{background: none;}''')

            self.LabelEnergy5 = QLabel(self.NPCWidget)
            self.LabelEnergy5.setGeometry(240,80,25,25)
            self.LabelEnergy5.setScaledContents(True)
            self.LabelEnergy5.setStyleSheet('''QLabel{background: none;}''')

        if True:
            self.LabelMood1 = QLabel(self.NPCWidget)
            self.LabelMood1.setGeometry(140,110,25,25)
            self.LabelMood1.setScaledContents(True)
            self.LabelMood1.setStyleSheet('''QLabel{background: none;}''')

            self.LabelMood2 = QLabel(self.NPCWidget)
            self.LabelMood2.setGeometry(165,110,25,25)
            self.LabelMood2.setScaledContents(True)
            self.LabelMood2.setStyleSheet('''QLabel{background: none;}''')

            self.LabelMood3 = QLabel(self.NPCWidget)
            self.LabelMood3.setGeometry(190,110,25,25)
            self.LabelMood3.setScaledContents(True)
            self.LabelMood3.setStyleSheet('''QLabel{background: none;}''')

            self.LabelMood4 = QLabel(self.NPCWidget)
            self.LabelMood4.setGeometry(215,110,25,25)
            self.LabelMood4.setScaledContents(True)
            self.LabelMood4.setStyleSheet('''QLabel{background: none;}''')

            self.LabelMood5 = QLabel(self.NPCWidget)
            self.LabelMood5.setGeometry(240,110,25,25)
            self.LabelMood5.setScaledContents(True)
            self.LabelMood5.setStyleSheet('''QLabel{background: none;}''')



        self.UpdateWidget()
        return self.NPCWidget

    def UpdateWidget(self):
        if Globals.SoLPCData["Targeting"] == self.ID:
            self.NPCWidget.setProperty("Selected",1)
            self.NPCWidget.style().polish(self.NPCWidget)
        else:
            self.NPCWidget.setProperty("Selected",0)
            self.NPCWidget.style().polish(self.NPCWidget)
        self.Data = Globals.SoLNPCData[self.ID]

        if self.Data["State"]["Arousal"] >= 20:
            self.LabelArousal1.setPixmap(QPixmap(f'''images/SoLResources/FilledHeart'''))
        else:
            self.LabelArousal1.setPixmap(QPixmap(f'''images/SoLResources/EmptyHeart'''))
        if self.Data["State"]["Arousal"] >= 40:
            self.LabelArousal2.setPixmap(QPixmap(f'''images/SoLResources/FilledHeart'''))
        else:
            self.LabelArousal2.setPixmap(QPixmap(f'''images/SoLResources/EmptyHeart'''))
        if self.Data["State"]["Arousal"] >= 60:
            self.LabelArousal3.setPixmap(QPixmap(f'''images/SoLResources/FilledHeart'''))
        else:
            self.LabelArousal3.setPixmap(QPixmap(f'''images/SoLResources/EmptyHeart'''))
        if self.Data["State"]["Arousal"] >= 80:
            self.LabelArousal4.setPixmap(QPixmap(f'''images/SoLResources/FilledHeart'''))
        else:
            self.LabelArousal4.setPixmap(QPixmap(f'''images/SoLResources/EmptyHeart'''))
        if self.Data["State"]["Arousal"] >= 100:
            self.LabelArousal5.setPixmap(QPixmap(f'''images/SoLResources/FilledHeart'''))
        else:
            self.LabelArousal5.setPixmap(QPixmap(f'''images/SoLResources/EmptyHeart'''))


        if self.Data["State"]["Energy"] >= self.Data["GeneralAbilities"]["MaxEnergy"] / 5:
            self.LabelEnergy1.setPixmap(QPixmap(f'''images/SoLResources/FilledEnergy'''))
        else:
            self.LabelEnergy1.setPixmap(QPixmap(f'''images/SoLResources/EmptyEnergy'''))
        if self.Data["State"]["Energy"] >= (self.Data["GeneralAbilities"]["MaxEnergy"] / 5) * 2:
            self.LabelEnergy2.setPixmap(QPixmap(f'''images/SoLResources/FilledEnergy'''))
        else:
            self.LabelEnergy2.setPixmap(QPixmap(f'''images/SoLResources/EmptyEnergy'''))
        if self.Data["State"]["Energy"] >= (self.Data["GeneralAbilities"]["MaxEnergy"] / 5) * 3:
            self.LabelEnergy3.setPixmap(QPixmap(f'''images/SoLResources/FilledEnergy'''))
        else:
            self.LabelEnergy3.setPixmap(QPixmap(f'''images/SoLResources/EmptyEnergy'''))
        if self.Data["State"]["Energy"] >= (self.Data["GeneralAbilities"]["MaxEnergy"] / 5) * 4:
            self.LabelEnergy4.setPixmap(QPixmap(f'''images/SoLResources/FilledEnergy'''))
        else:
            self.LabelEnergy4.setPixmap(QPixmap(f'''images/SoLResources/EmptyEnergy'''))
        if self.Data["State"]["Energy"] >= (self.Data["GeneralAbilities"]["MaxEnergy"] / 5) * 5:
            self.LabelEnergy5.setPixmap(QPixmap(f'''images/SoLResources/FilledEnergy'''))
        else:
            self.LabelEnergy5.setPixmap(QPixmap(f'''images/SoLResources/EmptyEnergy'''))


        if self.Data["State"]["Mood"] >= 0:
            if self.Data["State"]["Mood"] >= 20:
                self.LabelMood1.setPixmap(QPixmap(f'''images/SoLResources/BlueDiamond'''))
            else:
                self.LabelMood1.setPixmap(QPixmap(f'''images/SoLResources/EmptyDiamond'''))

            if self.Data["State"]["Mood"] >= 40:
                self.LabelMood2.setPixmap(QPixmap(f'''images/SoLResources/BlueDiamond'''))
            else:
                self.LabelMood2.setPixmap(QPixmap(f'''images/SoLResources/EmptyDiamond'''))

            if self.Data["State"]["Mood"] >= 60:
                self.LabelMood3.setPixmap(QPixmap(f'''images/SoLResources/BlueDiamond'''))
            else:
                self.LabelMood3.setPixmap(QPixmap(f'''images/SoLResources/EmptyDiamond'''))

            if self.Data["State"]["Mood"] >= 80:
                self.LabelMood4.setPixmap(QPixmap(f'''images/SoLResources/BlueDiamond'''))
            else:
                self.LabelMood4.setPixmap(QPixmap(f'''images/SoLResources/EmptyDiamond'''))

            if self.Data["State"]["Mood"] >= 100:
                self.LabelMood5.setPixmap(QPixmap(f'''images/SoLResources/BlueDiamond'''))
            else:
                self.LabelMood5.setPixmap(QPixmap(f'''images/SoLResources/EmptyDiamond'''))
        elif self.Data["State"]["Mood"] <= 0:
            if self.Data["State"]["Mood"] <= -20:
                self.LabelMood1.setPixmap(QPixmap(f'''images/SoLResources/RedDiamond'''))
            else:
                self.LabelMood1.setPixmap(QPixmap(f'''images/SoLResources/EmptyDiamond'''))

            if self.Data["State"]["Mood"] <= -40:
                self.LabelMood2.setPixmap(QPixmap(f'''images/SoLResources/RedDiamond'''))
            else:
                self.LabelMood2.setPixmap(QPixmap(f'''images/SoLResources/EmptyDiamond'''))

            if self.Data["State"]["Mood"] <= -60:
                self.LabelMood3.setPixmap(QPixmap(f'''images/SoLResources/RedDiamond'''))
            else:
                self.LabelMood3.setPixmap(QPixmap(f'''images/SoLResources/EmptyDiamond'''))

            if self.Data["State"]["Mood"] <= -80:
                self.LabelMood4.setPixmap(QPixmap(f'''images/SoLResources/RedDiamond'''))
            else:
                self.LabelMood4.setPixmap(QPixmap(f'''images/SoLResources/EmptyDiamond'''))

            if self.Data["State"]["Mood"] <= -100:
                self.LabelMood5.setPixmap(QPixmap(f'''images/SoLResources/RedDiamond'''))
            else:
                self.LabelMood5.setPixmap(QPixmap(f'''images/SoLResources/EmptyDiamond'''))

        if self.ID in Globals.SoLTempData["FavoriteNPC"]:
            self.LabelFavorite.setStyleSheet('''border-image: url(images/SoLResources/FilledStar.png); background-color:rgba(0,0,0,0); border-color:rgba(0,0,0,0); ''')
        else:
            self.LabelFavorite.setStyleSheet('''border-image: url(images/SoLResources/EmptyStar.png); background-color:rgba(0,0,0,0); border-color:rgba(0,0,0,0); ''')


        # print(Globals.SoLNPCData[Target]["Actions"]["CurrentTask"])
        # print(Globals.SoLNPCData[Actor]["Actions"]["CurrentTask"])
        Fluff = Globals.SoLNPCData[self.ID]["Actions"]["CurrentTask"]["Task"][1]["BriefFluff"]
        self.LabelAction.setText(Fluff)

def CheckNPCActions(self):
    try:
        ### FIRST IT CHECKS FOR ANY NPC THAT HAS ALREADY COMPLETED THEIR ACTION
        IdleNPCList = []
        DateData = Globals.SoLEnviorementData["DateData"]
        PCID = Globals.SoLPCData["ID"]
        for NPCID in Globals.SoLNPCData:
            if NPCID != PCID:
                Idle = 0
                if Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"]["HourFinish"] < Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"]["HourStart"]:
                    # 1200 - 400
                    if DateData["Hour"] > Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"]["HourFinish"] and DateData["Hour"] < Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"]["HourStart"]:
                        Idle = 1
                else:
                    # 400 - 1220
                    if DateData["Hour"] < Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"]["HourStart"] or DateData["Hour"] > Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"]["HourFinish"]:
                        Idle = 1
                if Idle == 1:
                    IdleNPCList.append(NPCID)
                    ApplyIdleTask(NPCID)
        for NPCID in IdleNPCList:
            PersonalityID = Globals.SoLNPCData[NPCID]["Personality"]
            Globals.SoLPersonalities[PersonalityID]["Reference"].CheckIdleAction(self, NPCID)



        if IdleNPCList != []:
            if False:
                if False:
                    ### FROM THE LIST OF FINISHED NPCS THEN IT CHECKS FOR ANY POSSIBLE SCHEDULED ACTION
                    NewList = []
                    for NPCID in IdleNPCList:
                        try:
                            NPCSchedule = Globals.SoLNPCSchedules[NPCID]
                            for Task in NPCSchedule:

                                if Task["HourStart"] <= DateData["Hour"] and Task["HourFinish"] >= DateData["Hour"]:
                                    Globals.SoLNPCData[NPCID]["Actions"]["PreviousTask"] = Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"]
                                    Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"] = Task

                                    Index = NPCSchedule.index(Task)
                                    if len(NPCSchedule) > Index + 1:
                                        NextTask = NPCSchedule[Index+1]
                                        Globals.SoLNPCData[NPCID]["Actions"]["FutureTask"] = NextTask
                                    else:
                                        Globals.SoLNPCData[NPCID]["Actions"]["FutureTask"] = ""
                                    break
                            else:
                                NewList.append(NPCID)
                        except:
                            NewList.append(NPCID)
                    IdleNPCList = NewList

                    ### IF THE NPCS DOESN'T HAVE ANY SCHEDULED ACTION THEN IT CHECKS FOR RANDOM MOVEMENT
                    for NPCID in IdleNPCList:
                        try:
                            # TODO MAKE THIS PING FOR THE CHARACTER PERSONALITY TO CHECK MOVEMENT
                            TODO
                        except:
                            RN = random.randint(1,5)
                            if RN == 5:
                                NPCLocation = Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"]["Location"]
                                PossibleLocations = []
                                try:
                                    PrePossibleLocations = Globals.SoLEnviorementData["Locations"][NPCLocation]["CanAccess"]
                                    for Location in PrePossibleLocations:
                                        if NPCID not in Globals.SoLEnviorementData["Locations"][Location]["Forbidden"]:
                                            PossibleLocations.append(Location)
                                except Exception as e:
                                    PossibleLocations = []

                                if PossibleLocations != []:
                                    PreviousLocation = Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"]["Location"]
                                    Location = random.choice(PossibleLocations)
                                    IdleTask = copy.deepcopy(Globals.SoLOtherData["IdlingTask"])
                                    IdleTask["Location"] = Location
                                    IdleTask["Task"][1]["BriefFluff"] = f'''Idling in {Globals.SoLEnviorementData["Locations"][Location]["Name"]}'''
                                    IdleTask["Task"][1]["LongFluff"] = f'''{Globals.SoLNPCData[NPCID]["Name"]} is Idling at {Globals.SoLEnviorementData["Locations"][Location]["Name"]}'''
                                    IdleTask["HourStart"] = DateData["Hour"]
                                    if Globals.SoLNPCData[NPCID]["Actions"]["FutureTask"] != "":
                                        if Globals.SoLNPCData[NPCID]["Actions"]["FutureTask"]["HourStart"] > DateData["Hour"] + 15:
                                            IdleTask["HourFinish"] = DateData["Hour"] + 15
                                        else:
                                            IdleTask["HourFinish"] = Globals.SoLNPCData[NPCID]["Actions"]["FutureTask"]["HourStart"]
                                    else:
                                        IdleTask["HourFinish"] = DateData["Hour"] + 15
                                    Globals.SoLNPCData[NPCID]["Actions"]["PreviousTask"] = Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"]
                                    Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"] = IdleTask
                                    try:
                                        Globals.SoLEnviorementData["Locations"][PreviousLocation]["inHere"].remove(NPCID)
                                        Globals.SoLEnviorementData["Locations"][Location]["inHere"].append(NPCID)
                                    except Exception as e:
                                        print(e)
                            else:
                                    PreviousLocation = Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"]["Location"]
                                    Location = PreviousLocation
                                    IdleTask = copy.deepcopy(Globals.SoLOtherData["IdlingTask"])
                                    IdleTask["Location"] = Location
                                    IdleTask["Task"][1]["BriefFluff"] = f'''Idling at {Globals.SoLEnviorementData["Locations"][Location]["Name"]}'''
                                    IdleTask["Task"][1]["LongFluff"] = f'''{Globals.SoLNPCData[NPCID]["Name"]} is Idling at {Globals.SoLEnviorementData["Locations"][Location]["Name"]}'''
                                    IdleTask["HourStart"] = DateData["Hour"]
                                    if Globals.SoLNPCData[NPCID]["Actions"]["FutureTask"] != "":
                                        if Globals.SoLNPCData[NPCID]["Actions"]["FutureTask"]["HourStart"] > DateData["Hour"] + 15:
                                            IdleTask["HourFinish"] = DateData["Hour"] + 15
                                        else:
                                            IdleTask["HourFinish"] = Globals.SoLNPCData[NPCID]["Actions"]["FutureTask"]["HourStart"]
                                    else:
                                        IdleTask["HourFinish"] = DateData["Hour"] + 15
                                    Globals.SoLNPCData[NPCID]["Actions"]["PreviousTask"] = Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"]
                                    Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"] = IdleTask
                                    try:
                                        Globals.SoLEnviorementData["Locations"][PreviousLocation]["inHere"].remove(NPCID)
                                    except Exception as e:
                                        ""
                                    try:
                                        Globals.SoLEnviorementData["Locations"][Location]["inHere"].append(NPCID)
                                    except:
                                        ""

                ### ONCE THE IDLE NPCS HAVE MOVED OR NOT, IT THEN CHECKS THE OTHER NPCS IN THEIR LOCATION AND CHECKS FOR A POSSIBLE INTERACTION
                IdleNPCListPost = IdleNPCList
                for NPCID in IdleNPCList:
                    if NPCID in IdleNPCListPost:
                        # TODO CALCULATE SOCIABILITY
                        Sociability = 0.7
                        RN = random.random()
                        Sociability = 1.1
                        if RN <= Sociability:
                            try:
                                NPCLocation = Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"]["Location"]
                                inHere = Globals.SoLEnviorementData["Locations"][NPCLocation]["inHere"]
                                if len(inHere) > 1:
                                    # TODO CHECK IF THE PLAYER IS ALLOWING OR NOT FOR THE NPCS TO TARGET THEM
                                    if PCID in inHere and False:
                                        inHere.remove(PCID)

                                    # CALCULATES THE WEIGHT OF EACH OTHER NPC IN THE AREA
                                    NPCWeights = {}
                                    TotalProbability = 0
                                    for NPCOther in inHere:
                                        if NPCOther != PCID:
                                            try:
                                                Weight = Globals.SoLNPCData[NPCID]["Relations"][NPCOther]["Permanent"]["Attraction"] + Globals.SoLNPCData[NPCID]["Relations"][NPCOther]["Permanent"]["Reliability"] + 100
                                            except:
                                                Weight = 100
                                            NPCWeights[NPCOther] = Weight
                                            TotalProbability += Weight
                                            # TODO SEND THE WEIGHTS TO BE PROCESSED

                                    NPCOther = random.choices(list(NPCWeights.keys()), list(NPCWeights.values()))[0]

                                    if NPCOther != NPCID:
                                        # GETS ALL THE AVAILABLE COMMANDS FOR THE SELECTED NPC AND GETS THEIR WEIGHT
                                        Commands = {}
                                        for CommandID in Globals.Commands:
                                            Available = Globals.Commands[CommandID]["Reference"].CheckCommandAvailable(self, CommandID, NPCID, NPCOther)
                                            if Available == 1:
                                                # TODO IMPLEMENT CONNOTATIONS AND WEIGHTS SYSTEM
                                                CommandWeight = 100
                                                Commands[CommandID] = CommandWeight

                                        # SELECTS THE COMMAND AND EXECUTES IT
                                        CommandID = random.choices(list(Commands.keys()), list(Commands.values()))[0]
                                        try:
                                            IdleNPCListPost.remove(NPCID)
                                            IdleNPCListPost.remove(NPCOther)
                                        except:
                                            ""
                                        print("TRIGGER", CommandID, NPCID, NPCOther)
                                        Globals.Commands[CommandID]["Reference"].TriggerCommand(self, CommandID, NPCOther, NPCID, None)
                            except Exception as e:
                                print("ERROR NPC ACTION", e)
                                ""
    except Exception as e:
        Log(2, "ERROR NPC ACTION", e)
def GetFlavorText(self):
    try:
        # GETS THE NPC FLAVOR
        PCID = Globals.SoLPCData["ID"]
        PCLocation = Globals.SoLNPCData[PCID]["Actions"]["CurrentTask"]["Location"]
        NPCFlavor = ""
        for NPCID in Globals.SoLEnviorementData["Locations"][PCLocation]["inHere"]:
            Flavor = Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"]["Task"][1]["LongFluff"]
            if Flavor.strip() != '':
                NPCFlavor += Flavor
                NPCFlavor += "<br/>"

        # GETS THE ENVIOREMENT FLAVOR
        EnviorementFlavor = ""
        if Globals.SoLEnviorementData['DateData']["Hour"] < 360:
            EnviorementFlavor = "It's very early in the morning, barely any people can be found roaming the city."
        elif Globals.SoLEnviorementData['DateData']["Hour"] < 720:
            EnviorementFlavor = "It's the morning, people can be seen going through their daily duties around the city."
        elif Globals.SoLEnviorementData['DateData']["Hour"] < 1200:
            EnviorementFlavor = "It's the evening, thing are quite lively at this hour as the streets fill with people getting done with their work, education or any otehr duties they attended through the day."
        else:
            EnviorementFlavor = "It's night time, people are starting to head back home and the streets are getting lonely by this hour."
        LocationFlavor = ""
        LocationFlavor = Globals.SoLEnviorementData["Locations"][PCLocation]["FlavorText"]


        # GETS THE PC TARGET FLAVOR
        def TargetStateFlavor():
            ### Checks for Mood and Arousal. Then uses it to value it's ambivalent, negative, and positive flavor text. Then tries to call for customText togeTPPos with a flag which might negate the generic flavor text.
            Target = Globals.SoLPCData["Targeting"]
            if Target != None and Target != PCID:
                TargetData = Globals.SoLNPCData[Target]
                TargetState = TargetData["State"]
                ActorData = Globals.SoLNPCData[PCID]
                ActorState = ActorData["State"]
                TEnergy = TargetState["Energy"]
                TMaxEnergy = TargetData["GeneralAbilities"]["MaxEnergy"]
                TMood = TargetState["Mood"]
                TArousal = TargetState["Arousal"]
                TAlcohol = TargetState["Alcohol"]
                TDrugs = TargetState["Drugs"]
                TSleep = TargetState["PConscious"]
                TBodyData = TargetData["BodyData"]
                TStructure = TBodyData["Sex"]
                TPSub = TBodyData["Pronouns"]["PSub"]  # He
                TPObj = TBodyData["Pronouns"]["PObj"]  # Him
                TPPos = TBodyData["Pronouns"]["PPos"]  # His
                TPIPos = TBodyData["Pronouns"]["PIPos"]  # His


                TEnergySate = TEnergy / (TMaxEnergy / 5); TEnergySate = round(TEnergySate)
                FlavorText = ""
                if TEnergySate == 0:
                    FlavorText += TPSub + " looks completly exhausted and ready to give up on what " + TPSub.lower() + " is currently doing."
                elif TEnergySate == 1:
                    FlavorText += "With just a glance you can tell " + TPSub.lower() + " is getting exhausted."
                elif TEnergySate == 2:
                    FlavorText += TPSub + " looks like " + TPSub.lower() + " is starting to need a break but still having enough energy in reserve."
                elif TEnergySate == 3:
                    FlavorText += TPSub + " looks slightly tired, but still having plenty of energy left."
                elif TEnergySate == 4:
                    FlavorText += TPSub + "  is energetic with barely any hint of tiredness."
                elif TEnergySate == 5:
                    FlavorText += TPSub + " seems to be fresh and full of energy to tackle on with the day."

                FlavorText += " "
                if TMood > 80:
                    FlavorText += TPSub + " has an exression full of excitement for whatever is to come, being in the very best kind of mood " + TPSub.lower() + " can be"
                elif TMood > 60:
                    FlavorText += TPSub + " is obviously quite cheerful with his whole body portraying how eager " + TPSub.lower() + " is."
                elif TMood > 40:
                    FlavorText += TPSub + " seems to be hapy with a nice smile across " + TPPos.lower() + " face."
                elif TMood > 20:
                    FlavorText += TPSub + " looks comfortable around you with a nice pleased expression on " + TPPos.lower() + " face."
                elif TMood > -20:
                    FlavorText += TPSub + " has a somewhat neutral expression on " + TPPos.lower() + " face."
                elif TMood > -40:
                    FlavorText += TPSub + "  is a bit uncomfortable around you, still not being overly hostile but not being too friendly either."
                elif TMood > -60:
                    FlavorText += TPSub + "  is looking bothered and just looking at how " + TPSub.lower() + " behaves " + TPSub.lower() + " is obviously getting upset."
                elif TMood > -80:
                    FlavorText += TPSub + " is openly angry with an overly agressive way of behaving comapred to " + TPPos.lower() + " usual self."
                elif TMood > -100:
                    FlavorText += TPSub + " acts and looks quite mad overall, being obviously not in the mood to have anyone come closer to " + TPPos.lower() + "."

                FlavorText += " "
                if TArousal > 80:
                    FlavorText += TPSub + "  has an expression of pure desire on it's eyes, with obvious signs of aroussal all over " + TPPos.lower() + " body."
                elif TArousal > 60:
                    FlavorText += TPSub + "  gets a heavy blush all over " + TPPos.lower() + " face, rubbing " + TPPos.lower() + " thighs together as if to hide something."
                elif TArousal > 40:
                    FlavorText += TPSub + "  fidgets with " + TPPos.lower() + " fingers a bit too much moving as if something was bothering " + TPPos.lower() + "."
                elif TArousal > 20:
                    FlavorText += "You can spot a light blush developing on " + TPPos.lower() + " cheeks."
            else:
                FlavorText = ""

            return FlavorText
        TargetFlavor = ""
        TargetFlavor = TargetStateFlavor()

        Globals.SoLFlavorDict["EnviorementFlavor"] = EnviorementFlavor + "<br/>" + LocationFlavor
        Globals.SoLFlavorDict["PCTargetFlavor"] = TargetFlavor
        Globals.SoLFlavorDict["NPCActionsFlavor"] = NPCFlavor
    except Exception as e:
        Log(3, "ERROR GetFlavorText", e, PCID, NPCID, Globals.SoLNPCData[NPCID])
def Refresh(self):
    try:
        self.RefreshSignal1.emit()
        ### CHECKS FOR NPC INTEACTIONS AND OTHER POSSIBLE UPDATES
        CheckNPCActions(self)

        ### REFRESHES THE NPC CARDS TO THE RIGHT
        try:
            PCID = Globals.SoLPCData["ID"]
            PCLocation = Globals.SoLNPCData[PCID]["Actions"]["CurrentTask"]["Location"]
            inHereList = Globals.SoLEnviorementData["Locations"][PCLocation]["inHere"].copy()
            FavoriteList = Globals.SoLTempData["FavoriteNPC"]

            NPCList = []
            for i in FavoriteList:
                if i in inHereList and i not in NPCList:
                    NPCList.append(i)

            for i in inHereList:
                if i not in FavoriteList and i not in NPCList:
                    NPCList.append(i)

            for NPCID in self.FormNPC.WigetsDict:
                if NPCID not in NPCList:
                    self.FormNPC.WigetsDict[NPCID]["Widget"].hide()
            if PCID in NPCList: NPCList.remove(PCID)

            Height = 0
            Index = 0
            for NPCID in NPCList:
                Height += 210
                if NPCID in self.FormNPC.WigetsDict:
                    self.FormNPC.WigetsDict[NPCID]["Object"].UpdateWidget()
                    self.FormNPC.WigetsDict[NPCID]["Widget"].show()
                else:
                    Object = GenericNPCObject(NPCID)
                    Widget = Object.GetWidget()
                    self.FormNPC.WigetsDict[NPCID] = {"Object":Object, "Widget":Widget}
                self.FormNPC.insertWidget(Index, self.FormNPC.WigetsDict[NPCID]["Widget"])
                Index += 1

            self.GroupBoxNPC.setMinimumHeight(Height)
            self.GroupBoxNPC.setMaximumHeight(Height)
        except Exception as e:
            Log(3, "ERROR SOL REFRESH NPCWidgets", e)
            ""

        ### CHECKS THE AVAILABLE COMMANDS
        try:
            for Widget in self.FormSoLButtons.WidgetsList:
                self.FormSoLButtons.removeWidget(Widget)
            self.FormSoLButtons.WidgetsList = []
            NPCID = Globals.SoLPCData["Targeting"]
            Layer, Row = 0, 0
            # Globals.Commands = { "Caress0":{"ID":"Caress0", "Reference":<module BasicCommands at 0x00f>, "OtherData":{}},  }
            for CommandID in Globals.Commands:
                Available = Globals.Commands[CommandID]["Reference"].CheckCommandAvailable(self, CommandID, PCID, NPCID)
                if Available == 1:
                    if Row > 4:
                        Row = 0
                        Layer += 1
                    if CommandID in self.FormSoLButtons.WidgetsList:
                        Button = self.FormSoLButtons.WidgetsList[CommandID]["Widget"]
                        self.FormSoLButtons.addWidget(Button, Layer, Row)
                    else:
                        Button = Globals.Commands[CommandID]["Reference"].GetCommandButton(self, CommandID, PCID, NPCID)
                        self.FormSoLButtons.addWidget(Button, Layer, Row)
                        self.FormSoLButtons.WidgetsList.append(Button)
                    Row += 1
            self.GroupBoxSoLButtons.setMinimumHeight((Layer + 1)*45)
            self.GroupBoxSoLButtons.setMaximumHeight((Layer + 1)*45)
            if Layer >= 1:
                self.GroupBoxSoLButtons.setMinimumWidth(870)
                self.GroupBoxSoLButtons.setMaximumWidth(870)
            else:
                self.GroupBoxSoLButtons.setMinimumWidth((Row)*174)
                self.GroupBoxSoLButtons.setMaximumWidth((Row)*174)
        except Exception as e:
            Log(3, "ERROR SOL REFRESH SoLButtons", e)
            ""

        ## CHECKS FOR THE ENVIOREMENT AND NPC EVENTS
        try:
            for Widget in self.FormSOLEventButtons.WidgetsList:
                self.FormSOLEventButtons.removeWidget(Widget)
            WidgetsList = []
            if PCLocation in Globals.Locations:
                ButtonList = Globals.Locations[PCLocation]["Reference"].GetLocationButtons(self, PCLocation)
                WidgetsList += ButtonList

            Layer, Row = 0, 0
            for Widget in WidgetsList:
                if Row > 4:
                    Row = 0
                    Layer += 1
                self.FormSOLEventButtons.addWidget(Widget, Layer, Row)
                self.FormSOLEventButtons.WidgetsList.append(Widget)
                Row += 1
            self.GroupBoxSolEventButtons.setMinimumHeight((Layer + 1)*45)
            if Layer >= 1:
                self.GroupBoxSolEventButtons.setMinimumWidth(870)
                self.GroupBoxSolEventButtons.setMaximumWidth(870)
            else:
                self.GroupBoxSolEventButtons.setMinimumWidth((Row)*174)
                self.GroupBoxSolEventButtons.setMaximumWidth((Row)*174)
        except Exception as e:
            Log(3, "ERROR SOL REFRESH SoLEventButtons", e)
            ""

        ### SETS UP THE CONTROL COMMANDS
        try:
            for Widget in self.FormControlCommands.WidgetsList:
                self.FormControlCommands.removeWidget(Widget)
            self.FormControlCommands.WidgetsList = []
            Layer, Row = 0, 0
            # Globals.Commands = { "Caress0":{"ID":"Caress0", "Reference":<module BasicCommands at 0x00f>, "OtherData":{}},  }
            for ControlID in Globals.ControlCommands:
                Available = Globals.ControlCommands[ControlID]["Reference"].CheckControlCommandAvailable(self, ControlID, PCID, NPCID, PCLocation)
                if Available == 1:
                    Button = Globals.ControlCommands[ControlID]["Reference"].GetContolCommandButton(self, ControlID, PCID, NPCID, PCLocation)
                    if Row > 4:
                        Row = 0
                        Layer += 1
                    self.FormControlCommands.addWidget(Button, Layer, Row)
                    self.FormControlCommands.WidgetsList.append(Button)
                    Row += 1
            self.GroupBoxControlCommands.setMinimumHeight((Layer + 1)*45)
            if Layer >= 1:
                self.GroupBoxControlCommands.setMinimumWidth(870)
                self.GroupBoxControlCommands.setMaximumWidth(870)
            else:
                self.GroupBoxControlCommands.setMinimumWidth((Row)*174)
                self.GroupBoxControlCommands.setMaximumWidth((Row)*174)
        except Exception as e:
            Log(3, "ERROR SOL REFRESH SoLControlButtons", e)
            ""

        self.GroupBoxPC.Height = 0
        ### SETS UP THE PC DATA TO THE LEFT
        try:
            for Widget in self.FormPC.WidgetsList:
                self.FormPC.removeWidget(Widget)
            self.FormPC.WidgetsList = []

            # CARD FOR THE PC
            PCID = Globals.SoLPCData["ID"]
            Object = GenericNPCObject(PCID)
            Widget = Object.GetWidget()
            self.FormPC.addWidget(Widget)
            self.FormPC.WidgetsList.append(Widget)
            self.GroupBoxPC.Height += Widget.height()
        except Exception as e:
            Log(3, "ERROR SOL REFRESH PCWidgets", e)
            ""

        # TARGET DATA
        try:
            TargetDataLabel = QLabel()
            TotalText = ''
            if NPCID != None:
                try:
                    for ValueID in Globals.SoLNPCData[NPCID]["Relations"][PCID]["Temporal"]:
                        if ValueID in Globals.SoLTValues:
                            try:
                                Text = Globals.SoLTValues[ValueID]["Reference"].GetValuesText(self, ValueID, PCID, NPCID)
                                TotalText += f'''{Text}<br/>'''
                            except Exception as e:
                                print("ERROR RETRIEVING TVALUE TEXT", e, ValueID)
                except:
                    ""
            TargetDataLabel.setText(TotalText)
            TargetDataLabel.setWordWrap(True)
            TargetDataLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
            scrollLabel = QScrollArea()
            scrollLabel.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            scrollLabel.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            scrollLabel.setWidgetResizable(True)
            scrollLabel.setMinimumWidth(350)
            scrollLabel.setMaximumWidth(350)
            scrollLabel.setMinimumHeight(150)
            scrollLabel.setMaximumHeight(150)
            scrollLabel.setStyleSheet('''
            QScrollArea{
            border: 1px solid black;
            background-color:rgb(23, 23, 23);
            }
            QLabel{
            border:none;
            }
            ''')
            scrollLabel.setWidget(TargetDataLabel)
            self.FormPC.addWidget(scrollLabel)
            self.FormPC.WidgetsList.append(scrollLabel)
            self.GroupBoxPC.Height += scrollLabel.height()
        except Exception as e:
            Log(3, "ERROR SOL REFRESH Target TValue", e)

        try:
            # FOR THE LOCATION OF FAVORITE NPC's
            FavoriteText = ""
            for NPCID in Globals.SoLTempData["FavoriteNPC"]:
                NPCName = Globals.SoLNPCData[NPCID]["Name"]

                NPCLocation = Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"]["Location"]
                LocationName = Globals.SoLEnviorementData["Locations"][NPCLocation]["Name"]
                FavoriteText += f"{NPCName}: {LocationName}<br>"

            FavLocationLabel = QLabel()
            FavLocationLabel.setText(FavoriteText)
            FavLocationLabel.setWordWrap(True)
            FavLocationLabel.setAlignment(Qt.AlignLeft | Qt.AlignTop)
            FavLocationScroll = QScrollArea()
            FavLocationScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            FavLocationScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            FavLocationScroll.setWidgetResizable(True)
            FavLocationScroll.setMinimumWidth(350)
            FavLocationScroll.setMaximumWidth(350)
            FavLocationScroll.setMinimumHeight(150)
            FavLocationScroll.setMaximumHeight(150)
            FavLocationScroll.setWidget(FavLocationLabel)
            self.FormPC.addWidget(FavLocationScroll)
            self.FormPC.WidgetsList.append(FavLocationScroll)
            self.GroupBoxPC.Height += FavLocationScroll.height()
        except Exception as e:
            Log(3, "ERROR SOL REFRESH Favorite Location", e)
            ""

        self.GroupBoxPC.setMinimumHeight(self.GroupBoxPC.Height + 30)
        self.GroupBoxPC.setMaximumHeight(self.GroupBoxPC.Height + 30)

        self.RefreshSignal2.emit()

        ### REFRESHES THE FLAVOR TEXT
        try:
            Hour, Day, Month, Year = GetDate(self)
            self.labelStatus.setText(f'''{Hour}            {Day} {Globals.SoLEnviorementData["DateData"]["Day"]}  {Month} {Year}''')
            GetFlavorText(self)

            TotalFlavor = ""
            for Text in Globals.SoLFlavorDict["EnviorementFlavor"]:
                TotalFlavor += Text
            else:
                if len(Globals.SoLFlavorDict["EnviorementFlavor"]) > 0:
                    TotalFlavor += "<br/><br/>"
                Globals.SoLFlavorDict["EnviorementFlavor"] = []

            for Text in Globals.SoLFlavorDict["PCActionsFlavor"]:
                TotalFlavor += Text
            else:
                if len(Globals.SoLFlavorDict["PCActionsFlavor"]) > 0:
                    TotalFlavor += "<br/><br/>"
                Globals.SoLFlavorDict["PCActionsFlavor"] = []

            for Text in Globals.SoLFlavorDict["PCTargetFlavor"]:
                TotalFlavor += Text
            else:
                if len(Globals.SoLFlavorDict["PCTargetFlavor"]) > 0:
                    TotalFlavor += "<br/><br/>"
                Globals.SoLFlavorDict["PCTargetFlavor"] = []

            for Text in Globals.SoLFlavorDict["NPCActionsFlavor"]:
                TotalFlavor += Text
            else:
                if len(Globals.SoLFlavorDict["NPCActionsFlavor"]) > 0:
                    TotalFlavor += "<br/><br/>"
                Globals.SoLFlavorDict["NPCActionsFlavor"] = []

            self.labelMain.setText(TotalFlavor)

        except Exception as e:
            Log(3, "ERROR SOL REFRESH labelMain", e)
            ""

        self.RefreshSignal3.emit()

    except Exception as e:
        Log(4, "ERROR SOL REFRESH", e)

def CommandsProcessing(self, TargetDict, ActorDict, CommandID, Target, Actor, Modification, Implementation):
    try:
        ActorName = Globals.SoLNPCData[Actor]["Name"]
        TargetName = Globals.SoLNPCData[Target]["Name"]
        # PACKS UP ORIGINAL DATA
        OriginalData = {"TargetDict":TargetDict, "ActorDict":ActorDict, "CommandID":CommandID, "Target":Target, "Actor":Actor, "Modification":Modification, "Implementation":Implementation}
        FinalData = {"TargetDict":TargetDict, "ActorDict":ActorDict, "CommandID":CommandID, "Target":Target, "Actor":Actor, "Modification":Modification, "Implementation":Implementation}

        # CHECKS IF THE CHARACTER ALREADY SHARE A RELATIONSHIP
        if Actor not in Globals.SoLNPCData[Target]["Relations"]:
            Globals.SoLNPCData[Target]["Relations"][Actor] = copy.deepcopy(Globals.SoLOtherData["baseRelationship"])
        if Target not in Globals.SoLNPCData[Actor]["Relations"]:
            Globals.SoLNPCData[Actor]["Relations"][Target] = copy.deepcopy(Globals.SoLOtherData["baseRelationship"])


        # CPS1.EMIT


        # SENDS THE DATA TO BE PROCESSED BY TRAITS
        for TraitID in Globals.SoLTraits:
            OriginalData, FinalData = Globals.SoLTraits[TraitID]["Reference"].CommandProcessTrait(self, OriginalData, FinalData, TraitID)

        # SENDS THE DATA TO BE PROCESSED BY ABILITIES
        for AbilityID in Globals.SoLAbilities:
            OriginalData, FinalData = Globals.SoLAbilities[AbilityID]["Reference"].CommandProcessAbility(self, OriginalData, FinalData, AbilityID)


        # CPS2.EMIT


        # SENDS THE DATA TO THE CHARACTER FUNCTION
        TargetUsePersonality = 1
        try:
            TargetFile = f'''{TargetName}{Target}Function.py'''
            if TargetFile[:-3] not in Globals.References:
                TargetPath = f'''NPCdata/{TargetName}{Target}'''
                if TargetPath not in sys.path:
                    sys.path.insert(0, TargetPath)
                TargetReference = __import__(TargetFile[:-3])
                Globals.References[TargetFile[:-3]] = TargetReference
                FinalData, TargetUsePersonality = TargetReference.CommandProcessFunction(self, FinalData, "Target")
        except Exception as e:
            ""

        ActorUsePersonality = 1
        try:
            ActorFile = f'''{ActorName}{Actor}Function.py'''
            if ActorFile[:-3] not in Globals.References:
                ActorPath = f'''NPCdata/{ActorName}{Actor}'''
                if ActorPath not in sys.path:
                    sys.path.insert(0, ActorPath)
                ActorReference = __import__(ActorFile[:-3])
                Globals.References[ActorFile[:-3]] = ActorReference
                FinalData, ActorUsePersonality = ActorReference.CommandProcessFunction(self, FinalData, "Actor")
        except Exception as e:
            ""

        # SENDS THE DATA TO THE PERSONALITIES
        if TargetUsePersonality == 1:
            Personality = Globals.SoLNPCData[Target]["Personality"]
            if Personality in Globals.SoLPersonalities:
                FinalData,  = Globals.SoLPersonalities[Personality]["Reference"].CommandProcessPersonality(self, FinalData, "Target")

        if ActorUsePersonality == 1:
            Personality = Globals.SoLNPCData[Actor]["Personality"]
            if Personality in Globals.SoLPersonalities:
                FinalData,  = Globals.SoLPersonalities[Personality]["Reference"].CommandProcessPersonality(self, FinalData, "Actor")


        # CPS3.EMIT


        # CHECKS FOR ENERGY AND RESISTANCE
        ResistancePass, EnergyPass = 0, 9
        if TargetDict["Resistance"] <= 0:
            ResistancePass = 1
        if (TargetDict["State"]["Energy"]*-1) <= Globals.SoLNPCData[Target]["State"]["Energy"]:
            EnergyPass = 1
        # ResistancePass, EnergyPass = 1, 1

        CommandStatus = ""
        if ResistancePass == 1 and EnergyPass == 1:
            CommandStatus = "Success"
            TargetTask = TargetDict["Task"]
            ActorTask = ActorDict["Task"]
        elif EnergyPass == 0:
            CommandStatus = "EnergyFailed"
            TargetTask = TargetDict["EnergyTask"]
            ActorTask = ActorDict["EnergyTask"]
        elif ResistancePass == 0:
            CommandStatus = "ResistanceFailed"
            TargetTask = TargetDict["ResistanceTask"]
            ActorTask = ActorDict["ResistanceTask"]
        FinalData["CommandStatus"] = CommandStatus
        FinalData["TargetTask"] = TargetTask
        FinalData["ActorTask"] = ActorTask


        # CPS4.EMIT


        # WRITES THE VALUES

        if ResistancePass == 1 and EnergyPass == 1:
            # TARGET
            for ValueID in FinalData["TargetDict"]["State"]:
                if ValueID in Globals.SoLNPCData[Target]["State"]:
                    Globals.SoLNPCData[Target]["State"][ValueID] += FinalData["TargetDict"]["State"][ValueID]
                else:
                    Globals.SoLNPCData[Target]["State"][ValueID] = FinalData["TargetDict"]["State"][ValueID]

            for ValueID in FinalData["TargetDict"]["Temporal"]:
                try:
                    if ValueID not in Globals.SoLNPCData[Target]["Relations"][Actor]["Temporal"] or type(Globals.SoLNPCData[Target]["Relations"][Actor]["Temporal"][ValueID]) == int:
                        Globals.SoLNPCData[Target]["Relations"][Actor]["Temporal"][ValueID] = Globals.SoLTValues[ValueID]["BaseData"].copy()

                    Globals.SoLNPCData[Target]["Relations"][Actor]["Temporal"][ValueID]["Amount"] += FinalData["TargetDict"]["Temporal"][ValueID]
                except Exception as e:
                    Log(3, "ERROR WRITTING TVALUE", e, ValueID)

            for ValueID in FinalData["TargetDict"]["Permanent"]:
                if ValueID in Globals.SoLNPCData[Target]["Relations"][Actor]["Permanent"]:
                    Globals.SoLNPCData[Target]["Relations"][Actor]["Permanent"][ValueID] += FinalData["TargetDict"]["Permanent"][ValueID]
                else:
                    Globals.SoLNPCData[Target]["Relations"][Actor]["Permanent"][ValueID] = FinalData["TargetDict"]["Permanent"][ValueID]

            # ACTOR
            for ValueID in FinalData["ActorDict"]["State"]:
                if ValueID in Globals.SoLNPCData[Actor]["State"]:
                    Globals.SoLNPCData[Actor]["State"][ValueID] += FinalData["ActorDict"]["State"][ValueID]
                else:
                    Globals.SoLNPCData[Actor]["State"][ValueID] = FinalData["ActorDict"]["State"][ValueID]

            for ValueID in FinalData["ActorDict"]["Temporal"]:
                try:
                    if ValueID not in Globals.SoLNPCData[Actor]["Relations"][Target]["Temporal"] or type(Globals.SoLNPCData[Actor]["Relations"][Target]["Temporal"][ValueID]) == int:
                        Globals.SoLNPCData[Actor]["Relations"][Target]["Temporal"][ValueID] = Globals.SoLTValues[ValueID]["BaseData"].copy()

                    Globals.SoLNPCData[Actor]["Relations"][Target]["Temporal"][ValueID]["Amount"] += FinalData["ActorDict"]["Temporal"][ValueID]
                except Exception as e:
                    Log(3, "ERROR WRITTING TVALUE", e, ValueID)

            for ValueID in FinalData["ActorDict"]["Permanent"]:
                if ValueID in Globals.SoLNPCData[Actor]["Relations"][Target]["Permanent"]:
                    Globals.SoLNPCData[Actor]["Relations"][Target]["Permanent"][ValueID] += FinalData["ActorDict"]["Permanent"][ValueID]
                else:
                    Globals.SoLNPCData[Actor]["Relations"][Target]["Permanent"][ValueID] = FinalData["ActorDict"]["Permanent"][ValueID]

            try:
                Globals.SoLNPCData[Actor]["Relations"][Target]["Permanent"]["InteractionExp"] += 1
            except:
                Globals.SoLNPCData[Actor]["Relations"][Target]["Permanent"]["InteractionExp"] = 1

            try:
                Globals.SoLNPCData[Target]["Relations"][Actor]["Permanent"]["InteractionExp"] += 1
            except:
                Globals.SoLNPCData[Target]["Relations"][Actor]["Permanent"]["InteractionExp"] = 1

            if Target not in Globals.SoLNPCData[Actor]["Actions"]["InteractionParty"] or Globals.SoLNPCData[Actor]["Actions"]["InteractionParty"][Target] < 3:
                Globals.SoLNPCData[Actor]["Actions"]["InteractionParty"][Target] = 3
            if Actor not in Globals.SoLNPCData[Target]["Actions"]["InteractionParty"] or Globals.SoLNPCData[Target]["Actions"]["InteractionParty"][Actor] < 3:
                Globals.SoLNPCData[Target]["Actions"]["InteractionParty"][Actor] = 3

        elif EnergyPass == 0:
            # TARGET
            for ValueID in FinalData["TargetDict"]["State"]:
                if ValueID in Globals.SoLNPCData[Target]["State"]:
                    Globals.SoLNPCData[Target]["State"][ValueID] += FinalData["TargetDict"]["State"][ValueID]
                else:
                    Globals.SoLNPCData[Target]["State"][ValueID] = FinalData["TargetDict"]["State"][ValueID]

            for ValueID in FinalData["TargetDict"]["Temporal"]:
                try:
                    if ValueID not in Globals.SoLNPCData[Target]["Relations"][Actor]["Temporal"] or type(Globals.SoLNPCData[Target]["Relations"][Actor]["Temporal"][ValueID]) == int:
                        Globals.SoLNPCData[Target]["Relations"][Actor]["Temporal"][ValueID] = Globals.SoLTValues[ValueID]["BaseData"].copy()

                    Globals.SoLNPCData[Target]["Relations"][Actor]["Temporal"][ValueID]["Amount"] += int(FinalData["TargetDict"]["Temporal"][ValueID] / 2)
                except Exception as e:
                    Log(3, "ERROR WRITTING TVALUE", e, ValueID)

            # ACTOR
            for ValueID in FinalData["ActorDict"]["State"]:
                if ValueID in Globals.SoLNPCData[Actor]["State"]:
                    Globals.SoLNPCData[Actor]["State"][ValueID] += FinalData["ActorDict"]["State"][ValueID]
                else:
                    Globals.SoLNPCData[Actor]["State"][ValueID] = FinalData["ActorDict"]["State"][ValueID]

            for ValueID in FinalData["ActorDict"]["Temporal"]:
                try:
                    if ValueID not in Globals.SoLNPCData[Actor]["Relations"][Target]["Temporal"] or type(Globals.SoLNPCData[Actor]["Relations"][Target]["Temporal"][ValueID]) == int:
                        Globals.SoLNPCData[Actor]["Relations"][Target]["Temporal"][ValueID] = Globals.SoLTValues[ValueID]["BaseData"].copy()

                    Globals.SoLNPCData[Actor]["Relations"][Target]["Temporal"][ValueID]["Amount"] += int(FinalData["ActorDict"]["Temporal"][ValueID] / 2)
                except Exception as e:
                    Log(3, "ERROR WRITTING TVALUE", e, ValueID)

            try:
                Globals.SoLNPCData[Actor]["Relations"][Target]["Permanent"]["InteractionExp"] += 1
            except:
                Globals.SoLNPCData[Actor]["Relations"][Target]["Permanent"]["InteractionExp"] = 1

            try:
                Globals.SoLNPCData[Target]["Relations"][Actor]["Permanent"]["InteractionExp"] += 1
            except:
                Globals.SoLNPCData[Target]["Relations"][Actor]["Permanent"]["InteractionExp"] = 1

            if Target not in Globals.SoLNPCData[Actor]["Actions"]["InteractionParty"] or Globals.SoLNPCData[Actor]["Actions"]["InteractionParty"][Target] < 3:
                Globals.SoLNPCData[Actor]["Actions"]["InteractionParty"][Target] = 3
            if Actor not in Globals.SoLNPCData[Target]["Actions"]["InteractionParty"] or Globals.SoLNPCData[Target]["Actions"]["InteractionParty"][Actor] < 3:
                Globals.SoLNPCData[Target]["Actions"]["InteractionParty"][Actor] = 3
        else:
            # TARGET
            try:
                Globals.SoLNPCData[Target]["State"]["Mood"] -= 5
                if Globals.SoLNPCData[Target]["State"]["Mood"] < -100:
                    Globals.SoLNPCData[Target]["State"]["Mood"] = -100
            except:
                ""
            for ValueID in FinalData["TargetDict"]["Temporal"]:
                if ValueID in ["Discomfort","Hate"]:
                    try:
                        if ValueID not in Globals.SoLNPCData[Target]["Relations"][Actor]["Temporal"] or type(Globals.SoLNPCData[Target]["Relations"][Actor]["Temporal"][ValueID]) == int:
                            Globals.SoLNPCData[Target]["Relations"][Actor]["Temporal"][ValueID] = Globals.SoLTValues[ValueID]["BaseData"].copy()

                        Globals.SoLNPCData[Target]["Relations"][Actor]["Temporal"][ValueID]["Amount"] += FinalData["TargetDict"]["Temporal"][ValueID]
                    except Exception as e:
                        Log(3, "ERROR WRITTING TVALUE", e, ValueID)

            # ACTOR
            for ValueID in FinalData["ActorDict"]["Temporal"]:
                if ValueID in ["Discomfort","Hate"]:
                    try:
                        if ValueID not in Globals.SoLNPCData[Actor]["Relations"][Target]["Temporal"] or type(Globals.SoLNPCData[Actor]["Relations"][Target]["Temporal"][ValueID]) == int:
                            Globals.SoLNPCData[Actor]["Relations"][Target]["Temporal"][ValueID] = Globals.SoLTValues[ValueID]["BaseData"].copy()

                        Globals.SoLNPCData[Actor]["Relations"][Target]["Temporal"][ValueID]["Amount"] += FinalData["ActorDict"]["Temporal"][ValueID]
                    except Exception as e:
                        Log(3, "ERROR WRITTING TVALUE", e, ValueID)

        for OtherID in list(Globals.SoLNPCData[Actor]["Actions"]["InteractionParty"].keys()):
            if Globals.SoLNPCData[Actor]["Actions"]["InteractionParty"] != Target:
                Globals.SoLNPCData[Actor]["Actions"]["InteractionParty"][OtherID] -= 1
                if Globals.SoLNPCData[Actor]["Actions"]["InteractionParty"][OtherID] <= 0:
                    Globals.SoLNPCData[Actor]["Actions"]["InteractionParty"].pop(OtherID)

        for OtherID in list(Globals.SoLNPCData[Target]["Actions"]["InteractionParty"].keys()):
            if Globals.SoLNPCData[Target]["Actions"]["InteractionParty"] != Actor:
                Globals.SoLNPCData[Target]["Actions"]["InteractionParty"][OtherID] -= 1
                if Globals.SoLNPCData[Target]["Actions"]["InteractionParty"][OtherID] <= 0:
                    Globals.SoLNPCData[Target]["Actions"]["InteractionParty"].pop(OtherID)


        Globals.SoLNPCData[Target]["Actions"]["PreviousTask"] = Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]
        Globals.SoLNPCData[Target]["Actions"]["CurrentTask"] = FinalData["TargetTask"]

        Globals.SoLNPCData[Actor]["Actions"]["PreviousTask"] = Globals.SoLNPCData[Actor]["Actions"]["CurrentTask"]
        Globals.SoLNPCData[Actor]["Actions"]["CurrentTask"] = FinalData["ActorTask"]



        if Actor == Globals.SoLPCData["ID"]:
            # GETS THE FLAVOR TEXT
            Flags = {"UseCommandsText":1, "UseCustomText":1}
            CustomText = ""
            if Target in Globals.SoLNPCFunctions:
                CustomText, FinalData, Flags = Globals.SoLNPCFunctions[Target].getFlavorText(self, CustomText, FinalData, Flags)
            else:
                try:
                    CustomText, FinalData, Flags = getGenericFlavorText(self, CustomText, FinalData, Flags)
                except:
                    CustomText = ""
            if Flags["UseCommandsText"] == 1:
                CommandText = FinalData["TargetTask"]["Task"][1]["LongFluff"]
                Globals.SoLFlavorDict["PCActionsFlavor"].append(CommandText)
            if Flags["UseCustomText"] == 1:
                Globals.SoLFlavorDict["PCActionsFlavor"].append(CustomText)

            # IF THE NPC IS GENERIC, THEN IT REMOVES THEM SO THEY ARE PERMANENT
            if Target in Globals.SoLTempData["TempNPC"]: Globals.SoLTempData["TempNPC"].remove(Target)


            # PASSESE THE TIME
            Time = FinalData["ActorTask"]["HourFinish"] - FinalData["ActorTask"]["HourStart"]
            PassTime(self, Time)

        # print("COMMAND PASS")
        return FinalData
    except Exception as e:
        # TargetDict, ActorDict, CommandID, Target, Actor, Modification, Implementation
        Log(5, "ERROR COMMAND PROCESSING", e, CommandID, Modification, Implementation, Target, Actor, TargetDict, ActorDict)
        # print(e)

    # CPS5.EMIT

def Move(self, Location, NPCID):
    # curframe = inspect.currentframe()
    # calframe = inspect.getouterframes(curframe, 2)
    # print('caller name:', calframe[1][3])

    # TODO Investigate why this doesn't work
    # print("MOVED", NPCID, Location)
    # PreLocation = Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"]["Location"]
    # try:
    #     Globals.SoLEnviorementData["Locations"][PreLocation]["inHere"].remove(NPCID)
    # except Exception as e:
    #     # print(1, e, NPCID, PreLocation, Globals.SoLEnviorementData["Locations"][PreLocation]["inHere"])
    #     ""
    ### PATCH
    for OtherLocation in Globals.SoLEnviorementData["Locations"]:
        if OtherLocation != Location and NPCID in Globals.SoLEnviorementData["Locations"][OtherLocation]["inHere"]:
            Globals.SoLEnviorementData["Locations"][OtherLocation]["inHere"].remove(NPCID)


    Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"]["Location"] = Location
    try:
        if NPCID not in Globals.SoLEnviorementData["Locations"][Location]["inHere"]: Globals.SoLEnviorementData["Locations"][Location]["inHere"].append(NPCID)
    except Exception as e:
        # print(1, e, Location, Globals.SoLEnviorementData["Locations"][Location]["inHere"])
        ""


    for NPCOther in Globals.SoLNPCData[NPCID]["Actions"]["HasFollowing"]:
        if NPCOther not in Globals.SoLEnviorementData["Locations"][Location]["inHere"]:
            Move(self, Location, NPCOther)

    if NPCID == Globals.SoLPCData["ID"]:
        if Globals.SoLPCData["Targeting"] not in Globals.SoLEnviorementData["Locations"][Location]["inHere"]:
            Globals.SoLPCData["Targeting"] = None
        Refresh(self)
    else:
        if Globals.SoLPCData["Targeting"] == NPCID:
            Globals.SoLPCData["Targeting"] = None


def Switch(self, NPCID):
    PCID = Globals.SoLPCData["ID"]
    Globals.SoLPCData["ID"] = NPCID
    Globals.References["SoLFunctions"].Refresh(Globals.Layouts["SoLUI"])
def PassTime(self, Amount):
    for i in range(Amount):
        Globals.SoLEnviorementData["DateData"]["Hour"] +=1
        if Globals.SoLEnviorementData["DateData"]["Hour"] >= 1440:
            Globals.SoLEnviorementData["DateData"]["Hour"] = 0
            Globals.SoLEnviorementData["DateData"]["DaysPlayed"] += 1

            Globals.SoLEnviorementData["DateData"]["Day"] += 1
            if Globals.SoLEnviorementData["DateData"]["Day"] > 30:
                Globals.SoLEnviorementData["DateData"]["Day"] = 1

                Globals.SoLEnviorementData["DateData"]["Month"] += 1
                if Globals.SoLEnviorementData["DateData"]["Month"] > 12:
                    Globals.SoLEnviorementData["DateData"]["Month"] = 1
                    Globals.SoLEnviorementData["DateData"]["Year"] += 1

        # CheckNPCActions(self)

        Globals.SignalData["TPS"] = {}
        Globals.References["SoLFunctions"].Emit("TPS")


    Refresh(self)
def GetDate(self):
    RawHour = Globals.SoLEnviorementData["DateData"]["Hour"]
    RawDay = Globals.SoLEnviorementData["DateData"]["Day"]
    RawMonth = Globals.SoLEnviorementData["DateData"]["Month"]
    RawYear = Globals.SoLEnviorementData["DateData"]["Year"]

    Hour = f'''{RawHour//60}: {RawHour%60}'''

    if RawDay % 7 == 0: Day = "Sunday"
    elif RawDay % 7 == 1: Day = "Monday"
    elif RawDay % 7 == 2: Day = "Tuesday"
    elif RawDay % 7 == 3: Day = "Wednesday"
    elif RawDay % 7 == 4: Day = "Thursday"
    elif RawDay % 7 == 5: Day = "Friday"
    elif RawDay % 7 == 6: Day = "Saturday"
    else: Day = "???"

    if RawMonth == 1: Month = "January"
    elif RawMonth == 2: Month = "February"
    elif RawMonth == 3: Month = "March"
    elif RawMonth == 4: Month = "April"
    elif RawMonth == 5: Month = "May"
    elif RawMonth == 6: Month = "June"
    elif RawMonth == 7: Month = "July"
    elif RawMonth == 8: Month = "August"
    elif RawMonth == 9: Month = "September"
    elif RawMonth == 10: Month = "October"
    elif RawMonth == 11: Month = "November"
    elif RawMonth == 12: Month = "December"
    else: Month = "???"

    Year = RawYear

    return Hour, Day, Month, Year
    ""
def ToggleFavorite(NPCID):
    try:
        if NPCID in Globals.SoLTempData["FavoriteNPC"]: Globals.SoLTempData["FavoriteNPC"].remove(NPCID)
        else: Globals.SoLTempData["FavoriteNPC"].append(NPCID)
    except Exception as e:
        print(e)

def CheckButtonFontSize(self, Button):
    if Button.fontMetrics().boundingRect(Button.text()).height() > Button.rect().height() or Button.fontMetrics().boundingRect(Button.text()).width() > Button.rect().width():
        ButtonH = Button.rect().height()
        ButtonW = Button.rect().width()
        font = Button.property("font")
        while True:
            TextH = Button.fontMetrics().boundingRect(Button.text()).height()
            TextW = Button.fontMetrics().boundingRect(Button.text()).width()

            newSize = font.pointSizeF() - 1
            font.setPointSizeF(newSize);
            Button.setFont(font)
            if TextH < ButtonH and TextW < ButtonW:
                break
def AdjustSize(Widget):
    Font = Globals.Layouts["MainF"].StyleData(Widget, "Font")
    FontSize = Globals.Layouts["MainF"].StyleData(Widget, "FontSize")
    ObjectWidth = Widget.width()
    ObjectHeight = Widget.height()
    if Font != None and FontSize != None:
        Text = Widget.text()
        if "<" in Text and ">" in Text:
            ""
            # CleanText = ""
            # OpIndices = [m.start() for m in re.finditer("<", Text)]
            # ClIndices = [m.start() for m in re.finditer(">", Text)]
            # CleanText = ""
            # for i in range(len(OpIndices)):
            #     if i == 0:
            #         CleanText =  Text[0:OpIndices[0]]
            #     else:
            #         try:
            #             CleanText += Text[ClIndices[i-1]+1:OpIndices[i]]
            #         except:
            #             ""
            # else:
            #     CleanText += Text[ClIndices[-1]+1:]
            #
            #
            # TempText = "" + Text
            # TempText = TempText.replace("<br/>", r"/n")
            # OpIndices = [m.start() for m in re.finditer("<", TempText)]
            # ClIndices = [m.start() for m in re.finditer(">", TempText)]
            # SemiCleanText = ""
            # for i in range(len(OpIndices)):
            #     if i == 0:
            #         SemiCleanText =  TempText[0:OpIndices[0]]
            #     else:
            #         try:
            #             SemiCleanText += TempText[ClIndices[i-1]+1:OpIndices[i]]
            #         except:
            #             ""
            # if SemiCleanText == "":
            #     SemiCleanText = TempText
            # BreakIndices = [m.start() for m in re.finditer(r"/n", SemiCleanText)]
        elif "\n" in Text:
            ""


            print(Text)
            print(Font, FontSize)
        else:
            Font = QFont(Font, FontSize)
            FM = QFontMetrics(Font)
            BR = FM.boundingRect(Text)
            FontWidth = BR.width()
            FontHeight = BR.height()
            if ObjectWidth >  FontWidth:
                if FontHeight > ObjectHeight:
                    return FontHeight
                else:
                    return ObjectHeight
            else:
                Lines = math.ceil( FontWidth / ObjectWidth )
                TotalHeight = Lines * FontHeight
                if TotalHeight > ObjectHeight:
                    return TotalHeight
                else:
                    return ObjectHeight
def GridLayoutMaker(self, Layout, WidgetsDict, MaxWidth, Separation):
    Height = 0
    Width = 0

    TotalHeight, TotalWidth = 0,0
    Layer, Row = 0,0

    LineHeight = 0
    LineWidth = 0
    if len(WidgetsDict) > 0:
        for ValueID in WidgetsDict:
            Object = WidgetsDict[ValueID]
            ObjectWidth = Object.width()
            ObjectHeight = Object.height()

            if LineWidth + ObjectWidth > MaxWidth:
                Layer += 1
                Row = 0

                TotalHeight += LineHeight + Separation

                LineHeight = 0
                LineWidth = 0

            Layout.addWidget(WidgetsDict[ValueID], Layer, Row)
            LineWidth += ObjectWidth + 5

            if ObjectHeight > LineHeight:
                LineHeight = ObjectHeight
            Row += 1
        else:
            TotalHeight += LineHeight + Separation


        if Layer > 0:
            Width = MaxWidth
        else:
            Width = LineWidth
        Height = TotalHeight
    # Width += 5
    return Width, Height
def GetImages(NPCData):
    ListPortraits, ListFullBody = [], []
    try:
        ID = NPCData["ID"]
        Name = NPCData["Name"]

        Files = os.listdir(f'''NPCdata/{Name}{ID}''')

        list = [File for File in Files if File.endswith((".png")) or File.endswith((".jpg")) or File.endswith((".jpeg"))]
        ListPortraits, ListFullBody = [], []
        ListPortraits = [File for File in list if File.startswith("Portrait")]
        ListFullBody = [File for File in list if File.startswith("FullBody")]
    except:
        ""

    return ListPortraits, ListFullBody
    # if ImageType == "Portrait" or ListFullBody == []:
    #     ImageName = random.choice(ListPortraits)
    # if ImageType == "FullBody" or ListPortraits == []:
    #     ImageName = random.choice(ListFullBody)
def GetGenericImage(NPCData):
    # Male_Human_2_Fair_Black_Androgynous_Muscular_1

    Race = NPCData["BodyData"]["Race"]
    Sex = NPCData["BodyData"]["Sex"]
    PhysicalAge = NPCData["BodyData"]["PhysicalAge"]
    SkinColor = NPCData["BodyData"]["SkinColor"]
    HairColor = NPCData["BodyData"]["HairColor"]
    Face = NPCData["BodyData"]["Face"]
    Complexion = NPCData["BodyData"]["Complexion"]

    FullImagesList = os.listdir("images/Generic")
    T0Text = f'''{Race}_{Sex}_{PhysicalAge}_{SkinColor}_{HairColor}_{Face}_{Complexion}'''
    T1Text = f'''{Race}_{Sex}_{PhysicalAge}_{SkinColor}_{HairColor}_{Face}'''
    T2Text = f'''{Race}_{Sex}_{PhysicalAge}_{SkinColor}_{HairColor}'''

    T0List = [k for k in FullImagesList if T0Text in k]
    T1List = [k for k in FullImagesList if T1Text in k]
    T2List = [k for k in FullImagesList if T2Text in k]

    PortraitList = []
    FullBodyList = []

    if T0List != []:
        PortraitList = [k for k in T0List if "Portrait" in k]
        FullBodyList = [k for k in T0List if "FullBody" in k]
    if T1List != []:
        if PortraitList == []: PortraitList = [k for k in T0List if "Portrait" in k]
        if FullBodyList == []: FullBodyList = [k for k in T0List if "FullBody" in k]
    if T2List != []:
        if PortraitList == []: PortraitList = [k for k in T0List if "Portrait" in k]
        if FullBodyList == []: FullBodyList = [k for k in T0List if "FullBody" in k]

    return PortraitList, FullBodyList

def ResetGenericNPC():
    for NPCID in Globals.SoLTempData["TempNPC"]:
        RemoveNPC(NPCID)
    Globals.SoLTempData["TempNPC"] = []

    NPCAmount = 15
    # Globals.SoLNPCData["005"] = {"ID":"005"}
    NameList = ["A", "B"]
    SkinList = ["A", "B"]
    HairList = ["A", "B"]

    for i in range(NPCAmount):
        try:
            try:
                NPCID = "00" + str(max( [int(k) for k in Globals.SoLNPCData if Globals.SoLNPCData[k]["ID"].startswith("00")] ) + 1)
            except Exception as e:
                NPCID = "001"

            Sex = random.choice(["Male","Female"])
            Globals.SoLNPCData[NPCID] = copy.deepcopy(Globals.SoLOtherData["BaseData"])
            Globals.SoLNPCData[NPCID]["Name"] = "R" + Sex[0:1] + "C " + NPCID
            Globals.SoLNPCData[NPCID]["ID"] = NPCID
            Globals.SoLNPCData[NPCID]["Personality"] = "Standard0"

            Energy = random.randrange(500,2000)
            Globals.SoLNPCData[NPCID]["State"]["Energy"] = Energy

            Globals.SoLNPCData[NPCID]["BodyData"]["FullName"] = "R" + Sex[0:1] + "C " + NPCID
            Globals.SoLNPCData[NPCID]["BodyData"]["SkinColor"] = random.choice(["Fair"])
            Globals.SoLNPCData[NPCID]["BodyData"]["HairColor"] = random.choice(["Black"])
            Globals.SoLNPCData[NPCID]["BodyData"]["PhysicalAge"] = random.randrange(0,7)
            Globals.SoLNPCData[NPCID]["BodyData"]["Race"] = "Human"

            if Sex == "Male":
                Globals.SoLNPCData[NPCID]["BodyData"]["Face"] = random.randrange(0,4)
                Globals.SoLNPCData[NPCID]["BodyData"]["Pronouns"] = {"PSub":"He", "PObj":"Him", "PPos":"His", "PIPos":"His"}
                Globals.SoLNPCData[NPCID]["BodyData"]["Chest"] = random.randrange(0,1)
                Globals.SoLNPCData[NPCID]["BodyData"]["VTightness"] = 0
                Globals.SoLNPCData[NPCID]["BodyData"]["PenisSize"] = random.randrange(1,5)
                Globals.SoLNPCData[NPCID]["BodyData"]["BallsSize"] = random.randrange(1,5)
                Globals.SoLNPCData[NPCID]["BodyData"]["VVirgin"] = 1
                Globals.SoLNPCData[NPCID]["BodyData"]["PVirgin"] = 1
            else:
                Globals.SoLNPCData[NPCID]["BodyData"]["Face"] = random.randrange(2,6)
                Globals.SoLNPCData[NPCID]["BodyData"]["Pronouns"] = {"PSub":"She", "PObj":"Her", "PPos":"Her", "PIPos":"Hers"}
                Globals.SoLNPCData[NPCID]["BodyData"]["Chest"] = random.randrange(2,7)
                Globals.SoLNPCData[NPCID]["BodyData"]["VTightness"] = random.randrange(1,5)
                Globals.SoLNPCData[NPCID]["BodyData"]["PenisSize"] = 0
                Globals.SoLNPCData[NPCID]["BodyData"]["BallsSize"] = 0
                Globals.SoLNPCData[NPCID]["BodyData"]["VVirgin"] = 1
                Globals.SoLNPCData[NPCID]["BodyData"]["PVirgin"] = 1

            Globals.SoLNPCData[NPCID]["BodyData"]["Eyes"] = "Hazel"
            Globals.SoLNPCData[NPCID]["BodyData"]["Lips"] = random.randrange(0,4)
            Globals.SoLNPCData[NPCID]["BodyData"]["Height"] = random.randrange(0,6)
            Globals.SoLNPCData[NPCID]["BodyData"]["Complexion"] = random.randrange(0,6)
            Globals.SoLNPCData[NPCID]["BodyData"]["Sex"] = Sex
            Globals.SoLNPCData[NPCID]["BodyData"]["Hips"] = random.randrange(0,5)
            Globals.SoLNPCData[NPCID]["BodyData"]["Ass"] = random.randrange(0,6)
            Globals.SoLNPCData[NPCID]["BodyData"]["ATightness"] = random.randrange(1,5)
            Globals.SoLNPCData[NPCID]["BodyData"]["AVirgin"] = 1
            Globals.SoLNPCData[NPCID]["BodyData"]["MVirgin"] = 1


            Globals.SoLNPCData[NPCID]["GeneralAbilities"]["MaxEnergy"] = Energy

            Globals.SoLNPCData[NPCID]["Descriptions"]["Backstory"] = ""
            Globals.SoLNPCData[NPCID]["Descriptions"]["Core"] = ""
            Globals.SoLNPCData[NPCID]["Descriptions"]["Head"] = ""
            Globals.SoLNPCData[NPCID]["Descriptions"]["Arms"] = ""
            Globals.SoLNPCData[NPCID]["Descriptions"]["Legs"] = ""
            Globals.SoLNPCData[NPCID]["Descriptions"]["Genitals"] = ""

            Globals.SoLNPCData[NPCID]["Actions"]["PreviousTask"] = Globals.SoLOtherData["IdlingTask"]
            Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"] = Globals.SoLOtherData["IdlingTask"]
            Globals.SoLNPCData[NPCID]["Actions"]["FutureTask"] = Globals.SoLOtherData["IdlingTask"]

            NPCList = Globals.SoLEnviorementData["Locations"]["ResidentialArea"]["inHere"].append(NPCID)
            Globals.SoLTempData["TempNPC"].append(NPCID)
        except:
            ""

    # for NPCID in Globals.SoLNPCData:
    #     Name = Globals.SoLNPCData[NPCID]["Name"]
    #     Location = Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"]["Location"]
    #     print(Name, Location)

def RemoveNPC(NPCID):
    if NPCID == Globals.SoLPCData["Targeting"]:
        Globals.SoLPCData["Targeting"] = None

    # Removes them from the inHere
    Location = Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"]["Location"]
    if NPCID in Globals.SoLEnviorementData["Locations"][Location]["inHere"]: Globals.SoLEnviorementData["Locations"][Location]["inHere"].remove(NPCID)

    # Removes them fron the relations
    for OtherID in Globals.SoLNPCData[NPCID]["Relations"]:
        if NPCID in Globals.SoLNPCData[OtherID]["Relations"]: Globals.SoLNPCData[OtherID]["Relations"].pop(NPCID)

    # Removes them from the dict
    Globals.SoLNPCData.pop(NPCID)
def ImportNPC(NPCData):
    try:
        NPCID = NPCData["ID"]
        Globals.SoLNPCData[NPCID] = NPCData

        Name = NPCData["Name"]
        if NPCData["OtherData"]["Home"] == None:
            NPCData["OtherData"]["Home"] = f"{Name}{NPCID} Room"
            # TODO
            # Data = {
            #     "PrivacyLevel": 0,
            #     "Allowed": [NPCID],
            #     "Forbidden": [],
            #     "Flags": {"Open": 0},
            #     "Name": f"{Name}{NPCID} Room",
            #     "FlavorText":"You are at the Southern Street, the main entrance connecting the city to the rest of the kingdom is here.",
            # }
            # AddLocation(f"{Name}{NPCID}Room", Data)
            # AddLocationConnection(f"{Name}{NPCID}Room", "ResidentialArea")

        try:
            NPCLocation = Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"]["Location"]
            Globals.SoLEnviorementData["Locations"][NPCLocation]["inHere"].append(NPCID)
        except:
            ""
    except Exception as e:
        Log(4, "ERROR IMPORTING NPC DATA", e, NPCData)

def Emit(Signal):
    if Signal in Globals.Signals:
        for Func in Globals.Signals[Signal]:
            Func()
def Connect(Signal, Func):
    if Signal in Globals.Signals:
        Globals.Signals[Signal].append(Func)
    else:
        Globals.Signals[Signal] = [Func]

def RandomChoice(Dict):
    try:
        NewDict = {}
        for Key in Dict:
            if Dict[Key] > 0:
                NewDict[Key] = Dict[Key]
        Choice = random.choices(list(NewDict.keys()), list(NewDict.values()))[0]
        return Choice
    except Exception as e:
        print("ERROR RandomChoice", e)

def Sleep(NPCID):
    try:
        Globals.SoLNPCData[NPCID]["State"]["PConscious"] = 0
        Globals.SoLNPCData[NPCID]["State"]["MConscious"] = 0
        Globals.SoLNPCData[NPCID]["State"]["Energy"] = Globals.SoLNPCData[NPCID]["GeneralAbilities"]["MaxEnergy"]
        Task = Globals.SoLOtherData["SleepTask"]
        Task["HourStart"] = Globals.SoLEnviorementData["DateData"]["Hour"]
        FinishHour = Globals.SoLEnviorementData["DateData"]["Hour"] + 480
        if FinishHour > 1440:
            FinishHour -= 1440
        Task["HourFinish"] = FinishHour

        for OtherID in Globals.SoLNPCData[NPCID]["Relations"]:
            for TValue in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Temporal"]:
                Data = Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Temporal"][TValue]
                Globals.SoLTValues[TValue]["Reference"].ProcessTAbility(NPCID, OtherID, Data)

        Globals.SoLNPCData[NPCID]["Actions"]["InteractionParty"] = {}

        if NPCID == Globals.SoLPCData["ID"]:
            PassTime(Globals.Layouts["SoLUI"], 480)
            Globals.Layouts["MainF"].gotoLayout("SleepUI")
        else:
            # ProcessGems(NPCID)
            ""

    except Exception as e:
        print(e)
def ApplyIdleTask(NPCID):
    DateData = Globals.SoLEnviorementData["DateData"]
    Globals.SoLNPCData[NPCID]["Actions"]["PreviousTask"] = Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"]
    Task = copy.deepcopy(Globals.SoLOtherData["IdlingTask"])
    Task["HourStart"] == DateData["Hour"]
    Task["HourFinish"] == DateData["Hour"] + 15
    Task["Task"][1]["BriefFluff"] = "Idle at " + Globals.SoLNPCData[NPCID]["Actions"]["PreviousTask"]["Location"]
    Task["Task"][1]["LongFluff"] = Globals.SoLNPCData[NPCID]["Name"] + " is idling at " + Globals.SoLNPCData[NPCID]["Actions"]["PreviousTask"]["Location"]
    Globals.SoLNPCData[NPCID]["Actions"]["CurrentTask"] = Task

def GetDescription(Area, NPCData, Options):
    Desc = []
    Part = []
    State = []

    BodyType = NPCData["BodyData"]
    Face = BodyType["Face"]
    Lips = BodyType["Lips"]
    Height = BodyType["Height"]
    HairColor = BodyType["HairColor"]
    SkinColor = BodyType["SkinColor"]
    Eyes = BodyType["Eyes"]
    Complexion = BodyType["Complexion"]
    BodySize = BodyType["Height"]
    ChestSize = BodyType["Chest"]
    HipsSize = BodyType["Hips"]
    AssSize = BodyType["Ass"]
    VTightness = BodyType["VTightness"]
    ATightness = BodyType["ATightness"]
    PenisSize = BodyType["PenisSize"]

    # with open('NPCdata.json', 'rb') as f:
    #     NPCdata = json.load(f)
    Arousal = NPCData["State"]["Arousal"]
    Mood = NPCData["State"]["Mood"]

    # TODO ADD NIPPLES
    ####
    if Area == "FaceType":
        Part.append("Face")

        if Face == 0: Desc.append('''Very Masculine''')
        elif Face == 1: Desc.append('''Masculine''')
        elif Face == 2: Desc.append('''Boyish''')
        elif Face == 3: Desc.append('''Androginous''')
        elif Face == 4: Desc.append('''Girlish''')
        elif Face == 5: Desc.append('''Femenine''')
        elif Face == 6: Desc.append('''Very Femenine''')

        if Mood < -70:
            State.append('''Upset''')
        elif Mood < -30:
            State.append('''Frowning''')
        if Mood > 30 and Mood < 70:
            State.append('''Happy''')
        if Mood >= 70:
            State.append('''Ecstatic''')
        else:
            State.append('''''')

    elif Area == "LipsSize":
        Part.append("Lips")

        if Lips == 0: Desc.append('''Thin''')
        elif Lips == 1: Desc.append('''Small''')
        elif Lips == 2: Desc.append('''Average''')
        elif Lips == 3: Desc.append('''Plump''')
        elif Lips == 4:Desc.append('''Big''')

        State.append('''''')
    elif Area == "Complexion":
        Part.append("Complexion")

        if Complexion == 0: Desc.append('''Scrawny''')
        elif Complexion == 1: Desc.append('''Thin''')
        elif Complexion == 2: Desc.append('''Slim''')
        elif Complexion == 3: Desc.append('''Average''')
        elif Complexion == 4: Desc.append('''Plump''')
        elif Complexion == 5: Desc.append('''Fat''')
        elif Complexion == 6: Desc.append('''Very Fat''')
        elif Complexion == 7: Desc.append('''Toned''')
        elif Complexion == 8: Desc.append('''Strong''')
        elif Complexion == 9: Desc.append('''Buff''')

        State.append('''''')
    elif Area == "Stomach":
        Part.append("Belly")
        Part.append("Midrift")
        Part.append("Stomach")

        if Complexion == 0: Desc.append('''Very Thin''')
        elif Complexion == 1: Desc.append('''Thin''')
        elif Complexion == 2: Desc.append('''Slim''')
        elif Complexion == 3: Desc.append('''Nice''')
        elif Complexion == 4: Desc.append('''Plump''')
        elif Complexion == 5: Desc.append('''Fat''')
        elif Complexion == 6: Desc.append('''Very Fat''')
        elif Complexion == 7: Desc.append('''Defined''')
        elif Complexion == 8: Desc.append('''Athletic''')
        elif Complexion == 9: Desc.append('''Strong''')

        State.append('''''')
    elif Area == "Thighs":
        Part.append("Thighs")

        if Complexion == 0: Desc.append('''Very Thin''')
        elif Complexion == 1: Desc.append('''Thin''')
        elif Complexion == 2: Desc.append('''Slim''')
        elif Complexion == 3: Desc.append('''Nice''')
        elif Complexion == 4: Desc.append('''Plump''')
        elif Complexion == 5: Desc.append('''Fat''')
        elif Complexion == 6: Desc.append('''Very Fat''')
        elif Complexion == 7: Desc.append('''Defined''')
        elif Complexion == 8: Desc.append('''Athletic''')
        elif Complexion == 9: Desc.append('''Strong''')

        State.append('''''')

    elif Area == "BodySize":
        Part.append("Size")
        Part.append("Height")

        if BodySize == 0: Desc.append('''Very Tiny''')
        elif BodySize == 1: Desc.append('''Tiny''')
        elif BodySize == 2: Desc.append('''Small''')
        elif BodySize == 3: Desc.append('''Average''')
        elif BodySize == 4: Desc.append('''Tall''')
        elif BodySize == 5: Desc.append('''Very Tall''')
        elif BodySize == 6: Desc.append('''Huge''')

        State.append('''''')
    elif Area == "HipsSize":
        Part.append("Hips")

        if HipsSize == 0: Desc.append('''Manly''')
        elif HipsSize == 1: Desc.append('''Straight''')
        elif HipsSize == 2: Desc.append('''Slim''')
        elif HipsSize == 3: Desc.append('''Average''')
        elif HipsSize == 4: Desc.append('''Wide''')
        elif HipsSize == 5: Desc.append('''Childbearing''')

        State.append('''''')
    elif Area == "ChestSize":
        if ChestSize <= 1:
            Part.append("Chest")
        elif ChestSize >= 2:
            Part.append("Breasts")
            Part.append("Tits")

        if ChestSize == 0: Desc.append('''Muscular''')
        elif ChestSize == 1: Desc.append('''Flat''')
        elif ChestSize == 2: Desc.append('''Bulging''')
        elif ChestSize == 3: Desc.append('''Small''')
        elif ChestSize == 4: Desc.append('''Average''')
        elif ChestSize == 5: Desc.append('''Big''')
        elif ChestSize == 6: Desc.append('''Very Big''')
        elif ChestSize == 7: Desc.append('''Huge''')

        State.append('''''')
    elif Area == "AssSize":
        Part.append("Ass")
        Part.append("Butt")
        Part.append("Behind")

        if AssSize == 0: Desc.append('''Masculine''')
        elif AssSize == 1: Desc.append('''Thin''')
        elif AssSize == 2: Desc.append('''Slim''')
        elif AssSize == 3: Desc.append('''Average''')
        elif AssSize == 4: Desc.append('''Plump''')
        elif AssSize == 5: Desc.append('''Big''')
        elif AssSize == 6: Desc.append('''Huge''')

        State.append('''''')
    elif Area == "VTightness":
        Part.append("Pussy")

        if VTightness == 0: Desc.append('''Non Existant''')
        elif VTightness == 1: Desc.append('''Very Tight''')
        elif VTightness == 2: Desc.append('''Tight''')
        elif VTightness == 3: Desc.append('''Nice''')
        elif VTightness == 4: Desc.append('''Loose''')
        elif VTightness == 5: Desc.append('''Very Loose''')

        if Arousal <= 40:
            State.append('''Dry''')
        else:
            State.append('''Wet''')
    elif Area == "ATightness":
        Part.append("Anus")
        Part.append("Asshole")

        if ATightness == 0: Desc.append('''Non Existant''')
        elif ATightness == 1: Desc.append('''Very Tight''')
        elif ATightness == 2: Desc.append('''Tight''')
        elif ATightness == 3: Desc.append('''Average''')
        elif ATightness == 4: Desc.append('''Loose''')
        elif ATightness == 5: Desc.append('''Very Loose''')

        State.append('''''')
    elif Area == "PenisSize":
        Part.append("Penis")
        Part.append("Cock")
        Part.append("Dick")

        if PenisSize == 0: Desc.append('''Non Existant''')
        elif PenisSize == 1: Desc.append('''Tiny''')
        elif PenisSize == 2: Desc.append('''Small''')
        elif PenisSize == 3: Desc.append('''Average''')
        elif PenisSize == 4: Desc.append('''Big''')
        elif PenisSize == 5: Desc.append('''Huge''')

        if Arousal <= 40:
            State.append('''Soft''')
            State.append('''Limp''')
        else:
            State.append('''Hard''')
            State.append('''Stiff''')
            State.append('''Firm''')
    elif Area == "Age":
        Part.append("")
        # if Age == 0:
        if True:
            Desc.append("Very Young")
        State.append('''''')
    elif Area == "Height":
        if Height == 0: Desc.append("Pixie Size")
        if Height == 1: Desc.append("Very Tiny")
        if Height == 2: Desc.append("Tiny")
        if Height == 3: Desc.append("Small")
        if Height == 4: Desc.append("Average")
        if Height == 5: Desc.append("Tall")
        if Height == 6: Desc.append("Very Tall")
        if Height == 7: Desc.append("Towering")

        State.append('''''')
        Part.append("")


    elif Area == "Hair":
        Desc.append(HairColor)
        State.append('''''')
        Part.append("Hair")
    elif Area == "Skin":
        Desc.append(SkinColor)
        State.append('''''')
        Part.append("Skin")
    elif Area == "Eyes":
        Desc.append(Eyes)
        State.append('''''')
        Part.append("Eyes")


    else:
        Log(1, "ERROR PART DESCRIPTION", "MISSING IMPLEMENTATION", Area)
        Part.append(Area)
        Desc.append(Area)
        State.append(Area)
    ####

    # BUILDS UP THE FINAL TEXT
    Final = ""
    def Processing(Option):
        if Option == "D":
            return random.choice(Desc)
        elif Option == "S":
            return random.choice(State)
        elif Option == "P":
            return random.choice(Part)
    for i in Options:
        Text = Processing(i)
        if Text != "":
            Final += f'''{Text} '''
    Length = len(Final)
    # REMOVES LAST SPACE
    Final = Final[0:Length-1]
    return Final.lower()

def GetPValueStaticWidget(PermanentID, Value):
    ValueLabel = QLabel()
    ValueLabel.setText(f'''{PermanentID}: {Value}''')
    ValueLabel.setProperty("Color","None")
    ValueLabel.setGeometry(0, 40, 150, 35)
    ValueLabel.setMaximumWidth(150)
    ValueLabel.setMinimumWidth(150)
    ValueLabel.setMaximumHeight(35)
    ValueLabel.setMinimumHeight(35)

    return ValueLabel
def GetTValueStaticWidget(TemporalID, Value):
    ValueLabel = QLabel()
    ValueLabel.setText(f'''{TemporalID}: {Value}''')
    ValueLabel.setProperty("Color","None")
    ValueLabel.setGeometry(0, 40, 150, 35)
    ValueLabel.setMaximumWidth(150)
    ValueLabel.setMinimumWidth(150)
    ValueLabel.setMaximumHeight(35)
    ValueLabel.setMinimumHeight(35)

    return ValueLabel
def GetGValueStaticWidget(GemsID, Value):
    ValueLabel = QLabel()
    ValueLabel.setText(f'''{GemsID}: {Value}''')
    ValueLabel.setProperty("Color","None")
    ValueLabel.setGeometry(0, 40, 150, 35)
    ValueLabel.setMaximumWidth(150)
    ValueLabel.setMinimumWidth(150)
    ValueLabel.setMaximumHeight(35)
    ValueLabel.setMinimumHeight(35)

    return ValueLabel

def Initialize(self, Reference):
    Globals.References["SoLFunctions"] = Reference
