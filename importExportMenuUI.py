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

class GenericNPCObject:
    def __init__(self, ID, Name, Status):
        self.ID = ID
        self.Name = Name
        self.Status = Status
        with open(f'''NPCdata/{self.Name}{ID}/{Name}{ID}Data.json''', 'rb') as f:
            self.Data = json.load(f)

    def GetWidget(self):
        NPCWidget = QWidget()
        NPCWidget.setMinimumWidth(365)
        NPCWidget.setMaximumWidth(365)
        NPCWidget.setMinimumHeight(130)
        NPCWidget.setMaximumHeight(130)
        NPCWidget.setStyleSheet('''
        .QWidget{
        border: 1px solid black;
        background : rgb(23, 23, 23)
        }
        QLabel{
        border: 1px solid black;
        background : rgb(35, 35, 35)
        }
        ''')

        LabelStatus = QLabel(NPCWidget)
        LabelStatus.setGeometry(0,0,20,130)


        try:
            ListPortraits, ListFullBody = Globals.References["SoLFunctions"].GetImages(self.Data)
            ImageType = "Portrait"

            if ImageType == "Portrait" or ListFullBody == []:
                ImageName = random.choice(ListPortraits)
            if ImageType == "FullBody" or ListPortraits == []:
                ImageName = random.choice(ListFullBody)

            LabelImage = QLabel(NPCWidget)
            LabelImage.setGeometry(20,0,130,130)
            LabelImage.setPixmap(QPixmap(f'''NPCdata/{self.Name}{self.ID}/{ImageName}'''))
            LabelImage.setScaledContents(True)
        except Exception as e:
            LabelImage = QLabel(NPCWidget)
            LabelImage.setGeometry(20,5,130,130)
            LabelImage.setStyleSheet('''
            QLabel{
            background : rgb(23, 23, 23)
            }
            ''')

        LabelName = QLabel(NPCWidget)
        LabelName.setGeometry(155,0,205,40)
        LabelName.setText(f'''{self.Data["Name"]} {self.ID}''')
        LabelName.setFont(QFont('Segoe UI', 14))
        LabelName.setAlignment(Qt.AlignVCenter | Qt.AlignHCenter)

        def DetailsFunc(self):
            ""
        ButtonDetails = QPushButton("Details", NPCWidget, clicked = lambda: DetailsFunc(self))
        ButtonDetails.setGeometry(155,45,100,40)
        ButtonDetails.setFont(QFont('Segoe UI', 12))

        def ImportFunc(self):
            with open(f'''NPCdata/{self.Name}{self.ID}/{self.Name}{self.ID}Data.json''', 'rb') as f:
                NPCData = json.load(f)
            try:
                Globals.References["SoLFunctions"].ImportNPC(NPCData)
                Globals.Layouts["ImportUI"].LabelStatus.setText(f'''Succesfully Imported {self.Name} {self.ID} ''')
            except Exception as e:
                Log(2, "ERROR IMPORTING NPC", e, self.ID, self.Name)
                Globals.Layouts["ImportUI"].LabelStatus.setText(f'''Error Importing {self.Name} {self.ID} ''')

            Globals.Layouts["ImportUI"].Refresh()
        ButtonImport = QPushButton("Import", NPCWidget, clicked = lambda: ImportFunc(self))
        ButtonImport.setGeometry(260,45,100,40)
        ButtonImport.setFont(QFont('Segoe UI', 12))

        def RemoveFunc(self):
            try:
                Globals.References["SoLFunctions"].RemoveNPC(self.ID)
                Globals.Layouts["ImportUI"].LabelStatus.setText(f'''Succesfully Removed {self.Name} {self.ID} ''')
            except Exception as e:
                Globals.Layouts["ImportUI"].LabelStatus.setText(f'''Failed to Remove {self.Name} {self.ID} ''')
                Log(4, "ERROR REMOVING NPC", e, self.ID, self.Name)

            Globals.Layouts["ImportUI"].Refresh()
        ButtonRemove = QPushButton("Remove", NPCWidget, clicked = lambda: RemoveFunc(self))
        ButtonRemove.setGeometry(155,90,100,40)
        ButtonRemove.setFont(QFont('Segoe UI', 12))

        def ExportFunc(self):
            ""
        ButtonExport = QPushButton("Export", NPCWidget, clicked = lambda: ExportFunc(self))
        ButtonExport.setGeometry(260,90,100,40)
        ButtonExport.setFont(QFont('Segoe UI', 12))

        if self.Status == "Active":
            LabelStatus.setStyleSheet('''
            QLabel{
            border: 1px solid black;
            background:rgb(0,255,0);
            }
            ''')
            ButtonImport.setCheckable(True)
            ButtonImport.setChecked(True)
            ButtonImport.setEnabled(False)
        elif self.Status == "Inactive":
            LabelStatus.setStyleSheet('''
            QLabel{
            border: 1px solid black;
            background:rgb(255,0,0);
            }
            ''')
            ButtonExport.setCheckable(True)
            ButtonExport.setChecked(True)
            ButtonExport.setEnabled(False)
        elif self.Status == "Temporal":
            LabelStatus.setStyleSheet('''
            QLabel{
            border: 1px solid black;
            background:rgb(255,255,0);
            }
            ''')
            ButtonImport.setCheckable(True)
            ButtonImport.setChecked(True)
            ButtonImport.setEnabled(False)

        return NPCWidget





class UiLayoutImport2Menu(object):
    def __init__(self):
        Globals.Layouts["ImportUI"] = self
        Globals.LayoutsData["ImportUI"] = {"Source":"importMenuUI", "Initialized":0}

    def UI(self):
        MainWindow = Globals.Layouts["MainF"]

        self.GUI = QWidget(MainWindow)
        # mainwindow.setWindowIcon(QtGui.QIcon('PhotoIcon.png'))
        self.GUI.setStyleSheet('''
        QWidget{
    	background-color:rgb(35, 35, 35);
        }
        QPushButton{
        	color:rgb(255, 255, 255)
        }
        QPushButton:hover{
        	color:rgb(255, 255, 0)
        }
        QLabel{
         border: 1px solid black;
         background : rgb(23, 23, 23);
         color:rgb(255, 255, 255)
        }
        QLineEdit{
        color:rgb(255, 255, 255)
        }
		QWidget{
    	background-color:rgb(35, 35, 35);
        }
        QPushButton{
        	color:rgb(255, 255, 255)
        }
        QPushButton:hover{
        	color:rgb(255, 255, 0)
        }
        QLabel{
         border: 1px solid black;
         background : rgb(35, 35, 35);
         color:rgb(255, 255, 255)
        }
        QLineEdit{
		border: 1px solid black;
        color:rgb(255, 255, 255)
        }
         ''')

        self.labelBack = QLabel(self.GUI)
        self.labelBack.setGeometry(230,10,820,780)
        self.labelBack.setStyleSheet('''
                QLabel{
         border: 1px solid black;
         background : rgb(23, 23, 23);
         color:rgb(255, 255, 255);
        }
        ''')

        self.labelText = QLabel(self.GUI)
        self.labelText.setGeometry(440,670,400,41)
        self.labelText.setFont(QFont('Segoe UI', 18))
        self.labelText.setAlignment(Qt.AlignVCenter)
        self.labelText.setAlignment(Qt.AlignHCenter)
        self.labelText.setStyleSheet('''
                QLabel{
         border: 1px solid black;
         background : rgb(23, 23, 23);
         color:rgb(255, 255, 255)
        }
        }
        ''')

        self.labelPage = QLabel("Page: 1", self.GUI)
        self.labelPage.setFont(QFont('Segoe UI', 10))
        self.labelPage.setGeometry(900,645,100,20)
        self.labelPage.setAlignment(Qt.AlignVCenter)
        self.labelPage.setAlignment(Qt.AlignHCenter)
        self.labelPage.setStyleSheet('''
                QLabel{
         border: 1px solid black;
         background : rgb(23, 23, 23);
         color:rgb(255, 255, 255)
        }
        }
        ''')


        self.buttonBack = QPushButton("Back", self.GUI, clicked = lambda: MainWindow.gotoPreviousLayout())
        self.buttonBack.setFont(QFont('Segoe UI', 14))
        self.buttonBack.setGeometry(260,670,160,35)

        self.buttonMaker = QPushButton("NPC Maker", self.GUI, clicked = lambda: MainWindow.gotoLayout("MakerUI"))
        self.buttonMaker.setFont(QFont('Segoe UI', 14))
        self.buttonMaker.setGeometry(260,715,160,35)


        self.buttonLeft = QPushButton("<---", self.GUI)
        self.buttonLeft.setFont(QFont('Segoe UI', 14))
        self.buttonLeft.setGeometry(863,670,80,35)
        self.buttonLeft.clicked.connect(self.previousPage)

        self.buttonRight = QPushButton("--->", self.GUI)
        self.buttonRight.setFont(QFont('Segoe UI', 14))
        self.buttonRight.setGeometry(952,670,80,35)
        self.buttonRight.clicked.connect(self.nextPage)


        self.labelStatus1 = QLabel(self.GUI)
        self.labelStatus1.setGeometry(240,20,10,40)

        self.labelCharacter1 = QLabel(self.GUI)
        self.labelCharacter1.setGeometry(250,20,600,40)
        self.labelCharacter1.setFont(QFont('Segoe UI', 14))
        self.labelCharacter1.setAlignment(Qt.AlignVCenter)

        self.buttonDetails1 = QPushButton("Details", self.GUI)
        self.buttonDetails1.setGeometry(860,23,80,35)
        self.buttonDetails1.setFont(QFont('Segoe UI', 14))
        self.buttonDetails1.clicked.connect(self.details1)

        self.buttonImport1 = QPushButton("Import", self.GUI)
        self.buttonImport1.setGeometry(949,23,80,35)
        self.buttonImport1.setFont(QFont('Segoe UI', 14))
        self.buttonImport1.clicked.connect(self.import1)


        self.labelStatus2 = QLabel(self.GUI)
        self.labelStatus2.setGeometry(240,65,10,40)

        self.labelCharacter2 = QLabel(self.GUI)
        self.labelCharacter2.setGeometry(250,65,600,40)
        self.labelCharacter2.setFont(QFont('Segoe UI', 14))
        self.labelCharacter2.setAlignment(Qt.AlignVCenter)

        self.buttonDetails2 = QPushButton("Details", self.GUI)
        self.buttonDetails2.setGeometry(860,68,80,35)
        self.buttonDetails2.setFont(QFont('Segoe UI', 14))
        self.buttonDetails2.clicked.connect(self.details2)

        self.buttonImport2 = QPushButton("Import", self.GUI)
        self.buttonImport2.setGeometry(949,68,80,35)
        self.buttonImport2.setFont(QFont('Segoe UI', 14))
        self.buttonImport2.clicked.connect(self.import2)


        self.labelStatus3 = QLabel(self.GUI)
        self.labelStatus3.setGeometry(240,110,10,40)

        self.labelCharacter3 = QLabel(self.GUI)
        self.labelCharacter3.setGeometry(250,110,600,40)
        self.labelCharacter3.setFont(QFont('Segoe UI', 14))
        self.labelCharacter3.setAlignment(Qt.AlignVCenter)

        self.buttonDetails3 = QPushButton("Details", self.GUI)
        self.buttonDetails3.setGeometry(860,113,80,35)
        self.buttonDetails3.setFont(QFont('Segoe UI', 14))
        self.buttonDetails3.clicked.connect(self.details3)

        self.buttonImport3 = QPushButton("Import", self.GUI)
        self.buttonImport3.setGeometry(949,113,80,35)
        self.buttonImport3.setFont(QFont('Segoe UI', 14))
        self.buttonImport3.clicked.connect(self.import3)


        self.labelStatus4 = QLabel(self.GUI)
        self.labelStatus4.setGeometry(240,155,10,40)

        self.labelCharacter4 = QLabel(self.GUI)
        self.labelCharacter4.setGeometry(250,155,600,40)
        self.labelCharacter4.setFont(QFont('Segoe UI', 14))
        self.labelCharacter4.setAlignment(Qt.AlignVCenter)

        self.buttonDetails4 = QPushButton("Details", self.GUI)
        self.buttonDetails4.setGeometry(860,158,80,35)
        self.buttonDetails4.setFont(QFont('Segoe UI', 14))
        self.buttonDetails4.clicked.connect(self.details4)

        self.buttonImport4 = QPushButton("Import", self.GUI)
        self.buttonImport4.setGeometry(949,158,80,35)
        self.buttonImport4.setFont(QFont('Segoe UI', 14))
        self.buttonImport4.clicked.connect(self.import4)


        self.labelStatus5 = QLabel(self.GUI)
        self.labelStatus5.setGeometry(240,200,10,40)

        self.labelCharacter5 = QLabel(self.GUI)
        self.labelCharacter5.setGeometry(250,200,600,40)
        self.labelCharacter5.setFont(QFont('Segoe UI', 14))
        self.labelCharacter5.setAlignment(Qt.AlignVCenter)

        self.buttonDetails5 = QPushButton("Details", self.GUI)
        self.buttonDetails5.setGeometry(860,203,80,35)
        self.buttonDetails5.setFont(QFont('Segoe UI', 14))
        self.buttonDetails5.clicked.connect(self.details5)

        self.buttonImport5 = QPushButton("Import", self.GUI)
        self.buttonImport5.setGeometry(949,203,80,35)
        self.buttonImport5.setFont(QFont('Segoe UI', 14))
        self.buttonImport5.clicked.connect(self.import5)


        self.labelStatus6 = QLabel(self.GUI)
        self.labelStatus6.setGeometry(240,245,10,40)

        self.labelCharacter6 = QLabel(self.GUI)
        self.labelCharacter6.setGeometry(250,245,600,40)
        self.labelCharacter6.setFont(QFont('Segoe UI', 14))
        self.labelCharacter6.setAlignment(Qt.AlignVCenter)

        self.buttonDetails6 = QPushButton("Details", self.GUI)
        self.buttonDetails6.setGeometry(860,248,80,35)
        self.buttonDetails6.setFont(QFont('Segoe UI', 14))
        self.buttonDetails6.clicked.connect(self.details6)

        self.buttonImport6 = QPushButton("Import", self.GUI)
        self.buttonImport6.setGeometry(949,248,80,35)
        self.buttonImport6.setFont(QFont('Segoe UI', 14))
        self.buttonImport6.clicked.connect(self.import6)


        self.labelStatus7 = QLabel(self.GUI)
        self.labelStatus7.setGeometry(240,290,10,40)

        self.labelCharacter7 = QLabel(self.GUI)
        self.labelCharacter7.setGeometry(250,290,600,40)
        self.labelCharacter7.setFont(QFont('Segoe UI', 14))
        self.labelCharacter7.setAlignment(Qt.AlignVCenter)

        self.buttonDetails7 = QPushButton("Details", self.GUI)
        self.buttonDetails7.setGeometry(860,293,80,35)
        self.buttonDetails7.setFont(QFont('Segoe UI', 14))
        self.buttonDetails7.clicked.connect(self.details7)

        self.buttonImport7 = QPushButton("Import", self.GUI)
        self.buttonImport7.setGeometry(949,293,80,35)
        self.buttonImport7.setFont(QFont('Segoe UI', 14))
        self.buttonImport7.clicked.connect(self.import7)


        self.labelStatus8 = QLabel(self.GUI)
        self.labelStatus8.setGeometry(240,335,10,40)

        self.labelCharacter8 = QLabel(self.GUI)
        self.labelCharacter8.setGeometry(250,335,600,40)
        self.labelCharacter8.setFont(QFont('Segoe UI', 14))
        self.labelCharacter8.setAlignment(Qt.AlignVCenter)

        self.buttonDetails8 = QPushButton("Details", self.GUI)
        self.buttonDetails8.setGeometry(860,338,80,35)
        self.buttonDetails8.setFont(QFont('Segoe UI', 14))
        self.buttonDetails8.clicked.connect(self.details8)

        self.buttonImport8 = QPushButton("Import", self.GUI)
        self.buttonImport8.setGeometry(949,338,80,35)
        self.buttonImport8.setFont(QFont('Segoe UI', 14))
        self.buttonImport8.clicked.connect(self.import8)


        self.labelStatus9 = QLabel(self.GUI)
        self.labelStatus9.setGeometry(240,380,10,40)

        self.labelCharacter9 = QLabel(self.GUI)
        self.labelCharacter9.setGeometry(250,380,600,40)
        self.labelCharacter9.setFont(QFont('Segoe UI', 14))
        self.labelCharacter9.setAlignment(Qt.AlignVCenter)

        self.buttonDetails9 = QPushButton("Details", self.GUI)
        self.buttonDetails9.setGeometry(860,383,80,35)
        self.buttonDetails9.setFont(QFont('Segoe UI', 14))
        self.buttonDetails9.clicked.connect(self.details9)

        self.buttonImport9 = QPushButton("Import", self.GUI)
        self.buttonImport9.setGeometry(949,383,80,35)
        self.buttonImport9.setFont(QFont('Segoe UI', 14))
        self.buttonImport9.clicked.connect(self.import9)


        self.labelStatus10 = QLabel(self.GUI)
        self.labelStatus10.setGeometry(240,425,10,40)

        self.labelCharacter10 = QLabel(self.GUI)
        self.labelCharacter10.setGeometry(250,425,600,40)
        self.labelCharacter10.setFont(QFont('Segoe UI', 14))
        self.labelCharacter10.setAlignment(Qt.AlignVCenter)

        self.buttonDetails10 = QPushButton("Details", self.GUI)
        self.buttonDetails10.setGeometry(860,428,80,35)
        self.buttonDetails10.setFont(QFont('Segoe UI', 14))
        self.buttonDetails10.clicked.connect(self.details10)

        self.buttonImport10 = QPushButton("Import", self.GUI)
        self.buttonImport10.setGeometry(949,428,80,35)
        self.buttonImport10.setFont(QFont('Segoe UI', 14))
        self.buttonImport10.clicked.connect(self.import10)


        self.labelStatus11 = QLabel(self.GUI)
        self.labelStatus11.setGeometry(240,470,10,40)

        self.labelCharacter11 = QLabel(self.GUI)
        self.labelCharacter11.setGeometry(250,470,600,40)
        self.labelCharacter11.setFont(QFont('Segoe UI', 14))
        self.labelCharacter11.setAlignment(Qt.AlignVCenter)

        self.buttonDetails11 = QPushButton("Details", self.GUI)
        self.buttonDetails11.setGeometry(860,473,80,35)
        self.buttonDetails11.setFont(QFont('Segoe UI', 14))
        self.buttonDetails11.clicked.connect(self.details11)

        self.buttonImport11 = QPushButton("Import", self.GUI)
        self.buttonImport11.setGeometry(949,473,80,35)
        self.buttonImport11.setFont(QFont('Segoe UI', 14))
        self.buttonImport11.clicked.connect(self.import11)


        self.labelStatus12 = QLabel(self.GUI)
        self.labelStatus12.setGeometry(240,515,10,40)

        self.labelCharacter12 = QLabel(self.GUI)
        self.labelCharacter12.setGeometry(250,515,600,40)
        self.labelCharacter12.setFont(QFont('Segoe UI', 14))
        self.labelCharacter12.setAlignment(Qt.AlignVCenter)

        self.buttonDetails12 = QPushButton("Details", self.GUI)
        self.buttonDetails12.setGeometry(860,518,80,35)
        self.buttonDetails12.setFont(QFont('Segoe UI', 14))
        self.buttonDetails12.clicked.connect(self.details12)

        self.buttonImport12 = QPushButton("Import", self.GUI)
        self.buttonImport12.setGeometry(949,518,80,35)
        self.buttonImport12.setFont(QFont('Segoe UI', 14))
        self.buttonImport12.clicked.connect(self.import12)


        self.labelStatus13 = QLabel(self.GUI)
        self.labelStatus13.setGeometry(240,560,10,40)

        self.labelCharacter13 = QLabel(self.GUI)
        self.labelCharacter13.setGeometry(250,560,600,40)
        self.labelCharacter13.setFont(QFont('Segoe UI', 14))
        self.labelCharacter13.setAlignment(Qt.AlignVCenter)

        self.buttonDetails13 = QPushButton("Details", self.GUI)
        self.buttonDetails13.setGeometry(860,563,80,35)
        self.buttonDetails13.setFont(QFont('Segoe UI', 14))
        self.buttonDetails13.clicked.connect(self.details13)

        self.buttonImport13 = QPushButton("Import", self.GUI)
        self.buttonImport13.setGeometry(949,563,80,35)
        self.buttonImport13.setFont(QFont('Segoe UI', 14))
        self.buttonImport13.clicked.connect(self.import13)


        self.labelStatus14 = QLabel(self.GUI)
        self.labelStatus14.setGeometry(240,605,10,40)

        self.labelCharacter14 = QLabel(self.GUI)
        self.labelCharacter14.setGeometry(250,605,600,40)
        self.labelCharacter14.setFont(QFont('Segoe UI', 14))
        self.labelCharacter14.setAlignment(Qt.AlignVCenter)

        self.buttonDetails14 = QPushButton("Details", self.GUI)
        self.buttonDetails14.setGeometry(860,608,80,35)
        self.buttonDetails14.setFont(QFont('Segoe UI', 14))
        self.buttonDetails14.clicked.connect(self.details14)

        self.buttonImport14 = QPushButton("Import", self.GUI)
        self.buttonImport14.setGeometry(949,608,80,35)
        self.buttonImport14.setFont(QFont('Segoe UI', 14))
        self.buttonImport14.clicked.connect(self.import14)


        self.importCheck()




    def importCheck(self):
        list = os.listdir("NPCdata")

        listCharacters = []
        for i in list:
            try:
                pathData = "NPCdata/" + str(i) + "/" + str(i) + "Data.json"
                with open(pathData, 'rb') as f:
                    saveData = json.load(f)
                Name = saveData["Name"]
                ID = saveData["ID"]
                if ID != "0":
                    x = {}
                    x["Name"] = Name
                    x["ID"] = ID
                    listCharacters.append(x)
                else:
                    toRemove = str(Name) + str(ID)
                    ""
            except:
                print("Invalid " + str(i))
                ""
        try:
            list.pop(toRemove)
        except:
            ""
        page = self.labelPage.text()
        length = len(page)
        page = page[6:length]

        amount = len(listCharacters)

        counter = int(page) * 14 - 14
        amount -=1

        def statusCheck(characterDict):
            with open("NPCdata.json", 'rb') as f:
                NPCdata = json.load(f)
            try:
                ID = characterDict["ID"]
                NPCdata[ID]
                status = "On"
            except:
                status = "Off"

            if status == "On":
                color = '''QLabel{
        background-color: rgb(23, 255, 0)
        } '''

            elif status == "Off":
                color = '''QLabel{
        background-color: rgb(255, 23, 23)
        } '''

            return color
            ""

        if counter <= amount:
            characterDict = listCharacters[counter]
            status = statusCheck(characterDict)
            self.labelStatus1.show()
            self.labelStatus1.setStyleSheet(status)
            x = str( str(characterDict["ID"] + " " + characterDict["Name"]))
            self.labelCharacter1.setText(x)
            self.labelCharacter1.show()
            self.buttonDetails1.show()
            self.buttonImport1.show()
            counter += 1
        else:
            self.labelStatus1.hide()
            self.labelCharacter1.hide()
            self.buttonDetails1.hide()
            self.buttonImport1.hide()
        if counter <= amount:
            characterDict = listCharacters[counter]
            status = statusCheck(characterDict)
            self.labelStatus2.show()
            self.labelStatus2.setStyleSheet(status)
            x = str( str(characterDict["ID"] + " " + characterDict["Name"]))
            self.labelCharacter2.setText(x)
            self.labelCharacter2.show()
            self.buttonDetails2.show()
            self.buttonImport2.show()
            counter += 1
        else:
            self.labelStatus2.hide()
            self.labelCharacter2.hide()
            self.buttonDetails2.hide()
            self.buttonImport2.hide()
        if counter <= amount:
            characterDict = listCharacters[counter]
            status = statusCheck(characterDict)
            self.labelStatus3.show()
            self.labelStatus3.setStyleSheet(status)
            x = str( str(characterDict["ID"] + " " + characterDict["Name"]))
            self.labelCharacter3.setText(x)
            self.labelCharacter3.show()
            self.buttonDetails3.show()
            self.buttonImport3.show()
            counter += 1
        else:
            self.labelStatus3.hide()
            self.labelCharacter3.hide()
            self.buttonDetails3.hide()
            self.buttonImport3.hide()
        if counter <= amount:
            characterDict = listCharacters[counter]
            status = statusCheck(characterDict)
            self.labelStatus4.show()
            self.labelStatus4.setStyleSheet(status)
            x = str( str(characterDict["ID"] + " " + characterDict["Name"]))
            self.labelCharacter4.setText(x)
            self.labelCharacter4.show()
            self.buttonDetails4.show()
            self.buttonImport4.show()
            counter += 1
        else:
            self.labelStatus4.hide()
            self.labelCharacter4.hide()
            self.buttonDetails4.hide()
            self.buttonImport4.hide()
        if counter <= amount:
            characterDict = listCharacters[counter]
            status = statusCheck(characterDict)
            self.labelStatus5.show()
            self.labelStatus5.setStyleSheet(status)
            x = str( str(characterDict["ID"] + " " + characterDict["Name"]))
            self.labelCharacter5.setText(x)
            self.labelCharacter5.show()
            self.buttonDetails5.show()
            self.buttonImport5.show()
            counter += 1
        else:
            self.labelStatus5.hide()
            self.labelCharacter5.hide()
            self.buttonDetails5.hide()
            self.buttonImport5.hide()
        if counter <= amount:
            characterDict = listCharacters[counter]
            status = statusCheck(characterDict)
            self.labelStatus6.show()
            self.labelStatus6.setStyleSheet(status)
            x = str( str(characterDict["ID"] + " " + characterDict["Name"]))
            self.labelCharacter6.setText(x)
            self.labelCharacter6.show()
            self.buttonDetails6.show()
            self.buttonImport6.show()
            counter += 1
        else:
            self.labelStatus6.hide()
            self.labelCharacter6.hide()
            self.buttonDetails6.hide()
            self.buttonImport6.hide()
        if counter <= amount:
            characterDict = listCharacters[counter]
            status = statusCheck(characterDict)
            self.labelStatus7.show()
            self.labelStatus7.setStyleSheet(status)
            x = str( str(characterDict["ID"] + " " + characterDict["Name"]))
            self.labelCharacter7.setText(x)
            self.labelCharacter7.show()
            self.buttonDetails7.show()
            self.buttonImport7.show()
            counter += 1
        else:
            self.labelStatus7.hide()
            self.labelCharacter7.hide()
            self.buttonDetails7.hide()
            self.buttonImport7.hide()
        if counter <= amount:
            characterDict = listCharacters[counter]
            status = statusCheck(characterDict)
            self.labelStatus8.show()
            self.labelStatus8.setStyleSheet(status)
            x = str( str(characterDict["ID"] + " " + characterDict["Name"]))
            self.labelCharacter8.setText(x)
            self.labelCharacter8.show()
            self.buttonDetails8.show()
            self.buttonImport8.show()
            counter += 1
        else:
            self.labelStatus8.hide()
            self.labelCharacter8.hide()
            self.buttonDetails8.hide()
            self.buttonImport8.hide()
        if counter <= amount:
            characterDict = listCharacters[counter]
            status = statusCheck(characterDict)
            self.labelStatus9.show()
            self.labelStatus9.setStyleSheet(status)
            x = str( str(characterDict["ID"] + " " + characterDict["Name"]))
            self.labelCharacter9.setText(x)
            self.labelCharacter9.show()
            self.buttonDetails9.show()
            self.buttonImport9.show()
            counter += 1
        else:
            self.labelStatus9.hide()
            self.labelCharacter9.hide()
            self.buttonDetails9.hide()
            self.buttonImport9.hide()
        if counter <= amount:
            characterDict = listCharacters[counter]
            status = statusCheck(characterDict)
            self.labelStatus10.show()
            self.labelStatus10.setStyleSheet(status)
            x = str( str(characterDict["ID"] + " " + characterDict["Name"]))
            self.labelCharacter10.setText(x)
            self.labelCharacter10.show()
            self.buttonDetails10.show()
            self.buttonImport10.show()
            counter += 1
        else:
            self.labelStatus10.hide()
            self.labelCharacter10.hide()
            self.buttonDetails10.hide()
            self.buttonImport10.hide()
        if counter <= amount:
            characterDict = listCharacters[counter]
            status = statusCheck(characterDict)
            self.labelStatus11.show()
            self.labelStatus11.setStyleSheet(status)
            x = str( str(characterDict["ID"] + " " + characterDict["Name"]))
            self.labelCharacter11.setText(x)
            self.labelCharacter11.show()
            self.buttonDetails11.show()
            self.buttonImport11.show()
            counter += 1
        else:
            self.labelStatus11.hide()
            self.labelCharacter11.hide()
            self.buttonDetails11.hide()
            self.buttonImport11.hide()
        if counter <= amount:
            characterDict = listCharacters[counter]
            status = statusCheck(characterDict)
            self.labelStatus12.show()
            self.labelStatus12.setStyleSheet(status)
            x = str( str(characterDict["ID"] + " " + characterDict["Name"]))
            self.labelCharacter12.setText(x)
            self.labelCharacter12.show()
            self.buttonDetails12.show()
            self.buttonImport12.show()
            counter += 1
        else:
            self.labelStatus12.hide()
            self.labelCharacter12.hide()
            self.buttonDetails12.hide()
            self.buttonImport12.hide()
        if counter <= amount:
            characterDict = listCharacters[counter]
            status = statusCheck(characterDict)
            self.labelStatus13.show()
            self.labelStatus13.setStyleSheet(status)
            x = str( str(characterDict["ID"] + " " + characterDict["Name"]))
            self.labelCharacter13.setText(x)
            self.labelCharacter13.show()
            self.buttonDetails13.show()
            self.buttonImport13.show()
            counter += 1
        else:
            self.labelStatus13.hide()
            self.labelCharacter13.hide()
            self.buttonDetails13.hide()
            self.buttonImport13.hide()
        if counter <= amount:
            characterDict = listCharacters[counter]
            status = statusCheck(characterDict)
            self.labelStatus14.show()
            self.labelStatus14.setStyleSheet(status)
            x = str( str(characterDict["ID"] + " " + characterDict["Name"]))
            self.labelCharacter14.setText(x)
            self.labelCharacter14.show()
            self.buttonDetails14.show()
            self.buttonImport14.show()
            counter += 1
        else:
            self.labelStatus14.hide()
            self.labelCharacter14.hide()
            self.buttonDetails14.hide()
            self.buttonImport14.hide()

        if counter <= amount:
            self.buttonRight.show()
        else:
            self.buttonRight.hide()
        if int(page) > 1:
            self.buttonLeft.show()
        else:
            self.buttonLeft.hide()

        #     self.labelSave1.show()
        #     self.labelSave1.setText(list(sortedDict)[amount-counter])
        #     self.buttonSave1.show()
        #     self.buttonLoad1.show()
        #     counter += 1
        # else:
        #     self.labelSave1.hide()
        #     self.buttonSave1.hide()
        #     self.buttonLoad1.hide()





    def nextPage(self):
        page = self.labelPage.text()
        length = len(page)
        page = page[6:length]
        page = int(page) + 1
        self.labelPage.setText("Page: "+str(page))

    def previousPage(self):
        page = self.labelPage.text()
        length = len(page)
        page = page[6:length]
        page = int(page) - 1
        self.labelPage.setText("Page: "+str(page))


    def importFun(self, labelNumber):
        list = os.listdir("NPCdata")
        listCharacters = []
        for i in list:
            try:
                pathData = "NPCdata/" + str(i) + "/" + str(i) + "Data.json"
                with open(pathData, 'rb') as f:
                    saveData = json.load(f)
                Name = saveData["Name"]
                ID = saveData["ID"]
                if ID != "0":
                    x = {}
                    x["Name"] = Name
                    x["ID"] = ID
                    listCharacters.append(x)
                else:
                    toRemove = str(Name) + str(ID)
                    ""
            except:
                ""

        try:
            list.pop(toRemove)
        except:
            ""
        page = self.labelPage.text()
        length = len(page)
        page = page[6:length]

        amount = len(listCharacters)



        labelNumber -= 1
        x = (int(page) * 14) - 14
        labelNumber += x
        x = listCharacters[labelNumber]
        path = "NPCdata/" + str(x["Name"]) + str(x["ID"]) + "/" + str(x["Name"]) + str(x["ID"]) + "Data.json"

        with open(path, 'rb') as f:
            NPCdata = json.load(f)
        with open("NPCdata.json", 'rb') as f:
            NPCdataWhole = json.load(f)
        ID = x["ID"]
        NPCdataWhole[ID] = NPCdata

        with open("NPCdata.json", 'w') as f:
            json.dump(NPCdataWhole, f)

        self.importCheck()
        self.labelText.setText("Succesful Import")


    def detailsCall(self, Name,ID):
        with open('tempData.json', 'rb') as f:
            x = json.load(f)
        x["DetailsData"] = {"Name":Name,"ID":ID,"Type":1,"From":"ImportMenu"}
        with open('tempData.json', 'w') as f:
            json.dump(x, f)

    def details1(self):
        Whole = self.labelCharacter1.text()
        Counter = 0
        for i in Whole:
            if i != " ":
                Counter += 1
            else:
                break
        ID = Whole[0:Counter]
        Counter += 1
        Length = len(Whole)
        Name = Whole[Counter:Length]
        self.detailsCall(Name, ID)
        ""

    def details2(self):
        Whole = self.labelCharacter2.text()
        Counter = 0
        for i in Whole:
            if i != " ":
                Counter += 1
            else:
                break
        ID = Whole[0:Counter]
        Counter += 1
        Length = len(Whole)
        Name = Whole[Counter:Length]
        self.detailsCall(Name, ID)
        ""

    def details3(self):
        Whole = self.labelCharacter3.text()
        Counter = 0
        for i in Whole:
            if i != " ":
                Counter += 1
            else:
                break
        ID = Whole[0:Counter]
        Counter += 1
        Length = len(Whole)
        Name = Whole[Counter:Length]
        self.detailsCall(Name, ID)
        ""

    def details4(self):
        Whole = self.labelCharacter4.text()
        Counter = 0
        for i in Whole:
            if i != " ":
                Counter += 1
            else:
                break
        ID = Whole[0:Counter]
        Counter += 1
        Length = len(Whole)
        Name = Whole[Counter:Length]
        self.detailsCall(Name, ID)
        ""

    def details5(self):
        Whole = self.labelCharacter5.text()
        Counter = 0
        for i in Whole:
            if i != " ":
                Counter += 1
            else:
                break
        ID = Whole[0:Counter]
        Counter += 1
        Length = len(Whole)
        Name = Whole[Counter:Length]
        self.detailsCall(Name, ID)
        ""

    def details6(self):
        Whole = self.labelCharacter6.text()
        Counter = 0
        for i in Whole:
            if i != " ":
                Counter += 1
            else:
                break
        ID = Whole[0:Counter]
        Counter += 1
        Length = len(Whole)
        Name = Whole[Counter:Length]
        self.detailsCall(Name, ID)
        ""

    def details7(self):
        Whole = self.labelCharacter7.text()
        Counter = 0
        for i in Whole:
            if i != " ":
                Counter += 1
            else:
                break
        ID = Whole[0:Counter]
        Counter += 1
        Length = len(Whole)
        Name = Whole[Counter:Length]
        self.detailsCall(Name, ID)
        ""

    def details8(self):
        Whole = self.labelCharacter8.text()
        Counter = 0
        for i in Whole:
            if i != " ":
                Counter += 1
            else:
                break
        ID = Whole[0:Counter]
        Counter += 1
        Length = len(Whole)
        Name = Whole[Counter:Length]
        self.detailsCall(Name, ID)
        ""

    def details9(self):
        Whole = self.labelCharacter9.text()
        Counter = 0
        for i in Whole:
            if i != " ":
                Counter += 1
            else:
                break
        ID = Whole[0:Counter]
        Counter += 1
        Length = len(Whole)
        Name = Whole[Counter:Length]
        self.detailsCall(Name, ID)
        ""

    def details10(self):
        Whole = self.labelCharacter10.text()
        Counter = 0
        for i in Whole:
            if i != " ":
                Counter += 1
            else:
                break
        ID = Whole[0:Counter]
        Counter += 1
        Length = len(Whole)
        Name = Whole[Counter:Length]
        self.detailsCall(Name, ID)
        ""

    def details11(self):
        Whole = self.labelCharacter11.text()
        Counter = 0
        for i in Whole:
            if i != " ":
                Counter += 1
            else:
                break
        ID = Whole[0:Counter]
        Counter += 1
        Length = len(Whole)
        Name = Whole[Counter:Length]
        self.detailsCall(Name, ID)
        ""

    def details12(self):
        Whole = self.labelCharacter12.text()
        Counter = 0
        for i in Whole:
            if i != " ":
                Counter += 1
            else:
                break
        ID = Whole[0:Counter]
        Counter += 1
        Length = len(Whole)
        Name = Whole[Counter:Length]
        self.detailsCall(Name, ID)
        ""

    def details13(self):
        Whole = self.labelCharacter13.text()
        Counter = 0
        for i in Whole:
            if i != " ":
                Counter += 1
            else:
                break
        ID = Whole[0:Counter]
        Counter += 1
        Length = len(Whole)
        Name = Whole[Counter:Length]
        self.detailsCall(Name, ID)
        ""

    def details14(self):
        Whole = self.labelCharacter14.text()
        Counter = 0
        for i in Whole:
            if i != " ":
                Counter += 1
            else:
                break
        ID = Whole[0:Counter]
        Counter += 1
        Length = len(Whole)
        Name = Whole[Counter:Length]
        self.detailsCall(Name, ID)
        ""




    def import1(self):
        self.importFun(1)
        ""

    def import2(self):
        self.importFun(2)
        ""

    def import3(self):
        self.importFun(3)
        ""

    def import4(self):
        self.importFun(4)
        ""

    def import5(self):
        self.importFun(5)
        ""

    def import6(self):
        self.importFun(6)
        ""

    def import7(self):
        self.importFun(7)
        ""

    def import8(self):
        self.importFun(8)
        ""

    def import9(self):
        self.importFun(9)
        ""

    def import10(self):
        self.importFun(10)
        ""

    def import11(self):
        self.importFun(11)
        ""

    def import12(self):
        self.importFun(13)
        ""

    def import13(self):
        self.importFun(13)
        ""

    def import14(self):
        self.importFun(14)
        ""

class UiLayoutImportMenu(object):
    def __init__(self):
        Globals.Layouts["ImportUI"] = self
        Globals.LayoutsData["ImportUI"] = {"Source":"importMenuUI", "Initialized":0}


    def UI(self):
        MainWindow = Globals.Layouts["MainF"]

        self.GUI = QWidget(MainWindow)


        self.labelBack = QLabel(self.GUI)
        self.labelBack.setGeometry(237,5,1125,950)
        self.labelBack.setProperty("Color","Dark")

        self.scrollNPC = QScrollArea(self.GUI)
        self.scrollNPC.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollNPC.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollNPC.setGeometry(237,5,1125,950)


        self.LabelControl = QLabel(self.GUI)
        self.LabelControl.setGeometry(5,964,1592,55)
        self.LabelControl.setStyleSheet('''
        QLabel{
        background-color:rgb(23,23,23);
        }
        ''')

        self.ButtonMenu = QPushButton("Back", self.GUI, clicked = lambda: MainWindow.gotoPreviousLayout())
        self.ButtonMenu.setGeometry(15,970,200,45)

        self.LabelStatus = QLabel(self.GUI)
        self.LabelStatus.setGeometry(595,970,400,45)
        self.LabelStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.LabelStatus.setStyleSheet('''
        QLabel{
        background-color:rgb(23,23,23);
        color:white;
        font-size: 16pt;
        font-family: Segoe UI;
        }
        ''')

        self.myformNPC = QGridLayout()
        self.myformNPC.WidgetsList = []
        self.mygroupboxNPC = QGroupBox()

        self.Refresh()

    def Refresh(self):
        for Widget in self.myformNPC.WidgetsList:
            self.myformNPC.removeWidget(Widget)

        NPCFiles = {}
        NPCCurrent = {}
        NPCStatus = {}

        DirList = os.listdir("NPCdata")
        for DirName in DirList:
            try:
                with open(f'''NPCdata/{DirName}/{DirName}Data.json''', 'rb') as f:
                    NPCdata = json.load(f)
                Name = NPCdata["Name"]
                ID = NPCdata["ID"]

                NPCFiles[ID] = NPCdata

            except Exception as e:
                ""
        NPCCurrent = list(Globals.SoLNPCData.keys())

        for NPCID in NPCFiles:
            if NPCID in NPCCurrent:
                NPCStatus[NPCID] = "Active"
            else:
                NPCStatus[NPCID] = "Inactive"

        for NPCID in NPCCurrent:
            if NPCID not in NPCCurrent:
                NPCStatus[NPCID] = "Temporal"





        Layer, Row = 0,0

        for NPCID in NPCStatus:
            if NPCID == Globals.SoLPCData["ID"]:
                continue
            try:
                Name = NPCFiles[NPCID]["Name"]
            except:
                Name = Globals.SoLNPCData[NPCID]["Name"]

            Object = GenericNPCObject(NPCID, Name, NPCStatus[NPCID])
            Widget = Object.GetWidget()
            self.myformNPC.addWidget(Widget, Layer, Row)
            self.myformNPC.WidgetsList.append(Widget)
            Row += 1
            if Row >= 3:
                Layer += 1
                Row = 0

        self.mygroupboxNPC.setLayout(self.myformNPC)
        self.scrollNPC.setWidget(self.mygroupboxNPC)
        # self.scrollNPC.setMinimumWidth(1125)
        # self.scrollNPC.setMaximumWidth(1125)
        # self.scrollNPC.setMinimumHeight(950)
        # self.scrollNPC.setMaximumHeight(950)
        # self.myformNPC.setContentsMargins(10, 0, 5, 5)

class UiLayoutExportMenu(object):
    def __init__(self):
        Globals.Layouts["ExportUI"] = self
        Globals.LayoutsData["ExportUI"] = {"Source":"exportMenuUI", "Initialized":0}


    def UI(self):
        MainWindow = Globals.Layouts["MainF"]

        self.GUI = QWidget(MainWindow)
        # mainwindow.setWindowIcon(QtGui.QIcon('PhotoIcon.png'))
        self.GUI.setStyleSheet('''
        QWidget{
    	background-color:rgb(35, 35, 35);
        }
        QPushButton{
        	color:rgb(255, 255, 255)
        }
        QPushButton:hover{
        	color:rgb(255, 255, 0)
        }
        QLabel{
         border: 1px solid black;
         background : rgb(23, 23, 23);
         color:rgb(255, 255, 255)
        }
        QLineEdit{
        color:rgb(255, 255, 255)
        }
		QWidget{
    	background-color:rgb(35, 35, 35);
        }
        QPushButton{
        	color:rgb(255, 255, 255)
        }
        QPushButton:hover{
        	color:rgb(255, 255, 0)
        }
        QLabel{
         border: 1px solid black;
         background : rgb(35, 35, 35);
         color:rgb(255, 255, 255)
        }
        QLineEdit{
		border: 1px solid black;
        color:rgb(255, 255, 255)
        }
         ''')

        self.labelBack = QLabel(self.GUI)
        self.labelBack.setGeometry(230,10,820,780)
        self.labelBack.setStyleSheet('''
                QLabel{
         border: 1px solid black;
         background : rgb(23, 23, 23);
         color:rgb(255, 255, 255);
        }
        ''')

        self.labelText = QLabel(self.GUI)
        self.labelText.setGeometry(440,670,400,41)
        self.labelText.setFont(QFont('Segoe UI', 18))
        self.labelText.setAlignment(Qt.AlignVCenter)
        self.labelText.setAlignment(Qt.AlignHCenter)
        self.labelText.setStyleSheet('''
                QLabel{
         border: 1px solid black;
         background : rgb(23, 23, 23);
         color:rgb(255, 255, 255)
        }
        }
        ''')

        self.labelPage = QLabel("Page: 1", self.GUI)
        self.labelPage.setFont(QFont('Segoe UI', 10))
        self.labelPage.setGeometry(900,645,100,20)
        self.labelPage.setAlignment(Qt.AlignVCenter)
        self.labelPage.setAlignment(Qt.AlignHCenter)
        self.labelPage.setStyleSheet('''
                QLabel{
         border: 1px solid black;
         background : rgb(23, 23, 23);
         color:rgb(255, 255, 255)
        }
        }
        ''')


        self.buttonBack = QPushButton("Back", self.GUI, clicked = lambda: MainWindow.gotoPreviousLayout())
        self.buttonBack.setFont(QFont('Segoe UI', 14))
        self.buttonBack.setGeometry(260,670,160,35)

        self.buttonLeft = QPushButton("<---", self.GUI)
        self.buttonLeft.setFont(QFont('Segoe UI', 14))
        self.buttonLeft.setGeometry(863,670,80,35)
        self.buttonLeft.clicked.connect(self.previousPage)

        self.buttonRight = QPushButton("--->", self.GUI)
        self.buttonRight.setFont(QFont('Segoe UI', 14))
        self.buttonRight.setGeometry(952,670,80,35)
        self.buttonRight.clicked.connect(self.nextPage)


        self.labelCharacter1 = QLabel(self.GUI)
        self.labelCharacter1.setGeometry(240,20,550,40)
        self.labelCharacter1.setFont(QFont('Segoe UI', 14))
        self.labelCharacter1.setAlignment(Qt.AlignVCenter)

        self.buttonExport1 = QPushButton("Export", self.GUI)
        self.buttonExport1.setGeometry(800,20,70,40)
        self.buttonExport1.setFont(QFont('Segoe UI', 14))
        self.buttonExport1.clicked.connect(self.export1)

        self.buttonDetails1 = QPushButton("Details", self.GUI, clicked = lambda: self.detailsCall("buttonDetails1"))
        self.buttonDetails1.setGeometry(880,20,70,40)
        self.buttonDetails1.setFont(QFont('Segoe UI', 14))
        self.buttonDetails1.clicked.connect(self.details1)

        self.buttonRemove1 = QPushButton("Remove", self.GUI)
        self.buttonRemove1.setGeometry(960,20,80,40)
        self.buttonRemove1.setFont(QFont('Segoe UI', 14))
        self.buttonRemove1.clicked.connect(self.remove1)


        self.labelCharacter2 = QLabel(self.GUI)
        self.labelCharacter2.setGeometry(240,70,550,40)
        self.labelCharacter2.setFont(QFont('Segoe UI', 14))
        self.labelCharacter2.setAlignment(Qt.AlignVCenter)

        self.buttonExport2 = QPushButton("Export", self.GUI)
        self.buttonExport2.setGeometry(800,70,70,40)
        self.buttonExport2.setFont(QFont('Segoe UI', 14))
        self.buttonExport2.clicked.connect(self.export2)

        self.buttonDetails2 = QPushButton("Details", self.GUI, clicked = lambda: self.detailsCall("buttonDetails2"))
        self.buttonDetails2.setGeometry(880,70,70,40)
        self.buttonDetails2.setFont(QFont('Segoe UI', 14))
        self.buttonDetails2.clicked.connect(self.details2)

        self.buttonRemove2 = QPushButton("Remove", self.GUI)
        self.buttonRemove2.setGeometry(960,70,80,40)
        self.buttonRemove2.setFont(QFont('Segoe UI', 14))
        self.buttonRemove2.clicked.connect(self.remove2)


        self.labelCharacter3 = QLabel(self.GUI)
        self.labelCharacter3.setGeometry(240,120,550,40)
        self.labelCharacter3.setFont(QFont('Segoe UI', 14))
        self.labelCharacter3.setAlignment(Qt.AlignVCenter)

        self.buttonExport3 = QPushButton("Export", self.GUI)
        self.buttonExport3.setGeometry(800,120,70,40)
        self.buttonExport3.setFont(QFont('Segoe UI', 14))
        self.buttonExport3.clicked.connect(self.export3)

        self.buttonDetails3 = QPushButton("Details", self.GUI, clicked = lambda: self.detailsCall("buttonDetails3"))
        self.buttonDetails3.setGeometry(880,120,70,40)
        self.buttonDetails3.setFont(QFont('Segoe UI', 14))
        self.buttonDetails3.clicked.connect(self.details3)

        self.buttonRemove3 = QPushButton("Remove", self.GUI)
        self.buttonRemove3.setGeometry(960,120,80,40)
        self.buttonRemove3.setFont(QFont('Segoe UI', 14))
        self.buttonRemove3.clicked.connect(self.remove3)


        self.labelCharacter4 = QLabel(self.GUI)
        self.labelCharacter4.setGeometry(240,170,550,40)
        self.labelCharacter4.setFont(QFont('Segoe UI', 14))
        self.labelCharacter4.setAlignment(Qt.AlignVCenter)

        self.buttonExport4 = QPushButton("Export", self.GUI)
        self.buttonExport4.setGeometry(800,170,70,40)
        self.buttonExport4.setFont(QFont('Segoe UI', 14))
        self.buttonExport4.clicked.connect(self.export4)

        self.buttonDetails4 = QPushButton("Details", self.GUI, clicked = lambda: self.detailsCall("buttonDetails4"))
        self.buttonDetails4.setGeometry(880,170,70,40)
        self.buttonDetails4.setFont(QFont('Segoe UI', 14))
        self.buttonDetails4.clicked.connect(self.details4)

        self.buttonRemove4 = QPushButton("Remove", self.GUI)
        self.buttonRemove4.setGeometry(960,170,80,40)
        self.buttonRemove4.setFont(QFont('Segoe UI', 14))
        self.buttonRemove4.clicked.connect(self.remove4)


        self.labelCharacter5 = QLabel(self.GUI)
        self.labelCharacter5.setGeometry(240,220,550,40)
        self.labelCharacter5.setFont(QFont('Segoe UI', 14))
        self.labelCharacter5.setAlignment(Qt.AlignVCenter)

        self.buttonExport5 = QPushButton("Export", self.GUI)
        self.buttonExport5.setGeometry(800,220,70,40)
        self.buttonExport5.setFont(QFont('Segoe UI', 14))
        self.buttonExport5.clicked.connect(self.export5)

        self.buttonDetails5 = QPushButton("Details", self.GUI, clicked = lambda: self.detailsCall("buttonDetails5"))
        self.buttonDetails5.setGeometry(880,220,70,40)
        self.buttonDetails5.setFont(QFont('Segoe UI', 14))
        self.buttonDetails5.clicked.connect(self.details5)

        self.buttonRemove5 = QPushButton("Remove", self.GUI)
        self.buttonRemove5.setGeometry(960,220,80,40)
        self.buttonRemove5.setFont(QFont('Segoe UI', 14))
        self.buttonRemove5.clicked.connect(self.remove5)


        self.labelCharacter6 = QLabel(self.GUI)
        self.labelCharacter6.setGeometry(240,270,550,40)
        self.labelCharacter6.setFont(QFont('Segoe UI', 14))
        self.labelCharacter6.setAlignment(Qt.AlignVCenter)

        self.buttonExport6 = QPushButton("Export", self.GUI)
        self.buttonExport6.setGeometry(800,270,70,40)
        self.buttonExport6.setFont(QFont('Segoe UI', 14))
        self.buttonExport6.clicked.connect(self.export6)

        self.buttonDetails6 = QPushButton("Details", self.GUI, clicked = lambda: self.detailsCall("buttonDetails6"))
        self.buttonDetails6.setGeometry(880,270,70,40)
        self.buttonDetails6.setFont(QFont('Segoe UI', 14))
        self.buttonDetails6.clicked.connect(self.details6)

        self.buttonRemove6 = QPushButton("Remove", self.GUI)
        self.buttonRemove6.setGeometry(960,270,80,40)
        self.buttonRemove6.setFont(QFont('Segoe UI', 14))
        self.buttonRemove6.clicked.connect(self.remove6)


        self.labelCharacter7 = QLabel(self.GUI)
        self.labelCharacter7.setGeometry(240,320,550,40)
        self.labelCharacter7.setFont(QFont('Segoe UI', 14))
        self.labelCharacter7.setAlignment(Qt.AlignVCenter)

        self.buttonExport7 = QPushButton("Export", self.GUI)
        self.buttonExport7.setGeometry(800,320,70,40)
        self.buttonExport7.setFont(QFont('Segoe UI', 14))
        self.buttonExport7.clicked.connect(self.export7)

        self.buttonDetails7 = QPushButton("Details", self.GUI, clicked = lambda: self.detailsCall("buttonDetails7"))
        self.buttonDetails7.setGeometry(880,320,70,40)
        self.buttonDetails7.setFont(QFont('Segoe UI', 14))
        self.buttonDetails7.clicked.connect(self.details7)

        self.buttonRemove7 = QPushButton("Remove", self.GUI)
        self.buttonRemove7.setGeometry(960,320,80,40)
        self.buttonRemove7.setFont(QFont('Segoe UI', 14))
        self.buttonRemove7.clicked.connect(self.remove7)


        self.labelCharacter8 = QLabel(self.GUI)
        self.labelCharacter8.setGeometry(240,370,550,40)
        self.labelCharacter8.setFont(QFont('Segoe UI', 14))
        self.labelCharacter8.setAlignment(Qt.AlignVCenter)

        self.buttonExport8 = QPushButton("Export", self.GUI)
        self.buttonExport8.setGeometry(800,370,70,40)
        self.buttonExport8.setFont(QFont('Segoe UI', 14))
        self.buttonExport8.clicked.connect(self.export8)

        self.buttonDetails8 = QPushButton("Details", self.GUI, clicked = lambda: self.detailsCall("buttonDetails8"))
        self.buttonDetails8.setGeometry(880,370,70,40)
        self.buttonDetails8.setFont(QFont('Segoe UI', 14))
        self.buttonDetails8.clicked.connect(self.details8)

        self.buttonRemove8 = QPushButton("Remove", self.GUI)
        self.buttonRemove8.setGeometry(960,370,80,40)
        self.buttonRemove8.setFont(QFont('Segoe UI', 14))
        self.buttonRemove8.clicked.connect(self.remove8)


        self.labelCharacter9 = QLabel(self.GUI)
        self.labelCharacter9.setGeometry(240,420,550,40)
        self.labelCharacter9.setFont(QFont('Segoe UI', 14))
        self.labelCharacter9.setAlignment(Qt.AlignVCenter)

        self.buttonExport9 = QPushButton("Export", self.GUI)
        self.buttonExport9.setGeometry(800,420,70,40)
        self.buttonExport9.setFont(QFont('Segoe UI', 14))
        self.buttonExport9.clicked.connect(self.export9)

        self.buttonDetails9 = QPushButton("Details", self.GUI, clicked = lambda: self.detailsCall("buttonDetails9"))
        self.buttonDetails9.setGeometry(880,420,70,40)
        self.buttonDetails9.setFont(QFont('Segoe UI', 14))
        self.buttonDetails9.clicked.connect(self.details9)

        self.buttonRemove9 = QPushButton("Remove", self.GUI)
        self.buttonRemove9.setGeometry(960,420,80,40)
        self.buttonRemove9.setFont(QFont('Segoe UI', 14))
        self.buttonRemove9.clicked.connect(self.remove9)


        self.labelCharacter10 = QLabel(self.GUI)
        self.labelCharacter10.setGeometry(240,470,550,40)
        self.labelCharacter10.setFont(QFont('Segoe UI', 14))
        self.labelCharacter10.setAlignment(Qt.AlignVCenter)

        self.buttonExport10 = QPushButton("Export", self.GUI)
        self.buttonExport10.setGeometry(800,470,70,40)
        self.buttonExport10.setFont(QFont('Segoe UI', 14))
        self.buttonExport10.clicked.connect(self.export10)

        self.buttonDetails10 = QPushButton("Details", self.GUI, clicked = lambda: self.detailsCall("buttonDetails10"))
        self.buttonDetails10.setGeometry(880,470,70,40)
        self.buttonDetails10.setFont(QFont('Segoe UI', 14))
        self.buttonDetails10.clicked.connect(self.details10)

        self.buttonRemove10 = QPushButton("Remove", self.GUI)
        self.buttonRemove10.setGeometry(960,470,80,40)
        self.buttonRemove10.setFont(QFont('Segoe UI', 14))
        self.buttonRemove10.clicked.connect(self.remove10)


        self.labelCharacter11 = QLabel(self.GUI)
        self.labelCharacter11.setGeometry(240,520,550,40)
        self.labelCharacter11.setFont(QFont('Segoe UI', 14))
        self.labelCharacter11.setAlignment(Qt.AlignVCenter)

        self.buttonExport11 = QPushButton("Export", self.GUI)
        self.buttonExport11.setGeometry(800,520,70,40)
        self.buttonExport11.setFont(QFont('Segoe UI', 14))
        self.buttonExport11.clicked.connect(self.export11)

        self.buttonDetails11 = QPushButton("Details", self.GUI, clicked = lambda: self.detailsCall("buttonDetails11"))
        self.buttonDetails11.setGeometry(880,520,70,40)
        self.buttonDetails11.setFont(QFont('Segoe UI', 14))
        self.buttonDetails11.clicked.connect(self.details11)

        self.buttonRemove11 = QPushButton("Remove", self.GUI)
        self.buttonRemove11.setGeometry(960,520,80,40)
        self.buttonRemove11.setFont(QFont('Segoe UI', 14))
        self.buttonRemove11.clicked.connect(self.remove11)


        self.labelCharacter12 = QLabel(self.GUI)
        self.labelCharacter12.setGeometry(240,570,550,40)
        self.labelCharacter12.setFont(QFont('Segoe UI', 14))
        self.labelCharacter12.setAlignment(Qt.AlignVCenter)

        self.buttonExport12 = QPushButton("Export", self.GUI)
        self.buttonExport12.setGeometry(800,570,70,40)
        self.buttonExport12.setFont(QFont('Segoe UI', 14))
        self.buttonExport12.clicked.connect(self.export12)

        self.buttonDetails12 = QPushButton("Details", self.GUI, clicked = lambda: self.detailsCall("buttonDetails12"))
        self.buttonDetails12.setGeometry(880,570,70,40)
        self.buttonDetails12.setFont(QFont('Segoe UI', 14))
        self.buttonDetails12.clicked.connect(self.details12)

        self.buttonRemove12 = QPushButton("Remove", self.GUI)
        self.buttonRemove12.setGeometry(960,570,80,40)
        self.buttonRemove12.setFont(QFont('Segoe UI', 14))
        self.buttonRemove12.clicked.connect(self.remove12)


        self.exportCheck()

    def Refresh(self):
        ""

    def previousPage(self):
        page = self.labelPage.text()
        length = len(page)
        page = page[6:length]
        page = int(page) - 1
        self.labelPage.setText("Page: "+str(page))

    def nextPage(self):
        page = self.labelPage.text()
        length = len(page)
        page = page[6:length]
        page = int(page) + 1
        self.labelPage.setText("Page: "+str(page))


    def exportCheck(self):
        with open("NPCdata.json", 'rb') as f:
            NPCdataWhole = json.load(f)
        listCharacters = []

        for i in NPCdataWhole:
            NPCdata = NPCdataWhole[i]
            x = str(i) + " " + str(NPCdata["Name"])
            listCharacters.append(x)

        page = self.labelPage.text()
        length = len(page)
        page = page[6:length]

        amount = len(listCharacters)

        counter = int(page) * 12 - 12
        amount -=1


        if counter <= amount:
            text = listCharacters[counter]
            self.labelCharacter1.setText(text)
            self.labelCharacter1.show()
            self.buttonExport1.show()
            self.buttonDetails1.show()
            self.buttonRemove1.show()
            counter += 1
        else:
            self.labelCharacter1.hide()
            self.buttonExport1.hide()
            self.buttonDetails1.hide()
            self.buttonRemove1.hide()
        if counter <= amount:
            text = listCharacters[counter]
            self.labelCharacter2.setText(text)
            self.labelCharacter2.show()
            self.buttonExport2.show()
            self.buttonDetails2.show()
            self.buttonRemove2.show()
            counter += 1
        else:
            self.labelCharacter2.hide()
            self.buttonExport2.hide()
            self.buttonDetails2.hide()
            self.buttonRemove2.hide()
        if counter <= amount:
            text = listCharacters[counter]
            self.labelCharacter3.setText(text)
            self.labelCharacter3.show()
            self.buttonExport3.show()
            self.buttonDetails3.show()
            self.buttonRemove3.show()
            counter += 1
        else:
            self.labelCharacter3.hide()
            self.buttonExport3.hide()
            self.buttonDetails3.hide()
            self.buttonRemove3.hide()
        if counter <= amount:
            text = listCharacters[counter]
            self.labelCharacter4.setText(text)
            self.labelCharacter4.show()
            self.buttonExport4.show()
            self.buttonDetails4.show()
            self.buttonRemove4.show()
            counter += 1
        else:
            self.labelCharacter4.hide()
            self.buttonExport4.hide()
            self.buttonDetails4.hide()
            self.buttonRemove4.hide()
        if counter <= amount:
            text = listCharacters[counter]
            self.labelCharacter5.setText(text)
            self.labelCharacter5.show()
            self.buttonExport5.show()
            self.buttonDetails5.show()
            self.buttonRemove5.show()
            counter += 1
        else:
            self.labelCharacter5.hide()
            self.buttonExport5.hide()
            self.buttonDetails5.hide()
            self.buttonRemove5.hide()
        if counter <= amount:
            text = listCharacters[counter]
            self.labelCharacter6.setText(text)
            self.labelCharacter6.show()
            self.buttonExport6.show()
            self.buttonDetails6.show()
            self.buttonRemove6.show()
            counter += 1
        else:
            self.labelCharacter6.hide()
            self.buttonExport6.hide()
            self.buttonDetails6.hide()
            self.buttonRemove6.hide()
        if counter <= amount:
            text = listCharacters[counter]
            self.labelCharacter7.setText(text)
            self.labelCharacter7.show()
            self.buttonExport7.show()
            self.buttonDetails7.show()
            self.buttonRemove7.show()
            counter += 1
        else:
            self.labelCharacter7.hide()
            self.buttonExport7.hide()
            self.buttonDetails7.hide()
            self.buttonRemove7.hide()
        if counter <= amount:
            text = listCharacters[counter]
            self.labelCharacter8.setText(text)
            self.labelCharacter8.show()
            self.buttonExport8.show()
            self.buttonDetails8.show()
            self.buttonRemove8.show()
            counter += 1
        else:
            self.labelCharacter8.hide()
            self.buttonExport8.hide()
            self.buttonDetails8.hide()
            self.buttonRemove8.hide()
        if counter <= amount:
            text = listCharacters[counter]
            self.labelCharacter9.setText(text)
            self.labelCharacter9.show()
            self.buttonExport9.show()
            self.buttonDetails9.show()
            self.buttonRemove9.show()
            counter += 1
        else:
            self.labelCharacter9.hide()
            self.buttonExport9.hide()
            self.buttonDetails9.hide()
            self.buttonRemove9.hide()
        if counter <= amount:
            text = listCharacters[counter]
            self.labelCharacter10.setText(text)
            self.labelCharacter10.show()
            self.buttonExport10.show()
            self.buttonDetails10.show()
            self.buttonRemove10.show()
            counter += 1
        else:
            self.labelCharacter10.hide()
            self.buttonExport10.hide()
            self.buttonDetails10.hide()
            self.buttonRemove10.hide()
        if counter <= amount:
            text = listCharacters[counter]
            self.labelCharacter11.setText(text)
            self.labelCharacter11.show()
            self.buttonExport11.show()
            self.buttonDetails11.show()
            self.buttonRemove11.show()
            counter += 1
        else:
            self.labelCharacter11.hide()
            self.buttonExport11.hide()
            self.buttonDetails11.hide()
            self.buttonRemove11.hide()
        if counter <= amount:
            text = listCharacters[counter]
            self.labelCharacter12.setText(text)
            self.labelCharacter12.show()
            self.buttonExport12.show()
            self.buttonDetails12.show()
            self.buttonRemove12.show()
            counter += 1
        else:
            self.labelCharacter12.hide()
            self.buttonExport12.hide()
            self.buttonDetails12.hide()
            self.buttonRemove12.hide()


        if counter <= amount:
            self.buttonRight.show()
        else:
            self.buttonRight.hide()
        if int(page) > 1:
            self.buttonLeft.show()
        else:
            self.buttonLeft.hide()

        ""

    def exportFun(self, text):
        ID = ""
        for i in text:
            if i != " ":
                ID += i
            else:
                ""
                break
        with open("NPCdata.json", 'rb') as f:
            NPCdataWhole = json.load(f)
        NPCdata = NPCdataWhole[ID]
        Name = NPCdata["Name"]

        YesRelations = NPCdata

        relations = NPCdata["Relations"]

        for i in relations:
            # print(character)
            character = relations[i]

            for i in character:
                category = character[i]
                for i in category:
                    category[i] = 0

        NPCdata["Relations"] = relations
        NoRelations = NPCdata["Relations"]


        path = "ExportedNPC/" + str(Name) + str(ID)
        try:
            os.makedirs(path)
        except:
            ""
        pathData = "ExportedNPC/" + str(Name) + str(ID) + "/" + str(Name) + str(ID) + "Data.json"


        with open(pathData, 'w') as f:
            json.dump(NoRelations, f)

        self.labelText.setText("Succesful Import")


    def removeFun(self, text):
        ID = ""
        for i in text:
            if i != " ":
                ID += i
            else:
                ""
                break
        with open("NPCdata.json", 'rb') as f:
            NPCdataWhole = json.load(f)
        NPCdataWhole.pop(ID)

        with open("NPCdata.json", 'w') as f:
            json.dump(NPCdataWhole, f)

        self.labelText.setText(text + " Removed")
        self.exportCheck()


    def detailsCall(self, who):
        if who == "buttonDetails1":
            Whole = self.labelCharacter1.text()
        elif who == "buttonDetails2":
            Whole = self.labelCharacter2.text()
        elif who == "buttonDetails3":
            Whole = self.labelCharacter3.text()
        elif who == "buttonDetails4":
            Whole = self.labelCharacter4.text()
        elif who == "buttonDetails5":
            Whole = self.labelCharacter5.text()
        elif who == "buttonDetails6":
            Whole = self.labelCharacter6.text()
        elif who == "buttonDetails7":
            Whole = self.labelCharacter7.text()
        elif who == "buttonDetails8":
            Whole = self.labelCharacter8.text()
        elif who == "buttonDetails9":
            Whole = self.labelCharacter9.text()
        elif who == "buttonDetails10":
            Whole = self.labelCharacter10.text()
        elif who == "buttonDetails11":
            Whole = self.labelCharacter11.text()
        elif who == "buttonDetails12":
            Whole = self.labelCharacter12.text()

        Counter = 0
        for i in Whole:
            if i != " ":
                Counter += 1
            else:
                break
        ID = Whole[0:Counter]
        Counter += 1
        Length = len(Whole)
        Name = Whole[Counter:Length]
        with open('tempData.json', 'rb') as f:
            tempData = json.load(f)
        tempData["DetailsData"] = {"Name":Name,"ID":ID,"Type":2,"From":"ExportMenu"}
        with open('tempData.json', 'w') as f:
            json.dump(tempData, f)




    def export1(self):
        text = self.labelCharacter1.text()
        self.exportFun(text)
        ""

    def export2(self):
        text = self.labelCharacter2.text()
        self.exportFun(text)
        ""

    def export3(self):
        text = self.labelCharacter3.text()
        self.exportFun(text)
        ""

    def export4(self):
        text = self.labelCharacter4.text()
        self.exportFun(text)
        ""

    def export5(self):
        text = self.labelCharacter5.text()
        self.exportFun(text)
        ""

    def export6(self):
        text = self.labelCharacter6.text()
        self.exportFun(text)
        ""

    def export7(self):
        text = self.labelCharacter7.text()
        self.exportFun(text)
        ""

    def export8(self):
        text = self.labelCharacter8.text()
        self.exportFun(text)
        ""

    def export9(self):
        text = self.labelCharacter9.text()
        self.exportFun(text)
        ""

    def export10(self):
        text = self.labelCharacter10.text()
        self.exportFun(text)
        ""

    def export11(self):
        text = self.labelCharacter11.text()
        self.exportFun(text)
        ""

    def export12(self):
        text = self.labelCharacter12.text()
        self.exportFun(text)
        ""


    def details1(self):
        ""

    def details2(self):
        ""

    def details3(self):
        ""

    def details4(self):
        ""

    def details5(self):
        ""

    def details6(self):
        ""

    def details7(self):
        ""

    def details8(self):
        ""

    def details9(self):
        ""

    def details10(self):
        ""

    def details11(self):
        ""

    def details12(self):
        ""



    def remove1(self):
        text = self.labelCharacter1.text()
        self.removeFun(text)
        ""

    def remove2(self):
        text = self.labelCharacter2.text()
        self.removeFun(text)
        ""

    def remove3(self):
        text = self.labelCharacter3.text()
        self.removeFun(text)
        ""

    def remove4(self):
        text = self.labelCharacter4.text()
        self.removeFun(text)
        ""

    def remove5(self):
        text = self.labelCharacter5.text()
        self.removeFun(text)
        ""

    def remove6(self):
        text = self.labelCharacter6.text()
        self.removeFun(text)
        ""

    def remove7(self):
        text = self.labelCharacter7.text()
        self.removeFun(text)
        ""

    def remove8(self):
        text = self.labelCharacter8.text()
        self.removeFun(text)
        ""

    def remove9(self):
        text = self.labelCharacter9.text()
        self.removeFun(text)
        ""

    def remove10(self):
        text = self.labelCharacter10.text()
        self.removeFun(text)
        ""

    def remove11(self):
        text = self.labelCharacter11.text()
        self.removeFun(text)
        ""

    def remove12(self):
        text = self.labelCharacter12.text()
        self.removeFun(text)
        ""


def Initialize(self, Reference):
    if "ImportUI" not in Globals.Layouts:
        Object = UiLayoutImportMenu()
    if "ExportUI" not in Globals.Layouts:
        Object = UiLayoutExportMenu()
