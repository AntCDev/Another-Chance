import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QTextCursor
import json
import os


class UiLayoutHelpMenu(object):
    def Ui(self, MainWindow):
        self.helpMenuUI = QWidget(MainWindow)
        # mainwindow.setWindowIcon(QtGui.QIcon('PhotoIcon.png'))
        self.helpMenuUI.setStyleSheet('''
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
        MainWindow.setCentralWidget(self.helpMenuUI)
        MainWindow.setFixedSize(1280, 800)


        self.labelBack = QLabel(self.helpMenuUI)
        self.labelBack.setGeometry(230,10,820,780)
        self.labelBack.setStyleSheet('''
                QLabel{
         border: 1px solid black;
         background : rgb(23, 23, 23);
         color:rgb(255, 255, 255);
        }
        ''')
        self.labelBack.setFont(QFont('Segoe UI', 14))

        self.buttonBack = QPushButton("Back To Menu", self.helpMenuUI)
        self.buttonBack.setFont(QFont('Segoe UI', 14))
        self.buttonBack.setGeometry(260,670,160,35)

        self.scroll = QScrollArea(self.helpMenuUI)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setWidgetResizable(True)
        self.scroll.setGeometry(230,10,820,780)
        self.scroll.setWidgetResizable(True)
        x = '''Help '''
        object = QLabel()
        object.setText(x)
        object.setWordWrap(True)
        object.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        object.setFont(QFont('Segoe UI', 14))
        object.setStyleSheet('''
                QLabel{
         border: 1px solid black;
         background : rgb(23, 23, 23);
         color:rgb(255, 255, 255);
        }
        ''')
        self.scroll.setWidget(object)
        self.buttonBack = QPushButton("Back To Menu", self.helpMenuUI)
        self.buttonBack.setFont(QFont('Segoe UI', 14))
        self.buttonBack.setGeometry(260,650,160,35)

def Initialize(self, Reference):
    ""
