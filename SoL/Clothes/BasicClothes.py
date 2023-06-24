import Globals

def Initialize(self, Reference):
    try:
        Globals.SolClothes
    except:
        Globals.SolClothes = {}

    List = ["Dress", "Glasses", "Hat", "Panties", "Shoes", "Socks", "Bra"]
    for ID in List:
        Globals.SolClothes[ID] = {"ID":ID, "Reference":Reference, "Tags":[]}

    # Data = {"ID":"Skirt0", "Reference":Reference}
    # AddedData = {"ID":"Skirt0", "Name":"Skirt", "Modifications":{"Color":"Blue", "State":"Broken" }, "OtherData":{} }

def AddClothes(NPCData, ID):
    Name = GetClothesName(ID)
    Data = {"ID":ID, "Name":Name, "Text":"", "Status":"Equiped", "Modifications":{}, "OtherData":{}}
    Text = GetClothesText(Data)
    Data["Text"] = Text
    NPCData["Clothes"][ID] = Data

def GetClothesName(ID):
    if ID == "Skirt0":
        return "Skirt"
    return ID

def GetClothesText(Data):
    ID = Data["ID"]
    if ID == 'Skirt':
        return "A simple skirt extending down to below the knee."
    return ""

def GetClothesPosition(ClothID):
    Positions = []
    if ClothID == "Dress":
        Positions.append("Upper")
        Positions.append("Lower")
    elif ClothID == "Glasses":
        Positions.append("Head")
    elif ClothID == "Hat":
        Positions.append("Head")
    elif ClothID == "Panties":
        Positions.append("Lower")
    elif ClothID == "Shoes":
        Positions.append("Legs")
    elif ClothID == "Socks":
        Positions.append("Legs")
    elif ClothID == "Bra":
        Positions.append("Upper")

    return Positions

def GetClothesModifications(ID):
    Widget = None
    return Widget

def GetClothesWidget(ID, Data):
    if Data == None:
        ""
