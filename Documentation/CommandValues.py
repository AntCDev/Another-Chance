TargetDict = {
    "State":{
        "Mood": 2,
        "Energy": -10,
        "Excitement": 0,
        "Arousal": 0,
        "Intoxication": 0,
        },
    "Temporal":{
        "Favor": 15,
        "Loyalty": 5,
        "Desire": 0,
        "Obedience": 0,
        "Superiority": 0,
        "Submission": 0,
        "Service": 0,
        "Shame": 0,

        "MPlea": 0,
        "CPlea": 0,
        "APlea": 0,
        "VPlea": 0,
        "PPlea": 0,

        "Pain": 0,
        "Fear": 0,
        "Discomfort": 5,
        "Hate": 0,
        },
    "Permanent":{
        "Attraction": 0,
        "Reliability": 0,
        "SpeechExp": 0,

        "MExp": 0,
        "MOrgasmExp": 0,
        "MPenetrationExp": 0,

        "CExp": 0,
        "COrgasmExp": 0,
        "CPenetrationExp": 0,

        "AEXP": 0,
        "AOrgasmExp": 0,
        "APenetrationExp": 0,

        "VExp": 0,
        "VOrgasmExp": 0,
        "VPenetrationExp": 0,

        "PExp": 0,
        "POrgasmExp": 0,
        "PPenetrationExp": 0,

        "AbnormalPenetrationExp": 0,

        "CaressExp": 0,
        "LickExp": 0,
        "PenetrateExp": 0,

        "ServiceExp": 0,
        "AlcoholExp": 0,
        },
    "Task":{
        "HourStart": DateData["Hour"],
        "HourFinish": DateData["Hour"] + 10,
        "Task": ["Idlying", {"BriefFluff": f'''Listening to {Globals.SoLNPCData[Actor]["Name"]}''', "LongFluff": f'''{Globals.SoLNPCData[Target]["Name"]} is listening to {Globals.SoLNPCData[Actor]["Name"]}.'''}],
        "InterruptionPenalty": -50,
        "Location": Globals.SoLNPCData[Target]["Actions"]["CurrentTask"]["Location"]
        },
    "Connotations":{
        "Simple":[0,0],

        "Basic":[0,0],
        "Sexual":[0,0],

        "Intimate":[0,0],
        "Active":[0,0],
        "Passive":[0,0],
        "Dominant":[0,0],
        "Submissive":[0,0],
        "Extroverted":[0,0],
        "Introverted":[0,0],

        "StartIntimacy":[0,0],
        "EndIntimacy":[0,0],

        "Friendly":[1,100],
        "Speech":[1,20],
        "Sing":[0,0],
        "Dance":[0,0],
        "Service":[0,0],
        "Playful":[0,0],
        "Serious":[0,0],
        "Gamble":[0,0],
        "Gift":[0,0],

        "Vanilla":[0,0],
        "Deviant":[0,0],
        "Agressive":[0,0],
        "SHarassement":[0,0],
        "Sadist":[0,0],
        "Masochist":[0,0],
        "Abuse":[0,0],
        "Humilliation":[0,0],
        "Homosexual":[0,0],
        "Bestiality":[0,0],
        "Watersports":[0,0],
        "Scat":[0,0],
        "Abnormal":[0,0],
        "Drugs":[0,0],
        "Alcohol":[0,0],
        "Exhibitionist":[0,0],
        "SexToy":[0,0],
        "Filth":[0,0],

        "Caress":[0,0],
        "Lick":[0,0],
        "Penetration"[0,0],

        "AbnormalPenetration":[0,0],
        "ExtremePenetration":[0,0],
        "MultiplePenetration":[0,0],

        "M":[0,0],
        "C":[0,0],
        "V":[0,0],
        "A":[0,0],
        "U":[0,0],
        "W":[0,0],

        "P":[0,0],
        "T":[0,0],
    },
    "Resistance":-40,
}

# M: Mouth
# C: Chest
# N: Nipples
# V: Vaginal
# A: Anal
# P: Penis
# B: Balls
# U: Urethra
# W: Womb
# T: SexToy

TargetDict = {
    "State":{

        },
    "Temporal":{

        },
    "Permanent":{

        },
    "Task":{},
    "ForcefulTask":{},
    "ResistanceTask":{},
    "EnergyTask":{},
    "Connotations":{

        },
    "Resistance":0
    }
ActorDict = {
    "State":{

        },
    "Temporal":{

        },
    "Permanent":{

        },
    "Task":{},
    "ForcefulTask":{},
    "ResistanceTask":{},
    "EnergyTask":{},
    "Connotations":{

        },
    "Resistance":0
    }
OtherData = {
    "Success":2
    }
