# import random
def oh(self):
    class Enemy:
        def __init__(self, Name, HP, EnemyID):
            self.Name = Name
            self.HP = HP
            self.ID = EnemyID
            self.Status = "Alive"
            self.CanBeTargeted = 1
            self.Effects = []

        def __del__(self):
            ""

        def DamageTaken(self, DMG):
            self.HP -= DMG
            if self.HP > 0:
                ""
            else:
                self.Status = "Dead"

            Globals.MainWindow["MainW"].refresh()

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

            TWidget.mouseReleaseEvent = lambda event: self.events({"ID":"Targeting"})

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


        def events(self, Data):
            ID = Data["ID"]
            if ID == "Targeting":
                if self.ID in Globals.BattleInfo["Target"]:
                    Globals.BattleInfo["Target"].remove(self.ID)
                else:
                    if self.CanBeTargeted == 1:
                        Globals.BattleInfo["Target"].append(self.ID)
            elif ID == "Attakced" or ID == "EnemyEffect" or ID == "AllyEffect":
                # PINGS THE EFFECTS AFFECTING SELF
                for Effect in self.Effects:
                    try:
                        # CHECKS IF THE REFERENCE FOR THE EFFECT FILE IS ALREADY EXISTING
                        if Effect["Origin"] in Globals.References:
                            Reference = Globals.Refenreces[Effect["Origin"]]
                        else:
                            # IF NOT THEN IT MAKES SURE THE PATH IS IN sys.path
                            PathFull = os.path.abspath(__file__)
                            NameLen = len(os.path.basename(__file__))
                            Path = PathFull[0:-NameLen]
                            Path += r'''\Combat\Effects '''
                            if Path not in sys.path:
                                sys.path.insert(0, Path)
                            # IMPORTS THE FILE AND ADDS THE REFERENCE.
                            Reference = __import__(Effect["Origin"])
                            Globals.Refenreces[Effect["Origin"]] = Reference

                        # PINGS THE EFFECT WITH THE DATA OF THE TRIGGER
                        Reference.TriggerEffect(self, Effect, Data)
                    except:
                        ""
                # WITH THE EFFECTS APPLIED THEN IT SENDS THE RESPECTIVE DAMAGE AND STATUSES
                Damage = Data["Damage"]
                DamageTaken(self, Damage)
                for Effect in Data["Effects"]:
                    self.Effects.append(Effect)





                self.DamageTaken(DMG)


                Globals.MainWindow["MainW"].refresh()


def getEnemies(self, Reference, FullList, Signal):
    FileReference.getEnemies(self, FileReference, lst, "Initial")
    if Signal == "Initial":
        # lst = {"Enemies":[], "Encounters":[], "EliteEnemies":[], "EliteEncounters":[], "BossEncounters":[]}
        EnemiesList = [{"ID":"ThiefBandit0", "Origin":"BasicEnemies", "CR":0.5} , {"ID":"RangerBandit0", "Origin":"BasicEnemies", "CR":0.5}, {"ID":"WarriorBandit0", "Origin":"BasicEnemies", "CR":0.5}]
        for i in EnemiesList:
            FullList["Enemies"].append(i)

        EnemyObject = Enemy(Name, HP, EnemyID)

def getObject(self, EnemyID, ID):
    if EnemyID == "ThiefBandit0":
        Enemy = Enemy("Thief", 25, ID)
    return Enemy
