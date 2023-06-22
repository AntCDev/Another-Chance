import json
import os
import pathlib
import sys

from PyQt5 import QtCore
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

import Globals

Log = Globals.Layouts["MainF"].Log
class UiLayoutMakerMenu(QWidget):
    def __init__(self):
        super().__init__()
        Globals.Layouts["MakerUI"] = self
        Globals.LayoutsData["MakerUI"] = {"Source":"makerMenuUI", "Initialized":0}
        self.TraitWidgetsDict = {}

        # CurrentPath = os.path.dirname(os.path.realpath(__file__))
        # CommandsPath = CurrentPath + "\\SoL\\Traits"
        TraitsPath = os.path.abspath( pathlib.Path() / "SoL" / "Traits" )
        if TraitsPath not in sys.path:
            sys.path.insert(0, TraitsPath)
        # FileList = os.listdir("SoL/Traits")
        FileList = os.listdir( os.path.abspath( pathlib.Path() / "SoL" / "Traits" ) )
        for FileName in FileList:
            try:
                if FileName.endswith(".py"):
                    Reference = __import__(FileName[:-3])
                    Globals.References[FileName[:-3]] = Reference
                    Reference.Initialize(self, Reference)
            except Exception as e:
                Log(1, "ERROR MAKER MENU INITIALIZE", e, FileName)


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
        background-color:rgb(35,35,35);
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

        self.MainLayout = QVBoxLayout()
        self.MainLayout.setContentsMargins(0, 5, 0, 5)

        self.MainBox = QGroupBox()
        self.MainBox.setLayout(self.MainLayout)
        self.MainBox.setMinimumWidth(1590)
        # self.MainBox.setMinimumHeight(1521)

        self.MainScroll = QScrollArea(self.GUI)
        self.MainScroll.setGeometry(5,5,1592,950)
        self.MainScroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.MainScroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.MainScroll.setWidget(self.MainBox)

        ### BODY CHARACTERISTICS
        self.BodyWidget = QWidget(self.GUI, objectName = "MainWidget")
        self.BodyWidget.setStyleSheet('''
        .QWidget#MainWidget{
        background-color:rgb(23, 23, 23);
        border:1px solid black;
        }
        .QWidget{
        background-color:rgb(23, 23, 23);
        border:none;
        }
        ''')
        self.BodyWidget.setMinimumWidth(1580)
        self.BodyWidget.Height = 200
        self.MainLayout.addWidget(self.BodyWidget)
        self.setBody()


        ### TRAIT CHARACTERISTICS
        self.TraitsWidget = QWidget(self.GUI)
        self.TraitsWidget.setStyleSheet('''
        .QWidget{
        background-color:rgb(23, 23, 23);
        border:1px solid black;
        }
        QGridLayout{
        border:1px solid red;
        }
        ''')
        self.TraitsWidget.setMinimumWidth(1580)
        self.TraitsWidget.Height = 500
        self.MainLayout.addWidget(self.TraitsWidget)
        self.setTraits()


        ### TRAIT DESCRPTIOPNS
        self.DescriptionsWidget = QWidget(self.GUI, objectName = "MainWidget")
        self.DescriptionsWidget.setStyleSheet('''
        .QWidget#MainWidget{
        background-color:rgb(23, 23, 23);
        border:1px solid black;
        }
        .QWidget{
        background-color:rgb(23, 23, 23);
        }
        ''')
        self.DescriptionsWidget.setMinimumWidth(1580)
        self.DescriptionsWidget.Height = 400
        self.MainLayout.addWidget(self.DescriptionsWidget)
        self.setDescriptions()


        self.BodyWidget.setMinimumHeight(self.BodyWidget.Height)
        self.BodyWidget.setMaximumHeight(self.BodyWidget.Height)
        self.TraitsWidget.setMinimumHeight(self.TraitsWidget.Height)
        self.TraitsWidget.setMaximumHeight(self.TraitsWidget.Height)
        self.DescriptionsWidget.setMinimumHeight(self.DescriptionsWidget.Height)
        self.DescriptionsWidget.setMaximumHeight(self.DescriptionsWidget.Height)

        Height = self.BodyWidget.height() + self.TraitsWidget.height() + self.DescriptionsWidget.height() + 45
        self.MainBox.setMinimumHeight(Height)
        self.MainBox.setMaximumHeight(Height)



        self.ControlWidget = QWidget(self.GUI)
        self.ControlWidget.setGeometry(5,964,1592,55)

        self.ControlWidget.setStyleSheet('''
        .QWidget{
        background-color:rgb(23,23,23);
        }
        ''')

        self.ButtonMenu = QPushButton("Back", self.ControlWidget, clicked = lambda: MainWindow.gotoPreviousLayout())
        self.ButtonMenu.setGeometry(10,6,200,45)

        self.ButtonSave = QPushButton("Save", self.ControlWidget, clicked = lambda: self.Save())
        self.ButtonSave.setGeometry(220,6,200,45)

        self.ButtonLoad = QPushButton("Load", self.ControlWidget, clicked = lambda: self.Load())
        self.ButtonLoad.setGeometry(1070,6,200,45)
        self.LoadBox = QComboBox(self.ControlWidget)
        self.LoadBox.setGeometry(1280,6,300,45)
        self.LoadBox.addItem("---")
        self.LoadBox.NPCData = {}
        self.CheckLoad()

        self.LabelStatus = QLabel(self.ControlWidget, objectName = "MainTitle")
        self.LabelStatus.setStyleSheet('''
        QLabel{
        background-color:rgb(23,23,23);
        color:white;
        font-size: 16pt;
        font-family: Segoe UI;
        }
        ''')
        self.LabelStatus.setGeometry(590,6,400,45)
        self.LabelStatus.setAlignment(QtCore.Qt.AlignCenter)


    def setBody(self):
        try:
            self.BodyLabel = QLabel("Body Characteristics", self.BodyWidget, objectName = "MainTitle")
            self.BodyLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.BodyLabel.setGeometry(10,5,1570,50)

            GeneralWidget = QWidget(self.BodyWidget)

            GeneralLabel = QLabel("General", GeneralWidget, objectName = "SubTitle")
            GeneralLabel.setGeometry(0,0,530,45)
            GeneralLabel.setAlignment(QtCore.Qt.AlignCenter)

            FullNameWidget = QWidget(GeneralWidget)
            self.FullNameLabel = QLabel("Full Name", FullNameWidget)
            self.FullNameLabel.setGeometry(0, 0, 348, 35)
            self.FullNameLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.FullNameLine = QLineEdit(FullNameWidget)
            self.FullNameLine.setGeometry(0, 40, 348, 35)
            FullNameWidget.setGeometry(0,55,350,82)

            MainNameWidget = QWidget(GeneralWidget)
            self.MainNameLabel = QLabel("Main Name", MainNameWidget)
            self.MainNameLabel.setGeometry(0, 0, 175, 35)
            self.MainNameLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.MainNameLine = QLineEdit(MainNameWidget)
            self.MainNameLine.setGeometry(0, 40, 175, 35)
            MainNameWidget.setGeometry(355,55,177,82)

            SkinColorWidget = QWidget(GeneralWidget)
            self.SkinColorLabel = QLabel("Skin Color", SkinColorWidget)
            self.SkinColorLabel.setGeometry(0, 0, 173, 35)
            self.SkinColorLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.SkinColorLine = QLineEdit(SkinColorWidget)
            self.SkinColorLine.setGeometry(0, 40, 173, 35)
            SkinColorWidget.setGeometry(0,140,175,82)

            RaceWidget = QWidget(GeneralWidget)
            self.RaceLabel = QLabel("Race", RaceWidget)
            self.RaceLabel.setGeometry(0, 0, 173, 35)
            self.RaceLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.RaceLine = QLineEdit(RaceWidget)
            self.RaceLine.setGeometry(0, 40, 173, 35)
            RaceWidget.setGeometry(178,140,175,82)

            AgeWidget = QWidget(GeneralWidget)
            self.AgeLabel = QLabel("Physical Age", AgeWidget)
            self.AgeLabel.setGeometry(0, 0, 174, 35)
            self.AgeLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.AgeBox = QComboBox(AgeWidget)
            self.AgeBox.setGeometry(0, 40, 174, 35)
            self.AgeBox.addItem("0")
            self.AgeBox.addItem("1")
            self.AgeBox.addItem("2")
            self.AgeBox.addItem("3")
            self.AgeBox.addItem("4")
            self.AgeBox.addItem("5")
            self.AgeBox.addItem("6")
            self.AgeBox.addItem("7+")


            self.AgeBox.setCurrentIndex(2)
            AgeWidget.setGeometry(356,140,176,82)



            EnergyWidget = QWidget(GeneralWidget)
            self.EnergyLabel = QLabel("Energy", EnergyWidget)
            self.EnergyLabel.setGeometry(0, 0, 173, 35)
            self.EnergyLabel.setAlignment(QtCore.Qt.AlignCenter)

            def LineChange(self):
                try:
                    Value = int(self.EnergyLine.text())
                    if Value < 500:
                        Value = 500
                    elif Value > 2500:
                        Value = 2500

                    self.EnergySlider.UserInput = 1
                    self.EnergySlider.setValue( Value )
                    self.EnergySlider.UserInput = 0
                except Exception as e:
                    ""
            def LineFinished(self):
                try:
                    Value = int(self.EnergyLine.text())
                    if Value < 500:
                        Value = 500
                    elif Value > 2500:
                        Value = 2500
                    if self.EnergySlider.value() == Value:
                        self.EnergyLine.setText(str( self.EnergySlider.value() ))
                    else:
                        self.EnergySlider.UserInput = 0
                        self.EnergySlider.setValue( Value )
                except Exception as e:
                    ""
            self.EnergyLine = QLineEdit("1500", EnergyWidget)
            self.EnergyLine.setGeometry(0, 40, 45, 35)
            self.EnergyLine.setAlignment(QtCore.Qt.AlignCenter)
            self.EnergyLine.editingFinished.connect(lambda: LineFinished(self))
            self.EnergyLine.textEdited.connect(lambda: LineChange(self))

            def SliderChange(self):
                try:
                    if self.EnergySlider.UserInput == 0:
                        self.EnergyLine.setText(str( self.EnergySlider.value() ))
                except Excpetion as e:
                    ""
            self.EnergySlider = QSlider(EnergyWidget)
            self.EnergySlider.UserInput = 0
            self.EnergySlider.setOrientation(QtCore.Qt.Horizontal)
            self.EnergySlider.setGeometry(50, 40, 123, 35)
            self.EnergySlider.setMinimum(500)
            self.EnergySlider.setMaximum(2500)
            self.EnergySlider.setValue(1500)
            self.EnergySlider.setTickInterval(10)
            self.EnergySlider.valueChanged.connect(lambda: SliderChange(self))
            EnergyWidget.setGeometry(0,225,175,82)


            PersonalityWidget = QWidget(GeneralWidget)
            self.PersonalityLabel = QLabel("Personality", PersonalityWidget)
            self.PersonalityLabel.setGeometry(0, 0, 174, 35)
            self.PersonalityLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.PersonalityBox = QComboBox(PersonalityWidget)
            self.PersonalityBox.setGeometry(0, 40, 174, 35)
            self.PersonalityBox.Personalities = []
            for PersonalityID in Globals.SoLPersonalities:
                Text = Globals.SoLPersonalities[PersonalityID]["Reference"].GetName(self, PersonalityID)
                self.PersonalityBox.Personalities.append(PersonalityID)
                self.PersonalityBox.addItem(Text)
            PersonalityWidget.setGeometry(178,225,176,82)

            IDWidget = QWidget(GeneralWidget)
            self.IDLabel = QLabel("ID", IDWidget)
            self.IDLabel.setGeometry(0, 0, 55, 35)
            self.IDLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.IDLine = QLineEdit(IDWidget)
            self.IDLine.setGeometry(0, 40, 55, 35)
            IDWidget.setGeometry(475,225,57,82)

            GeneralWidget.setGeometry(10,65,530,305)




            HeadWidget = QWidget(self.BodyWidget)

            HeadLabel = QLabel("Head", HeadWidget, objectName = "SubTitle")
            HeadLabel.setGeometry(0,0,405,45)
            HeadLabel.setAlignment(QtCore.Qt.AlignCenter)

            HairColorWidget = QWidget(HeadWidget)
            self.HairColorLabel = QLabel("Hair Color", HairColorWidget)
            self.HairColorLabel.setGeometry(0, 0, 200, 35)
            self.HairColorLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.HairColorLine = QLineEdit(HairColorWidget)
            self.HairColorLine.setGeometry(0, 40, 200, 35)
            HairColorWidget.setGeometry(0,55,202,82)

            FaceWidget = QWidget(HeadWidget)
            self.FaceLabel = QLabel("Face Type", FaceWidget)
            self.FaceLabel.setGeometry(0, 0, 200, 35)
            self.FaceLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.FaceBox = QComboBox(FaceWidget)
            self.FaceBox.setGeometry(0, 40, 200, 35)
            self.FaceBox.addItem("Very Masculine")
            self.FaceBox.addItem("Masculine")
            self.FaceBox.addItem("Boyish")
            self.FaceBox.addItem("Androgynous")
            self.FaceBox.addItem("Girlish")
            self.FaceBox.addItem("Femenine")
            self.FaceBox.addItem("Very Femenine")
            FaceWidget.setGeometry(0,140,202,82)

            EyesWidget = QWidget(HeadWidget)
            self.EyesLabel = QLabel("Eye Color", EyesWidget)
            self.EyesLabel.setGeometry(0, 0, 200, 35)
            self.EyesLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.EyesLine = QLineEdit(EyesWidget)
            self.EyesLine.setGeometry(0, 40, 200, 35)
            EyesWidget.setGeometry(205,55,202,82)

            LipWidget = QWidget(HeadWidget)
            self.LipLabel = QLabel("Lips Size", LipWidget)
            self.LipLabel.setGeometry(0, 0, 200, 35)
            self.LipLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.LipBox = QComboBox(LipWidget)
            self.LipBox.setGeometry(0, 40, 200, 35)
            self.LipBox.addItem("Thin")
            self.LipBox.addItem("Small")
            self.LipBox.addItem("Average")
            self.LipBox.addItem("Plump")
            self.LipBox.addItem("Big")
            LipWidget.setGeometry(205,140,202,82)

            HeadWidget.setGeometry(553,65,410,220)





            BodyWidget = QWidget(self.BodyWidget)

            BodyLabel = QLabel("Body", BodyWidget, objectName = "SubTitle")
            BodyLabel.setGeometry(0,0,610,45)
            BodyLabel.setAlignment(QtCore.Qt.AlignCenter)

            BodySizeWidget = QWidget(BodyWidget)
            self.BodySizeLabel = QLabel("Height", BodySizeWidget)
            self.BodySizeLabel.setGeometry(0, 0, 200, 35)
            self.BodySizeLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.BodySizeBox = QComboBox(BodySizeWidget)
            self.BodySizeBox.setGeometry(0, 40, 200, 35)
            self.BodySizeBox.addItem("Pixie Size")
            self.BodySizeBox.addItem("Very Tiny")
            self.BodySizeBox.addItem("Tiny")
            self.BodySizeBox.addItem("Small")
            self.BodySizeBox.addItem("Average")
            self.BodySizeBox.addItem("Tall")
            self.BodySizeBox.addItem("Very Tall")
            self.BodySizeBox.addItem("Towering")
            BodySizeWidget.setGeometry(0,55,202,82)

            BodyTypeWidget = QWidget(BodyWidget)
            self.BodyTypeLabel = QLabel("Complexion", BodyTypeWidget)
            self.BodyTypeLabel.setGeometry(0, 0, 200, 35)
            self.BodyTypeLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.BodyTypeBox = QComboBox(BodyTypeWidget)
            self.BodyTypeBox.setGeometry(0, 40, 200, 35)
            self.BodyTypeBox.addItem("Scrawny")
            self.BodyTypeBox.addItem("Thin")
            self.BodyTypeBox.addItem("Slim")
            self.BodyTypeBox.addItem("Average")
            self.BodyTypeBox.addItem("Plump")
            self.BodyTypeBox.addItem("Fat")
            self.BodyTypeBox.addItem("Very Fat")
            self.BodyTypeBox.addItem("Toned")
            self.BodyTypeBox.addItem("Strong")
            self.BodyTypeBox.addItem("Buff")
            BodyTypeWidget.setGeometry(205,55,202,82)

            def setTempPronouns(self, Type):
                if Type == "Female":
                    self.PSubLine.setPlaceholderText("She")
                    self.PObjLine.setPlaceholderText("Her")
                    self.PPosLine.setPlaceholderText("Her")
                    self.PIPosLine.setPlaceholderText("Hers")
                elif Type == "Male":
                    self.PSubLine.setPlaceholderText("He")
                    self.PObjLine.setPlaceholderText("Him")
                    self.PPosLine.setPlaceholderText("His")
                    self.PIPosLine.setPlaceholderText("His")
            PStructureWidget = QWidget(BodyWidget)
            self.PSrtuctureLabel = QLabel("Sex", PStructureWidget)
            self.PSrtuctureLabel.setGeometry(0, 0, 200, 35)
            self.PSrtuctureLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.PStructureGroup = QButtonGroup(PStructureWidget)
            self.PStructureGroup.setExclusive(True)
            self.PStructureButtonM = QRadioButton("Male", PStructureWidget, clicked = lambda: setTempPronouns(self, "Male"))
            self.PStructureButtonM.setGeometry(0,40,90,35)
            self.PStructureButtonM.setFont(QFont('Segoe UI', 8))
            self.PStructureButtonF = QRadioButton("Female", PStructureWidget, clicked = lambda: setTempPronouns(self, "Female"))
            self.PStructureButtonF.setGeometry(95,40,95,35)
            self.PStructureButtonF.setFont(QFont('Segoe UI', 8))
            PStructureWidget.setGeometry(410,55,202,82)


            HipWidget = QWidget(BodyWidget)
            self.HipLabel = QLabel("Hip Size", HipWidget)
            self.HipLabel.setGeometry(0, 0, 200, 35)
            self.HipLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.HipBox = QComboBox(HipWidget)
            self.HipBox.setGeometry(0, 40, 200, 35)
            self.HipBox.addItem("Manly")
            self.HipBox.addItem("Straight")
            self.HipBox.addItem("Slim")
            self.HipBox.addItem("Average")
            self.HipBox.addItem("Wide")
            self.HipBox.addItem("Childbearing")
            HipWidget.setGeometry(0,140,202,82)

            AssWidget = QWidget(BodyWidget)
            self.AssLabel = QLabel("Ass Size", AssWidget)
            self.AssLabel.setGeometry(0, 0, 200, 35)
            self.AssLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.AssBox = QComboBox(AssWidget)
            self.AssBox.setGeometry(0, 40, 200, 35)
            self.AssBox.addItem("Manish")
            self.AssBox.addItem("Thin")
            self.AssBox.addItem("Slim")
            self.AssBox.addItem("Average")
            self.AssBox.addItem("Plump")
            self.AssBox.addItem("Big")
            self.AssBox.addItem("Huge")
            AssWidget.setGeometry(205,140,202,82)

            PronounsWidget = QWidget(BodyWidget)
            self.PronounsLabel = QLabel("Pronouns", PronounsWidget)
            self.PronounsLabel.setGeometry(0, 0, 200, 35)
            self.PronounsLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.PSubLine = QLineEdit(PronounsWidget)
            self.PSubLine.setGeometry(5, 40, 40, 35)
            self.PSubLine.setPlaceholderText("She")
            self.PObjLine = QLineEdit(PronounsWidget)
            self.PObjLine.setGeometry(50, 40, 40, 35)
            self.PObjLine.setPlaceholderText("Her")
            self.PPosLine = QLineEdit(PronounsWidget)
            self.PPosLine.setGeometry(95, 40, 40, 35)
            self.PPosLine.setPlaceholderText("Her")
            self.PIPosLine = QLineEdit(PronounsWidget)
            self.PIPosLine.setGeometry(140, 40, 55, 35)
            self.PIPosLine.setPlaceholderText("Hers")
            PronounsWidget.setGeometry(410,140,202,82)

            ChestWidget = QWidget(BodyWidget)
            self.ChestLabel = QLabel("Chest Size", ChestWidget)
            self.ChestLabel.setGeometry(0, 0, 200, 35)
            self.ChestLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.ChestBox = QComboBox(ChestWidget)
            self.ChestBox.setGeometry(0, 40, 200, 35)
            self.ChestBox.addItem("Muscular")
            self.ChestBox.addItem("Flat")
            self.ChestBox.addItem("Bulging")
            self.ChestBox.addItem("Small")
            self.ChestBox.addItem("Average")
            self.ChestBox.addItem("Big")
            self.ChestBox.addItem("Huge")
            self.ChestBox.addItem("Huger")
            ChestWidget.setGeometry(0,225,202,82)

            VWidget = QWidget(BodyWidget)
            self.VLabel = QLabel("Vaginal Tightness", VWidget)
            self.VLabel.setGeometry(0, 0, 200, 35)
            self.VLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.VBox = QComboBox(VWidget)
            self.VBox.setGeometry(0, 40, 200, 35)
            self.VBox.addItem("Doesn't Have")
            self.VBox.addItem("Very Tight")
            self.VBox.addItem("Tight")
            self.VBox.addItem("Average")
            self.VBox.addItem("Loose")
            self.VBox.addItem("Very Loose")
            VWidget.setGeometry(205,225,202,82)

            AWidget = QWidget(BodyWidget)
            self.ALabel = QLabel("Anal Tightness", AWidget)
            self.ALabel.setGeometry(0, 0, 200, 35)
            self.ALabel.setAlignment(QtCore.Qt.AlignCenter)
            self.ABox = QComboBox(AWidget)
            self.ABox.setGeometry(0, 40, 200, 35)
            self.ABox.addItem("Doesn't Have")
            self.ABox.addItem("Very Tight")
            self.ABox.addItem("Tight")
            self.ABox.addItem("Average")
            self.ABox.addItem("Loose")
            self.ABox.addItem("Very Loose")
            AWidget.setGeometry(410,225,202,82)

            PWidget = QWidget(BodyWidget)
            self.PLabel = QLabel("Penis Size", PWidget)
            self.PLabel.setGeometry(0, 0, 200, 35)
            self.PLabel.setFont(QFont('Segoe UI', 14))
            self.PLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.PBox = QComboBox(PWidget)
            self.PBox.setGeometry(0, 40, 200, 35)
            self.PBox.setFont(QFont('Segoe UI', 11))
            self.PBox.addItem("Doesn't Have")
            self.PBox.addItem("Tiny")
            self.PBox.addItem("Small")
            self.PBox.addItem("Average")
            self.PBox.addItem("Big")
            self.PBox.addItem("Huge")
            PWidget.setGeometry(0,310,202,82)

            BWidget = QWidget(BodyWidget)
            self.BLabel = QLabel("Balls Size", BWidget)
            self.BLabel.setGeometry(0, 0, 200, 35)
            self.BLabel.setAlignment(QtCore.Qt.AlignCenter)
            self.BBox = QComboBox(BWidget)
            self.BBox.setGeometry(0, 40, 200, 35)
            self.BBox.addItem("Doesn't Have")
            self.BBox.addItem("Tiny")
            self.BBox.addItem("Small")
            self.BBox.addItem("Average")
            self.BBox.addItem("Big")
            self.BBox.addItem("Huge")
            BWidget.setGeometry(205,310,202,82)

            VirginWidget = QWidget(BodyWidget)
            self.VirginLabel = QLabel("Virginities", VirginWidget)
            self.VirginLabel.setGeometry(0, 0, 200, 35)
            self.VirginLabel.setAlignment(QtCore.Qt.AlignCenter)

            self.VVirginLabel = QLabel("V", VirginWidget)
            self.VVirginLabel.setGeometry(45,40,25,25)
            self.VVirginBox = QCheckBox(VirginWidget)
            self.VVirginBox.setGeometry(50,65,15,15)
            self.VVirginBox.setChecked(True)

            self.AVirginLabel = QLabel("A", VirginWidget)
            self.AVirginLabel.setGeometry(75,40,25,25)
            self.AVirginBox = QCheckBox(VirginWidget)
            self.AVirginBox.setGeometry(80,65,15,15)
            self.AVirginBox.setChecked(True)

            self.PVirginLabel = QLabel("P", VirginWidget)
            self.PVirginLabel.setGeometry(105,40,25,25)
            self.PVirginBox = QCheckBox(VirginWidget)
            self.PVirginBox.setGeometry(110,65,15,15)
            self.PVirginBox.setChecked(True)

            self.MVirginLabel = QLabel("M", VirginWidget)
            self.MVirginLabel.setGeometry(135,40,25,25)
            self.MVirginBox = QCheckBox(VirginWidget)
            self.MVirginBox.setGeometry(140,65,15,15)
            self.MVirginBox.setChecked(True)
            VirginWidget.setGeometry(410,310,202,82)

            BodyWidget.setGeometry(970,65,610,425)

            Height = 470
            self.BodyWidget.Height = Height
        except Exception as e:
            print(e)

    def setTraits(self):
        self.TraitsLabel = QLabel("Traits", self.TraitsWidget, objectName = "MainTitle")
        self.TraitsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.TraitsLabel.setGeometry(5,5,1580,50)

        for TraitID in Globals.SoLTraits:
            try:
                TraitWidget = Globals.SoLTraits[TraitID]["Reference"].GetTraitSelection(self, TraitID)
                if TraitWidget == None:
                    Log(1, "ERROR RETRIEVING TRAIT WIDGET", "No widget available", TraitID, Globals.SoLTraits[TraitID]["Reference"])
                    continue
                    # raise "No widget available"
                self.TraitWidgetsDict[TraitID] = TraitWidget
            except Exception as e:
                Log(2, "ERROR RETRIEVING TRAIT WIDGET", e, TraitID, Globals.SoLTraits[TraitID]["Reference"])


        MaxWidth = self.TraitsWidget.width()
        MaxHeight = self.TraitsWidget.height()

        TotalWidth = 0
        TotalHeight = 0

        TempHeight = 0
        TempWidth = 5

        Row, Layer = 0, 0
        TraitsLayout = QGridLayout()
        for TraitID in self.TraitWidgetsDict:
            TempWidth += 5
            ObjectWidth = self.TraitWidgetsDict[TraitID].width()
            ObjectHeight = self.TraitWidgetsDict[TraitID].height()

            if ObjectHeight > TempHeight:
                TempHeight = ObjectHeight

            if TempWidth + ObjectWidth < MaxWidth:
                TraitsLayout.addWidget(self.TraitWidgetsDict[TraitID], Layer, Row)
                TempWidth += ObjectWidth + 10
                Row += 1
            else:
                Layer += 1
                Row = 0
                TraitsLayout.addWidget(self.TraitWidgetsDict[TraitID], Layer, Row)

                TempWidth = 5
                TotalHeight += TempHeight + 10
                TempWidth += ObjectWidth + 10
                Row += 1
        else:
            TotalHeight += TempHeight + 5

        if Layer >= 1:
            Width = MaxWidth
            Height = TotalHeight
        else:
            Width = TotalWidth + 5
            Height = TempHeight + 10

        TraitsLayoutWidget = QWidget(self.TraitsWidget)
        TraitsLayoutWidget.setLayout(TraitsLayout)
        TraitsLayoutWidget.setGeometry(QRect(0,55,Width,Height))
        TraitsLayoutWidget.setStyleSheet('''
        .QWidget{
        border: none;
        background-color: rgba(23,23,23,0);
        }
        ''')

        self.TraitsWidget.Height = Height + 55
        self.TraitsWidget.setMinimumHeight(Height + 55)
        self.TraitsWidget.setMaximumHeight(Height + 55)

    def setDescriptions(self):
        self.DescriptionsLabel = QLabel("Descriptions", self.DescriptionsWidget, objectName = "MainTitle")
        self.DescriptionsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.DescriptionsLabel.setGeometry(5,5,1580,50)


        LegsWidget = QWidget(self.DescriptionsWidget)
        self.LegsLabel = QLabel("Legs", LegsWidget)
        self.LegsLabel.setGeometry(0,0,520,45)
        self.LegsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.LegsLine = QTextEdit(LegsWidget)
        self.LegsLine.setGeometry(0,50,520,300)
        self.LegsLine.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        LegsWidget.setGeometry(5,60,520,302)

        ArmsWidget = QWidget(self.DescriptionsWidget)
        self.ArmsLabel = QLabel("Arms", ArmsWidget)
        self.ArmsLabel.setGeometry(0,0,520,45)
        self.ArmsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ArmsLine = QTextEdit(ArmsWidget)
        self.ArmsLine.setGeometry(0,50,520,300)
        self.ArmsLine.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        ArmsWidget.setGeometry(535,60,520,302)

        FaceWidget = QWidget(self.DescriptionsWidget)
        self.FaceLabel = QLabel("Face", FaceWidget)
        self.FaceLabel.setGeometry(0,0,520,45)
        self.FaceLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.FaceLine = QTextEdit(FaceWidget)
        self.FaceLine.setGeometry(0,50,520,300)
        self.FaceLine.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        FaceWidget.setGeometry(1065,60,520,302)


        CoreWidget = QWidget(self.DescriptionsWidget)
        self.CoreLabel = QLabel("Core", CoreWidget)
        self.CoreLabel.setGeometry(0,0,520,45)
        self.CoreLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.CoreLine = QTextEdit(CoreWidget)
        self.CoreLine.setGeometry(0,50,520,300)
        self.CoreLine.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        CoreWidget.setGeometry(5,370,520,302)

        StoryWidget = QWidget(self.DescriptionsWidget)
        self.StoryLabel = QLabel("Backstory", StoryWidget)
        self.StoryLabel.setGeometry(0,0,520,45)
        self.StoryLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.StoryLine = QTextEdit(StoryWidget)
        self.StoryLine.setGeometry(0,50,520,300)
        self.StoryLine.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        StoryWidget.setGeometry(535,370,520,302)


        GenitalsWidget = QWidget(self.DescriptionsWidget)
        self.GenitalsLabel = QLabel("Genitals", GenitalsWidget)
        self.GenitalsLabel.setGeometry(0,0,520,45)
        self.GenitalsLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.GenitalsLine = QTextEdit(GenitalsWidget)
        self.GenitalsLine.setGeometry(0,50,520,300)
        self.GenitalsLine.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        GenitalsWidget.setGeometry(1065,370,520,302)


        self.DescriptionsWidget.Height = 680
        self.DescriptionsWidget.setMinimumHeight(680)
        self.DescriptionsWidget.setMaximumHeight(680)

    def CheckLoad(self):
        Path = "NPCData"
        DirList = os.listdir(Path)
        for DirName in DirList:
            try:
                # with pathlib.Path.open(f'''NPCData/{DirName}/{DirName}Data.json''', 'rb') as f:
                with pathlib.Path.open(pathlib.Path() / "NPCData" / DirName / f"{DirName}Data.json" , 'rb') as f:
                    NPCData = json.load(f)
                Name = NPCData["Name"]
                ID = NPCData["ID"]
                self.LoadBox.addItem(f'''{Name} {ID}''' )
                self.LoadBox.NPCData[f'''{Name} {ID}'''] = NPCData
            except Exception as e:
                ""

    def Load(self):
        try:
            Current = self.LoadBox.currentText()
            NPCData = self.LoadBox.NPCData[Current]
            if NPCData["Version"] == 1:
                self.FullNameLine.setText(NPCData["FullName"])
                self.MainNameLine.setText(NPCData["Name"])
                self.SkinColorLine.setText(NPCData["BodyType"]["SkinColor"])
                self.HairColorLine.setText(NPCData["BodyType"]["HairColor"])
                self.RaceLine.setText(NPCData["BodyType"]["Race"])
                # self.EyesLine.setText(NPCData["BodyType"]["SkinColor"])
                self.IDLine.setText(NPCData["ID"])
                self.FaceBox.setCurrentIndex(NPCData["BodyType"]["FaceType"])
                self.BodySizeBox.setCurrentIndex(NPCData["BodyType"]["BodySize"])
                self.BodyTypeBox.setCurrentIndex(NPCData["BodyType"]["Complexion"])
                self.ChestBox.setCurrentIndex(NPCData["BodyType"]["ChestSize"])
                self.HipBox.setCurrentIndex(NPCData["BodyType"]["HipsSize"])
                self.AssBox.setCurrentIndex(NPCData["BodyType"]["AssSize"])
                self.LipBox.setCurrentIndex(NPCData["BodyType"]["LipsSize"])
                self.VBox.setCurrentIndex(NPCData["BodyType"]["VTightness"])
                self.ABox.setCurrentIndex(NPCData["BodyType"]["ATightness"])
                self.PBox.setCurrentIndex(NPCData["BodyType"]["PenisSize"])
                self.BBox.setCurrentIndex(NPCData["BodyType"]["BallsSize"])

                self.VVirginBox.setChecked(NPCData["Traits"]["isVirginV"])
                self.AVirginBox.setChecked(NPCData["Traits"]["isVirginA"])
                self.PVirginBox.setChecked(NPCData["Traits"]["isVirginP"])
                self.MVirginBox.setChecked(NPCData["Traits"]["isVirginM"])

                if NPCData["BodyType"]["Pronouns"]["Structure"] == "Male":
                    self.PSubLine.setText(NPCData["BodyType"]["Pronouns"]["Pronoun1"])
                    self.PObjLine.setText(NPCData["BodyType"]["Pronouns"]["Pronoun2"])
                    self.PPosLine.setText(NPCData["BodyType"]["Pronouns"]["Pronoun3"])
                    self.PIPosLine.setText(NPCData["BodyType"]["Pronouns"]["Pronoun3"])

                    self.PStructureButtonM.setChecked(True)
                    self.PStructureButtonF.setChecked(False)
                if NPCData["BodyType"]["Pronouns"]["Structure"] == "Female":
                    self.PSubLine.setText(NPCData["BodyType"]["Pronouns"]["Pronoun1"])
                    self.PObjLine.setText(NPCData["BodyType"]["Pronouns"]["Pronoun2"])
                    self.PPosLine.setText(NPCData["BodyType"]["Pronouns"]["Pronoun2"])
                    self.PIPosLine.setText(NPCData["BodyType"]["Pronouns"]["Pronoun3"])

                    self.PStructureButtonM.setChecked(False)
                    self.PStructureButtonF.setChecked(True)

                # print(self.TraitWidgetsDict["Courage0"].ReturnValue(self.TraitWidgetsDict["Courage0"]))
                try:
                    self.TraitWidgetsDict["Courage0"].LoadValue(self.TraitWidgetsDict["Courage0"], NPCData["Traits"]["isCourage"])
                    self.TraitWidgetsDict["Attitude0"].LoadValue(self.TraitWidgetsDict["Attitude0"], NPCData["Traits"]["isAttitude"])
                    self.TraitWidgetsDict["Pride0"].LoadValue(self.TraitWidgetsDict["Pride0"], NPCData["Traits"]["isPride"])
                    self.TraitWidgetsDict["Dere0"].LoadValue(self.TraitWidgetsDict["Dere0"], NPCData["Traits"]["isDere"])
                    self.TraitWidgetsDict["SelfControl0"].LoadValue(self.TraitWidgetsDict["SelfControl0"], NPCData["Traits"]["isControl"])
                    self.TraitWidgetsDict["Cheerfulness0"].LoadValue(self.TraitWidgetsDict["Cheerfulness0"], NPCData["Traits"]["isCheerful"])
                    self.TraitWidgetsDict["Shyness0"].LoadValue(self.TraitWidgetsDict["Shyness0"], NPCData["Traits"]["isShy"])
                    self.TraitWidgetsDict["Gullible0"].LoadValue(self.TraitWidgetsDict["Gullible0"], NPCData["Traits"]["isGullible"])
                    self.TraitWidgetsDict["Charm0"].LoadValue(self.TraitWidgetsDict["Charm0"], NPCData["Traits"]["isCharm"])
                    self.TraitWidgetsDict["SubstanceResistance0"].LoadValue(self.TraitWidgetsDict["SubstanceResistance0"], NPCData["Traits"]["isSubstanceResistance"])
                    self.TraitWidgetsDict["SexualInterest0"].LoadValue(self.TraitWidgetsDict["SexualInterest0"], NPCData["Traits"]["isSexualInterest"])
                    self.TraitWidgetsDict["Virtue0"].LoadValue(self.TraitWidgetsDict["Virtue0"], NPCData["Traits"]["isVirtue"])
                    self.TraitWidgetsDict["Chastity0"].LoadValue(self.TraitWidgetsDict["Chastity0"], NPCData["Traits"]["isChastity"])
                    self.TraitWidgetsDict["Openess0"].LoadValue(self.TraitWidgetsDict["Openess0"], NPCData["Traits"]["isOpenessTrait"])
                    self.TraitWidgetsDict["PainResistance0"].LoadValue(self.TraitWidgetsDict["PainResistance0"], NPCData["Traits"]["isPainResistance"])
                    self.TraitWidgetsDict["ArousalEase0"].LoadValue(self.TraitWidgetsDict["ArousalEase0"], NPCData["Traits"]["isAroussalEase"])
                    self.TraitWidgetsDict["ResponseToPleasure0"].LoadValue(self.TraitWidgetsDict["ResponseToPleasure0"], NPCData["Traits"]["isResponseToPleasure"])
                    self.TraitWidgetsDict["Perversion0"].LoadValue(self.TraitWidgetsDict["Perversion0"], NPCData["Traits"]["isPerversion"])
                    self.TraitWidgetsDict["Dominance0"].LoadValue(self.TraitWidgetsDict["Dominance0"], NPCData["Traits"]["isDominanceTrait"])
                    self.TraitWidgetsDict["Forceful0"].LoadValue(self.TraitWidgetsDict["Forceful0"], NPCData["Traits"]["isForcefulTrait"])
                    self.TraitWidgetsDict["Loyalty0"].LoadValue(self.TraitWidgetsDict["Loyalty0"], NPCData["Traits"]["isLoyaltyTrait"])
                    self.TraitWidgetsDict["Violence0"].LoadValue(self.TraitWidgetsDict["Violence0"], NPCData["Traits"]["isViolenceTrait"])
                    self.TraitWidgetsDict["Beauty0"].LoadValue(self.TraitWidgetsDict["Beauty0"], NPCData["Traits"]["isBeautyTrait"])
                    self.TraitWidgetsDict["Shame0"].LoadValue(self.TraitWidgetsDict["Shame0"], NPCData["Traits"]["isShameTrait"])
                    self.TraitWidgetsDict["Will0"].LoadValue(self.TraitWidgetsDict["Will0"], NPCData["Traits"]["isWillTrait"])
                    self.TraitWidgetsDict["Influence0"].LoadValue(self.TraitWidgetsDict["Influence0"], NPCData["Traits"]["isInfluenceTrait"])
                    self.TraitWidgetsDict["Fertility0"].LoadValue(self.TraitWidgetsDict["Fertility0"], NPCData["Traits"]["isFertility"])
                    dict = {"V":NPCData["Traits"]["isLewdV"], "A":NPCData["Traits"]["isLewdA"], "B":NPCData["Traits"]["isLewdB"], "P":NPCData["Traits"]["isLewdP"], "M":NPCData["Traits"]["isLewdM"] }
                    self.TraitWidgetsDict["LewdBody0"].LoadValue(self.TraitWidgetsDict["LewdBody0"], dict)

                except Exception as e:
                    print("Ee", e)
            elif NPCData["Version"] == 2:
                self.MainNameLine.setText(NPCData["Name"])
                self.IDLine.setText(NPCData["ID"])

                self.FullNameLine.setText(NPCData["BodyData"]["FullName"])
                try:
                    self.AgeBox.setCurrentIndex(NPCData["BodyData"]["PhysicalAge"])
                except Exception as e:
                    ""
                try:
                    self.EnergySlider.setValue(NPCData["GeneralAbilities"]["MaxEnergy"])
                except Exception as e:
                    ""
                try:
                    self.PersonalityBox.setCurrentIndex( self.PersonalityBox.Personalities.index(NPCData["Personality"]) )
                except Exception as e:
                    ""



                self.SkinColorLine.setText(NPCData["BodyData"]["SkinColor"])
                self.HairColorLine.setText(NPCData["BodyData"]["HairColor"])
                self.RaceLine.setText(NPCData["BodyData"]["Race"])
                self.EyesLine.setText(NPCData["BodyData"]["Eyes"])
                self.FaceBox.setCurrentIndex(NPCData["BodyData"]["Face"])
                self.BodySizeBox.setCurrentIndex(NPCData["BodyData"]["Height"])
                self.BodyTypeBox.setCurrentIndex(NPCData["BodyData"]["Complexion"])
                self.ChestBox.setCurrentIndex(NPCData["BodyData"]["Chest"])
                self.HipBox.setCurrentIndex(NPCData["BodyData"]["Hips"])
                self.AssBox.setCurrentIndex(NPCData["BodyData"]["Ass"])
                self.LipBox.setCurrentIndex(NPCData["BodyData"]["Lips"])
                self.VBox.setCurrentIndex(NPCData["BodyData"]["VTightness"])
                self.ABox.setCurrentIndex(NPCData["BodyData"]["ATightness"])
                self.PBox.setCurrentIndex(NPCData["BodyData"]["PenisSize"])
                self.BBox.setCurrentIndex(NPCData["BodyData"]["BallsSize"])

                self.VVirginBox.setChecked(NPCData["BodyData"]["VVirgin"])
                self.AVirginBox.setChecked(NPCData["BodyData"]["AVirgin"])
                self.PVirginBox.setChecked(NPCData["BodyData"]["PVirgin"])
                self.MVirginBox.setChecked(NPCData["BodyData"]["MVirgin"])


                self.PSubLine.setText(NPCData["BodyData"]["Pronouns"]["PSub"])
                self.PObjLine.setText(NPCData["BodyData"]["Pronouns"]["PObj"])
                self.PPosLine.setText(NPCData["BodyData"]["Pronouns"]["PPos"])
                self.PIPosLine.setText(NPCData["BodyData"]["Pronouns"]["PIPos"])

                if NPCData["BodyData"]["Sex"] == "Male":
                    self.PStructureButtonM.setChecked(True)
                    self.PStructureButtonF.setChecked(False)
                if NPCData["BodyData"]["Sex"] == "Female":
                    self.PStructureButtonM.setChecked(False)
                    self.PStructureButtonF.setChecked(True)

                for TraitID in NPCData["Traits"]:
                    if TraitID in self.TraitWidgetsDict:
                        try:
                            self.TraitWidgetsDict[TraitID].LoadValue(self.TraitWidgetsDict[TraitID], NPCData["Traits"][TraitID])
                        except:
                            ""

                self.LegsLine.setText(NPCData["Descriptions"]["Legs"])
                self.ArmsLine.setText(NPCData["Descriptions"]["Arms"])
                self.FaceLine.setText(NPCData["Descriptions"]["Head"])
                self.CoreLine.setText(NPCData["Descriptions"]["Core"])
                self.StoryLine.setText(NPCData["Descriptions"]["Backstory"])
                self.GenitalsLine.setText(NPCData["Descriptions"]["Genitals"])

                self.LabelStatus.setText(f'''Succesfully loaded {NPCData["Name"]} {NPCData["ID"]}''')
        except Exception as e:
            print(e)
            ""
            # print(e)

    def Save(self):
        try:
            NPCData = {}
            FullName = self.FullNameLine.text()
            Name = self.MainNameLine.text()
            Age = self.AgeBox.currentIndex()
            MaxEnergy = self.EnergySlider.value()
            Personality = self.PersonalityBox.Personalities[self.PersonalityBox.currentIndex()]
            SkinColor = self.SkinColorLine.text()
            Race = self.RaceLine.text()
            ID = self.IDLine.text()
            HairColor = self.HairColorLine.text()
            Face = self.FaceBox.currentIndex()
            Eyes = self.EyesLine.text()
            Lips = self.LipBox.currentIndex()
            Height = self.BodySizeBox.currentIndex()
            Complexion = self.BodyTypeBox.currentIndex()
            PSub = self.PSubLine.text()
            PObj = self.PObjLine.text()
            PPos = self.PPosLine.text()
            PIPos = self.PIPosLine.text()
            Sex = "Male" if self.PStructureButtonM.isChecked() else "Female"

            Hips = self.HipBox.currentIndex()
            Ass = self.AssBox.currentIndex()
            Chest = self.ChestBox.currentIndex()
            V = self.VBox.currentIndex()
            A = self.ABox.currentIndex()
            P = self.PBox.currentIndex()
            B = self.BBox.currentIndex()
            VVirgin = self.VVirginBox.isChecked()
            AVirgin = self.AVirginBox.isChecked()
            PVirgin = self.PVirginBox.isChecked()
            MVirgin = self.MVirginBox.isChecked()

            # LegsDesc = self.LegsLine.toHtml()
            LegsDesc = self.LegsLine.toPlainText()
            ArmsDesc = self.ArmsLine.toPlainText()
            FaceDesc = self.FaceLine.toPlainText()
            CoreDesc = self.CoreLine.toPlainText()
            StoryDesc = self.StoryLine.toPlainText()
            GenitalsDesc = self.GenitalsLine.toPlainText()

            NPCData = Globals.SoLOtherData["BaseData"]
            NPCData["Name"] = Name
            NPCData["ID"] = ID
            NPCData["Personality"] = Personality

            NPCData["State"]["Energy"] = MaxEnergy

            NPCData["BodyData"]["FullName"] = FullName
            NPCData["BodyData"]["SkinColor"] = SkinColor
            NPCData["BodyData"]["HairColor"] = HairColor
            NPCData["BodyData"]["PhysicalAge"] = Age
            NPCData["BodyData"]["Race"] = Race
            NPCData["BodyData"]["Face"] = Face
            NPCData["BodyData"]["Eyes"] = Eyes
            NPCData["BodyData"]["Lips"] = Lips
            NPCData["BodyData"]["Height"] = Height
            NPCData["BodyData"]["Complexion"] = Complexion
            NPCData["BodyData"]["Sex"] = Sex
            NPCData["BodyData"]["Pronouns"] = {"PSub":PSub, "PObj":PObj, "PPos":PPos, "PIPos":PIPos}
            NPCData["BodyData"]["Hips"] = Hips
            NPCData["BodyData"]["Ass"] = Ass
            NPCData["BodyData"]["Chest"] = Chest
            NPCData["BodyData"]["VTightness"] = V
            NPCData["BodyData"]["ATightness"] = A
            NPCData["BodyData"]["PenisSize"] = P
            NPCData["BodyData"]["BallsSize"] = B
            NPCData["BodyData"]["VVirgin"] = VVirgin
            NPCData["BodyData"]["AVirgin"] = AVirgin
            NPCData["BodyData"]["PVirgin"] = PVirgin
            NPCData["BodyData"]["MVirgin"] = MVirgin


            NPCData["GeneralAbilities"]["MaxEnergy"] = MaxEnergy

            NPCData["Descriptions"]["Backstory"] = StoryDesc
            NPCData["Descriptions"]["Core"] = CoreDesc
            NPCData["Descriptions"]["Head"] = FaceDesc
            NPCData["Descriptions"]["Arms"] = ArmsDesc
            NPCData["Descriptions"]["Legs"] = LegsDesc
            NPCData["Descriptions"]["Genitals"] = GenitalsDesc

            # NPCData["Actions"]["PreviousTask"] = Globals.SoLOtherData["IdlingTask"]
            # NPCData["Actions"]["CurrentTask"] = Globals.SoLOtherData["IdlingTask"]
            # NPCData["Actions"]["FutureTask"] = Globals.SoLOtherData["IdlingTask"]

            for TraitID in self.TraitWidgetsDict:
                Value = self.TraitWidgetsDict[TraitID].ReturnValue(self.TraitWidgetsDict[TraitID])
                NPCData["Traits"][TraitID] = Value

            if ID == "" or Name == "":
                self.LabelStatus.setText("Please fill the ID or Name")
            else:
                self.LabelStatus.setText(f'''Succesfully saved {Name} {ID}''')

                Path = os.path.abspath( pathlib.Path() / "NPCData" / f"{Name}{ID}" )
                # Path = "NPCData/" + Name + ID
                if not pathlib.Path.exists(Path):
                    pathlib.Path.mkdir(Path, parents=True)
                FullPath = os.path.abspath( pathlib.Path() / "NPCData" / f"{Name}{ID}" / f"{Name}{ID}Data.json" )
                # FullPath = f'''{Path}/{Name}{ID}Data.json'''
                with pathlib.Path.open(FullPath, 'w') as f:
                    json.dump(NPCData, f)

        except Exception as e:
            self.LabelStatus.setText('''Something went wrong''')
            Log(2, "ERROR SAVING CHARACTER DATA", e, NPCData)
            print(e)

    def Refresh(self):
        ""
    def ResizeEvent(self):
        Width = Globals.Layouts["MainF"].width()
        Height = Globals.Layouts["MainF"].height()
        Diff = 1024 - Height

        self.MainScroll.setGeometry(5,5,1592,955-Diff)
        self.ControlWidget.setGeometry(5,964-Diff,1592,55)


def Initialize(self, Reference):
    if "MakerUI" not in Globals.Layouts:
        Object = UiLayoutMakerMenu()
