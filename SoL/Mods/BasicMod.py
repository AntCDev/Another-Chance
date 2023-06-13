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


def Initialize(self, Reference):
    Globals.References["BasicMod"] = Reference

    # List = ["Back to Menu", "Move", "Quick Save"]
    # for ControlID in List:
    #     Globals.ControlCommands[ControlID] = {"ID":ControlID, "Reference":Reference, "OtherData":{}}
    #
    # if "SoLNPCData" in Globals.CurrentSession:
    #     Globals.SoLNPCData = Globals.CurrentSession["SoLNPCData"]
    # else:
    #     Globals.SoLNPCData = {}
    #
    # if "SoLPCData" in Globals.CurrentSession:
    #     Globals.SoLPCData = Globals.CurrentSession["SoLPCData"]
    # else:
    #     Globals.SoLPCData = {
    #         "ID":"",
    #         "Targeting":None,
    #         "Flags":{},
    #         "Abilities":{},
    #         "OtherData":{},
    #         }
    #     for ID in Globals.SoLNPCData:
    #         Globals.SoLPCData["ID"] = ID
    #         break
    #
    # if "SoLTempData" in Globals.CurrentSession:
    #     Globals.SoLTempData = Globals.CurrentSession["SoLTempData"]
    #     if "TempNPC" not in Globals.SoLTempData: Globals.SoLTempData["TempNPC"] = []
    #     if "FavoriteNPC" not in Globals.SoLTempData: Globals.SoLTempData["FavoriteNPC"] = []
    # else:
    #     Globals.SoLTempData = {
    #         "TempNPC":[],
    #         "FavoriteNPC":[],
    #         }
    #
    # if True:
    #     Globals.SoLOtherData = {
    #     "baseRelationship":{
    #         "Temporal": {},
    #         "Permanent": {
    #             "Attraction": 0,
    #             "Reliability": 0,
    #             },
    #         "Gems": {},
    #         "Flags": {
    #             "HasConsent": 0
    #             },
    #         "Abilities": {},
    #         "Preferences": {},
    #         "FallenData": {},
    #         },
    #     "IdlingTask":{
    #         "HourStart": 0,
    #         "HourFinish": 1,
    #         "Task": ["Idling", {"BriefFluff": "Idling in the streets of ", "LongFluff": ""} ],
    #         "InterruptionPenalty": 0,
    #         "Location": "ResidentialArea",
    #         },
    #     "SleepTask":{
    #         "HourStart": 0,
    #         "HourFinish": 0,
    #         "Task": ["Sleeping", {"BriefFluff": "Sleeping at ", "LongFluff": ""} ],
    #         "InterruptionPenalty": 0,
    #         "Location": "ResidentialArea",
    #         },
    #     "BaseData":{
    #         "Name":"",
    #         "ID":"",
    #         "Personality":"Personality",
    #         "State": {
    #             "Energy": 0,
    #             "Mood": 0,
    #             "Arousal": 0,
    #             "Alcohol": 0,
    #             "Drugs": 0,
    #             "PConscious": 1,
    #             "MConscious": 1,
    #             },
    #         "Relations":{},
    #         "BodyData":{
    #             "FullName":"",
    #             "SkinColor":"",
    #             "HairColor":"",
    #             "PhysicalAge":"",
    #             "Race":"",
    #             "Face":"",
    #             "Eyes":"",
    #             "Lips":"",
    #             "Height":"",
    #             "Complexion":"",
    #             "Sex":"",
    #             "Pronouns":{"PSub":"", "PObj":"", "PPos":"", "PIPos":""},
    #             "Hips":0,
    #             "Ass":0,
    #             "Chest":0,
    #             "VTightness":0,
    #             "ATightness":0,
    #             "PenisSize":0,
    #             "BallsSize":0,
    #             "VVirgin":0,
    #             "AVirgin":0,
    #             "PVirgin":0,
    #             "MVirgin":0
    #             },
    #         "OtherData":{"Home":None},
    #         "Traits":{},
    #         "GeneralFlags":{},
    #         "GeneralAbilities":{"MaxEnergy": 0},
    #         "CombatAbilities": {
    #             "DeckName": None,
    #             },
    #         "Descriptions": {
    #             "Backstory": "",
    #             "Core": "",
    #             "Head": "",
    #             "Arms": "",
    #             "Legs": "",
    #             "Genitals": ""
    #             },
    #         "Actions": {
    #             "Intention": None,
    #             "Action": None,
    #             "PreviousTask": {},
    #             "CurrentTask": {},
    #             "FutureTask": {},
    #             "TaskData":{},
    #             "HasFollowing": [],
    #             "InteractionParty": {},
    #             "SexualPary":[],
    #             "IsFollowing": None,
    #             "isInSexScene": [],
    #             "Targeting": None,
    #         },
    #         "Items":{},
    #         "Version":2,
    #         },
    #     }
    #
    # if "PlayerConfig" in Globals.CurrentSession:
    #     Globals.PlayerConfig = Globals.CurrentSession["PlayerConfig"]
    # else:
    #     Globals.PlayerConfig = {
    #     "Interactions":1,
    #     "BetweenNPC":1,
    #     "NPCtoPC":0,
    #     "RandomNPC":1,
    #     "RandomAmount":15,
    #     "RandomRatio":{"Male":35,"Female":55,"FutaRatio":10}
    #     }
    #
    # # if False:
    # if "SoLEnviorementData" in Globals.CurrentSession:
    #     print(1)
    #     Globals.SoLEnviorementData = Globals.CurrentSession["SoLEnviorementData"]
    # else:
    #     print(2)
    #     Globals.SoLEnviorementData ={
    #         "Locations":{
    #             "SouthernStreet": {
    #                 "CanAccess": [
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                     "UpperShoppingArea",
    #                     "Garrison",
    #                     "TrainingArea",
    #                 ],
    #                 "AccesedFrom": [
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                     "UpperShoppingArea",
    #                     "Garrison",
    #                     "TrainingArea",
    #                     "LowerShoppingArea",
    #                     "ResidentialArea",
    #                     "Temple",
    #                     "CommunalArea",
    #                     "SlaversCamp",
    #                     "MainPlaza",
    #                     "Academia",
    #                     "PaladinsArea",
    #                     "Library",
    #                     "University",
    #                     "YourRoom",
    #                 ],
    #                 "PrivacyLevel": 0,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "Southern Street",
    #                 "BaseText":"You are at the Southern Street, the main entrance connecting the city to the rest of the kingdom is here.",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #             "EasternStreet": {
    #                 "CanAccess": [
    #                     "SouthernStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                     "LowerShoppingArea",
    #                     "ResidentialArea",
    #                 ],
    #                 "AccesedFrom": [
    #                     "SouthernStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                     "UpperShoppingArea",
    #                     "Garrison",
    #                     "TrainingArea",
    #                     "LowerShoppingArea",
    #                     "ResidentialArea",
    #                     "Temple",
    #                     "CommunalArea",
    #                     "SlaversCamp",
    #                     "MainPlaza",
    #                     "Academia",
    #                     "PaladinsArea",
    #                     "Library",
    #                     "University",
    #                     "YourRoom",
    #                 ],
    #                 "PrivacyLevel": 0,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "Eastern Street",
    #                 "BaseText":"You are at the Eastern Street, where most of the residential area of the city resides.",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #             "NorthernStreet": {
    #                 "CanAccess": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                     "SlaversCamp",
    #                 ],
    #                 "AccesedFrom": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                     "UpperShoppingArea",
    #                     "Garrison",
    #                     "TrainingArea",
    #                     "LowerShoppingArea",
    #                     "ResidentialArea",
    #                     "Temple",
    #                     "CommunalArea",
    #                     "SlaversCamp",
    #                     "MainPlaza",
    #                     "Academia",
    #                     "PaladinsArea",
    #                     "Library",
    #                     "University",
    #                     "YourRoom",
    #                 ],
    #                 "PrivacyLevel": 0,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "Northern Street",
    #                 "BaseText":"You are at the Northern Street, one of the gates leading into the outside world resides there, as well as the not as controlled part of the city.",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #             "WesternStreet": {
    #                 "CanAccess": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                     "Temple",
    #                     "CommunalArea",
    #                 ],
    #                 "AccesedFrom": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                     "UpperShoppingArea",
    #                     "Garrison",
    #                     "TrainingArea",
    #                     "LowerShoppingArea",
    #                     "ResidentialArea",
    #                     "Temple",
    #                     "CommunalArea",
    #                     "SlaversCamp",
    #                     "MainPlaza",
    #                     "Academia",
    #                     "PaladinsArea",
    #                     "Library",
    #                     "University",
    #                     "YourRoom",
    #                 ],
    #                 "PrivacyLevel": 0,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "Western Street",
    #                 "BaseText":"You are at the Western Street, the church and communal area can be found here.",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #             "MainStreet": {
    #                 "CanAccess": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                     "MainPlaza",
    #                 ],
    #                 "AccesedFrom": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                     "UpperShoppingArea",
    #                     "Garrison",
    #                     "TrainingArea",
    #                     "LowerShoppingArea",
    #                     "ResidentialArea",
    #                     "Temple",
    #                     "CommunalArea",
    #                     "SlaversCamp",
    #                     "MainPlaza",
    #                     "Academia",
    #                     "PaladinsArea",
    #                     "Library",
    #                     "University",
    #                     "YourRoom",
    #                 ],
    #                 "PrivacyLevel": 0,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "Main Street",
    #                 "BaseText":"You are at the Main Street, the principal connection between all the sides of the city.",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #             "DefenseStreet": {
    #                 "CanAccess": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                     "Academia",
    #                     "PaladinsArea",
    #                     "TrainingArea",
    #                 ],
    #                 "AccesedFrom": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                     "UpperShoppingArea",
    #                     "Garrison",
    #                     "TrainingArea",
    #                     "LowerShoppingArea",
    #                     "ResidentialArea",
    #                     "Temple",
    #                     "CommunalArea",
    #                     "SlaversCamp",
    #                     "MainPlaza",
    #                     "Academia",
    #                     "PaladinsArea",
    #                     "Library",
    #                     "University",
    #                     "YourRoom",
    #                 ],
    #                 "PrivacyLevel": 0,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "Defense Street",
    #                 "BaseText":"You are at the Defense Street, The main garrison of the city is stationed here, as well as their training grounds.",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #             "LibraryStreet": {
    #                 "CanAccess": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                     "MainPlaza",
    #                     "Academia",
    #                     "Library",
    #                 ],
    #                 "AccesedFrom": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                     "UpperShoppingArea",
    #                     "Garrison",
    #                     "TrainingArea",
    #                     "LowerShoppingArea",
    #                     "ResidentialArea",
    #                     "Temple",
    #                     "CommunalArea",
    #                     "SlaversCamp",
    #                     "MainPlaza",
    #                     "Academia",
    #                     "PaladinsArea",
    #                     "Library",
    #                     "University",
    #                     "YourRoom",
    #                 ],
    #                 "PrivacyLevel": 0,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "Library Street",
    #                 "BaseText":"You are at the Library Street, connecting the residential district with the main part of the city, it's usually rather populated by commoners coming or going towards the main plaza.",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #             "TempleStreet": {
    #                 "CanAccess": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                     "Temple",
    #                     "MainPlaza",
    #                     "CommunalArea",
    #                 ],
    #                 "AccesedFrom": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                     "UpperShoppingArea",
    #                     "Garrison",
    #                     "TrainingArea",
    #                     "LowerShoppingArea",
    #                     "ResidentialArea",
    #                     "Temple",
    #                     "CommunalArea",
    #                     "SlaversCamp",
    #                     "MainPlaza",
    #                     "Academia",
    #                     "PaladinsArea",
    #                     "Library",
    #                     "University",
    #                     "YourRoom",
    #                 ],
    #                 "PrivacyLevel": 0,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "Temple Street",
    #                 "BaseText":"You are at the Temple Street, The main temple of the city, as well as some low income housing can be found in this area.",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #             "UniversityStreet": {
    #                 "CanAccess": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "Home",
    #                     "University",
    #                     "Laboratory",
    #                 ],
    #                 "AccesedFrom": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "Home",
    #                     "UpperShoppingArea",
    #                     "Garrison",
    #                     "TrainingArea",
    #                     "LowerShoppingArea",
    #                     "ResidentialArea",
    #                     "Temple",
    #                     "CommunalArea",
    #                     "SlaversCamp",
    #                     "MainPlaza",
    #                     "Academia",
    #                     "PaladinsArea",
    #                     "Library",
    #                     "University",
    #                     "Laboratory",
    #                     "YourRoom",
    #                 ],
    #                 "PrivacyLevel": 0,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "University Street",
    #                 "BaseText":"You are at the University Street, Many students can be seen around talking about their educative matters, or just resting in between lessons..",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #             "Home": {
    #                 "CanAccess": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "YourRoom",
    #                 ],
    #                 "AccesedFrom": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "UpperShoppingArea",
    #                     "Garrison",
    #                     "TrainingArea",
    #                     "LowerShoppingArea",
    #                     "ResidentialArea",
    #                     "Temple",
    #                     "CommunalArea",
    #                     "SlaversCamp",
    #                     "MainPlaza",
    #                     "Academia",
    #                     "PaladinsArea",
    #                     "Library",
    #                     "University",
    #                     "YourRoom",
    #                 ],
    #                 "PrivacyLevel": 10,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "Home",
    #                 "BaseText":"You are at your home, nothing too fancy, but you can find everything to sate your basic necesities in here.",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #             "UpperShoppingArea": {
    #                 "CanAccess": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                 ],
    #                 "AccesedFrom": ["SouthernStreet"],
    #                 "PrivacyLevel": 0,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "Upper Shopping Area",
    #                 "BaseText":"You are at the Upper Shopping Area, where most noblemen come for any expensive resources they might need, or for merchants to trade in big enough quantities.",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #             "Garrison": {
    #                 "CanAccess": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "TrainingArea",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                 ],
    #                 "AccesedFrom": ["DefenseStreet", "Garrison"],
    #                 "PrivacyLevel": 0,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "Garrison",
    #                 "BaseText":"You are at the Garrison, soldiers can be seen around going around their day, some more eager and formal than the others but everyone is still doing their part.",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #             "TrainingArea": {
    #                 "CanAccess": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "Garrison",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                 ],
    #                 "AccesedFrom": ["DefenseStreet", "Garrison"],
    #                 "PrivacyLevel": 2,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "Training Area",
    #                 "BaseText":"You are at the Training Area, for the most part being filled with soldiers doing their daily training, but there are also some common people trying to better themselves.",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #             "LowerShoppingArea": {
    #                 "CanAccess": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                 ],
    #                 "AccesedFrom": ["EasternStreet", "ResidentialArea"],
    #                 "PrivacyLevel": 0,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "Lower Shopping Area",
    #                 "BaseText":"You are at the Lower Shopping Area, where most people come to get their daily groceries and anything else they might need.",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #             "ResidentialArea": {
    #                 "CanAccess": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                     "LowerShoppingArea",
    #                 ],
    #                 "AccesedFrom": ["EasternStreet"],
    #                 "PrivacyLevel": 0,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "Residential Area",
    #                 "BaseText":"You are at the Residential Area, where most people reside.",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #             "Temple": {
    #                 "CanAccess": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "CommunalArea",
    #                     "UniversityStreet",
    #                     "Home",
    #                 ],
    #                 "AccesedFrom": ["WesternStreet", "TempleStreet", "CommunalArea"],
    #                 "PrivacyLevel": 0,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "Temple",
    #                 "BaseText":"You are at the Temple, many members of the church can be seen working to administer the place and helping the faithful as needed",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #             "CommunalArea": {
    #                 "CanAccess": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "Temple",
    #                     "UniversityStreet",
    #                     "Home",
    #                 ],
    #                 "AccesedFrom": ["WesternStreet", "TempleStreet", "Temple"],
    #                 "PrivacyLevel": 2,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "Communal Area",
    #                 "BaseText":"You are at the Communal Area, the area around the temple can usually be seens with people enjoying some peace in this place.",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #             "SlaversCamp": {
    #                 "CanAccess": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                 ],
    #                 "AccesedFrom": ["NorthernStreet"],
    #                 "PrivacyLevel": 0,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "Slavers Camp",
    #                 "BaseText":"You are at the Slavers Camp, set up along the north exit many people can be seen trading with exotic good, as well as captured slaves.",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #             "MainPlaza": {
    #                 "CanAccess": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                 ],
    #                 "AccesedFrom": ["MainStreet", "LibraryStreet", "TempleStreet"],
    #                 "PrivacyLevel": 0,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "Main Plaza",
    #                 "BaseText":"You are at the Main Plaza, near the center of the city it it's filled with people mostly commuting, be it young friends playing around, or noblemen rubbing elbows with one another.",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #             "Academia": {
    #                 "CanAccess": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                 ],
    #                 "AccesedFrom": ["DefenseStreet", "LibraryStreet"],
    #                 "PrivacyLevel": 0,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "Academia",
    #                 "BaseText":"You are at the Academia, having separated themselves from the university, it's populated with the upper class of the city coming to learn about the arcane arts .",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #             "PaladinsArea": {
    #                 "CanAccess": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                 ],
    #                 "AccesedFrom": ["DefenseStreet"],
    #                 "PrivacyLevel": 0,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "Paladins Area",
    #                 "BaseText":"You are at the Paladins Area, the soldiers trained by the church forces can be found here, as well as the special equipement they need to train their arcane skills, as well as just for prayer overall.",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #             "Library": {
    #                 "CanAccess": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                 ],
    #                 "AccesedFrom": ["LibraryStreet"],
    #                 "PrivacyLevel": 4,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "Library",
    #                 "BaseText":"You are at the Library, usually occupied by commoners trying to better their understanding of the world.",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #             "University": {
    #                 "CanAccess": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                 ],
    #                 "AccesedFrom": ["UniversityStreet"],
    #                 "PrivacyLevel": 1,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "University",
    #                 "BaseText":"You are at the University, anyone who wishes to have an education can be found in the general stundents loungue, or at their more specific areas depending on the education level they are pursuing.",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #             "Laboratory": {
    #                 "CanAccess": ["UniversityStreet"],
    #                 "AccesedFrom": ["UniversityStreet"],
    #                 "PrivacyLevel": 10,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "Laboratory",
    #                 "BaseText":"You are at the Laboratory, most researchers come here to pursue the nation's understanding of the world, or to develop new technologies in all kinds of fields.",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #             "YourRoom": {
    #                 "CanAccess": [
    #                     "SouthernStreet",
    #                     "EasternStreet",
    #                     "NorthernStreet",
    #                     "WesternStreet",
    #                     "MainStreet",
    #                     "DefenseStreet",
    #                     "LibraryStreet",
    #                     "TempleStreet",
    #                     "UniversityStreet",
    #                     "Home",
    #                 ],
    #                 "AccesedFrom": ["Home"],
    #                 "PrivacyLevel": 10,
    #                 "Allowed": [],
    #                 "Forbidden": [],
    #                 "Flags": {"Open": 1},
    #                 "Name": "Your Room",
    #                 "BaseText":"You are at Your Room, your bed and personal posessions can be found here.",
    #                 "FlavorText":[],
    #                 "inHere": [],
    #             },
    #         },
    #         "DateData": {
    #             "Hour": 480,
    #             "Day": 12,
    #             "Month": 3,
    #             "Year": 1395,
    #             "Weather": "Sunny",
    #             "DaysPlayed": 0,
    #             "Previous": 480,
    #         },
    #         }
    # # if "SoLNPCSchedules" not in Globals.CurrentSession:
    # #     ""
    # # else:
    # #     Globals.SoLNPCSchedules = Globals.CurrentSession["SoLNPCSchedules"]
    #
    # # if "SoLFlavorDict" not in Globals.CurrentSession:
    # if True:
    #     Globals.SoLFlavorDict = {
    #         "EnviorementFlavor":[],
    #         "PCActionsFlavor":[],
    #         "PCTargetFlavor":[],
    #         "NPCActionsFlavor":[],
    #         }
    # else:
    #     Globals.SoLFlavorDict = Globals.CurrentSession["SoLFlavorDict"]
    #
    # FallenList = ["Love", "Lust", "Submission"]
    # for i in FallenList:
    #     Globals.SoLFallenStates[i] = {"ID": i, "Reference": Reference, "OtherData": {}}



    SetBaseData()

    Globals.References["SoLFunctions"].Connect("CTS1", CTSHandling1)
    Globals.References["SoLFunctions"].Connect("CTS2", CTSHandling2)
    Globals.References["SoLFunctions"].Connect("CTS3", CTSHandling3)

def SetBaseData():
    Reference = Globals.References["BasicMod"]
    List = ["Back to Menu", "Move", "Quick Save"]
    for ControlID in List:
        Globals.ControlCommands[ControlID] = {"ID":ControlID, "Reference":Reference, "OtherData":{}}

    if "SoLNPCData" in Globals.CurrentSession:
        Globals.SoLNPCData = Globals.CurrentSession["SoLNPCData"]
    else:
        Globals.SoLNPCData = {}

    if "SoLPCData" in Globals.CurrentSession:
        Globals.SoLPCData = Globals.CurrentSession["SoLPCData"]
    else:
        Globals.SoLPCData = {
            "Name":"",
            "ID":"",
            "Quest":{
                "CurrentQuestText":"",
                "CurrentQuest":"",
                },
            "Abilities":{},
            "Flags":{},
            "Targeting":None,
            "OtherData":{},
            }
        for ID in Globals.SoLNPCData:
            Globals.SoLPCData["ID"] = ID
            break

    if "SoLTempData" in Globals.CurrentSession:
        Globals.SoLTempData = Globals.CurrentSession["SoLTempData"]
        Globals.SoLTempData["TempNPC"] = []
        Globals.SoLTempData["FavoriteNPC"] = []
    else:
        Globals.SoLTempData = {
            "TempNPC":[],
            "FavoriteNPC":[],

            }

    if True:
        Globals.SoLOtherData = {
        "baseRelationship":{
            "Temporal": {},
            "Permanent": {
                "Attraction": 0,
                "Reliability": 0,
                },
            "Gems": {},
            "Flags": {
                "HasConsent": 0
                },
            "Abilities": {},
            "Preferences": {},
            "FallenData": {},
            },
        "IdlingTask":{
            "HourStart": 0,
            "HourFinish": 1,
            "Task": ["Idling", {"BriefFluff": "Idling in the streets of ", "LongFluff": ""} ],
            "InterruptionPenalty": 0,
            "Location": "ResidentialArea",
            },
        "SleepTask":{
            "HourStart": 0,
            "HourFinish": 0,
            "Task": ["Sleeping", {"BriefFluff": "Sleeping at ", "LongFluff": ""} ],
            "InterruptionPenalty": 0,
            "Location": "ResidentialArea",
            },
        "BaseData":{
            "Name":"",
            "ID":"",
            "Personality":"Personality",
            "State": {
                "Energy": 0,
                "Mood": 0,
                "Arousal": 0,
                "Alcohol": 0,
                "Drugs": 0,
                "PConscious": 1,
                "MConscious": 1,
                },
            "Relations":{},
            "BodyData":{
                "FullName":"",
                "SkinColor":"",
                "HairColor":"",
                "PhysicalAge":"",
                "Race":"",
                "Face":"",
                "Eyes":"",
                "Lips":"",
                "Height":"",
                "Complexion":"",
                "Sex":"",
                "Pronouns":{"PSub":"", "PObj":"", "PPos":"", "PIPos":""},
                "Hips":0,
                "Ass":0,
                "Chest":0,
                "VTightness":0,
                "ATightness":0,
                "PenisSize":0,
                "BallsSize":0,
                "VVirgin":0,
                "AVirgin":0,
                "PVirgin":0,
                "MVirgin":0
                },
            "OtherData":{"Home":None},
            "Traits":{},
            "GeneralFlags":{},
            "GeneralAbilities":{"MaxEnergy": 0},
            "CombatAbilities": {
                "DeckName": None,
                },
            "Descriptions": {
                "Backstory": "",
                "Core": "",
                "Head": "",
                "Arms": "",
                "Legs": "",
                "Genitals": ""
                },
            "Actions": {
                "Intention": None,
                "Action": None,
                "PreviousTask": {},
                "CurrentTask": {},
                "FutureTask": {},
                "TaskData":{},
                "HasFollowing": [],
                "InteractionParty": {},
                "SexualPary":[],
                "IsFollowing": None,
                "isInSexScene": [],
                "Targeting": None,
            },
            "Items":{},
            "isInSexScene": 0,
            "Version":2,
            },
        }

    if "PlayerConfig" in Globals.CurrentSession:
        Globals.PlayerConfig = Globals.CurrentSession["PlayerConfig"]
    else:
        Globals.PlayerConfig = {
        "Interactions":1,
        "BetweenNPC":1,
        "NPCtoPC":0,
        "RandomNPC":1,
        "RandomAmount":15,
        "RandomRatio":{"Male":35,"Female":55,"FutaRatio":10}
        }

    # if "SoLEnviorementData" in Globals.CurrentSession:
    if "SoLEnviorementData" in Globals.CurrentSession:
        Globals.SoLEnviorementData = Globals.CurrentSession["SoLEnviorementData"]
    else:
        Globals.SoLEnviorementData ={
            "Locations":{
                "SouthernStreet": {
                    "CanAccess": [
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                        "UpperShoppingArea",
                        "Garrison",
                        "TrainingArea",
                    ],
                    "AccesedFrom": [
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                        "UpperShoppingArea",
                        "Garrison",
                        "TrainingArea",
                        "LowerShoppingArea",
                        "ResidentialArea",
                        "Temple",
                        "CommunalArea",
                        "SlaversCamp",
                        "MainPlaza",
                        "Academia",
                        "PaladinsArea",
                        "Library",
                        "University",
                        "YourRoom",
                    ],
                    "PrivacyLevel": 0,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "Southern Street",
                    "BaseText":"You are at the Southern Street, the main entrance connecting the city to the rest of the kingdom is here.",
                    "FlavorText":[],
                    "inHere": [],
                },
                "EasternStreet": {
                    "CanAccess": [
                        "SouthernStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                        "LowerShoppingArea",
                        "ResidentialArea",
                    ],
                    "AccesedFrom": [
                        "SouthernStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                        "UpperShoppingArea",
                        "Garrison",
                        "TrainingArea",
                        "LowerShoppingArea",
                        "ResidentialArea",
                        "Temple",
                        "CommunalArea",
                        "SlaversCamp",
                        "MainPlaza",
                        "Academia",
                        "PaladinsArea",
                        "Library",
                        "University",
                        "YourRoom",
                    ],
                    "PrivacyLevel": 0,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "Eastern Street",
                    "BaseText":"You are at the Eastern Street, where most of the residential area of the city resides.",
                    "FlavorText":[],
                    "inHere": [],
                },
                "NorthernStreet": {
                    "CanAccess": [
                        "SouthernStreet",
                        "EasternStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                        "SlaversCamp",
                    ],
                    "AccesedFrom": [
                        "SouthernStreet",
                        "EasternStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                        "UpperShoppingArea",
                        "Garrison",
                        "TrainingArea",
                        "LowerShoppingArea",
                        "ResidentialArea",
                        "Temple",
                        "CommunalArea",
                        "SlaversCamp",
                        "MainPlaza",
                        "Academia",
                        "PaladinsArea",
                        "Library",
                        "University",
                        "YourRoom",
                    ],
                    "PrivacyLevel": 0,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "Northern Street",
                    "BaseText":"You are at the Northern Street, one of the gates leading into the outside world resides there, as well as the not as controlled part of the city.",
                    "FlavorText":[],
                    "inHere": [],
                },
                "WesternStreet": {
                    "CanAccess": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                        "Temple",
                        "CommunalArea",
                    ],
                    "AccesedFrom": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                        "UpperShoppingArea",
                        "Garrison",
                        "TrainingArea",
                        "LowerShoppingArea",
                        "ResidentialArea",
                        "Temple",
                        "CommunalArea",
                        "SlaversCamp",
                        "MainPlaza",
                        "Academia",
                        "PaladinsArea",
                        "Library",
                        "University",
                        "YourRoom",
                    ],
                    "PrivacyLevel": 0,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "Western Street",
                    "BaseText":"You are at the Western Street, the church and communal area can be found here.",
                    "FlavorText":[],
                    "inHere": [],
                },
                "MainStreet": {
                    "CanAccess": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                        "MainPlaza",
                    ],
                    "AccesedFrom": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                        "UpperShoppingArea",
                        "Garrison",
                        "TrainingArea",
                        "LowerShoppingArea",
                        "ResidentialArea",
                        "Temple",
                        "CommunalArea",
                        "SlaversCamp",
                        "MainPlaza",
                        "Academia",
                        "PaladinsArea",
                        "Library",
                        "University",
                        "YourRoom",
                    ],
                    "PrivacyLevel": 0,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "Main Street",
                    "BaseText":"You are at the Main Street, the principal connection between all the sides of the city.",
                    "FlavorText":[],
                    "inHere": [],
                },
                "DefenseStreet": {
                    "CanAccess": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                        "Academia",
                        "PaladinsArea",
                        "TrainingArea",
                    ],
                    "AccesedFrom": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                        "UpperShoppingArea",
                        "Garrison",
                        "TrainingArea",
                        "LowerShoppingArea",
                        "ResidentialArea",
                        "Temple",
                        "CommunalArea",
                        "SlaversCamp",
                        "MainPlaza",
                        "Academia",
                        "PaladinsArea",
                        "Library",
                        "University",
                        "YourRoom",
                    ],
                    "PrivacyLevel": 0,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "Defense Street",
                    "BaseText":"You are at the Defense Street, The main garrison of the city is stationed here, as well as their training grounds.",
                    "FlavorText":[],
                    "inHere": [],
                },
                "LibraryStreet": {
                    "CanAccess": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                        "MainPlaza",
                        "Academia",
                        "Library",
                    ],
                    "AccesedFrom": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                        "UpperShoppingArea",
                        "Garrison",
                        "TrainingArea",
                        "LowerShoppingArea",
                        "ResidentialArea",
                        "Temple",
                        "CommunalArea",
                        "SlaversCamp",
                        "MainPlaza",
                        "Academia",
                        "PaladinsArea",
                        "Library",
                        "University",
                        "YourRoom",
                    ],
                    "PrivacyLevel": 0,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "Library Street",
                    "BaseText":"You are at the Library Street, connecting the residential district with the main part of the city, it's usually rather populated by commoners coming or going towards the main plaza.",
                    "FlavorText":[],
                    "inHere": [],
                },
                "TempleStreet": {
                    "CanAccess": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "UniversityStreet",
                        "Home",
                        "Temple",
                        "MainPlaza",
                        "CommunalArea",
                    ],
                    "AccesedFrom": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "UniversityStreet",
                        "Home",
                        "UpperShoppingArea",
                        "Garrison",
                        "TrainingArea",
                        "LowerShoppingArea",
                        "ResidentialArea",
                        "Temple",
                        "CommunalArea",
                        "SlaversCamp",
                        "MainPlaza",
                        "Academia",
                        "PaladinsArea",
                        "Library",
                        "University",
                        "YourRoom",
                    ],
                    "PrivacyLevel": 0,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "Temple Street",
                    "BaseText":"You are at the Temple Street, The main temple of the city, as well as some low income housing can be found in this area.",
                    "FlavorText":[],
                    "inHere": [],
                },
                "UniversityStreet": {
                    "CanAccess": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "Home",
                        "University",
                        "Laboratory",
                    ],
                    "AccesedFrom": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "Home",
                        "UpperShoppingArea",
                        "Garrison",
                        "TrainingArea",
                        "LowerShoppingArea",
                        "ResidentialArea",
                        "Temple",
                        "CommunalArea",
                        "SlaversCamp",
                        "MainPlaza",
                        "Academia",
                        "PaladinsArea",
                        "Library",
                        "University",
                        "Laboratory",
                        "YourRoom",
                    ],
                    "PrivacyLevel": 0,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "University Street",
                    "BaseText":"You are at the University Street, Many students can be seen around talking about their educative matters, or just resting in between lessons..",
                    "FlavorText":[],
                    "inHere": [],
                },
                "Home": {
                    "CanAccess": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "YourRoom",
                    ],
                    "AccesedFrom": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "UpperShoppingArea",
                        "Garrison",
                        "TrainingArea",
                        "LowerShoppingArea",
                        "ResidentialArea",
                        "Temple",
                        "CommunalArea",
                        "SlaversCamp",
                        "MainPlaza",
                        "Academia",
                        "PaladinsArea",
                        "Library",
                        "University",
                        "YourRoom",
                    ],
                    "PrivacyLevel": 10,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "Home",
                    "BaseText":"You are at your home, nothing too fancy, but you can find everything to sate your basic necesities in here.",
                    "FlavorText":[],
                    "inHere": [],
                },
                "UpperShoppingArea": {
                    "CanAccess": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                    ],
                    "AccesedFrom": ["SouthernStreet"],
                    "PrivacyLevel": 0,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "Upper Shopping Area",
                    "BaseText":"You are at the Upper Shopping Area, where most noblemen come for any expensive resources they might need, or for merchants to trade in big enough quantities.",
                    "FlavorText":[],
                    "inHere": [],
                },
                "Garrison": {
                    "CanAccess": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "TrainingArea",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                    ],
                    "AccesedFrom": ["DefenseStreet", "Garrison"],
                    "PrivacyLevel": 0,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "Garrison",
                    "BaseText":"You are at the Garrison, soldiers can be seen around going around their day, some more eager and formal than the others but everyone is still doing their part.",
                    "FlavorText":[],
                    "inHere": [],
                },
                "TrainingArea": {
                    "CanAccess": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "Garrison",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                    ],
                    "AccesedFrom": ["DefenseStreet", "Garrison"],
                    "PrivacyLevel": 2,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "Training Area",
                    "BaseText":"You are at the Training Area, for the most part being filled with soldiers doing their daily training, but there are also some common people trying to better themselves.",
                    "FlavorText":[],
                    "inHere": [],
                },
                "LowerShoppingArea": {
                    "CanAccess": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                    ],
                    "AccesedFrom": ["EasternStreet", "ResidentialArea"],
                    "PrivacyLevel": 0,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "Lower Shopping Area",
                    "BaseText":"You are at the Lower Shopping Area, where most people come to get their daily groceries and anything else they might need.",
                    "FlavorText":[],
                    "inHere": [],
                },
                "ResidentialArea": {
                    "CanAccess": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                        "LowerShoppingArea",
                    ],
                    "AccesedFrom": ["EasternStreet"],
                    "PrivacyLevel": 0,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "Residential Area",
                    "BaseText":"You are at the Residential Area, where most people reside.",
                    "FlavorText":[],
                    "inHere": [],
                },
                "Temple": {
                    "CanAccess": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "CommunalArea",
                        "UniversityStreet",
                        "Home",
                    ],
                    "AccesedFrom": ["WesternStreet", "TempleStreet", "CommunalArea"],
                    "PrivacyLevel": 0,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "Temple",
                    "BaseText":"You are at the Temple, many members of the church can be seen working to administer the place and helping the faithful as needed",
                    "FlavorText":[],
                    "inHere": [],
                },
                "CommunalArea": {
                    "CanAccess": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "Temple",
                        "UniversityStreet",
                        "Home",
                    ],
                    "AccesedFrom": ["WesternStreet", "TempleStreet", "Temple"],
                    "PrivacyLevel": 2,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "Communal Area",
                    "BaseText":"You are at the Communal Area, the area around the temple can usually be seens with people enjoying some peace in this place.",
                    "FlavorText":[],
                    "inHere": [],
                },
                "SlaversCamp": {
                    "CanAccess": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                    ],
                    "AccesedFrom": ["NorthernStreet"],
                    "PrivacyLevel": 0,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "Slavers Camp",
                    "BaseText":"You are at the Slavers Camp, set up along the north exit many people can be seen trading with exotic good, as well as captured slaves.",
                    "FlavorText":[],
                    "inHere": [],
                },
                "MainPlaza": {
                    "CanAccess": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                    ],
                    "AccesedFrom": ["MainStreet", "LibraryStreet", "TempleStreet"],
                    "PrivacyLevel": 0,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "Main Plaza",
                    "BaseText":"You are at the Main Plaza, near the center of the city it it's filled with people mostly commuting, be it young friends playing around, or noblemen rubbing elbows with one another.",
                    "FlavorText":[],
                    "inHere": [],
                },
                "Academia": {
                    "CanAccess": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                    ],
                    "AccesedFrom": ["DefenseStreet", "LibraryStreet"],
                    "PrivacyLevel": 0,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "Academia",
                    "BaseText":"You are at the Academia, having separated themselves from the university, it's populated with the upper class of the city coming to learn about the arcane arts .",
                    "FlavorText":[],
                    "inHere": [],
                },
                "PaladinsArea": {
                    "CanAccess": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                    ],
                    "AccesedFrom": ["DefenseStreet"],
                    "PrivacyLevel": 0,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "Paladins Area",
                    "BaseText":"You are at the Paladins Area, the soldiers trained by the church forces can be found here, as well as the special equipement they need to train their arcane skills, as well as just for prayer overall.",
                    "FlavorText":[],
                    "inHere": [],
                },
                "Library": {
                    "CanAccess": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                    ],
                    "AccesedFrom": ["LibraryStreet"],
                    "PrivacyLevel": 4,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "Library",
                    "BaseText":"You are at the Library, usually occupied by commoners trying to better their understanding of the world.",
                    "FlavorText":[],
                    "inHere": [],
                },
                "University": {
                    "CanAccess": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                    ],
                    "AccesedFrom": ["UniversityStreet"],
                    "PrivacyLevel": 1,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "University",
                    "BaseText":"You are at the University, anyone who wishes to have an education can be found in the general stundents loungue, or at their more specific areas depending on the education level they are pursuing.",
                    "FlavorText":[],
                    "inHere": [],
                },
                "Laboratory": {
                    "CanAccess": ["UniversityStreet"],
                    "AccesedFrom": ["UniversityStreet"],
                    "PrivacyLevel": 10,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "Laboratory",
                    "BaseText":"You are at the Laboratory, most researchers come here to pursue the nation's understanding of the world, or to develop new technologies in all kinds of fields.",
                    "FlavorText":[],
                    "inHere": [],
                },
                "YourRoom": {
                    "CanAccess": [
                        "SouthernStreet",
                        "EasternStreet",
                        "NorthernStreet",
                        "WesternStreet",
                        "MainStreet",
                        "DefenseStreet",
                        "LibraryStreet",
                        "TempleStreet",
                        "UniversityStreet",
                        "Home",
                    ],
                    "AccesedFrom": ["Home"],
                    "PrivacyLevel": 10,
                    "Allowed": [],
                    "Forbidden": [],
                    "Flags": {"Open": 1},
                    "Name": "Your Room",
                    "BaseText":"You are at Your Room, your bed and personal posessions can be found here.",
                    "FlavorText":[],
                    "inHere": [],
                },
            },
            "DateData": {
                "Hour": 480,
                "Day": 12,
                "Month": 3,
                "Year": 1395,
                "Weather": "Sunny",
                "DaysPlayed": 0,
                "Previous": 480,
            },
            }

    if "SoLNPCSchedules" not in Globals.CurrentSession:
        ""
    else:
        Globals.SoLNPCSchedules = Globals.CurrentSession["SoLNPCSchedules"]

    # if "SoLFlavorDict" not in Globals.CurrentSession:
    if True:
        Globals.SoLFlavorDict = {
            "EnviorementFlavor":[],
            "PCActionsFlavor":[],
            "PCTargetFlavor":[],
            "NPCActionsFlavor":[],
            }
    else:
        Globals.SoLFlavorDict = Globals.CurrentSession["SoLFlavorDict"]

    FallenList = ["Love", "Lust", "Submission"]
    for i in FallenList:
        Globals.SoLFallenStates[i] = {"ID": i, "Reference": Reference, "OtherData": {}}

    ""

def CTSHandling1():
    Data = Globals.SignalData["CTS1"]["Values"]

def CTSHandling2():
    Data = Globals.SignalData["CTS2"]["Values"]

def CTSHandling3():
    Data = Globals.SignalData["CTS3"]["Values"]

def GetFallenRelationData(Data):
    FallenList = ["Love", "Lust", "Submission"]
    # Data = {"ID":FallenID, "Level":Value,"OtherData":{}}
    Relation = 0
    # if Data["ID"] == "Love":
    if Data["Level"] != 0:
        Relation = Data["Level"] + 1
    return Relation

def FallenChange(FallenID, NPCID, OtherID, Data, Value):
    if list(Data.keys()) == ["Level"]:
        Data = {"ID":FallenID, "Level":Value,"OtherData":{}}
    else:
        Data["Level"] = Value
    Globals.SoLNPCData[NPCID]["Relations"][OtherID]["FallenData"][FallenID] = Data
    Globals.LayoutsData["Active"].Refresh()

def GetFallenConditions(FallenID, NPCID, OtherID, Flags):
    Value = 0
    try:
        Value = Globals.SoLNPCData[NPCID]["Relations"][OtherID]["FallenData"][FallenID]["Level"]
    except Exception as e:
        ""
    Dict = {}
    TARelation = Globals.SoLNPCData[NPCID]["Relations"][OtherID]
    Permanent = TARelation["Permanent"]

    if FallenID == "Love":
        # 1: Affection
            # Gain: 1500 Reliability / 500 Attaction
            # Lose:
        # 2: Love
            # Gain: 3500 Reliability / 1500 Attaction
            # Lose:

        if Value == 0:
            Dict[0] = {"Level":0, "Title":"---", "Text":"Current Level", "Available":0}

            Dict[1] = {"Level":1, "Title":"Affection", "Text":"1500 Reliability / 500 Attaction", "Available":0}
            if ("Attaction" in Permanent and Permanent["Attaction"] >= 1500 and "Reliability" in Permanent and Permanent["Reliability"] >= 500) or Flags["ForceAvailable"]: Dict[1]["Available"] = 1

            Dict[2] = {"Level":1, "Title":"Love", "Text":"3500 Reliability / 1500 Attaction", "Available":0}
        elif Value == 1:
            Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Fear Gems", "Available":0}
            if ("Fear" in TARelation["Gems"] and TARelation["Gems"]["Fear"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1

            Dict[1] = {"Level":1, "Title":"Affection", "Text":"CurrentLevel", "Available":0}

            Dict[2] = {"Level":1, "Title":"Love", "Text":"3500 Reliability / 1500 Attaction", "Available":0}
            if ("Attaction" in Permanent and Permanent["Attaction"] >= 3500 and "Reliability" in Permanent and Permanent["Reliability"] >= 1500) or Flags["ForceAvailable"]: Dict[2]["Available"] = 1
        elif Value == 2:
            Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Fear Gems", "Available":0}

            Dict[1] = {"Level":0, "Title":"Affection", "Text":"2500 Fear Gems", "Available":0}
            if ("Fear" in TARelation["Gems"] and TARelation["Gems"]["Fear"]["Amount"] >= 2500) or Flags["ForceAvailable"] == 1: Dict[1]["Available"] = 1

            Dict[2] = {"Level":1, "Title":"Love", "Text":"CurrentLevel", "Available":0}


        # Dict[0] = {"Level":0, "Title":"---", "Text":"", "Available":0}
        #
        # Dict[1] = {"Level":1, "Title":"Affection", "Text":"1500 Reliability / 500 Attaction", "Available":0}
        # if (("Reliability" in Permanent and Permanent["Reliability"] >= 1500 and "Attaction" in Permanent and Permanent["Attaction"] >= 500) or Flags["ForceAvailable"]) and Value == 0: Dict[1]["Available"] = 1
        #
        # Dict[2] = {"Level":1, "Title":"Love", "Text":"3500 Reliability / 1500 Attaction", "Available":0}
        # if (("Reliability" in Permanent and Permanent["Reliability"] >= 3500 and "Attaction" in Permanent and Permanent["Attaction"] >= 1500) or Flags["ForceAvailable"]) and Value == 0: Dict[2]["Available"] = 1
        #
        # if Value != 0:
        #     if Value == 1:
        #         Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Fear Gems", "Available":0}
        #         if ("Fear" in Gems and Gems["Fear"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1
        #     if Value == 2:
        #         Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Fear Gems", "Available":0}
        #         if ("Fear" in Gems and Gems["Fear"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1



    elif FallenID == "Lust":
        if Value == 0:
            Dict[0] = {"Level":0, "Title":"---", "Text":"Current Level", "Available":0}

            Dict[1] = {"Level":1, "Title":"Lewd", "Text":"1500 Attaction / 500 Reliability", "Available":0}
            if ("Reliability" in Permanent and Permanent["Reliability"] >= 1500 and "Attaction" in Permanent and Permanent["Attaction"] >= 500) or Flags["ForceAvailable"]: Dict[1]["Available"] = 1

            Dict[2] = {"Level":1, "Title":"Lustfull", "Text":"3500 Attaction / 1500 Reliability", "Available":0}
        elif Value == 1:
            Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Fear Gems", "Available":0}
            if ("Fear" in TARelation["Gems"] and TARelation["Gems"]["Fear"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1

            Dict[1] = {"Level":1, "Title":"Lewd", "Text":"CurrentLevel", "Available":0}

            Dict[2] = {"Level":1, "Title":"Lustfull", "Text":"3500 Attaction / 1500 Reliability", "Available":0}
            if ("Reliability" in Permanent and Permanent["Reliability"] >= 3500 and "Attaction" in Permanent and Permanent["Attaction"] >= 1500) or Flags["ForceAvailable"]: Dict[2]["Available"] = 1
        elif Value == 2:
            Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Fear Gems", "Available":0}

            Dict[1] = {"Level":0, "Title":"Lewd", "Text":"2500 Fear Gems", "Available":0}
            if ("Fear" in TARelation["Gems"] and TARelation["Gems"]["Fear"]["Amount"] >= 2500) or Flags["ForceAvailable"] == 1: Dict[1]["Available"] = 1

            Dict[2] = {"Level":1, "Title":"Lustfull", "Text":"CurrentLevel", "Available":0}



    elif FallenID == "Submission":
        # 1: Submissive
            # Gain: 1500 ServiceExp or 1500 PainExp + MasochismExp
            # Lose:
        # 2: Slave
            # Gain: 3500 ServiceExp or 3500 PainExp + MasochismExp
            # Lose:
        if Value == 0:
            Dict[0] = {"Level":0, "Title":"---", "Text":"Current Level", "Available":0}

            Gems = 0
            if "PainExp" in Permanent: Gems += Permanent["PainExp"]
            if "MasochismExp" in Permanent: Gems += Permanent["MasochismExp"]
            Dict[1] = {"Level":1, "Title":"Submissive", "Text":"1500 ServiceExp or 1500 PainExp + MasochismExp", "Available":0}
            if (Gems >= 1500 or ("ServiceExp" in Permanent and Permanent["ServiceExp"] >= 1500)) or Flags["ForceAvailable"]: Dict[1]["Available"] = 1

            Dict[2] = {"Level":2, "Title":"Slave", "Text":"3500 ServiceExp or 3500 PainExp + MasochismExp", "Available":0}
        elif Value == 1:
            Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Fear Gems", "Available":0}
            if ("Fear" in TARelation["Gems"] and TARelation["Gems"]["Fear"]["Amount"] >= 1500) or Flags["ForceAvailable"] == 1: Dict[0]["Available"] = 1

            Dict[1] = {"Level":1, "Title":"Submissive", "Text":"CurrentLevel", "Available":0}

            Gems = 0
            if "PainExp" in Permanent: Gems += Permanent["PainExp"]
            if "MasochismExp" in Permanent: Gems += Permanent["MasochismExp"]
            Dict[2] = {"Level":1, "Title":"Slave", "Text":"3500 ServiceExp or 3500 PainExp + MasochismExp", "Available":0}
            if (Gems >= 3500 or ("ServiceExp" in Permanent and Permanent["ServiceExp"] >= 3500)) or Flags["ForceAvailable"]: Dict[2]["Available"] = 1
        elif Value == 2:
            Dict[0] = {"Level":0, "Title":"---", "Text":"1500 Fear Gems", "Available":0}

            Dict[1] = {"Level":0, "Title":"Submissive", "Text":"2500 Fear Gems", "Available":0}
            if ("Fear" in TARelation["Gems"] and TARelation["Gems"]["Fear"]["Amount"] >= 2500) or Flags["ForceAvailable"] == 1: Dict[1]["Available"] = 1

            Dict[2] = {"Level":1, "Title":"Slave", "Text":"CurrentLevel", "Available":0}

    return Dict

def GetFallenDynamicWidget(FallenID, Data, NPCID, OtherID, Flags):
    try:
        Value = Data["Level"]
    except:
        Data = {"Level": 0}
        Value = 0

    Conditions = GetFallenConditions(FallenID, NPCID, OtherID, Flags)

    if True:
        WidgetsList = []
        Widget = QWidget(objectName = "Transparent")

        TitleLabel = QLabel(f"{FallenID}", Widget, objectName = "SubTitle")
        TitleLabel.setProperty("Color","Light")
        TitleLabel.setGeometry(0,0,250,40)
        TitleLabel.setMinimumHeight(40)
        TitleLabel.setMaximumHeight(40)
        TitleLabel.setAlignment(QtCore.Qt.AlignCenter)

        Holder = QWidget(Widget)
        Holder.setGeometry(0,45,250,0)

        Layout = QVBoxLayout()
        Layout.setSpacing(0)
        Layout.setContentsMargins(0, 0, 0, 0)
        Widget.setContentsMargins(0, 0, 0, 0)
        Holder.setLayout(Layout)

        Height = 0

        if 0 in Conditions:
            Widget0 = QWidget()

            BackLabel0 = QLabel(Widget0)
            BackLabel0.setProperty("Color","Dark")
            Label0 = QLabel(Widget0, objectName = "SmallText")
            Label0.setProperty("Color","Dark")
            Label0.setProperty("Border","None")
            Label0.setGeometry(0,0,215,35)
            Label0.setWordWrap(True)

            Available = Conditions[0]["Available"]
            if Available == 1:
                def Click0():
                    if Button0.Available == 1:
                        FallenChange(FallenID, NPCID, OtherID, Data, 0)
                Button0 = QPushButton(Widget0, clicked = lambda: Click0())
                Button0.setStyleSheet("border-image: url(Resources/SoLResources/Cycle.png); ")
                Button0.setGeometry(215,1,33,33)
                Button0.setProperty("Color","Dark")
                Button0.Available = Available

                if Value != 0:
                    Label0.setProperty("Selected",1)

            if Value == 0:
                Label0.setText(f'''{Conditions[0]["Title"]}: Current Level''')
            elif Value == 1:
                Label0.setText(f'''{Conditions[0]["Title"]}: {Conditions[0]["Text"]}''')
            else:
                Label0.setText(f'''{Conditions[0]["Title"]}: {Conditions[0]["Text"]}''')
                Label0.setProperty("Selected",-1)
            # if Value != 0:
            #     Label0.setText(f'''{Conditions[0]["Title"]}: {Conditions[0]["Text"]}''')
            # else:
            #     Label0.setText(f'''{Conditions[0]["Title"]}: Current Level''')

            LabelHeight = Globals.References["SoLFunctions"].AdjustSize(Label0)
            Label0.setGeometry(1,1,214,LabelHeight)
            BackLabel0.setGeometry(0,0,250,LabelHeight+2)

            Widget0.setMinimumHeight(BackLabel0.height())
            Widget0.setMaximumHeight(BackLabel0.height())

            Layout.addWidget(Widget0)
            Height += Widget0.height()

        if 1 in Conditions:
            Widget1 = QWidget()

            BackLabel1 = QLabel(Widget1)
            BackLabel1.setProperty("Color","Dark")
            Label1 = QLabel(Widget1, objectName = "SmallText")
            Label1.setProperty("Color","Dark")
            Label1.setProperty("Border","None")
            Label1.setGeometry(0,0,215,35)
            Label1.setWordWrap(True)

            Available = Conditions[1]["Available"]
            if Available == 1:
                def Click1():
                    if Button1.Available == 1:
                        FallenChange(FallenID, NPCID, OtherID, Data, 1)
                Button1 = QPushButton(Widget1, clicked = lambda: Click1())
                Button1.setStyleSheet("border-image: url(Resources/SoLResources/Cycle.png); ")
                Button1.setGeometry(215,1,33,33)
                Button1.setProperty("Color","Dark")
                Button1.Available = Available

                if Value != 1:
                    Label1.setProperty("Selected",1)


            if Value == 0:
                Label1.setText(f'''{Conditions[1]["Title"]}: {Conditions[1]["Text"]}''')
            elif Value == 1:
                Label1.setText(f'''{Conditions[1]["Title"]}: Current Level''')
            else:
                Label1.setText(f'''{Conditions[1]["Title"]}: {Conditions[1]["Text"]}''')
            # elif Value != 0 and Value != 1:
            #     Label1.setProperty("Selected",-1)
            # if Value != 1:
            #     Label1.setText(f'''{Conditions[1]["Title"]}: {Conditions[1]["Text"]}''')
            # else:
            #     Label1.setText(f'''{Conditions[1]["Title"]}: Current Level''')

            LabelHeight = Globals.References["SoLFunctions"].AdjustSize(Label1)
            Label1.setGeometry(1,1,214,LabelHeight)
            BackLabel1.setGeometry(0,0,250,LabelHeight+2)

            Widget1.setMinimumHeight(BackLabel1.height())
            Widget1.setMaximumHeight(BackLabel1.height())

            Layout.addWidget(Widget1)
            Height += Widget1.height()

        if 2 in Conditions:
            Widget2 = QWidget()

            BackLabel2 = QLabel(Widget2)
            BackLabel2.setProperty("Color","Dark")
            Label2 = QLabel(Widget2, objectName = "SmallText")
            Label2.setProperty("Color","Dark")
            Label2.setProperty("Border","None")
            Label2.setGeometry(0,0,215,35)
            Label2.setWordWrap(True)

            Available = Conditions[2]["Available"]
            if Available == 1:
                def Click2():
                    if Button2.Available == 1:
                        FallenChange(FallenID, NPCID, OtherID, Data, 2)
                Button2 = QPushButton(Widget2, clicked = lambda: Click2())
                Button2.setStyleSheet("border-image: url(Resources/SoLResources/Cycle.png); ")
                Button2.setGeometry(215,1,33,33)
                Button2.setProperty("Color","Dark")
                Button2.Available = Available

                if Value != 2:
                    Label2.setProperty("Selected",1)
            if Value == 0:
                Label2.setText(f'''{Conditions[2]["Title"]}: {Conditions[2]["Text"]}''')
                Label2.setProperty("Selected",-1)
            elif Value == 1:
                Label2.setText(f'''{Conditions[2]["Title"]}: {Conditions[2]["Text"]}''')
            else:
                Label2.setText(f'''{Conditions[2]["Title"]}: Current Level''')
            # elif Value != 0 and Value != 2:
            #     Label2.setProperty("Selected",-1)
            # if Value != 2:
            #     Label2.setText(f'''{Conditions[2]["Title"]}: {Conditions[2]["Text"]}''')
            # else:
            #     Label2.setText(f'''{Conditions[2]["Title"]}: Current Level''')

            LabelHeight = Globals.References["SoLFunctions"].AdjustSize(Label2)
            Label2.setGeometry(1,1,214,LabelHeight)
            BackLabel2.setGeometry(0,0,250,LabelHeight+2)

            Widget2.setMinimumHeight(BackLabel2.height())
            Widget2.setMaximumHeight(BackLabel2.height())

            Layout.addWidget(Widget2)
            Height += Widget2.height()

        Holder.setMinimumHeight(Height)
        Holder.setMaximumHeight(Height)

        Widget.setMinimumHeight(Height+45)
        Widget.setMaximumHeight(Height+45)

        Widget.setMinimumWidth(250)
        Widget.setMaximumWidth(250)

        return Widget

    return None



def GetStaticFallenWidget(FallenID, FallenData, RelationData):
    def check(Amount,Needed):
        if Amount >= Needed:
            return f'''<font color=#FFFF00>'''
        else:
            return f'''<font color=#FFFFFF>'''
    Attraction = RelationData["Permanent"]["Attraction"]
    Reliability = RelationData["Permanent"]["Reliability"]

    if FallenID == "Love":
        FallenWidget = QWidget()
        FallenWidget.setStyleSheet('''
        QWidget{
        background-color:rgb(23,23,23)
        }
        QLabel{
        background-color:rgb(23,23,23)
        }
        ''')

        Label = QLabel(FallenWidget)
        Label.setGeometry(0,0,200,145)
        Text = f'''<strong>Affection: </strong><br/>{check(Reliability,1000)}Reliability: 1000</Font><br/> {check(Attraction,300)}Attraction: 300</Font><br/>'''
        Label.setText(Text)
        Label.setFont(QFont('Segoe UI', 12))
        Label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)


        FallenWidget.setMinimumWidth(200)
        FallenWidget.setMaximumWidth(200)
        FallenWidget.setMinimumHeight(150)
        FallenWidget.setMaximumHeight(150)
        return FallenWidget
    elif FallenID == "Lust":
        FallenWidget = QWidget()
        FallenWidget.setStyleSheet('''
        QWidget{
        background-color:rgb(23,23,23)
        }
        QLabel{
        background-color:rgb(23,23,23)
        }
        ''')

        Label = QLabel(FallenWidget)
        Label.setGeometry(0,0,200,145)
        Text = f'''<strong>Lewd: </strong><br/> {check(Attraction,1000)}Attraction: 1000</Font><br/> {check(Reliability,300)}Reliability: 300</Font><br/>'''
        Label.setText(Text)
        Label.setFont(QFont('Segoe UI', 12))
        Label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)


        FallenWidget.setMinimumWidth(200)
        FallenWidget.setMaximumWidth(200)
        FallenWidget.setMinimumHeight(150)
        FallenWidget.setMaximumHeight(150)
        return FallenWidget
    elif FallenID == "Submission":
        FallenWidget = QWidget()
        FallenWidget.setStyleSheet('''
        QWidget{
        background-color:rgb(23,23,23)
        }
        QLabel{
        background-color:rgb(23,23,23)
        }
        ''')

        Label = QLabel(FallenWidget)
        Label.setGeometry(0,0,200,150)
        Text = f'''<strong>Affection: </strong><br/>{check(Reliability,1000)}SubmissionExp: 1000</Font><br/> {check(Attraction,300)}ServiceExp: 300</Font><br/>'''
        Label.setText(Text)
        Label.setFont(QFont('Segoe UI', 12))
        Label.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)


        FallenWidget.setMinimumWidth(200)
        FallenWidget.setMaximumWidth(200)
        FallenWidget.setMinimumHeight(150)
        FallenWidget.setMaximumHeight(150)
        return FallenWidget
    return None


def GetMoveButtons(self, Location, PCID):
    def BG(Location, PCID):
        try:
            Globals.References["SoLFunctions"].Move(Globals.Layouts["SoLUI"], Location, PCID)
            self.MoveButtons = 0
        except Exception as e:
            Log(3, "ERROR MOVE COMMAND", e, Location)
    Button = QPushButton(clicked = lambda: BG(Location, PCID))
    Text = Globals.SoLEnviorementData["Locations"][Location]["Name"]
    Button.setText(Text)
    Button.setMinimumWidth(165)
    Button.setMinimumHeight(35)
    Button.setMaximumWidth(165)
    Button.setMaximumHeight(35)
    Button.setFont(QFont('Segoe UI', 14))

    Globals.References["SoLFunctions"].CheckButtonFontSize(self, Button)
    return Button

def CheckControlCommandAvailable(self, ControlID, PCID, NPCID, PCLocation):
    if True:
        return 1
def GetContolCommandButton(self, ControlID, PCID, NPCID, PCLocation):
    try:
        if True:
            def BG():
                try:
                    TriggerControlCommand(self, ControlID, PCID, NPCID)
                except Exception as e:
                    Log(3, "ERROR COMMAND EVENT PRESSED", e, ControlID, __name__)
            Button = QPushButton(clicked = lambda: BG())
            Button.setText(ControlID)
            Button.setMinimumWidth(165)
            Button.setMinimumHeight(35)
            Button.setMaximumWidth(165)
            Button.setMaximumHeight(35)
            Button.setFont(QFont('Segoe UI', 14))

            Globals.References["SoLFunctions"].CheckButtonFontSize(self, Button)
            return Button
    except Exception as e:
        Log(3, "ERROR GetCommandButton", e, ControlID, __name__)
def TriggerControlCommand(self, ControlID, PCID, NPCID):
    if ControlID == "Move":
        try:
            MoveButtons = self.MoveButtons
        except:
            MoveButtons = 0

        if MoveButtons == 0:
            self.MoveButtons = 1
            PCID = Globals.SoLPCData["ID"]
            PCLocation = Globals.SoLNPCData[PCID]["Actions"]["CurrentTask"]["Location"]

            for Widget in self.FormSoLButtons.WidgetsList:
                self.FormSoLButtons.removeWidget(Widget)
            self.FormSoLButtons.WidgetsList = []

            Layer, Row = 0, 0
            for Location in Globals.SoLEnviorementData["Locations"][PCLocation]["CanAccess"]:
                Button = GetMoveButtons(self, Location, PCID)
                if Row > 4:
                    Row = 0
                    Layer += 1
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
        else:
            self.MoveButtons = 0
            Globals.References["SoLFunctions"].Refresh(self)



    elif ControlID == "Back to Menu":
        Globals.Layouts["MainF"].gotoLayout("MainMenuUI")
    elif ControlID == "Quick Save":
        Globals.CurrentSession["SoLNPCData"] = Globals.SoLNPCData
        Globals.CurrentSession["SoLPCData"] = Globals.SoLPCData
        Globals.CurrentSession["SoLTempData"] = Globals.SoLTempData
        Globals.CurrentSession["SoLOtherData"] = Globals.SoLOtherData
        Globals.CurrentSession["SoLEnviorementData"] = Globals.SoLEnviorementData
        Globals.CurrentSession["SoLNPCSchedules"] = Globals.SoLNPCSchedules
        Globals.CurrentSession["SoLFlavorDict"] = Globals.SoLFlavorDict
        with open('CurrentSession.json', 'w') as f:
            json.dump(Globals.CurrentSession, f)
    else:
        print(ControlID)
