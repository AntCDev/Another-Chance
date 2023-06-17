import json
import os
import os.path
import pathlib

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

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
        # Name = self.Path[6:]
        # Name = Name[:-4]
        #
        # try:
        #     print("GGG", pathlib.Path(self.Path).name[:-4] )
        # except Exception as e:
        #     print("BB", e)

        Name = pathlib.Path(self.Path).name[:-4]

        SaveName.setText(Name)
        SaveName.setGeometry(0,0,1115,45)

        def DeleteFunc(self):
            Globals.Layouts["SaveUI"].Remove(self.Path)
        RemoveButton = QLabel(SaveWidget)
        RemoveButton.setGeometry(960,2,45,45)
        RemoveButton.mouseReleaseEvent = lambda event: DeleteFunc(self)
        RemoveButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "removeIcon.png" ) ))
        RemoveButton.setStyleSheet("border:none; background:none;")
        RemoveButton.setScaledContents(True)

        def SaveFunc(self):
            Globals.Layouts["SaveUI"].Save(self.Path)
        SaveButton = QLabel(SaveWidget)
        SaveButton.setGeometry(1015,2,45,45)
        SaveButton.mouseReleaseEvent = lambda event: SaveFunc(self)
        SaveButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "saveIcon.png" ) ))
        SaveButton.setStyleSheet("border:none; background:none;")
        SaveButton.setScaledContents(True)

        def LoadFunc(self):
            Globals.Layouts["SaveUI"].Load(self.Path)
        LoadButton = QLabel(SaveWidget)
        LoadButton.setGeometry(1065,2,45,45)
        LoadButton.mouseReleaseEvent = lambda event: LoadFunc(self)
        LoadButton.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "loadIcon.png" ) ))
        LoadButton.setStyleSheet("border:none; background:none;")
        LoadButton.setScaledContents(True)


        return SaveWidget

class UiLayoutSaveMenu:
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

        self.ButtonSave = QLabel(self.GUI)
        self.ButtonSave.setGeometry(1272,7,40,40)
        self.ButtonSave.mouseReleaseEvent = lambda event: self.Save(self.LineSave.text())
        self.ButtonSave.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "saveIcon.png" ) ))
        self.ButtonSave.setStyleSheet("border:none; background:none;")
        self.ButtonSave.setScaledContents(True)

        self.ButtonLoad = QLabel(self.GUI)
        self.ButtonLoad.setGeometry(1317,7,40,40)
        self.ButtonLoad.mouseReleaseEvent = lambda event: self.Load(self.LineSave.text())
        self.ButtonLoad.setPixmap(QPixmap( os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "loadIcon.png" ) ))
        self.ButtonLoad.setStyleSheet("border:none; background:none;")
        self.ButtonLoad.setScaledContents(True)


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

        FilesList = os.listdir(  os.path.abspath( pathlib.Path() / "saves" )  )

        # FilesList = os.listdir("saves/")
        Saves = []
        for FileName in FilesList:
            if FileName.endswith(".sav"):
                SavePath = os.path.abspath( pathlib.Path() / "saves" / str(FileName) )
                # SavePath = "saves/" + str(FileName)
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
            Path = os.path.abspath( pathlib.Path() / "saves" )
            if not FilePath.startswith(Path):
                FilePath = os.path.abspath( pathlib.Path() / "saves" / FilePath )
            if not FilePath.endswith(".sav"):
                FilePath = f'''{FilePath}.sav'''

            Globals.CurrentSession["SoLNPCData"] = Globals.SoLNPCData
            Globals.CurrentSession["SoLPCData"] = Globals.SoLPCData
            Globals.CurrentSession["SoLTempData"] = Globals.SoLTempData
            Globals.CurrentSession["SoLOtherData"] = Globals.SoLOtherData
            Globals.CurrentSession["SoLEnviorementData"] = Globals.SoLEnviorementData
            Globals.CurrentSession["SoLNPCSchedules"] = Globals.SoLNPCSchedules
            Globals.CurrentSession["SoLFlavorDict"] = Globals.SoLFlavorDict
            with pathlib.Path.open(FilePath, 'w') as f:
                json.dump(Globals.CurrentSession, f)
            self.Refresh()

            Name = pathlib.Path(FilePath).name[:-4]
            self.LabelStatus.setText(f'''Successfully  saved {Name}''')

    def Load(self, FilePath):
        if FilePath == "":
            self.LabelStatus.setText("Please input a save name")
        else:
            try:
                Path = os.path.abspath( pathlib.Path() / "saves" )
                if not FilePath.startswith(Path):
                    FilePath = os.path.abspath( pathlib.Path() / "saves" / FilePath )
                if not FilePath.endswith(".sav"):
                    FilePath = f'''{FilePath}.sav'''

                with pathlib.Path.open(FilePath, 'rb') as f:
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

                Name = pathlib.Path(FilePath).name[:-4]
                self.LabelStatus.setText(f'''Successfully  loaded {Name}''')
            except:
                Name = pathlib.Path(FilePath).name[:-4]
                self.LabelStatus.setText(f'''Couldn't load {Name}''')

    def Remove(self, FilePath):
        Path = os.path.abspath( pathlib.Path() / "saves" )
        if not FilePath.startswith(Path):
            FilePath = os.path.abspath( pathlib.Path() / "saves" / FilePath )
        if not FilePath.endswith(".sav"):
            FilePath = f'''{FilePath}.sav'''

        pathlib.Path.unlink(FilePath)

        self.Refresh()

        Name = pathlib.Path(FilePath).name[:-4]
        self.LabelStatus.setText(f'''Successfully  removed {Name}''')


def Initialize(self, Reference):
    if "SaveUI" not in Globals.Layouts:
        Object = UiLayoutSaveMenu()
