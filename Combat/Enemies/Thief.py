from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QTextCursor
import Globals

class Enemy:
    def __init__(self, Name, HP, EnemyID):
        self.Name = Name
        self.HP = HP
        print(EnemyID)
        self.ID = EnemyID
        self.Status = "Alive"

    def __del__(self):
        print(f"")

    def Testa(self):
        print("Ohno")

    def DamageTaken(self, DMG):
        # print("Damages")
        self.HP -= DMG
        if self.HP > 0:
            # print("You'll never get me")
            ""
        else:
            # print("I've been gotten")
            ""
            try:
                Globals.BattleInfo["Target"].remove(self.ID)
            except:
                ""
            self.Status = "Dead"
        Globals.MainWindow["MainW"].refresh()


    def BaseData(self):
        BD = {"CR":0.5, "DL":1}
        return BD

    def ObjectWidget(self, EnemyID):
        TWidget = QWidget()
        # self.Enemy1.setGeometry(300,300,220,320)
        TWidget.setFixedSize(320,280)
        TWidget.setStyleSheet('''
        QWidget{
        border: 1px solid black;
        background-color:rgb(23, 23, 23);
        }
        ''')
        if self.ID in Globals.BattleInfo["Target"]:
            TWidget.setStyleSheet('''
            QWidget{
            border: 1px solid black;
            background-color:rgb(23, 23, 23);
            }
            .QWidget
            {
            border: 1px solid black;
            border-color:rgb(160,160,50)
            }''')
        else:
            TWidget.setStyleSheet('''
            QWidget{
            border: 1px solid black;
            background-color:rgb(23, 23, 23);
            }
            ''')
        # print(Globals.BattleInfo["Target"])
        # print(self.ID)
        # TWidget.mouseReleaseEvent = lambda event: print(f'{self}      {Globals.Enemies["MainW"]}')
        # TWidget.mouseReleaseEvent = lambda event: Globals.Enemies["MainW"].wrking()
        TWidget.mouseReleaseEvent = lambda event: self.events("Targeting")

        EnemyName = QPushButton("Aria", TWidget, clicked = lambda: print("Name"))
        EnemyName.setFont(QFont('Segoe UI', 12))
        EnemyName.setGeometry(10,10,300,30)
        EnemyName.setStyleSheet('''
        QPushButton{
        border: 1px solid black;
        background : rgb(35, 35, 35);
        color:rgb(255, 255, 255)
        }
        ''')

        EnemyPortrait = QLabel(TWidget)
        EnemyPortrait.setGeometry(10, 49, 100, 100)

        labelHP = QLabel(TWidget)
        labelHP.setGeometry(113,50,100,31)
        labelHP.setText(f'''<p><span style=" font-weight:600; color:#ff0000;">HP: {self.HP}</span></p> ''')
        labelHP.setFont(QFont('Segoe UI', 10))
        labelHP.setStyleSheet('''
        QLabel{
            color:red;
            background-color:rgb(35,35,35);
            }
        ''')
        labelSHP1 = QLabel(TWidget)
        labelSHP1.setGeometry(218,53,18,25)
        labelSHP1.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')
        labelSHP2 = QLabel(TWidget)
        labelSHP2.setGeometry(236,53,18,25)
        labelSHP2.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')
        labelSHP3 = QLabel(TWidget)
        labelSHP3.setGeometry(254,53,18,25)
        labelSHP3.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')
        labelSHP4 = QLabel(TWidget)
        labelSHP4.setGeometry(272,53,18,25)
        labelSHP4.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')
        labelSHP5 = QLabel(TWidget)
        labelSHP5.setGeometry(290,53,18,25)
        labelSHP5.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')


        labelMT = QLabel(TWidget)
        labelMT.setGeometry(113,83,100,31)
        labelMT.setText('''<p><span style=" font-weight:600;">MT: 700</span></p> ''')
        labelMT.setFont(QFont('Segoe UI', 10))
        labelMT.setStyleSheet('''
        QLabel{
            color:rgb(214, 0, 255);
            background-color:rgb(35,35,35);
            }
        ''')
        labelSMT1 = QLabel(TWidget)
        labelSMT1.setGeometry(218,86,18,25)
        labelSMT1.setStyleSheet('''QLabel{background-color:rgb(214, 0, 255) }''')
        labelSMT2 = QLabel(TWidget)
        labelSMT2.setGeometry(236,86,18,25)
        labelSMT2.setStyleSheet('''QLabel{background-color:rgb(214, 0, 255) }''')
        labelSMT3 = QLabel(TWidget)
        labelSMT3.setGeometry(254,86,18,25)
        labelSMT3.setStyleSheet('''QLabel{background-color:rgb(214, 0, 255) }''')
        labelSMT4 = QLabel(TWidget)
        labelSMT4.setGeometry(272,86,18,25)
        labelSMT4.setStyleSheet('''QLabel{background-color:rgb(214, 0, 255) }''')
        labelSMT5 = QLabel(TWidget)
        labelSMT5.setGeometry(290,86,18,25)
        labelSMT5.setStyleSheet('''QLabel{background-color:rgb(214, 0, 255) }''')


        labelEN = QLabel(TWidget)
        labelEN.setGeometry(113,117,100,31)
        labelEN.setText('''<p><span style=" font-weight:600;">EN: 500</span></p> ''')
        labelEN.setFont(QFont('Segoe UI', 10))
        labelEN.setStyleSheet('''
        QLabel{
            color:rgb(0, 100, 255);
            background-color:rgb(35,35,35);
            }
        ''')
        labelSEN1 = QLabel(TWidget)
        labelSEN1.setGeometry(218,120,18,25)
        labelSEN1.setStyleSheet('''QLabel{background-color:rgb(0, 100, 255) }''')
        labelSEN2 = QLabel(TWidget)
        labelSEN2.setGeometry(236,120,18,25)
        labelSEN2.setStyleSheet('''QLabel{background-color:rgb(0, 100, 255) }''')
        labelSEN3 = QLabel(TWidget)
        labelSEN3.setGeometry(254,120,18,25)
        labelSEN3.setStyleSheet('''QLabel{background-color:rgb(0, 100, 255) }''')
        labelSEN4 = QLabel(TWidget)
        labelSEN4.setGeometry(272,120,18,25)
        labelSEN4.setStyleSheet('''QLabel{background-color:rgb(0, 100, 255) }''')
        labelSEN5 = QLabel(TWidget)
        labelSEN5.setGeometry(290,120,18,25)
        labelSEN5.setStyleSheet('''QLabel{background-color:rgb(0, 100, 255) }''')


        labelActions = QLabel(TWidget)
        labelActions.setGeometry(10,150,300,75)
        labelActions.setText('''<html><head/><body>Quick Attack:<br/><span style=" font-weight:600; color:#00ff7f;">Quick.</span> 5 x 2 to Chraum<br/><span style=" font-weight:600; color:#1e74ff;">2nd Line</span><br/><span style=" font-weight:600; color:#1e74ff;">3rd Line</span></body></html> ''')
        labelActions.setFont(QFont('Segoe UI', 9))
        labelActions.setAlignment(Qt.AlignLeft)
        labelActions.setAlignment(Qt.AlignTop)
        labelActions.setStyleSheet('''
        QLabel{
            background-color:rgb(23,23,23);
            }
        ''')

        labelStatus = QLabel(TWidget)
        labelStatus.setGeometry(10,230,300,40)
        labelStatus.setAlignment(Qt.AlignLeft)


        return TWidget


    def events(self, ID):
        if ID == "Targeting":
            if self.ID in Globals.BattleInfo["Target"]:
                Globals.BattleInfo["Target"].remove(self.ID)
            else:
                Globals.BattleInfo["Target"].append(self.ID)

            # self.HP -= 10
            # if self.HP > 0:
            #     # print("You'll never get me")
            #     ""
            # else:
            #     # print("I've been gotten")
            #     ""
            #     try:
            #         Globals.BattleInfo["Target"].remove(self.ID)
            #     except:
            #         ""
            #     self.Status = "Dead"
            Globals.MainWindow["MainW"].refresh()
