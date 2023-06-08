import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QTextCursor
import json
import os
import os.path
import Globals
Log = Globals.Layouts["MainF"].Log

class SaveObject:
    def __init__(self, Path):
        self.Path = Path

    def GetWidget(self):
        SaveWidget = QWidget()
        SaveWidget.setMinimumWidth(1115)
        SaveWidget.setMaximumWidth(1115)
        SaveWidget.setMinimumHeight(45)
        SaveWidget.setMaximumHeight(45)
        SaveWidget.setStyleSheet('''
        .QWidget{
        border: 1px solid black;
        background : rgb(23, 23, 23)
        }
        QLabel{
        border: 1px solid black;
        background : rgb(35, 35, 35)
        }
        ''')

        SaveName = QLabel(SaveWidget)
        Name = self.Path[6:]
        Name = Name[:-4]

        SaveName.setText(Name)
        SaveName.setGeometry(0,0,1115,45)

        def DeleteFunc(self):
            Globals.Layouts["SaveUI"].Remove(self.Path)
        RemoveButton = QPushButton(SaveWidget, clicked = lambda: DeleteFunc(self))
        RemoveButton.setStyleSheet("border-image: url(Resources/SoLResources/removeIcon.png); ")
        RemoveButton.setGeometry(960,2,45,45)

        def SaveFunc(self):
            Globals.Layouts["SaveUI"].Save(self.Path)
        SaveButton = QPushButton(SaveWidget, clicked = lambda: SaveFunc(self))
        SaveButton.setStyleSheet("border-image: url(Resources/SoLResources/saveIcon.png); ")
        SaveButton.setGeometry(1015,2,45,45)

        def LoadFunc(self):
            Globals.Layouts["SaveUI"].Load(self.Path)
        LoadButton = QPushButton(SaveWidget, clicked = lambda: LoadFunc(self))
        LoadButton.setStyleSheet("border-image: url(Resources/SoLResources/loadIcon.png);")
        LoadButton.setGeometry(1065,2,45,45)


        return SaveWidget


class UiLayoutSaveMenuOld(object):
    def UIOld(self):
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
        }gb(255, 255, 255)
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
        self.labelText.setGeometry(440,650,400,41)
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
        self.labelPage.setGeometry(900,625,100,20)
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



        self.buttonBack = QPushButton("Back To Menu", self.GUI)
        self.buttonBack.setFont(QFont('Segoe UI', 14))
        self.buttonBack.setGeometry(260,650,160,35)

        self.buttonLeft = QPushButton("<---", self.GUI)
        self.buttonLeft.setFont(QFont('Segoe UI', 14))
        self.buttonLeft.setGeometry(863,650,80,35)
        self.buttonLeft.clicked.connect(self.previousPage)

        self.buttonRight = QPushButton("--->", self.GUI)
        self.buttonRight.setFont(QFont('Segoe UI', 14))
        self.buttonRight.setGeometry(952,650,80,35)
        self.buttonRight.clicked.connect(self.nextPage)


        self.lineSaveTop = QLineEdit(self.GUI)
        self.lineSaveTop.setFont(QFont('Segoe UI', 14))
        self.lineSaveTop.setGeometry(240,30,700,40)
        self.lineSaveTop.setPlaceholderText("Save Name")
        self.lineSaveTop.setAlignment(Qt.AlignVCenter)

        self.buttonSaveTop = QPushButton(self.GUI)
        self.buttonSaveTop.setStyleSheet("background-image : url(Resources/saveIcon.png);")
        self.buttonSaveTop.setGeometry(950,30,40,40)
        self.buttonSaveTop.clicked.connect(self.saveButtonTop)

        self.buttonLoadTop = QPushButton(self.GUI)
        self.buttonLoadTop.setStyleSheet("background-image : url(Resources/loadIcon.png);")
        self.buttonLoadTop.setGeometry(995,30,40,40)
        self.buttonLoadTop.clicked.connect(self.loadButtonTop)


        self.labelSave1 = QLabel(self.GUI)
        self.labelSave1.setFont(QFont('Segoe UI', 14))
        self.labelSave1.setGeometry(240,130,655,40)
        self.labelSave1.setAlignment(Qt.AlignVCenter)

        self.buttonSave1 = QPushButton(self.GUI)
        self.buttonSave1.setStyleSheet("background-image : url(Resources/saveIcon.png);")
        self.buttonSave1.setGeometry(905,130,40,40)
        self.buttonSave1.clicked.connect(self.saveButton1)

        self.buttonLoad1 = QPushButton(self.GUI)
        self.buttonLoad1.setStyleSheet("background-image : url(Resources/loadIcon.png);")
        self.buttonLoad1.setGeometry(950,130,40,40)
        self.buttonLoad1.clicked.connect(self.loadButton1)

        self.buttonDelete1 = QPushButton(self.GUI, clicked = lambda: self.deleteFun(1))
        self.buttonDelete1.setStyleSheet("background-image : url(Resources/deleteIcon.png);")
        self.buttonDelete1.setGeometry(995,130,40,40)


        self.labelSave2 = QLabel(self.GUI)
        self.labelSave2.setFont(QFont('Segoe UI', 14))
        self.labelSave2.setGeometry(240,180,655,40)
        self.labelSave2.setAlignment(Qt.AlignVCenter)

        self.buttonSave2 = QPushButton(self.GUI)
        self.buttonSave2.setStyleSheet("background-image : url(Resources/saveIcon.png);")
        self.buttonSave2.setGeometry(905,180,40,40)
        self.buttonSave2.clicked.connect(self.saveButton2)

        self.buttonLoad2 = QPushButton(self.GUI)
        self.buttonLoad2.setStyleSheet("background-image : url(Resources/loadIcon.png);")
        self.buttonLoad2.setGeometry(950,180,40,40)
        self.buttonLoad2.clicked.connect(self.loadButton2)

        self.buttonDelete2 = QPushButton(self.GUI, clicked = lambda: self.deleteFun(2))
        self.buttonDelete2.setStyleSheet("background-image : url(Resources/deleteIcon.png);")
        self.buttonDelete2.setGeometry(995,180,40,40)


        self.labelSave3 = QLabel(self.GUI)
        self.labelSave3.setFont(QFont('Segoe UI', 14))
        self.labelSave3.setGeometry(240,230,655,40)
        self.labelSave3.setAlignment(Qt.AlignVCenter)

        self.buttonSave3 = QPushButton(self.GUI)
        self.buttonSave3.setStyleSheet("background-image : url(Resources/saveIcon.png);")
        self.buttonSave3.setGeometry(905,230,40,40)
        self.buttonSave3.clicked.connect(self.saveButton3)

        self.buttonLoad3 = QPushButton(self.GUI)
        self.buttonLoad3.setStyleSheet("background-image : url(Resources/loadIcon.png);")
        self.buttonLoad3.setGeometry(950,230,40,40)
        self.buttonLoad3.clicked.connect(self.loadButton3)

        self.buttonDelete3 = QPushButton(self.GUI, clicked = lambda: self.deleteFun(3))
        self.buttonDelete3.setStyleSheet("background-image : url(Resources/deleteIcon.png);")
        self.buttonDelete3.setGeometry(995,230,40,40)


        self.labelSave4 = QLabel(self.GUI)
        self.labelSave4.setFont(QFont('Segoe UI', 14))
        self.labelSave4.setGeometry(240,280,655,40)
        self.labelSave4.setAlignment(Qt.AlignVCenter)

        self.buttonSave4 = QPushButton(self.GUI)
        self.buttonSave4.setStyleSheet("background-image : url(Resources/saveIcon.png);")
        self.buttonSave4.setGeometry(905,280,40,40)
        self.buttonSave4.clicked.connect(self.saveButton4)

        self.buttonLoad4 = QPushButton(self.GUI)
        self.buttonLoad4.setStyleSheet("background-image : url(Resources/loadIcon.png);")
        self.buttonLoad4.setGeometry(950,280,40,40)
        self.buttonLoad4.clicked.connect(self.loadButton4)

        self.buttonDelete4 = QPushButton(self.GUI, clicked = lambda: self.deleteFun(4))
        self.buttonDelete4.setStyleSheet("background-image : url(Resources/deleteIcon.png);")
        self.buttonDelete4.setGeometry(995,280,40,40)


        self.labelSave5 = QLabel(self.GUI)
        self.labelSave5.setFont(QFont('Segoe UI', 14))
        self.labelSave5.setGeometry(240,330,655,40)
        self.labelSave5.setAlignment(Qt.AlignVCenter)

        self.buttonSave5 = QPushButton(self.GUI)
        self.buttonSave5.setStyleSheet("background-image : url(Resources/saveIcon.png);")
        self.buttonSave5.setGeometry(905,330,40,40)
        self.buttonSave5.clicked.connect(self.saveButton5)

        self.buttonLoad5 = QPushButton(self.GUI)
        self.buttonLoad5.setStyleSheet("background-image : url(Resources/loadIcon.png);")
        self.buttonLoad5.setGeometry(950,330,40,40)
        self.buttonLoad5.clicked.connect(self.loadButton5)

        self.buttonDelete5 = QPushButton(self.GUI, clicked = lambda: self.deleteFun(5))
        self.buttonDelete5.setStyleSheet("background-image : url(Resources/deleteIcon.png);")
        self.buttonDelete5.setGeometry(995,330,40,40)


        self.labelSave6 = QLabel(self.GUI)
        self.labelSave6.setFont(QFont('Segoe UI', 14))
        self.labelSave6.setGeometry(240,380,655,40)
        self.labelSave6.setAlignment(Qt.AlignVCenter)

        self.buttonSave6 = QPushButton(self.GUI)
        self.buttonSave6.setStyleSheet("background-image : url(Resources/saveIcon.png);")
        self.buttonSave6.setGeometry(905,380,40,40)
        self.buttonSave6.clicked.connect(self.saveButton6)

        self.buttonLoad6 = QPushButton(self.GUI)
        self.buttonLoad6.setStyleSheet("background-image : url(Resources/loadIcon.png);")
        self.buttonLoad6.setGeometry(950,380,40,40)
        self.buttonLoad6.clicked.connect(self.loadButton6)

        self.buttonDelete6 = QPushButton(self.GUI, clicked = lambda: self.deleteFun(6))
        self.buttonDelete6.setStyleSheet("background-image : url(Resources/deleteIcon.png);")
        self.buttonDelete6.setGeometry(995,380,40,40)


        self.labelSave7 = QLabel(self.GUI)
        self.labelSave7.setFont(QFont('Segoe UI', 14))
        self.labelSave7.setGeometry(240,430,655,40)
        self.labelSave7.setAlignment(Qt.AlignVCenter)

        self.buttonSave7 = QPushButton(self.GUI)
        self.buttonSave7.setStyleSheet("background-image : url(Resources/saveIcon.png);")
        self.buttonSave7.setGeometry(905,430,40,40)
        self.buttonSave7.clicked.connect(self.saveButton7)

        self.buttonLoad7 = QPushButton(self.GUI)
        self.buttonLoad7.setStyleSheet("background-image : url(Resources/loadIcon.png);")
        self.buttonLoad7.setGeometry(950,430,40,40)
        self.buttonLoad7.clicked.connect(self.loadButton7)

        self.buttonDelete7 = QPushButton(self.GUI, clicked = lambda: self.deleteFun(7))
        self.buttonDelete7.setStyleSheet("background-image : url(Resources/deleteIcon.png);")
        self.buttonDelete7.setGeometry(995,430,40,40)


        self.labelSave8 = QLabel(self.GUI)
        self.labelSave8.setFont(QFont('Segoe UI', 14))
        self.labelSave8.setGeometry(240,480,655,40)
        self.labelSave8.setAlignment(Qt.AlignVCenter)

        self.buttonSave8 = QPushButton(self.GUI)
        self.buttonSave8.setStyleSheet("background-image : url(Resources/saveIcon.png);")
        self.buttonSave8.setGeometry(905,480,40,40)
        self.buttonSave8.clicked.connect(self.saveButton8)

        self.buttonLoad8 = QPushButton(self.GUI)
        self.buttonLoad8.setStyleSheet("background-image : url(Resources/loadIcon.png);")
        self.buttonLoad8.setGeometry(950,480,40,40)
        self.buttonLoad8.clicked.connect(self.loadButton8)

        self.buttonDelete8 = QPushButton(self.GUI, clicked = lambda: self.deleteFun(8))
        self.buttonDelete8.setStyleSheet("background-image : url(Resources/deleteIcon.png);")
        self.buttonDelete8.setGeometry(995,480,40,40)


        self.labelSave9 = QLabel(self.GUI)
        self.labelSave9.setFont(QFont('Segoe UI', 14))
        self.labelSave9.setGeometry(240,530,655,40)
        self.labelSave9.setAlignment(Qt.AlignVCenter)

        self.buttonSave9 = QPushButton(self.GUI)
        self.buttonSave9.setStyleSheet("background-image : url(Resources/saveIcon.png);")
        self.buttonSave9.setGeometry(905,530,40,40)
        self.buttonSave9.clicked.connect(self.saveButton9)

        self.buttonLoad9 = QPushButton(self.GUI)
        self.buttonLoad9.setStyleSheet("background-image : url(Resources/loadIcon.png);")
        self.buttonLoad9.setGeometry(950,530,40,40)
        self.buttonLoad9.clicked.connect(self.loadButton9)

        self.buttonDelete9 = QPushButton(self.GUI, clicked = lambda: self.deleteFun(9))
        self.buttonDelete9.setStyleSheet("background-image : url(Resources/deleteIcon.png);")
        self.buttonDelete9.setGeometry(995,530,40,40)


        self.labelSave10 = QLabel(self.GUI)
        self.labelSave10.setFont(QFont('Segoe UI', 14))
        self.labelSave10.setGeometry(240,580,655,40)
        self.labelSave10.setAlignment(Qt.AlignVCenter)

        self.buttonSave10 = QPushButton(self.GUI)
        self.buttonSave10.setStyleSheet("background-image : url(Resources/saveIcon.png);")
        self.buttonSave10.setGeometry(905,580,40,40)
        self.buttonSave10.clicked.connect(self.saveButton10)

        self.buttonLoad10 = QPushButton(self.GUI)
        self.buttonLoad10.setStyleSheet("background-image : url(Resources/loadIcon.png);")
        self.buttonLoad10.setGeometry(950,580,40,40)
        self.buttonLoad10.clicked.connect(self.loadButton10)

        self.buttonDelete10 = QPushButton(self.GUI, clicked = lambda: self.deleteFun(10))
        self.buttonDelete10.setStyleSheet("background-image : url(Resources/deleteIcon.png);")
        self.buttonDelete10.setGeometry(995,580,40,40)

        self.saveCheck()



    def saveCheck(self):
        # with open('saveData.json', 'rb') as f:
        #     saves = json.load(f)
        # ###CHECKS THAT FILES INDEED EXIST IF NOT THEN DELETES THE ENTRY FROM THE FILE
        # toRemoveList = []
        # for i in saves:
        #     pathFile = "saves/" + i
        #     fileExists = os.path.exists(pathFile)
        #     if fileExists == False:
        #         toRemoveList.append(i)
        # if toRemoveList != []:
        #     for i in toRemoveList:
        #         saves.pop(i)
        # ###CHECKS IF THERE IS NEW FILES IN THE SAVES FOLDER, IF SO THEN ASSIGN THEM VALUES AT THE TOP.
        # savesList = os.listdir("saves/")
        # for i in savesList:
        #     if i in saves:
        #         ""
        #     else:
        #         try:
        #             maxValue = max(saves.values())
        #             newValue = maxValue + 1
        #             saves[i] = newValue
        #         except:
        #             maxValue = 1
        #             newValue = maxValue + 1
        #             saves[i] = newValue
        # ###SORTS THE DICT
        # halfSortedDict = sorted(saves.items(), key=lambda x: x[1])
        # sortedDict = {}
        # for i in halfSortedDict:
        #     sortedDict[i[0]] = i[1]
        # ####CHECKS FOR THE PAGE


        saves = os.listdir("saves/")
        newlist = []
        for i in saves:
            x = "saves/" + str(i)
            newlist.append(x)
        newlist.sort(key=os.path.getmtime)
        sortedDict = []
        for i in newlist:
            length = len(i)
            x = i[6:length]
            sortedDict.append(x)

        page = self.labelPage.text()
        length = len(page)
        page = page[6:length]

        ###APPEARS THE LABELS AND ASSIGNS THEM A SAVE.
        amount = len(sortedDict)

        counter = int(page) * 10 - 10
        amount -=1
        if counter <= amount:
            self.labelSave1.show()
            self.labelSave1.setText(list(sortedDict)[amount-counter])
            self.buttonSave1.show()
            self.buttonLoad1.show()
            self.buttonDelete1.show()
            counter += 1
        else:
            self.labelSave1.hide()
            self.buttonSave1.hide()
            self.buttonLoad1.hide()
            self.buttonDelete1.hide()
        if counter <= amount:
            self.labelSave2.show()
            self.labelSave2.setText(list(sortedDict)[amount-counter])
            self.buttonSave2.show()
            self.buttonLoad2.show()
            self.buttonDelete2.show()
            counter += 1
        else:
            self.labelSave2.hide()
            self.buttonSave2.hide()
            self.buttonLoad2.hide()
            self.buttonDelete2.hide()
        if counter <= amount:
            self.labelSave3.show()
            self.labelSave3.setText(list(sortedDict)[amount-counter])
            self.buttonSave3.show()
            self.buttonLoad3.show()
            self.buttonDelete3.show()
            counter += 1
        else:
            self.labelSave3.hide()
            self.buttonSave3.hide()
            self.buttonLoad3.hide()
            self.buttonDelete3.hide()
        if counter <= amount:
            self.labelSave4.show()
            self.labelSave4.setText(list(sortedDict)[amount-counter])
            self.buttonSave4.show()
            self.buttonLoad4.show()
            self.buttonDelete4.show()
            counter += 1
        else:
            self.labelSave4.hide()
            self.buttonSave4.hide()
            self.buttonLoad4.hide()
            self.buttonDelete4.hide()
        if counter <= amount:
            self.labelSave5.show()
            self.labelSave5.setText(list(sortedDict)[amount-counter])
            self.buttonSave5.show()
            self.buttonLoad5.show()
            self.buttonDelete5.show()
            counter += 1
        else:
            self.labelSave5.hide()
            self.buttonSave5.hide()
            self.buttonLoad5.hide()
            self.buttonDelete5.hide()
        if counter <= amount:
            self.labelSave6.show()
            self.labelSave6.setText(list(sortedDict)[amount-counter])
            self.buttonSave6.show()
            self.buttonLoad6.show()
            self.buttonDelete6.show()
            counter += 1
        else:
            self.labelSave6.hide()
            self.buttonSave6.hide()
            self.buttonLoad6.hide()
            self.buttonDelete6.hide()
        if counter <= amount:
            self.labelSave7.show()
            self.labelSave7.setText(list(sortedDict)[amount-counter])
            self.buttonSave7.show()
            self.buttonLoad7.show()
            self.buttonDelete7.show()
            counter += 1
        else:
            self.labelSave7.hide()
            self.buttonSave7.hide()
            self.buttonLoad7.hide()
            self.buttonDelete7.hide()
        if counter <= amount:
            self.labelSave8.show()
            self.labelSave8.setText(list(sortedDict)[amount-counter])
            self.buttonSave8.show()
            self.buttonLoad8.show()
            self.buttonDelete8.show()
            counter += 1
        else:
            self.labelSave8.hide()
            self.buttonSave8.hide()
            self.buttonLoad8.hide()
            self.buttonDelete8.hide()
        if counter <= amount:
            self.labelSave9.show()
            self.labelSave9.setText(list(sortedDict)[amount-counter])
            self.buttonSave9.show()
            self.buttonLoad9.show()
            self.buttonDelete9.show()
            counter += 1
        else:
            self.labelSave9.hide()
            self.buttonSave9.hide()
            self.buttonLoad9.hide()
            self.buttonDelete9.hide()
        if counter <= amount:
            self.labelSave10.show()
            self.labelSave10.setText(list(sortedDict)[amount-counter])
            self.buttonSave10.show()
            self.buttonLoad10.show()
            self.buttonDelete10.show()
            counter += 1
        else:
            self.labelSave10.hide()
            self.buttonSave10.hide()
            self.buttonLoad10.hide()
            self.buttonDelete10.hide()

        ### APPEARS THE PAGE BUTTONS
        if counter <= amount:
            self.buttonRight.show()
        else:
            self.buttonRight.hide()

        if int(page) > 1:
            self.buttonLeft.show()
        else:
            self.buttonLeft.hide()


        #### WRITES THE POSSIBLE CHANGES TO THE saveData FILE
        with open('saveData.json', 'w') as f:
            json.dump(sortedDict, f)

    def nextPage(self):
        page = self.labelPage.text()
        length = len(page)
        page = page[6:length]
        page = int(page) + 1
        self.labelPage.setText("Page: "+str(page))
        self.saveCheck()

    def previousPage(self):
        page = self.labelPage.text()
        length = len(page)
        page = page[6:length]
        page = int(page) - 1
        self.labelPage.setText("Page: "+str(page))
        self.saveCheck()

    def saveFun(self, saveName):
        if saveName == "":
            self.labelText.setText("Please Enter a Name")
        else:
            false = "no"
            for i in saveName:
                if i == ":":
                    self.labelText.setText('''Please Remove the ':' ''')
                    false = "yes"
                else:
                    ""
            if false != "yes":

                with open('tempData.json', 'rb') as f:
                    tempData = json.load(f)
                with open('enviorementData.json', 'rb') as f:
                    enviorementData = json.load(f)
                with open('NPCData.json', 'rb') as f:
                    NPCData = json.load(f)
                with open('PCdata.json', 'rb') as f:
                    PCdata = json.load(f)

                data = {"tempData":tempData, "enviorementData":enviorementData, "NPCData":NPCData, "PCdata":PCdata}
                savePath = "saves/" + str(saveName)

                length = len(savePath)
                y = int(length) - 4
                z = int(length)
                x = savePath[y:z]

                if x == ".sav":
                    ""
                else:
                    savePath += ".sav"
                with open(savePath, 'w') as f:
                    json.dump(data, f)
                # self.updateList(saveName)
                self.labelText.setText('''Succesful Save''')
                self.saveCheck()

    def deleteFun(self, button):
        if button == 1: save = self.labelSave1.text()
        elif button == 2: save = self.labelSave2.text()
        elif button == 3: save = self.labelSave3.text()
        elif button == 4: save = self.labelSave4.text()
        elif button == 5: save = self.labelSave5.text()
        elif button == 6: save = self.labelSave6.text()
        elif button == 7: save = self.labelSave7.text()
        elif button == 8: save = self.labelSave8.text()
        elif button == 9: save = self.labelSave9.text()
        elif button == 10: save = self.labelSave10.text()
        path = "saves/" + str(save)
        os.remove(path)
        self.labelText.setText('''Savefile Deleted''')
        self.saveCheck()


    def loadFun(self, saveName):
        path = "saves/" + str(saveName)
        if os.path.exists(path):
            try:
                with open(path, 'rb') as f:
                    saveData = json.load(f)

                saveName = "saves/" + str(saveName)
                with open(saveName, 'rb') as f:
                    data = json.load(f)


                tempData = data["tempData"]
                enviorementData = data["enviorementData"]
                NPCData = data["NPCData"]
                PCdata = data["PCdata"]


                with open("tempData.json", 'w') as f:
                    json.dump(tempData, f)
                with open("NPCData.json", 'w') as f:
                    json.dump(NPCData, f)
                with open("enviorementData.json", 'w') as f:
                    json.dump(enviorementData, f)
                with open("PCdata.json", 'w') as f:
                    json.dump(PCdata, f)



                self.labelText.setText("Succesful Load")




            except:
                self.labelText.setText("Save Corrupted")

        else:
            self.labelText.setText("Save Doesn't Exist")



    def saveButtonTop(self):
        save = self.lineSaveTop.text()
        self.saveFun(save)

    def saveButton1(self):
        save = self.labelSave1.text()
        self.saveFun(save)

    def saveButton2(self):
        save = self.labelSave2.text()
        self.saveFun(save)

    def saveButton3(self):
        save = self.labelSave3.text()
        self.saveFun(save)

    def saveButton4(self):
        save = self.labelSave4.text()
        self.saveFun(save)

    def saveButton5(self):
        save = self.labelSave5.text()
        self.saveFun(save)

    def saveButton6(self):
        save = self.labelSave6.text()
        self.saveFun(save)

    def saveButton7(self):
        save = self.labelSave7.text()
        self.saveFun(save)

    def saveButton8(self):
        save = self.labelSave8.text()
        self.saveFun(save)

    def saveButton9(self):
        save = self.labelSave9.text()
        self.saveFun(save)

    def saveButton10(self):
        save = self.labelSave10.text()
        self.saveFun(save)



    def loadButtonTop(self):
        save = self.lineSaveTop.text()
        self.loadFun(save)

    def loadButton1(self):
        save = self.labelSave1.text()
        self.loadFun(save)

    def loadButton2(self):
        save = self.labelSave2.text()
        self.loadFun(save)

    def loadButton3(self):
        save = self.labelSave3.text()
        self.loadFun(save)

    def loadButton4(self):
        save = self.labelSave4.text()
        self.loadFun(save)

    def loadButton5(self):
        save = self.labelSave5.text()
        self.loadFun(save)

    def loadButton6(self):
        save = self.labelSave6.text()
        self.loadFun(save)

    def loadButton7(self):
        save = self.labelSave7.text()
        self.loadFun(save)

    def loadButton8(self):
        save = self.labelSave8.text()
        self.loadFun(save)

    def loadButton9(self):
        save = self.labelSave9.text()
        self.loadFun(save)

    def loadButton10(self):
        save = self.labelSave10.text()
        self.loadFun(save)


class UiLayoutSaveMenu(object):
    def __init__(self):
        Globals.Layouts["SaveUI"] = self
        Globals.LayoutsData["SaveUI"] = {"Source":"SoLMenuUI", "Initialized":0}

    def UI(self):
        MainWindow = Globals.Layouts["MainF"]
        self.GUI = QWidget(MainWindow)
        self.GUI.setStyleSheet('''
        QWidget{
        background-color:rgb(35,35,35);
        }
        .QGroupBox{
        border:none;
        background:none;
        }

        .QScrollArea{
        border:none;
        background-color:rgba(23,23,23,0)
        }

        QPushButton{
        color:rgb(255, 255, 255);
        font-size: 14pt;
        font-family: Segoe UI;
        }
        QPushButton:hover{
        color:rgb(255, 255, 0);
        }

        QLabel{
        color:rgb(255, 255, 255);
        border:1px solid black;
        font-size: 16pt;
        font-family: Segoe UI;
        }
        QLabel:hover{
        color:rgb(255, 255, 0);
        }

        QLabel#MainTitle{
        color:rgb(255, 255, 255);
        border:1px solid black;
        font-size: 20pt;
        font-family: Segoe UI;
        }

        QLabel#SubTitle{
        color:rgb(255, 255, 255);
        border:1px solid black;
        font-size: 18pt;
        font-family: Segoe UI;
        }
        QLabel#SubTitle:hover{
        color:rgb(255, 255, 0);
        }

        QLineEdit{
        color:rgb(255, 255, 255);
        border:1px solid black;
        background-color:rgb(23,23,23);
        font-size: 14pt;
        font-family: Segoe UI;
        }

        QTextEdit{
        color:rgb(255, 255, 255);
        border:1px solid black;
        background-color:rgb(35,35,35);
        font-size: 14pt;
        font-family: Segoe UI;
        }

        QComboBox{
        background-color:rgb(23,23,23);
        color:rgb(255, 255, 255);
        font-size: 14pt;
        font-family: Segoe UI;
        }
        QComboBox:hover{
        color:rgb(255, 255, 0);
        }
		QComboBox QAbstractItemView {
        border: 1px solid grey;
        color: white;
        selection-color: yellow;
		}

        QRadioButton{
        color:rgb(255, 255, 255);
        font-size: 14pt;
        font-family: Segoe UI;
        }
        QRadioButton:hover{
        color:rgb(255, 255, 0);
        }

        QToolTip{
        background-color: rgb(23,23,23);
        color: white;
        border: 1px solid black;
        font-size: 14pt;
        font-family: Segoe UI;


        }

        ''')

        self.LineSave = QLineEdit(self.GUI)
        self.LineSave.setGeometry(237,5,1125,45)

        self.ButtonSave = QPushButton(self.GUI, clicked = lambda: self.Save(self.LineSave.text()) )
        self.ButtonSave.setStyleSheet("border-image: url(Resources/SoLResources/saveIcon.png);")
        self.ButtonSave.setGeometry(1272,7,40,40)

        self.ButtonLoad = QPushButton(self.GUI, clicked = lambda: self.Load(self.LineSave.text()) )
        self.ButtonLoad.setStyleSheet("border-image: url(Resources/SoLResources/loadIcon.png);")
        self.ButtonLoad.setGeometry(1317,7,40,40)

        self.ScrollSaves = QScrollArea(self.GUI)
        self.ScrollSaves.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollSaves.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ScrollSaves.setGeometry(237,55,1125,900)
        self.ScrollSaves.setStyleSheet('''
        .QScrollArea{
        border: none;
        background-color:rgb(23, 23, 23);
        }
        QGroupBox{
        border: none;
        }
        ''')
        self.FormSaves = QVBoxLayout()
        self.GroupBoxSaves = QGroupBox()
        self.GroupBoxSaves.setLayout(self.FormSaves)
        self.GroupBoxSaves.setMinimumWidth(1125)
        self.GroupBoxSaves.setMaximumWidth(1125)
        self.ScrollSaves.setWidget(self.GroupBoxSaves)
        self.FormSaves.setContentsMargins(0, 0, 0, 5)
        self.FormSaves.WigetsDict = {}
        self.FormSaves.setContentsMargins(5, 0, 0, 0)


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

        self.Refresh()


    def Refresh(self):
        DateData = Globals.SoLEnviorementData["DateData"]
        TempName = f'''{DateData["Year"]}_{DateData["Month"]}_{DateData["Day"]}_{int((DateData["Hour"]-(DateData["Hour"]%60))/60)}_{DateData["Hour"]%60}'''
        self.LineSave.setPlaceholderText(TempName)

        FilesList = os.listdir("saves/")
        Saves = []
        for FileName in FilesList:
            if FileName.endswith(".sav"):
                SavePath = "saves/" + str(FileName)
                Saves.append(SavePath)
        Saves.sort(key=os.path.getmtime)
        Saves.reverse()

        for SaveName in self.FormSaves.WigetsDict:
            self.FormSaves.removeWidget(self.FormSaves.WigetsDict[SaveName]["Widget"])
        self.FormSaves.WigetsDict = {}

        for SaveName in Saves:
            Object = SaveObject(SaveName)
            Widget = Object.GetWidget()
            self.FormSaves.addWidget(Widget)
            self.FormSaves.WigetsDict[SaveName] = {"Object":Object, "Widget":Widget}

        Height = len(self.FormSaves.WigetsDict)*50
        self.GroupBoxSaves.setMinimumHeight(Height)
        self.GroupBoxSaves.setMaximumHeight(Height)

    def Save(self, FilePath):
        if FilePath == "":
            self.LabelStatus.setText("Please input a save name")
        else:
            OriginalName = FilePath
            if not FilePath.startswith("saves/"):
                FilePath = f'''saves/{FilePath}'''
            if not FilePath.endswith(".sav"):
                FilePath = f'''{FilePath}.sav'''

            Globals.CurrentSession["SoLNPCData"] = Globals.SoLNPCData
            Globals.CurrentSession["SoLPCData"] = Globals.SoLPCData
            Globals.CurrentSession["SoLTempData"] = Globals.SoLTempData
            Globals.CurrentSession["SoLOtherData"] = Globals.SoLOtherData
            Globals.CurrentSession["SoLEnviorementData"] = Globals.SoLEnviorementData
            Globals.CurrentSession["SoLNPCSchedules"] = Globals.SoLNPCSchedules
            Globals.CurrentSession["SoLFlavorDict"] = Globals.SoLFlavorDict
            with open(FilePath, 'w') as f:
                json.dump(Globals.CurrentSession, f)
            self.Refresh()

            Name = FilePath[6:]
            Name = Name[:-4]
            self.LabelStatus.setText(f'''Successfully  saved {Name}''')

    def Load(self, FilePath):
        if FilePath == "":
            self.LabelStatus.setText("Please input a save name")
        else:
            try:
                OriginalName = FilePath
                if not FilePath.startswith("saves/"):
                    FilePath = f'''saves/{FilePath}'''
                if not FilePath.endswith(".sav"):
                    FilePath = f'''{FilePath}.sav'''

                with open(FilePath, 'rb') as f:
                    NewSession = json.load(f)

                Globals.CurrentSession = NewSession

                Globals.SoLNPCData = Globals.CurrentSession["SoLNPCData"]
                Globals.SoLPCData = Globals.CurrentSession["SoLPCData"]
                Globals.SoLTempData = Globals.CurrentSession["SoLTempData"]
                Globals.SoLOtherData = Globals.CurrentSession["SoLOtherData"]
                Globals.SoLEnviorementData = Globals.CurrentSession["SoLEnviorementData"]
                Globals.SoLNPCSchedules = Globals.CurrentSession["SoLNPCSchedules"]
                Globals.SoLFlavorDict = Globals.CurrentSession["SoLFlavorDict"]


                self.Refresh()

                Name = FilePath[6:]
                Name = Name[:-4]
                self.LabelStatus.setText(f'''Successfully  loaded {Name}''')
            except:
                Name = FilePath[6:]
                Name = Name[:-4]
                self.LabelStatus.setText(f'''Couldn't load {Name}''')

    def Remove(self, FilePath):
        OriginalName = FilePath
        if not FilePath.startswith("saves/"):
            FilePath = f'''saves/{FilePath}'''
        if not FilePath.endswith(".sav"):
            FilePath = f'''{FilePath}.sav'''

        os.remove(FilePath)

        self.Refresh()

        Name = FilePath[6:]
        Name = Name[:-4]
        self.LabelStatus.setText(f'''Successfully  removed {Name}''')


def Initialize(self, Reference):
    if "SaveUI" not in Globals.Layouts:
        Object = UiLayoutSaveMenu()
