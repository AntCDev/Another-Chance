from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QTextCursor
import Globals
import random
import os
Log = Globals.Layouts["MainF"].Log

class Worker(QObject):
    def __init__(self, Func, Data, AnimationID, Cast, parent = None):
        super(Worker, self).__init__()
        self.Func = Func
        self.Data = Data
        self.AnimationID = AnimationID
        self.Cast = Cast
        self._isRunning = True

        ID = list(Globals.Threads.keys())[-1]
        self.ThreadID = ID

    finished = pyqtSignal()
    progress = pyqtSignal(int)
    ping = pyqtSignal()
    ping2 = pyqtSignal()

    def run(self):
        self.Func(self, self.AnimationID)

    def task(self):
        try:
            if self._isRunning:
                # print("Thread", hex(id(self.Data)))
                Globals.AnimationData[self.AnimationID]["Thread"] = self
                # Globals.BattleAniData["Thread"] = self
                self.Func(self.AnimationID, self.Cast)
        except Exception as e:
            Log(2, "ERROR THREAD TASK", e, self.Func, "BasicEnemies")

    def clean(self):
        Globals.AnimationData[AnimationID].pop(self.AnimationID)
        Globals.FinishedThreads.append(self.ThreadID)


    def stop(self):
        self._isRunning = False

def CleanThreads(self):
    lst = Globals.FinishedThreads
    try:
        for ThreadID in lst:
            Globals.Threads[ThreadID]["Worker"].stop()
            Globals.Threads[ThreadID]["Thread"].quit()
            Globals.Threads[ThreadID]["Thread"].wait()

            Globals.Threads.pop(ThreadID)
            Globals.FinishedThreads.remove(ThreadID)

            # if Globals.Threads[ThreadID]["Thread"].isFinished():
            #     Globals.Threads[ThreadID]["Thread"].quit()
            #     Globals.Threads[ThreadID]["Worker"].deleteLater()
            #     # Globals.Threads[ThreadID]["Thread"].deleteLater()
            #     Globals.Threads[ThreadID]["Thread"].deleteLater()
            #
            #     Globals.Threads.pop(ThreadID)
            #     Globals.FinishedThreads.remove(ThreadID)
            # else:
            #     print("Unfinished:", ThreadID)
    except Exception as e:
        Log(2, "ERROR CLEANING THREADS:", e)
def getAnimationID():
    try:
        ID = max(Globals.AnimationData.keys()) + 1
    except:
        ID = 0
    Globals.AnimationData[ID] = {}
    return ID




# import random
class Enemy:
    def __init__(self, Name, HP, EnemyID):
        print("Created")
        self.Name = Name
        self.MaxHP = HP
        self.HP = HP
        self.ID = EnemyID
        self.Shield = 12
        self.Mental = 150
        self.Status = "Alive"
        self.CanBeTargeted = 1
        self.Effects = {}
        self.Selected = 0
        self.Target = 0
        self.Attack = {}
        self.getIntention()
        ""

    def __del__(self):
        ""

    def DamageTaken(self, DMG):
        print("OHNOW")
        self.HP -= DMG
        if self.HP > 0:
            ""
        else:
            self.Status = "Dead"

        Globals.Layouts["BattleMenu"].Refresh()

    def ObjectWidget(self):
        TWidget = QWidget()
        # self.Enemy1.setGeometry(300,300,220,320)
        TWidget.setFixedSize(400,240)
        TWidget.setStyleSheet('''
        QWidget{
        border: 1px solid black;
        background-color:rgb(23, 23, 23);
        }
        ''')

        if self.CanBeTargeted != 0:
            if self.ID in list(Globals.BattleInfo["Enemies"].keys()):
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
                .QWidget
                {
                border: 1px solid black;
                border-color:rgb(23,23,23)
                }
                ''')
        else:
            TWidget.setStyleSheet('''
            QWidget{
            border: 1px solid black;
            background-color:rgb(23, 23, 23);
            }
            .QWidget
            {
            border: 3px solid black;
            border-color:rgb(80,35,35)
            }
            ''')

        # TWidget.mouseReleaseEvent = lambda event: self.events({"Type":"Targeting"})
        TWidget.mouseReleaseEvent = lambda event: self.EnemyClick()

        EnemyName = QPushButton(self.Name, TWidget, clicked = lambda: print("Name"))
        EnemyName.setFont(QFont('Segoe UI', 12))
        EnemyName.setGeometry(110,5,280,30)
        EnemyName.setStyleSheet('''
        QPushButton{
        border: 1px solid black;
        background : rgb(35, 35, 35);
        color:rgb(255, 255, 255)
        }
        ''')

        EnemyPortrait = QLabel(TWidget)
        EnemyPortrait.setGeometry(5, 5, 100, 100)

        labelHP = QLabel(TWidget)
        labelHP.setGeometry(110,40,90,30)
        labelHP.setText(f'''<p><span style=" font-weight:600; color:#ff0000;">HP: {self.HP}</span></p> ''')
        labelHP.setFont(QFont('Segoe UI', 10))
        labelHP.setStyleSheet('''
        QLabel{
            color:red;
            background-color:rgb(35,35,35);
            }
        ''')
        labelSHP1 = QLabel(TWidget)
        labelSHP1.setGeometry(110,77,18,25)
        labelSHP1.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')
        labelSHP2 = QLabel(TWidget)
        labelSHP2.setGeometry(128,77,18,25)
        labelSHP2.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')
        labelSHP3 = QLabel(TWidget)
        labelSHP3.setGeometry(146,77,18,25)
        labelSHP3.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')
        labelSHP4 = QLabel(TWidget)
        labelSHP4.setGeometry(164,77,18,25)
        labelSHP4.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')
        labelSHP5 = QLabel(TWidget)
        labelSHP5.setGeometry(182,77,18,25)
        labelSHP5.setStyleSheet('''QLabel{background-color:rgb(214, 0, 0) }''')


        labelSH = QLabel(TWidget)
        labelSH.setGeometry(205,40,90,30)
        labelSH.setText(f'''<p><span style=" font-weight:600;">SH: {self.Shield}</span></p> ''')
        labelSH.setFont(QFont('Segoe UI', 10))
        labelSH.setStyleSheet('''
        QLabel{
            color:rgb(150,150,150);
            background-color:rgb(35,35,35);
            }
        ''')
        labelSSH1 = QLabel(TWidget)
        labelSSH1.setGeometry(205,77,18,25)
        labelSSH1.setStyleSheet('''QLabel{background-color:rgb(150,150,150) }''')
        labelSSH2 = QLabel(TWidget)
        labelSSH2.setGeometry(223,77,18,25)
        labelSSH2.setStyleSheet('''QLabel{background-color:rgb(150,150,150) }''')
        labelSSH3 = QLabel(TWidget)
        labelSSH3.setGeometry(241,77,18,25)
        labelSSH3.setStyleSheet('''QLabel{background-color:rgb(150,150,150) }''')
        labelSSH4 = QLabel(TWidget)
        labelSSH4.setGeometry(259,77,18,25)
        labelSSH4.setStyleSheet('''QLabel{background-color:rgb(150,150,150) }''')
        labelSSH5 = QLabel(TWidget)
        labelSSH5.setGeometry(277,77,18,25)
        labelSSH5.setStyleSheet('''QLabel{background-color:rgb(150,150,150) }''')


        labelMT = QLabel(TWidget)
        labelMT.setGeometry(300,40,90,30)
        labelMT.setText(f'''<p><span style=" font-weight:600;">MT: {self.Mental}</span></p> ''')
        labelMT.setFont(QFont('Segoe UI', 10))
        labelMT.setStyleSheet('''
        QLabel{
            color:rgb(214, 0, 255);
            background-color:rgb(35,35,35);
            }
        ''')
        labelSMT1 = QLabel(TWidget)
        labelSMT1.setGeometry(300,77,18,25)
        labelSMT1.setStyleSheet('''QLabel{background-color:rgb(214, 0, 255) }''')
        labelSMT2 = QLabel(TWidget)
        labelSMT2.setGeometry(318,77,18,25)
        labelSMT2.setStyleSheet('''QLabel{background-color:rgb(214, 0, 255) }''')
        labelSMT3 = QLabel(TWidget)
        labelSMT3.setGeometry(336,77,18,25)
        labelSMT3.setStyleSheet('''QLabel{background-color:rgb(214, 0, 255) }''')
        labelSMT4 = QLabel(TWidget)
        labelSMT4.setGeometry(354,77,18,25)
        labelSMT4.setStyleSheet('''QLabel{background-color:rgb(214, 0, 255) }''')
        labelSMT5 = QLabel(TWidget)
        labelSMT5.setGeometry(372,77,18,25)
        labelSMT5.setStyleSheet('''QLabel{background-color:rgb(214, 0, 255) }''')


        labelActions = QLabel(TWidget)
        labelActions.setGeometry(5,110,390,75)
        Text = self.AttackText()
        # labelActions.setText('''<html><head/><body>Quick Attack:<br/><span style=" font-weight:600; color:#00ff7f;">Quick.</span> 5 x 2 to Chraum<br/><span style=" font-weight:600; color:#1e74ff;">2nd Line</span><br/><span style=" font-weight:600; color:#1e74ff;">3rd Line</span></body></html> ''')
        labelActions.setText(Text)
        labelActions.setFont(QFont('Segoe UI', 9))
        labelActions.setAlignment(Qt.AlignLeft)
        labelActions.setAlignment(Qt.AlignTop)
        labelActions.setStyleSheet('''
        QLabel{
            background-color:rgb(23,23,23);
            }
        ''')

        labelStatus = QLabel(TWidget)
        labelStatus.setGeometry(5,190,390,40)
        labelStatus.setAlignment(Qt.AlignLeft)
        labelStatus.setStyleSheet('''QLabel{background-color:rgb(214, 0, 255) }''')

        self.scrollEF = QScrollArea(TWidget)
        self.scrollEF.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollEF.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollEF.setGeometry(5,190,390,40)
        self.scrollEF.setStyleSheet('''
        QScrollArea{
        background-color:rgb(23, 23, 23);
        border: 1px solid black;
        border-right: none;
        border-left: none;
        ''')

        ### Draws the allies form on the left
        try:
            self.myformEF = QHBoxLayout()
            isEmpty = 1
            for Effect in self.Effects:
                self.Effects[Effect]["ID"]
                IconWidget = Globals.BattleInfo["EffectsDict"][self.Effects[Effect]["ID"]].getIcon(Effect, self)
                IconWidget.setFixedSize(40, 40)
                self.myformEF.addWidget(IconWidget)
                isEmpty = 0
            self.myformEF.setContentsMargins(0, 0, 0, 0)
            mygroupboxEF = QGroupBox()
            if isEmpty == 0:
                mygroupboxEF.setLayout(self.myformEF)
            self.scrollEF.setWidget(mygroupboxEF)
        except Exception as e:
            Log(2, "ERROR EnemyObject EFFECT ICON,", e, self)



        return TWidget

    def EnemyClick(self):
        try:
            if self.Selected == 1:
                if self.ID in list(Globals.BattleInfo["Enemies"].keys()):
                    Globals.BattleInfo["Enemies"].pop(self.ID)
                self.Selected = 0
            else:
                if self.CanBeTargeted != 0:
                    if self.ID not in list(Globals.BattleInfo["Enemies"].keys()):
                        Index = list(Globals.BattleObjects["Enemies"].keys()).index(self.ID)
                        Globals.BattleInfo["Enemies"][self.ID] = Index
                    self.Selected = 1
            Globals.Layouts["BattleMenu"].Refresh()
        except Exception as e:
            ""


    def AttackTrigger(self):
        try:
            Source = Globals.References[os.path.basename(__file__)[:-3]]
            Attack = self.Attack
            Target = self.Target
            Move = Attack["AttackID"]
            if Move == {}:
                return
            if Move == "Slash0":
                # SETTING INITIAL DATA FOR THE ANIMATIONS
                AnimationID = getAnimationID()
                Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
                Globals.AnimationData[AnimationID] = Data

                # TRIGGERING THE ATTACK
                Target = self.Target
                Parent = self.ID
                AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":self, "Damage":5, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack} }
                Globals.Layouts["BattleMenu"].CastAttack( AttackData )


                # CALLING FOR THE ANIMATION
                self.AttackAnimation(AnimationID, 0)
            elif Move == "Defend0":
                # SETTING INITIAL DATA FOR THE ANIMATIONS
                AnimationID = getAnimationID()
                Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
                Globals.AnimationData[AnimationID] = Data

                # TRIGGERING THE ATTACK
                Target = self.ID
                Parent = self.ID
                AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":self, "Damage":0, "Healing":0, "ShieldDamage":0, "Shield":5, "MentalDamage":0, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack} }
                Globals.Layouts["BattleMenu"].CastAttack( AttackData )


                # CALLING FOR THE ANIMATION
                self.AttackAnimation(AnimationID, 0)
            elif Move == "StrongAttack0":
                # SETTING INITIAL DATA FOR THE ANIMATIONS
                AnimationID = getAnimationID()
                Data = {"Targets":[], "MentalDamage":0, "MentalHealing":0, "Target":'', "Cast":0, "AttackID":Move, "DmgDealt":0, "Animation":[]}
                Globals.AnimationData[AnimationID] = Data

                # TRIGGERING THE ATTACK
                Target = self.Target
                Parent = self.ID
                AttackData = { "Target":Target, "Parent":Parent, "AttackID":Move, "Type":"Attack", "Flags":{ "Confirmation":1, "EffectsTrigger":1 }, "Source":self, "Damage":10, "Healing":0, "ShieldDamage":0, "Shield":0, "MentalDamage":0, "MentalHealing":0, "Effects":{}, "AnimationID":AnimationID, "OtherData":{"Attack":Attack} }
                Globals.Layouts["BattleMenu"].CastAttack( AttackData )

                # CALLING FOR THE ANIMATION
                self.AttackAnimation(AnimationID, 0)
        except Exception as e:
            Log(4, "ERROR ENEMY ATTACK TRIGGER", e, self)
    def AttackConfirmed(self, OriginalData, FinalData, Results):
        try:
            Attack = self.Attack
            Target = self.Target
            if Attack == {}:
                return
            if Attack["AttackID"] == "Slash0":
                if Results["DamageDealt"] > 0 or Results["ShieldDamage"] > 0:
                    AnimationID = FinalData["AnimationID"]
                    Target = Results["Target"]
                    Globals.AnimationData[AnimationID]["Target"] = Target
            elif Attack["AttackID"] == "Defend0":
                if Results["ShieldApplied"] > 0:
                    AnimationID = FinalData["AnimationID"]
                    Target = Results["Target"]
                    Globals.AnimationData[AnimationID]["Target"] = Target
            elif Attack["AttackID"] == "StrongAttack0":
                if Results["DamageDealt"] > 0 or Results["ShieldDamage"] > 0:
                    AnimationID = FinalData["AnimationID"]
                    Target = Results["Target"]
                    Globals.AnimationData[AnimationID]["Target"] = Target
        except Exception as e:
            Log(4, "ERROR ENEMY ATTACK CONFIRMED", e, self)
        return OriginalData, FinalData, Results
    def AttackAnimation(self, AnimationID, Cast):
        try:
            Data = Globals.AnimationData[AnimationID]
            try:
                if Data["Target"] in list(Globals.BattleObjects["Enemies"].keys()):
                    Type = "Enemies"
                elif Data["Target"] in list(Globals.BattleObjects["Allies"].keys()):
                    Type = "Allies"
            except:
                ""
            if Data["AttackID"] == "Defend0":
                if Cast == 0:
                    try:
                        ID = max(list(Globals.Threads.keys()))
                        ID += 1
                    except:
                        ID = 0
                    Globals.AnimationData[AnimationID]["ThreadID"] = ID
                    Cast = 1
                    Globals.Threads[ID] = {}
                    Globals.Threads[ID]["Thread"] = QThread()
                    Globals.Threads[ID]["Worker"] = Worker(self.AttackAnimation, Data, AnimationID, Cast)

                    Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                    Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                    Cast = 2
                    Globals.Threads[ID]["Worker"].ping.connect(lambda: self.AttackAnimation(AnimationID, Cast))

                    Globals.Threads[ID]["Thread"].start()

                elif Cast == 1:
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                elif Cast == 2:
                    Target = Globals.AnimationData[AnimationID]["Target"]
                    Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                    TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                    TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                    Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                    Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                    BRX = TLX + Width - 100
                    BRY = TLY + Height - 100

                    RN1 = random.randint(TLX, BRX)
                    RN2 = random.randint(TLY, BRY)
                    widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                    widget.setGeometry(RN1,RN2,100,100)
                    widget.show()
                    widget.raise_()
                    widget.setScaledContents(True)
                    widget.setStyleSheet('''
                    border: 0px solid black;
                    background-color: rgba(0,0,0,0%);
                    ''')
                    image = QImage("Resources/CombatResources/Shield1.png")
                    imagepix = QPixmap.fromImage(image)
                    widget.setPixmap(imagepix)
                    Globals.Layouts["BattleMenu"].Fade(widget)
            if Data["AttackID"] == "Slash0":
                if Cast == 0:
                    try:
                        ID = max(list(Globals.Threads.keys()))
                        ID += 1
                    except:
                        ID = 0
                    Globals.AnimationData[AnimationID]["ThreadID"] = ID
                    Cast = 1
                    Globals.Threads[ID] = {}
                    Globals.Threads[ID]["Thread"] = QThread()
                    Globals.Threads[ID]["Worker"] = Worker(self.AttackAnimation, Data, AnimationID, Cast)

                    Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                    Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                    Cast = 2
                    Globals.Threads[ID]["Worker"].ping.connect(lambda: self.AttackAnimation(AnimationID, Cast))

                    Globals.Threads[ID]["Thread"].start()

                elif Cast == 1:
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                elif Cast == 2:
                    Target = Globals.AnimationData[AnimationID]["Target"]
                    Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                    TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                    TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                    Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                    Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                    BRX = TLX + Width - 100
                    BRY = TLY + Height - 100

                    RN1 = random.randint(TLX, BRX)
                    RN2 = random.randint(TLY, BRY)
                    widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                    widget.setGeometry(RN1,RN2,100,100)
                    widget.show()
                    widget.raise_()
                    widget.setScaledContents(True)
                    widget.setStyleSheet('''
                    border: 0px solid black;
                    background-color: rgba(0,0,0,0%);
                    ''')
                    image = QImage("Resources/CombatResources/AttackEffect1.png")
                    imagepix = QPixmap.fromImage(image)
                    widget.setPixmap(imagepix)
                    Globals.Layouts["BattleMenu"].Fade(widget)
            if Data["AttackID"] == "StrongAttack0":
                if Cast == 0:
                    try:
                        ID = max(list(Globals.Threads.keys()))
                        ID += 1
                    except:
                        ID = 0
                    Globals.AnimationData[AnimationID]["ThreadID"] = ID
                    Cast = 1
                    Globals.Threads[ID] = {}
                    Globals.Threads[ID]["Thread"] = QThread()
                    Globals.Threads[ID]["Worker"] = Worker(self.AttackAnimation, Data, AnimationID, Cast)

                    Globals.Threads[ID]["Worker"].moveToThread(Globals.Threads[ID]["Thread"])
                    Globals.Threads[ID]["Thread"].started.connect(Globals.Threads[ID]["Worker"].task)

                    Cast = 2
                    Globals.Threads[ID]["Worker"].ping.connect(lambda: self.AttackAnimation(AnimationID, Cast))

                    Globals.Threads[ID]["Thread"].start()

                elif Cast == 1:
                    Globals.AnimationData[AnimationID]["Thread"].ping.emit()
                elif Cast == 2:
                    Target = Globals.AnimationData[AnimationID]["Target"]
                    Parent = Globals.BattleObjects[Type][Target]["Widget"].parent().parent().parent().parent()

                    TLX = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).x()
                    TLY = Globals.BattleObjects[Type][Target]["Widget"].mapTo(Parent, QPoint(0, 0)).y()

                    Width =  Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().width()
                    Height = Globals.BattleObjects[Type][Target]["Widget"].frameGeometry().height()
                    BRX = TLX + Width - 100
                    BRY = TLY + Height - 100

                    RN1 = random.randint(TLX, BRX)
                    RN2 = random.randint(TLY, BRY)
                    widget = QLabel(Globals.Layouts["BattleMenu"].GUI)
                    widget.setGeometry(RN1,RN2,100,100)
                    widget.show()
                    widget.raise_()
                    widget.setScaledContents(True)
                    widget.setStyleSheet('''
                    border: 0px solid black;
                    background-color: rgba(0,0,0,0%);
                    ''')
                    image = QImage("Resources/CombatResources/AttackEffect3.png")
                    imagepix = QPixmap.fromImage(image)
                    widget.setPixmap(imagepix)
                    Globals.Layouts["BattleMenu"].Fade(widget)
        except Exception as e:
            Log(3, "ERROR ENEMY ATTACK ANIMATION", e, self)
    def AttackText(self):
        try:
            Attack = self.Attack
            Target = self.Target
            if Attack == {}:
                return
            if Attack["AttackID"] == "Slash0":
                Text = f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>5</b></span> Damage to <span style="color:rgb(100,140,255);"><b>{Globals.BattleObjects["Allies"][self.Target]["Object"].Name}</b></span><br>
                </span></p>
                </body></html>
                '''
                return Text
            elif Attack["AttackID"] == "Defend0":
                Text = f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Gain <span style="color:red;"><b>5</b></span> Shield<br>
                </span></p>
                </body></html>
                '''
                return Text
            elif Attack["AttackID"] == "StrongAttack0":
                Text = f'''
                <html><head/><body>
                <p style="line-height:1.3"><span>
                Deal <span style="color:red;"><b>10</b></span> Damage to <span style="color:rgb(100,140,255);"><b>{Globals.BattleObjects["Allies"][self.Target]["Object"].Name}</b></span><br>
                </span></p>
                </body></html>
                '''
                return Text
        except Exception as e:
            Log(1, "ERROR ENEMY ATTACKTEXT", e, self)

    def CallToAction(self):
        self.AttackTrigger()
        self.getIntention()
    def getIntention(self):
        try:
            # GETS THE TARGET
            AvailableAllies = []
            for AllyID in Globals.BattleObjects["Allies"]:
                Ally = Globals.BattleObjects["Allies"][AllyID]["Object"]
                if Ally.Status == "Alive":
                    AvailableAllies.append(AllyID)
            if len(AvailableAllies) == 0:
                return
            Target = random.choice(AvailableAllies)
            self.Target = Target

            # GETS THE ATTACK
            AttacksList = [ {"AttackID":"Slash0", "Other":{}}, {"AttackID":"Defend0", "Other":{}}, {"AttackID":"StrongAttack0", "Other":{}} ]
            Attack = random.choice(AttacksList)
            self.Attack = Attack
        except Exception as e:
            Log(2, "ERROR ENEMY getIntention", e, self)



    def DamageRecieved(self, Damage, OriginalData, FinalData, Results):
        OrigianlHP = self.HP
        OriginalShield = self.Shield
        Shield = self.Shield
        if Shield != 0:
            if Shield >= Damage:
                Shield -= Damage
                self.Shield -= Damage
            else:
                Damage -= Shield
                self.Shield = 0

                self.HP -= Damage
        else:
            self.HP -= Damage

        if self.HP <= 0:
            self.Defeated()

        DamageTaken = OrigianlHP - self.HP
        ShieldDamage = OriginalShield - self.Shield
        return DamageTaken, ShieldDamage, OriginalData, FinalData, Results


    def Defeated(self):
        self.Status = "Defeated"
        self.HP = 0
        if self.Selected == 1:
            if self.ID in list(Globals.BattleInfo["Allies"].keys()):
                Globals.BattleInfo["Allies"].pop(self.ID)
            self.Selected = 0

    def HealingRecieved(self, Healing, OriginalData, FinalData, Results):
        self.HP += Healing
        HealingTaken = Healing
        return HealingTaken, OriginalData, FinalData, Results


    def MentalDamageRecieved(self, MentalDamage, OriginalData, FinalData, Results):
        OrigianlMental = self.Mental
        self.Mental -= MentalDamage
        if self.Mental < 0:
            self.Mental = 0

        MentalDamageTaken = OrigianlMental - self.Mental
        return MentalDamageTaken, OriginalData, FinalData, Results
    def MentalHealingRecieved(self, MentalHealing, OriginalData, FinalData, Results):
        OrigianlMental = self.Mental
        self.Mental += MentalHealing

        MentalDamageTaken = self.Mental - OrigianlMental
        return MentalHealingTaken, OriginalData, FinalData, Results


    def ShieldDamageRecieved(self, ShieldDamage, OriginalData, FinalData, Results):
        OrigianlShield = self.Shield
        self.Shield -= ShieldDamage
        if self.Shield < 0:
            self.Shield = 0

        ShieldDamageTaken = OrigianlShield - self.Shield
        return ShieldDamageTaken, OriginalData, FinalData, Results
    def ShieldRecieved(self, Shield, OriginalData, FinalData, Results):
        OrigianlShield = self.Shield
        self.Shield += Shield

        ShieldTaken = self.Shield - OrigianlShield
        return ShieldTaken, OriginalData, FinalData, Results


    def EffectRecieved(self, Effects, OriginalData, FinalData, Results):
        EffectsApplied = {}
        for Effect in Effects:
            if Effects[Effect]["Level"] >= 1:
                if Effect in list(self.Effects.keys()):
                    self.Effects[Effect]["Level"] += Effects[Effect]["Level"]
                else:
                    self.Effects[Effect] = Effects[Effect]
            EffectsApplied[Effect] = Effects[Effect]
        return EffectsApplied, OriginalData, FinalData, Results


def getEnemies(self, Reference, FullList, Signal):
    if Signal == "Initial":
        # lst = {"Enemies":[], "Encounters":{"Generic":[], "Custom":[]}, "EliteEnemies":[], "EliteEncounters":{"Generic":[], "Custom":[]}, "BossEncounters":{"Generic":[], "Custom":[]}}
        # EnemiesList = [{"ID":"ThiefBandit0", "Origin":"BasicEnemies", "CR":0.5} , {"ID":"RangerBandit0", "Origin":"BasicEnemies", "CR":0.5}, {"ID":"WarriorBandit0", "Origin":"BasicEnemies", "CR":0.5}]
        EnemiesList = [{"ID":"ThiefBandit0", "Origin":"BasicEnemies", "CR":0.5}]
        for i in EnemiesList:
            FullList["Enemies"].append(i)

        EliteEnemies = [{"ID":"EliteBandit0", "Origin":"BasicEnemies", "CR":1}]
        for i in EliteEnemies:
            FullList["EliteEnemies"].append(i)
    elif Signal == "Post":
        ""
    return FullList

def getObject(self, EnemyID, ID, IDCounter):
    if EnemyID == "ThiefBandit0":
        EnemyObject = Enemy(f"ThiefBandit{IDCounter}", 20, ID)
    elif EnemyID == "RangerBandit0":
        EnemyObject = Enemy(f"RangerBandit{IDCounter}", 15, ID)
    elif EnemyID == "WarriorBandit0":
        EnemyObject = Enemy(f"WarriorBandit{IDCounter}", 30, ID)

    elif EnemyID == "EliteBandit0":
        EnemyObject = Enemy(f"EliteBandit{IDCounter}", 30, ID)
    return EnemyObject

# getObject("ohj", "WarriorBandit0", 2)
