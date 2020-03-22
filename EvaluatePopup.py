
from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
import driver as d
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "fantasy_cricket.db")

match = "match"
stats = "stats"
teams = "teams"

connection = d.create_connection(db_path)

class Ui_MainWindow2(object):
    def setup(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(665, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.Head_Label_2 = QtWidgets.QLabel(self.centralwidget)
        self.Head_Label_2.setObjectName("Head_Label_2")
        self.horizontalLayout_8.addWidget(self.Head_Label_2)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_8)
        spacerItem2 = QtWidgets.QSpacerItem(17, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.TeamDropDown = QtWidgets.QComboBox(self.centralwidget)
        self.TeamDropDown.setMinimumSize(QtCore.QSize(150, 30))
        self.TeamDropDown.setObjectName("TeamDropDown")
        self.horizontalLayout_7.addWidget(self.TeamDropDown)
        spacerItem4 = QtWidgets.QSpacerItem(168, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem4)
        self.MatchDropDown = QtWidgets.QComboBox(self.centralwidget)
        self.MatchDropDown.setMinimumSize(QtCore.QSize(150, 30))
        self.MatchDropDown.setObjectName("MatchDropDown")
        self.horizontalLayout_7.addWidget(self.MatchDropDown)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_5.addWidget(self.line)
        spacerItem6 = QtWidgets.QSpacerItem(15, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_5.addItem(spacerItem6)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem7)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.PlayerList = QtWidgets.QListWidget(self.centralwidget)
        self.PlayerList.setMinimumSize(QtCore.QSize(200, 0))
        self.PlayerList.setObjectName("PlayerList")
        self.verticalLayout_3.addWidget(self.PlayerList)
        self.horizontalLayout_6.addLayout(self.verticalLayout_3)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem8)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Team_Points_2 = QtWidgets.QHBoxLayout()
        self.Team_Points_2.setObjectName("Team_Points_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.Team_Points_2.addWidget(self.label_5)
        self.TotalPointsNo = QtWidgets.QLabel(self.centralwidget)
        self.TotalPointsNo.setObjectName("TotalPointsNo")
        self.Team_Points_2.addWidget(self.TotalPointsNo)
        self.verticalLayout_4.addLayout(self.Team_Points_2)
        self.PointsList = QtWidgets.QListWidget(self.centralwidget)
        self.PointsList.setObjectName("PointsList")
        self.verticalLayout_4.addWidget(self.PointsList)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem9)
        self.verticalLayout_5.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.Calculate_Score = QtWidgets.QPushButton(self.centralwidget)
        self.Calculate_Score.setMinimumSize(QtCore.QSize(150, 30))
        self.Calculate_Score.setObjectName("Calculate_Score")
        self.horizontalLayout_5.addWidget(self.Calculate_Score)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 665, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.renderTeamDropDown()
        self.renderMatchDropDown()
        #Connect CalculateButton

        self.Calculate_Score.clicked.connect(lambda: self.calculateScoreBtn())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Evaluate Window"))
        self.Head_Label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Evaluate the Performance of you Fantasy Team</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Players</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Points</span></p></body></html>"))
        self.TotalPointsNo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#0000ff;\">##</span></p></body></html>"))
        self.Calculate_Score.setText(_translate("MainWindow", "Calculate Score"))
    
    def getColData(self,data,col):
        reqData = []
        for i in data:
            reqData.append(i[col])
        return reqData

    def renderTeamDropDown(self):
        _translate = QtCore.QCoreApplication.translate
        data = d.select_all_data(connection,"teams")
        teams = self.getColData(data,0)
        count = 0
        for i in teams:
            self.TeamDropDown.addItem("")
            self.TeamDropDown.setItemText(count,_translate("MainWindow", i))
            count += 1
    #Method to Render Drop Down Menu
    def renderMatchDropDown(self):
        _translate = QtCore.QCoreApplication.translate
        cursor = connection.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        data = cursor.fetchall()
        filtered_data = self.getColData(data,0)
        matchList = []
        for i in filtered_data:
            if not i.find("match"):
                matchList.append(i)
        count = 0
        for i in matchList:
            self.MatchDropDown.addItem("")
            self.MatchDropDown.setItemText(count,_translate("MainWindow", i))
            count += 1    

    def renderPlayerList(self,List):
        self.PlayerList.clear()
        _translate = QtCore.QCoreApplication.translate
        for i in range(0,len(List)):
            item = QtWidgets.QListWidgetItem()
            self.PlayerList.addItem(item)
        count = 0
        for i in List:
            item = self.PlayerList.item(count)
            item.setText(_translate("MainWindow", i))
            count+=1
    #Method to Render The points List
    def renderPointsList(self,List):
        self.PointsList.clear()
        _translate = QtCore.QCoreApplication.translate
        for i in range(0,len(List)):
            item = QtWidgets.QListWidgetItem()
            self.PointsList.addItem(item)
        count = 0
        totalPoint = 0
        for i in List:
            item = self.PointsList.item(count)
            item.setText(_translate("MainWindow", str(i)))
            count+=1
            totalPoint += i
        self.TotalPointsNo.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#0000ff;\">"+str(totalPoint)+"</span></p></body></html>"))
    #Methid to Fetch Players
    def teamPlayerList(self, teamName):
        data = d.select_all_data(connection,"teams")
        players = ""
        for i in data:
            if i[0] == teamName:
                players = i[1]
        playerList = list(players.split(" "))
        return playerList
    #Method to Get Team Points
    def teamPointList(self,List,match):
        Match_List = d.select_all_data(connection,match)
        Stat_List = d.select_all_data(connection,"stats")
        Point_List = []
        for data in List:
            for i in Match_List:
                    if i[0] == data:
                        for j in Stat_List:
                            if j[0] == data:
                                point = d.bat_score(i)
                                point += d.bowl_score(i)
                                Point_List.append(point)
        return Point_List
    #Method to run on Click of Calculate Button
    def calculateScoreBtn(self):
        team = self.TeamDropDown.currentText()
        match = self.MatchDropDown.currentText()
        teamPlayerList = self.teamPlayerList(team)
        self.renderPlayerList(teamPlayerList)
        teamPointList = self.teamPointList(teamPlayerList,match)
        self.renderPointsList(teamPointList)
        
    #General Fucntion to Display Message Popups
    def message_popup(self,message,additionalInfo=''):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setWindowIcon(QIcon("||"))
        msg.setText(message)
        msg.setInformativeText(additionalInfo)
        msg.setWindowTitle("Attention")
        msg.exec_()
    