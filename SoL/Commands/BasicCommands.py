
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import Globals

Log = Globals.Layouts["MainF"].Log

def GetCommands(self, Reference):
    CommandsList = ["Conversation0", "Skinship0", "ServeThem0", "GetLapPillow0", "GiveLapPillow0", "BellyCaress0", "PinchCheek0", "ButtCaress0", "Hug0", "Kiss0", "BreastCaress0", "AnalCaress0", "PussyCaress0", "PenisCaress0", "ServeAlcohol0", "PushDown0", "GetFollow0"]
    CommandsList +=["CaressSex0", "GetCaressSex0", "PussyCaressSex0", "GetPussyCaressSex0", "FingeringSex0", "GetFingeringSex0", "CunnilingusSex0", "GetCunnilingusSex0", "PenissCaressSex0", "GetPenisCaressSex0", "HandJobSex0", "GetHandjobSex0", "BlowjobSex0", "GetBlowjobSex0", "BreastCaressSex0", "GetBreastCaressSex0", "NippleTeaseSex0", "GetNippleTeaseSex0", "NippleSuckingSex0", "GetNippleSuckingSex0", "AnalCaressSex0", "GetAnalCaressSex0", "AnalFingeringSex0", "GetAnalFingeringSex0", "RimjobSex0", "GetRimjobSex0", "MasturbateSex0", "GetMasturbateSex0", "AMasturbateSex0", "GetAMasturbateSex0", "ThighjobSex0", "GetThighjobSex0", "FootjobSex0", "GetFootjobSex0", "TitjobSex0", "GetTitjobSex0", "ButtjonbSex0", "GetButtjobSex0", "FacesittingSex0", "GetFacesittingSex0", "AFacesittingSex0", "GetAFacesittingSex0", "AssSpankingSex0", "GetAssSpankingSex0", "BreastSlappingSex0", "GetBreastSlappingSex0", "MissionarySex0", "GetMissionarySex0", "DoggyStyleSex0", "GetDoggyStyleSex0", "CowgirlSex0", "GetCowgirlSex0", "LotusSex0", "GetLotusSex0", "AMissionarySex0", "GetAMissionarySex0", "ADoggyStyleSex0", "GetADoggyStyleSex0", "ACowgirlSex0", "GetACowgirlSex0", "ALotusSex0", "GetALotusSex0", "StopSex0"]

    # CommandsList = ["Conversation0"]
    for CommandID in CommandsList:
        Globals.Commands[CommandID] = {"ID":CommandID, "Reference":Reference, "OtherData":{}}

def CheckCommandAvailable(self, CommandID, Actor, Target):
    try:
        Status = 0
        TVTightness = Globals.SoLNPCData[Target]["BodyData"]["VTightness"]
        TPenisSize = Globals.SoLNPCData[Target]["BodyData"]["PenisSize"]
        TATightness = Globals.SoLNPCData[Target]["BodyData"]["ATightness"]
        AVTightness = Globals.SoLNPCData[Actor]["BodyData"]["VTightness"]
        APenisSize = Globals.SoLNPCData[Actor]["BodyData"]["PenisSize"]
        AATightness = Globals.SoLNPCData[Actor]["BodyData"]["ATightness"]

        if Target != None and Target not in Globals.SoLNPCData[Actor]["Actions"]["isInSexScene"]:
            if CommandID == "Conversation0":
                Status = 1
            elif CommandID == "Skinship0":
                Status = 1
            elif CommandID == "ServeThem0":
                Status = 1
            elif CommandID == "GetLapPillow0":
                if Globals.SoLNPCData[Actor]["BodyData"]["Height"] - Globals.SoLNPCData[Target]["BodyData"]["Height"] <= 4 : Status = 1
            elif CommandID == "GiveLapPillow0":
                if Globals.SoLNPCData[Target]["BodyData"]["Height"] - Globals.SoLNPCData[Actor]["BodyData"]["Height"] <= 4 : Status = 1
            elif CommandID == "BellyCaress0":
                Status = 1
            elif CommandID == "PinchCheek0":
                Status = 1
            elif CommandID == "ButtCaress0":
                Status = 1
            elif CommandID == "Hug0":
                Status = 1
            elif CommandID == "Kiss0":
                Status = 1
            elif CommandID == "BreastCaress0":
                Status = 1
            elif CommandID == "AnalCaress0":
                Status = 1
            elif CommandID == "PussyCaress0":
                if TVTightness > 0: Status = 1
            elif CommandID == "PenisCaress0":
                if TPenisSize > 0: Status = 1
            elif CommandID == "ServeAlcohol0":
                return Status
                if  "Alcohol" in Globals.SoLNPCData[Actor]["Items"] and Globals.SoLNPCData[Actor]["Items"]["Alcohol"] > 0: Status = 1
            elif CommandID == "PushDown0":
                Status = 1
            elif CommandID == "GetFollow0":
                Status = 1
            # if Globals.SoLNPCData[Target]["isInSexScene"] and Globals.SoLNPCData[Actor]["isInSexScene"]:
        elif Target != None and Target in Globals.SoLNPCData[Actor]["Actions"]["isInSexScene"]:
            if CommandID == "CaressSex0":
                Status = 1
            elif CommandID == "GetCaressSex0":
                Status = 1

            elif CommandID == "PussyCaressSex0":
                if TVTightness > 0: Status = 1
            elif CommandID == "GetPussyCaressSex0":
                if AVTightness > 0: Status = 1
            elif CommandID == "FingeringSex0":
                if TVTightness > 0: Status = 1
            elif CommandID == "GetFingeringSex0":
                if AVTightness > 0: Status = 1
            elif CommandID == "CunnilingusSex0":
                if TVTightness > 0: Status = 1
            elif CommandID == "GetCunnilingusSex0":
                if AVTightness > 0: Status = 1

            elif CommandID == "PenisCaressSex0":
                if TPenisSize > 0: Status = 1
            elif CommandID == "GetPenisCaressSex0":
                if APenisSize > 0: Status = 1
            elif CommandID == "HandJobSex0":
                if TPenisSize > 0: Status = 1
            elif CommandID == "GetHandjobSex0":
                if APenisSize > 0: Status = 1
            elif CommandID == "BlowjobSex0":
                if TPenisSize > 0: Status = 1
            elif CommandID == "GetBlowjobSex0":
                if APenisSize > 0: Status = 1

            elif CommandID == "BreastCaressSex0":
                Status = 1
            elif CommandID == "GetBreastCaressSex0":
                Status = 1
            elif CommandID == "NippleTeaseSex0":
                Status = 1
            elif CommandID == "GetNippleTeaseSex0":
                Status = 1
            elif CommandID == "NippleSuckingSex0":
                Status = 1
            elif CommandID == "GetNippleSuckingSex0":
                Status = 1

            elif CommandID == "AnalCaressSex0":
                Status = 1
            elif CommandID == "GetAnalCaressSex0":
                Status = 1
            elif CommandID == "AnalFingeringSex0":
                Status = 1
            elif CommandID == "GetAnalFingeringSex0":
                Status = 1
            elif CommandID == "RimjobSex0":
                Status = 1
            elif CommandID == "GetRimjobSex0":
                Status = 1

            elif CommandID == "MasturbateSex0":
                Status = 1
            elif CommandID == "GetMasturbateSex0":
                Status = 1
            elif CommandID == "AMasturbateSex0":
                Status = 1
            elif CommandID == "GetAMasturbateSex0":
                Status = 1

            elif CommandID == "FootjobSex0":
                if TPenisSize > 0 or TVTightness > 0: Status = 1
            elif CommandID == "GetFootjobSex0":
                if APenisSize > 0 or AVTightness > 0: Status = 1
            elif CommandID == "ButtjonbSex0":
                if TPenisSize > 0: Status = 1
            elif CommandID == "GetButtjonbSex0":
                if APenisSize > 0: Status = 1
            elif CommandID == "ThighjobSex0":
                if TPenisSize > 0: Status = 1
            elif CommandID == "GetThighjobSex0":
                if APenisSize > 0: Status = 1
            elif CommandID == "TitjobSex0":
                if TPenisSize > 0: Status = 1
            elif CommandID == "GetTitjobSex0":
                if APenisSize > 0: Status = 1

            elif CommandID == "FacesittingSex0":
                if AVTightness > 0: Status = 1
            elif CommandID == "GetFacesittingSex0":
                if TVTightness > 0: Status = 1
            elif CommandID == "AFacesittingSex0":
                if AATightness > 0: Status = 1
            elif CommandID == "GetAFacesittingSex0":
                if TATightness > 0: Status = 1

            elif CommandID == "AssSpankingSex0":
                Status = 1
            elif CommandID == "GetAssSpankingSex0":
                Status = 1
            elif CommandID == "BreastSlappingSex0":
                Status = 1
            elif CommandID == "GetBreastSlappingSex0":
                Status = 1

            elif CommandID == "MissionarySex0":
                if TVTightness > 0 and APenisSize > 0: Status = 1
            elif CommandID == "GetMissionarySex0":
                if AVTightness > 0 and TPenisSize > 0: Status = 1
            elif CommandID == "DoggyStyleSex0":
                if TVTightness > 0 and APenisSize > 0: Status = 1
            elif CommandID == "GetDoggyStyleSex0":
                if AVTightness > 0 and TPenisSize > 0: Status = 1
            elif CommandID == "GetCowgirlSex0":
                if TVTightness > 0 and APenisSize > 0: Status = 1
            elif CommandID == "CowgirlSex0":
                if AVTightness > 0 and TPenisSize > 0: Status = 1
            elif CommandID == "LotusSex0":
                if TVTightness > 0 and APenisSize > 0: Status = 1
            elif CommandID == "GetLotusSex0":
                if AVTightness > 0 and TPenisSize > 0: Status = 1

            elif CommandID == "AMissionarySex0":
                if APenisSize > 0: Status = 1
            elif CommandID == "GetAMissionarySex0":
                if TPenisSize > 0: Status = 1
            elif CommandID == "ADoggyStyleSex0":
                if APenisSize > 0: Status = 1
            elif CommandID == "GetADoggyStyleSex0":
                if TPenisSize > 0: Status = 1
            elif CommandID == "GetCowgirlSex0":
                if APenisSize > 0: Status = 1
            elif CommandID == "CowgirlSex0":
                if TPenisSize > 0: Status = 1
            elif CommandID == "LotusSex0":
                if APenisSize > 0: Status = 1
            elif CommandID == "GetALotusSex0":
                if TPenisSize > 0: Status = 1
            elif CommandID == "StopSex0":
                Status = 1

        # Globals.SignalData["CommandCheckSignal"]["CommandID"] = CommandID
        # Globals.SignalData["CommandCheckSignal"]["Status"] = Status
        # Globals.SignalData["CommandCheckSignal"]["Actor"] = Actor
        # Globals.SignalData["CommandCheckSignal"]["Target"] = Target
        # self.CommandCheckSignal.emit()
        # # CommandID = Globals.SignalData["CommandCheckSignal"]["CommandID"]
        # Status = Globals.SignalData["CommandCheckSignal"]["Status"]
        # # Actor = Globals.SignalData["CommandCheckSignal"]["Actor"]
        # # Target = Globals.SignalData["CommandCheckSignal"]["Target"]
        return Status

    except Exception as e:
        if Target != None:
            Log(2, "ERROR CHECK COMMAND AVAILABLE", e, CommandID, Actor, Target)
        return 0

def GetCommandButton(self, CommandID, PCID, NPCID):
    try:
        def GetText(CommandID):
            if CommandID == "Conversation0": Text = "Talk"
            elif CommandID == "Skinship0": Text = "Skinship"
            elif CommandID == "ServeThem0": Text = "ServeThem"
            elif CommandID == "GetLapPillow0": Text = "Get Lap Pillow"
            elif CommandID == "GiveLapPillow0": Text = "Give Lap Pillow"
            elif CommandID == "BellyCaress0": Text = "Belly Caress"
            elif CommandID == "PinchCheek0": Text = "Pinch Cheek"
            elif CommandID == "ButtCaress0": Text = "Butt Caress"
            elif CommandID == "Hug0": Text = "Hug"
            elif CommandID == "Kiss0": Text = "Kiss"
            elif CommandID == "BreastCaress0": Text = "Breasts Caress"
            elif CommandID == "AnalCaress0": Text = "Anal Caress"
            elif CommandID == "PussyCaress0": Text = "Pussy Caress"
            elif CommandID == "PenisCaress0": Text = "Penis Caress"
            elif CommandID == "ServeAlcohol0": Text = "Serve Alcohol"
            elif CommandID == "PushDown0": Text = "Push Down"
            elif CommandID == "GetFollow0": Text = "Ask to Follow"

            elif CommandID == "CaressSex0": Text = "Caress"
            elif CommandID == "GetCaressSex0": Text = "Get Caress"
            elif CommandID == "PussyCaressSex0": Text = "Pussy Caress"
            elif CommandID == "GetPussyCaressSex0": Text = "Get Pussy Caress"
            elif CommandID == "FingeringSex0": Text = "Fingering"
            elif CommandID == "GetFingeringSex0": Text = "Get Fingering"
            elif CommandID == "PenissCaressSex0": Text = "Penis Caress"
            elif CommandID == "GetPenisCaressSex0": Text = "Get Penis Caress"
            elif CommandID == "HandJobSex0": Text = "Handjob"
            elif CommandID == "GetHandjobSex0": Text = "Get HandJob"
            elif CommandID == "BreastCaressSex0": Text = "Breasts Caress"
            elif CommandID == "GetBreastCaressSex0": Text = "Get Breasts Caress"
            elif CommandID == "NippleTeaseSex0": Text = "Nipple Tease"
            elif CommandID == "GetNippleTeaseSex0": Text = "Get Nipple Tease"
            elif CommandID == "TitjobSex0": Text = "Titjob"
            elif CommandID == "GetTitjobSex0": Text = "Get Titjob"
            elif CommandID == "NippleSuckingSex0": Text = "Nipple Sucking"
            elif CommandID == "GetNippleSuckingSex0": Text = "Get Nipple Sucking"
            elif CommandID == "MasturbateSex0": Text = "Masturbate"
            elif CommandID == "GetMasturbateSex0": Text = "Ask to Masturbate"
            elif CommandID == "AMasturbateSex0": Text = "Anal Masturbate"
            elif CommandID == "GetAMasturbateSex0": Text = "Ask to Anal Masturbate"
            elif CommandID == "CunnilingusSex0": Text = "Cunnilingus"
            elif CommandID == "GetCunnilingusSex0": Text = "Get Cunnilingus"
            elif CommandID == "BlowjobSex0": Text = "Blowjob"
            elif CommandID == "GetBlowjobSex0": Text = "Get Blowjob"
            elif CommandID == "RimjobSex0": Text = "Rimjob"
            elif CommandID == "GetRimjobSex0": Text = "Get Rimjob"
            elif CommandID == "ThighjobSex0": Text = "Thighjob"
            elif CommandID == "GetThighjobSex0": Text = "Get Thigjob"
            elif CommandID == "FootjobSex0": Text = "Footjob"
            elif CommandID == "GetFootjobSex0": Text = "Get Footjob"
            elif CommandID == "ButtjonbSex0": Text = "Buttjob"
            elif CommandID == "GetButtjobSex0": Text = "Get Buttjob"
            elif CommandID == "FacesittingSex0": Text = "Facesitting"
            elif CommandID == "GetFacesittingSex0": Text = "Get Facesitting"
            elif CommandID == "AFacesittingSex0": Text = "Anal Facesitting"
            elif CommandID == "GetAFacesittingSex0": Text = "Get Anal Facesitting"
            elif CommandID == "AssSpankingSex0": Text = "Ass Spanking"
            elif CommandID == "GetAssSpankingSex0": Text = "Get Ass Spanking"
            elif CommandID == "BreastSlappingSex0": Text = "Breasts Spanking"
            elif CommandID == "GetBreastSlappingSex0": Text = "Get Breasts Spanking"
            elif CommandID == "MissionarySex0": Text = "Missionary"
            elif CommandID == "GetMissionarySex0": Text = "Get Missionary"
            elif CommandID == "DoggyStyleSex0": Text = "Doggy Style"
            elif CommandID == "GetDoggyStyleSex0": Text = "Get DoggyStyle"
            elif CommandID == "CowgirlSex0": Text = "Cowgirl"
            elif CommandID == "GetCowgirlSex0": Text = "Get Cowgirl"
            elif CommandID == "LotusSex0": Text = "Lotus"
            elif CommandID == "GetLotusSex0": Text = "Get Lotus"
            elif CommandID == "AMissionarySex0": Text = "Anal Missionary"
            elif CommandID == "GetAMissionarySex0": Text = "Get Anal Missionary"
            elif CommandID == "ADoggyStyleSex0": Text = "Anal DoggyStyle"
            elif CommandID == "GetADoggyStyleSex0": Text = "Get Anal DoggyStyle"
            elif CommandID == "ACowgirlSex0": Text = "Give Anal Cowgirl"
            elif CommandID == "GetACowgirlSex0": Text = "Anal Cowgirl"
            elif CommandID == "ALotusSex0": Text = "Anal Lotus"
            elif CommandID == "GetALotusSex0": Text = "Get Anal Lotus"
            else: Text = CommandID
            return Text

        # if CommandID == "Caress0":
        if True:
            def BG():
                try:
                    TriggerCommand(self, CommandID, NPCID, PCID, None)
                    # Globals.References["SoLFunctions"].Refresh(self)
                except Exception as e:
                    Log(3, "ERROR COMMAND PRESSED", e, CommandID, __name__)
            Button = QPushButton(clicked = lambda: BG())
            Text = GetText(CommandID)
            Button.setText(Text)
            Button.setMinimumWidth(165)
            Button.setMinimumHeight(35)
            Button.setMaximumWidth(165)
            Button.setMaximumHeight(35)
            Button.setFont(QFont('Segoe UI', 14))

            Globals.References["SoLFunctions"].CheckButtonFontSize(self, Button)
            return Button
    except Exception as e:
        Log(3, "ERROR GetCommandButton", e, CommandID, __name__)

def TriggerCommand(self, CommandID, Target, Actor, Modification):
    try:
        # TVC / Text Values Connotations
        Implementation = ''

        # # CTS 1 SGINAL
        # Data = Globals.SignalData["CTS1"]["Values"]
        # Data["CommandID"], Data["Target"], Data["Actor"] = CommandID, Target, Actor
        Globals.SignalData["CTS1"] = { "Values":{ "CommandID":CommandID, "Target":Target, "Actor":Actor } }
        Globals.References["SoLFunctions"].Emit("CTS1")
        CommandID, Target, Actor = Globals.SignalData["CTS1"]["Values"]["CommandID"], Globals.SignalData["CTS1"]["Values"]["Target"], Globals.SignalData["CTS1"]["Values"]["Actor"]
        # self.CTS1.emit()
        # CommandID, Target, Actor = Data["CommandID"], Data["Target"], Data["Actor"]
        # #

        Desc = Globals.References["SoLFunctions"].GetDescription
        TargetDict, ActorDict = {}, {}
        DateData = Globals.SoLEnviorementData["DateData"]
        TargetData = Globals.SoLNPCData[Target]
        ActorData = Globals.SoLNPCData[Actor]
        TName = Globals.SoLNPCData[Target]["Name"]
        AName = Globals.SoLNPCData[Actor]["Name"]
        TPSub, TPObj, TPPos, TPIPos = Globals.SoLNPCData[Target]["BodyData"]["Pronouns"]["PSub"].lower(), Globals.SoLNPCData[Target]["BodyData"]["Pronouns"]["PObj"].lower(), Globals.SoLNPCData[Target]["BodyData"]["Pronouns"]["PPos"].lower(), Globals.SoLNPCData[Target]["BodyData"]["Pronouns"]["PIPos"].lower()
        APSub, APObj, APPos, APIPos = Globals.SoLNPCData[Actor]["BodyData"]["Pronouns"]["PSub"].lower(), Globals.SoLNPCData[Actor]["BodyData"]["Pronouns"]["PObj"].lower(), Globals.SoLNPCData[Actor]["BodyData"]["Pronouns"]["PPos"].lower(), Globals.SoLNPCData[Actor]["BodyData"]["Pronouns"]["PIPos"].lower()
        # TPSub = She He
        # TPObj = Her Him
        # TPPos = Her His
        # TPIPos = Hers His

        if CommandID == "Conversation0":
            TargetDict = {
                "State":{
                    "Mood": 3,
                    "Energy": -5,
                    },
                "Temporal":{
                    "Favor": 5,
                    },
                "Permanent":{
                    "SpeechExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Conversation", {"BriefFluff": f'''Listening to {AName}.''', "LongFluff": f'''{TName} is listening to {AName} talk.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Conversation", {"BriefFluff": f'''Bored listening to {AName}''', "LongFluff": f'''{TName} is unninteresed with {AName}'s conversation.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Conversation", {"BriefFluff": f'''Tiredly listening to {AName}.''', "LongFluff": f'''{TName} is tiredly trying to listen to {AName} talk.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":-20,
                }
            ActorDict = {
                "State":{
                    "Energy": -5,
                    },
                "Temporal":{
                    },
                "Permanent":{
                    "SpeechExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Conversation", {"BriefFluff": f'''Talking with {TName}.''', "LongFluff": f'''{AName} is talking with {TName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Conversation", {"BriefFluff": f'''Fails to talk with {TName}.''', "LongFluff": f'''{AName} is failing to talk with {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Conversation", {"BriefFluff": f'''Tiredly talking with {TName}.''', "LongFluff": f'''{AName} is tiredly talking with {TName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                },
                "Connotations":{},
                "Resistance":0,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "Skinship0":
            TargetDict = {
                "State":{
                    "Mood": 1,
                    "Energy": -10,
                    "Excitement": 1,
                    },
                "Temporal":{
                    "Favor": 10,
                    "Submission":2,
                    "Shame":2,
                    "Discomfort": 5,
                    },
                "Permanent":{
                    "Attraction": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Playing with {AName}.''', "LongFluff": f'''{TName} is messing around with {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting {AName}'s attempt of playing.''', "LongFluff": f'''{TName} resists {AName}'s attempts of messing around.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Tries to keep up with {AName}'s playing.''', "LongFluff": f'''{TName} doesn't have enough energy to keep up with {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":-10,
                }
            ActorDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 2,
                    },
                "Temporal":{
                    "Shame":2,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Playing with {TName}.''', "LongFluff": f'''{AName} is messing around with {TName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Actor]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Fails to play with {TName}.''', "LongFluff": f'''{AName} attempts to play with {TName} but fails to do it.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Actor]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Tries to play with {TName}.''', "LongFluff": f'''{AName} attempts to play with {TName} but doesn't have the energy.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Actor]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":0,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "ServeThem0":
            TargetDict = {
                "State":{
                    "Mood": 4,
                    "Energy": 5,
                    },
                "Temporal":{
                    "Favor": 10,
                    "Superiority": 3,
                    },
                "Permanent":{
                    "Reliability": 2,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Being cared by {AName}.''', "LongFluff": f'''{TName} is being cared and serviced by {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Rejecting {AName}'s care.''', "LongFluff": f'''{TName} is recjecting any attempt to be serviced by {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to keep up with {AName}'s care. ''', "LongFluff": f'''{TName} is trying to keep up with {AName}'s servicing.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":5,
                }
            ActorDict = {
                "State":{
                    "Energy": -20,
                    },
                "Temporal":{
                    "Submission":2,
                    "Discomfort": 2,
                    },
                "Permanent":{
                    "ServiceExp":2,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Servicing {TName}.''', "LongFluff": f'''{AName} is caring and servicing for {TName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Actor]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Forcing {APObj}self to service {TName}.''', "LongFluff": f'''{AName} is trying to force {APObj}self to care and service {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Actor]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to servcie {TName}.''', "LongFluff": f'''{AName} is trying to keep up servicing and caring for {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Actor]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":15,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetLapPillow0":
            TargetDict = {
                "State":{
                    "Energy": -10,
                    },
                "Temporal":{
                    "Obedience": 5,
                    "Shame":5,
                    "Discomfort": 10,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "ServiceExp":1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Giving a lap pillow to {AName}.''', "LongFluff": f'''{TName} is letting {AName} use {TPPos} lap to rest {APPos} head.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Rejecting giving {AName} a lap pillow.''', "LongFluff": f'''{TName} rejects giving a lap pillow to {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to give {AName} a lap pillow.''', "LongFluff": f'''{TName} tries to focus on giving {AName} a lap pillow.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":20,
                }
            ActorDict = {
                "State":{
                    "Mood": 3,
                    "Energy": 5,
                    },
                "Temporal":{
                    "Favor": 15,
                    "Shame":2,
                    },
                "Permanent":{
                    "Reliability": 2,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting a lap pillow from {TName}.''', "LongFluff": f'''{AName} is resting {APPos} head on {TName}'s lap.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Actor]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Forcing {APObj}self to get a lap pillow from {TName}.''', "LongFluff": f'''{AName} is forcing {APObj}self to get a lap pillow from {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Actor]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to get a lap pillow from {TName}.''', "LongFluff": f'''{AName} is trying to focus and get a lap pillow from {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Actor]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":5,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GiveLapPillow0":
            TargetDict = {
                "State":{
                    "Mood": 3,
                    "Energy": 5,
                    },
                "Temporal":{
                    "Favor": 15,
                    "Submission":0,
                    "Shame":0,
                    "Discomfort": 5,
                    },
                "Permanent":{
                    "Attraction": 0,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Receiving a lap pillow from {AName}.''', "LongFluff": f'''{TName} is resting {TPPos} head on {AName}'s lap.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting Receiving a lap pillow from {AName}.''', "LongFluff": f'''{TName} is rejecting {AName}'s offer for a lap pillow.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to Receive a lap pillow from {AName}.''', "LongFluff": f'''{TName} is trying to focus on Receiving a lap pillow from {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":15,
                }
            ActorDict = {
                "State":{
                    "Energy": -10,
                    },
                "Temporal":{
                    "Superiority": 5,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Gving a lap pillow to {TName} ''', "LongFluff": f'''{AName} is giving a lap pillow to {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Actor]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Forcing {APObj}self to give {TName} a lap pillow.''', "LongFluff": f'''{AName} is trying to foce {APObj}self to give {TName} a lap pillow.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Actor]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to give {TName} a lap pillow.''', "LongFluff": f'''{AName} is trying to focus {APObj}self on giving {TName} a lap pillow.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Actor]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":0,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "BellyCaress0":
            TargetDict = {
                "State":{
                    "Energy": -5,
                    "Excitement": 2,
                    },
                "Temporal":{
                    "Desire": 3,
                    "Submission":2,
                    "Shame":5,
                    "Discomfort": 10,
                    },
                "Permanent":{
                    "Attraction": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting {TPPos} belly caressed by {AName}.''', "LongFluff": f'''{TName} is having {TPPos} belly caressed '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting {AName}'s attempt to caress {TPPos} belly.''', "LongFluff": f'''{TName} is rejecting {AName}'s attempts at caressing {TPPos} belly.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while {AName} caresses {TPPos} belly.''', "LongFluff": f'''{TName} is trying to focus while {AName} caresses {TPPos} belly.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":15,
                }
            ActorDict = {
                "State":{
                    "Energy": -5,
                    "Excitement": 2,
                    },
                "Temporal":{
                    "Desire": 5,
                    "Superiority": 5,
                    },
                "Permanent":{
                    "Attraction": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Caressing {TName}'s belly.''', "LongFluff": f'''{AName} is caressing {TName}'s belly.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Fails to caress {TName}'s belly.''', "LongFluff": f'''{AName} fails to caress {TName}'s belly.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Forcing {APObj}self to caress {TName}'s belly.''', "LongFluff": f'''{AName} tries to focus {APObj}self to caress {TName}'s belly.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":5,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "PinchCheek0":
            TargetDict = {
                "State":{
                    "Mood": -1,
                    "Energy": -5,
                    },
                "Temporal":{
                    "Obedience": 5,
                    "Submission": 5,
                    "Shame": 2,
                    "Pain": 3,
                    "Discomfort": 10,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting {TPPos} cheeks pinched by {AName}.''', "LongFluff": f'''{TName} is having {TPPos} cheeks playfully pinched by {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting as {AName} tries to pinch {TPPos} cheeks.''', "LongFluff": f'''{TName} is resisting as {AName} attempts to pinch {TPPos} cheeks.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus as {AName} pinches {TPPos} cheeks.''', "LongFluff": f'''{TName} is trying to focus as {AName} pinches {TPPos} cheeks.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":10,
                }
            ActorDict = {
                "State":{
                    "Energy": -10,
                    },
                "Temporal":{
                    "Superiority": 5,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Pinching {TName}'s cheeks.''', "LongFluff": f'''{AName} is playfully pinching {TName}'s cheeks.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to pinch {TName}'s cheeks.''', "LongFluff": f'''{AName} fails to pinch on {AName}'s cheeks.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Tries to focus on pinching {TName}'s cheeks.''', "LongFluff": f'''{AName} tries to focus while pinching on {TName}'s cheeks.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":5,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "ButtCaress0":
            TargetDict = {
                "State":{
                    "Energy":-15,
                    "Excitement": 3,
                    "Arousal": 2,
                    },
                "Temporal":{
                    "Favor": 5,
                    "Desire": 5,
                    "Submission": 10,
                    "Shame": 10,
                    "Discomfort": 25,
                    },
                "Permanent":{
                    "Attraction": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Letting {AName} caress {TPPos} {Desc("AssSize", TargetData, "P")}.''', "LongFluff": f'''{TName} is letting {AName} caress {TPPos} {Desc("AssSize", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting {AName} trying to caress {TPPos} {Desc("AssSize", TargetData, "P")}.''', "LongFluff": f'''{TName} is resisting as {AName} is trying to caress {TPPos} {Desc("AssSize", TargetData, "P")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus as {AName} caresses {TPPos} {Desc("AssSize", TargetData, "P")}.''', "LongFluff": f'''{TName} is trying to focus while {AName} caresses {TPPos} {Desc("AssSize", TargetData, "P")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":25,
                }
            ActorDict = {
                "State":{
                    "Energy":-15,
                    "Mood": 2,
                    "Excitement": 3,
                    },
                "Temporal":{
                    "Desire": 10,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Caressing {TName}'s {Desc("AssSize", TargetData, "P")}.''', "LongFluff": f'''{AName} is caressing {TName}'s {Desc("AssSize", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to caress {TName}'s {Desc("AssSize", TargetData, "P")}.''', "LongFluff": f'''{AName} failed to try and caress {TName}'s {Desc("AssSize", TargetData, "P")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to caress {TName}'s {Desc("AssSize", TargetData, "P")}.''', "LongFluff": f'''{AName} is trying to focus on caressing {TName}'s {Desc("AssSize", TargetData, "P")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":15,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "Hug0":
            TargetDict = {
                "State":{
                    "Mood": 3,
                    "Energy": -10,
                    },
                "Temporal":{
                    "Favor": 10,
                    "Loyalty": 5,
                    "Discomfort": 10,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "Reliability": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Being hugged by {AName}.''', "LongFluff": f'''{TName} is being hugged by {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting {AName}'s hug.''', "LongFluff": f'''{TName} is resisting as {AName} attempts to hug {TPObj} '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on {AName}'s hug.''', "LongFluff": f'''{TName} is trying to stay focused as {AName} hugs {TPObj},'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":15,
                }
            ActorDict = {
                "State":{
                    "Mood": 3,
                    "Energy": -10,
                    },
                "Temporal":{
                    "Favor": 10,
                    "Loyalty": 5,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "Reliability": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Hugging {TName}''', "LongFluff": f'''{AName} is hugging {TName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to hug {TName}.''', "LongFluff": f'''{AName} fails to hug {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on hugging {TName}.''', "LongFluff": f'''{AName} is trying to focus on hugging {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":10,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "Kiss0":
            TargetDict = {
                "State":{
                    "Energy": -15,
                    "Mood": 5,
                    "Excitement": 4,
                    },
                "Temporal":{
                    "Favor": 15,
                    "Loyalty": 5,
                    "Desire": 5,
                    "Submission": 5,
                    "MPlea": 5,
                    "Discomfort": 25,
                    },
                "Permanent":{
                    "Attraction": 3,
                    "MExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting kissed by {AName}.''', "LongFluff": f'''{TName} is getting kissed by {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resising {AName}'s kiss.''', "LongFluff": f'''{TName} is resisting as {AName} attempts to kiss {TPObj}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on {AName}'s kiss.''', "LongFluff": f'''{TName} is trying to focus as {AName} kisses {TPObj}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":40,
                }
            ActorDict = {
                "State":{
                    "Energy": -15,
                    "Mood": 5,
                    "Excitement": 3,
                    },
                "Temporal":{
                    "Favor": 15,
                    "Loyalty": 5,
                    "Desire": 5,
                    "MPlea": 5,
                    },
                "Permanent":{
                    "Attraction": 2,
                    "MExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Kissing {TName}.''', "LongFluff": f'''{AName} is kissing {TName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to kiss {TName}.''', "LongFluff": f'''{AName} tries but fails to kiss {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Tries to focus on kissint {TName}.''', "LongFluff": f'''{AName} tries to keep {TPPos} focus while kissing {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":30,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "BreastCaress0":
            TargetDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 2,
                    "Arousal": 4,
                    },
                "Temporal":{
                    "Desire": 5,
                    "Submission": 5,
                    "Shame": 5,
                    "CPlea": 5,
                    "Discomfort": 30,
                    },
                "Permanent":{
                    "CExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Having {TPPos} {Desc("ChestSize", TargetData, "P")} caressed by {AName}.''', "LongFluff": f'''{TName} is having {TPPos} {Desc("ChestSize", TargetData, "DSP")} caressed by {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting {AName}'s attempt to caress {TPPos} {Desc("ChestSize", TargetData, "P")}.''', "LongFluff": f'''{TName} resists as {AName} attempts to caress {TPPos} {Desc("ChestSize", TargetData, "P")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus as {AName} caresses {TPPos} {Desc("ChestSize", TargetData, "P")}.''', "LongFluff": f'''{TName} is trying to focus while {AName} is caressing {TPPos} {Desc("ChestSize", TargetData, "P")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":30,
                }
            ActorDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 3,
                    },
                "Temporal":{
                    "Desire": 10,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Caressing {TName}'s {Desc("ChestSize", TargetData, "P")}.''', "LongFluff": f'''{AName} is caressing {TName}'s {Desc("ChestSize", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to caress {TName}'s {Desc("ChestSize", TargetData, "P")}. ''', "LongFluff": f'''{AName} tries to caress {TName}'S {Desc("ChestSize", TargetData, "P")}, but fails to do so.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on caressing {TName}'s {Desc("ChestSize", TargetData, "P")}.''', "LongFluff": f'''[AName] attempts to focuas as {APSub} caresses {TPPos} {Desc("ChestSize", TargetData, "P")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":15,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "AnalCaress0":
            TargetDict = {
                "State":{
                    "Energy": -15,
                    "Excitement": 1,
                    "Arousal": 1,
                    },
                "Temporal":{
                    "Submission": 15,
                    "Shame": 10,
                    "APlea": 3,
                    "Pain": 5,
                    "Discomfort": 40,
                    },
                "Permanent":{
                    "AExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Having {TPPos} {Desc("ATightness", TargetData, "P")} caressed by {AName}.''', "LongFluff": f'''{TName} is having {TPPos} {Desc("ATightness", TargetData, "DSP")} caressed by {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting {AName}'s attempt to caress {TPPos} {Desc("ATightness", TargetData, "P")}.''', "LongFluff": f'''{TName} resists as {AName} attempts to caress {TPPos} {Desc("ATightness", TargetData, "P")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus as {AName} caresses {TPPos} {Desc("ATightness", TargetData, "P")}.''', "LongFluff": f'''{TName} is trying to focus while {AName} is caressing {TPPos} {Desc("ATightness", TargetData, "P")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":40,
                }
            ActorDict = {
                "State":{
                    "Energy": -10,
                    },
                "Temporal":{
                    "Superiority": 5,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Caressing {TName}'s {Desc("ATightness", TargetData, "P")}.''', "LongFluff": f'''{AName} is caressing {TName}'s {Desc("ATightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to caress {TName}'s {Desc("ATightness", TargetData, "P")}. ''', "LongFluff": f'''{AName} tries to caress {TName}'S {Desc("ATightness", TargetData, "P")}, but fails to do so.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on caressing {TName}'s {Desc("ATightness", TargetData, "P")}.''', "LongFluff": f'''[AName] attempts to focuas as {APSub} caresses {TPPos} {Desc("ATightness", TargetData, "P")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":25,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "PussyCaress0":
            TargetDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 3,
                    "Arousal": 5,
                    },
                "Temporal":{
                    "Desire": 10,
                    "Submission": 5,
                    "VPlea": 5,
                    "Discomfort": 35,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "VExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Having {TPPos} {Desc("VTightness", TargetData, "P")} caressed by {AName}''', "LongFluff": f'''{TName} is having {TPPos} {Desc("VTightness", TargetData, "DSP")} caressed by {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting {AName}'s attempt to caress {TPPos} {Desc("VTightness", TargetData, "P")}''', "LongFluff": f'''{TName} resists as {AName} attempts to caress {TPPos} {Desc("VTightness", TargetData, "P")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus as {AName} caresses {TPPos} {Desc("VTightness", TargetData, "P")}.''', "LongFluff": f'''{TName} is trying to focus while {AName} is caressing {TPPos} {Desc("VTightness", TargetData, "P")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":35,
                }
            ActorDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 3,
                    },
                "Temporal":{
                    "Desire": 5,
                    "Superiority": 5,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Caressing {TName}'s {Desc("VTightness", TargetData, "P")}.''', "LongFluff": f'''{AName} is caressing {TName}'s {Desc("VTightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to caress {TName}'s {Desc("VTightness", TargetData, "P")}. ''', "LongFluff": f'''{AName} tries to caress {TName}'S {Desc("VTightness", TargetData, "P")}, but fails to do so.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on caressing {TName}'s {Desc("VTightness", TargetData, "P")}.''', "LongFluff": f'''[AName] attempts to focuas as {APSub} caresses {TPPos} {Desc("VTightness", TargetData, "P")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":20,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "PenisCaress0":
            TargetDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 3,
                    "Arousal": 5,
                    },
                "Temporal":{
                    "Desire": 10,
                    "Submission": 5,
                    "PPlea": 5,
                    "Discomfort": 35,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "PExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Having {TPPos} {Desc("PenisSize", TargetData, "P")} caressed by {AName}.''', "LongFluff": f'''{TName} is having {TPPos} {Desc("PenisSize", TargetData, "DSP")} caressed by {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting {AName}'s attempt to caress {TPPos} {Desc("PenisSize", TargetData, "P")}.''', "LongFluff": f'''{TName} resists as {AName} attempts to caress {TPPos} {Desc("PenisSize", TargetData, "P")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus as {AName} caresses {TPPos} {Desc("PenisSize", TargetData, "P")}.''', "LongFluff": f'''{TName} is trying to focus while {AName} is caressing {TPPos} {Desc("PenisSize", TargetData, "P")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":35,
                }
            ActorDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 3,
                    },
                "Temporal":{
                    "Desire": 5,
                    "Superiority": 5,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Caressing {TName}'s {Desc("PenisSize", TarTargetDataget, "P")}.''', "LongFluff": f'''{AName} is caressing {TName}'s {Desc("PenisSize", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to caress {TName}'s {Desc("PenisSize", TargetData, "P")}. ''', "LongFluff": f'''{AName} tries to caress {TName}'S {Desc("PenisSize", TargetData, "P")}, but fails to do so.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on caressing {TName}'s {Desc("PenisSize", TargetData, "P")}.''', "LongFluff": f'''[AName] attempts to focuas as {APSub} caresses {TPPos} {Desc("PenisSize", TargetData, "P")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":20,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "ServeAlcohol0":
            TargetDict = {
                "State":{
                    "Mood": 2,
                    "Energy": -5,
                    "Intoxication": 15,
                    },
                "Temporal":{
                    "Favor": 10,
                    "Discomfort": 5,
                    },
                "Permanent":{
                    "Reliability": 1,
                    "AlcoholExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Has a drink poured by {AName}.''', "LongFluff": f'''{TName} is sharing a drink with {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Denying a drink by {AName}.''', "LongFluff": f'''{TName} is denying a drink offered by {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on drinking with {AName}.''', "LongFluff": f'''{TName} is trying to focus as {TPSub} shares a drink with {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":15,
                }
            ActorDict = {
                "State":{
                    "Energy": -10,
                    },
                "Temporal":{
                    },
                "Permanent":{
                    "ServiceExp": 0,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Pouring some alcohol for {TName}.''', "LongFluff": f'''{AName} is porung some alcohol for {TName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Fails to share some alcohol with {TName}.''', "LongFluff": f'''{AName} fails to share some alcohol with {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Tries to focus on sharingg alcohol with {TName}.''', "LongFluff": f'''{AName} attempts to focus while serving some alcohol to {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":10,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "PushDown0":
            TargetDict = {
                "State":{
                    "Energy": -5,
                    "Excitement": 10,
                    "Arousal": 10,
                    },
                "Temporal":{
                    "Desire": 15,
                    "Discomfort": 55,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 5,
                    "Task": ["PushedDown", {"BriefFluff": f'''Getting pushed down by {AName}''', "LongFluff": f'''{TName} is getting pushed down by {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 5,
                    "Task": ["PushedDown", {"BriefFluff": f'''Resisting being pushed down by {AName}''', "LongFluff": f'''{TName} is resisting being pushed down by {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 5,
                    "Task": ["PushedDown", {"BriefFluff": f'''Trying to focus as {AName} pushes {TPObj} down''', "LongFluff": f'''{TName} is trying to focus while being pushed down by {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                },
                "Connotations":{},
                "Resistance":55,
                }
            ActorDict = {
                "State":{
                    "Energy": -5,
                    "Excitement": 10,
                    "Arousal": 10,
                    },
                "Temporal":{
                    "Desire": 15,
                    "Discomfort": 55,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 5,
                    "Task": ["PushedDown", {"BriefFluff": f'''Pushing down {TName}''', "LongFluff": f'''{AName} is pushing down {TName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Actor]["Actions"]["CurrentTask"]["Location"],
                },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 5,
                    "Task": ["PushedDown", {"BriefFluff": f'''Trying push down {TName}''', "LongFluff": f'''{AName} is trying to push down {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Actor]["Actions"]["CurrentTask"]["Location"],
                },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 5,
                    "Task": ["PushedDown", {"BriefFluff": f'''Trying to focus on pushing down {TName}''', "LongFluff": f'''{AName} is trying to focus while pushing down {TName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Actor]["Actions"]["CurrentTask"]["Location"],
                },
                "Connotations":{},
                "Resistance":50,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetFollow0":
            TargetDict = {
                "State":{
                    "Energy": -5,
                    },
                "Temporal":{
                    "Discomfort": 10,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 5,
                    "Task": ["PushedDown", {"BriefFluff": f'''Starting to follow {AName}''', "LongFluff": f'''{TName} is starting to follow {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 5,
                    "Task": ["PushedDown", {"BriefFluff": f'''Refusing to follow {AName}''', "LongFluff": f'''{TName} is refusing to follow {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 5,
                    "Task": ["PushedDown", {"BriefFluff": f'''Trying to focus on following {AName}''', "LongFluff": f'''{TName} is trying to focus while following {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                },
                "Connotations":{},
                "Resistance":-5,
                }
            ActorDict = {
                "State":{
                    "Energy": -5,
                    "Excitement": 10,
                    "Arousal": 10,
                    },
                "Temporal":{
                    "Desire": 15,
                    "Discomfort": 55,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 5,
                    "Task": ["PushedDown", {"BriefFluff": f'''Getting {TName} to follow {APObj}''', "LongFluff": f'''{AName} is getting {TName} to follow {APObj}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Actor]["Actions"]["CurrentTask"]["Location"],
                },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 5,
                    "Task": ["PushedDown", {"BriefFluff": f'''Failing to get {TName} to follow {APObj}''', "LongFluff": f'''{AName} is trying and failing to get {TName} to follow {APObj}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Actor]["Actions"]["CurrentTask"]["Location"],
                },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 5,
                    "Task": ["PushedDown", {"BriefFluff": f'''Tiredly makiing {TName} follow {APObj}''', "LongFluff": f'''{AName} is tiredly making {TName} follow {APObj}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Actor]["Actions"]["CurrentTask"]["Location"],
                },
                "Connotations":{},
                "Resistance":-5,
                }
            OtherData = {
                "Success":2,
                }


        elif CommandID == "CaressSex0":
            TargetDict = {
                "State":{
                    "Energy": -15,
                    "Arousal": 5,
                    },
                "Temporal":{
                    "Favor": 10,
                    "Desire": 10,
                    "CPlea": 5,
                    "Discomfort": 30,
                    },
                "Permanent":{
                    "Attraction": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Being caressed by {AName}''', "LongFluff": f'''{TName} is being caressed by {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting being caressed by {AName}''', "LongFluff": f'''{TName} is resisting being caressed by {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on {AName}'s caressing.''', "LongFluff": f'''{TName} is trying to focus while being caressed by {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":30,
                }
            if Globals.SoLNPCData[Target]["BodyData"]["VTightness"] >= 1:
                TargetDict["Temporal"]["VPlea"] = 5
                TargetDict["Connotations"]["V"] = [1,5]
            if Globals.SoLNPCData[Target]["BodyData"]["PenisSize"] >= 1:
                TargetDict["Temporal"]["PPlea"] = 5
                TargetDict["Connotations"]["P"] = [1,5]
            ActorDict = {
                "State":{
                    "Energy": -15,
                    "Excitement": 2,
                    },
                "Temporal":{
                    "Service":10,
                    },
                "Permanent":{
                    "ServiceExp": 1,
                    "CaressExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Caressing {TName}''', "LongFluff": f'''{AName} is caressing {TName}'s body.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Refusing to caress {TName} ''', "LongFluff": f'''{AName} is refusing to caress {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus and caress {TName}.''', "LongFluff": f'''{AName} is trying to focus on caressing {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":15,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetCaressSex0":
            TargetDict = {
                "State":{
                    "Energy": -15,
                    "Excitement": 2,
                    },
                "Temporal":{
                    "Obedience": 5,
                    "Submission": 10,
                    "Service": 5,
                    "Shame": 10,
                    "Discomfort": 35,
                    },
                "Permanent":{
                    "ServiceExp": 1,
                    "CaressExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Caressing {AName}''', "LongFluff": f'''{TName} is caressing {AName}'s body at {APPos} request.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Refusing to caress {AName}''', "LongFluff": f'''{TName} is refussing to caress {AName}'s body.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Tiredly caressing {AName}.''', "LongFluff": f'''{TName} is tiredly trying to do as instructed and caress {AName}'s body '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":35,
                }
            ActorDict = {
                "State":{
                    "Mood": 3,
                    "Energy": -15,
                    "Arousal": 5,
                    },
                "Temporal":{
                    "Favor": 10,
                    "Superiority": 10,
                    "CPlea": 5,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting caressed by {TName}.''', "LongFluff": f'''{AName} is getting {APPos} caressed by {TName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to make {TName} caress {APObj}.''', "LongFluff": f'''{AName} is trying to convince {TName} to caress {TPPos} body.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on {TName}'s caress.''', "LongFluff": f'''{AName} is trying to focus while {TName} caresses {APPos} body.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":25,
                }
            if Globals.SoLNPCData[Actor]["BodyData"]["VTightness"] >= 1:
                ActorDict["Temporal"]["VPlea"] = 5
                ActorDict["Connotations"]["V"] = [1,5]
            if Globals.SoLNPCData[Actor]["BodyData"]["PenisSize"] >= 1:
                ActorDict["Temporal"]["PPlea"] = 5
                ActorDict["Connotations"]["P"] = [1,5]
            OtherData = {
                "Success":2,
                }

        elif CommandID == "PussyCaressSex0":
            TargetDict = {
                "State":{
                    "Mood": 2,
                    "Energy": -15,
                    "Excitement": 3,
                    "Arousal": 4,
                    },
                "Temporal":{
                    "Favor": 10,
                    "Desire": 5,
                    "Shame": 5,
                    "VPlea": 10,
                    "Discomfort": 35,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "VExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Having {TPPos} {Desc("VTightness", TargetData, "P")} caressed''', "LongFluff": f'''{TName} is having {TPPos} {Desc("VTightness", TargetData, "DSP")} caressed by {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting {AName}'s attempt to caress {TPPos} {Desc("VTightness", TargetData, "P")}''', "LongFluff": f'''{TName} resists as {AName} attempts to caress {TPPos} {Desc("VTightness", TargetData, "P")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus as {AName} caresses {TPPos} {Desc("VTightness", TargetData, "P")}''', "LongFluff": f'''{TName} is trying to focus while {AName} is caressing {TPPos} {Desc("VTightness", TargetData, "P")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":35,
                }
            ActorDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 3,
                    },
                "Temporal":{
                    "Service":5,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Caressing {TName}'s {Desc("VTightness", TargetData, "P")}''', "LongFluff": f'''{AName} is caressing {TName}'s {Desc("VTightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to caress {TName}'s {Desc("VTightness", TargetData, "P")}''', "LongFluff": f'''{AName} tries to caress {TName}'S {Desc("VTightness", TargetData, "P")}, but fails to do so.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on caressing {TName}'s {Desc("VTightness", TargetData, "P")}''', "LongFluff": f'''{AName} attempts to focuas as {APSub} caresses {TPPos} {Desc("VTightness", TargetData, "P")}'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":25,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetPussyCaressSex0":
            TargetDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 2,
                    },
                "Temporal":{
                    "Submission": 10,
                    "Obedience": 10,
                    "Shame": 10,
                    "Discomfort": 30,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Caressingg {AName}'s {Desc("VTightness", ActorData, "P")}''', "LongFluff": f'''{TName} is caressing {AName}'s {Desc("VTightness", ActorData, "DSP")} after being asked to.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Refusing to caress {AName}'s {Desc("VTightness", ActorData, "P")}''', "LongFluff": f'''{TName} is refusing to caress {AName}'s {Desc("VTightness", ActorData, "DSP")} after being asked to.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus and caress [AName]'s {Desc("VTightness", ActorData, "P")}''', "LongFluff": f'''{TName} is trying to focus while caressing {AName}'s {Desc("VTightness", ActorData, "DSP")} after being asked to.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":30,
                }
            ActorDict = {
                "State":{
                    "Mood": 3,
                    "Energy": -15,
                    "Arousal": 4,
                    },
                "Temporal":{
                    "Superiority": 10,
                    "VPlea": 10,
                    },
                "Permanent":{
                    "VExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Having {TName} caress {APPos} {Desc("VTightness", ActorData, "P")}''', "LongFluff": f'''{AName} is having {APPos} {Desc("VTightness", ActorData, "DSP")} caresed by {TName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to have {TName} caress {APPos} {Desc("VTightness", ActorData, "P")}''', "LongFluff": f'''{AName} is failing to get {TName} to caress {APPos} {Desc("VTightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while {TName} is caressing {APPos} {Desc("VTightness", ActorData, "P")}''', "LongFluff": f'''{AName} is trying to focus while having {AName} caress {APPos} {Desc("VTightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":20,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "FingeringSex0":
            TargetDict = {
                "State":{
                    "Energy": -20,
                    "Arousal": 7,
                    },
                "Temporal":{
                    "Desire": 10,
                    "Shame": 15,
                    "VPlea": 15,
                    "Discomfort": 45,
                    },
                "Permanent":{
                    "Attraction": 2,
                    "VExp": 2,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Being fingered by {AName}''', "LongFluff": f'''{TName} is having {TPPos} {Desc("VTightness", TargetData, "DSP")} fingered by {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting {AName}'s attempts to Finger {TPObj}''', "LongFluff": f'''{TName} is resisting {AName}'s attempts at fingering {TPPos} {Desc("VTightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''{TName} is trying to focus while being fingered''', "LongFluff": f'''{TName} is trying to focus while {AName} fingers {TPPos} {Desc("VTightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":0,
                }
            ActorDict = {
                "State":{
                    "Energy": -15,
                    "Excitement": 2,
                    },
                "Temporal":{
                    "Service":5,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    "ServiceExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Fingering {TName}'s {Desc("VTightness", TargetData, "P")}''', "LongFluff": f'''{AName} is fingering {TName}'s {Desc("VTightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to finger {TName}'s {Desc("VTightness", TargetData, "P")}''', "LongFluff": f'''{TName} is failing to finger {TPPos} {Desc("VTightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on fingering {TName}''', "LongFluff": f'''{AName} is trying to focus on fingering {TName}'s {Desc("VTightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":0,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetFingeringSex0":
            TargetDict = {
                "State":{
                    "Energy": -15,
                    "Excitement": 2,
                    },
                "Temporal":{
                    "Desire": 5,
                    "Obedience": 10,
                    "Submission": 10,
                    "Service": 5,
                    "Shame": 15,
                    "Discomfort": 40,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    "ServiceExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Fingering {AName}'s {Desc("VTightness", ActorData, "P")}''', "LongFluff": f'''{TName} is fingering {AName}'s {Desc("VTightness", ActorData, "DSP")} after being asked to.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Refusing to finger {AName}'s {Desc("VTightness", ActorData, "P")}''', "LongFluff": f'''{TName} is refusinng to finger {AName}'s {Desc("VTightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on fingering {AName}'s {Desc("VTightness", ActorData, "P")}''', "LongFluff": f'''{TName} is trying to focus while fingering {AName}'s {Desc("VTightness", ActorData, "P")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance": 40,
                }
            ActorDict = {
                "State":{
                    "Energy": -20,
                    "Arousal": 7,
                    },
                "Temporal":{
                    "Superiority": 10,
                    "VPlea": 15,
                    },
                "Permanent":{
                    "VExp": 2,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting fingered by {TName}''', "LongFluff": f'''{AName} is getting {APPos} {Desc("VTightness", ActorData, "DSP")} fingered by {TName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to get {TName} to finger {APObj}''', "LongFluff": f'''{AName} is failing to get {TName} to finger {APPos} {Desc("VTightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while {TName} fingers {APObj}''', "LongFluff": f'''{AName} is trying to focus while {TName} fingers {APPos} {Desc("VTightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":30,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "CunnilingusSex0":
            TargetDict = {
                "State":{
                    "Mood": 3,
                    "Energy": -25,
                    "Arousal": 15,
                    },
                "Temporal":{
                    "Favor": 15,
                    "Loyalty": 10,
                    "Desire": 10,
                    "Shame": 10,
                    "VPlea": 15,
                    "Discomfort": 65,
                    },
                "Permanent":{
                    "Attraction": 3,
                    "Reliability": 1,
                    "VExp": 2,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting {TPPos} {Desc("VTightness", TargetData, "P")} eaten''', "LongFluff": f'''{TName} is having {TPPos} {Desc("VTightness", TargetData, "DSP")} eaten by {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Refusing to get {TPPos} {Desc("VTightness", TargetData, "P")} eaten by {AName}''', "LongFluff": f'''{TName} is refusing to have {AName} eat {TPPos} {Desc("VTightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while {AName} eats {TPPos} {Desc("VTightness", TargetData, "P")}''', "LongFluff": f'''{TName} is trying to focus while {AName} eats {TPPos} {Desc("VTightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":65,
                }
            ActorDict = {
                "State":{
                    "Excitement": 3,
                    "Energy": -20,
                    },
                "Temporal":{
                    "Service": 10,
                    },
                "Permanent":{
                    "LickExp": 1,
                    "ServiceExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Eating {TName}'s {Desc("VTightness", TargetData, "P")}.''', "LongFluff": f'''{AName} is eating {TName}'s {Desc("VTightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to eat {TName}'s {Desc("VTightness", TargetData, "P")}''', "LongFluff": f'''{AName} is failing to eat {TName}'s {Desc("VTightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on eating {TName}'s {Desc("VTightness", TargetData, "P")}''', "LongFluff": f'''{AName} is trying to focus on eating {TName}'s {Desc("VTightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":55,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetCunnilingusSex0":
            TargetDict = {
                "State":{
                    "Excitement": 3,
                    "Energy": -20,
                    },
                "Temporal":{
                    "Obedience": 15,
                    "Submission": 10,
                    "Service": 15,
                    "Shame": 20,
                    "Discomfort": 75,
                    },
                "Permanent":{
                    "LickExp": 1,
                    "ServiceExp": 2,

                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Eating {AName}'s {Desc("VTightness", ActorData, "P")}''', "LongFluff": f'''{TName} is eating {AName}'s {Desc("VTightness", ActorData, "DSP")} at {APPos} request.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Refusing to eat {AName}'s {Desc("VTightness", ActorData, "P")}''', "LongFluff": f'''{TName} is refusin to eat {AName}'s {Desc("VTightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on eating {AName}'s {Desc("VTightness", ActorData, "P")}''', "LongFluff": f'''{TName} is trying to focus on eating {AName}'s {Desc("VTightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":75,
                }
            ActorDict = {
                "State":{
                    "Mood": 3,
                    "Energy": -25,
                    "Arousal": 15,
                    },
                "Temporal":{
                    "Favor": 15,
                    "Desire": 10,
                    "Superiority": 10,
                    "VPlea": 15,
                    },
                "Permanent":{
                    "Attraction": 2,
                    "VExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Having {TName} eat {APPos} {Desc("VTightness", ActorData, "P")}''', "LongFluff": f'''{AName} is having {TName} eat {APPos} {Desc("VTightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to get {TName} to eat {APPos} {Desc("VTightness", ActorData, "P")}''', "LongFluff": f'''{AName} is failing to get {TName} to eat {APPos} {Desc("VTightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while {TName} eats {APPos} {Desc("VTightness", ActorData, "P")}''', "LongFluff": f'''{AName} is trying to focus while {TName} eats {APPos} {Desc("VTightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":55,
                }
            OtherData = {
                "Success":2,
                }

        elif CommandID == "PenisCaressSex0":
            TargetDict = {
                "State":{
                    "Mood": 2,
                    "Energy": -15,
                    "Excitement": 3,
                    "Arousal": 4,
                    },
                "Temporal":{
                    "Favor": 10,
                    "Desire": 5,
                    "Shame": 5,
                    "PPlea": 10,
                    "Discomfort": 35,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "PExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Having {TPPos} {Desc("PenisSize", TargetData, "P")} caressed''', "LongFluff": f'''{TName} is having {TPPos} {Desc("PenisSize", TargetData, "DSP")} caressed by {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting having {TPPos} {Desc("PenisSize", TargetData, "P")} caressed.''', "LongFluff": f'''{TName} is resisting {AName}'s attempts at caressing {TPPos} {Desc("PenisSize", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus as {AName} caresses {TPPos} {Desc("PenisSize", TargetData, "P")}''', "LongFluff": f'''{TName} is trying to focus while {AName} caresses {TPPos} {Desc("PenisSize", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":35,
                }
            ActorDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 3,
                    },
                "Temporal":{
                    "Service":5,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Caressing {TName}'s {Desc("PenisSize", TargetData, "P")}''', "LongFluff": f'''{AName} is caressing {TName}'s {Desc("PenisSize", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to caress {TName}'s {Desc("PenisSize", TargetData, "P")}''', "LongFluff": f'''{AName} is attemtpign and failing to caress [TName]'s {Desc("PenisSize", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on caressing {TName}'s {Desc("PenisSize", TargetData, "P")}''', "LongFluff": f'''{AName} is trying to focus on caressing {TName}'s {Desc("PenisSize", TargetData, "DSP")}. '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":25,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetPenisCaressSex0":
            TargetDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 2,
                    },
                "Temporal":{
                    "Submission": 10,
                    "Obedience": 10,
                    "Shame": 10,
                    "Discomfort": 30,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Caressing {AName}'s {Desc("PenisSize", ActorData, "P")}''', "LongFluff": f'''{TName} is caressingg {AName}'s {Desc("PenisSize", ActorData, "DSP")} after being asked to.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Refusing to caress {AName}'s {Desc("PenisSize", ActorData, "P")}.''', "LongFluff": f'''{TName} is refusinng to caress {AName}' {Desc("PenisSize", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on caressingn {AName}'s {Desc("PenisSize", ActorData, "P")} ''', "LongFluff": f'''{TName} is trying to focus on caressing {AName}'s {Desc("PenisSize", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":30,
                }
            ActorDict = {
                "State":{
                    "Mood": 3,
                    "Energy": -15,
                    "Arousal": 4,
                    },
                "Temporal":{
                    "Superiority": 10,
                    "PPlea": 10,
                    },
                "Permanent":{
                    "PExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting {APPos} {Desc("PenisSize", ActorData, "P")}.''', "LongFluff": f'''{AName} is getting {APPos} {Desc("PenisSize", ActorData, "DSP")} caressed by {TName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failign to get {TName} to caress {APPos} {Desc("PenisSize", ActorData, "P")}.''', "LongFluff": f'''{AName} is failing to get {TName} to caress [APPos] {Desc("PenisSize", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus as {TName} caresses {APPos} {Desc("PenisSize", ActorData, "P")}''', "LongFluff": f'''{AName} is trying to focus as {TName} caresses {APPos} {Desc("PenisSize", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":20,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "HandJobSex0":
            TargetDict = {
                "State":{
                    "Energy": -20,
                    "Arousal": 7,
                    },
                "Temporal":{
                    "Desire": 10,
                    "Shame": 15,
                    "PPlea": 15,
                    "Discomfort": 45,
                    },
                "Permanent":{
                    "Attraction": 2,
                    "PExp": 2,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": '''Receiving a handjob''', "LongFluff": f'''{TName} is receiving a handjob by {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": '''Refusing to get a handjob''', "LongFluff": f'''{TName} is refusing to get a handjob by {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": '''Trying to focus while getting a handjob''', "LongFluff": f'''{TName} is trying to focus while getting a handjob by {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":0,
                }
            ActorDict = {
                "State":{
                    "Energy": -15,
                    "Excitement": 2,
                    },
                "Temporal":{
                    "Service":5,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    "ServiceExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Giving a handjob to {TName}''', "LongFluff": f'''{AName} is using {APPos} hands to pleasure {TName}'s {Desc("PenisSize", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to give a handjob to {TName}''', "LongFluff": f'''{AName} is failing to use {APPos} hands to pleasure {TName}'s {Desc("PenisSize", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on giving a handjob to {TName}''', "LongFluff": f'''{AName} is trying to focus while pleasuring {TName}'s {Desc("PenisSize", TargetData, "DSP")} with {APPos} hands.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":0,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetHandjobSex0":
            TargetDict = {
                "State":{
                    "Energy": -15,
                    "Excitement": 2,
                    },
                "Temporal":{
                    "Desire": 5,
                    "Obedience": 10,
                    "Submission": 10,
                    "Service": 5,
                    "Shame": 15,
                    "Discomfort": 40,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    "ServiceExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Giving a handjob to {AName}''', "LongFluff": f'''{TName} is pleasuring {AName}'s {Desc("PenisSize", ActorData, "DSP")} with {TPPos} hands.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Refusing to give a handjob to {AName}''', "LongFluff": f'''{TName} is refusing to give {AName} a handjob.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while giving a handjob to {AName}''', "LongFluff": f'''{TName} is trying to focus while using {TPPos} hands to pleasure {Desc("PenisSize", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance": 40,
                }
            ActorDict = {
                "State":{
                    "Energy": -20,
                    "Arousal": 7,
                    },
                "Temporal":{
                    "Superiority": 10,
                    "PPlea": 15,
                    },
                "Permanent":{
                    "PExp": 2,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting a handjob from {TName}.''', "LongFluff": f'''{AName} is getting a handjob from {TName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": '''Failing to get a handjob''', "LongFluff": f'''{AName} is failing to get a handjob from {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": '''Trying to focus while getting a handjob''', "LongFluff": f'''{AName} is trying to focus while getting a handjob from {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":30,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "BlowjobSex0":
            TargetDict = {
                "State":{
                    "Mood": 3,
                    "Energy": -25,
                    "Arousal": 15,
                    },
                "Temporal":{
                    "Favor": 15,
                    "Loyalty": 10,
                    "Desire": 10,
                    "Shame": 10,
                    "PPlea": 15,
                    "Discomfort": 65,
                    },
                "Permanent":{
                    "Attraction": 3,
                    "Reliability": 1,
                    "PExp": 2,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting {TPPos} {Desc("PenisSize", TargetData, "P")} sucked off. ''', "LongFluff": f'''{TName} is getting {TPPos} {Desc("PenisSize", TargetData, "DSP")} sucked off by {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisiting {AName}'s attempts at giving {TPObj} a blowjob''', "LongFluff": f'''{TName} is resisitngn {AName}'s attempt at giving {TPObj} a blowjob.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": '''Trying to focus while gettingn a blowjob.''', "LongFluff": f'''{TName} is trying to focus while {AName} is sucking off {TPPos} {Desc("PenisSize", TargetData, "DSP")} '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":65,
                }
            ActorDict = {
                "State":{
                    "Excitement": 3,
                    "Energy": -20,
                    },
                "Temporal":{
                    "Service": 10,
                    },
                "Permanent":{
                    "LickExp": 1,
                    "ServiceExp": 1,
                    "MPenetrationExp":1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Giving a blowjob to {TName}.''', "LongFluff": f'''{AName} is sucking off {TName}'s {Desc("PenisSize", TargetData, "DSP")}'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to give a blowjob to {TName}''', "LongFluff": f'''{AName} is failing to give a blowjob to {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while giving a blowjob to {TName}''', "LongFluff": f'''{AName} is trying to focus while giving a blowjob to {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":55,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetBlowjobSex0":
            TargetDict = {
                "State":{
                    "Excitement": 3,
                    "Energy": -20,
                    },
                "Temporal":{
                    "Obedience": 15,
                    "Submission": 10,
                    "Service": 15,
                    "Shame": 20,
                    "Discomfort": 75,
                    },
                "Permanent":{
                    "LickExp": 1,
                    "ServiceExp": 2,
                    "MPenetrationExp":1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Giving a blowjob to {AName}''', "LongFluff": f'''{TName} is sucking off [AName]'s {Desc("PenisSize", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Refusing to give a blowjob to {AName}.''', "LongFluff": f'''{TName} is refusing to give a blowjob to {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while giving a blowjob to {AName}''', "LongFluff": f'''{TName} is trying to focus while sucking off {AName}'s {Desc("PenisSize", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":75,
                }
            ActorDict = {
                "State":{
                    "Mood": 3,
                    "Energy": -25,
                    "Arousal": 15,
                    },
                "Temporal":{
                    "Favor": 15,
                    "Desire": 10,
                    "Superiority": 10,
                    "PPlea": 15,
                    },
                "Permanent":{
                    "Attraction": 2,
                    "PExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting a blowjob from {TName} ''', "LongFluff": f'''{AName} is getting {APPos} {Desc("PenisSize", ActorData, "DSP")} sucked off by {TName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to get a blowjob from {TName} ''', "LongFluff": f'''{AName} is failing to get a blowjob from {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": '''Trying to focus while getting a blowjob''', "LongFluff": f'''{AName} is trying to focus while {AName} is sucking off {APPos} {Desc("PenisSize", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":55,
                }
            OtherData = {
                "Success":2,
                }

        elif CommandID == "BreastCaressSex0":
            TargetDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 3,
                    "Arousal": 3,
                    },
                "Temporal":{
                    "Desire": 5,
                    "Submission": 5,
                    "Shame": 5,
                    "CPlea": 10,
                    "Discomfort": 30,
                    },
                "Permanent":{
                    "CExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting {TPPos} {Desc("ChestSize", TargetData, "P")} caressed''', "LongFluff": f'''{TName} is having {TPPos} {Desc("ChestSize", TargetData, "DSP")} caressed by {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting to have {TPPos} {Desc("ChestSize", TargetData, "P")} caressed.''', "LongFluff": f'''{TName} is reisting {AName}'s attempt at caressing {TPPos} {Desc("ChestSize", TargetData, "DSP")} '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while having {TPPos} {Desc("ChestSize", TargetData, "P")} caressed''', "LongFluff": f'''{TName} is tryingn to focus while {AName} caresses {TPPos} {Desc("ChestSize", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":30,
                }
            ActorDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 3,
                    },
                "Temporal":{
                    },
                "Permanent":{
                    "CaressExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Caresing {TName}'s {Desc("ChestSize", TargetData, "P")}''', "LongFluff": f'''{AName} is caressing {TName}'s {Desc("ChestSize", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to caress {TName}'s {Desc("ChestSize", TargetData, "P")}''', "LongFluff": f'''{AName} is failingn to caress {TName}'s {Desc("ChestSize", TargetData, "DSP")} '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on caressing {TName}'s {Desc("ChestSize", TargetData, "P")}''', "LongFluff": f'''{AName} is trying to focus while caressing {TName}'s {Desc("ChestSize", TargetData, "P")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":20,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetBreastCaressSex0":
            TargetDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 1,
                    },
                "Temporal":{
                    "Obedience": 5,
                    "Shame": 10,
                    "Discomfort": 35,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Caressing {AName}'s {Desc("ChestSize", ActorData, "P")}''', "LongFluff": f'''{TName} is caressing {AName}'s {Desc("ChestSize", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Refusing to caress {AName}'s {Desc("ChestSize", ActorData, "P")}''', "LongFluff": f'''{TName} is refusing to caress {AName}'s {Desc("ChestSize", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on caressing {AName}'s {Desc("ChestSize", ActorData, "P")}''', "LongFluff": f'''{TName} is trying to focus while caressing {AName}'s {Desc("ChestSize", ActorData, "DSP")}. '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":35,
                }
            ActorDict = {
                "State":{
                    "Energy": -15,
                    "Arousal": 3,
                    },
                "Temporal":{
                    "Superiority": 5,
                    "CPlea": 10,
                    },
                "Permanent":{
                    "CExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting {APPos} {Desc("ChestSize", ActorData, "P")} caressed''', "LongFluff": f'''{AName} is having [APPos] {Desc("ChestSize", ActorData, "DSP")} caressed by {TName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to get {TName} to caress {APPos} {Desc("ChestSize", ActorData, "P")}''', "LongFluff": f'''{AName} is failing to get {TName} to caress [APPos] {Desc("ChestSize", ActorData, "DSP")} '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while having {APPos} {Desc("ChestSize", ActorData, "P")} caressed.''', "LongFluff": f'''{AName} is trying to stay focused while {TName} caresses {APPos} {Desc("ChestSize", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":25,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "NippleTeaseSex0":
            TargetDict = {
                "State":{
                    "Energy": -15,
                    "Arousal": 5,
                    },
                "Temporal":{
                    "Submission": 10,
                    "Shame": 10,
                    "CPlea": 15,
                    "Discomfort": 35,
                    },
                "Permanent":{
                    "CExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Having {TPPos} nipples teased.''', "LongFluff": f'''{TName} is having {TPPos} nipples caressed by [AName].'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting having {TPPos} nipples teased''', "LongFluff": f'''{TName} is resisting {AName}'s attempts at teasing {TPPos} nipples.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while having {TPPos} nipples teased.''', "LongFluff": f'''{TName} is trying to focus while {AName} plays with {TPPos} nipples.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":35,
                }
            ActorDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 0,
                    },
                "Temporal":{
                    },
                "Permanent":{
                    "CaressExp": 0,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Teasing {TName}'s nipples ''', "LongFluff": f'''{AName} is playing with {TName}'s nipples.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to tease {TName}'s nipples.''', "LongFluff": f'''{AName} is failing to tease {TName}'s nipples.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on teasing {TName}'s nipples.''', "LongFluff": f'''{AName} is trying to focus while teasing {TName}'s nipples.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":25,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetNippleTeaseSex0":
            TargetDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 1,
                    },
                "Temporal":{
                    "Submission": 5,
                    "Obedience": 3,
                    "Shame": 10,
                    "Discomfort": 40,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Teasing {AName}'s nipples''', "LongFluff": f'''{TName} is playing wiht {AName}'s nipples.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Refusing to tease {AName}'s nipples''', "LongFluff": f'''{TName} is refusing to tease {AName}'s nipples.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on teasing {AName}'s nipples''', "LongFluff": f'''{TName} is trying to focus while teasing [AName]'s nipples.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":40,
                }
            ActorDict = {
                "State":{
                    "Energy": -15,
                    "Arousal": 5,
                    },
                "Temporal":{
                    "Superiority": 10,
                    "CPlea": 15,
                    },
                "Permanent":{
                    "CExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Having {APPos} nippleas teased''', "LongFluff": f'''{AName} is having {APPos} nipples teased by {TName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to get {TName} to tease {APPos} nipples.''', "LongFluff": f'''{AName} is failing to get {TName} to play with {APPos} nipples.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while having {APPos} nipples played with.''', "LongFluff": f'''{AName} is trying to focus while {TName} plays with {APPos} nipples.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":30,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "NippleSuckingSex0":
            TargetDict = {
                "State":{
                    "Energy": -10,
                    "Mood": 1,
                    "Excitement": 1,
                    "Arousal": 7,
                    },
                "Temporal":{
                    "Favor": 5,
                    "Desire": 10,
                    "Shame": 15,
                    "CPlea": 20,
                    "Discomfort": 50,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "CExp": 2,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Having {TPPos} {Desc("ChestSize", TargetData, "P")} sucked''', "LongFluff": f'''{TName} is having {TPPos} {Desc("ChestSize", TargetData, "DSP")} sucked.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting {AName}'s attempts at sucking on {TPPos} {Desc("ChestSize", TargetData, "P")}''', "LongFluff": f'''{TName} is refusing {AName}'s attempts at sucking on her {Desc("ChestSize", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while having {TPPos} {Desc("ChestSize", TargetData, "P")} sucked''', "LongFluff": f'''{TName} is trying to stay focused while {AName} sucks on {TPPos} {Desc("ChestSize", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":50,
                }
            ActorDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 1,
                    },
                "Temporal":{
                    "Service": 10,
                    },
                "Permanent":{
                    "LickExp": 1,
                    "ServiceExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Sucking on {TName}'s {Desc("ChestSize", TargetData, "P")}''', "LongFluff": f'''{AName} is scuking on {TName}'s {Desc("ChestSize", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to suck on {TName}'s {Desc("ChestSize", TargetData, "P")}''', "LongFluff": f'''{AName} is failing to suck on {TName}'s {Desc("ChestSize", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on sucking on {TName}'s {Desc("ChestSize", TargetData, "P")}''', "LongFluff": f'''{AName} is trying to stay focused on sucking on {TName}'s {Desc("ChestSize", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":40,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetNippleSuckingSex0":
            TargetDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 2,
                    },
                "Temporal":{
                    "Obedience": 10,
                    "Submission": 10,
                    "Service": 10,
                    "Shame": 15,
                    "Discomfort": 55,
                    },
                "Permanent":{
                    "LickExp": 1,
                    "ServiceExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Sucking on {AName}'s {Desc("ChestSize", ActorData, "P")}''', "LongFluff": f'''{TName} is sucking on {AName}'s {Desc("ChestSize", ActorData, "DSP")} after being asked to.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Refusing to suck on {AName}'s {Desc("ChestSize", ActorData, "P")}''', "LongFluff": f'''{TName} is refusing to suck on {AName}'s {Desc("ChestSize", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on sucking on {AName}'s {Desc("ChestSize", ActorData, "P")} ''', "LongFluff": f'''{TName} is trying to stay focused while sucking on {AName}'s {Desc("ChestSize", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":55,
                }
            ActorDict = {
                "State":{
                    "Energy": -10,
                    "Arousal": 7,
                    },
                "Temporal":{
                    "Superiority": 10,
                    "CPlea": 20,
                    },
                "Permanent":{
                    "CExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Having {APPos} {Desc("ChestSize", ActorData, "P")} sucked''', "LongFluff": f'''{AName} is having {APPos} {Desc("ChestSize", ActorData, "DSP")} sucked by {TName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to get {TName} to scuk on {APPos} {Desc("ChestSize", ActorData, "P")}''', "LongFluff": f'''{AName} is failing to get {TName} to suck on {APPos} {Desc("ChestSize", ActorData, "DSP")} '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focused while having {APPos} {Desc("ChestSize", ActorData, "P")} sucked on''', "LongFluff": f'''{AName} is trying to stay focused while {TName} sucks on {APPos} {Desc("ChestSize", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":45,
                }
            OtherData = {
                "Success":2,
                }

        elif CommandID == "AnalCaressSex0":
            TargetDict = {
                "State":{
                    "Energy": -15,
                    "Excitement": 1,
                    "Arousal": 1,
                    },
                "Temporal":{
                    "Submission": 15,
                    "Shame": 20,
                    "APlea": 3,
                    "Pain": 5,
                    "Discomfort": 40,
                    },
                "Permanent":{
                    "AExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Having {TPPos} {Desc("ATightness", TargetData, "P")} caressed''', "LongFluff": f'''{TName} is having {TPPos} {Desc("ATightness", TargetData, "DSP")} caressed by {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting {AName}'s attempt to caress {TPPos} {Desc("ATightness", TargetData, "P")}''', "LongFluff": f'''{TName} resists as {AName} attempts to caress {TPPos} {Desc("ATightness", TargetData, "P")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus as {AName} caresses {TPPos} {Desc("VTightness", TargetData, "P")}''', "LongFluff": f'''{TName} is trying to focus while {AName} is caressing {TPPos} {Desc("VTightness", TargetData, "P")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":40,
                }
            ActorDict = {
                "State":{
                    "Energy": -10,
                    },
                "Temporal":{
                    },
                "Permanent":{
                    "CaressExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Caressing {TName}'s {Desc("ATightness", TargetData, "P")}''', "LongFluff": f'''{AName} is caressing {TName}'s {Desc("ATightness", TargetData, "DSP")}. '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to caress {TName}'s {Desc("ATightness", TargetData, "P")}''', "LongFluff": f'''{AName} tries to caress {TName}'S {Desc("ATightness", TargetData, "P")}, but fails to do so. '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on caressing {TName}'s {Desc("ATightness", TargetData, "P")}''', "LongFluff": f'''{AName} attempts to focuas as {APSub} caresses {TPPos} {Desc("ATightness", TargetData, "P")}'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":30,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetAnalCaressSex0":
            TargetDict = {
                "State":{
                    "Energy": -10,
                    },
                "Temporal":{
                    "Submission": 10,
                    "Obedience": 10,
                    "Shame": 20,
                    "Discomfort": 50,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Caressingg {AName}'s {Desc("ATightness", ActorData, "P")}''', "LongFluff": f'''{TName} is caressing {AName}'s {Desc("ATightness", ActorData, "DSP")} after being asked to.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Refusing to caress {AName}'s {Desc("ATightness", ActorData, "P")}''', "LongFluff": f'''{TName} is refusing to caress {AName}'s {Desc("ATightness", ActorData, "DSP")} after being asked to.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus and caress [AName]'s {Desc("ATightness", ActorData, "P")}''', "LongFluff": f'''{TName} is trying to focus while caressing {AName}'s {Desc("ATightness", ActorData, "DSP")} after being asked to.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":50,
                }
            ActorDict = {
                "State":{
                    "Energy": -20,
                    "Arousal": 2,
                    },
                "Temporal":{
                    "Superiority": 10,
                    "APlea": 3,
                    "Pain": 5,
                    },
                "Permanent":{
                    "AEXP": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Having {TName} caress {APPos} {Desc("ATightness", ActorData, "P")}''', "LongFluff": f'''{AName} is having {APPos} {Desc("ATightness", ActorData, "DSP")} caresed by {TName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to have {TName} caress {APPos} {Desc("ATightness", ActorData, "P")}''', "LongFluff": f'''{AName} is failing to get {TName} to caress {APPos} {Desc("ATightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while {TName} is caressing {APPos} {Desc("ATightness", ActorData, "P")}''', "LongFluff": f'''{AName} is trying to focus while having {AName} caress {APPos} {Desc("ATightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":40,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "AnalFingeringSex0":
            TargetDict = {
                "State":{
                    "Energy": -20,
                    "Arousal": 3,
                    },
                "Temporal":{
                    "Submission": 15,
                    "Shame": 20,
                    "APlea": 5,
                    "Pain": 15,
                    "Discomfort": 50,
                    },
                "Permanent":{
                    "AEXP": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Being anally fingered by {AName}''', "LongFluff": f'''{TName} is having {TPPos} {Desc("ATightness", TargetData, "DSP")} fingered by {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting {AName}'s attempts to anally Finger {TPObj}''', "LongFluff": f'''{TName} is resisting {AName}'s attempts at fingering {TPPos} {Desc("ATightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''{TName} is trying to focus while being anally fingered''', "LongFluff": f'''{TName} is trying to focus while {AName} fingers {TPPos} {Desc("ATightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance": 50,
                }
            ActorDict = {
                "State":{
                    "Energy": -10,
                    },
                "Temporal":{
                    },
                "Permanent":{
                    "CaressExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Fingering {TName}'s {Desc("ATightness", TargetData, "P")}''', "LongFluff": f'''{AName} is fingering {TName}'s {Desc("ATightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to finger {TName}'s {Desc("ATightness", TargetData, "P")}''', "LongFluff": f'''{TName} is failing to finger {TPPos} {Desc("ATightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on anally fingering {TName}''', "LongFluff": f'''{AName} is trying to focus on fingering {TName}'s {Desc("ATightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":40,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetAnalFingeringSex0":
            TargetDict = {
                "State":{
                    "Energy": -10,
                    },
                "Temporal":{
                    "Submission": 15,
                    "Obedience": 15,
                    "Shame": 30,
                    "Discomfort": 60,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Fingering {AName}'s {Desc("ATightness", ActorData, "P")}''', "LongFluff": f'''{TName} is fingering {AName}'s {Desc("ATightness", ActorData, "DSP")} after being asked to.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Refusing to finger {AName}'s {Desc("ATightness", ActorData, "P")}''', "LongFluff": f'''{TName} is refusinng to finger {AName}'s {Desc("ATightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on fingering {AName}'s {Desc("ATightness", ActorData, "P")}''', "LongFluff": f'''{TName} is trying to focus while fingering {AName}'s {Desc("ATightness", ActorData, "P")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":60,
                }
            ActorDict = {
                "State":{
                    "Energy": -20,
                    "Arousal": 4,
                    },
                "Temporal":{
                    "Superiority": 10,
                    "APlea": 5,
                    "Pain": 8,
                    },
                "Permanent":{
                    "AEXP": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting anally fingered by {TName}''', "LongFluff": f'''{AName} is getting {APPos} {Desc("ATightness", ActorData, "DSP")} fingered by {TName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to get {TName} to anally finger {APObj}''', "LongFluff": f'''{AName} is failing to get {TName} to finger {APPos} {Desc("ATightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while {TName} anally fingers {APObj}''', "LongFluff": f'''{AName} is trying to focus while {TName} fingers {APPos} {Desc("ATightness", ActorData, "DSP")} '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":50,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "RimjobSex0":
            TargetDict = {
                "State":{
                    "Energy": -25,
                    "Excitement": 4,
                    "Arousal": 5,
                    },
                "Temporal":{
                    "Desire": 15,
                    "Submission": 10,
                    "Shame": 25,
                    "APlea": 15,
                    "Pain": 5,
                    "Discomfort": 70,
                    },
                "Permanent":{
                    "AEXP": 2,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting {TPPos} {Desc("ATightness", TargetData, "P")} eaten''', "LongFluff": f'''{TName} is having {TPPos} {Desc("ATightness", TargetData, "DSP")} eaten by {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Refusing to get {TPPos} {Desc("ATightness", TargetData, "P")} eaten by {AName} ''', "LongFluff": f'''{TName} is refusing to have {AName} eat {TPPos} {Desc("ATightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while {AName} eats {TPPos} {Desc("ATightness", TargetData, "P")}''', "LongFluff": f'''{TName} is trying to focus while {AName} eats {TPPos} {Desc("ATightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance": 70,
                }
            ActorDict = {
                "State":{
                    "Energy": -15,
                    "Excitement": 3,
                    },
                "Temporal":{
                    "Service": 10,
                    },
                "Permanent":{
                    "LickExp": 1,
                    "ServiceExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Eating {TName}'s {Desc("ATightness", TargetData, "P")}''', "LongFluff": f'''{AName} is eating {TName}'s {Desc("ATightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to eat {TName}'s {Desc("ATightness", TargetData, "P")}''', "LongFluff": f'''{AName} is failing to eat {TName}'s {Desc("ATightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on eating {TName}'s {Desc("ATightness", TargetData, "P")}''', "LongFluff": f'''{AName} is trying to focus on eating {TName}'s {Desc("ATightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":60,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetRimjobSex0":
            TargetDict = {
                "State":{
                    "Mood": -2,
                    "Energy": -15,
                    },
                "Temporal":{
                    "Obedience": 15,
                    "Submission": 20,
                    "Service": 15,
                    "Shame": 30,
                    "Discomfort": 80,
                    },
                "Permanent":{
                    "LickExp": 1,
                    "ServiceExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Eating {AName}'s {Desc("ATightness", ActorData, "P")}''', "LongFluff": f'''{TName} is eating {AName}'s {Desc("ATightness", ActorData, "DSP")} at {APPos} request.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Refusing to eat {AName}'s {Desc("ATightness", ActorData, "P")}''', "LongFluff": f'''{TName} is refusin to eat {AName}'s {Desc("ATightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus on eating {AName}'s {Desc("ATightness", ActorData, "P")}''', "LongFluff": f'''{TName} is trying to focus on eating {AName}'s {Desc("ATightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":80,
                }
            ActorDict = {
                "State":{
                    "Energy": -20,
                    "Excitement": 4,
                    "Arousal": 5,
                    },
                "Temporal":{
                    "Superiority": 16,
                    },
                "Permanent":{
                    "AEXP": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Having {TName} eat {APPos} {Desc("ATightness", ActorData, "P")}''', "LongFluff": f'''{AName} is having {TName} eat {APPos} {Desc("ATightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to get {TName} to eat {APPos} {Desc("ATightness", ActorData, "P")}''', "LongFluff": f'''{AName} is failing to get {TName} to eat {APPos} {Desc("ATightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''rying to focus while {TName} eats {APPos} {Desc("ATightness", ActorData, "P")}''', "LongFluff": f'''{AName} is trying to focus while {TName} eats {APPos} {Desc("ATightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":70,
                }
            OtherData = {
                "Success":2,
                }

        ####
        elif CommandID == "MasturbateSex0":
            TargetDict = {
                "State":{
                    "Energy": -5,
                    "Excitement": 2,
                    },
                "Temporal":{
                    "Desire": 5,
                    "Shame": 5,
                    "Discomfort": 15,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":15,
                }
            ActorDict = {
                "State":{
                    "Energy": -15,
                    "Excitement": 7,
                    "Arousal": 7,
                    },
                "Temporal":{
                    "Shame": 15,
                    "CPlea": 10,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":5,
                }
            OtherData = {
                "Success":2,
                }
            if Globals.SoLNPCData[Actor]["BodyData"]["VTightness"] >= 1:
                ActorDict["Temporal"]["VPlea"] = 10
                ActorDict["Connotations"]["V"] = [1,5]
            if Globals.SoLNPCData[Actor]["BodyData"]["PenisSize"] >= 1:
                ActorDict["Temporal"]["PPlea"] = 10
                ActorDict["Connotations"]["P"] = [1,5]
        elif CommandID == "GetMasturbateSex0":
            TargetDict = {
                "State":{
                    "Energy": -15,
                    "Excitement": 7,
                    "Arousal": 7,
                    },
                "Temporal":{
                    "Obedience": 10,
                    "Submission": 10,
                    "Shame": 20,
                    "Discomfort": 35,
                    "CPlea": 10,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":35,
                }
            ActorDict = {
                "State":{
                    "Energy": -5,
                    "Excitement": 3,
                    },
                "Temporal":{
                    "Desire": 5,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":25,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "AMasturbateSex0":
            TargetDict = {
                "State":{
                    "Energy": -5,
                    "Excitement": 1,
                    },
                "Temporal":{
                    "Desire": 3,
                    "Shame": 10,
                    "Discomfort": 20,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":20,
                }
            ActorDict = {
                "State":{
                    "Energy": -15,
                    "Excitement": 4,
                    "Arousal": 4,
                    },
                "Temporal":{
                    "Shame": 20,
                    "APlea": 7,
                    "Pain": 5,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":5,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetAMasturbateSex0":
            TargetDict = {
                "State":{
                    "Energy": -20,
                    "Excitement": 4,
                    "Arousal": 4,
                    },
                "Temporal":{
                    "Obedience": 15,
                    "Submission": 15,
                    "Shame": 30,
                    "Discomfort": 45,
                    "CPlea": 7,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":45,
                }
            ActorDict = {
                "State":{
                    "Energy": -5,
                    "Excitement": 1,
                    },
                "Temporal":{
                    "Desire": 5,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":35,
                }
            OtherData = {
                "Success":2,
                }

        elif CommandID == "FootjobSex0":
            TargetDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 5,
                    "Arousal": 3,
                    },
                "Temporal":{
                    "Favor": 10,
                    "Desire": 5,
                    "Shame": 10,
                    "Discomfort": 25,
                    },
                "Permanent":{
                    "Attraction": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Footjob", {"BriefFluff": f'''Giving a footjob to  {Globals.SoLNPCData[Actor]["Name"]}''', "LongFluff": f'''{Globals.SoLNPCData[Target]["Name"]} is pleasuring {Globals.SoLNPCData[Actor]["Name"]} with their feet.'''}],
                    "InterruptionPenalty": 30,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":25,
                }
            ActorDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 3,
                    },
                "Temporal":{
                    "Service": 5,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    "ServiceExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Footjob", {"BriefFluff": f'''Receiving a footjob from {Globals.SoLNPCData[Actor]["Name"]}''', "LongFluff": f'''{Globals.SoLNPCData[Target]["Name"]} is being pleasured with  {Globals.SoLNPCData[Actor]["Name"]}'s feet'''}],
                    "InterruptionPenalty": 30,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":20,
                }
            OtherData = {
                "Success":2,
                }
            if Globals.SoLNPCData[Target]["BodyData"]["VTightness"] >= 1:
                TargetDict["Permanent"]["VExp"] = 1
                TargetDict["Temporal"]["VPlea"] = 7
                TargetDict["Connotations"]["V"] = [1,15]
            if Globals.SoLNPCData[Target]["BodyData"]["PenisSize"] >= 1:
                TargetDict["Permanent"]["PExp"] = 1
                TargetDict["Temporal"]["PPlea"] = 7
                TargetDict["Connotations"]["P"] = [1,15]
        elif CommandID == "GetFootjobSex0":
            TargetDict = {
                "State":{
                    "Energy": -10,
                    },
                "Temporal":{
                    "Submission": 10,
                    "Service": 10,
                    "Shame": 10,
                    "Discomfort": 35,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    "ServiceExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":35,
                }
            ActorDict = {
                "State":{
                    "Energy": -15,
                    "Excitement": 4,
                    "Arousal": 2,
                    },
                "Temporal":{
                    "Desire": 5,
                    "Superiority": 10,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":25,
                }
            OtherData = {
                "Success":2,
                }
            if Globals.SoLNPCData[Actor]["BodyData"]["VTightness"] >= 1:
                ActorDict["Permanent"]["VExp"] = 1
                ActorDict["Temporal"]["VPlea"] = 7
                ActorDict["Connotations"]["V"] = [1,15]
            if Globals.SoLNPCData[Actor]["BodyData"]["PenisSize"] >= 1:
                ActorDict["Permanent"]["PExp"] = 1
                ActorDict["Temporal"]["PPlea"] = 7
                ActorDict["Connotations"]["P"] = [1,15]
        ####
        elif CommandID == "ButtjonbSex0":
            TargetDict = {
                "State":{
                    "Energy": -15,
                    "Excitement": 5,
                    "Arousal": 4,
                    },
                "Temporal":{
                    "Favor": 10,
                    "Desire": 8,
                    "Shame": 13,
                    "PPlea": 8,
                    "Discomfort": 30,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "PExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Receiving a buttjob from {AName}''', "LongFluff": f'''{TName} is getting {TPPos} {Desc("PenisSize", TargetData, "DSP")} pleasure by {AName} with {APPos} {Desc("AssSize", ActorData, "DP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting to get a buttjob from {AName}''', "LongFluff": f'''{TName} is refusing to get a buttjob by {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while receiving a buttjob by {AName}''', "LongFluff": f'''{TName} is trying to stay focused while getting {TPPos} {Desc("PenisSize", TargetData, "DSP")} pleasure by {AName} with {APPos} {Desc("AssSize", ActorData, "DP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":30,
                }
            ActorDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 3,
                    },
                "Temporal":{
                    "Service": 7,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    "ServiceExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Giving {TName} a buttjob''', "LongFluff": f'''{AName} is using {APPos} {Desc("AssSize", ActorData, "DP")} to pleasure {TName}'s {Desc("PenisSize", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to give {TName} a buttjob''', "LongFluff": f'''{AName} is failing to give {TName} a buttjob.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while giving {TName} a buttjob.''', "LongFluff": f'''{AName} is trying to stay focused while using {APPos} {Desc("AssSize", ActorData, "DP")} to pleasure {TName}'s {Desc("PenisSize", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":25,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetButtjonbSex0":
            TargetDict = {
                "State":{
                    "Energy": -10,
                    },
                "Temporal":{
                    "Submission": 15,
                    "Service": 10,
                    "Shame": 15,
                    "Discomfort": 40,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    "ServiceExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Giving a buttjob to {AName}''', "LongFluff": f'''{TName} is using {TPPos} {Desc("AssSize", TargetData, "DP")} to pleasure {TName}'s {Desc("PenisSize", ActorData, "DSP")} after being asked to.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Refusing to give a buttjob to {AName}''', "LongFluff": f'''{TName} is refusing to give a buttjob to {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focused while giving a buttjob to {AName}''', "LongFluff": f'''{TName} is trying to stay focused while using {TPPos} {Desc("AssSize", TargetData, "DP")} to pleasure {TName}'s {Desc("PenisSize", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":40,
                }
            ActorDict = {
                "State":{
                    "Energy": -15,
                    "Excitement": 5,
                    "Arousal": 3,
                    },
                "Temporal":{
                    "Desire": 10,
                    "Superiority": 15,
                    "PPlea": 10,
                    },
                "Permanent":{
                    "PExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting a buttjob from {TName}''', "LongFluff": f'''{AName} is getting {APPos} {Desc("PenisSize", ActorData, "DSP")} pleasured by {TName} using {TPPos} {Desc("AssSize", TargetData, "DP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to get a buttjob from {TName}''', "LongFluff": f'''{AName} is failing to get a buttjob from {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focusd while getting a buttjob from {TName}''', "LongFluff": f'''{AName} is trying to stay focused while getting {APPos} {Desc("PenisSize", ActorData, "DSP")} pleasured by {TName} using {TPPos} {Desc("AssSize", TargetData, "DP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":30,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "ThighjobSex0":
            TargetDict = {
                "State":{
                    "Energy": -15,
                    "Excitement": 8,
                    "Arousal": 5,
                    },
                "Temporal":{
                    "Favor": 20,
                    "Desire": 12,
                    "Shame": 20,
                    "PPlea": 10,
                    "Discomfort": 40,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "PExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Receiving a thighjob from {AName}''', "LongFluff": f'''{TName} is getting {TPPos} {Desc("PenisSize", TargetData, "DSP")} pleasure by {AName} with {APPos} thighs.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting to get a thighjob from {AName}''', "LongFluff": f'''{TName} is refusing to get a thighjob by {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while receiving a thighjob by {AName}''', "LongFluff": f'''{TName} is trying to stay focused while getting {TPPos} {Desc("PenisSize", TargetData, "DSP")} pleasure by {AName} with {APPos} thighs.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":40,
                }
            ActorDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 5,
                    },
                "Temporal":{
                    "Service": 15,
                    "VPlea": 2,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    "ServiceExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Giving {TName} a thighjob''', "LongFluff": f'''{AName} is using {APPos} thighs to pleasure {TName}'s {Desc("PenisSize", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to give {TName} a thighjob''', "LongFluff": f'''{AName} is failing to give {TName} a thighjob.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while giving {TName} a thighjob.''', "LongFluff": f'''{AName} is trying to stay focused while using {APPos} thighs to pleasure {TName}'s {Desc("PenisSize", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":35,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetThighjobSex0":
            TargetDict = {
                "State":{
                    "Energy": -10,
                    },
                "Temporal":{
                    "Submission": 25,
                    "Service": 15,
                    "Shame": 25,
                    "Discomfort": 50,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    "ServiceExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f''''Giving a thighjob to {AName}''', "LongFluff": f'''{TName} is using {TPPos} thighs to pleasure {TName}'s {Desc("PenisSize", ActorData, "DSP")} after being asked to.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Refusing to give a thighjob to {AName}''', "LongFluff": f'''{TName} is refusing to give a thighjob to {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focused while giving a thighjob to {AName}''', "LongFluff": f'''{TName} is trying to stay focused while using {TPPos} thighs to pleasure {TName}'s {Desc("PenisSize", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":50,
                }
            ActorDict = {
                "State":{
                    "Energy": -15,
                    "Excitement": 8,
                    "Arousal": 5,
                    },
                "Temporal":{
                    "Desire": 20,
                    "Superiority": 25,
                    "PPlea": 12,
                    },
                "Permanent":{
                    "PExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting a thighjob from {TName}''', "LongFluff": f'''{AName} is getting {APPos} {Desc("PenisSize", ActorData, "DSP")} pleasured by {TName} using {TPPos} thighs.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to get a thighjob from {TName}''', "LongFluff": f'''{AName} is failing to get a thighjob from {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focusd while getting a thighjob from {TName}''', "LongFluff": f'''{AName} is trying to stay focused while getting {APPos} {Desc("PenisSize", ActorData, "DSP")} pleasured by {TName} using {TPPos} thighs.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":40,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "TitjobSex0":
            TargetDict = {
                "State":{
                    "Energy": -15,
                    "Excitement": 5,
                    "Arousal": 8,
                    },
                "Temporal":{
                    "Favor": 10,
                    "Desire": 15,
                    "Shame": 15,
                    "PPlea": 12,
                    "Discomfort": 35,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "PExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Receiving a titjob from {AName}''', "LongFluff": f'''{TName} is getting {TPPos} {Desc("PenisSize", TargetData, "DSP")} pleasure by {AName} with {APPos} {Desc("ChestSize", ActorData, "DP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting to get a titjob from {AName}''', "LongFluff": f'''{TName} is refusing to get a titjob by {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while receiving a titjob by {AName}''', "LongFluff": f'''{TName} is trying to stay focused while getting {TPPos} {Desc("PenisSize", TargetData, "DSP")} pleasure by {AName} with {APPos} {Desc("ChestSize", ActorData, "DP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":35,
                }
            ActorDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 5,
                    },
                "Temporal":{
                    "Service": 15,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    "ServiceExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Giving {TName} a titjob''', "LongFluff": f'''{AName} is using {APPos} {Desc("ChestSize", ActorData, "DP")} to pleasure {TName}'s {Desc("PenisSize", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to give {TName} a titjob''', "LongFluff": f'''{AName} is failing to give {TName} a titjob.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while giving {TName} a titjob.''', "LongFluff": f'''{AName} is trying to stay focused while using {APPos} {Desc("ChestSize", ActorData, "DP")} to pleasure {TName}'s {Desc("PenisSize", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":30,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetTitjobSex0":
            TargetDict = {
                "State":{
                    "Energy": -10,
                    },
                "Temporal":{
                    "Submission": 30,
                    "Service": 10,
                    "Shame": 20,
                    "Discomfort": 50,
                    },
                "Permanent":{
                    "CaressExp": 1,
                    "ServiceExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Giving a titjob to {AName}''', "LongFluff": f'''{TName} is using {TPPos} {Desc("ChestSize", TargetData, "DP")} to pleasure {TName}'s {Desc("PenisSize", ActorData, "DSP")} after being asked to.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Refusing to give a titjob to {AName}''', "LongFluff": f'''{TName} is refusing to give a titjob to {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focused while giving a titjob to {AName}''', "LongFluff": f'''{TName} is trying to stay focused while using {TPPos} {Desc("ChestSize", TargetData, "DP")} to pleasure {TName}'s {Desc("PenisSize", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":50,
                }
            ActorDict = {
                "State":{
                    "Energy": -15,
                    "Excitement": 10,
                    "Arousal": 7,
                    },
                "Temporal":{
                    "Desire": 20,
                    "Superiority": 20,
                    "PPlea": 15,
                    },
                "Permanent":{
                    "PExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting a titjob from {TName}''', "LongFluff": f'''{AName} is getting {APPos} {Desc("PenisSize", ActorData, "DSP")} pleasured by {TName} using {TPPos} {Desc("ChestSize", TargetData, "DP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to get a titjob from {TName}''', "LongFluff": f'''{AName} is failing to get a titjob from {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focusd while getting a titjob from {TName}''', "LongFluff": f'''{AName} is trying to stay focused while getting {APPos} {Desc("PenisSize", ActorData, "DSP")} pleasured by {TName} using {TPPos} {Desc("ChestSize", TargetData, "DP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":40,
                }
            OtherData = {
                "Success":2,
                }

        elif CommandID == "FacesittingSex0":
            TargetDict = {
                "State":{
                    "Energy": -15,
                    "Excitement": 1,
                    },
                "Temporal":{
                    "Obedience": 15,
                    "Submission": 40,
                    "Service": 15,
                    "Shame": 25,
                    "Discomfort": 80,
                    },
                "Permanent":{
                    "LickExp": 1,
                    "ServiceExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting facesit by {AName}''', "LongFluff": f'''{TName} is using her face to support, and pleasure {AName}'s {Desc("VTightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Refusing to be facesit by {AName}''', "LongFluff": f'''{TName} is refusing to let {AName} sit on {TPPos} face.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focused while being facesit by {AName}''', "LongFluff": f'''{TName} is trying to stay focused while using {TPPos} face to support, and pleasure {AName}'s {Desc("VTightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":80,
                }
            ActorDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 5,
                    "Arousal": 4,
                    },
                "Temporal":{
                    "Superiority": 25,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Sitting on {TName}'s face''', "LongFluff": f'''{AName} is using {TName}'s face as a seat and to pleasure {APPos} {Desc("VTightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failling to sit on {TName}'s face''', "LongFluff": f'''{AName} is failling to sit on {TName}'s face.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focused while sitting on {TName}'s face''', "LongFluff": f'''{AName} is trying to stay focuse while using {TName}'s face as a seat and to pleasure {APPos} {Desc("VTightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":70,
                }
            OtherData = {
                "Success":2,
                }
            if Globals.SoLNPCData[Actor]["BodyData"]["VTightness"] >= 1:
                ActorDict["Permanent"]["VExp"] = 1
                ActorDict["Temporal"]["VPlea"] = 10
                ActorDict["Connotations"]["V"] = [1,15]
            # if Globals.SoLNPCData[Actor]["BodyData"]["PenisSize"] >= 1:
            #     ActorDict["Permanent"]["PExp"] = 1
            #     ActorDict["Temporal"]["PPlea"] = 3
            #     ActorDict["Connotations"]["P"] = [1,5]
        elif CommandID == "GetFacesittingSex0":
            TargetDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 4,
                    "Arousal": 3,
                    },
                "Temporal":{
                    "Desire": 10,
                    "Superiority": 10,
                    "Shame": 15,
                    "Discomfort": 75,
                    },
                "Permanent":{
                    "Attraction": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Sitting on {AName}'s face''', "LongFluff": f'''{TName} is using {AName}'s face as a seat and to pleasure {TPPos} {Desc("VTightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Refusing to sit on {AName}'s face''', "LongFluff": f'''{TName} is refusing to sit on {AName}'s face.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focused while sitting on {AName}'s face''', "LongFluff": f'''{TName} is trying to stay focuse while using {AName}'s face as a seat and to pleasure {TPPos} {Desc("VTightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance": 75,
                }
            ActorDict = {
                "State":{
                    "Energy": -15,
                    "Excitement": 3,
                    },
                "Temporal":{
                    "Desire": 10,
                    "Service": 10,
                    "Shame": 15,
                    },
                "Permanent":{
                    "LickExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting facesit by {TName}''', "LongFluff": f'''{AName} is using her face to support, and pleasure {TName}'s {Desc("VTightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to be facesit by {TName}''', "LongFluff": f'''{AName} is failing to be facesit by {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focused while being facesit by {TName}''', "LongFluff": f'''{AName} is trying to stay focused while using {APPos} face to support, and pleasure {TName}'s {Desc("VTightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":65,
                }
            OtherData = {
                "Success":2,
                }
            if Globals.SoLNPCData[Target]["BodyData"]["VTightness"] >= 1:
                TargetDict["Permanent"]["VExp"] = 1
                TargetDict["Temporal"]["VPlea"] = 10
                TargetDict["Connotations"]["V"] = [1,15]
            # if Globals.SoLNPCData[Target]["BodyData"]["PenisSize"] >= 1:
            #     TargetDict["Permanent"]["PExp"] = 1
            #     TargetDict["Temporal"]["PPlea"] = 3
            #     TargetDict["Connotations"]["P"] = [1,5]
        elif CommandID == "AFacesittingSex0":
            TargetDict = {
                "State":{
                    "Mood": -2,
                    "Energy": -20,
                    "Excitement": -2,
                    },
                "Temporal":{
                    "Obedience": 20,
                    "Submission": 30,
                    "Service": 25,
                    "Shame": 40,
                    "Discomfort": 95,
                    },
                "Permanent":{
                    "LickExp": 1,
                    "Reliability": -1,
                    "ServiceExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting anally facesit by {AName}''', "LongFluff": f'''{TName} is using her face to support, and pleasure {AName}'s {Desc("ATightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Refusing to be anally facesit by {AName}''', "LongFluff": f'''{TName} is refusing to let {AName} anally sit on {TPPos} face.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focused while being anally facesit by {AName}''', "LongFluff": f'''{TName} is trying to stay focused while using {TPPos} face to support, and pleasure {AName}'s {Desc("ATightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":95,
                }
            ActorDict = {
                "State":{
                    "Energy": -15,
                    "Excitement": 5,
                    "Arousal": 3,
                    },
                "Temporal":{
                    "Superiority": 25,
                    "Shame": 20,
                    "APlea": 10,
                    "Pain": 5,
                    },
                "Permanent":{
                    "AEXP": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Anally sitting on {TName}'s face''', "LongFluff": f'''{AName} is using {TName}'s face as a seat and to pleasure {APPos} {Desc("ATightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failling to anally sit on {TName}'s face''', "LongFluff": f'''{AName} is failling to anally sit on {TName}'s face.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focused while anally sitting on {TName}'s face''', "LongFluff": f'''{AName} is trying to stay focuse while using {TName}'s face as a seat and to pleasure {APPos} {Desc("ATightness", ActorData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":85,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetAFacesittingSex0":
            TargetDict = {
                "State":{
                    "Energy": -15,
                    "Excitement": 3,
                    },
                "Temporal":{
                    "Obedience": 20,
                    "Submission": 20,
                    "Shame": 20,
                    "APlea": 10,
                    "Pain": 5,
                    "Discomfort": 90,
                    },
                "Permanent":{
                    "AEXP": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Anally sitting on {AName}'s face''', "LongFluff": f'''{TName} is using {AName}'s face as a seat and to pleasure {TPPos} {Desc("ATightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Refusing to anally sit on {AName}'s face''', "LongFluff": f'''{TName} is refusing to anally sit on {AName}'s face.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focused while anally sitting on {AName}'s face''', "LongFluff": f'''{TName} is trying to stay focuse while using {AName}'s face as a seat and to pleasure {TPPos} {Desc("ATightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":90,
                }
            ActorDict = {
                "State":{
                    "Energy": -10,
                    "Excitement": 2,
                    },
                "Temporal":{
                    "Superiority": 20,
                    "Service": 15,
                    "Shame": 20,
                    },
                "Permanent":{
                    "LickExp": 1,
                    "ServiceExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting anally facesit by {TName}''', "LongFluff": f'''{AName} is using her face to support, and pleasure {TName}'s {Desc("ATightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to be anally facesit by {TName}''', "LongFluff": f'''{AName} is failing to be anally facesit by {TName}. '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focused while being anally facesit by {TName}''', "LongFluff": f'''{AName} is trying to stay focused while using {APPos} face to support, and pleasure {TName}'s {Desc("ATightness", TargetData, "DSP")}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":80,
                }
            OtherData = {
                "Success":2,
                }

        #####
        elif CommandID == "AssSpankingSex0":
            TargetDict = {
                "State":{
                    "Mood": -1,
                    "Energy": -20,
                    "Excitement": 2,
                    },
                "Temporal":{
                    "Obedience": 15,
                    "Submission": 20,
                    "Shame": 15,
                    "Pain": 10,
                    "Fear": 5,
                    "Discomfort": 50,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":10,
                }
            ActorDict = {
                "State":{
                    "Energy": -10,
                    },
                "Temporal":{
                    "Superiority": 0,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":0,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetAssSpankingSex0":
            TargetDict = {
                "State":{
                    "Energy": -10,
                    },
                "Temporal":{
                    "Desire": 5,
                    "Obedience": 5,
                    "Superiority": 10,
                    "Shame": 10,
                    "Discomfort": 40,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":40,
                }
            ActorDict = {
                "State":{
                    "Energy": -20,
                    "Excitement": 2,
                    },
                "Temporal":{
                    "Obedience": 5,
                    "Submission": 5,
                    "Shame": 15,
                    "Pain": 10,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":30,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "BreastSlappingSex0":
            TargetDict = {
                "State":{
                    "Mood": -1,
                    "Energy": -20,
                    "Excitement": 2,
                    },
                "Temporal":{
                    "Obedience": 15,
                    "Submission": 20,
                    "Shame": 15,
                    "CPlea": 3,
                    "Pain": 10,
                    "Fear": 5,
                    "Discomfort": 40,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":10,
                }
            ActorDict = {
                "State":{
                    "Energy": -10,
                    },
                "Temporal":{
                    "Superiority": 0,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":0,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetBreastSlappingSex0":
            TargetDict = {
                "State":{
                    "Energy": -10,
                    },
                "Temporal":{
                    "Desire": 7,
                    "Obedience": 5,
                    "Superiority": 10,
                    "Shame": 15,
                    "Discomfort": 30,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":40,
                }
            ActorDict = {
                "State":{
                    "Energy": -20,
                    "Excitement": 2,
                    },
                "Temporal":{
                    "Obedience": 5,
                    "Submission": 5,
                    "Shame": 15,
                    "Pain": 10,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":30,
                }
            OtherData = {
                "Success":2,
                }
        ####

        elif CommandID == "MissionarySex0":
            TargetDict = {
                "State":{
                    "Mood": 5,
                    "Energy": -25,
                    "Excitement": 4,
                    "Arousal": 5,
                    },
                "Temporal":{
                    "Favor": 15,
                    "Loyalty": 5,
                    "VPlea": 20,
                    "Discomfort": 100,
                    },
                "Permanent":{
                    "Reliability": 1,
                    "VExp": 1,
                    "VPenetrationExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting fucked by {AName}''', "LongFluff": f'''{TName} is having {TPPos} {Desc("VTightness", TargetData, "DSP")} fucked by {AName}'s {Desc("PenisSize", ActorData, "DSP")} in the missionary position.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting being fucked by {AName}''', "LongFluff": f'''{TName} is reisting {AName}'s attempts at fucking {TPPos} {Desc("VTightness", TargetData, "P")} in the missionary position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while being fucked by {AName}''', "LongFluff": f'''{TName} is trying to stay focused while having {TPPos} {Desc("VTightness", TargetData, "DSP")} fucked by {AName}'s {Desc("PenisSize", ActorData, "DSP")} in the missionary position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":100,
                }
            ActorDict = {
                "State":{
                    "Mood": 5,
                    "Energy": -20,
                    "Excitement": 5,
                    "Arousal": 5,
                    },
                "Temporal":{
                    "Favor": 15,
                    "Loyalty": 10,
                    "Desire": 10,
                    "PPlea": 20,
                    },
                "Permanent":{
                    "Reliability": 1,
                    "PExp": 1,
                    "PenetrateExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Fucking {TName}''', "LongFluff": f'''{AName} is using {APPos} {Desc("PenisSize", ActorData, "DSP")} to fuck {TName}'s {Desc("VTightness", TargetData, "DSP")} in the missionary position.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to fuck {TName}''', "LongFluff": f'''{AName} is failing to fuck {TName}'s {Desc("VTightness", TargetData, "P")} in the missionary position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focused while fucking {TName}''', "LongFluff": f'''{AName} is trying to stay focused while using {APPos} {Desc("PenisSize", ActorData, "DSP")} to fuck {TName}'s {Desc("VTightness", TargetData, "DSP")} in the missionary position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":90,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetMissionarySex0":
            TargetDict = {
                "State":{
                    "Mood": 5,
                    "Energy": -20,
                    "Excitement": 5,
                    "Arousal": 5,
                    },
                "Temporal":{
                    "Favor": 15,
                    "Loyalty": 10,
                    "Desire": 5,
                    "Obedience": 15,
                    "Submission": 10,
                    "PPlea": 20,
                    "Discomfort": 100,
                    },
                "Permanent":{
                    "Reliability": 1,
                    "PExp": 1,
                    "PenetrateExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Fucking {AName}''', "LongFluff": f'''{TName} is using {TPPos} {Desc("PenisSize", TargetData, "DSP")} to fuck {AName}'s {Desc("VTightness", ActorData, "DSP")} in the missionary position.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting fucking {AName}''', "LongFluff": f'''{TName} is resisting fucking {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focused while fucking {AName}''', "LongFluff": f'''{TName} is trying t o stay focused while using {TPPos} {Desc("PenisSize", TargetData, "DSP")} to fuck {AName}'s {Desc("VTightness", ActorData, "DSP")} in the missionary position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":100,
                }
            ActorDict = {
                "State":{
                    "Mood": 5,
                    "Energy": -25,
                    "Excitement": 4,
                    "Arousal": 5,
                    },
                "Temporal":{
                    "Favor": 15,
                    "Loyalty": 5,
                    "Desire": 10,
                    "VPlea": 20,
                    },
                "Permanent":{
                    "Reliability": 1,
                    "VExp": 1,
                    "VPenetrationExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting fucked by {TName}''', "LongFluff": f'''{AName} is having {APPos} {Desc("VTightness", ActorData, "DSP")} fucked by {TName}'s {Desc("PenisSize", TargetData, "DSP")} in the missionary position.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to get fucked by {TName}''', "LongFluff": f'''{AName} is failing to get fucked by {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focuse while getting fucked by {TName}''', "LongFluff": f'''{AName} is trying to focus while having {APPos} {Desc("VTightness", ActorData, "DSP")} fucked by {TName}'s {Desc("PenisSize", TargetData, "DSP")} in the missionary position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":90,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "DoggyStyleSex0":
            TargetDict = {
                "State":{
                    "Energy": -30,
                    "Excitement": 3,
                    "Arousal": 7,
                    },
                "Temporal":{
                    "Shame": 20,
                    "VPlea": 25,
                    "Desire": 10,
                    "Discomfort": 80,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "VExp": 1,
                    "VPenetrationExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting fucked by {AName}''', "LongFluff": f'''{TName} is having {TPPos} {Desc("VTightness", TargetData, "DSP")} fucked by {AName}'s {Desc("PenisSize", ActorData, "DSP")} in the doggystyle position.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting being fucked by {AName}''', "LongFluff": f'''{TName} is reisting {AName}'s attempts at fucking {TPPos} {Desc("VTightness", TargetData, "P")} in the doggystyle position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while being fucked by {AName}''', "LongFluff": f'''{TName} is trying to stay focused while having {TPPos} {Desc("VTightness", TargetData, "DSP")} fucked by {AName}'s {Desc("PenisSize", ActorData, "DSP")} in the doggystyle position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":80,
                }
            ActorDict = {
                "State":{
                    "Energy": -25,
                    "Excitement": 3,
                    "Arousal": 7,
                    },
                "Temporal":{
                    "Desire": 15,
                    "PPlea": 25,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "PExp": 1,
                    "PenetrateExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Fucking {TName}''', "LongFluff": f'''{AName} is using {APPos} {Desc("PenisSize", ActorData, "DSP")} to fuck {TName}'s {Desc("VTightness", TargetData, "DSP")} in the missionary position.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to fuck {TName}''', "LongFluff": f'''{AName} is failing to fuck {TName}'s {Desc("VTightness", TargetData, "P")} in the missionary position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focused while fucking {TName}''', "LongFluff": f'''{AName} is trying to stay focused while using {APPos} {Desc("PenisSize", ActorData, "DSP")} to fuck {TName}'s {Desc("VTightness", TargetData, "DSP")} in the missionary position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":70,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetDoggyStyleSex0":
            TargetDict = {
                "State":{
                    "Energy": -25,
                    "Excitement": 3,
                    "Arousal": 7,
                    },
                "Temporal":{
                    "Desire": 5,
                    "Obedience": 10,
                    "Submission": 5,
                    "Shame": 5,
                    "PPlea": 25,
                    "Discomfort": 80,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "PExp": 1,
                    "PenetrateExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Fucking {AName}''', "LongFluff": f'''{TName} is using {TPPos} {Desc("PenisSize", TargetData, "DSP")} to fuck {AName}'s {Desc("VTightness", ActorData, "DSP")} in the doggystyle position.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting fucking {AName}''', "LongFluff": f'''{TName} is resisting fucking {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focused while fucking {AName}''', "LongFluff": f'''{TName} is trying t o stay focused while using {TPPos} {Desc("PenisSize", TargetData, "DSP")} to fuck {AName}'s {Desc("VTightness", ActorData, "DSP")} in the doggystyle position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":80,
                }
            ActorDict = {
                "State":{
                    "Energy": -30,
                    "Excitement": 3,
                    "Arousal": 7,
                    },
                "Temporal":{
                    "Desire": 10,
                    "VPlea": 25,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "VExp": 1,
                    "VPenetrationExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting fucked by {TName}''', "LongFluff": f'''{AName} is having {APPos} {Desc("VTightness", ActorData, "DSP")} fucked by {TName}'s {Desc("PenisSize", TargetData, "DSP")} in the doggystyle position.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to get fucked by {TName}''', "LongFluff": f'''{AName} is failing to get fucked by {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focuse while getting fucked by {TName}''', "LongFluff": f'''{AName} is trying to focus while having {APPos} {Desc("VTightness", ActorData, "DSP")} fucked by {TName}'s {Desc("PenisSize", TargetData, "DSP")} in the doggystyle position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":70,
                }
            OtherData = {
                "Success":2,
                }
        ####
        elif CommandID == "GetCowgirlSex0":
            TargetDict = {
                "State":{
                    "Mood": 2,
                    "Energy": -35,
                    "Excitement": 7,
                    "Arousal": 5,
                    },
                "Temporal":{
                    "Favor": 15,
                    "Loyalty": 10,
                    "Shame": 20,
                    "VPlea": 30,
                    "Discomfort": 100,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "VExp": 1,
                    "VPenetrationExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":100,
                }
            ActorDict = {
                "State":{
                    "Energy": -30,
                    "Excitement": 10,
                    "Arousal": 5,
                    },
                "Temporal":{
                    "Desire": 20,
                    "PPlea": 30,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "PExp": 1,
                    "PenetrateExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":90,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "CowgirlSex0":
            TargetDict = {
                "State":{
                    "Energy": -30,
                    "Excitement": 10,
                    "Arousal": 5,
                    },
                "Temporal":{
                    "Desire": 10,
                    "Obedience": 10,
                    "Submission": 10,
                    "Shame": 15,
                    "PPlea": 30,
                    "Discomfort": 100,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "PExp": 1,
                    "PenetrateExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":100,
                }
            ActorDict = {
                "State":{
                    "Mood": 2,
                    "Energy": -35,
                    "Excitement": 7,
                    "Arousal": 5,
                    },
                "Temporal":{
                    "Favor": 15,
                    "Loyalty": 10,
                    "Desire": 20,
                    "VPlea": 30,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "VExp": 1,
                    "VPenetrationExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":90,
                }
            OtherData = {
                "Success":2,
                }
        ####
        elif CommandID == "LotusSex0":
            TargetDict = {
                "State":{
                    "Mood": 10,
                    "Energy": -35,
                    "Excitement": 10,
                    "Arousal": 8,
                    },
                "Temporal":{
                    "Favor": 35,
                    "Loyalty": 35,
                    "Desire": 20,
                    "Shame": 20,
                    "VPlea": 30,
                    "Discomfort": 120,
                    },
                "Permanent":{
                    "Attraction": 2,
                    "Reliability": 2,
                    "VExp": 1,
                    "VPenetrationExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting fucked by {AName}''', "LongFluff": f'''{TName} is having {TPPos} {Desc("VTightness", TargetData, "DSP")} fucked by {AName}'s {Desc("PenisSize", ActorData, "DSP")} in the lotus position.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting being fucked by {AName}''', "LongFluff": f'''{TName} is reisting {AName}'s attempts at fucking {TPPos} {Desc("VTightness", TargetData, "P")} in the lotus position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while being fucked by {AName}''', "LongFluff": f'''{TName} is trying to stay focused while having {TPPos} {Desc("VTightness", TargetData, "DSP")} fucked by {AName}'s {Desc("PenisSize", ActorData, "DSP")} in the lotus position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":120,
                }
            ActorDict = {
                "State":{
                    "Mood": 10,
                    "Energy": -30,
                    "Excitement": 10,
                    "Arousal": 8,
                    },
                "Temporal":{
                    "Favor": 35,
                    "Loyalty": 35,
                    "Desire": 20,
                    "PPlea": 30,
                    },
                "Permanent":{
                    "Attraction": 2,
                    "Reliability": 2,
                    "PExp": 1,
                    "PenetrateExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Fucking {TName}''', "LongFluff": f'''{AName} is using {APPos} {Desc("PenisSize", ActorData, "DSP")} to fuck {TName}'s {Desc("VTightness", TargetData, "DSP")} in the lotus position.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to fuck {TName}''', "LongFluff": f'''{AName} is failing to fuck {TName}'s {Desc("VTightness", TargetData, "P")} in the lotus position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focused while fucking {TName}''', "LongFluff": f'''{AName} is trying to stay focused while using {APPos} {Desc("PenisSize", ActorData, "DSP")} to fuck {TName}'s {Desc("VTightness", TargetData, "DSP")} in the lotus position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":110,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetLotusSex0":
            TargetDict = {
                "State":{
                    "Mood": 10,
                    "Energy": -30,
                    "Excitement": 10,
                    "Arousal": 8,
                    },
                "Temporal":{
                    "Favor": 35,
                    "Loyalty": 35,
                    "Desire": 20,
                    "Obedience": 25,
                    "Submission": 15,
                    "Shame": 25,
                    "PPlea": 30,
                    "Discomfort": 120,
                    },
                "Permanent":{
                    "Attraction": 2,
                    "Reliability": 2,
                    "PExp": 1,
                    "PenetrateExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Fucking {AName}''', "LongFluff": f'''{TName} is using {TPPos} {Desc("PenisSize", TargetData, "DSP")} to fuck {AName}'s {Desc("VTightness", ActorData, "DSP")} in the lotus position.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f''''Resisting fucking {AName}''', "LongFluff": f'''{TName} is resisting fucking {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focused while fucking {AName}''', "LongFluff": f'''{TName} is trying t o stay focused while using {TPPos} {Desc("PenisSize", TargetData, "DSP")} to fuck {AName}'s {Desc("VTightness", ActorData, "DSP")} in the lotus position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":120,
                }
            ActorDict = {
                "State":{
                    "Mood": 10,
                    "Energy": -35,
                    "Excitement": 10,
                    "Arousal": 8,
                    },
                "Temporal":{
                    "Favor": 35,
                    "Loyalty": 35,
                    "Desire": 20,
                    "Shame": 25,
                    "VPlea": 30,
                    },
                "Permanent":{
                    "Attraction": 2,
                    "Reliability": 2,
                    "VExp": 1,
                    "VPenetrationExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting fucked by {TName}''', "LongFluff": f'''{AName} is having {APPos} {Desc("VTightness", ActorData, "DSP")} fucked by {TName}'s {Desc("PenisSize", TargetData, "DSP")} in the lotus position.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to get fucked by {TName}''', "LongFluff": f'''{AName} is failing to get fucked by {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focuse while getting fucked by {TName}''', "LongFluff": f'''{AName} is trying to focus while having {APPos} {Desc("VTightness", ActorData, "DSP")} fucked by {TName}'s {Desc("PenisSize", TargetData, "DSP")} in the lotus position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":110,
                }
            OtherData = {
                "Success":2,
                }

        elif CommandID == "AMissionarySex0":
            TargetDict = {
                "State":{
                    "Mood": 3,
                    "Energy": -30,
                    "Excitement": 3,
                    "Arousal": 4,
                    },
                "Temporal":{
                    "Favor": 15,
                    "Loyalty": 5,
                    "Shame": 20,
                    "Obedience": 15,
                    "Submission": 15,
                    "APlea": 20,
                    "Discomfort": 100,
                    },
                "Permanent":{
                    "Reliability": 1,
                    "AExp": 1,
                    "APenetrationExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting anally fucked by {AName}''', "LongFluff": f'''{TName} is having {TPPos} {Desc("ATightness", TargetData, "DSP")} fucked by {AName}'s {Desc("PenisSize", ActorData, "DSP")} in the missionary position.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting being anally fucked by {AName}''', "LongFluff": f'''{TName} is reisting {AName}'s attempts at fucking {TPPos} {Desc("ATightness", TargetData, "P")} in the missionary position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while being ANALLY fucked by {AName}''', "LongFluff": f'''{TName} is trying to stay focused while having {TPPos} {Desc("ATightness", TargetData, "DSP")} fucked by {AName}'s {Desc("PenisSize", ActorData, "DSP")} in the missionary position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":110,
                }
            ActorDict = {
                "State":{
                    "Mood": 4,
                    "Energy": -25,
                    "Excitement": 4,
                    "Arousal": 4,
                    },
                "Temporal":{
                    "Favor": 15,
                    "Loyalty": 10,
                    "Desire": 10,
                    "PPlea": 20,
                    },
                "Permanent":{
                    "Reliability": 1,
                    "PExp": 1,
                    "PenetrateExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Anally fucking {TName}''', "LongFluff": f'''{AName} is using {APPos} {Desc("PenisSize", ActorData, "DSP")} to fuck {TName}'s {Desc("ATightness", TargetData, "DSP")} in the missionary position.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to anally fuck {TName}''', "LongFluff": f'''{AName} is failing to fuck {TName}'s {Desc("ATightness", TargetData, "P")} in the missionary position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focused while ANALLY fucking {TName}''', "LongFluff": f'''{AName} is trying to stay focused while using {APPos} {Desc("PenisSize", ActorData, "DSP")} to fuck {TName}'s {Desc("ATightness", TargetData, "DSP")} in the missionary position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":100,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetAMissionarySex0":
            TargetDict = {
                "State":{
                    "Mood": 3,
                    "Energy": -25,
                    "Excitement": 4,
                    "Arousal": 4,
                    },
                "Temporal":{
                    "Favor": 15,
                    "Loyalty": 10,
                    "Desire": 5,
                    "Obedience": 10,
                    "Submission": 15,
                    "PPlea": 20,
                    "Discomfort": 110,
                    },
                "Permanent":{
                    "Reliability": 1,
                    "PExp": 1,
                    "PenetrateExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Anally fucking {AName}''', "LongFluff": f'''{TName} is using {TPPos} {Desc("PenisSize", TargetData, "DSP")} to fuck {AName}'s {Desc("ATightness", ActorData, "DSP")} in the missionary position.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting anally fucking {AName}''', "LongFluff": f'''{TName} is resisting anally fucking {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focused while anally fucking {AName}''', "LongFluff": f'''{TName} is trying t o stay focused while using {TPPos} {Desc("PenisSize", TargetData, "DSP")} to fuck {AName}'s {Desc("ATightness", ActorData, "DSP")} in the missionary position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":110,
                }
            ActorDict = {
                "State":{
                    "Mood": 5,
                    "Energy": -25,
                    "Excitement": 4,
                    "Arousal": 5,
                    },
                "Temporal":{
                    "Favor": 15,
                    "Loyalty": 5,
                    "Desire": 10,
                    "APlea": 20,
                    },
                "Permanent":{
                    "Reliability": 1,
                    "AExp": 1,
                    "APenetrationExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting anally fucked by {TName}''', "LongFluff": f'''{AName} is having {APPos} {Desc("ATightness", ActorData, "DSP")} fucked by {TName}'s {Desc("PenisSize", TargetData, "DSP")} in the missionary position.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to get anally fucked by {TName}''', "LongFluff": f'''{AName} is failing to get anally fucked by {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focuse while getting anally fucked by {TName}''', "LongFluff": f'''{AName} is trying to focus while having {APPos} {Desc("ATightness", ActorData, "DSP")} fucked by {TName}'s {Desc("PenisSize", TargetData, "DSP")} in the missionary position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":100,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "ADoggyStyleSex0":
            TargetDict = {
                "State":{
                    "Energy": -35,
                    "Excitement": 2,
                    "Arousal": 6,
                    },
                "Temporal":{
                    "Shame": 35,
                    "APlea": 25,
                    "Desire": 10,
                    "Submission": 15,
                    "Discomfort": 90,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "AExp": 1,
                    "APenetrationExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting anally fucked by {AName}''', "LongFluff": f'''{TName} is having {TPPos} {Desc("ATightness", TargetData, "DSP")} fucked by {AName}'s {Desc("PenisSize", ActorData, "DSP")} in the doggystyle position.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting being anally fucked by {AName}''', "LongFluff": f'''{TName} is reisting {AName}'s attempts at fucking {TPPos} {Desc("ATightness", TargetData, "P")} in the doggystyle position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while being anally fucked by {AName}''', "LongFluff": f'''{TName} is trying to stay focused while having {TPPos} {Desc("ATightness", TargetData, "DSP")} fucked by {AName}'s {Desc("PenisSize", ActorData, "DSP")} in the doggystyle position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":90,
                }
            ActorDict = {
                "State":{
                    "Energy": -25,
                    "Excitement": 3,
                    "Arousal": 7,
                    },
                "Temporal":{
                    "Desire": 15,
                    "PPlea": 25,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "PExp": 1,
                    "PenetrateExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Anally fucking {TName}''', "LongFluff": f'''{AName} is using {APPos} {Desc("PenisSize", ActorData, "DSP")} to fuck {TName}'s {Desc("ATightness", TargetData, "DSP")} in the missionary position.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to anally fuck {TName}''', "LongFluff": f'''{AName} is failing to fuck {TName}'s {Desc("ATightness", TargetData, "P")} in the missionary position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focused while anally fucking {TName}''', "LongFluff": f'''{AName} is trying to stay focused while using {APPos} {Desc("PenisSize", ActorData, "DSP")} to fuck {TName}'s {Desc("ATightness", TargetData, "DSP")} in the doggystyle position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":80,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetADoggyStyleSex0":
            TargetDict = {
                "State":{
                    "Energy": -30,
                    "Excitement": 2,
                    "Arousal": 6,
                    },
                "Temporal":{
                    "Desire": 5,
                    "Obedience": 10,
                    "Submission": 20,
                    "Shame": 20,
                    "PPlea": 25,
                    "Discomfort": 90,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "PExp": 1,
                    "PenetrateExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Anally fucking {AName} ''', "LongFluff": f'''{TName} is using {TPPos} {Desc("PenisSize", TargetData, "DSP")} to fuck {AName}'s {Desc("ATightness", ActorData, "DSP")} in the doggystyle position.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting anally fucking {AName}''', "LongFluff": f'''{TName} is resisting anally fucking {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focused while anally fucking {AName}''', "LongFluff": f'''{TName} is trying t o stay focused while using {TPPos} {Desc("PenisSize", TargetData, "DSP")} to fuck {AName}'s {Desc("ATightness", ActorData, "DSP")} in the doggystyle position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":90,
                }
            ActorDict = {
                "State":{
                    "Energy": -35,
                    "Excitement": 2,
                    "Arousal": 6,
                    },
                "Temporal":{
                    "Desire": 10,
                    "APlea": 25,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "AExp": 1,
                    "APenetrationExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting anally fucked by {TName}''', "LongFluff": f'''{AName} is having {APPos} {Desc("ATightness", ActorData, "DSP")} fucked by {TName}'s {Desc("PenisSize", TargetData, "DSP")} in the doggystyle position.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to get anally fucked by {TName}''', "LongFluff": f'''{AName} is failing to get anally fucked by {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focuse while getting anally fucked by {TName}''', "LongFluff": f'''{AName} is trying to focus while having {APPos} {Desc("ATightness", ActorData, "DSP")} fucked by {TName}'s {Desc("PenisSize", TargetData, "DSP")} in the doggystyle position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":80,
                }
            OtherData = {
                "Success":2,
                }
        ####
        elif CommandID == "GetCowgirlSex0":
            TargetDict = {
                "State":{
                    "Mood": 1,
                    "Energy": -40,
                    "Excitement": 6,
                    "Arousal": 4,
                    },
                "Temporal":{
                    "Favor": 15,
                    "Loyalty": 10,
                    "Obedience": 15,
                    "Shame": 35,
                    "APlea": 30,
                    "Discomfort": 110,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "AExp": 1,
                    "APenetrationExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":100,
                }
            ActorDict = {
                "State":{
                    "Energy": -35,
                    "Excitement": 8,
                    "Arousal": 4,
                    },
                "Temporal":{
                    "Desire": 20,
                    "PPlea": 30,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "PExp": 1,
                    "PenetrateExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":90,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "CowgirlSex0":
            TargetDict = {
                "State":{
                    "Energy": -35,
                    "Excitement": 8,
                    "Arousal": 4,
                    },
                "Temporal":{
                    "Desire": 10,
                    "Obedience": 25,
                    "Submission": 25,
                    "Shame": 30,
                    "PPlea": 30,
                    "Discomfort": 110,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "PExp": 1,
                    "PenetrateExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":110,
                }
            ActorDict = {
                "State":{
                    "Energy": -40,
                    "Excitement": 6,
                    "Arousal": 4,
                    },
                "Temporal":{
                    "Favor": 15,
                    "Loyalty": 10,
                    "Desire": 20,
                    "APlea": 30,
                    },
                "Permanent":{
                    "Attraction": 1,
                    "AExp": 1,
                    "APenetrationExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": ''' ''', "LongFluff": ''' '''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":100,
                }
            OtherData = {
                "Success":2,
                }
        ####
        elif CommandID == "LotusSex0":
            TargetDict = {
                "State":{
                    "Mood": 10,
                    "Energy": -40,
                    "Excitement": 9,
                    "Arousal": 7,
                    },
                "Temporal":{
                    "Favor": 35,
                    "Loyalty": 35,
                    "Desire": 20,
                    "Shame": 30,
                    "APlea": 30,
                    "Discomfort": 130,
                    },
                "Permanent":{
                    "Attraction": 2,
                    "Reliability": 2,
                    "AExp": 1,
                    "APenetrationExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting anally fucked by {AName}''', "LongFluff": f'''{TName} is having {TPPos} {Desc("ATightness", TargetData, "DSP")} fucked by {AName}'s {Desc("PenisSize", ActorData, "DSP")} in the lotus position.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting being anally fucked by {AName}''', "LongFluff": f'''{TName} is reisting {AName}'s attempts at fucking {TPPos} {Desc("ATightness", TargetData, "P")} in the lotus position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focus while being anally fucked by {AName}''', "LongFluff": f'''{TName} is trying to stay focused while having {TPPos} {Desc("ATightness", TargetData, "DSP")} fucked by {AName}'s {Desc("PenisSize", ActorData, "DSP")} in the missionary position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":130,
                }
            ActorDict = {
                "State":{
                    "Mood": 10,
                    "Energy": -35,
                    "Excitement": 9,
                    "Arousal": 7,
                    },
                "Temporal":{
                    "Favor": 35,
                    "Loyalty": 35,
                    "Desire": 20,
                    "PPlea": 30,
                    },
                "Permanent":{
                    "Attraction": 2,
                    "Reliability": 2,
                    "PExp": 1,
                    "PenetrateExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Anally fucking {TName} ''', "LongFluff": f'''{AName} is using {APPos} {Desc("PenisSize", ActorData, "DSP")} to fuck {TName}'s {Desc("ATightness", TargetData, "DSP")} in the lotus position.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to anally fuck {TName}''', "LongFluff": f'''{AName} is failing to fuck {TName}'s {Desc("ATightness", TargetData, "P")} in the lotus position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focused while anally fucking {TName}''', "LongFluff": f'''{AName} is trying to stay focused while using {APPos} {Desc("PenisSize", ActorData, "DSP")} to fuck {TName}'s {Desc("ATightness", TargetData, "DSP")} in the lotus position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":120,
                }
            OtherData = {
                "Success":2,
                }
        elif CommandID == "GetALotusSex0":
            TargetDict = {
                "State":{
                    "Mood": 10,
                    "Energy": -35,
                    "Excitement": 9,
                    "Arousal": 7,
                    },
                "Temporal":{
                    "Favor": 35,
                    "Loyalty": 35,
                    "Desire": 20,
                    "Obedience": 40,
                    "Submission": 30,
                    "Shame": 35,
                    "PPlea": 30,
                    "Discomfort": 130,
                    },
                "Permanent":{
                    "Attraction": 2,
                    "Reliability": 2,
                    "PExp": 1,
                    "PenetrateExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Anally fucking {AName} ''', "LongFluff": f'''{TName} is using {TPPos} {Desc("PenisSize", TargetData, "DSP")} to fuck {AName}'s {Desc("ATightness", ActorData, "DSP")} in the lotus position.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Resisting anally fucking {AName}''', "LongFluff": f'''{TName} is resisting anally fucking {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to stay focused while anally fucking {AName}''', "LongFluff": f'''{TName} is trying t o stay focused while using {TPPos} {Desc("PenisSize", TargetData, "DSP")} to fuck {AName}'s {Desc("ATightness", ActorData, "DSP")} in the lotus position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":130,
                }
            ActorDict = {
                "State":{
                    "Mood": 10,
                    "Energy": -40,
                    "Excitement": 9,
                    "Arousal": 7,
                    },
                "Temporal":{
                    "Favor": 35,
                    "Loyalty": 35,
                    "Desire": 20,
                    "Shame": 35,
                    "APlea": 30,
                    },
                "Permanent":{
                    "Attraction": 2,
                    "Reliability": 2,
                    "AExp": 1,
                    "APenetrationExp": 1,
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Getting anally fucked by {TName}''', "LongFluff": f'''{AName} is having {APPos} {Desc("ATightness", ActorData, "DSP")} fucked by {TName}'s {Desc("PenisSize", TargetData, "DSP")} in the lotus position.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Failing to get anally fucked by {TName}''', "LongFluff": f'''{AName} is failing to get anally fucked by {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 15,
                    "Task": ["Skinship", {"BriefFluff": f'''Trying to focuse while getting anally fucked by {TName}''', "LongFluff": f'''{AName} is trying to focus while having {APPos} {Desc("ATightness", ActorData, "DSP")} fucked by {TName}'s {Desc("PenisSize", TargetData, "DSP")} in the lotus position.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                    },
                "Connotations":{},
                "Resistance":110,
                }
            OtherData = {
                "Success":2,
                }

        elif CommandID == "StopSex0":
            TargetDict = {
                "State":{
                    "Energy": -0,
                    },
                "Temporal":{
                    "Discomfort": 15,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 5,
                    "Task": ["PushedDown", {"BriefFluff": f'''Stopping being intimate with {AName}''', "LongFluff": f'''{TName} is stopping being intimate with {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 5,
                    "Task": ["PushedDown", {"BriefFluff": f'''Refusing to stop being intimate with {AName}''', "LongFluff": f'''{TName} is refusing to stop being intimate with {AName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 5,
                    "Task": ["PushedDown", {"BriefFluff": f'''Focuing on stopping being intimate with {AName}''', "LongFluff": f'''{TName} is trying to focus on stopping being intimate with {AName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"],
                },
                "Connotations":{},
                "Resistance":15,
                }
            ActorDict = {
                "State":{
                    "Energy": -0,
                    },
                "Temporal":{
                    "Discomfort": 15,
                    },
                "Permanent":{
                    },
                "Task":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 5,
                    "Task": ["PushedDown", {"BriefFluff": f'''Stopping being intimate with {TName}''', "LongFluff": f'''{AName} is stopping being intimate with {TName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Actor]["Actions"]["CurrentTask"]["Location"],
                },
                "ForcefulTask":{},
                "ResistanceTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 5,
                    "Task": ["PushedDown", {"BriefFluff": f'''Trying stop being intimate with {TName}''', "LongFluff": f'''{AName} is trying to stop being intimate with {TName}.'''}],
                    "InterruptionPenalty": -20,
                    "Location": Globals.SoLNPCData[Actor]["Actions"]["CurrentTask"]["Location"],
                },
                "EnergyTask":{
                    "HourStart": DateData["Hour"],
                    "HourFinish": DateData["Hour"] + 5,
                    "Task": ["PushedDown", {"BriefFluff": f'''Trying to focus on stopping being intiamte with {TName}''', "LongFluff": f'''{AName} is trying to focus while stopping being intimate with {TName}.'''}],
                    "InterruptionPenalty": 20,
                    "Location": Globals.SoLNPCData[Actor]["Actions"]["CurrentTask"]["Location"],
                },
                "Connotations":{},
                "Resistance":15,
                }
            OtherData = {
                "Success":2,
                }

        if TargetDict != {} and ActorDict != {}:
            TargetConnotations, ActorConnotations = GetConnotations(self, CommandID, Actor, Target, OtherData)
            TargetDict["Connotations"] = TargetConnotations
            ActorDict["Connotations"] = ActorConnotations

            # # CTS2 SIGNAL
            # Data = Globals.SignalData["CTS2"]["Values"]
            # Data["CommandID"], Data["Modification"], Data["Implementation"], Data["Target"], Data["Actor"], Data["TargetDict"], Data["ActorDict"] = CommandID, Modification, Implementation, Target, Actor, TargetDict, ActorDict
            # self.CTS2.emit()
            # CommandID, Modification, Implementation, Target, Actor, TargetDict, ActorDict = Data["CommandID"], Data["Modification"], Data["Implementation"], Data["Target"], Data["Actor"], Data["TargetDict"], Data["ActorDict"]
            # #

            OriginalData = {"TargetDict":TargetDict, "ActorDict":ActorDict, "CommandID":CommandID, "Target":Target, "Actor":Target}
            FinalData = Globals.References["SoLFunctions"].CommandsProcessing(self, TargetDict, ActorDict, CommandID, Target, Actor, Modification, Implementation)

            ConfirmCommand(self, FinalData)

            # # CTS3 SIGNAL
            # Data = Globals.SignalData["CTS3"]["Values"]
            # Data["Modification"], Data["Implementation"], Data["OriginalData"], Data["FinalData"] = Modification, Implementation, OriginalData, FinalData
            # self.CTS3.emit()
            # Modification, Implementation, OriginalData, FinalData = Data["Modification"], Data["Implementation"], Data["OriginalData"], Data["FinalData"]
            # #

            return FinalData

    except Exception as e:
        Log(3, "ERROR COMMAND TRIGGERED", e, __name__, CommandID, Actor, Target)

def ConfirmCommand(self, FinalData):
    try:
        if FinalData["CommandID"] == "PushDown0":
            if FinalData["CommandStatus"] == "Success" or FinalData["CommandStatus"] == "EnergyFailed":
                Target = FinalData["Target"]
                Actor = FinalData["Actor"]
                if Target not in Globals.SoLNPCData[Actor]["Actions"]["isInSexScene"]: Globals.SoLNPCData[Actor]["Actions"]["isInSexScene"].append(Target)
                if Actor not in Globals.SoLNPCData[Target]["Actions"]["isInSexScene"]: Globals.SoLNPCData[Target]["Actions"]["isInSexScene"].append(Actor)
        elif FinalData["CommandID"] == "StopSex0":
            if FinalData["CommandStatus"] == "Success" or FinalData["CommandStatus"] == "EnergyFailed":
                Target = FinalData["Target"]
                Actor = FinalData["Actor"]
                if Target in Globals.SoLNPCData[Actor]["Actions"]["isInSexScene"]: Globals.SoLNPCData[Actor]["Actions"]["isInSexScene"].remove(Target)
                if Actor in Globals.SoLNPCData[Target]["Actions"]["isInSexScene"]: Globals.SoLNPCData[Target]["Actions"]["isInSexScene"].remove(Actor)
        elif FinalData["CommandID"] == "GetFollow0":
            if FinalData["CommandStatus"] == "Success" or FinalData["CommandStatus"] == "EnergyFailed":
                Target = FinalData["Target"]
                Actor = FinalData["Actor"]
                Globals.SoLNPCData[Target]["Actions"]["IsFollowing"] = [Actor,5]
                Globals.SoLNPCData[Actor]["Actions"]["HasFollowing"].append(Target)
    except Exception as e:
        Log(3,"ERROR ConfirmCommand", e, FinalData)

def GetConnotations(self, CommandID, Actor, Target, OtherData):
    if CommandID == "Conversation0":
        TargetConnotations = {
            "Simple":[1,0],
            "Basic":[1,100],
        }
        ActorConnotations = {
            "Simple":[1,0],
            "Basic":[1,100],
        }
    elif CommandID == "Skinship0":
        TargetConnotations = {
            "Simple":[1,0],
            "Passive":[1,0],
            "Playful":[2,60],
            "Basic":[1,50],
            }
        ActorConnotations = {
            "Simple":[1,0],
            "Active":[1,0],
            "Playful":[2,60],
            "Basic":[1,50],
            }
    elif CommandID == "ServeThem0":
        TargetConnotations = {
            "Simple":[1,10],
            "Basic":[1,0],
            "Dominant":[1,10],
            }
        ActorConnotations = {
            "Simple":[1,5],
            "Basic":[1,0],
            "Submissive":[1,25],
            "Friendly":[1,5],
            "Service":[1,15],
            }
    elif CommandID == "GetLapPillow0":
        TargetConnotations = {
            "Simple":[1,0],
            "Passive":[1,10],
            "Intimate":[1,15],
            "Submissive":[1,15],
            }
        ActorConnotations = {
            "Simple":[1,0],
            "Active":[1,10],
            "Extroverted":[1,25],
            "Intimate":[1,15],
            }
    elif CommandID == "GiveLapPillow0":
        TargetConnotations = {
            "Simple":[1,0],
            "Intimate":[1,15],
            "Passive":[1,10],
            }
        ActorConnotations = {
            "Simple":[1,0],
            "Intimate":[1,15],
            "Active":[1,10],
            "Dominant":[1,15],
            "Extroverted":[1,15],
            "Friendly":[1,10],
            }
    elif CommandID == "BellyCaress0":
        TargetConnotations = {
            "Simple":[1,0],
            "Intimate":[1,10],
            "Passive":[1,5],
            "Submissive":[1,15],
            }
        ActorConnotations = {
            "Simple":[1,0],
            "Intimate":[1,5],
            "Active":[1,10],
            "Extroverted":[1,10],
            "Playful":[1,15],
            }
    elif CommandID == "PinchCheek0":
        TargetConnotations = {
            "Simple":[1,0],
            "Passive":[1,10],
            }
        ActorConnotations = {
            "Simple":[1,0],
            "Active":[1,5],
            "Dominant":[1,15],
            "Extroverted":[1,10],
            "Playful":[1,15],
            }
    elif CommandID == "ButtCaress0":
        TargetConnotations = {
            "Sexual":[1,10],
            "Passive":[1,5],
            "Submissive":[1,5],
            "Caress":[1,15],
            }
        ActorConnotations = {
            "Sexual":[1,0],
            "Active":[1,10],
            "Dominant":[1,5],
            "Extroverted":[1,10],
            "SHarassement":[1,15],
            }
    elif CommandID == "Hug0":
        TargetConnotations = {
            "Basic":[1,10],
            "Simple":[1,0],
            "Intimate":[1,10],
            "Friendly":[1,20],
            }
        ActorConnotations = {
            "Basic":[1,10],
            "Simple":[1,0],
            "Intimate":[1,10],
            "Active":[1,5],
            "Friendly":[1,20],
            }
    elif CommandID == "Kiss0":
        TargetConnotations = {
            "Basic":[1,5],
            "Simple":[1,0],
            "Intimate":[2,20],
            "Passive":[1,5],
            "Vanilla":[1,10],
            "Kiss":[1,10],
            }
        ActorConnotations = {
            "Basic":[1,5],
            "Simple":[1,0],
            "Intimate":[1,10],
            "Active":[1,5],
            "Extroverted":[1,5],
            "Friendly":[1,5],
            "Vanilla":[1,10],
            "Kiss":[1,10],
            }
    elif CommandID == "BreastCaress0":
        TargetConnotations = {
            "Sexual":[1,15],
            "Passive":[1,5],
            "Submissive":[1,5],
            "Caress":[1,5],
            "C":[1,15],
            }
        ActorConnotations = {
            "Sexual":[1,20],
            "Active":[1,10],
            "Dominant":[1,10],
            }
    elif CommandID == "AnalCaress0":
        TargetConnotations = {
            "Sexual":[2,10],
            "Passive":[1,5],
            "Submissive":[1,5],
            "A":[1,10],
            "Caress":[1,5],
            }
        ActorConnotations = {
            "Sexual":[1,10],
            "Active":[1,5],
            "Dominant":[1,10],
            }
    elif CommandID == "PussyCaress0":
        TargetConnotations = {
            "Sexual":[1,10],
            "Passive":[1,5],
            "Submissive":[1,5],
            "Caress":[1,5],
            "V":[1,15],
            }
        ActorConnotations = {
            "Sexual":[1,15],
            "Active":[1,5],
            "Dominant":[1,5],
            }
    elif CommandID == "PenisCaress0":
        TargetConnotations = {
            "Sexual":[1,10],
            "Passive":[1,5],
            "Submissive":[1,5],
            "Caress":[1,5],
            "P":[1,15],
            }
        ActorConnotations = {
            "Sexual":[1,15],
            "Active":[1,5],
            "Dominant":[1,5],
            }
    elif CommandID == "ServeAlcohol0":
        TargetConnotations = {
            "Basic":[1,10],
            "Simple":[1,0],
            "Friendly":[1,10],
            "Alcohol":[1,20],
            }
        ActorConnotations = {
            "Basic":[1,10],
            "Simple":[1,0],
            "Friendly":[1,10],
            "Service":[1,5],
            }
    elif CommandID == "PushDown0":
        TargetConnotations = {
            "Simple":[1,15],
            "Active":[1,10],
            "Sexual":[2,50],
            "StartIntimacy":[1,0],
            }
        ActorConnotations = {
            "Simple":[1,15],
            "Passive":[1,10],
            "Sexual":[2,50],
            "StartIntimacy":[1,0],
            }
    elif CommandID == "GetFollow0":
        TargetConnotations = {
            "Simple":[1,15],
            "Active":[1,10],
            }
        ActorConnotations = {
            "Simple":[1,15],
            "Passive":[1,10],
            }


    elif CommandID == "CaressSex0":
        TargetConnotations = {
            "Sexual":[1,20],
            "Passive":[1,5],
            "Submissive":[1,5],
            "Caress":[2,15],
            "C":[1,5],
            }
        ActorConnotations = {
            "Sexual":[1,15],
            "Active":[1,5],
            "Dominant":[1,5],
            "Service":[1,10],
            "Caress":[1,10],
            "Vanilla":[1,15],
            }
    elif CommandID == "GetCaressSex0":
        TargetConnotations = {
            "Sexual":[1,20],
            "Active":[1,5],
            "Submissive":[1,10],
            }
        ActorConnotations = {
            "Sexual":[1,15],
            "Passive":[1,5],
            "Dominant":[1,10],
            "Vanilla":[1,10],
            "Caress":[2,10],
            "C":[1,5],
            }

    elif CommandID == "PussyCaressSex0":
        TargetConnotations = {
            "Sexual":[1,15],
            "Intimate":[1,5],
            "Passive":[1,5],
            "Submissive":[1,5],
            "Caress":[1,15],
            "V":[1,10],
            }
        ActorConnotations = {
            "Sexual":[1,15],
            "Active":[1,10],
            "Dominant":[1,10],
            }
    elif CommandID == "GetPussyCaressSex0":
        TargetConnotations = {
            "Sexual":[1,20],
            "Active":[1,10],
            "Submissive":[1,10],
            }
        ActorConnotations = {
            "Sexual":[1,15],
            "Passive":[1,5],
            "Dominant":[1,10],
            "Vanilla":[1,5],
            "Caress":[1,15],
            "V":[1,10],
            }
    elif CommandID == "FingeringSex0":
        TargetConnotations = {
            "Sexual":[2,25],
            "Passive":[1,5],
            "Submissive":[1,5],
            "Caress":[2,15],
            "V":[1,10],
            "Intimate":[2,20],
            }
        ActorConnotations = {
            "Sexual":[2,25],
            "Active":[1,10],
            "Dominant":[1,10],
            "Intimate":[2,15],
            }
    elif CommandID == "GetFingeringSex0":
        TargetConnotations = {
            "Sexual":[2,15],
            "Active":[1,10],
            "Submissive":[2,10],
            "Intimate":[2,15],
            }
        ActorConnotations = {
            "Sexual":[2,20],
            "Passive":[1,5],
            "Dominant":[1,10],
            "Caress":[2,15],
            "V":[1,10],
            }
    elif CommandID == "CunnilingusSex0":
        TargetConnotations = {
            "Sexual":[3,30],
            "Submissive":[2,5],
            "Intimate":[1,15],
            "Passive":[1,5],
            "Lick":[1,10],
            "V":[2,20],
            }
        ActorConnotations = {
            "Sexual":[3,25],
            "Active":[1,10],
            "Dominant":[1,10],
            "Intimate":[2,15],
            }
    elif CommandID == "GetCunnilingusSex0":
        TargetConnotations = {
            "Sexual":[3,30],
            "Intimate":[2,35],
            "Active":[1,5],
            "Submissive":[1,10],
            }
        ActorConnotations = {
            "Sexual":[3,25],
            "Intimate":[2,15],
            "Passive":[1,5],
            "Dominant":[1,10],
            "Lick":[1,10],
            "V":[2,15],
            }

    elif CommandID == "PenissCaressSex0":
        TargetConnotations = {
            "Sexual":[1,15],
            "Intimate":[1,5],
            "Passive":[1,5],
            "Submissive":[1,5],
            "Caress":[1,15],
            "P":[1,10],
            }
        ActorConnotations = {
            "Sexual":[1,15],
            "Active":[1,10],
            "Dominant":[1,10],
            }
    elif CommandID == "GetPenisCaressSex0":
        TargetConnotations = {
            "Sexual":[1,20],
            "Active":[1,10],
            "Submissive":[1,10],
            }
        ActorConnotations = {
            "Sexual":[1,15],
            "Passive":[1,5],
            "Dominant":[1,10],
            "Vanilla":[1,5],
            "Caress":[1,15],
            "P":[1,10],
            }
    elif CommandID == "HandJobSex0":
        TargetConnotations = {
            "Sexual":[2,25],
            "Passive":[1,5],
            "Submissive":[1,5],
            "Caress":[2,15],
            "P":[1,10],
            "Intimate":[2,20],
            }
        ActorConnotations = {
            "Sexual":[2,25],
            "Active":[1,10],
            "Dominant":[1,10],
            "Intimate":[2,15],
            }
    elif CommandID == "GetHandjobSex0":
        TargetConnotations = {
            "Sexual":[2,15],
            "Active":[1,10],
            "Submissive":[2,10],
            "Intimate":[2,15],
            }
        ActorConnotations = {
            "Sexual":[2,20],
            "Passive":[1,5],
            "Dominant":[1,10],
            "Caress":[2,15],
            "P":[1,10],
            }
    elif CommandID == "BlowjobSex0":
        TargetConnotations = {
            "Sexual":[3,30],
            "Submissive":[2,5],
            "Intimate":[1,15],
            "Passive":[1,5],
            "Lick":[1,10],
            "P":[2,20],
            }
        ActorConnotations = {
            "Sexual":[3,25],
            "Active":[1,10],
            "Dominant":[1,10],
            "Intimate":[2,15],
            }
    elif CommandID == "GetBlowjobSex0":
        TargetConnotations = {
            "Sexual":[3,30],
            "Intimate":[2,35],
            "Active":[1,5],
            "Submissive":[1,10],
            }
        ActorConnotations = {
            "Sexual":[3,25],
            "Intimate":[2,15],
            "Passive":[1,5],
            "Dominant":[1,10],
            "Lick":[1,10],
            "P":[2,15],
            }

    elif CommandID == "BreastCaressSex0":
        TargetConnotations = {
            "Sexual":[1,15],
            "Passive":[1,5],
            "Submissive":[1,5],
            "Caress":[1,5],
            "C":[1,15],
            }
        ActorConnotations = {
            "Sexual":[1,20],
            "Active":[1,10],
            "Dominant":[1,10],
            }
    elif CommandID == "GetBreastCaressSex0":
        TargetConnotations = {
            "Sexual":[1,15],
            "Active":[1,5],
            "Submissive":[1,10],
            }
        ActorConnotations = {
            "Sexual":[1,15],
            "Passive":[1,5],
            "Dominant":[1,10],
            "Caress":[1,10],
            "C":[1,10],
            }
    elif CommandID == "NippleTeaseSex0":
        TargetConnotations = {
            "Sexual":[1,15],
            "Passive":[1,5],
            "Submissive":[1,5],
            "Caress":[2,20],
            "C":[1,15],
            }
        ActorConnotations = {
            "Sexual":[1,25],
            "Active":[1,5],
            "Dominant":[1,5],
            }
    elif CommandID == "GetNippleTeaseSex0":
        TargetConnotations = {
            "Sexual":[1,15],
            "Active":[1,5],
            "Submissive":[1,10],
            }
        ActorConnotations = {
            "Sexual":[1,15],
            "Passive":[1,5],
            "Dominant":[1,10],
            "Caress":[2,15],
            "C":[1,15],
            }
    elif CommandID == "NippleSuckingSex0":
        TargetConnotations = {
            "Sexual":[2,25],
            "Passive":[1,5],
            "Submissive":[1,5],
            "Lick":[1,10],
            "C":[2,20],
            }
        ActorConnotations = {
            "Sexual":[2,25],
            "Active":[1,10],
            "Dominant":[1,10],
            }
    elif CommandID == "GetNippleSuckingSex0":
        TargetConnotations = {
            "Sexual":[2,25],
            "Active":[1,5],
            "Submissive":[1,15],
            }
        ActorConnotations = {
            "Sexual":[2,25],
            "Passive":[1,5],
            "Dominant":[1,15],
            "Lick":[1,10],
            "C":[1,10],
            }

    elif CommandID == "AnalCaressSex0":
        TargetConnotations = {
            "Sexual":[2,15],
            "Passive":[1,5],
            "Submissive":[1,5],
            "A":[1,10],
            "Caress":[1,10],
            }
        ActorConnotations = {
            "Sexual":[2,15],
            "Active":[1,5],
            "Dominant":[1,10],
            }
    elif CommandID == "GetAnalCaressSex0":
        TargetConnotations = {
            "Sexual":[2,15],
            "Active":[1,5],
            "Submissive":[2,20],
            }
        ActorConnotations = {
            "Sexual":[2,15],
            "Passive":[1,5],
            "Dominant":[1,10],
            "Caress":[1,10],
            "A":[1,10],
            }
    elif CommandID == "AnalFingeringSex0":
        TargetConnotations = {
            "Sexual":[3,20],
            "Passive":[1,5],
            "Submissive":[1,10],
            "Caress":[3,10],
            "A":[1,15],
            }
        ActorConnotations = {
            "Sexual":[3,25],
            "Active":[1,5],
            "Dominant":[1,10],
            }
    elif CommandID == "GetAnalFingeringSex0":
        TargetConnotations = {
            "Sexual":[3,30],
            "Active":[1,5],
            "Submissive":[2,25],
            }
        ActorConnotations = {
            "Sexual":[3,25],
            "Passive":[1,5],
            "Dominant":[2,15],
            "Caress":[1,10],
            "A":[1,10],
            }
    elif CommandID == "RimjobSex0":
        TargetConnotations = {
            "Sexual":[4,30],
            "Passive":[1,5],
            "Submissive":[2,10],
            "Deviant":[1,15],
            "Lick":[1,10],
            "A":[2,15],
            }
        ActorConnotations = {
            "Sexual":[4,30],
            "Active":[1,5],
            "Dominant":[1,5],
            "Deviant":[1,15],
            }
    elif CommandID == "GetRimjobSex0":
        TargetConnotations = {
            "Sexual":[4,35],
            "Active":[1,5],
            "Submissive":[2,25],
            "Deviant":[1,10],
            "Masochist":[1,5],
            }
        ActorConnotations = {
            "Sexual":[4,35],
            "Passive":[1,5],
            "Dominant":[1,10],
            "Deviant":[1,15],
            "Sadist":[1,5],
            "Lick":[1,5],
            "A":[2,15],
            }

    elif CommandID == "MasturbateSex0":
        TargetConnotations = {
            "Sexual":[1,15],
            "Passive":[1,5],
            }
        ActorConnotations = {
            "Sexual":[1,10],
            "Intimate":[1,5],
            "Active":[1,5],
            "Dominant":[1,5],
            "Extroverted":[1,5],
            "Caress":[1,10],
            "C":[1,5],
            "Exhibitionist":[1,10],
            }
    elif CommandID == "GetMasturbateSex0":
        TargetConnotations = {
            "Sexual":[1,15],
            "Intimate":[1,10],
            "Active":[1,5],
            "Submissive":[1,5],
            "Exhibitionist":[1,10],
            "Caress":[1,10],
            "C":[1,5],
            }
        ActorConnotations = {
            "Sexual":[1,15],
            "Passive":[1,5],
            "Dominant":[1,10],
            }
    elif CommandID == "AMasturbateSex0":
        TargetConnotations = {
            "Sexual":[1,20],
            "Passive":[1,5],
            }
        ActorConnotations = {
            "Sexual":[1,15],
            "Intimate":[1,5],
            "Active":[1,5],
            "Dominant":[1,5],
            "Extroverted":[1,5],
            "Caress":[1,10],
            "A":[1,5],
            "Exhibitionist":[1,15],
            }
    elif CommandID == "GetAMasturbateSex0":
        TargetConnotations = {
            "Sexual":[1,20],
            "Active":[1,5],
            "Submissive":[1,10],
            "Exhibitionist":[1,15],
            "Caress":[1,10],
            "C":[1,5],
            }
        ActorConnotations = {
            "Sexual":[1,15],
            "Passive":[1,5],
            "Dominant":[1,10],
            }

    elif CommandID == "FootjobSex0":
        TargetConnotations = {
            "Sexual":[1,10],
            "Active":[1,5],
            "Submissive":[1,5],
            "Caress":[1,5],
            }
        ActorConnotations = {
            "Sexual":[1,10],
            "Passive":[1,10],
            "Dominant":[1,10],
            }
    elif CommandID == "GetFootjobSex0":
        TargetConnotations = {
            "Sexual":[1,10],
            "Active":[1,5],
            "Submissive":[1,15],
            }
        ActorConnotations = {
            "Sexual":[1,10],
            "Passive":[1,5],
            "Dominant":[1,15],
            "Caress":[1,5],
            }
    elif CommandID == "ButtjonbSex0":
        TargetConnotations = {
            "Sexual":[2,15],
            "Active":[1,10],
            "Submissive":[1,5],
            "Caress":[1,5],
            "P":[1,10],
            }
        ActorConnotations = {
            "Sexual":[2,20],
            "Passive":[1,10],
            "Dominant":[1,10],
            }
    elif CommandID == "GetButtjonbSex0":
        TargetConnotations = {
            "Sexual":[1,15],
            "Active":[1,5],
            "Submissive":[2,20],
            }
        ActorConnotations = {
            "Sexual":[1,15],
            "Passive":[1,5],
            "Dominant":[2,20],
            "Caress":[1,5],
            "P":[1,5],
            }
    elif CommandID == "ThighjobSex0":
        TargetConnotations = {
            "Sexual":[2,15],
            "Intimate":[1,10],
            "Active":[1,10],
            "Submissive":[1,5],
            "Caress":[1,5],
            "P":[1,15],
            }
        ActorConnotations = {
            "Sexual":[2,20],
            "Passive":[2,15],
            "Dominant":[1,10],
            "Caress":[1,3],
            "V":[1,3],
            }
    elif CommandID == "GetThighjobSex0":
        TargetConnotations = {
            "Sexual":[2,20],
            "Intimate":[1,10],
            "Active":[1,5],
            "Submissive":[2,20],
            }
        ActorConnotations = {
            "Sexual":[2,20],
            "Passive":[1,5],
            "Dominant":[2,25],
            "Caress":[1,5],
            "P":[1,5],
            }
    elif CommandID == "TitjobSex0":
        TargetConnotations = {
            "Sexual":[2,15],
            "Active":[1 ,15],
            "Submissive":[1,5],
            "Caress":[1,10],
            "P":[1,15],
            }
        ActorConnotations = {
            "Sexual":[2,20],
            "Passive":[2,10],
            "Dominant":[1,10],
            }
    elif CommandID == "GetTitjobSex0":
        TargetConnotations = {
            "Sexual":[2,25],
            "Active":[1,5],
            "Submissive":[2,25],
            }
        ActorConnotations = {
            "Sexual":[2,20],
            "Passive":[1,5],
            "Dominant":[2,20],
            "Caress":[1,5],
            "P":[1,10],
            }

    elif CommandID == "FacesittingSex0":
        TargetConnotations = {
            "Sexual":[3,25],
            "Passive":[1,5],
            "Submissive":[2,20],
            "Humilliation":[2,25],
            }
        ActorConnotations = {
            "Sexual":[3,25],
            "Active":[1,5],
            "Dominant":[2,20],
            "Sadist":[1,10],
            "Lick":[1,5],
            }
    elif CommandID == "GetFacesittingSex0":
        TargetConnotations = {
            "Sexual":[3,35],
            "Active":[1,10],
            "Submissive":[1,10],
            "Lick":[1,10],
            }
        ActorConnotations = {
            "Sexual":[3,25],
            "Passive":[1,10],
            "Dominant":[1,10],
            "Humilliation":[2,25],
            }
    elif CommandID == "AFacesittingSex0":
        TargetConnotations = {
            "Sexual":[4,40],
            "Passive":[1,5],
            "Submissive":[2,20],
            "Deviant":[1,10],
            "Humilliation":[2,25],
            }
        ActorConnotations = {
            "Sexual":[4,35],
            "Passive":[1,5],
            "Dominant":[2,25],
            "Deviant":[1,10],
            "Sadist":[1,10],
            "Lick":[1,5],
            "A":[2,20],
            }
    elif CommandID == "GetAFacesittingSex0":
        TargetConnotations = {
            "Sexual":[4,35],
            "Active":[1,5],
            "Submissive":[2,15],
            "Deviant":[1,10],
            "Humilliation":[1,10],
            "Lick":[1,10],
            "A":[2,25],
            }
        ActorConnotations = {
            "Sexual":[4,40],
            "Passive":[1,5],
            "Dominant":[2,20],
            "Deviant":[1,15],
            }

    elif CommandID == "AssSpankingSex0":
        TargetConnotations = {
            "Sexual":[1,10],
            "Passive":[1,5],
            "Submissive":[2,20],
            "Abuse":[1,15],
            "Masochist":[1,15],
            }
        ActorConnotations = {
            "Sexual":[1,10],
            "Active":[1,5],
            "Dominant":[1,10],
            "Sadist":[1,15],
            }
    elif CommandID == "GetAssSpankingSex0":
        TargetConnotations = {
            "Sexual":[1,10],
            "Active":[1,5],
            "Submissive":[1,10],
            "Sadist":[1,15],
            }
        ActorConnotations = {
            "Sexual":[1,10],
            "Passive":[1,5],
            "Dominant":[1,5],
            "Masochist":[1,15],
            "Abuse":[1,15],
            }
    elif CommandID == "BreastSlappingSex0":
        TargetConnotations = {
            "Sexual":[1,10],
            "Passive":[1,5],
            "Submissive":[1,15],
            "Abuse":[1,10],
            "Masochist":[1,10],
            "C":[1,10],
            }
        ActorConnotations = {
            "Sexual":[1,15],
            "Active":[1,5],
            "Dominant":[1,10],
            "Sadist":[1,10],
            }
    elif CommandID == "GetBreastSlappingSex0":
        TargetConnotations = {
            "Sexual":[1,15],
            "Active":[1,5],
            "Submissive":[1,10],
            "Sadist":[1,10],
            }
        ActorConnotations = {
            "Sexual":[1,15],
            "Passive":[1,5],
            "Dominant":[1,5],
            "Masochist":[1,10],
            "Abuse":[1,10],
            "C":[1,15],
            }

    elif CommandID == "MissionarySex0":
        TargetConnotations = {
            "Sexual":[4,40],
            "Intimate":[3,35],
            "Passive":[1,10],
            "Submissive":[1,10],
            "Vanilla":[2,25],
            "Penetration":[2,20],
            "V":[3,20],
            }
        ActorConnotations = {
            "Sexual":[4,40],
            "Intimate":[3,35],
            "Active":[1,10],
            "Dominant":[1,10],
            "Vanilla":[2,25],
            "P":[3,20],
            }
    elif CommandID == "GetMissionarySex0":
        TargetConnotations = {
            "Sexual":[4,40],
            "Intimate":[3,35],
            "Active":[1,5],
            "Submissive":[1,15],
            "Vanilla":[2,25],
            "P":[3,20],
            }
        ActorConnotations = {
            "Sexual":[4,40],
            "Intimate":[3,35],
            "Passive":[1,5],
            "Dominant":[1,15],
            "Vanilla":[2,25],
            "Penetration":[2,20],
            "V":[3,20],
            }
    elif CommandID == "DoggyStyleSex0":
        TargetConnotations = {
            "Sexual":[4,45],
            "Passive":[1,15],
            "Submissive":[1,15],
            "Penetration":[2,25],
            "V":[3,35],
            }
        ActorConnotations = {
            "Sexual":[4,45],
            "Active":[1,15],
            "Dominant":[1,15],
            "P":[3,35],
            }
    elif CommandID == "GetDoggyStyleSex0":
        TargetConnotations = {
            "Sexual":[4,45],
            "Active":[1,10],
            "Submissive":[2,20],
            "P":[3,35],
            }
        ActorConnotations = {
            "Sexual":[4,45],
            "Passive":[1,15],
            "Dominant":[1,10],
            "Penetration":[2,25],
            "V":[3,25],
            }
    elif CommandID == "GetCowgirlSex0":
        TargetConnotations = {
            "Sexual":[4,45],
            "Active":[3,35],
            "Submissive":[1,10],
            "Penetration":[2,25],
            "V":[3,35],
            }
        ActorConnotations = {
            "Sexual":[4,45],
            "Passive":[2,25],
            "Dominant":[1,10],
            "P":[3,35],
            }
    elif CommandID == "CowgirlSex0":
        TargetConnotations = {
            "Sexual":[4,45],
            "Pasive":[1,15],
            "Submissive":[1,15],
            "P":[3,35],
            }
        ActorConnotations = {
            "Sexual":[4,45],
            "Active":[3,35],
            "Dominant":[2,25],
            "Penetration":[2,20],
            "V":[3,35],
            }
    elif CommandID == "LotusSex0":
        TargetConnotations = {
            "Sexual":[4,40],
            "Intimate":[5,55],
            "Passive":[1,10],
            "Submissive":[1,10],
            "Vanilla":[3,35],
            "Penetration":[2,20],
            "V":[3,20],
            }
        ActorConnotations = {
            "Sexual":[4,40],
            "Intimate":[5,55],
            "Active":[1,10],
            "Dominant":[1,10],
            "Vanilla":[3,35],
            "P":[3,20],
            }
    elif CommandID == "GetLotusSex0":
        TargetConnotations = {
            "Sexual":[4,40],
            "Intimate":[5,55],
            "Active":[1,10],
            "Submissive":[2,25],
            "Vanilla":[3,35],
            "P":[3,20],
            }
        ActorConnotations = {
            "Sexual":[4,40],
            "Intimate":[5,55],
            "Passive":[1,10],
            "Dominant":[1,15],
            "Vanilla":[3,35],
            "Penetration":[2,20],
            "V":[3,20],
            }

    elif CommandID == "AMissionarySex0":
        TargetConnotations = {
            "Sexual":[4,45],
            "Intimate":[3,35],
            "Passive":[1,10],
            "Submissive":[1,10],
            "Penetration":[2,20],
            "A":[3,20],
            }
        ActorConnotations = {
            "Sexual":[4,45],
            "Intimate":[3,35],
            "Active":[1,10],
            "Dominant":[1,10],
            "P":[3,20],
            }
    elif CommandID == "GetAMissionarySex0":
        TargetConnotations = {
            "Sexual":[4,45],
            "Intimate":[3,35],
            "Active":[1,5],
            "Submissive":[1,15],
            "P":[3,20],
            }
        ActorConnotations = {
            "Sexual":[4,45],
            "Intimate":[3,35],
            "Passive":[1,5],
            "Dominant":[1,15],
            "Penetration":[2,20],
            "A":[3,20],
            }
    elif CommandID == "ADoggyStyleSex0":
        TargetConnotations = {
            "Sexual":[4,50],
            "Passive":[1,15],
            "Submissive":[1,15],
            "Penetration":[2,25],
            "A":[3,35],
            }
        ActorConnotations = {
            "Sexual":[4,50],
            "Active":[1,15],
            "Dominant":[1,15],
            "P":[3,35],
            }
    elif CommandID == "GetADoggyStyleSex0":
        TargetConnotations = {
            "Sexual":[4,50],
            "Active":[1,10],
            "Submissive":[2,20],
            "P":[3,35],
            }
        ActorConnotations = {
            "Sexual":[4,50],
            "Passive":[1,15],
            "Dominant":[1,10],
            "Penetration":[2,25],
            "A":[3,25],
            }
    elif CommandID == "GetCowgirlSex0":
        TargetConnotations = {
            "Sexual":[4,50],
            "Active":[3,35],
            "Submissive":[1,10],
            "Penetration":[2,25],
            "A":[3,35],
            }
        ActorConnotations = {
            "Sexual":[4,50],
            "Passive":[2,25],
            "Dominant":[1,10],
            "P":[3,35],
            }
    elif CommandID == "CowgirlSex0":
        TargetConnotations = {
            "Sexual":[4,50],
            "Pasive":[1,15],
            "Submissive":[1,15],
            "P":[3,35],
            }
        ActorConnotations = {
            "Sexual":[4,45],
            "Active":[3,35],
            "Dominant":[2,25],
            "Penetration":[2,20],
            "A":[3,35],
            }
    elif CommandID == "LotusSex0":
        TargetConnotations = {
            "Sexual":[4,45],
            "Intimate":[5,55],
            "Passive":[1,10],
            "Submissive":[1,10],
            "Vanilla":[3,35],
            "Penetration":[2,20],
            "A":[3,20],
            }
        ActorConnotations = {
            "Sexual":[4,45],
            "Intimate":[5,55],
            "Active":[1,10],
            "Dominant":[1,10],
            "Vanilla":[3,35],
            "P":[3,20],
            }
    elif CommandID == "GetALotusSex0":
        TargetConnotations = {
            "Sexual":[4,45],
            "Intimate":[5,55],
            "Active":[1,10],
            "Submissive":[2,25],
            "Vanilla":[3,35],
            "P":[3,20],
            }
        ActorConnotations = {
            "Sexual":[4,45],
            "Intimate":[5,55],
            "Passive":[1,10],
            "Dominant":[1,15],
            "Vanilla":[3,35],
            "Penetration":[2,20],
            "A":[3,20],
            }
    elif CommandID == "StopSex0":
        TargetConnotations = {
            "Simple":[1,15],
            "Active":[1,10],
            "Sexual":[2,50],
            "EndIntimacy":[1,0],
            }
        ActorConnotations = {
            "Simple":[1,15],
            "Passive":[1,10],
            "Sexual":[2,50],
            "EndIntimacy":[1,0],
            }


    else:
        TargetConnotations = {}
        ActorConnotations = {}



    return TargetConnotations, ActorConnotations
def Initialize(self, Reference):
    GetCommands(self, Reference)
