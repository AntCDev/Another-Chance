import sys
import PyQt5
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QTextCursor, QFont, QFontDatabase
import json
import os
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
        QFontDatabase.addApplicationFont("images/OtherResources/Segoe UI.ttf")

        DisclaimerAgreed = 0

        Globals.Layouts["MainF"] = self
        self.setWindowTitle('Another Chance')
        self.setWindowIcon(QtGui.QIcon('logo.jpg'))
        self.setFixedSize(1600, 1024)
        self.LayoutsBox = QHBoxLayout()
        self.LayoutsWidget = QWidget(self)
        self.LayoutsWidget.setLayout(self.LayoutsBox);
        self.LayoutsWidget.setGeometry(0,0,1650,1024);

        self.LayoutsBox.setContentsMargins(0, 0, 0, 0)

        self.setStyleSheet('''
            .QWidget{
                background-color:rgb(35,35,35);
                }
                .QWidget#Transparent{
                    background:none;
                    border:none;
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
                    }
                .QScrollArea[Color = "Light"]{
                    background-color:rgb(35,35,35);
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

            QLineEdit{
                color:white;
                border:1px solid black;
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
            with open('CurrentSession.json', 'rb') as f:
                Globals.CurrentSession = json.load(f)
        except:
            Globals.CurrentSession = {}

        CurrentPath = os.path.dirname(os.path.realpath(__file__))

        # IMPORTS THE BASIC MOD AND FUNCTIONS
        Reference = __import__("Globals")
        Reference.Initialize(self, Reference)

        Reference = __import__("SoLFunctions")
        Reference.Initialize(self, Reference)

        ModsPath = CurrentPath + "\\SoL\\Mods"
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
        ModsPath = CurrentPath + "\\SoL\\Mods"
        if ModsPath not in sys.path:
            sys.path.insert(0, ModsPath)
        FileList = os.listdir("SoL/Mods")
        for File in FileList:
            try:
                if File.endswith(".py") and File != "BasicMod.py":
                    Reference = __import__(File[:-3])
                    Globals.References[File[:-3]] = Reference
                    Reference.Initialize(self, Reference)
            except Exception as e:
                Log(3, "ERROR INITIALIZE Mods", e, File)

        # IMPORTS THE LOCATIONS
        LocationsPath = CurrentPath + "\\SoL\\Locations"
        if LocationsPath not in sys.path:
            sys.path.insert(0, LocationsPath)
        FileList = os.listdir("SoL/Locations")
        for File in FileList:
            try:
                if File.endswith(".py"):
                    Reference = __import__(File[:-3])
                    Globals.References[File[:-3]] = Reference
                    Reference.Initialize(self, Reference)
            except Exception as e:
                Log(2, "ERROR INITIALIZE Locations", e, File)


        # IMPORTS THE COMMANDS
        CommandsPath = CurrentPath + "\\SoL\\Commands"
        if CommandsPath not in sys.path:
            sys.path.insert(0, CommandsPath)
        FileList = os.listdir("SoL/Commands")
        for File in FileList:
            try:
                if File.endswith(".py"):
                    Reference = __import__(File[:-3])
                    Globals.References[File[:-3]] = Reference
                    Reference.Initialize(self, Reference)
            except Exception as e:
                Log(2, "ERROR INITIALIZE Commands", e, File)

        # IMPORTS THE ABILITIES
        AbilitiesPath = CurrentPath + "\\SoL\\Abilities"
        if AbilitiesPath not in sys.path:
            sys.path.insert(0, AbilitiesPath)
        FileList = os.listdir("SoL/Abilities")
        for File in FileList:
            try:
                if File.endswith(".py"):
                    Reference = __import__(File[:-3])
                    Globals.References[File[:-3]] = Reference
                    Reference.Initialize(self, Reference)
            except Exception as e:
                Log(2, "ERROR INITIALIZE Abilities", e, File)

        # IMPORTS THE TRAITS
        TraitsPath = CurrentPath + "\\SoL\\Traits"
        if TraitsPath not in sys.path:
            sys.path.insert(0, TraitsPath)
        FileList = os.listdir("SoL/Traits")
        for File in FileList:
            try:
                if File.endswith(".py"):
                    Reference = __import__(File[:-3])
                    Globals.References[File[:-3]] = Reference
                    Reference.Initialize(self, Reference)
            except Exception as e:
                Log(2, "ERROR INITIALIZE Traits", e, File)

        # IMPORTS THE PERSONALITIES
        PersonalitiesPath = CurrentPath + "\\SoL\\Personalities"
        if PersonalitiesPath not in sys.path:
            sys.path.insert(0, PersonalitiesPath)
        FileList = os.listdir("SoL/Personalities")
        for File in FileList:
            try:
                if File.endswith(".py"):
                    Reference = __import__(File[:-3])
                    Globals.References[File[:-3]] = Reference
                    Reference.Initialize(self, Reference)
            except Exception as e:
                Log(2, "ERROR INITIALIZE Personalities", e, File)

        # IMPORTS THE NPC FUNCTIONS
        for NPCFullID in os.listdir("NPCData"):
            if os.path.isdir("NPCData/" + NPCFullID):
                try:
                    FilesList = os.listdir(f"NPCData/{NPCFullID}")
                    if f"{NPCFullID}Functions.py" in FilesList:
                        Path = f'''{CurrentPath}\\NPCData\\{NPCFullID}'''
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
                    LayoutOther.show()

            self.show()
        except Exception as e:
            Log(4, "ERROR SWITCHING LAYOUT", e, Layout)

    def gotoPreviousLayout(self):
        Globals.LayoutsData["Active"].GUI.hide()
        Globals.LayoutsData["Active"].comesFrom.GUI.show()
        Globals.LayoutsData["Active"] = Globals.LayoutsData["Active"].comesFrom
        Globals.LayoutsData["Active"].Refresh()

    def resizeEvent(self, event):
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
            Globals.Layouts["BattleMenu"].KeyHandling("Pressed", key, e)
        except:
            ""

    def keyReleaseEvent(self, e):
        try:
            key = e.nativeVirtualKey()      # To prevent Shift+1 to turn into ! instead of 1
            key = self.keyList(key)
            Globals.Layouts["BattleMenu"].KeyHandling("Released", key, e)
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
