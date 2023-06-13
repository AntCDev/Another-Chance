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
                if Globals.SoLNPCData[ID]["Actions"]["InteractionParty"] == {}:
                    if random.randint(0,5) >= 5:
                        # print("MOVE", ID)
                        CheckMovement(self, ID)

                # CHECKS FOR POSSIBLE ACTIONS
                Sociability = 0.7
                if random.random() > Sociability and Globals.PlayerConfig["Interactions"] == 1:
                    NPCLocation = Globals.SoLNPCData[ID]["Actions"]["CurrentTask"]["Location"]

                    List = Globals.SoLEnviorementData["Locations"][NPCLocation]["inHere"].copy()
                    if ID in List:
                        List.remove(ID)

                        PCID = Globals.SoLPCData["ID"]
                    if Globals.PlayerConfig["NPCtoPC"] == 0:
                        if PCID in List:
                            List.remove(PCID)
                    if Globals.PlayerConfig["BetweenNPC"] == 0:
                        if PCID in List:
                            List = [PCID]
                        else:
                            List = []

                    if List != []:
                        NPCWeights = {}
                        for NPCOther in List:
                            try:
                                Weight = Globals.SoLNPCData[ID]["Relations"][NPCOther]["Permanent"]["Attraction"] + Globals.SoLNPCData[ID]["Relations"][NPCOther]["Permanent"]["Reliability"] - Globals.SoLNPCData[ID]["Relations"][NPCOther]["Fear"] - (Globals.SoLNPCData[ID]["Relations"][NPCOther]["Hate"] * 3) + 75
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
    try:
        Location = Globals.SoLNPCData[ID]["Actions"]["CurrentTask"]["Location"]
        Connected = Globals.SoLEnviorementData["Locations"][Location]["CanAccess"]
        Possible = []
        for OtherLocation in Connected:
            if Globals.SoLEnviorementData["Locations"][OtherLocation]["Flags"]["Open"] == 1:
                if ID not in Globals.SoLEnviorementData["Locations"][OtherLocation]["Forbidden"]:
                    Possible.append(OtherLocation)
            elif Globals.SoLEnviorementData["Locations"][OtherLocation]["Flags"]["Open"] == 0:
                if ID in Globals.SoLEnviorementData["Locations"][OtherLocation]["Allowed"]:
                    Possible.append(OtherLocation)

        if Possible != []:
            NewLocation = random.choice(Possible)
            Globals.References["SoLFunctions"].Move(Globals.Layouts["SoLUI"], NewLocation, ID)
    except Exception as e:
        Log(2, "ERROR CheckMovement", e, ID)




def CheckAction(self, ID, NPCID):
    try:
        CommandWeights = {}
        for CommandID in Globals.Commands:
            Available = Globals.Commands[CommandID]["Reference"].CheckCommandAvailable(self, CommandID, ID, NPCID)
            if Available == 1:

                TargetConnotations, ActorConnotations = Globals.Commands[CommandID]["Reference"].GetConnotations(self, CommandID, ID, NPCID, {"Succes":0})

                Globals.SignalData["CAS1"] = {"CommandID":CommandID, "ID":ID, "NPCID":NPCID, "Flags":{"Succes":0}, "TargetConnotations":TargetConnotations, "ActorConnotations":ActorConnotations}
                Globals.References["SoLFunctions"].Emit("CAS1")
                TargetConnotations, ActorConnotations = Globals.SignalData["CAS1"]["TargetConnotations"], Globals.SignalData["CAS1"]["ActorConnotations"]

                TargetConnotations, ActorConnotations = ProcessConnotations(self, ID, NPCID, "Actor", TargetConnotations, ActorConnotations)

                Globals.SignalData["CAS2"] = {"CommandID":CommandID, "ID":ID, "NPCID":NPCID, "Flags":{"Succes":0}, "TargetConnotations":TargetConnotations, "ActorConnotations":ActorConnotations}
                Globals.References["SoLFunctions"].Emit("CAS2")
                TargetConnotations, ActorConnotations = Globals.SignalData["CAS2"]["TargetConnotations"], Globals.SignalData["CAS2"]["ActorConnotations"]

                Weight = 0
                for Connotation in ActorConnotations:
                    Weight = Weight + ActorConnotations[Connotation][1]

                CommandWeights[CommandID] = Weight

        CommandID = Globals.References["SoLFunctions"].RandomChoice(CommandWeights)
        Globals.Commands[CommandID]["Reference"].TriggerCommand(self, CommandID, NPCID, ID, None)
    except Exception as e:
        Log(3, "ERROR CheckAction", e, "Standard0", ID, NPCID)


def ProcessCommand(self, ID, NPCID, Who):
    if Who == "Target":
        TargetData = Globals.SoLNPCData[ID]
        ActorData = Globals.SoLNPCData[NPCID]
    else:
        TargetData = Globals.SoLNPCData[NPCID]
        ActorData = Globals.SoLNPCData[ID]

def ProcessConnotations(self, ID, NPCID, Who, TargetConnotations, ActorConnotations):
    try:
        Relation = 0
        try:
            for FallenID in Globals.SoLNPCData[ID]["Relations"][NPCID]["FallenData"]:
                Relation = Globals.SoLFallenStates[FallenID].GetFallenRelationData(Globals.SoLNPCData[ID]["Relations"][NPCID]["FallenData"][FallenID])
        except:
            ""
        if Relation == 0:
            try:
                if Globals.SoLNPCData[ID]["Relations"][NPCID]["Permanent"]["InteractionExp"] >= 50:
                    Relation = 1
            except:
                ""

        if Who == "Actor":
            if "Sexual" in ActorConnotations:
                if ActorConnotations["Sexual"][0] > Relation:
                    ActorConnotations["Sexual"][1] = ActorConnotations["Sexual"][1] * (ActorConnotations["Sexual"][0] + 1 - Relation) * -1
                if True: # TOOD MAKE CHECK FOR SEXUALITY
                    if Globals.SoLNPCData[NPCID]["BodyData"]["Sex"] == Globals.SoLNPCData[NPCID]["BodyData"]["Sex"]:
                        if ActorConnotations["Sexual"][1] < 0:
                            ActorConnotations["Sexual"][1] = ActorConnotations["Sexual"][1] * 2
                        elif ActorConnotations["Sexual"][1] > 0:
                            ActorConnotations["Sexual"][1] = int(ActorConnotations["Sexual"][1] / 2)
            if "StartIntimacy" in ActorConnotations:
                if Relation < 2:
                    ActorConnotations["StartIntimacy"][1] = -50
            if "Intimate" in ActorConnotations:
                if ActorConnotations["Intimate"][0] > Relation:
                    ActorConnotations["Intimate"][1] = ActorConnotations["Intimate"][1] * (ActorConnotations["Intimate"][0] + 1 - Relation) * -1
    except Exception as e:
        Log(2, "ERROR ProcessConnotations", e, ID, NPCID, Who, TargetConnotations, ActorConnotations)

    return TargetConnotations, ActorConnotations

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
