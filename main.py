import json
import os
import pathlib
import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QFontDatabase
from PyQt5.QtWidgets import *

import Globals


def Log(*args):
    # 0 Non Issue
    # 1 Minor Issue
    # 2 Non Essential issue
    # 3 Essential Issue
    # 4 Possible Crashing Source
    # 5 Likely Crasing Source
    Level = args[0]
    Type = "Print"
    Tolerance = 0

    Separator = ''' || '''
    Message = f'''{Level}: '''
    for i in range(len(args)-1):
        Message += str(args[i+1]) + Separator
    else:
        Message = Message[:-len(Separator)]

    if Type == "Print" and Level >= Tolerance:
        print(Message)

class MainWindow(QMainWindow):
    resized = QtCore.pyqtSignal()
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        QFontDatabase.addApplicationFont("Resources/OtherResources/Segoe UI.ttf")

        DisclaimerAgreed = 0

        Globals.Layouts["MainF"] = self
        self.setWindowTitle('Another Chance')
        self.setWindowIcon(QtGui.QIcon('logo.jpg'))
        self.resize(1600, 1024)
        self.setMaximumWidth(1600)
        self.setMinimumWidth(1600)
        self.setMaximumHeight(1024)
        self.setMinimumHeight(700)

        self.LayoutsBox = QHBoxLayout()
        self.LayoutsWidget = QWidget(self)
        self.LayoutsWidget.setLayout(self.LayoutsBox)
        self.LayoutsWidget.setGeometry(0,0,1650,1024)

        self.LayoutsBox.setContentsMargins(0, 0, 0, 0)

        self.setStyleSheet('''
            .QWidget{
                background-color:rgb(35,35,35);
                }
                .QWidget#Transparent{
                    background:none;
                    border:none;
                    }
                .QWidget[Color = "Dark"]{
                    border:1px solid black;
                    background-color:rgb(23,23,23);
                    }

            .QGridLayout{
                border:none;
                background:none;
                }
            .QVBoxLayout{
                border:none;
                background:none;
                }
            .QGroupBox{
                border:none;
                background:none;
                }

            .QScrollArea{
                border:none;
                background-color:rgba(23,23,23,0)
                }
                .QScrollArea[Color = "Dark"]{
                    background-color:rgb(23,23,23);
                    border: 1px solid black;
                    }
                .QScrollArea[Color = "Light"]{
                    background-color:rgb(35,35,35);
                    border: 1px solid black;
                    }

            QPushButton{
                color:white;
                font-size: 14pt;
                font-family: Segoe UI;
                background-color:rgb(35,35,35);
                }
                QPushButton:hover{
                    color:yellow;
                    }
                QPushButton[Color = "Dark"]{
                    background-color:rgb(23,23,23);
                    }
                QPushButton[Color = "Light"]{
                    background-color:rgb(35,35,35);
                    }
                QPushButton[Enabled = "0"]{
                    color:grey;
                    }
                QPushButton[Enabled = "1"]{
                    }

            QLabel{
                color:white;
                border:1px solid black;
                font-family: Segoe UI;
                font-size: 12pt;
                }

                QLabel:hover{
                color:yellow;
                }

                QLabel#MainTitle{
                    font-size: 28pt;
                    }
                QLabel#Title{
                    font-size: 16pt;
                    }
                QLabel#SubTitle{
                    font-size: 14pt;
                    }
                QLabel#SmallText{
                    font-size: 10pt;
                    }

                QLabel[Selected = "1"]{
                    color:yellow;
                    }
                QLabel[Selected = "-1"]{
                    color:grey;
                    }
                QLabel[Color = "Dark"]{
                    background-color:rgb(23,23,23);
                    }
                QLabel[Color = "Light"]{
                    background-color:rgb(35,35,35);
                    }
                QLabel[Color = "None"]{
                    background:none;
                    border:none;
                    }
                QLabel[Border = "None"]{
                    border:none;
                    }
                QLabel[Border = "Selected"]{
                    border: 1px solid yellow;
                    }

            QLineEdit{
                font-size: 14pt;
                font-family: Segoe UI;
                color:white;
                border:1px solid black;
                background-color:rgb(35,35,35);
                }
                QLineEdit[Color = "Dark"]{
                    background-color:rgb(23,23,23);
                    }
                QLineEdit[Color = "Light"]{
                    background-color:rgb(35,35,35);
                    }

            QTextEdit{
                color:white;
                border:1px solid black;
                background-color:rgb(35,35,35);
                }

            QComboBox{
                background-color:rgb(23,23,23);
                color:white;
                }
                QComboBox:hover{
                    color:yellow;
                    }
        		QComboBox QAbstractItemView {
                    border: 1px solid grey;
                    color: white;
                    selection-color: yellow;
            		}

            QRadioButton{
                color:white;
                }
                QRadioButton:hover{
                    color:yellow;
                    }

            QToolTip{
                background-color: rgb(23,23,23);
                color: white;
                border: 1px solid black;
                }
            ''')
        def SD(Object, Type):
            if Type == "Font":
                return "Segoe UI"
            if Type == "FontSize":
                if isinstance(Object, QPushButton):
                    return 14
                else:
                    ObjectName = Object.objectName()
                    if ObjectName == "MainTitle": return 20
                    elif ObjectName == "Title": return 16
                    elif ObjectName == "SubTitle": return 14
                    elif ObjectName == "SmallText": return 10
                    else: return 12

        self.StyleData = SD

        self.Log = Log
        self.LayoutsBox.LayoutsList = []

        try:
            with pathlib.Path.open('CurrentSession.json', 'rb') as f:
                Globals.CurrentSession = json.load(f)
        except:
            Globals.CurrentSession = {}

        # CurrentPath = os.path.dirname(os.path.realpath(__file__))
        # CurrentPath = os.path.abspath( pathlib.Path() / "Resources" / "SoLResources" / "FilledHeart" )
        CurrentPath = pathlib.Path()

        # IMPORTS THE BASIC MOD AND FUNCTIONS
        Reference = __import__("Globals")
        Reference.Initialize(self, Reference)

        Reference = __import__("SoLFunctions")
        Reference.Initialize(self, Reference)

        ModsPath = os.path.abspath( pathlib.Path() / "SoL" / "Mods" )
        # ModsPath = CurrentPath + "\\SoL\\Mods"
        if ModsPath not in sys.path:
            sys.path.insert(0, ModsPath)
        try:
            Reference = __import__("BasicMod")
            Globals.References["BasicMod"] = Reference
            Reference.Initialize(self, Reference)
        except Exception as e:
            Log(5, "ERROR INITIALIZE BASIC MOD", e)



        # IMPORTS THE BASIC FILES
        FileList = os.listdir()
        for File in FileList:
            if File.endswith(".py") and File != "main.py":
                try:
                    Reference = __import__(File[:-3])
                    Globals.References[File[:-3]] = Reference
                    Reference.Initialize(self, Reference)
                except Exception as e:
                    Log(4, "ERROR INITIALIZE FILES", e, File)

        # IMPORTS THE MODS
        ModsPath = os.path.abspath( pathlib.Path() / "SoL" / "Mods" )
        # ModsPath = CurrentPath + "\\SoL\\Mods"
        if ModsPath not in sys.path:
            sys.path.insert(0, ModsPath)
        # FileList = os.listdir("SoL/Mods")
        FileList = os.listdir(os.path.abspath( pathlib.Path() / "SoL" / "Mods" ))
        for File in FileList:
            try:
                if File.endswith(".py") and File != "BasicMod.py":
                    Reference = __import__(File[:-3])
                    Globals.References[File[:-3]] = Reference
                    Reference.Initialize(self, Reference)
            except Exception as e:
                Log(3, "ERROR INITIALIZE Mods", e, File)

        # IMPORTS THE LOCATIONS
        LocationsPath = os.path.abspath( pathlib.Path() / "SoL" / "Locations" )
        # LocationsPath = CurrentPath + "\\SoL\\Locations"
        if LocationsPath not in sys.path:
            sys.path.insert(0, LocationsPath)
        # FileList = os.listdir("SoL/Locations")
        FileList = os.listdir(os.path.abspath( pathlib.Path() / "SoL" / "Locations" ))
        for File in FileList:
            try:
                if File.endswith(".py"):
                    Reference = __import__(File[:-3])
                    Globals.References[File[:-3]] = Reference
                    Reference.Initialize(self, Reference)
            except Exception as e:
                Log(2, "ERROR INITIALIZE Locations", e, File)


        # IMPORTS THE COMMANDS
        CommandsPath = os.path.abspath( pathlib.Path() / "SoL" / "Commands" )
        # CommandsPath = CurrentPath + "\\SoL\\Commands"
        if CommandsPath not in sys.path:
            sys.path.insert(0, CommandsPath)
        # FileList = os.listdir("SoL/Commands")
        FileList = os.listdir(os.path.abspath( pathlib.Path() / "SoL" / "Commands" ))
        for File in FileList:
            try:
                if File.endswith(".py"):
                    Reference = __import__(File[:-3])
                    Globals.References[File[:-3]] = Reference
                    Reference.Initialize(self, Reference)
            except Exception as e:
                Log(2, "ERROR INITIALIZE Commands", e, File)

        # IMPORTS THE ABILITIES
        AbilitiesPath = os.path.abspath( pathlib.Path() / "SoL" / "Abilities" )
        # AbilitiesPath = CurrentPath + "\\SoL\\Abilities"
        if AbilitiesPath not in sys.path:
            sys.path.insert(0, AbilitiesPath)
        FileList = os.listdir(os.path.abspath( pathlib.Path() / "SoL" / "Abilities" ))
        for File in FileList:
            try:
                if File.endswith(".py"):
                    Reference = __import__(File[:-3])
                    Globals.References[File[:-3]] = Reference
                    Reference.Initialize(self, Reference)
            except Exception as e:
                Log(2, "ERROR INITIALIZE Abilities", e, File)

        # IMPORTS THE TRAITS
        TraitsPath = os.path.abspath( pathlib.Path() / "SoL" / "Traits" )
        # TraitsPath = CurrentPath + "\\SoL\\Traits"
        if TraitsPath not in sys.path:
            sys.path.insert(0, TraitsPath)
        # FileList = os.listdir("SoL/Traits")
        FileList = os.listdir(os.path.abspath( pathlib.Path() / "SoL" / "Traits" ))
        for File in FileList:
            try:
                if File.endswith(".py"):
                    Reference = __import__(File[:-3])
                    Globals.References[File[:-3]] = Reference
                    Reference.Initialize(self, Reference)
            except Exception as e:
                Log(2, "ERROR INITIALIZE Traits", e, File)

        # IMPORTS THE PERSONALITIES
        PersonalitiesPath = os.path.abspath( pathlib.Path() / "SoL" / "Personalities" )
        # PersonalitiesPath = CurrentPath + "\\SoL\\Personalities"
        if PersonalitiesPath not in sys.path:
            sys.path.insert(0, PersonalitiesPath)
        # FileList = os.listdir("SoL/Personalities")
        FileList = os.listdir(os.path.abspath( pathlib.Path() / "SoL" / "Personalities" ))
        for File in FileList:
            try:
                if File.endswith(".py"):
                    Reference = __import__(File[:-3])
                    Globals.References[File[:-3]] = Reference
                    Reference.Initialize(self, Reference)
            except Exception as e:
                Log(2, "ERROR INITIALIZE Personalities", e, File)

        # IMPORTS THE CLOTHES
        ClothesPath = os.path.abspath( pathlib.Path() / "SoL" / "Clothes" )
        # ClothesPath = CurrentPath + "\\SoL\\Clothes"
        if ClothesPath not in sys.path:
            sys.path.insert(0, ClothesPath)
        # FileList = os.listdir("SoL/Clothes")
        FileList = os.listdir(os.path.abspath( pathlib.Path() / "SoL" / "Clothes" ))
        for File in FileList:
            try:
                if File.endswith(".py"):
                    Reference = __import__(File[:-3])
                    Globals.References[File[:-3]] = Reference
                    Reference.Initialize(self, Reference)
            except Exception as e:
                Log(2, "ERROR INITIALIZE Clothes", e, File)


        # IMPORTS THE NPC FUNCTIONS
        for NPCFullID in os.listdir("NPCData"):
            # if os.path.isdir("NPCData/" + NPCFullID):
            if pathlib.Path.is_dir( pathlib.Path() / "NPCData" / NPCFullID ):
                try:
                    # FilesList = os.listdir(f"NPCData/{NPCFullID}")
                    FilesList = os.listdir(os.path.abspath( pathlib.Path() / "NPCData" / NPCFullID ))
                    if f"{NPCFullID}Functions.py" in FilesList:
                        # Path = f'''{CurrentPath}\\NPCData\\{NPCFullID}'''
                        Path = os.path.abspath( pathlib.Path() / "NPCData" / NPCFullID )
                        if Path not in sys.path:
                            sys.path.insert(0, Path)
                        File = f"{NPCFullID}Functions.py"
                        Reference = __import__(File[:-3])
                        Globals.References[File[:-3]] = Reference
                        Reference.Initialize(self, Reference)
                except Exception as e:
                    Log(2, "ERROR INITIALIZE NPCFunctions", e, File)

        if DisclaimerAgreed == 0:
            self.gotoLayout("DisclaimerUI")
        else:
            self.gotoLayout("MainMenuUI")
        self.show()

    def gotoLayout(self, Layout):
        try:
            Object = Globals.Layouts[Layout]

            Object.comesFrom = Globals.LayoutsData["Active"]
            Globals.LayoutsData["Previous"] = Globals.LayoutsData["Active"]
            Globals.LayoutsData["Active"] = Object

            try:
                if Object.GUI not in self.LayoutsBox.LayoutsList:
                    self.LayoutsBox.LayoutsList.append(Object.GUI)
                    self.LayoutsBox.addWidget(Object.GUI)
            except:
                Object.UI()
                if Object.GUI not in self.LayoutsBox.LayoutsList:
                    self.LayoutsBox.LayoutsList.append(Object.GUI)
                    self.LayoutsBox.addWidget(Object.GUI)

            for LayoutOther in self.LayoutsBox.LayoutsList:
                LayoutOther.hide()
                if LayoutOther == Object.GUI:
                    Object.Refresh()
                    try:
                        Globals.LayoutsData["Active"].ResizeEvent()
                    except:
                        ""
                    LayoutOther.show()

            self.show()
        except Exception as e:
            Log(4, "ERROR SWITCHING LAYOUT", e, Layout)

    def gotoPreviousLayout(self):
        Globals.LayoutsData["Active"].GUI.hide()
        Globals.LayoutsData["Active"].comesFrom.GUI.show()
        Globals.LayoutsData["Active"] = Globals.LayoutsData["Active"].comesFrom
        Globals.LayoutsData["Active"].Refresh()
        try:
            Globals.LayoutsData["Active"].ResizeEvent()
        except:
            ""

    def resizeEvent(self, event):
        try:
            Globals.LayoutsData["Active"].ResizeEvent()
        except:
            ""

        self.resized.emit()

    def someFunction(self):
        try:
            Globals.Layouts["BattleMenu"].ressEvent()
        except:
            ""

    # overriding key press event
    def keyList(self, key):
        if key == 17:       # Control
            key = "Control"
        elif key == 16:     # Shift
            key = "Shift"
        elif key == 13:     # Enter
            key = "Enter"
        elif key == 18:     # Alt
            key = "Alt"
        if key == 27:       # Esc
            key = "Esc"
        elif key == 192:    # Tilde, key to the left of 1
            key = "Tilde"
        elif key == 20:     # Mayus
            key = "Mayus"
        elif key == 81:     # Q
            key = "Q"
        elif key == 87:     # W
            key = "W"
        elif key == 69:     # E
            key = "E"
        elif key == 65:     # A
            key = "A"
        elif key == 83:     # S
            key = "S"
        elif key == 68:     # D
            key = "D"
        elif key == 90:     # Z
            key = "Z"
        elif key == 88:     # X
            key = "X"
        elif key == 67:     # C
            key = "C"
        elif key == 32:     # Space
            key = "Space"
        elif key == 48:     # 0
            key = "0"
        elif key == 49:     # 1
            key = "1"
        elif key == 50:     # 2
            key = "2"
        elif key == 51:     # 3
            key = "3"
        elif key == 52:     # 4
            key = "4"
        elif key == 53:     # 5
            key = "5"
        elif key == 54:     # 6
            key = "6"
        elif key == 55:     # 7
            key = "7"
        elif key == 56:     # 8
            key = "8"
        elif key == 57:     # 9
            key = "9"
        elif key == 84:     # T
            key = "T"
        return key

    def keyPressEvent(self, e):
        try:
            key = e.nativeVirtualKey()      # To prevent Shift+1 to turn into ! instead of 1
            key = self.keyList(key)
            Globals.Keys[key] = e
            # Globals.Layouts[]
            # Globals.Layouts["BattleMenu"].KeyHandling("Pressed", key, e)
        except:
            ""
        try:
            if "Control" in Globals.Keys and "Shift" in Globals.Keys and "1" in Globals.Keys:
                try:
                    self.gotoPreviousLayout()
                except:
                    ""
            if "Control" in Globals.Keys and "Shift" in Globals.Keys and "2" in Globals.Keys:
                try:
                    if Globals.LayoutsData["Active"] != Globals.Layouts["MainMenuUI"]:
                        self.gotoLayout("MainMenuUI")
                except Exception as e:
                    ""
        except Exception as e:
            ""

    def keyReleaseEvent(self, e):
        try:
            key = e.nativeVirtualKey()      # To prevent Shift+1 to turn into ! instead of 1
            key = self.keyList(key)
            # Globals.Layouts["BattleMenu"].KeyHandling("Released", key, e)
            Globals.Keys.pop(key)
        except:
            ""


    def closeEvent(self, event):
        ""
        # report_session()

# pid = os.getpid()
# print(pid)
if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow()
    sys.exit(app.exec_())
