import random
import Globals
Log = Globals.Layouts["MainF"].Log


def Initialize(self, Reference):


    List = ["Standard0"]
    for PersonalityID in List:
        Globals.SoLPersonalities[PersonalityID] = {"ID":PersonalityID, "Reference":Reference, "OtherData":{}}
    # CheckIdleAction(self,"02")

    Globals.References["SoLFunctions"].Connect("TPS", TPSHandling)

def TPSHandling():
    ""
    # for NPCID in Globals.SoLNPCData:
    #     if Globals.SoLNPCData[NPCID]["Personality"] == "Standard0":
    #         if Globals.SoLNPCData[NPCID]["State"]["Energy"] < 50:
    #             Globals.References["SoLFunctions"].Sleep(480, NPCID)
    #             print("Sleep", NPCID)


def CheckIdleAction(self, ID):
    try:
        Personality = Globals.SoLNPCData[ID]["Personality"]

        if Personality == "Standard0":

            # CHECKS FOR POSSIBLE SLEEP
            # if True:
            if Globals.SoLNPCData[ID]["State"]["Energy"] > 50:

                # WAKES THE CHARACTER UP
                Globals.SoLNPCData[ID]["State"]["PConscious"] = 1
                Globals.SoLNPCData[ID]["State"]["MConscious"] = 1

                # CHECKS FOR RANDOM MOVEMENT
                if Globals.SoLNPCData[ID]["Actions"]["InteractionParty"] == [] and Globals.SoLNPCData[ID]["Actions"]["Targeting"] == None:
                    if random.random() > 0.8:
                        CheckMovement(self, ID)

                # CHECKS FOR POSSIBLE ACTIONS
                Sociability = 0.6
                if random.random() > Sociability:
                    NPCData = Globals.SoLNPCData[ID]
                    NPCData["Actions"]["InteractionParty"] = []
                    NPCLocation = NPCData["Actions"]["CurrentTask"]["Location"]
                    inHere = Globals.SoLEnviorementData["Locations"][NPCLocation]["inHere"]

                    List = []
                    for OtherID in Globals.SoLEnviorementData["Locations"][NPCLocation]["inHere"]:
                        if OtherID != ID:
                            List.append(OtherID)

                    # if NPCData["Actions"]["InteractionParty"] != []:
                    #     List = list(set(List + NPCData["Actions"]["InteractionParty"]))
                    # if NPCData["Actions"]["Targeting"] != None and NPCData["Actions"]["Targeting"] != []:
                    #     if NPCData["Actions"]["Targeting"] not in List:
                    #         List.append(NPCData["Actions"]["Targeting"])

                    PCID = Globals.SoLPCData["ID"]
                    if PCID in List:
                        List.remove(PCID)
                    if List != []:
                        NPCWeights = {}
                        for NPCOther in List:
                            try:
                                Weight = NPCData["Relations"][NPCOther]["Permanent"]["Attraction"] + NPCData["Relations"][NPCOther]["Permanent"]["Reliability"] - NPCData["Relations"][NPCOther]["Fear"] - (NPCData["Relations"][NPCOther]["Hate"] * 3) + 75
                            except:
                                Weight = 50
                            NPCWeights[NPCOther] = Weight
                        OtherID = random.choices(list(NPCWeights.keys()), list(NPCWeights.values()))[0]
                        CheckAction(self, ID, OtherID)
            else:
                Globals.References["SoLFunctions"].Sleep(ID)
                Home = Globals.SoLNPCData[ID]["OtherData"]["Home"]
                Globals.References["SoLFunctions"].Move( Globals.Layouts["SoLUI"], Home, ID )

    except Exception as e:
        Log(3, "ERROR CheckIdleAction", e, __name__, ID)


def CheckMovement(self, ID):
    Globals.SoLNPCData[ID]


def CheckAction(self, ID, NPCID):
    CommandWeights = {}
    for CommandID in Globals.Commands:
        Available = Globals.Commands[CommandID]["Reference"].CheckCommandAvailable(self, CommandID, ID, NPCID)
        if Available == 1:
            TargetConnotations, ActorConnotations = Globals.Commands[CommandID]["Reference"].GetConnotations(self, CommandID, ID, NPCID, {"Succes":0})
            TargetConnotations, ActorConnotations = ProcessConnotations(self, ID, NPCID, "Actor", TargetConnotations, ActorConnotations)

            Weight = 0
            for Connotation in TargetConnotations:
                Weight += TargetConnotations[Connotation][1]

            CommandWeights[CommandID] = Weight
    CommandID = random.choices(list(CommandWeights.keys()), list(CommandWeights.values()))[0]
    # print(ID, NPCID, CommandID)
    Globals.Commands[CommandID]["Reference"].TriggerCommand(self, CommandID, NPCID, ID, None)

def ProcessCommand(self, ID, NPCID, Who):
    if Who == "Target":
        TargetData = Globals.SoLNPCData[ID]
        ActorData = Globals.SoLNPCData[NPCID]
    else:
        TargetData = Globals.SoLNPCData[NPCID]
        ActorData = Globals.SoLNPCData[ID]

def ProcessConnotations(self, ID, NPCID, Who, TargetConnotations, ActorConnotations):
    return TargetConnotations, ActorConnotations
    ""

def GetName(self, PersonalityID):
    if PersonalityID == "Standard0":
        return "Standard"

def CommandProcessPersonality(self, FinalData, Who):
    # FinalData.keys() = 'TargetDict', 'ActorDict', 'CommandID', 'Target', 'Actor', 'Modification', 'Implementation'
    Intimacy = 0
    Lewdity = 0
    Submission = 0
    Love = 0

    if Who == "Target":


        if Intimacy == 0:
            if "Intimacy" in FinalData:
                ""
            ""
        # print(FinalData.keys())


    # print(Who)
    return [FinalData]
