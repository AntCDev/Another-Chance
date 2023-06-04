def getDeck(self, Deck, DrawDeck, SR):
    # UseClass, Deck, DrawDeck
    return 1, [], [], []

def getObject(self):
    return 0

def getDialogue(self, Action):

    #### STANDARD UPACKING OF DATA
    with open('NPCdata.json', 'rb') as f:
        NPCdata = json.load(f)
    with open('tempData.json', 'rb') as f:
        tempData = json.load(f)
    PCID = tempData["PlayerID"]
    TData = NPCdata[Target]
    TBodyType = TData["BodyType"]
    TName = TData["Name"]
    TStructure = TBodyType["Pronouns"]["Structure"]

    AData = NPCdata[Actor]
    ABodyType = AData["BodyType"]
    AName = AData["Name"]
    AStructure = ABodyType["Pronouns"]["Structure"]

    TARelation = TData["Relations"][Actor]
    TAFlags = TARelation["Flags"]

    ATRelation = AData["Relations"][Target]
    ATFlags = ATRelation["Flags"]


    Relation = 0
    if TAFlags["isLove"] == 1 or TAFlags["isLust"] == 1:
        Relation = 3
    elif TAFlags["isAffection"] == 1 or TAFlags["isLewd"] == 1:
        Relation = 2
    elif TAFlags["isAcquitance"] == 1:
        Relation = 1
    else:
        Relation = 0

    RLewd = 0
    if TAFlags["isLewd"] == 1:
        RLewd = 1
    if TAFlags["isLust"] == 1:
        RLewd = 2

    RAffection = 0
    if TAFlags["isAffection"] == 1:
        RAffection = 1
    if TAFlags["isLove"] == 1:
        RAffection = 2


    TypeOfCommand = commandDict["TypeOfCommand"]

    TPSub = ""
    TPObj = ""
    TPPos = ""
    TPIPos = ""

    APSub = ""
    APObj = ""
    APPos = ""
    APIPos = ""

    if TStructure == "Male":
        TPSub = TBodyType["Pronouns"]["Pronoun1"]  # He
        TPObj = TBodyType["Pronouns"]["Pronoun2"]  # Him
        TPPos = TBodyType["Pronouns"]["Pronoun3"]  # His
        TPIPos = TBodyType["Pronouns"]["Pronoun3"]  # His
    elif TStructure == "Female":
        TPSub = TBodyType["Pronouns"]["Pronoun1"]  # She
        TPObj = TBodyType["Pronouns"]["Pronoun2"]  # Her
        TPPos = TBodyType["Pronouns"]["Pronoun2"]  # Her
        TPIPos = TBodyType["Pronouns"]["Pronoun3"]  # Hers

    if AStructure == "Male":
        APSub = ABodyType["Pronouns"]["Pronoun1"]  # He
        APObj = ABodyType["Pronouns"]["Pronoun2"]  # Him
        APPos = ABodyType["Pronouns"]["Pronoun3"]  # His
        APIPos = ABodyType["Pronouns"]["Pronoun3"]  # His
    elif AStructure == "Female":
        APSub = ABodyType["Pronouns"]["Pronoun1"]  # She
        APObj = ABodyType["Pronouns"]["Pronoun2"]  # Her
        APPos = ABodyType["Pronouns"]["Pronoun2"]  # Her
        APIPos = ABodyType["Pronouns"]["Pronoun3"]  # Hers

    PossibleText = []

    if Relation == 0:
        if Action == "Conversation":
            if Actor == PCID:
                if Success == 1:
                    if ATRelation["Permanent"]["SpeechExp"] == 1:
                        P1 = f'''"Oh hey there, you are...{AName} right? I don't think i introduced myself before, I'm Leanne one of the many guards of this town, so if you ahve any problem you can come to me, things are a bit too peaceful for my taste so i'll be thankful if you find me anything interesting to do." '''
                    else:
                        RN = ranmdon.randint(0,2)
                        if RN == 0:
                            P1 = f'''"So {Actor} have you been doing well in this lovely town of ours? If you ahven't already i'd recommend you check out every place around here, except maybe the back gate unless you want to check what would've been of you if we hadn't found you first." '''
                        elif RN == 1:
                            P1 = f'''"Hmm? What i'm doing? '''
                            if TData["Actions"]["CurrentTask"] == "Idlying":
                                P1 += f'''I guess not much, jsut enjoying to see the people pass, ro waiting for anything to happen. What abotu you, do you want to go do something interesting?" '''
                            elif TData["Actions"]["CurrentTask"] == "Working":
                                P1 += f'''I'm working which is to say not much more than walking around, this job used to be a lot more exciting a few years back, but well i guess that just shows we did a good job." '''
                            elif TData["Actions"]["CurrentTask"] == "Following":
                                if PCID == TData["Actions"]["IsFollowing"]:
                                    P1 += f'''Well i'm following you, what else would i be doing? I'm also curious about where you are leading me, but i like surprises so don't spoil me." '''
                                else:
                                    P1 += f'''I'm following {NPCdata[TData["Actions"]["IsFollowing"]]["Name"]}, not exactly sure where we are going but it's always interesting to find out."'''
                            else:
                                P1 += f'''...Good question, not sure what i'm doing here, i guess we can find out together."'''
                        elif RN == 2:
                            list = []
                            if "02" in list(AData["Relations"].keys()):
                                list.append(f'''"So you've met {NPCdata["02"]["Name"]}, what can i say about her, i heard she used to help us in some way, but i never got to talk too much with her, it feels like she has her own bubble that i'm not allowed in... But you might have more luck than me if you have a taste for girls like her."''')
                            if "03" in list(AData["Relations"].keys()):
                                list.append(f'''"What do i think about {NPCdata["03"]["Name"]}? Well i guess she is to thank for how peaceful things currently are, she also tried to turn me into a paladin a few times i considered the idea but for now i think i like the normal kind of combat more. Besides that i think she is a good woman overall, i'd say give it a shot if you are interesed but that might be thought she is a very devoted woman to her duties after all."''')
                            if "04" in list(AData["Relations"].keys()):
                                list.append(f'''"{NPCdata["04"]["Name"]}?... Oh, i think i know who you are talking about, it's that ginger girl right with the twintails and all. Yeah i haven't talked too much about her, not that i have anything against her it's just that we don't move in each other's circles too much. The most i've interacted with her was when i was punished with aiding in charity and she was there, she looked a bit off but if she was there i assume she is a good girl."''')
                            if "05" in list(AData["Relations"].keys()):
                                list.append(f'''"{NPCdata["05"]["Name"]} did you say? I thought  was just imagining things but if she is really here i wonder what kind of business she has here, it'd be foolish for her to try and act up, but perhaps her hatred for that woman might make her do stupid things. Wouldn't recommend you get too involved with her, even if you are safe from a physical stand point she is stil lfamous for how cunning she is."''')
                            if "06" in list(AData["Relations"].keys()):
                                list.append(f'''"You want to know more about {NPCdata["06"]["Name"]}? Well i think you could already guess but she is a minor noble, or at least that's what she tells everyoen who insists enough, but i feel like there is more to that. Either way as i said she doesn't really talk too much with anyone below a certain level, and i'm not above it so there is not much i can tell you, but if you like troublesome girls she might be ideal for you."''')
                            if "07" in list(AData["Relations"].keys()):
                                P2 = f'''"... Oh you mean that strange girl, sorry i didn't recognized the name {NPCdata["07"]["Name"]}, but with the description i think i know who you are talking about. So about her, i think she used to be a slave, perhaps she still is, not sure, but i do know that she is in good terms with us, some of the rookies like to play with her on their free time, i myself haven't interacted too much with her, for now she looks like a weird but nice girl, but who knows how she might grow up to be, the only advice i'd give you is stay away from her mouth, i've seen a few of the rookies come back with bite marks on them.'''
                                if "06" in list(AData["Relations"].keys()):
                                    P2+= f''' So she is {NPCdata["06"]["Name"]} property? Interesting i wouldn't have guessed that, i wonder what kind of business a girl like her has with that kind of slave, if anything i'd expect someone who can help with paperwork, i've heard nobles have to deal with a ton of that, but i doubt {NPCdata["07"]["Name"]} is really cappable of that."'''
                                else:
                                    P2 += f'''"'''
                                list.append(P2)
                            if "08" in list(AData["Relations"].keys()):
                                list.append(f'''"Are you asking about the trader {NPCdata["08"]["Name"]}? I guess i've met him a few times, he gives good prices for us so he is our go to with whatever we need, and sometimes i've had to do the talking. I'm not sure, i don't trust those traders in general, specially those as succesfull as him, but leaving aside how untrustful i am, well he has done good things for the town so i can't really say anything negative about him, maybe if you get on his good side you could get in his kind of trade too."''')
                            if "09" in list(AData["Relations"].keys()):
                                list.append(f'''"Hmm i think you are refering to {NPCdata["09"]["Name"]} i've seen him a few times while patrolling the residential area, haven't really talked too mcuh to him, the most was helping find his home once, but besides that there is not much i can tell you abotu him, he looks like you average boy, playful and sometimes getting in trouble but nothing too serious, maybe you can play with him if you are bored." ''')
                            P1 = random.choice(list)
                else:
                    RN = random.randint(0,2)
                    P1 = f'''"It's a bit boring to just talk, do you have something more itneresting to do?" '''
            else:
                if Success == 1:
                    P1 = f'''{Target} is having a cordial conversation with {Actor}.'''
                else:
                    P1 = f'''{Target} looks rather bored while {Actor} talks with {APObj}.'''
            PossibleText.append(P1)
        elif Action == "ServeThem":
            if Actor == PCID:
                if Success == 1:
                    RN = random.randint(0,2)
                    if RN == 0:
                        P1 = f'''"You want to do something for me?... I'm feeling kind of thirsty so i guess something nice to drink could do.'''
                        RN2 = random.randing(0,2)
                        if RN2 == 0:
                            P1 += f''' Some Tea? I guess that works too, never been too much a fan of it, but i don't dislike it either."'''
                        elif RN2 == 1:
                            P1 += f''' Coffee, that's a lot better, i've been trying to not abuse it as much recently, but since you are offering it so nicely i think ic an make an exception."'''
                        elif RN2 == 2:
                            P1 += f''' Water is nice too, not my first choice whiel trying to relax but it's good to stay healthy."'''
                    elif RN == 1:
                        P1 = f'''"Hmm... I'm not in need for anything you can do, but a moment of rest is always good so let's go sit over there for a bit."'''
                else:
                    P1 = f'''"Not in the mood for anything right now."'''
            else:
                if Success == 1:
                    P1 = f'''{TName} is enjoying a break while being served by {AName}.'''
                else:
                    P1 = f'''{TName} is gettign tired of resting and dismisses {AName}'s attempts at serving her. '''
        elif Action == "Skinship":
            if Actor == PCID:
                if Success == 1:
                    RN = random.randint(0,2)
                    if RN == 0:
                        P1 = f'''"Are you curious about my body? This uniform might not show that off but i'm pretty strong, liek this feel how firm is my belly." '''
                    elif RN == 1:
                        P1 = f'''"I'm glad you are interesed in my body, not many can guess how nice it's with these fancy clothes on me, they aren't my taste but i've been told they make the publc feel safer than with my other clothes." '''
                else:
                    P1 = f''' '''
            else:
                if Success == 1:
                    P1 = f''' '''
                else:
                    P1 = f''' '''
        elif Action == "GetLapPillow":
            if Actor == PCID:
                if Success == 1:
                    RN = random.randint(0,2)
                    if RN == 0:
                        P1 = f''' '''
                    elif RN == 1:
                        P1 = f''' '''
                else:
                    P1 = f''' '''
            else:
                if Success == 1:
                    P1 = f''' '''
                else:
                    P1 = f''' '''




        elif Action == "Skinship":
            if Actor == PCID:
                if Success == 1:
                    RN = random.randint(0,2)
                    if RN == 0:
                        P1 = f''' '''
                    elif RN == 1:
                        P1 = f''' '''
                else:
                    P1 = f''' '''
            else:
                if Success == 1:
                    P1 = f''' '''
                else:
                    P1 = f''' '''
