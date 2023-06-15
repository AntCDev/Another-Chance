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
import os
import pathlib

def Initialize(self, Reference):
    AbilitiesList = ["Obedience", "Lust", "Intimacy", "Submission", "Superiority", "CSense", "VSense", "ASense", "PSense", "MSense", "Service", "Sadism", "Masochism", "Exhibitionism"]
    for AbilityID in AbilitiesList:
        Globals.SoLAbilities[AbilityID] = {"ID":AbilityID, "Reference":Reference, "OtherData":{}}

    # Globals.SoLAbilities["Exhibitionism0"] = {"ID":"Exhibitionism0", "Reference":Reference, "OtherData":{}}

    # Gems = ["Favor", "Hate", "Submission", "Superiority", "PPlea", "Service", "Pain", "Shame", "Fear", "Desire", "APlea", "VPlea", "CPlea", "BPlea", "MPlea"]

    # TValuesList = ["Favor", "Discomfort", "Desire", "Obedience", "Submission", "VPlea", "CPlea", "APlea", "BPlea", "MPlea", "PPlea", "Service", "Pain", "Superiority", "Lubrication", "Shame", "Loyalty", "Fear", "Hate"]
    TValuesList = ["Favor", "Loyalty", "Desire", "Obedience", "Superiority", "Submission", "Service", "Shame", "MPlea", "CPlea", "APlea", "VPlea", "PPlea", "Pain", "Fear", "Discomfort", "Hate"]
    for ID in TValuesList:
        Globals.SoLTValues[ID] = {"ID":ID, "Reference":Reference, "Type":"Positive", "BaseData":{"ID":ID, "Amount":0, "OtherData":{}}, "OtherData":{}}

    GPList = ["Favor", "Loyalty", "Desire", "Obedience", "Superiority", "Submission", "Service", "Shame", "MPLea", "CPlea", "APlea", "VPlea", "PPlea", "Pain", "Fear"]
    GNList = ["Discomfort", "Hate"]
    for ID in GPList:
        Globals.SoLGValues[ID] = {"ID":ID, "Reference":Reference, "Type":"Positive", "BaseData":{"ID":ID, "Amount":0, "OtherData":{}}, "OtherData":{}}
    for ID in GNList:
        Globals.SoLGValues[ID] = {"ID":ID, "Reference":Reference, "Type":"Negative", "BaseData":{"ID":ID, "Amount":0, "OtherData":{}}, "OtherData":{}}


# def ProcessingAbility(self, TargetDict, ActorDict, CommandID, Actor, Target, AbilityID, Who):
#     return TargetDict, ActorDict

def CommandProcessAbility(self, OriginalData, FinalData, AbilityID):
    try:
        Target = FinalData["Target"]
        TargetData = Globals.SoLNPCData[Target]
        Actor = FinalData["Actor"]
        ActorData = Globals.SoLNPCData[Actor]
        # "Obedience", "Lust", "Intimacy", "Submission", "CSense", "VSense", "ASense", "BSense", "PSense", "MSense", "Service", "Sadism", "Masochism", "Exhibitionism"
        if AbilityID == "Obedience":
            # IF THE TARGET HAS OBEDIENCE, THEN THE RESISTANCE IS LOWERED BY 5 PER LEVEL
            if "Obedience" in TargetData["Relations"][Actor]["Abilities"]:
                Data = TargetData["Relations"][Actor]["Abilities"]["Obedience"]
                Level = Data["Level"]
                if Level > 0:
                    if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (5 * Level)
        elif AbilityID == "Lust":
            # IF THE TARGET HAS LUST. IF THE TARGETDICT HAS A SEXUAL CONNOTATION THEN THE RESISTANCE IS LOWERED BY 5 * LEVEL. IF THE TargetDict HAS AROUSAL THEN IT IS INCRESED BY 0.1 PER LEVEL. IF THE TargetDict HAS EXCITEMENT THEN IT IS INCRESED BY 0.1 PER LEVEL
            if "Lust" in TargetData["Relations"][Actor]["Abilities"]:
                Data = TargetData["Relations"][Actor]["Abilities"]["Lust"]
                Level = Data["Level"]
                if Level > 0 and "Sexual" in FinalData["TargetDict"]["Connotations"]:
                    if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (5 * Level)
                    if "Arousal" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Arousal"] += FinalData["TargetDict"]["State"]["Arousal"] * (0.1 * Level)
                    if "Excitement" in FinalData["TargetDict"]["State"]: FinalData["TargetDict"]["State"]["Excitement"] += FinalData["TargetDict"]["State"]["Excitement"] * (0.1 * Level)
        elif AbilityID == "Intimacy":
            # IF THE TARGET HAS INTIMACY, THEN THE RESISTANCE IS LOWERED BY 5 PER LEVEL, IF THE TARGETDICT HAS THE INTIMATE CONNOTATION THEN THE RESISTANCE IS LOWERED BY 5 MORE PER LEVEL
            if "Intimacy" in TargetData["Relations"][Actor]["Abilities"]:
                Data = TargetData["Relations"][Actor]["Abilities"]["Intimacy"]
                Level = Data["Level"]
                if Level > 0:
                    if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (5 * Level)
                    if "Resistance" in FinalData["TargetDict"] and "Intimate" in FinalData["TargetDict"]["Connotations"]: FinalData["TargetDict"]["Resistance"] -= (2 * Level * FinalData["TargetDict"]["Connotations"]["Intimate"][0])
        elif AbilityID == "Submission":
            # IF THE TARGET HAS SUBMISSION THEN THE RESISTANCE IS LOWERED BY 5 PER LEVEL, 5 MORE IF THE TARGETDICT HAS THE SUBMISSIVE CONNOTATION, 5 LESS IF THE TARGETDICT HAS THE DOMINANT CONNOTATION
            if "Submission" in TargetData["Relations"][Actor]["Abilities"]:
                Data = TargetData["Relations"][Actor]["Abilities"]["Submission"]
                Level = Data["Level"]
                if Level > 0:
                    if "Submissive" in FinalData["TargetDict"]["Connotations"] and "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (5 * Level)
                    if "Dominant" not in FinalData["TargetDict"]["Connotations"] and "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (5 * Level)
        elif AbilityID == "CSense":
            # IF THE TARGET HAS CPLEA THEN THE CPLEA IS INCREASED AND THE RESISTANCE IS REDUCED
            if "CSense" in TargetData["Relations"][Actor]["Abilities"]:
                Data = TargetData["Relations"][Actor]["Abilities"]["CSense"]
                Level = Data["Level"]
                if Level > 0 and "CPlea" in FinalData["TargetDict"]["Temporal"]:
                    FinalData["TargetDict"]["Temporal"]["CPlea"] += FinalData["TargetDict"]["Temporal"]["CPlea"] * (0.5 * Level)
                    if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (3 * Level)
            # IF THE TARGET HAS CPLEA THEN THE CPLEA IS INCREASED AND THE RESISTANCE IS REDUCED
            if "CSense" in ActorData["Relations"][Target]["Abilities"]:
                Data = ActorData["Relations"][Target]["Abilities"]["CSense"]
                Level = Data["Level"]
                if Level > 0 and "CPlea" in FinalData["ActorDict"]["Temporal"]:
                    FinalData["ActorDict"]["Temporal"]["CPlea"] += FinalData["ActorDict"]["Temporal"]["CPlea"] * (0.5 * Level)
                    if "Resistance" in FinalData["ActorDict"]: FinalData["ActorDict"]["Resistance"] -= (3 * Level)
        elif AbilityID == "VSense":
            # IF THE TARGET HAS VPlea THEN THE VPlea IS INCREASED AND THE RESISTANCE IS REDUCED
            if "VSense" in TargetData["Relations"][Actor]["Abilities"]:
                Data = TargetData["Relations"][Actor]["Abilities"]["VSense"]
                Level = Data["Level"]
                if Level > 0 and "VPlea" in FinalData["TargetDict"]["Temporal"]:
                    FinalData["TargetDict"]["Temporal"]["VPlea"] += FinalData["TargetDict"]["Temporal"]["VPlea"] * (0.5 * Level)
                    if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (3 * Level)
            # IF THE TARGET HAS CPLEA THEN THE CPLEA IS INCREASED AND THE RESISTANCE IS REDUCED
            if "VSense" in ActorData["Relations"][Target]["Abilities"]:
                Data = ActorData["Relations"][Target]["Abilities"]["VSense"]
                Level = Data["Level"]
                if Level > 0 and "VPlea" in FinalData["ActorDict"]["Temporal"]:
                    FinalData["ActorDict"]["Temporal"]["VPlea"] += FinalData["ActorDict"]["Temporal"]["VPlea"] * (0.5 * Level)
                    if "Resistance" in FinalData["ActorDict"]: FinalData["ActorDict"]["Resistance"] -= (3 * Level)
        elif AbilityID == "ASense":
            # IF THE TARGET HAS APlea THEN THE APlea IS INCREASED AND THE RESISTANCE IS REDUCED
            if "ASense" in TargetData["Relations"][Actor]["Abilities"]:
                Data = TargetData["Relations"][Actor]["Abilities"]["ASense"]
                Level = Data["Level"]
                if Level > 0 and "APlea" in FinalData["TargetDict"]["Temporal"]:
                    FinalData["TargetDict"]["Temporal"]["APlea"] += FinalData["TargetDict"]["Temporal"]["APlea"] * (0.5 * Level)
                    if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (3 * Level)
            # IF THE TARGET HAS CPLEA THEN THE CPLEA IS INCREASED AND THE RESISTANCE IS REDUCED
            if "ASense" in ActorData["Relations"][Target]["Abilities"]:
                Data = ActorData["Relations"][Target]["Abilities"]["ASense"]
                Level = Data["Level"]
                if Level > 0 and "APlea" in FinalData["ActorDict"]["Temporal"]:
                    FinalData["ActorDict"]["Temporal"]["APlea"] += FinalData["ActorDict"]["Temporal"]["APlea"] * (0.5 * Level)
                    if "Resistance" in FinalData["ActorDict"]: FinalData["ActorDict"]["Resistance"] -= (3 * Level)
        elif AbilityID == "PSense":
            # IF THE TARGET HAS CPLEA THEN THE PPlea IS INCREASED AND THE RESISTANCE IS REDUCED
            if "PSense" in TargetData["Relations"][Actor]["Abilities"]:
                Data = TargetData["Relations"][Actor]["Abilities"]["PSense"]
                Level = Data["Level"]
                if Level > 0 and "PPlea" in FinalData["TargetDict"]["Temporal"]:
                    FinalData["TargetDict"]["Temporal"]["PPlea"] += FinalData["TargetDict"]["Temporal"]["PPlea"] * (0.5 * Level)
                    if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (3 * Level)
            # IF THE TARGET HAS CPLEA THEN THE CPLEA IS INCREASED AND THE RESISTANCE IS REDUCED
            if "PSense" in ActorData["Relations"][Target]["Abilities"]:
                Data = ActorData["Relations"][Target]["Abilities"]["PSense"]
                Level = Data["Level"]
                if Level > 0 and "PPlea" in FinalData["ActorDict"]["Temporal"]:
                    FinalData["ActorDict"]["Temporal"]["PPlea"] += FinalData["ActorDict"]["Temporal"]["PPlea"] * (0.5 * Level)
                    if "Resistance" in FinalData["ActorDict"]: FinalData["ActorDict"]["Resistance"] -= (3 * Level)
        elif AbilityID == "MSense":
            # IF THE TARGET HAS MPlea THEN THE MPlea IS INCREASED AND THE RESISTANCE IS REDUCED
            if "MSense" in TargetData["Relations"][Actor]["Abilities"]:
                Data = TargetData["Relations"][Actor]["Abilities"]["MSense"]
                Level = Data["Level"]
                if Level > 0 and "MPlea" in FinalData["TargetDict"]["Temporal"]:
                    FinalData["TargetDict"]["Temporal"]["MPlea"] += FinalData["TargetDict"]["Temporal"]["MPlea"] * (0.5 * Level)
                    if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (3 * Level)
            # IF THE TARGET HAS CPLEA THEN THE CPLEA IS INCREASED AND THE RESISTANCE IS REDUCED
            if "MSense" in ActorData["Relations"][Target]["Abilities"]:
                Data = ActorData["Relations"][Target]["Abilities"]["MSense"]
                Level = Data["Level"]
                if Level > 0 and "MPlea" in FinalData["ActorDict"]["Temporal"]:
                    FinalData["ActorDict"]["Temporal"]["MPlea"] += FinalData["ActorDict"]["Temporal"]["MPlea"] * (0.5 * Level)
                    if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (3 * Level)
        elif AbilityID == "Service":
            # IF THE TARGET HAS Service, THEN THE RESISTANCE IS LOWERED BY 5 PER LEVEL, IF THE TARGETDICT HAS THE Service CONNOTATION THEN THE RESISTANCE IS LOWERED BY 5 MORE PER LEVEL
            if "Service" in TargetData["Relations"][Actor]["Abilities"]:
                Data = TargetData["Relations"][Actor]["Abilities"]["Service"]
                Level = Data["Level"]
                if Level > 0:
                    if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (5 * Level)
                    if "Resistance" in FinalData["TargetDict"] and "Service" in FinalData["TargetDict"]["Connotations"]: FinalData["TargetDict"]["Resistance"] -= (2 * Level * FinalData["TargetDict"]["Connotations"]["Intimate"][0])
        elif AbilityID == "Sadism":
            if "Sadism" in ActorData["Relations"][Target]["Abilities"]:
                Data = ActorData["Relations"][Target]["Abilities"]["Service"]
                Level = Data["Level"]
                if Level > 0:
                    if "Pain" in FinalData["TargetDict"]["Temporal"]:
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (0.5 * Level)
                        FinalData["TargetDict"]["Temporal"]["Pain"] += FinalData["TargetDict"]["Temporal"]["Pain"] * (0.5 * Level)
                    if "Sadist" in FinalData["ActorDict"]["Connotations"]:
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (1 * Level * FinalData["ActorDict"]["Connotations"]["Sadist"][0])
                    if "Abuse" in FinalData["TargetDict"]["Connotations"]:
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (1 * Level * FinalData["TargetDict"]["Connotations"]["Abuse"][0])
                    if "Humilliation" in FinalData["TargetDict"]["Connotations"]:
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (1 * Level * FinalData["TargetDict"]["Connotations"]["Humilliation"][0])
            if "Sadism" in TargetData["Relations"][Actor]["Abilities"]:
                Data = TargetData["Relations"][Actor]["Abilities"]["Service"]
                Level = Data["Level"]
                if Level > 0:
                    if "Pain" in FinalData["ActorDict"]["Temporal"]:
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (0.5 * Level)
                        FinalData["ActorDict"]["Temporal"]["Pain"] += FinalData["ActorDict"]["Temporal"]["Pain"] * (0.5 * Level)
                    if "Sadist" in FinalData["TargetDict"]["Connotations"]:
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (1 * Level * FinalData["TargetDict"]["Connotations"]["Sadist"][0])
                    if "Abuse" in FinalData["ActorDict"]["Connotations"]:
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (1 * Level * FinalData["ActorDict"]["Connotations"]["Abuse"][0])
                    if "Humilliation" in FinalData["ActorDict"]["Connotations"]:
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (1 * Level * FinalData["ActorDict"]["Connotations"]["Humilliation"][0])
        elif AbilityID == "Masochism":
            if "Masochism" in TargetData["Relations"][Actor]["Abilities"]:
                Data = TargetData["Relations"][Actor]["Abilities"]["Service"]
                Level = Data["Level"]
                if Level > 0:
                    if "Pain" in FinalData["TargetDict"]["Temporal"]:
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (1.5 * Level)
                        FinalData["TargetDict"]["Temporal"]["Pain"] += FinalData["TargetDict"]["Temporal"]["Pain"] * (0.5 * Level)
                    if "Masochist" in FinalData["TargetDict"]["Connotations"]:
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (1 * Level * FinalData["TargetDict"]["Connotations"]["Masochist"][0])
                    if "Abuse" in FinalData["TargetDict"]["Connotations"]:
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (1 * Level * FinalData["TargetDict"]["Connotations"]["Abuse"][0])
                    if "Humilliation" in FinalData["TargetDict"]["Connotations"]:
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (1 * Level * FinalData["TargetDict"]["Connotations"]["Humilliation"][0])
            if "Masochism" in ActorData["Relations"][Target]["Abilities"]:
                Data = ActorData["Relations"][Target]["Abilities"]["Service"]
                Level = Data["Level"]
                if Level > 0:
                    if "Pain" in FinalData["ActorDict"]["Temporal"]:
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (1.5 * Level)
                        FinalData["ActorDict"]["Temporal"]["Pain"] += FinalData["ActorDict"]["Temporal"]["Pain"] * (0.5 * Level)
                    if "Masochist" in FinalData["ActorDict"]["Connotations"]:
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (1 * Level * FinalData["ActorDict"]["Connotations"]["Masochist"][0])
                    if "Abuse" in FinalData["ActorDict"]["Connotations"]:
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (1 * Level * FinalData["ActorDict"]["Connotations"]["Abuse"][0])
                    if "Humilliation" in FinalData["ActorDict"]["Connotations"]:
                        if "Resistance" in FinalData["TargetDict"]: FinalData["TargetDict"]["Resistance"] -= (1 * Level * FinalData["ActorDict"]["Connotations"]["Humilliation"][0])
        elif AbilityID == "Exhibitionism":
            if "Exhibitionism" in TargetData["Relations"][Actor]["Abilities"]:
                Data = TargetData["Relations"][Actor]["Abilities"]["Exhibitionism"]
                Level = Data["Level"]
                if Level > 0:
                    if "Resistance" in FinalData["TargetDict"] and "Exhibitionist" in FinalData["TargetDict"]["Connotations"]: FinalData["TargetDict"]["Resistance"] -= (2 * Level * FinalData["TargetDict"]["Connotations"]["Exhibitionist"][0])

    except Exception as e:
        print("ERROR CommandProcessAbility", e, AbilityID, OriginalData, FinalData)
        ""

    return OriginalData, FinalData

def ProcessTAbility(NPCID, OtherID, TValueData):
    TID = TValueData["ID"]
    Amount = TValueData["Amount"]
    Gems = 0
    Gems = 10 ** (len(str(Amount))-2)
    if Gems < 10:
        Gems = 0

    if Gems > 0 and Amount > 0:
        GemsID = TID

        try:
            if GemsID not in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]:
                Data = Globals.SoLGValues[GemsID]["BaseData"]
            else:
                Data = Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"][GemsID]
            Data["Amount"] += Gems
            Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"][GemsID] = Data
        except Exception as e:
            ""
    Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Temporal"][TID]["Amount"] = 0


def AbilityChange(AbilityID, NPCID, OtherID, Change):
    if AbilityID in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Abilities"]:
        Data = Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Abilities"][AbilityID]
    else:
        Data = {"ID":AbilityID, "Level":0, "OtherData":{}}
    Data["Level"] += Change
    if Data["Level"] < 0:
        Data["Level"] = 0
    elif Data["Level"] > 10:
        Data["Level"] = 10
    Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Abilities"][AbilityID] = Data
    Globals.LayoutsData["Active"].Refresh()

def GetAbilityConditions(AbilityID, Level, Type, NPCID, OtherID):
    Text = ""
    Available = 0

    try:
        if AbilityID == "Obedience":
            if Level == 0:
                Type = "Downgrade"
                if Type == "Downgrade":
                    Text = '''25 Superiority Gems '''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 25: Available = 1
            elif Level == 1:
                if Type == "Upgrade":
                    Text = '''25 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 25: Available = 1
                elif Type == "Downgrade":
                    Text = '''50 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 50: Available = 1
            elif Level == 2:
                if Type == "Upgrade":
                    Text = '''50 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 50: Available = 1
                elif Type == "Downgrade":
                    Text = '''100 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 100: Available = 1
            elif Level == 3:
                if Type == "Upgrade":
                    Text = '''100 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 100: Available = 1
                elif Type == "Downgrade":
                    Text = '''200 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 200: Available = 1
            elif Level == 4:
                if Type == "Upgrade":
                    Text = '''200 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 200: Available = 1
                elif Type == "Downgrade":
                    Text = '''400 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 400: Available = 1
            elif Level == 5:
                if Type == "Upgrade":
                    Text = '''400 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 400: Available = 1
                elif Type == "Downgrade":
                    Text = '''800 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 800: Available = 1
            elif Level == 6:
                if Type == "Upgrade":
                    Text = '''800 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 800: Available = 1
                elif Type == "Downgrade":
                    Text = '''1600 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 1600: Available = 1
            elif Level == 7:
                if Type == "Upgrade":
                    Text = '''1600 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 1600: Available = 1
                elif Type == "Downgrade":
                    Text = '''3200 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 3200: Available = 1
            elif Level == 8:
                if Type == "Upgrade":
                    Text = '''3200 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 3200: Available = 1
                elif Type == "Downgrade":
                    Text = '''6400 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 6400: Available = 1
            elif Level == 9:
                if Type == "Upgrade":
                    Text = '''6400 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 6400: Available = 1
                elif Type == "Downgrade":
                    Text = '''12800 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 12800: Available = 1
            elif Level == 10:
                if Type == "Upgrade":
                    Text = '''12800 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 12800: Available = 1
        elif AbilityID == "Lust":
            if Level == 0:
                Type = "Downgrade"
                if Type == "Downgrade":
                    Text = '''25 Loyalty Gems '''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 25: Available = 1
            elif Level == 1:
                if Type == "Upgrade":
                    Text = '''25 Desire Gems'''
                    if "Desire" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Desire"]["Amount"] > 25: Available = 1
                elif Type == "Downgrade":
                    Text = '''50 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 50: Available = 1
            elif Level == 2:
                if Type == "Upgrade":
                    Text = '''50 Desire Gems'''
                    if "Desire" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Desire"]["Amount"] > 50: Available = 1
                elif Type == "Downgrade":
                    Text = '''100 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 100: Available = 1
            elif Level == 3:
                if Type == "Upgrade":
                    Text = '''100 Desire Gems'''
                    if "Desire" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Desire"]["Amount"] > 100: Available = 1
                elif Type == "Downgrade":
                    Text = '''200 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 200: Available = 1
            elif Level == 4:
                if Type == "Upgrade":
                    Text = '''200 Desire Gems'''
                    if "Desire" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Desire"]["Amount"] > 200: Available = 1
                elif Type == "Downgrade":
                    Text = '''400 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 400: Available = 1
            elif Level == 5:
                if Type == "Upgrade":
                    Text = '''400 Desire Gems'''
                    if "Desire" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Desire"]["Amount"] > 400: Available = 1
                elif Type == "Downgrade":
                    Text = '''800 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 800: Available = 1
            elif Level == 6:
                if Type == "Upgrade":
                    Text = '''800 Desire Gems'''
                    if "Desire" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Desire"]["Amount"] > 800: Available = 1
                elif Type == "Downgrade":
                    Text = '''1600 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 1600: Available = 1
            elif Level == 7:
                if Type == "Upgrade":
                    Text = '''1600 Desire Gems'''
                    if "Desire" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Desire"]["Amount"] > 1600: Available = 1
                elif Type == "Downgrade":
                    Text = '''3200 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 3200: Available = 1
            elif Level == 8:
                if Type == "Upgrade":
                    Text = '''3200 Desire Gems'''
                    if "Desire" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Desire"]["Amount"] > 3200: Available = 1
                elif Type == "Downgrade":
                    Text = '''6400 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 6400: Available = 1
            elif Level == 9:
                if Type == "Upgrade":
                    Text = '''6400 Desire Gems'''
                    if "Desire" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Desire"]["Amount"] > 6400: Available = 1
                elif Type == "Downgrade":
                    Text = '''12800 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 12800: Available = 1
            elif Level == 10:
                if Type == "Upgrade":
                    Text = '''12800 Desire Gems'''
                    if "Desire" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Desire"]["Amount"] > 12800: Available = 1
        elif AbilityID == "Intimacy":
            if Level == 0:
                Type = "Downgrade"
                if Type == "Downgrade":
                    Text = '''25 Hate Gems '''
                    if "Hate" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Hate"]["Amount"] > 25: Available = 1
            elif Level == 1:
                if Type == "Upgrade":
                    Text = '''25 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 25: Available = 1
                elif Type == "Downgrade":
                    Text = '''50 Hate Gems'''
                    if "Hate" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Hate"]["Amount"] > 50: Available = 1
            elif Level == 2:
                if Type == "Upgrade":
                    Text = '''50 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 50: Available = 1
                elif Type == "Downgrade":
                    Text = '''100 Hate Gems'''
                    if "Hate" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Hate"]["Amount"] > 100: Available = 1
            elif Level == 3:
                if Type == "Upgrade":
                    Text = '''100 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 100: Available = 1
                elif Type == "Downgrade":
                    Text = '''200 Hate Gems'''
                    if "Hate" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Hate"]["Amount"] > 200: Available = 1
            elif Level == 4:
                if Type == "Upgrade":
                    Text = '''200 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 200: Available = 1
                elif Type == "Downgrade":
                    Text = '''400 Hate Gems'''
                    if "Hate" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Hate"]["Amount"] > 400: Available = 1
            elif Level == 5:
                if Type == "Upgrade":
                    Text = '''400 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 400: Available = 1
                elif Type == "Downgrade":
                    Text = '''800 Hate Gems'''
                    if "Hate" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Hate"]["Amount"] > 800: Available = 1
            elif Level == 6:
                if Type == "Upgrade":
                    Text = '''800 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 800: Available = 1
                elif Type == "Downgrade":
                    Text = '''1600 Hate Gems'''
                    if "Hate" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Hate"]["Amount"] > 1600: Available = 1
            elif Level == 7:
                if Type == "Upgrade":
                    Text = '''1600 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 1600: Available = 1
                elif Type == "Downgrade":
                    Text = '''3200 Hate Gems'''
                    if "Hate" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Hate"]["Amount"] > 3200: Available = 1
            elif Level == 8:
                if Type == "Upgrade":
                    Text = '''3200 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 3200: Available = 1
                elif Type == "Downgrade":
                    Text = '''6400 Hate Gems'''
                    if "Hate" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Hate"]["Amount"] > 6400: Available = 1
            elif Level == 9:
                if Type == "Upgrade":
                    Text = '''6400 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 6400: Available = 1
                elif Type == "Downgrade":
                    Text = '''12800 Hate Gems'''
                    if "Hate" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Hate"]["Amount"] > 12800: Available = 1
            elif Level == 10:
                if Type == "Upgrade":
                    Text = '''12800 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 12800: Available = 1
        elif AbilityID == "Submission":
            if Level == 0:
                Type = "Downgrade"
                if Type == "Downgrade":
                    Text = '''25 Superiority Gems '''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 25: Available = 1
            elif Level == 1:
                if Type == "Upgrade":
                    Text = '''25 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 25: Available = 1
                elif Type == "Downgrade":
                    Text = '''50 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 50: Available = 1
            elif Level == 2:
                if Type == "Upgrade":
                    Text = '''50 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 50: Available = 1
                elif Type == "Downgrade":
                    Text = '''100 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 100: Available = 1
            elif Level == 3:
                if Type == "Upgrade":
                    Text = '''100 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 100: Available = 1
                elif Type == "Downgrade":
                    Text = '''200 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 200: Available = 1
            elif Level == 4:
                if Type == "Upgrade":
                    Text = '''200 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 200: Available = 1
                elif Type == "Downgrade":
                    Text = '''400 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 400: Available = 1
            elif Level == 5:
                if Type == "Upgrade":
                    Text = '''400 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 400: Available = 1
                elif Type == "Downgrade":
                    Text = '''800 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 800: Available = 1
            elif Level == 6:
                if Type == "Upgrade":
                    Text = '''800 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 800: Available = 1
                elif Type == "Downgrade":
                    Text = '''1600 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 1600: Available = 1
            elif Level == 7:
                if Type == "Upgrade":
                    Text = '''1600 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 1600: Available = 1
                elif Type == "Downgrade":
                    Text = '''3200 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 3200: Available = 1
            elif Level == 8:
                if Type == "Upgrade":
                    Text = '''3200 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 3200: Available = 1
                elif Type == "Downgrade":
                    Text = '''6400 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 6400: Available = 1
            elif Level == 9:
                if Type == "Upgrade":
                    Text = '''6400 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 6400: Available = 1
                elif Type == "Downgrade":
                    Text = '''12800 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 12800: Available = 1
            elif Level == 10:
                if Type == "Upgrade":
                    Text = '''12800 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 12800: Available = 1
        elif AbilityID == "Superiority":
            if Level == 0:
                Type = "Downgrade"
                if Type == "Downgrade":
                    Text = '''25 Submission Gems '''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 25: Available = 1
            elif Level == 1:
                if Type == "Upgrade":
                    Text = '''25 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 25: Available = 1
                elif Type == "Downgrade":
                    Text = '''50 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 50: Available = 1
            elif Level == 2:
                if Type == "Upgrade":
                    Text = '''50 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 50: Available = 1
                elif Type == "Downgrade":
                    Text = '''100 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 100: Available = 1
            elif Level == 3:
                if Type == "Upgrade":
                    Text = '''100 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 100: Available = 1
                elif Type == "Downgrade":
                    Text = '''200 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 200: Available = 1
            elif Level == 4:
                if Type == "Upgrade":
                    Text = '''200 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 200: Available = 1
                elif Type == "Downgrade":
                    Text = '''400 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 400: Available = 1
            elif Level == 5:
                if Type == "Upgrade":
                    Text = '''400 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 400: Available = 1
                elif Type == "Downgrade":
                    Text = '''800 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 800: Available = 1
            elif Level == 6:
                if Type == "Upgrade":
                    Text = '''800 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 800: Available = 1
                elif Type == "Downgrade":
                    Text = '''1600 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 1600: Available = 1
            elif Level == 7:
                if Type == "Upgrade":
                    Text = '''1600 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 1600: Available = 1
                elif Type == "Downgrade":
                    Text = '''3200 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 3200: Available = 1
            elif Level == 8:
                if Type == "Upgrade":
                    Text = '''3200 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 3200: Available = 1
                elif Type == "Downgrade":
                    Text = '''6400 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 6400: Available = 1
            elif Level == 9:
                if Type == "Upgrade":
                    Text = '''6400 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 6400: Available = 1
                elif Type == "Downgrade":
                    Text = '''12800 Submission Gems'''
                    if "Submission" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Submission"]["Amount"] > 12800: Available = 1
            elif Level == 10:
                if Type == "Upgrade":
                    Text = '''12800 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 12800: Available = 1
        elif AbilityID == "CSense":
            if Level == 0:
                Type = "Downgrade"
                if Type == "Downgrade":
                    Text = '''25 Loyalty Gems '''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 25: Available = 1
            elif Level == 1:
                if Type == "Upgrade":
                    Text = '''25 CPlea Gems'''
                    if "CPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["CPlea"]["Amount"] > 25: Available = 1
                elif Type == "Downgrade":
                    Text = '''50 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 50: Available = 1
            elif Level == 2:
                if Type == "Upgrade":
                    Text = '''50 CPlea Gems'''
                    if "CPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["CPlea"]["Amount"] > 50: Available = 1
                elif Type == "Downgrade":
                    Text = '''100 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 100: Available = 1
            elif Level == 3:
                if Type == "Upgrade":
                    Text = '''100 CPlea Gems'''
                    if "CPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["CPlea"]["Amount"] > 100: Available = 1
                elif Type == "Downgrade":
                    Text = '''200 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 200: Available = 1
            elif Level == 4:
                if Type == "Upgrade":
                    Text = '''200 CPlea Gems'''
                    if "CPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["CPlea"]["Amount"] > 200: Available = 1
                elif Type == "Downgrade":
                    Text = '''400 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 400: Available = 1
            elif Level == 5:
                if Type == "Upgrade":
                    Text = '''400 CPlea Gems'''
                    if "CPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["CPlea"]["Amount"] > 400: Available = 1
                elif Type == "Downgrade":
                    Text = '''800 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 800: Available = 1
            elif Level == 6:
                if Type == "Upgrade":
                    Text = '''800 CPlea Gems'''
                    if "CPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["CPlea"]["Amount"] > 800: Available = 1
                elif Type == "Downgrade":
                    Text = '''1600 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 1600: Available = 1
            elif Level == 7:
                if Type == "Upgrade":
                    Text = '''1600 CPlea Gems'''
                    if "CPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["CPlea"]["Amount"] > 1600: Available = 1
                elif Type == "Downgrade":
                    Text = '''3200 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 3200: Available = 1
            elif Level == 8:
                if Type == "Upgrade":
                    Text = '''3200 CPlea Gems'''
                    if "CPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["CPlea"]["Amount"] > 3200: Available = 1
                elif Type == "Downgrade":
                    Text = '''6400 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 6400: Available = 1
            elif Level == 9:
                if Type == "Upgrade":
                    Text = '''6400 CPlea Gems'''
                    if "CPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["CPlea"]["Amount"] > 6400: Available = 1
                elif Type == "Downgrade":
                    Text = '''12800 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 12800: Available = 1
            elif Level == 10:
                if Type == "Upgrade":
                    Text = '''12800 CPlea Gems'''
                    if "CPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["CPlea"]["Amount"] > 12800: Available = 1
        elif AbilityID == "VSense":
            if Level == 0:
                Type = "Downgrade"
                if Type == "Downgrade":
                    Text = '''25 Loyalty Gems '''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 25: Available = 1
            elif Level == 1:
                if Type == "Upgrade":
                    Text = '''25 VPlea Gems'''
                    if "VPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["CPlea"]["Amount"] > 25: Available = 1
                elif Type == "Downgrade":
                    Text = '''50 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 50: Available = 1
            elif Level == 2:
                if Type == "Upgrade":
                    Text = '''50 VPlea Gems'''
                    if "VPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["CPlea"]["Amount"] > 50: Available = 1
                elif Type == "Downgrade":
                    Text = '''100 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 100: Available = 1
            elif Level == 3:
                if Type == "Upgrade":
                    Text = '''100 VPlea Gems'''
                    if "VPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["CPlea"]["Amount"] > 100: Available = 1
                elif Type == "Downgrade":
                    Text = '''200 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 200: Available = 1
            elif Level == 4:
                if Type == "Upgrade":
                    Text = '''200 VPlea Gems'''
                    if "VPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["CPlea"]["Amount"] > 200: Available = 1
                elif Type == "Downgrade":
                    Text = '''400 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 400: Available = 1
            elif Level == 5:
                if Type == "Upgrade":
                    Text = '''400 VPlea Gems'''
                    if "VPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["CPlea"]["Amount"] > 400: Available = 1
                elif Type == "Downgrade":
                    Text = '''800 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 800: Available = 1
            elif Level == 6:
                if Type == "Upgrade":
                    Text = '''800 VPlea Gems'''
                    if "VPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["CPlea"]["Amount"] > 800: Available = 1
                elif Type == "Downgrade":
                    Text = '''1600 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 1600: Available = 1
            elif Level == 7:
                if Type == "Upgrade":
                    Text = '''1600 VPlea Gems'''
                    if "VPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["CPlea"]["Amount"] > 1600: Available = 1
                elif Type == "Downgrade":
                    Text = '''3200 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 3200: Available = 1
            elif Level == 8:
                if Type == "Upgrade":
                    Text = '''3200 VPlea Gems'''
                    if "VPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["CPlea"]["Amount"] > 3200: Available = 1
                elif Type == "Downgrade":
                    Text = '''6400 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 6400: Available = 1
            elif Level == 9:
                if Type == "Upgrade":
                    Text = '''6400 VPlea Gems'''
                    if "VPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["CPlea"]["Amount"] > 6400: Available = 1
                elif Type == "Downgrade":
                    Text = '''12800 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 12800: Available = 1
            elif Level == 10:
                if Type == "Upgrade":
                    Text = '''12800 VPlea Gems'''
                    if "VPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["CPlea"]["Amount"] > 12800: Available = 1
        elif AbilityID == "ASense":
            if Level == 0:
                Type = "Downgrade"
                if Type == "Downgrade":
                    Text = '''25 Loyalty Gems '''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 25: Available = 1
            elif Level == 1:
                if Type == "Upgrade":
                    Text = '''25 APlea Gems'''
                    if "APlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["APlea"]["Amount"] > 25: Available = 1
                elif Type == "Downgrade":
                    Text = '''50 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 50: Available = 1
            elif Level == 2:
                if Type == "Upgrade":
                    Text = '''50 APlea Gems'''
                    if "APlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["APlea"]["Amount"] > 50: Available = 1
                elif Type == "Downgrade":
                    Text = '''100 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 100: Available = 1
            elif Level == 3:
                if Type == "Upgrade":
                    Text = '''100 APlea Gems'''
                    if "APlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["APlea"]["Amount"] > 100: Available = 1
                elif Type == "Downgrade":
                    Text = '''200 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 200: Available = 1
            elif Level == 4:
                if Type == "Upgrade":
                    Text = '''200 APlea Gems'''
                    if "APlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["APlea"]["Amount"] > 200: Available = 1
                elif Type == "Downgrade":
                    Text = '''400 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 400: Available = 1
            elif Level == 5:
                if Type == "Upgrade":
                    Text = '''400 APlea Gems'''
                    if "APlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["APlea"]["Amount"] > 400: Available = 1
                elif Type == "Downgrade":
                    Text = '''800 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 800: Available = 1
            elif Level == 6:
                if Type == "Upgrade":
                    Text = '''800 APlea Gems'''
                    if "APlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["APlea"]["Amount"] > 800: Available = 1
                elif Type == "Downgrade":
                    Text = '''1600 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 1600: Available = 1
            elif Level == 7:
                if Type == "Upgrade":
                    Text = '''1600 APlea Gems'''
                    if "APlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["APlea"]["Amount"] > 1600: Available = 1
                elif Type == "Downgrade":
                    Text = '''3200 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 3200: Available = 1
            elif Level == 8:
                if Type == "Upgrade":
                    Text = '''3200 APlea Gems'''
                    if "APlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["APlea"]["Amount"] > 3200: Available = 1
                elif Type == "Downgrade":
                    Text = '''6400 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 6400: Available = 1
            elif Level == 9:
                if Type == "Upgrade":
                    Text = '''6400 APlea Gems'''
                    if "APlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["APlea"]["Amount"] > 6400: Available = 1
                elif Type == "Downgrade":
                    Text = '''12800 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 12800: Available = 1
            elif Level == 10:
                if Type == "Upgrade":
                    Text = '''12800 APlea Gems'''
                    if "APlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["APlea"]["Amount"] > 12800: Available = 1
        elif AbilityID == "PSense":
            if Level == 0:
                Type = "Downgrade"
                if Type == "Downgrade":
                    Text = '''25 Loyalty Gems '''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 25: Available = 1
            elif Level == 1:
                if Type == "Upgrade":
                    Text = '''25 PPlea Gems'''
                    if "PPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["APlea"]["Amount"] > 25: Available = 1
                elif Type == "Downgrade":
                    Text = '''50 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 50: Available = 1
            elif Level == 2:
                if Type == "Upgrade":
                    Text = '''50 PPlea Gems'''
                    if "PPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["APlea"]["Amount"] > 50: Available = 1
                elif Type == "Downgrade":
                    Text = '''100 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 100: Available = 1
            elif Level == 3:
                if Type == "Upgrade":
                    Text = '''100 PPlea Gems'''
                    if "PPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["APlea"]["Amount"] > 100: Available = 1
                elif Type == "Downgrade":
                    Text = '''200 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 200: Available = 1
            elif Level == 4:
                if Type == "Upgrade":
                    Text = '''200 PPlea Gems'''
                    if "PPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["APlea"]["Amount"] > 200: Available = 1
                elif Type == "Downgrade":
                    Text = '''400 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 400: Available = 1
            elif Level == 5:
                if Type == "Upgrade":
                    Text = '''400 PPlea Gems'''
                    if "PPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["APlea"]["Amount"] > 400: Available = 1
                elif Type == "Downgrade":
                    Text = '''800 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 800: Available = 1
            elif Level == 6:
                if Type == "Upgrade":
                    Text = '''800 PPlea Gems'''
                    if "PPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["APlea"]["Amount"] > 800: Available = 1
                elif Type == "Downgrade":
                    Text = '''1600 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 1600: Available = 1
            elif Level == 7:
                if Type == "Upgrade":
                    Text = '''1600 PPlea Gems'''
                    if "PPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["APlea"]["Amount"] > 1600: Available = 1
                elif Type == "Downgrade":
                    Text = '''3200 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 3200: Available = 1
            elif Level == 8:
                if Type == "Upgrade":
                    Text = '''3200 PPlea Gems'''
                    if "PPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["APlea"]["Amount"] > 3200: Available = 1
                elif Type == "Downgrade":
                    Text = '''6400 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 6400: Available = 1
            elif Level == 9:
                if Type == "Upgrade":
                    Text = '''6400 PPlea Gems'''
                    if "PPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["APlea"]["Amount"] > 6400: Available = 1
                elif Type == "Downgrade":
                    Text = '''12800 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 12800: Available = 1
            elif Level == 10:
                if Type == "Upgrade":
                    Text = '''12800 PPlea Gems'''
                    if "PPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["APlea"]["Amount"] > 12800: Available = 1
        elif AbilityID == "MSense":
            if Level == 0:
                Type = "Downgrade"
                if Type == "Downgrade":
                    Text = '''25 Loyalty Gems '''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 25: Available = 1
            elif Level == 1:
                if Type == "Upgrade":
                    Text = '''25 MPlea Gems'''
                    if "MPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["MPlea"]["Amount"] > 25: Available = 1
                elif Type == "Downgrade":
                    Text = '''50 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 50: Available = 1
            elif Level == 2:
                if Type == "Upgrade":
                    Text = '''50 MPlea Gems'''
                    if "MPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["MPlea"]["Amount"] > 50: Available = 1
                elif Type == "Downgrade":
                    Text = '''100 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 100: Available = 1
            elif Level == 3:
                if Type == "Upgrade":
                    Text = '''100 MPlea Gems'''
                    if "MPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["MPlea"]["Amount"] > 100: Available = 1
                elif Type == "Downgrade":
                    Text = '''200 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 200: Available = 1
            elif Level == 4:
                if Type == "Upgrade":
                    Text = '''200 MPlea Gems'''
                    if "MPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["MPlea"]["Amount"] > 200: Available = 1
                elif Type == "Downgrade":
                    Text = '''400 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 400: Available = 1
            elif Level == 5:
                if Type == "Upgrade":
                    Text = '''400 MPlea Gems'''
                    if "MPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["MPlea"]["Amount"] > 400: Available = 1
                elif Type == "Downgrade":
                    Text = '''800 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 800: Available = 1
            elif Level == 6:
                if Type == "Upgrade":
                    Text = '''800 MPlea Gems'''
                    if "MPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["MPlea"]["Amount"] > 800: Available = 1
                elif Type == "Downgrade":
                    Text = '''1600 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 1600: Available = 1
            elif Level == 7:
                if Type == "Upgrade":
                    Text = '''1600 MPlea Gems'''
                    if "MPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["MPlea"]["Amount"] > 1600: Available = 1
                elif Type == "Downgrade":
                    Text = '''3200 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 3200: Available = 1
            elif Level == 8:
                if Type == "Upgrade":
                    Text = '''3200 MPlea Gems'''
                    if "MPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["MPlea"]["Amount"] > 3200: Available = 1
                elif Type == "Downgrade":
                    Text = '''6400 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 6400: Available = 1
            elif Level == 9:
                if Type == "Upgrade":
                    Text = '''6400 MPlea Gems'''
                    if "MPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["MPlea"]["Amount"] > 6400: Available = 1
                elif Type == "Downgrade":
                    Text = '''12800 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 12800: Available = 1
            elif Level == 10:
                if Type == "Upgrade":
                    Text = '''12800 MPlea Gems'''
                    if "MPlea" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["MPlea"]["Amount"] > 12800: Available = 1
        elif AbilityID == "Service":
            if Level == 0:
                Type = "Downgrade"
                if Type == "Downgrade":
                    Text = '''25 Superiority Gems '''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 25: Available = 1
            elif Level == 1:
                if Type == "Upgrade":
                    Text = '''25 Service Gems'''
                    if "Service" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 25: Available = 1
                elif Type == "Downgrade":
                    Text = '''50 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 50: Available = 1
            elif Level == 2:
                if Type == "Upgrade":
                    Text = '''50 Service Gems'''
                    if "Service" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 50: Available = 1
                elif Type == "Downgrade":
                    Text = '''100 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 100: Available = 1
            elif Level == 3:
                if Type == "Upgrade":
                    Text = '''100 Service Gems'''
                    if "Service" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 100: Available = 1
                elif Type == "Downgrade":
                    Text = '''200 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 200: Available = 1
            elif Level == 4:
                if Type == "Upgrade":
                    Text = '''200 Service Gems'''
                    if "Service" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 200: Available = 1
                elif Type == "Downgrade":
                    Text = '''400 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 400: Available = 1
            elif Level == 5:
                if Type == "Upgrade":
                    Text = '''400 Service Gems'''
                    if "Service" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 400: Available = 1
                elif Type == "Downgrade":
                    Text = '''800 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 800: Available = 1
            elif Level == 6:
                if Type == "Upgrade":
                    Text = '''800 Service Gems'''
                    if "Service" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 800: Available = 1
                elif Type == "Downgrade":
                    Text = '''1600 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 1600: Available = 1
            elif Level == 7:
                if Type == "Upgrade":
                    Text = '''1600 Service Gems'''
                    if "Service" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 1600: Available = 1
                elif Type == "Downgrade":
                    Text = '''3200 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 3200: Available = 1
            elif Level == 8:
                if Type == "Upgrade":
                    Text = '''3200 Service Gems'''
                    if "Service" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 3200: Available = 1
                elif Type == "Downgrade":
                    Text = '''6400 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 6400: Available = 1
            elif Level == 9:
                if Type == "Upgrade":
                    Text = '''6400 Service Gems'''
                    if "Service" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 6400: Available = 1
                elif Type == "Downgrade":
                    Text = '''12800 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 12800: Available = 1
            elif Level == 10:
                if Type == "Upgrade":
                    Text = '''12800 Service Gems'''
                    if "Service" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 12800: Available = 1
        elif AbilityID == "Sadism":
            if Level == 0:
                Type = "Downgrade"
                if Type == "Downgrade":
                    Text = '''25 Pain Gems '''
                    if "Pain" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 25: Available = 1
            elif Level == 1:
                if Type == "Upgrade":
                    Text = '''25 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 25: Available = 1
                elif Type == "Downgrade":
                    Text = '''50 Pain Gems'''
                    if "Pain" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 50: Available = 1
            elif Level == 2:
                if Type == "Upgrade":
                    Text = '''50 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 50: Available = 1
                elif Type == "Downgrade":
                    Text = '''100 Pain Gems'''
                    if "Pain" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 100: Available = 1
            elif Level == 3:
                if Type == "Upgrade":
                    Text = '''100 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 100: Available = 1
                elif Type == "Downgrade":
                    Text = '''200 Pain Gems'''
                    if "Pain" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 200: Available = 1
            elif Level == 4:
                if Type == "Upgrade":
                    Text = '''200 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 200: Available = 1
                elif Type == "Downgrade":
                    Text = '''400 Pain Gems'''
                    if "Pain" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 400: Available = 1
            elif Level == 5:
                if Type == "Upgrade":
                    Text = '''400 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 400: Available = 1
                elif Type == "Downgrade":
                    Text = '''800 Pain Gems'''
                    if "Pain" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 800: Available = 1
            elif Level == 6:
                if Type == "Upgrade":
                    Text = '''800 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 800: Available = 1
                elif Type == "Downgrade":
                    Text = '''1600 Pain Gems'''
                    if "Pain" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 1600: Available = 1
            elif Level == 7:
                if Type == "Upgrade":
                    Text = '''1600 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 1600: Available = 1
                elif Type == "Downgrade":
                    Text = '''3200 Pain Gems'''
                    if "Pain" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 3200: Available = 1
            elif Level == 8:
                if Type == "Upgrade":
                    Text = '''3200 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 3200: Available = 1
                elif Type == "Downgrade":
                    Text = '''6400 Pain Gems'''
                    if "Pain" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 6400: Available = 1
            elif Level == 9:
                if Type == "Upgrade":
                    Text = '''6400 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 6400: Available = 1
                elif Type == "Downgrade":
                    Text = '''12800 Pain Gems'''
                    if "Pain" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 12800: Available = 1
            elif Level == 10:
                if Type == "Upgrade":
                    Text = '''12800 Loyalty Gems'''
                    if "Loyalty" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Loyalty"]["Amount"] > 12800: Available = 1
        elif AbilityID == "Masochism":
            if Level == 0:
                Type = "Downgrade"
                if Type == "Downgrade":
                    Text = '''25 Superiority Gems '''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 25: Available = 1
            elif Level == 1:
                if Type == "Upgrade":
                    Text = '''25 Pain Gems'''
                    if "Pain" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 25: Available = 1
                elif Type == "Downgrade":
                    Text = '''50 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 50: Available = 1
            elif Level == 2:
                if Type == "Upgrade":
                    Text = '''50 Pain Gems'''
                    if "Pain" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 50: Available = 1
                elif Type == "Downgrade":
                    Text = '''100 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 100: Available = 1
            elif Level == 3:
                if Type == "Upgrade":
                    Text = '''100 Pain Gems'''
                    if "Pain" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 100: Available = 1
                elif Type == "Downgrade":
                    Text = '''200 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 200: Available = 1
            elif Level == 4:
                if Type == "Upgrade":
                    Text = '''200 Pain Gems'''
                    if "Pain" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 200: Available = 1
                elif Type == "Downgrade":
                    Text = '''400 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 400: Available = 1
            elif Level == 5:
                if Type == "Upgrade":
                    Text = '''400 Pain Gems'''
                    if "Pain" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 400: Available = 1
                elif Type == "Downgrade":
                    Text = '''800 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 800: Available = 1
            elif Level == 6:
                if Type == "Upgrade":
                    Text = '''800 Pain Gems'''
                    if "Pain" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 800: Available = 1
                elif Type == "Downgrade":
                    Text = '''1600 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 1600: Available = 1
            elif Level == 7:
                if Type == "Upgrade":
                    Text = '''1600 Pain Gems'''
                    if "Pain" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 1600: Available = 1
                elif Type == "Downgrade":
                    Text = '''3200 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 3200: Available = 1
            elif Level == 8:
                if Type == "Upgrade":
                    Text = '''3200 Pain Gems'''
                    if "Pain" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 3200: Available = 1
                elif Type == "Downgrade":
                    Text = '''6400 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 6400: Available = 1
            elif Level == 9:
                if Type == "Upgrade":
                    Text = '''6400 Pain Gems'''
                    if "Pain" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 6400: Available = 1
                elif Type == "Downgrade":
                    Text = '''12800 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 12800: Available = 1
            elif Level == 10:
                if Type == "Upgrade":
                    Text = '''12800 Pain Gems'''
                    if "Pain" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Service"]["Amount"] > 12800: Available = 1
        elif AbilityID == "Exhibitionism":
            if Level == 0:
                Type = "Downgrade"
                if Type == "Downgrade":
                    Text = '''25 Superiority Gems '''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 25: Available = 1
            elif Level == 1:
                if Type == "Upgrade":
                    Text = '''25 Shame Gems'''
                    if "Shame" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Shame"]["Amount"] > 25: Available = 1
                elif Type == "Downgrade":
                    Text = '''50 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 50: Available = 1
            elif Level == 2:
                if Type == "Upgrade":
                    Text = '''50 Shame Gems'''
                    if "Shame" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Shame"]["Amount"] > 50: Available = 1
                elif Type == "Downgrade":
                    Text = '''100 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 100: Available = 1
            elif Level == 3:
                if Type == "Upgrade":
                    Text = '''100 Shame Gems'''
                    if "Shame" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Shame"]["Amount"] > 100: Available = 1
                elif Type == "Downgrade":
                    Text = '''200 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 200: Available = 1
            elif Level == 4:
                if Type == "Upgrade":
                    Text = '''200 Shame Gems'''
                    if "Shame" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Shame"]["Amount"] > 200: Available = 1
                elif Type == "Downgrade":
                    Text = '''400 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 400: Available = 1
            elif Level == 5:
                if Type == "Upgrade":
                    Text = '''400 Shame Gems'''
                    if "Shame" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Shame"]["Amount"] > 400: Available = 1
                elif Type == "Downgrade":
                    Text = '''800 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 800: Available = 1
            elif Level == 6:
                if Type == "Upgrade":
                    Text = '''800 Shame Gems'''
                    if "Shame" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Shame"]["Amount"] > 800: Available = 1
                elif Type == "Downgrade":
                    Text = '''1600 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 1600: Available = 1
            elif Level == 7:
                if Type == "Upgrade":
                    Text = '''1600 Shame Gems'''
                    if "Shame" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Shame"]["Amount"] > 1600: Available = 1
                elif Type == "Downgrade":
                    Text = '''3200 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 3200: Available = 1
            elif Level == 8:
                if Type == "Upgrade":
                    Text = '''3200 Shame Gems'''
                    if "Shame" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Shame"]["Amount"] > 3200: Available = 1
                elif Type == "Downgrade":
                    Text = '''6400 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 6400: Available = 1
            elif Level == 9:
                if Type == "Upgrade":
                    Text = '''6400 Shame Gems'''
                    if "Shame" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Shame"]["Amount"] > 6400: Available = 1
                elif Type == "Downgrade":
                    Text = '''12800 Superiority Gems'''
                    if "Superiority" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Superiority"]["Amount"] > 12800: Available = 1
            elif Level == 10:
                if Type == "Upgrade":
                    Text = '''12800 Shame Gems'''
                    if "Shame" in Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"] and Globals.SoLNPCData[NPCID]["Relations"][OtherID]["Gems"]["Shame"]["Amount"] > 12800: Available = 1

        return Text, Available
    except Exception as e:
        Log(2, "ERROR RETRIEVING ABILITY CONDITIONS", e, AbilityID, Level, Type)


def GetAbilityStaticWidget(AbilityID, Data):
    try:
        Value = Data["Level"]
    except:
        Value = 0
    if AbilityID == "Obedience":
        AbilityLabel = QLabel()
        AbilityLabel.setAlignment(QtCore.Qt.AlignCenter)
        AbilityLabel.setFont(QFont('Segoe UI', 12))
        AbilityLabel.setText(f'''Obedience: {Value}''')

        AbilityLabel.setMinimumWidth(200)
        AbilityLabel.setMaximumWidth(200)
        AbilityLabel.setMinimumHeight(35)
        AbilityLabel.setMaximumHeight(35)

        return AbilityLabel
    elif AbilityID == "Lust":
        AbilityLabel = QLabel()
        AbilityLabel.setAlignment(QtCore.Qt.AlignCenter)
        AbilityLabel.setFont(QFont('Segoe UI', 12))
        AbilityLabel.setText(f'''Lust: {Value}''')

        AbilityLabel.setMinimumWidth(200)
        AbilityLabel.setMaximumWidth(200)
        AbilityLabel.setMinimumHeight(35)
        AbilityLabel.setMaximumHeight(35)

        return AbilityLabel
    elif AbilityID == "Intimacy":
        AbilityLabel = QLabel()
        AbilityLabel.setAlignment(QtCore.Qt.AlignCenter)
        AbilityLabel.setFont(QFont('Segoe UI', 12))
        AbilityLabel.setText(f'''Intimacy: {Value}''')

        AbilityLabel.setMinimumWidth(200)
        AbilityLabel.setMaximumWidth(200)
        AbilityLabel.setMinimumHeight(35)
        AbilityLabel.setMaximumHeight(35)

        return AbilityLabel
    elif AbilityID == "Submission":
        AbilityLabel = QLabel()
        AbilityLabel.setAlignment(QtCore.Qt.AlignCenter)
        AbilityLabel.setFont(QFont('Segoe UI', 12))
        AbilityLabel.setText(f'''Submission: {Value}''')

        AbilityLabel.setMinimumWidth(200)
        AbilityLabel.setMaximumWidth(200)
        AbilityLabel.setMinimumHeight(35)
        AbilityLabel.setMaximumHeight(35)

        return AbilityLabel
    elif AbilityID == "Superiority":
        AbilityLabel = QLabel()
        AbilityLabel.setAlignment(QtCore.Qt.AlignCenter)
        AbilityLabel.setFont(QFont('Segoe UI', 12))
        AbilityLabel.setText(f'''Superiority: {Value}''')

        AbilityLabel.setMinimumWidth(200)
        AbilityLabel.setMaximumWidth(200)
        AbilityLabel.setMinimumHeight(35)
        AbilityLabel.setMaximumHeight(35)

        return AbilityLabel
    elif AbilityID == "CSense":
        AbilityLabel = QLabel()
        AbilityLabel.setAlignment(QtCore.Qt.AlignCenter)
        AbilityLabel.setFont(QFont('Segoe UI', 12))
        AbilityLabel.setText(f'''CSense: {Value}''')

        AbilityLabel.setMinimumWidth(200)
        AbilityLabel.setMaximumWidth(200)
        AbilityLabel.setMinimumHeight(35)
        AbilityLabel.setMaximumHeight(35)

        return AbilityLabel
    elif AbilityID == "VSense":
        AbilityLabel = QLabel()
        AbilityLabel.setAlignment(QtCore.Qt.AlignCenter)
        AbilityLabel.setFont(QFont('Segoe UI', 12))
        AbilityLabel.setText(f'''VSense: {Value}''')

        AbilityLabel.setMinimumWidth(200)
        AbilityLabel.setMaximumWidth(200)
        AbilityLabel.setMinimumHeight(35)
        AbilityLabel.setMaximumHeight(35)

        return AbilityLabel
    elif AbilityID == "ASense":
        AbilityLabel = QLabel()
        AbilityLabel.setAlignment(QtCore.Qt.AlignCenter)
        AbilityLabel.setFont(QFont('Segoe UI', 12))
        AbilityLabel.setText(f'''ASense: {Value}''')

        AbilityLabel.setMinimumWidth(200)
        AbilityLabel.setMaximumWidth(200)
        AbilityLabel.setMinimumHeight(35)
        AbilityLabel.setMaximumHeight(35)

        return AbilityLabel
    elif AbilityID == "PSense":
        AbilityLabel = QLabel()
        AbilityLabel.setAlignment(QtCore.Qt.AlignCenter)
        AbilityLabel.setFont(QFont('Segoe UI', 12))
        AbilityLabel.setText(f'''PSense: {Value}''')

        AbilityLabel.setMinimumWidth(200)
        AbilityLabel.setMaximumWidth(200)
        AbilityLabel.setMinimumHeight(35)
        AbilityLabel.setMaximumHeight(35)

        return AbilityLabel
    elif AbilityID == "MSense":
        AbilityLabel = QLabel()
        AbilityLabel.setAlignment(QtCore.Qt.AlignCenter)
        AbilityLabel.setFont(QFont('Segoe UI', 12))
        AbilityLabel.setText(f'''MSense: {Value}''')

        AbilityLabel.setMinimumWidth(200)
        AbilityLabel.setMaximumWidth(200)
        AbilityLabel.setMinimumHeight(35)
        AbilityLabel.setMaximumHeight(35)

        return AbilityLabel
    elif AbilityID == "Service":
        AbilityLabel = QLabel()
        AbilityLabel.setAlignment(QtCore.Qt.AlignCenter)
        AbilityLabel.setFont(QFont('Segoe UI', 12))
        AbilityLabel.setText(f'''Service: {Value}''')

        AbilityLabel.setMinimumWidth(200)
        AbilityLabel.setMaximumWidth(200)
        AbilityLabel.setMinimumHeight(35)
        AbilityLabel.setMaximumHeight(35)

        return AbilityLabel
    elif AbilityID == "Sadism":
        AbilityLabel = QLabel()
        AbilityLabel.setAlignment(QtCore.Qt.AlignCenter)
        AbilityLabel.setFont(QFont('Segoe UI', 12))
        AbilityLabel.setText(f'''Sadism: {Value}''')

        AbilityLabel.setMinimumWidth(200)
        AbilityLabel.setMaximumWidth(200)
        AbilityLabel.setMinimumHeight(35)
        AbilityLabel.setMaximumHeight(35)

        return AbilityLabel
    elif AbilityID == "Masochism":
        AbilityLabel = QLabel()
        AbilityLabel.setAlignment(QtCore.Qt.AlignCenter)
        AbilityLabel.setFont(QFont('Segoe UI', 12))
        AbilityLabel.setText(f'''Masochism: {Value}''')

        AbilityLabel.setMinimumWidth(200)
        AbilityLabel.setMaximumWidth(200)
        AbilityLabel.setMinimumHeight(35)
        AbilityLabel.setMaximumHeight(35)

        return AbilityLabel
    elif AbilityID == "Exhibitionism":
        AbilityLabel = QLabel()
        AbilityLabel.setAlignment(QtCore.Qt.AlignCenter)
        AbilityLabel.setFont(QFont('Segoe UI', 12))
        AbilityLabel.setText(f'''Exhibitionism: {Value}''')

        AbilityLabel.setMinimumWidth(200)
        AbilityLabel.setMaximumWidth(200)
        AbilityLabel.setMinimumHeight(35)
        AbilityLabel.setMaximumHeight(35)

        return AbilityLabel

    return None


def GetAbilityDynamicWidget(AbilityID, Data, NPCID, OtherID, Flags):
    Value = 0
    if Data != None:
        Value = Data["Level"]

    if AbilityID == "Obedience":
        Widget = QWidget(objectName = "Transparent")

        TitleLabel = QLabel("Obedience", Widget, objectName = "SubTitle")
        TitleLabel.setProperty("Color","Light")
        TitleLabel.setGeometry(0,0,250,40)
        TitleLabel.setMinimumHeight(40)
        TitleLabel.setMaximumHeight(40)

        Holder = QWidget(Widget)
        Holder.setGeometry(0,45,250,0)

        Layout = QVBoxLayout()
        Layout.setSpacing(0)
        Layout.setContentsMargins(0, 0, 0, 0)
        Widget.setContentsMargins(0, 0, 0, 0)
        Holder.setLayout(Layout)

        Height = 0

        if Value < 10:
            UL = QWidget()

            ULBackLabel = QLabel(UL)
            ULBackLabel.setProperty("Color","Dark")
            ULLabel = QLabel(UL, objectName = "SmallText")
            ULLabel.setProperty("Color","Dark")
            ULLabel.setProperty("Border","None")
            ULLabel.setGeometry(0,0,215,35)
            ULLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value+1, "Upgrade", NPCID, OtherID)
            if "UpgradeForceAvailable" in Flags and Flags["UpgradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                ULLabel.setProperty("Selected",1)

            ULLabel.setText(f'''Obedience {Value+1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(ULLabel)
            ULLabel.setGeometry(5,1,210,FontHeight)
            ULBackLabel.setGeometry(0,0,250,FontHeight+2)

            def ULClick():
                if ULButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, 1)
                    except Exception as e:
                        print(e)
            ULButton = QLabel(UL)
            ULButton.setGeometry(215,1,33,33)
            ULButton.mouseReleaseEvent = lambda event: ULClick()
            ULButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "UpArrow.png" ) ))
            ULButton.setProperty("Color","None")
            ULButton.setScaledContents(True)
            ULButton.Available = Available

            "            "

            UL.setMinimumHeight(ULBackLabel.height())
            UL.setMaximumHeight(ULBackLabel.height())

            Layout.addWidget(UL)
            Height += UL.height()

        CL = QWidget()

        CLLabel = QLabel(CL, objectName = "SmallText")
        CLLabel.setProperty("Color","Dark")
        CLLabel.setGeometry(0,0,250,35)

        Text = "Current Level"
        CLLabel.setText(f'''Obedience {Value}: {Text}''')

        CL.setMinimumHeight(35)
        CL.setMaximumHeight(35)

        Layout.addWidget(CL)
        Height += CL.height()

        if Value > 0:
            DL = QWidget()

            DLBackLabel = QLabel(DL)
            DLBackLabel.setProperty("Color","Dark")
            DLLabel = QLabel(DL, objectName = "SmallText")
            DLLabel.setProperty("Color","Dark")
            DLLabel.setProperty("Border","None")
            DLLabel.setGeometry(0,0,215,35)
            DLLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value-1, "Downgrade", NPCID, OtherID)
            if "DowngradeForceAvailable" in Flags and Flags["DowngradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                DLLabel.setProperty("Selected",1)

            DLLabel.setText(f'''Obedience {Value-1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(DLLabel)
            DLLabel.setGeometry(5,1,210,FontHeight)
            DLBackLabel.setGeometry(0,0,250,FontHeight+2)

            def DLClick():
                if DLButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, -1)
                    except Exception as e:
                        print(e)
            DLButton = QLabel(DL)
            DLButton.setGeometry(215,1,33,33)
            DLButton.mouseReleaseEvent = lambda event: DLClick()
            DLButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "DownArrow.png" ) ))
            DLButton.setProperty("Color","None")
            DLButton.setScaledContents(True)
            DLButton.Available = Available

            DL.setMinimumHeight(DLBackLabel.height())
            DL.setMaximumHeight(DLBackLabel.height())

            Layout.addWidget(DL)
            Height += DL.height()

        Holder.setMinimumHeight(Height)
        Holder.setMaximumHeight(Height)

        Widget.setMinimumHeight(Height+45)
        Widget.setMaximumHeight(Height+45)

        Widget.setMinimumWidth(250)
        Widget.setMaximumWidth(250)

        return Widget

    elif AbilityID == "Lust":
        Widget = QWidget(objectName = "Transparent")

        TitleLabel = QLabel("Lust", Widget, objectName = "SubTitle")
        TitleLabel.setProperty("Color","Light")
        TitleLabel.setGeometry(0,0,250,40)
        TitleLabel.setMinimumHeight(40)
        TitleLabel.setMaximumHeight(40)

        Holder = QWidget(Widget)
        Holder.setGeometry(0,45,250,0)

        Layout = QVBoxLayout()
        Layout.setSpacing(0)
        Layout.setContentsMargins(0, 0, 0, 0)
        Widget.setContentsMargins(0, 0, 0, 0)
        Holder.setLayout(Layout)

        Height = 0

        if Value < 10:
            UL = QWidget()

            ULBackLabel = QLabel(UL)
            ULBackLabel.setProperty("Color","Dark")
            ULLabel = QLabel(UL, objectName = "SmallText")
            ULLabel.setProperty("Color","Dark")
            ULLabel.setProperty("Border","None")
            ULLabel.setGeometry(0,0,215,35)
            ULLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value+1, "Upgrade", NPCID, OtherID)
            if "UpgradeForceAvailable" in Flags and Flags["UpgradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                ULLabel.setProperty("Selected",1)

            ULLabel.setText(f'''Lust {Value+1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(ULLabel)
            ULLabel.setGeometry(5,1,210,FontHeight)
            ULBackLabel.setGeometry(0,0,250,FontHeight+2)

            def ULClick():
                if ULButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, 1)
                    except Exception as e:
                        print(e)
            ULButton = QLabel(UL)
            ULButton.setGeometry(215,1,33,33)
            ULButton.mouseReleaseEvent = lambda event: ULClick()
            ULButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "UpArrow.png" ) ))
            ULButton.setProperty("Color","None")
            ULButton.setScaledContents(True)
            ULButton.Available = Available
            UL.setMinimumHeight(ULBackLabel.height())
            UL.setMaximumHeight(ULBackLabel.height())

            Layout.addWidget(UL)
            Height += UL.height()

        CL = QWidget()

        CLLabel = QLabel(CL, objectName = "SmallText")
        CLLabel.setProperty("Color","Dark")
        CLLabel.setGeometry(0,0,250,35)

        Text = "Current Level"
        CLLabel.setText(f'''Lust {Value}: {Text}''')

        CL.setMinimumHeight(35)
        CL.setMaximumHeight(35)

        Layout.addWidget(CL)
        Height += CL.height()

        if Value > 0:
            DL = QWidget()

            DLBackLabel = QLabel(DL)
            DLBackLabel.setProperty("Color","Dark")
            DLLabel = QLabel(DL, objectName = "SmallText")
            DLLabel.setProperty("Color","Dark")
            DLLabel.setProperty("Border","None")
            DLLabel.setGeometry(0,0,215,35)
            DLLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value-1, "Downgrade", NPCID, OtherID)
            if "DowngradeForceAvailable" in Flags and Flags["DowngradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                DLLabel.setProperty("Selected",1)

            DLLabel.setText(f'''Lust {Value-1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(DLLabel)
            DLLabel.setGeometry(5,1,210,FontHeight)
            DLBackLabel.setGeometry(0,0,250,FontHeight+2)

            def DLClick():
                if DLButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, -1)
                    except Exception as e:
                        print(e)
            DLButton = QLabel(DL)
            DLButton.setGeometry(215,1,33,33)
            DLButton.mouseReleaseEvent = lambda event: DLClick()
            DLButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "DownArrow.png" ) ))
            DLButton.setProperty("Color","None")
            DLButton.setScaledContents(True)
            DLButton.Available = Available
            DL.setMinimumHeight(DLBackLabel.height())
            DL.setMaximumHeight(DLBackLabel.height())

            Layout.addWidget(DL)
            Height += DL.height()

        Holder.setMinimumHeight(Height)
        Holder.setMaximumHeight(Height)

        Widget.setMinimumHeight(Height+45)
        Widget.setMaximumHeight(Height+45)

        Widget.setMinimumWidth(250)
        Widget.setMaximumWidth(250)

        return Widget
    elif AbilityID == "Intimacy":
        Widget = QWidget(objectName = "Transparent")

        TitleLabel = QLabel("Intimacy", Widget, objectName = "SubTitle")
        TitleLabel.setProperty("Color","Light")
        TitleLabel.setGeometry(0,0,250,40)
        TitleLabel.setMinimumHeight(40)
        TitleLabel.setMaximumHeight(40)

        Holder = QWidget(Widget)
        Holder.setGeometry(0,45,250,0)

        Layout = QVBoxLayout()
        Layout.setSpacing(0)
        Layout.setContentsMargins(0, 0, 0, 0)
        Widget.setContentsMargins(0, 0, 0, 0)
        Holder.setLayout(Layout)

        Height = 0

        if Value < 10:
            UL = QWidget()

            ULBackLabel = QLabel(UL)
            ULBackLabel.setProperty("Color","Dark")
            ULLabel = QLabel(UL, objectName = "SmallText")
            ULLabel.setProperty("Color","Dark")
            ULLabel.setProperty("Border","None")
            ULLabel.setGeometry(0,0,215,35)
            ULLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value+1, "Upgrade", NPCID, OtherID)
            if "UpgradeForceAvailable" in Flags and Flags["UpgradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                ULLabel.setProperty("Selected",1)

            ULLabel.setText(f'''Intimacy {Value+1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(ULLabel)
            ULLabel.setGeometry(5,1,210,FontHeight)
            ULBackLabel.setGeometry(0,0,250,FontHeight+2)

            def ULClick():
                if ULButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, 1)
                    except Exception as e:
                        print(e)
            ULButton = QLabel(UL)
            ULButton.setGeometry(215,1,33,33)
            ULButton.mouseReleaseEvent = lambda event: ULClick()
            ULButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "UpArrow.png" ) ))
            ULButton.setProperty("Color","None")
            ULButton.setScaledContents(True)
            ULButton.Available = Available
            UL.setMinimumHeight(ULBackLabel.height())
            UL.setMaximumHeight(ULBackLabel.height())

            Layout.addWidget(UL)
            Height += UL.height()

        CL = QWidget()

        CLLabel = QLabel(CL, objectName = "SmallText")
        CLLabel.setProperty("Color","Dark")
        CLLabel.setGeometry(0,0,250,35)

        Text = "Current Level"
        CLLabel.setText(f'''Intimacy {Value}: {Text}''')

        CL.setMinimumHeight(35)
        CL.setMaximumHeight(35)

        Layout.addWidget(CL)
        Height += CL.height()

        if Value > 0:
            DL = QWidget()

            DLBackLabel = QLabel(DL)
            DLBackLabel.setProperty("Color","Dark")
            DLLabel = QLabel(DL, objectName = "SmallText")
            DLLabel.setProperty("Color","Dark")
            DLLabel.setProperty("Border","None")
            DLLabel.setGeometry(0,0,215,35)
            DLLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value-1, "Downgrade", NPCID, OtherID)
            if "DowngradeForceAvailable" in Flags and Flags["DowngradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                DLLabel.setProperty("Selected",1)

            DLLabel.setText(f'''Intimacy {Value-1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(DLLabel)
            DLLabel.setGeometry(5,1,210,FontHeight)
            DLBackLabel.setGeometry(0,0,250,FontHeight+2)

            def DLClick():
                if DLButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, -1)
                    except Exception as e:
                        print(e)
            DLButton = QLabel(DL)
            DLButton.setGeometry(215,1,33,33)
            DLButton.mouseReleaseEvent = lambda event: DLClick()
            DLButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "DownArrow.png" ) ))
            DLButton.setProperty("Color","None")
            DLButton.setScaledContents(True)
            DLButton.Available = Available
            DL.setMinimumHeight(DLBackLabel.height())
            DL.setMaximumHeight(DLBackLabel.height())

            Layout.addWidget(DL)
            Height += DL.height()

        Holder.setMinimumHeight(Height)
        Holder.setMaximumHeight(Height)

        Widget.setMinimumHeight(Height+45)
        Widget.setMaximumHeight(Height+45)

        Widget.setMinimumWidth(250)
        Widget.setMaximumWidth(250)

        return Widget
    elif AbilityID == "Submission":
        Widget = QWidget(objectName = "Transparent")

        TitleLabel = QLabel("Submission", Widget, objectName = "SubTitle")
        TitleLabel.setProperty("Color","Light")
        TitleLabel.setGeometry(0,0,250,40)
        TitleLabel.setMinimumHeight(40)
        TitleLabel.setMaximumHeight(40)

        Holder = QWidget(Widget)
        Holder.setGeometry(0,45,250,0)

        Layout = QVBoxLayout()
        Layout.setSpacing(0)
        Layout.setContentsMargins(0, 0, 0, 0)
        Widget.setContentsMargins(0, 0, 0, 0)
        Holder.setLayout(Layout)

        Height = 0

        if Value < 10:
            UL = QWidget()

            ULBackLabel = QLabel(UL)
            ULBackLabel.setProperty("Color","Dark")
            ULLabel = QLabel(UL, objectName = "SmallText")
            ULLabel.setProperty("Color","Dark")
            ULLabel.setProperty("Border","None")
            ULLabel.setGeometry(0,0,215,35)
            ULLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value+1, "Upgrade", NPCID, OtherID)
            if "UpgradeForceAvailable" in Flags and Flags["UpgradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                ULLabel.setProperty("Selected",1)

            ULLabel.setText(f'''Submission {Value+1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(ULLabel)
            ULLabel.setGeometry(5,1,210,FontHeight)
            ULBackLabel.setGeometry(0,0,250,FontHeight+2)

            def ULClick():
                if ULButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, 1)
                    except Exception as e:
                        print(e)
            ULButton = QLabel(UL)
            ULButton.setGeometry(215,1,33,33)
            ULButton.mouseReleaseEvent = lambda event: ULClick()
            ULButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "UpArrow.png" ) ))
            ULButton.setProperty("Color","None")
            ULButton.setScaledContents(True)
            ULButton.Available = Available
            UL.setMinimumHeight(ULBackLabel.height())
            UL.setMaximumHeight(ULBackLabel.height())

            Layout.addWidget(UL)
            Height += UL.height()

        CL = QWidget()

        CLLabel = QLabel(CL, objectName = "SmallText")
        CLLabel.setProperty("Color","Dark")
        CLLabel.setGeometry(0,0,250,35)

        Text = "Current Level"
        CLLabel.setText(f'''Submission {Value}: {Text}''')

        CL.setMinimumHeight(35)
        CL.setMaximumHeight(35)

        Layout.addWidget(CL)
        Height += CL.height()

        if Value > 0:
            DL = QWidget()

            DLBackLabel = QLabel(DL)
            DLBackLabel.setProperty("Color","Dark")
            DLLabel = QLabel(DL, objectName = "SmallText")
            DLLabel.setProperty("Color","Dark")
            DLLabel.setProperty("Border","None")
            DLLabel.setGeometry(0,0,215,35)
            DLLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value-1, "Downgrade", NPCID, OtherID)
            if "DowngradeForceAvailable" in Flags and Flags["DowngradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                DLLabel.setProperty("Selected",1)

            DLLabel.setText(f'''Submission {Value-1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(DLLabel)
            DLLabel.setGeometry(5,1,210,FontHeight)
            DLBackLabel.setGeometry(0,0,250,FontHeight+2)

            def DLClick():
                if DLButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, -1)
                    except Exception as e:
                        print(e)
            DLButton = QLabel(DL)
            DLButton.setGeometry(215,1,33,33)
            DLButton.mouseReleaseEvent = lambda event: DLClick()
            DLButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "DownArrow.png" ) ))
            DLButton.setProperty("Color","None")
            DLButton.setScaledContents(True)
            DLButton.Available = Available
            DL.setMinimumHeight(DLBackLabel.height())
            DL.setMaximumHeight(DLBackLabel.height())

            Layout.addWidget(DL)
            Height += DL.height()

        Holder.setMinimumHeight(Height)
        Holder.setMaximumHeight(Height)

        Widget.setMinimumHeight(Height+45)
        Widget.setMaximumHeight(Height+45)

        Widget.setMinimumWidth(250)
        Widget.setMaximumWidth(250)

        return Widget
    elif AbilityID == "Superiority":
        Widget = QWidget(objectName = "Transparent")

        TitleLabel = QLabel("Superiority", Widget, objectName = "SubTitle")
        TitleLabel.setProperty("Color","Light")
        TitleLabel.setGeometry(0,0,250,40)
        TitleLabel.setMinimumHeight(40)
        TitleLabel.setMaximumHeight(40)

        Holder = QWidget(Widget)
        Holder.setGeometry(0,45,250,0)

        Layout = QVBoxLayout()
        Layout.setSpacing(0)
        Layout.setContentsMargins(0, 0, 0, 0)
        Widget.setContentsMargins(0, 0, 0, 0)
        Holder.setLayout(Layout)

        Height = 0

        if Value < 10:
            UL = QWidget()

            ULBackLabel = QLabel(UL)
            ULBackLabel.setProperty("Color","Dark")
            ULLabel = QLabel(UL, objectName = "SmallText")
            ULLabel.setProperty("Color","Dark")
            ULLabel.setProperty("Border","None")
            ULLabel.setGeometry(0,0,215,35)
            ULLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value+1, "Upgrade", NPCID, OtherID)
            if "UpgradeForceAvailable" in Flags and Flags["UpgradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                ULLabel.setProperty("Selected",1)

            ULLabel.setText(f'''Superiority {Value+1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(ULLabel)
            ULLabel.setGeometry(5,1,210,FontHeight)
            ULBackLabel.setGeometry(0,0,250,FontHeight+2)

            def ULClick():
                if ULButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, 1)
                    except Exception as e:
                        print(e)
            ULButton = QLabel(UL)
            ULButton.setGeometry(215,1,33,33)
            ULButton.mouseReleaseEvent = lambda event: ULClick()
            ULButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "UpArrow.png" ) ))
            ULButton.setProperty("Color","None")
            ULButton.setScaledContents(True)
            ULButton.Available = Available
            UL.setMinimumHeight(ULBackLabel.height())
            UL.setMaximumHeight(ULBackLabel.height())

            Layout.addWidget(UL)
            Height += UL.height()

        CL = QWidget()

        CLLabel = QLabel(CL, objectName = "SmallText")
        CLLabel.setProperty("Color","Dark")
        CLLabel.setGeometry(0,0,250,35)

        Text = "Current Level"
        CLLabel.setText(f'''Superiority {Value}: {Text}''')

        CL.setMinimumHeight(35)
        CL.setMaximumHeight(35)

        Layout.addWidget(CL)
        Height += CL.height()

        if Value > 0:
            DL = QWidget()

            DLBackLabel = QLabel(DL)
            DLBackLabel.setProperty("Color","Dark")
            DLLabel = QLabel(DL, objectName = "SmallText")
            DLLabel.setProperty("Color","Dark")
            DLLabel.setProperty("Border","None")
            DLLabel.setGeometry(0,0,215,35)
            DLLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value-1, "Downgrade", NPCID, OtherID)
            if "DowngradeForceAvailable" in Flags and Flags["DowngradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                DLLabel.setProperty("Selected",1)

            DLLabel.setText(f'''Superiority {Value-1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(DLLabel)
            DLLabel.setGeometry(5,1,210,FontHeight)
            DLBackLabel.setGeometry(0,0,250,FontHeight+2)

            def DLClick():
                if DLButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, -1)
                    except Exception as e:
                        print(e)
            DLButton = QLabel(DL)
            DLButton.setGeometry(215,1,33,33)
            DLButton.mouseReleaseEvent = lambda event: DLClick()
            DLButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "DownArrow.png" ) ))
            DLButton.setProperty("Color","None")
            DLButton.setScaledContents(True)
            DLButton.Available = Available
            DL.setMinimumHeight(DLBackLabel.height())
            DL.setMaximumHeight(DLBackLabel.height())

            Layout.addWidget(DL)
            Height += DL.height()

        Holder.setMinimumHeight(Height)
        Holder.setMaximumHeight(Height)

        Widget.setMinimumHeight(Height+45)
        Widget.setMaximumHeight(Height+45)

        Widget.setMinimumWidth(250)
        Widget.setMaximumWidth(250)

        return Widget
    elif AbilityID == "CSense":
        Widget = QWidget(objectName = "Transparent")

        TitleLabel = QLabel("CSense", Widget, objectName = "SubTitle")
        TitleLabel.setProperty("Color","Light")
        TitleLabel.setGeometry(0,0,250,40)
        TitleLabel.setMinimumHeight(40)
        TitleLabel.setMaximumHeight(40)

        Holder = QWidget(Widget)
        Holder.setGeometry(0,45,250,0)

        Layout = QVBoxLayout()
        Layout.setSpacing(0)
        Layout.setContentsMargins(0, 0, 0, 0)
        Widget.setContentsMargins(0, 0, 0, 0)
        Holder.setLayout(Layout)

        Height = 0

        if Value < 10:
            UL = QWidget()

            ULBackLabel = QLabel(UL)
            ULBackLabel.setProperty("Color","Dark")
            ULLabel = QLabel(UL, objectName = "SmallText")
            ULLabel.setProperty("Color","Dark")
            ULLabel.setProperty("Border","None")
            ULLabel.setGeometry(0,0,215,35)
            ULLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value+1, "Upgrade", NPCID, OtherID)
            if "UpgradeForceAvailable" in Flags and Flags["UpgradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                ULLabel.setProperty("Selected",1)

            ULLabel.setText(f'''CSense {Value+1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(ULLabel)
            ULLabel.setGeometry(5,1,210,FontHeight)
            ULBackLabel.setGeometry(0,0,250,FontHeight+2)

            def ULClick():
                if ULButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, 1)
                    except Exception as e:
                        print(e)
            ULButton = QLabel(UL)
            ULButton.setGeometry(215,1,33,33)
            ULButton.mouseReleaseEvent = lambda event: ULClick()
            ULButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "UpArrow.png" ) ))
            ULButton.setProperty("Color","None")
            ULButton.setScaledContents(True)
            ULButton.Available = Available
            UL.setMinimumHeight(ULBackLabel.height())
            UL.setMaximumHeight(ULBackLabel.height())

            Layout.addWidget(UL)
            Height += UL.height()

        CL = QWidget()

        CLLabel = QLabel(CL, objectName = "SmallText")
        CLLabel.setProperty("Color","Dark")
        CLLabel.setGeometry(0,0,250,35)

        Text = "Current Level"
        CLLabel.setText(f'''CSense {Value}: {Text}''')

        CL.setMinimumHeight(35)
        CL.setMaximumHeight(35)

        Layout.addWidget(CL)
        Height += CL.height()

        if Value > 0:
            DL = QWidget()

            DLBackLabel = QLabel(DL)
            DLBackLabel.setProperty("Color","Dark")
            DLLabel = QLabel(DL, objectName = "SmallText")
            DLLabel.setProperty("Color","Dark")
            DLLabel.setProperty("Border","None")
            DLLabel.setGeometry(0,0,215,35)
            DLLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value-1, "Downgrade", NPCID, OtherID)
            if "DowngradeForceAvailable" in Flags and Flags["DowngradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                DLLabel.setProperty("Selected",1)

            DLLabel.setText(f'''CSense {Value-1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(DLLabel)
            DLLabel.setGeometry(5,1,210,FontHeight)
            DLBackLabel.setGeometry(0,0,250,FontHeight+2)

            def DLClick():
                if DLButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, -1)
                    except Exception as e:
                        print(e)
            DLButton = QLabel(DL)
            DLButton.setGeometry(215,1,33,33)
            DLButton.mouseReleaseEvent = lambda event: DLClick()
            DLButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "DownArrow.png" ) ))
            DLButton.setProperty("Color","None")
            DLButton.setScaledContents(True)
            DLButton.Available = Available
            DL.setMinimumHeight(DLBackLabel.height())
            DL.setMaximumHeight(DLBackLabel.height())

            Layout.addWidget(DL)
            Height += DL.height()

        Holder.setMinimumHeight(Height)
        Holder.setMaximumHeight(Height)

        Widget.setMinimumHeight(Height+45)
        Widget.setMaximumHeight(Height+45)

        Widget.setMinimumWidth(250)
        Widget.setMaximumWidth(250)

        return Widget
    elif AbilityID == "VSense":
        Widget = QWidget(objectName = "Transparent")

        TitleLabel = QLabel("VSense", Widget, objectName = "SubTitle")
        TitleLabel.setProperty("Color","Light")
        TitleLabel.setGeometry(0,0,250,40)
        TitleLabel.setMinimumHeight(40)
        TitleLabel.setMaximumHeight(40)

        Holder = QWidget(Widget)
        Holder.setGeometry(0,45,250,0)

        Layout = QVBoxLayout()
        Layout.setSpacing(0)
        Layout.setContentsMargins(0, 0, 0, 0)
        Widget.setContentsMargins(0, 0, 0, 0)
        Holder.setLayout(Layout)

        Height = 0

        if Value < 10:
            UL = QWidget()

            ULBackLabel = QLabel(UL)
            ULBackLabel.setProperty("Color","Dark")
            ULLabel = QLabel(UL, objectName = "SmallText")
            ULLabel.setProperty("Color","Dark")
            ULLabel.setProperty("Border","None")
            ULLabel.setGeometry(0,0,215,35)
            ULLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value+1, "Upgrade", NPCID, OtherID)
            if "UpgradeForceAvailable" in Flags and Flags["UpgradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                ULLabel.setProperty("Selected",1)

            ULLabel.setText(f'''VSense {Value+1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(ULLabel)
            ULLabel.setGeometry(5,1,210,FontHeight)
            ULBackLabel.setGeometry(0,0,250,FontHeight+2)

            def ULClick():
                if ULButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, 1)
                    except Exception as e:
                        print(e)
            ULButton = QLabel(UL)
            ULButton.setGeometry(215,1,33,33)
            ULButton.mouseReleaseEvent = lambda event: ULClick()
            ULButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "UpArrow.png" ) ))
            ULButton.setProperty("Color","None")
            ULButton.setScaledContents(True)
            ULButton.Available = Available
            UL.setMinimumHeight(ULBackLabel.height())
            UL.setMaximumHeight(ULBackLabel.height())

            Layout.addWidget(UL)
            Height += UL.height()

        CL = QWidget()

        CLLabel = QLabel(CL, objectName = "SmallText")
        CLLabel.setProperty("Color","Dark")
        CLLabel.setGeometry(0,0,250,35)

        Text = "Current Level"
        CLLabel.setText(f'''VSense {Value}: {Text}''')

        CL.setMinimumHeight(35)
        CL.setMaximumHeight(35)

        Layout.addWidget(CL)
        Height += CL.height()

        if Value > 0:
            DL = QWidget()

            DLBackLabel = QLabel(DL)
            DLBackLabel.setProperty("Color","Dark")
            DLLabel = QLabel(DL, objectName = "SmallText")
            DLLabel.setProperty("Color","Dark")
            DLLabel.setProperty("Border","None")
            DLLabel.setGeometry(0,0,215,35)
            DLLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value-1, "Downgrade", NPCID, OtherID)
            if "DowngradeForceAvailable" in Flags and Flags["DowngradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                DLLabel.setProperty("Selected",1)

            DLLabel.setText(f'''VSense {Value-1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(DLLabel)
            DLLabel.setGeometry(5,1,210,FontHeight)
            DLBackLabel.setGeometry(0,0,250,FontHeight+2)

            def DLClick():
                if DLButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, -1)
                    except Exception as e:
                        print(e)
            DLButton = QLabel(DL)
            DLButton.setGeometry(215,1,33,33)
            DLButton.mouseReleaseEvent = lambda event: DLClick()
            DLButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "DownArrow.png" ) ))
            DLButton.setProperty("Color","None")
            DLButton.setScaledContents(True)
            DLButton.Available = Available
            DL.setMinimumHeight(DLBackLabel.height())
            DL.setMaximumHeight(DLBackLabel.height())

            Layout.addWidget(DL)
            Height += DL.height()

        Holder.setMinimumHeight(Height)
        Holder.setMaximumHeight(Height)

        Widget.setMinimumHeight(Height+45)
        Widget.setMaximumHeight(Height+45)

        Widget.setMinimumWidth(250)
        Widget.setMaximumWidth(250)

        return Widget
    elif AbilityID == "ASense":
        Widget = QWidget(objectName = "Transparent")

        TitleLabel = QLabel("ASense", Widget, objectName = "SubTitle")
        TitleLabel.setProperty("Color","Light")
        TitleLabel.setGeometry(0,0,250,40)
        TitleLabel.setMinimumHeight(40)
        TitleLabel.setMaximumHeight(40)

        Holder = QWidget(Widget)
        Holder.setGeometry(0,45,250,0)

        Layout = QVBoxLayout()
        Layout.setSpacing(0)
        Layout.setContentsMargins(0, 0, 0, 0)
        Widget.setContentsMargins(0, 0, 0, 0)
        Holder.setLayout(Layout)

        Height = 0

        if Value < 10:
            UL = QWidget()

            ULBackLabel = QLabel(UL)
            ULBackLabel.setProperty("Color","Dark")
            ULLabel = QLabel(UL, objectName = "SmallText")
            ULLabel.setProperty("Color","Dark")
            ULLabel.setProperty("Border","None")
            ULLabel.setGeometry(0,0,215,35)
            ULLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value+1, "Upgrade", NPCID, OtherID)
            if "UpgradeForceAvailable" in Flags and Flags["UpgradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                ULLabel.setProperty("Selected",1)

            ULLabel.setText(f'''ASense {Value+1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(ULLabel)
            ULLabel.setGeometry(5,1,210,FontHeight)
            ULBackLabel.setGeometry(0,0,250,FontHeight+2)

            def ULClick():
                if ULButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, 1)
                    except Exception as e:
                        print(e)
            ULButton = QLabel(UL)
            ULButton.setGeometry(215,1,33,33)
            ULButton.mouseReleaseEvent = lambda event: ULClick()
            ULButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "UpArrow.png" ) ))
            ULButton.setProperty("Color","None")
            ULButton.setScaledContents(True)
            ULButton.Available = Available
            UL.setMinimumHeight(ULBackLabel.height())
            UL.setMaximumHeight(ULBackLabel.height())

            Layout.addWidget(UL)
            Height += UL.height()

        CL = QWidget()

        CLLabel = QLabel(CL, objectName = "SmallText")
        CLLabel.setProperty("Color","Dark")
        CLLabel.setGeometry(0,0,250,35)

        Text = "Current Level"
        CLLabel.setText(f'''ASense {Value}: {Text}''')

        CL.setMinimumHeight(35)
        CL.setMaximumHeight(35)

        Layout.addWidget(CL)
        Height += CL.height()

        if Value > 0:
            DL = QWidget()

            DLBackLabel = QLabel(DL)
            DLBackLabel.setProperty("Color","Dark")
            DLLabel = QLabel(DL, objectName = "SmallText")
            DLLabel.setProperty("Color","Dark")
            DLLabel.setProperty("Border","None")
            DLLabel.setGeometry(0,0,215,35)
            DLLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value-1, "Downgrade", NPCID, OtherID)
            if "DowngradeForceAvailable" in Flags and Flags["DowngradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                DLLabel.setProperty("Selected",1)

            DLLabel.setText(f'''ASense {Value-1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(DLLabel)
            DLLabel.setGeometry(5,1,210,FontHeight)
            DLBackLabel.setGeometry(0,0,250,FontHeight+2)

            def DLClick():
                if DLButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, -1)
                    except Exception as e:
                        print(e)
            DLButton = QLabel(DL)
            DLButton.setGeometry(215,1,33,33)
            DLButton.mouseReleaseEvent = lambda event: DLClick()
            DLButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "DownArrow.png" ) ))
            DLButton.setProperty("Color","None")
            DLButton.setScaledContents(True)
            DLButton.Available = Available
            DL.setMinimumHeight(DLBackLabel.height())
            DL.setMaximumHeight(DLBackLabel.height())

            Layout.addWidget(DL)
            Height += DL.height()

        Holder.setMinimumHeight(Height)
        Holder.setMaximumHeight(Height)

        Widget.setMinimumHeight(Height+45)
        Widget.setMaximumHeight(Height+45)

        Widget.setMinimumWidth(250)
        Widget.setMaximumWidth(250)

        return Widget
    elif AbilityID == "PSense":
        Widget = QWidget(objectName = "Transparent")

        TitleLabel = QLabel("PSense", Widget, objectName = "SubTitle")
        TitleLabel.setProperty("Color","Light")
        TitleLabel.setGeometry(0,0,250,40)
        TitleLabel.setMinimumHeight(40)
        TitleLabel.setMaximumHeight(40)

        Holder = QWidget(Widget)
        Holder.setGeometry(0,45,250,0)

        Layout = QVBoxLayout()
        Layout.setSpacing(0)
        Layout.setContentsMargins(0, 0, 0, 0)
        Widget.setContentsMargins(0, 0, 0, 0)
        Holder.setLayout(Layout)

        Height = 0

        if Value < 10:
            UL = QWidget()

            ULBackLabel = QLabel(UL)
            ULBackLabel.setProperty("Color","Dark")
            ULLabel = QLabel(UL, objectName = "SmallText")
            ULLabel.setProperty("Color","Dark")
            ULLabel.setProperty("Border","None")
            ULLabel.setGeometry(0,0,215,35)
            ULLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value+1, "Upgrade", NPCID, OtherID)
            if "UpgradeForceAvailable" in Flags and Flags["UpgradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                ULLabel.setProperty("Selected",1)

            ULLabel.setText(f'''PSense {Value+1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(ULLabel)
            ULLabel.setGeometry(5,1,210,FontHeight)
            ULBackLabel.setGeometry(0,0,250,FontHeight+2)

            def ULClick():
                if ULButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, 1)
                    except Exception as e:
                        print(e)
            ULButton = QLabel(UL)
            ULButton.setGeometry(215,1,33,33)
            ULButton.mouseReleaseEvent = lambda event: ULClick()
            ULButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "UpArrow.png" ) ))
            ULButton.setProperty("Color","None")
            ULButton.setScaledContents(True)
            ULButton.Available = Available
            UL.setMinimumHeight(ULBackLabel.height())
            UL.setMaximumHeight(ULBackLabel.height())

            Layout.addWidget(UL)
            Height += UL.height()

        CL = QWidget()

        CLLabel = QLabel(CL, objectName = "SmallText")
        CLLabel.setProperty("Color","Dark")
        CLLabel.setGeometry(0,0,250,35)

        Text = "Current Level"
        CLLabel.setText(f'''PSense {Value}: {Text}''')

        CL.setMinimumHeight(35)
        CL.setMaximumHeight(35)

        Layout.addWidget(CL)
        Height += CL.height()

        if Value > 0:
            DL = QWidget()

            DLBackLabel = QLabel(DL)
            DLBackLabel.setProperty("Color","Dark")
            DLLabel = QLabel(DL, objectName = "SmallText")
            DLLabel.setProperty("Color","Dark")
            DLLabel.setProperty("Border","None")
            DLLabel.setGeometry(0,0,215,35)
            DLLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value-1, "Downgrade", NPCID, OtherID)
            if "DowngradeForceAvailable" in Flags and Flags["DowngradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                DLLabel.setProperty("Selected",1)

            DLLabel.setText(f'''PSense {Value-1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(DLLabel)
            DLLabel.setGeometry(5,1,210,FontHeight)
            DLBackLabel.setGeometry(0,0,250,FontHeight+2)

            def DLClick():
                if DLButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, -1)
                    except Exception as e:
                        print(e)
            DLButton = QLabel(DL)
            DLButton.setGeometry(215,1,33,33)
            DLButton.mouseReleaseEvent = lambda event: DLClick()
            DLButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "DownArrow.png" ) ))
            DLButton.setProperty("Color","None")
            DLButton.setScaledContents(True)
            DLButton.Available = Available
            DL.setMinimumHeight(DLBackLabel.height())
            DL.setMaximumHeight(DLBackLabel.height())

            Layout.addWidget(DL)
            Height += DL.height()

        Holder.setMinimumHeight(Height)
        Holder.setMaximumHeight(Height)

        Widget.setMinimumHeight(Height+45)
        Widget.setMaximumHeight(Height+45)

        Widget.setMinimumWidth(250)
        Widget.setMaximumWidth(250)

        return Widget
    elif AbilityID == "MSense":
        Widget = QWidget(objectName = "Transparent")

        TitleLabel = QLabel("MSense", Widget, objectName = "SubTitle")
        TitleLabel.setProperty("Color","Light")
        TitleLabel.setGeometry(0,0,250,40)
        TitleLabel.setMinimumHeight(40)
        TitleLabel.setMaximumHeight(40)

        Holder = QWidget(Widget)
        Holder.setGeometry(0,45,250,0)

        Layout = QVBoxLayout()
        Layout.setSpacing(0)
        Layout.setContentsMargins(0, 0, 0, 0)
        Widget.setContentsMargins(0, 0, 0, 0)
        Holder.setLayout(Layout)

        Height = 0

        if Value < 10:
            UL = QWidget()

            ULBackLabel = QLabel(UL)
            ULBackLabel.setProperty("Color","Dark")
            ULLabel = QLabel(UL, objectName = "SmallText")
            ULLabel.setProperty("Color","Dark")
            ULLabel.setProperty("Border","None")
            ULLabel.setGeometry(0,0,215,35)
            ULLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value+1, "Upgrade", NPCID, OtherID)
            if "UpgradeForceAvailable" in Flags and Flags["UpgradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                ULLabel.setProperty("Selected",1)

            ULLabel.setText(f'''MSense {Value+1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(ULLabel)
            ULLabel.setGeometry(5,1,210,FontHeight)
            ULBackLabel.setGeometry(0,0,250,FontHeight+2)

            def ULClick():
                if ULButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, 1)
                    except Exception as e:
                        print(e)
            ULButton = QLabel(UL)
            ULButton.setGeometry(215,1,33,33)
            ULButton.mouseReleaseEvent = lambda event: ULClick()
            ULButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "UpArrow.png" ) ))
            ULButton.setProperty("Color","None")
            ULButton.setScaledContents(True)
            ULButton.Available = Available
            UL.setMinimumHeight(ULBackLabel.height())
            UL.setMaximumHeight(ULBackLabel.height())

            Layout.addWidget(UL)
            Height += UL.height()

        CL = QWidget()

        CLLabel = QLabel(CL, objectName = "SmallText")
        CLLabel.setProperty("Color","Dark")
        CLLabel.setGeometry(0,0,250,35)

        Text = "Current Level"
        CLLabel.setText(f'''MSense {Value}: {Text}''')

        CL.setMinimumHeight(35)
        CL.setMaximumHeight(35)

        Layout.addWidget(CL)
        Height += CL.height()

        if Value > 0:
            DL = QWidget()

            DLBackLabel = QLabel(DL)
            DLBackLabel.setProperty("Color","Dark")
            DLLabel = QLabel(DL, objectName = "SmallText")
            DLLabel.setProperty("Color","Dark")
            DLLabel.setProperty("Border","None")
            DLLabel.setGeometry(0,0,215,35)
            DLLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value-1, "Downgrade", NPCID, OtherID)
            if "DowngradeForceAvailable" in Flags and Flags["DowngradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                DLLabel.setProperty("Selected",1)

            DLLabel.setText(f'''MSense {Value-1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(DLLabel)
            DLLabel.setGeometry(5,1,210,FontHeight)
            DLBackLabel.setGeometry(0,0,250,FontHeight+2)

            def DLClick():
                if DLButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, -1)
                    except Exception as e:
                        print(e)
            DLButton = QLabel(DL)
            DLButton.setGeometry(215,1,33,33)
            DLButton.mouseReleaseEvent = lambda event: DLClick()
            DLButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "DownArrow.png" ) ))
            DLButton.setProperty("Color","None")
            DLButton.setScaledContents(True)
            DLButton.Available = Available
            DL.setMinimumHeight(DLBackLabel.height())
            DL.setMaximumHeight(DLBackLabel.height())

            Layout.addWidget(DL)
            Height += DL.height()

        Holder.setMinimumHeight(Height)
        Holder.setMaximumHeight(Height)

        Widget.setMinimumHeight(Height+45)
        Widget.setMaximumHeight(Height+45)

        Widget.setMinimumWidth(250)
        Widget.setMaximumWidth(250)

        return Widget
    elif AbilityID == "Service":
        Widget = QWidget(objectName = "Transparent")

        TitleLabel = QLabel("Service", Widget, objectName = "SubTitle")
        TitleLabel.setProperty("Color","Light")
        TitleLabel.setGeometry(0,0,250,40)
        TitleLabel.setMinimumHeight(40)
        TitleLabel.setMaximumHeight(40)

        Holder = QWidget(Widget)
        Holder.setGeometry(0,45,250,0)

        Layout = QVBoxLayout()
        Layout.setSpacing(0)
        Layout.setContentsMargins(0, 0, 0, 0)
        Widget.setContentsMargins(0, 0, 0, 0)
        Holder.setLayout(Layout)

        Height = 0

        if Value < 10:
            UL = QWidget()

            ULBackLabel = QLabel(UL)
            ULBackLabel.setProperty("Color","Dark")
            ULLabel = QLabel(UL, objectName = "SmallText")
            ULLabel.setProperty("Color","Dark")
            ULLabel.setProperty("Border","None")
            ULLabel.setGeometry(0,0,215,35)
            ULLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value+1, "Upgrade", NPCID, OtherID)
            if "UpgradeForceAvailable" in Flags and Flags["UpgradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                ULLabel.setProperty("Selected",1)

            ULLabel.setText(f'''Service {Value+1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(ULLabel)
            ULLabel.setGeometry(5,1,210,FontHeight)
            ULBackLabel.setGeometry(0,0,250,FontHeight+2)

            def ULClick():
                if ULButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, 1)
                    except Exception as e:
                        print(e)
            ULButton = QLabel(UL)
            ULButton.setGeometry(215,1,33,33)
            ULButton.mouseReleaseEvent = lambda event: ULClick()
            ULButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "UpArrow.png" ) ))
            ULButton.setProperty("Color","None")
            ULButton.setScaledContents(True)
            ULButton.Available = Available
            UL.setMinimumHeight(ULBackLabel.height())
            UL.setMaximumHeight(ULBackLabel.height())

            Layout.addWidget(UL)
            Height += UL.height()

        CL = QWidget()

        CLLabel = QLabel(CL, objectName = "SmallText")
        CLLabel.setProperty("Color","Dark")
        CLLabel.setGeometry(0,0,250,35)

        Text = "Current Level"
        CLLabel.setText(f'''Service {Value}: {Text}''')

        CL.setMinimumHeight(35)
        CL.setMaximumHeight(35)

        Layout.addWidget(CL)
        Height += CL.height()

        if Value > 0:
            DL = QWidget()

            DLBackLabel = QLabel(DL)
            DLBackLabel.setProperty("Color","Dark")
            DLLabel = QLabel(DL, objectName = "SmallText")
            DLLabel.setProperty("Color","Dark")
            DLLabel.setProperty("Border","None")
            DLLabel.setGeometry(0,0,215,35)
            DLLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value-1, "Downgrade", NPCID, OtherID)
            if "DowngradeForceAvailable" in Flags and Flags["DowngradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                DLLabel.setProperty("Selected",1)

            DLLabel.setText(f'''Service {Value-1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(DLLabel)
            DLLabel.setGeometry(5,1,210,FontHeight)
            DLBackLabel.setGeometry(0,0,250,FontHeight+2)

            def DLClick():
                if DLButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, -1)
                    except Exception as e:
                        print(e)
            DLButton = QLabel(DL)
            DLButton.setGeometry(215,1,33,33)
            DLButton.mouseReleaseEvent = lambda event: DLClick()
            DLButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "DownArrow.png" ) ))
            DLButton.setProperty("Color","None")
            DLButton.setScaledContents(True)
            DLButton.Available = Available
            DL.setMinimumHeight(DLBackLabel.height())
            DL.setMaximumHeight(DLBackLabel.height())

            Layout.addWidget(DL)
            Height += DL.height()

        Holder.setMinimumHeight(Height)
        Holder.setMaximumHeight(Height)

        Widget.setMinimumHeight(Height+45)
        Widget.setMaximumHeight(Height+45)

        Widget.setMinimumWidth(250)
        Widget.setMaximumWidth(250)

        return Widget
    elif AbilityID == "Sadism":
        Widget = QWidget(objectName = "Transparent")

        TitleLabel = QLabel("Sadism", Widget, objectName = "SubTitle")
        TitleLabel.setProperty("Color","Light")
        TitleLabel.setGeometry(0,0,250,40)
        TitleLabel.setMinimumHeight(40)
        TitleLabel.setMaximumHeight(40)

        Holder = QWidget(Widget)
        Holder.setGeometry(0,45,250,0)

        Layout = QVBoxLayout()
        Layout.setSpacing(0)
        Layout.setContentsMargins(0, 0, 0, 0)
        Widget.setContentsMargins(0, 0, 0, 0)
        Holder.setLayout(Layout)

        Height = 0

        if Value < 10:
            UL = QWidget()

            ULBackLabel = QLabel(UL)
            ULBackLabel.setProperty("Color","Dark")
            ULLabel = QLabel(UL, objectName = "SmallText")
            ULLabel.setProperty("Color","Dark")
            ULLabel.setProperty("Border","None")
            ULLabel.setGeometry(0,0,215,35)
            ULLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value+1, "Upgrade", NPCID, OtherID)
            if "UpgradeForceAvailable" in Flags and Flags["UpgradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                ULLabel.setProperty("Selected",1)

            ULLabel.setText(f'''Sadism {Value+1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(ULLabel)
            ULLabel.setGeometry(5,1,210,FontHeight)
            ULBackLabel.setGeometry(0,0,250,FontHeight+2)

            def ULClick():
                if ULButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, 1)
                    except Exception as e:
                        print(e)
            ULButton = QLabel(UL)
            ULButton.setGeometry(215,1,33,33)
            ULButton.mouseReleaseEvent = lambda event: ULClick()
            ULButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "UpArrow.png" ) ))
            ULButton.setProperty("Color","None")
            ULButton.setScaledContents(True)
            ULButton.Available = Available
            UL.setMinimumHeight(ULBackLabel.height())
            UL.setMaximumHeight(ULBackLabel.height())

            Layout.addWidget(UL)
            Height += UL.height()

        CL = QWidget()

        CLLabel = QLabel(CL, objectName = "SmallText")
        CLLabel.setProperty("Color","Dark")
        CLLabel.setGeometry(0,0,250,35)

        Text = "Current Level"
        CLLabel.setText(f'''Sadism {Value}: {Text}''')

        CL.setMinimumHeight(35)
        CL.setMaximumHeight(35)

        Layout.addWidget(CL)
        Height += CL.height()

        if Value > 0:
            DL = QWidget()

            DLBackLabel = QLabel(DL)
            DLBackLabel.setProperty("Color","Dark")
            DLLabel = QLabel(DL, objectName = "SmallText")
            DLLabel.setProperty("Color","Dark")
            DLLabel.setProperty("Border","None")
            DLLabel.setGeometry(0,0,215,35)
            DLLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value-1, "Downgrade", NPCID, OtherID)
            if "DowngradeForceAvailable" in Flags and Flags["DowngradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                DLLabel.setProperty("Selected",1)

            DLLabel.setText(f'''Sadism {Value-1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(DLLabel)
            DLLabel.setGeometry(5,1,210,FontHeight)
            DLBackLabel.setGeometry(0,0,250,FontHeight+2)

            def DLClick():
                if DLButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, -1)
                    except Exception as e:
                        print(e)
            DLButton = QLabel(DL)
            DLButton.setGeometry(215,1,33,33)
            DLButton.mouseReleaseEvent = lambda event: DLClick()
            DLButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "DownArrow.png" ) ))
            DLButton.setProperty("Color","None")
            DLButton.setScaledContents(True)
            DLButton.Available = Available
            DL.setMinimumHeight(DLBackLabel.height())
            DL.setMaximumHeight(DLBackLabel.height())

            Layout.addWidget(DL)
            Height += DL.height()

        Holder.setMinimumHeight(Height)
        Holder.setMaximumHeight(Height)

        Widget.setMinimumHeight(Height+45)
        Widget.setMaximumHeight(Height+45)

        Widget.setMinimumWidth(250)
        Widget.setMaximumWidth(250)

        return Widget
    elif AbilityID == "Masochism":
        Widget = QWidget(objectName = "Transparent")

        TitleLabel = QLabel("Masochism", Widget, objectName = "SubTitle")
        TitleLabel.setProperty("Color","Light")
        TitleLabel.setGeometry(0,0,250,40)
        TitleLabel.setMinimumHeight(40)
        TitleLabel.setMaximumHeight(40)

        Holder = QWidget(Widget)
        Holder.setGeometry(0,45,250,0)

        Layout = QVBoxLayout()
        Layout.setSpacing(0)
        Layout.setContentsMargins(0, 0, 0, 0)
        Widget.setContentsMargins(0, 0, 0, 0)
        Holder.setLayout(Layout)

        Height = 0

        if Value < 10:
            UL = QWidget()

            ULBackLabel = QLabel(UL)
            ULBackLabel.setProperty("Color","Dark")
            ULLabel = QLabel(UL, objectName = "SmallText")
            ULLabel.setProperty("Color","Dark")
            ULLabel.setProperty("Border","None")
            ULLabel.setGeometry(0,0,215,35)
            ULLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value+1, "Upgrade", NPCID, OtherID)
            if "UpgradeForceAvailable" in Flags and Flags["UpgradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                ULLabel.setProperty("Selected",1)

            ULLabel.setText(f'''Masochism {Value+1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(ULLabel)
            ULLabel.setGeometry(5,1,210,FontHeight)
            ULBackLabel.setGeometry(0,0,250,FontHeight+2)

            def ULClick():
                if ULButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, 1)
                    except Exception as e:
                        print(e)
            ULButton = QLabel(UL)
            ULButton.setGeometry(215,1,33,33)
            ULButton.mouseReleaseEvent = lambda event: ULClick()
            ULButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "UpArrow.png" ) ))
            ULButton.setProperty("Color","None")
            ULButton.setScaledContents(True)
            ULButton.Available = Available
            UL.setMinimumHeight(ULBackLabel.height())
            UL.setMaximumHeight(ULBackLabel.height())

            Layout.addWidget(UL)
            Height += UL.height()

        CL = QWidget()

        CLLabel = QLabel(CL, objectName = "SmallText")
        CLLabel.setProperty("Color","Dark")
        CLLabel.setGeometry(0,0,250,35)

        Text = "Current Level"
        CLLabel.setText(f'''Masochism {Value}: {Text}''')

        CL.setMinimumHeight(35)
        CL.setMaximumHeight(35)

        Layout.addWidget(CL)
        Height += CL.height()

        if Value > 0:
            DL = QWidget()

            DLBackLabel = QLabel(DL)
            DLBackLabel.setProperty("Color","Dark")
            DLLabel = QLabel(DL, objectName = "SmallText")
            DLLabel.setProperty("Color","Dark")
            DLLabel.setProperty("Border","None")
            DLLabel.setGeometry(0,0,215,35)
            DLLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value-1, "Downgrade", NPCID, OtherID)
            if "DowngradeForceAvailable" in Flags and Flags["DowngradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                DLLabel.setProperty("Selected",1)

            DLLabel.setText(f'''Masochism {Value-1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(DLLabel)
            DLLabel.setGeometry(5,1,210,FontHeight)
            DLBackLabel.setGeometry(0,0,250,FontHeight+2)

            def DLClick():
                if DLButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, -1)
                    except Exception as e:
                        print(e)
            DLButton = QLabel(DL)
            DLButton.setGeometry(215,1,33,33)
            DLButton.mouseReleaseEvent = lambda event: DLClick()
            DLButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "DownArrow.png" ) ))
            DLButton.setProperty("Color","None")
            DLButton.setScaledContents(True)
            DLButton.Available = Available
            DL.setMinimumHeight(DLBackLabel.height())
            DL.setMaximumHeight(DLBackLabel.height())

            Layout.addWidget(DL)
            Height += DL.height()

        Holder.setMinimumHeight(Height)
        Holder.setMaximumHeight(Height)

        Widget.setMinimumHeight(Height+45)
        Widget.setMaximumHeight(Height+45)

        Widget.setMinimumWidth(250)
        Widget.setMaximumWidth(250)

        return Widget
    elif AbilityID == "Exhibitionism":
        Widget = QWidget(objectName = "Transparent")

        TitleLabel = QLabel("Exhibitionism", Widget, objectName = "SubTitle")
        TitleLabel.setProperty("Color","Light")
        TitleLabel.setGeometry(0,0,250,40)
        TitleLabel.setMinimumHeight(40)
        TitleLabel.setMaximumHeight(40)

        Holder = QWidget(Widget)
        Holder.setGeometry(0,45,250,0)

        Layout = QVBoxLayout()
        Layout.setSpacing(0)
        Layout.setContentsMargins(0, 0, 0, 0)
        Widget.setContentsMargins(0, 0, 0, 0)
        Holder.setLayout(Layout)

        Height = 0

        if Value < 10:
            UL = QWidget()

            ULBackLabel = QLabel(UL)
            ULBackLabel.setProperty("Color","Dark")
            ULLabel = QLabel(UL, objectName = "SmallText")
            ULLabel.setProperty("Color","Dark")
            ULLabel.setProperty("Border","None")
            ULLabel.setGeometry(0,0,215,35)
            ULLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value+1, "Upgrade", NPCID, OtherID)
            if "UpgradeForceAvailable" in Flags and Flags["UpgradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                ULLabel.setProperty("Selected",1)

            ULLabel.setText(f'''Exhibitionism {Value+1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(ULLabel)
            ULLabel.setGeometry(5,1,210,FontHeight)
            ULBackLabel.setGeometry(0,0,250,FontHeight+2)

            def ULClick():
                if ULButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, 1)
                    except Exception as e:
                        print(e)
            ULButton = QLabel(UL)
            ULButton.setGeometry(215,1,33,33)
            ULButton.mouseReleaseEvent = lambda event: ULClick()
            ULButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "UpArrow.png" ) ))
            ULButton.setProperty("Color","None")
            ULButton.setScaledContents(True)
            ULButton.Available = Available
            UL.setMinimumHeight(ULBackLabel.height())
            UL.setMaximumHeight(ULBackLabel.height())

            Layout.addWidget(UL)
            Height += UL.height()

        CL = QWidget()

        CLLabel = QLabel(CL, objectName = "SmallText")
        CLLabel.setProperty("Color","Dark")
        CLLabel.setGeometry(0,0,250,35)

        Text = "Current Level"
        CLLabel.setText(f'''Exhibitionism {Value}: {Text}''')

        CL.setMinimumHeight(35)
        CL.setMaximumHeight(35)

        Layout.addWidget(CL)
        Height += CL.height()

        if Value > 0:
            DL = QWidget()

            DLBackLabel = QLabel(DL)
            DLBackLabel.setProperty("Color","Dark")
            DLLabel = QLabel(DL, objectName = "SmallText")
            DLLabel.setProperty("Color","Dark")
            DLLabel.setProperty("Border","None")
            DLLabel.setGeometry(0,0,215,35)
            DLLabel.setWordWrap(True)

            Text, Available = GetAbilityConditions(AbilityID, Value-1, "Downgrade", NPCID, OtherID)
            if "DowngradeForceAvailable" in Flags and Flags["DowngradeForceAvailable"] == 1:
                Available = 1
            if Available == 1:
                DLLabel.setProperty("Selected",1)

            DLLabel.setText(f'''Exhibitionism {Value-1}: {Text}''')

            FontHeight = Globals.References["SoLFunctions"].AdjustSize(DLLabel)
            DLLabel.setGeometry(5,1,210,FontHeight)
            DLBackLabel.setGeometry(0,0,250,FontHeight+2)

            def DLClick():
                if DLButton.Available == 1:
                    try:
                        AbilityChange(AbilityID, NPCID, OtherID, -1)
                    except Exception as e:
                        print(e)
            DLButton = QLabel(DL)
            DLButton.setGeometry(215,1,33,33)
            DLButton.mouseReleaseEvent = lambda event: DLClick()
            DLButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "DownArrow.png" ) ))
            DLButton.setProperty("Color","None")
            DLButton.setScaledContents(True)
            DLButton.Available = Available
            DL.setMinimumHeight(DLBackLabel.height())
            DL.setMaximumHeight(DLBackLabel.height())

            Layout.addWidget(DL)
            Height += DL.height()

        Holder.setMinimumHeight(Height)
        Holder.setMaximumHeight(Height)

        Widget.setMinimumHeight(Height+45)
        Widget.setMaximumHeight(Height+45)

        Widget.setMinimumWidth(250)
        Widget.setMaximumWidth(250)

        return Widget



    ""



def GetValuesText(self, ValueID, Actor, Target):
    Data = Globals.SoLNPCData[Target]["Relations"][Actor]["Temporal"][ValueID]
    Text = f'''{ValueID}: {Data["Amount"]}'''
    return Text

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
    try:
        Amount = Value["Amount"]
    except:
        Amount = 0

    ValueLabel = QLabel()
    ValueLabel.setText(f'''{TemporalID}: {Amount}''')
    ValueLabel.setProperty("Color","None")
    ValueLabel.setGeometry(0, 40, 150, 35)
    ValueLabel.setMaximumWidth(150)
    ValueLabel.setMinimumWidth(150)
    ValueLabel.setMaximumHeight(35)
    ValueLabel.setMinimumHeight(35)

    return ValueLabel

def GetGValueStaticWidget(GemsID, Value):
    try:
        Amount = Value["Amount"]
    except:
        Amount = 0
    ValueLabel = QLabel()
    ValueLabel.setText(f'''{GemsID}: {Amount}''')
    ValueLabel.setProperty("Color","None")
    ValueLabel.setGeometry(0, 40, 150, 35)
    ValueLabel.setMaximumWidth(150)
    ValueLabel.setMinimumWidth(150)
    ValueLabel.setMaximumHeight(35)
    ValueLabel.setMinimumHeight(35)

    return ValueLabel
