

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sqlite3
#Defined Modules !!IMPORTANT!!
import driver as d
import EvaluatePopup as popup
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "fantasy_cricket.db")

#Sqlite Configuration

filename = "fantasy_cricket.db"
match = "match"
stats = "stats"
teams = "teams"
connection = d.create_connection(db_path)


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    #Active UI Global Data List
    player_stat_list = []
    player_team_list = []
    player_match_stat = []
    point_table = []
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(654, 492)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setMaximumSize(QtCore.QSize(636, 16777215))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.Top_Header = QtWidgets.QFrame(self.frame_4)
        self.Top_Header.setGeometry(QtCore.QRect(20, 20, 611, 81))
        self.Top_Header.setAutoFillBackground(False)
        self.Top_Header.setStyleSheet("background: qlineargradient(spread:pad, x1:1, y1:0.006, x2:1, y2:0, stop:0 rgba(196, 196, 196, 255), stop:1 rgba(255, 255, 255, 255));\n"
"border-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"")
        self.Top_Header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Top_Header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Top_Header.setObjectName("Top_Header")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Top_Header)
        self.verticalLayout.setObjectName("verticalLayout")
        self.your_selections = QtWidgets.QLabel(self.Top_Header)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.your_selections.setFont(font)
        self.your_selections.setObjectName("your_selections")
        self.verticalLayout.addWidget(self.your_selections)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.Info_Bar = QtWidgets.QHBoxLayout()
        self.Info_Bar.setObjectName("Info_Bar")
        self.Batsmen = QtWidgets.QHBoxLayout()
        self.Batsmen.setObjectName("Batsmen")
        self.BAT = QtWidgets.QLabel(self.Top_Header)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BAT.setFont(font)
        self.BAT.setObjectName("BAT")
        self.Batsmen.addWidget(self.BAT)
        self.BAT_NO = QtWidgets.QLabel(self.Top_Header)
        self.BAT_NO.setTextFormat(QtCore.Qt.RichText)
        self.BAT_NO.setObjectName("BAT_NO")
        self.Batsmen.addWidget(self.BAT_NO)
        self.Info_Bar.addLayout(self.Batsmen)
        self.AllRounder = QtWidgets.QHBoxLayout()
        self.AllRounder.setObjectName("AllRounder")
        self.AR = QtWidgets.QLabel(self.Top_Header)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.AR.setFont(font)
        self.AR.setObjectName("AR")
        self.AllRounder.addWidget(self.AR)
        self.AR_NO = QtWidgets.QLabel(self.Top_Header)
        self.AR_NO.setObjectName("AR_NO")
        self.AllRounder.addWidget(self.AR_NO)
        self.Info_Bar.addLayout(self.AllRounder)
        self.WicketKeeper = QtWidgets.QHBoxLayout()
        self.WicketKeeper.setObjectName("WicketKeeper")
        self.WK = QtWidgets.QLabel(self.Top_Header)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.WK.setFont(font)
        self.WK.setObjectName("WK")
        self.WicketKeeper.addWidget(self.WK)
        self.WK_NO = QtWidgets.QLabel(self.Top_Header)
        self.WK_NO.setObjectName("WK_NO")
        self.WicketKeeper.addWidget(self.WK_NO)
        self.Info_Bar.addLayout(self.WicketKeeper)
        self.Bowlers = QtWidgets.QHBoxLayout()
        self.Bowlers.setObjectName("Bowlers")
        self.BOW = QtWidgets.QLabel(self.Top_Header)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.BOW.setFont(font)
        self.BOW.setObjectName("BOW")
        self.Bowlers.addWidget(self.BOW)
        self.BOW_NO = QtWidgets.QLabel(self.Top_Header)
        self.BOW_NO.setObjectName("BOW_NO")
        self.Bowlers.addWidget(self.BOW_NO)
        self.Info_Bar.addLayout(self.Bowlers)
        self.verticalLayout.addLayout(self.Info_Bar)
        self.verticalLayout_3.addWidget(self.Top_Header)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.Points_Used = QtWidgets.QFrame(self.frame_4)
        self.Points_Used.setGeometry(QtCore.QRect(310, 110, 291, 311))
        self.Points_Used.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Points_Used.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Points_Used.setObjectName("Points_Used")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Points_Used)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Points_Used_2 = QtWidgets.QHBoxLayout()
        self.Points_Used_2.setObjectName("Points_Used_2")
        self.PointUsed = QtWidgets.QLabel(self.Points_Used)
        self.PointUsed.setObjectName("PointUsed")
        self.Points_Used_2.addWidget(self.PointUsed)
        self.Point_Used_No = QtWidgets.QLabel(self.Points_Used)
        self.Point_Used_No.setObjectName("Point_Used_No")
        self.Points_Used_2.addWidget(self.Point_Used_No)
        self.verticalLayout_4.addLayout(self.Points_Used_2)
        self.Main_Body_Used = QtWidgets.QVBoxLayout()
        self.Main_Body_Used.setObjectName("Main_Body_Used")
        self.Team = QtWidgets.QHBoxLayout()
        self.Team.setObjectName("Team")
        self.Team_Name_Value = QtWidgets.QLabel(self.Points_Used)
        self.Team_Name_Value.setObjectName("Team_Name_Value")
        self.Main_Body_Used.addLayout(self.Team)
        self.Player_List_Team = QtWidgets.QListWidget(self.Points_Used)
        self.Player_List_Team.setObjectName("Player_List_Team")
        self.Main_Body_Used.addWidget(self.Player_List_Team)
        self.verticalLayout_4.addLayout(self.Main_Body_Used)
        self.Points_Table = QtWidgets.QFrame(self.frame_4)
        self.Points_Table.setGeometry(QtCore.QRect(20, 110, 276, 311))
        self.Points_Table.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Points_Table.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Points_Table.setObjectName("Points_Table")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.Points_Table)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.Points_Available = QtWidgets.QHBoxLayout()
        self.Points_Available.setObjectName("Points_Available")
        self.Points_Avail = QtWidgets.QLabel(self.Points_Table)
        self.Points_Avail.setObjectName("Points_Avail")
        self.Points_Available.addWidget(self.Points_Avail)
        self.Points_Avail_No = QtWidgets.QLabel(self.Points_Table)
        self.Points_Avail_No.setObjectName("Points_Avail_No")
        self.Points_Available.addWidget(self.Points_Avail_No)
        self.verticalLayout_2.addLayout(self.Points_Available)
        self.Choice_Radio = QtWidgets.QHBoxLayout()
        self.Choice_Radio.setObjectName("Choice_Radio")
        self.BAT_2 = QtWidgets.QRadioButton(self.Points_Table)
        self.BAT_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.BAT_2.setObjectName("BAT_2")
        self.Choice_Radio.addWidget(self.BAT_2)
        self.BOW_2 = QtWidgets.QRadioButton(self.Points_Table)
        self.BOW_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.BOW_2.setObjectName("BOW_2")
        self.Choice_Radio.addWidget(self.BOW_2)
        self.AR_2 = QtWidgets.QRadioButton(self.Points_Table)
        self.AR_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.AR_2.setObjectName("AR_2")
        self.Choice_Radio.addWidget(self.AR_2)
        self.WK_2 = QtWidgets.QRadioButton(self.Points_Table)
        self.WK_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.WK_2.setObjectName("WK_2")
        self.Choice_Radio.addWidget(self.WK_2)
        self.verticalLayout_2.addLayout(self.Choice_Radio)
        self.Player_List = QtWidgets.QListWidget(self.Points_Table)
        self.Player_List.setObjectName("Player_List")
        self.verticalLayout_2.addWidget(self.Player_List)
        self.horizontalLayout.addWidget(self.Points_Table)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.Points_Used = QtWidgets.QFrame(self.frame_4)
        self.Points_Used.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Points_Used.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Points_Used.setObjectName("Points_Used")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.Points_Used)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Points_Used_2 = QtWidgets.QHBoxLayout()
        self.Points_Used_2.setObjectName("Points_Used_2")
        self.PointUsed = QtWidgets.QLabel(self.Points_Used)
        self.PointUsed.setObjectName("PointUsed")
        self.Points_Used_2.addWidget(self.PointUsed)
        self.Point_Used_No = QtWidgets.QLabel(self.Points_Used)
        self.Point_Used_No.setObjectName("Point_Used_No")
        self.Points_Used_2.addWidget(self.Point_Used_No)
        self.verticalLayout_4.addLayout(self.Points_Used_2)
        self.Main_Body_Used = QtWidgets.QVBoxLayout()
        self.Main_Body_Used.setObjectName("Main_Body_Used")
        self.Team = QtWidgets.QHBoxLayout()
        self.Team.setObjectName("Team")
        self.Team_Name_Label = QtWidgets.QLabel(self.Points_Used)
        self.Team_Name_Label.setObjectName("Team_Name_Label")
        self.Team.addWidget(self.Team_Name_Label)
        self.Team_Name = QtWidgets.QLineEdit(self.Points_Used)
        self.Team_Name.setObjectName("Team_Name")
        self.Team.addWidget(self.Team_Name)
        self.Main_Body_Used.addLayout(self.Team)
        self.Main_Body_Used.addWidget(self.Player_List_Team)
        self.verticalLayout_4.addLayout(self.Main_Body_Used)
        self.horizontalLayout.addWidget(self.Points_Used)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.gridLayout.addWidget(self.frame_4, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 654, 21))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setAutoFillBackground(False)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        #Radio Buttons Functionality
        self.BAT_2.toggled.connect(lambda: self.toggle_radio(self.BAT_2.text(),self.player_stat_list))
        self.BOW_2.toggled.connect(lambda: self.toggle_radio(self.BOW_2.text(),self.player_stat_list))
        self.AR_2.toggled.connect(lambda: self.toggle_radio(self.AR_2.text(),self.player_stat_list))
        self.WK_2.toggled.connect(lambda: self.toggle_radio(self.WK_2.text(),self.player_stat_list))
        #Window_Menu Fucntions
        self.actionNEW_Team.triggered.connect(lambda: self.newMenuButton())
        self.actionEVALUATE_Team.triggered.connect(lambda: self.evaluatePopup())
        self.actionSAVE_Team.triggered.connect(lambda: self.saveMenuButton())
        self.actionOPEN_Team.triggered.connect(lambda: self.openMenuButton())
       
        #List Transaction Fucntions
        self.Player_List.doubleClicked.connect(lambda : self.PlayerListClick(self.Player_List.currentItem(),self.player_stat_list))
        self.Player_List_Team.doubleClicked.connect(lambda: self.SelectedListClick(self.Player_List_Team.currentItem(),self.player_team_list))
        self.retranslateUi(MainWindow)
        self.setPoints("####","####")
        self.setSelections("##","##","##","##")
        self.point_table.append(0)
        self.point_table.append(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    
    #Defined Functions
    #Open a new team
    def newMenuButton(self):
        self.player_stat_list = []
        self.player_team_list = []
        self.player_match_stat = []
        self.point_table = []
        self.point_table.append(1000)
        self.point_table.append(0)
        self.setPoints(self.point_table[0],self.point_table[1])
        self.setSelections(00,00,00,00)
        self.render_Player_List([])
        self.render_Selected_Player([])
        self.Team_Name.setText("")
        self.Team_Name.setPlaceholderText("Enter Team Name Here")
        self.player_stat_list = d.select_all_data(connection,"stats")
        self.player_match_stat = d.select_all_data(connection,"match")
        self.check_toggled()
        
    #Save Current Team in GUI
    def saveMenuButton(self):
        Table_data = []
        if not len(self.getName(self.player_team_list)):
            self.message_popup("Empty Teams Cannot be Added !!!")
            return
        if self.Team_Name.text() == "":
            self.message_popup("Enter Team Name !!!")
            return 
        Table_data.append(self.Team_Name.text())
        Table_data.append(self.getName(self.player_team_list))
        Table_data.append(self.point_table[1])
        res = d.insert_data(connection,"teams",Table_data)
        if not res :
            self.message_popup("Team Already Exists Try Different Name!!!!!")
        else :
            self.message_popup("Team Successfully Added")
            self.newMenuButton()
    #Open a Team from Saved Teams
    def openMenuButton(self):   
        dialogBox = QtWidgets.QDialog()
        dialogBox.setMaximumHeight(100)
        dialogBox.setMaximumWidth(200)
        dialogBox.setMinimumHeight(100)
        dialogBox.setMinimumWidth(200)
        dialogBox.setWindowTitle("Open a Team")
        
        OpenButton = QtWidgets.QPushButton("Open Team",dialogBox)
        OpenButton.move(60,50)
        TeamDropDown = QtWidgets.QComboBox(dialogBox)
        TeamDropDown.move(30,10)
        # Data for Dropdwon Menu
        _translate = QtCore.QCoreApplication.translate
        data = d.select_all_data(connection,"teams")
        teams = []
        if data:
            for i in data:
                teams.append(i[0])
        else:
            self.message_popup("No Team Found Try Adding a Team First !!")
            return

        count = 0
        for i in teams:
            TeamDropDown.addItem("")
            TeamDropDown.setItemText(count,_translate("MainWindow", i))
            count += 1
        #Button Click Fucntionality
        OpenButton.clicked.connect(lambda: self.OpenTeamClick(TeamDropDown, dialogBox))

        dialogBox.setWindowModality(Qt.ApplicationModal)
        dialogBox.exec_()
    #Adds Relevent data on Poening the team and Update GUI  
    def OpenTeamClick(self,Dropdown, dialogBox):
        self.player_stat_list = []
        self.player_team_list = []
        self.player_match_stat = []
        self.point_table = []

        #Initializing Data Lists from Match and Stats table
        self.player_stat_list = d.select_all_data(connection,"stats")
        self.player_match_stat = d.select_all_data(connection,"match")
        team = Dropdown.currentText()
        dialogBox.close()
        teamsData = d.select_all_data(connection,"teams")
        totalPlayers = []
        teamPlayers = []
        totalPoints = 0
        for i in teamsData:
            if i[0] == team:
                teamPlayers = list(i[1].split(" "))
                totalPoints = i[2]
                break
        self.point_table.append(1000 - int(totalPoints))
        self.point_table.append(int(totalPoints))
        self.setPoints(self.point_table[0],self.point_table[1])
        self.Team_Name.setText(team)

        player_stat_list = []
        for i in teamPlayers:
            for j in self.player_stat_list:
                if i == j[0]:
                    self.player_team_list.append(j)

        self.player_stat_list = list(set(self.player_stat_list) - set(self.player_team_list))
        self.render_Player_List(self.getName(self.player_stat_list))
        self.render_Selected_Player(self.getName(self.player_team_list))
        self.check_toggled()
        self.checkYourSelection(self.player_team_list)
        #Deleting team After Opening
        d.delete_team(connection,"teams",team)
    #Fucntion to Calculate Points of Players
    def calcPoint(self,data,Stat_List,Match_List,sign):
        if sign == "+":
            for i in Match_List:
                if i[0] == data:
                    for j in Stat_List:
                        if j[0] == data:
                            point = d.bat_score(i)
                            point += d.bowl_score(i)
                            self.point_table[0] -= point
                            self.point_table[1] += point
                            self.setPoints(self.point_table[0],self.point_table[1])
        elif sign == "-":
            for i in Match_List:
                if i[0] == data:
                    for j in Stat_List:
                        if j[0] == data:
                            point = d.bat_score(i)
                            point += d.bowl_score(i)
                            self.point_table[0] += point
                            self.point_table[1] -= point
                            self.setPoints(self.point_table[0],self.point_table[1])
    #Get Names of all Players from Man List
    def getName(self, List):
        name_list = []
        for i in List:
            name_list.append(i[0])
        return name_list
    #Wicket Keeper Exception to PopUp and Stop GUI
    def wicketKeeperException(self,item,List):
        count = 0
        itemx = ""
        for j in self.player_team_list:
            if j[6] == "WK":
                count += 1
        for j in List:
            if j[0] == item.text():
                itemx = j
        if count >= 1 and itemx[6] == "WK":
            self.message_popup("You cannot have More than 1 WicketKeeper","Error Violation of Rules")
            return 1 
        return 0
    #To check if selected Players Exceeds 1000 Points
    def ExcessPointsException(self,player, List):
        for i in List:
            if i[0] == player:
                playerPoint = d.bat_score(i)
                playerPoint += d.bowl_score(i)
        if self.point_table[1]+playerPoint > 1000:
            return 1
        else:
            return 0
    #Method for functionality when a item is Double clicked in the Player List 
    def PlayerListClick(self, item, List):
        NewList = []
        NewItem = []
        if self.wicketKeeperException(item,List):
            return
        if self.ExcessPointsException(item.text(),self.player_match_stat):
            self.message_popup("Can't Have Team Value Greater Than 1000 Points !!","Game Rules Violation")
            return 
        
        #Commiting Data to main Data List
        for i in List:
            if i[0] != item.text():
                NewList.append(i)
            else:
                self.player_team_list.append(i)

        # print(NewItem)
        NewItem = self.getName(self.player_team_list)
        self.calcPoint(item.text(),self.player_stat_list,self.player_match_stat,"+")
        self.render_Selected_Player(NewItem)
        self.player_stat_list = NewList
        name_list = self.getName(self.player_stat_list)
        self.checkYourSelection(self.player_team_list)
        self.check_toggled()
    #Methods to Update GUI when a Player is Clicked in the Selected Player List
    def SelectedListClick(self,item,List):
        NewList = []
        newNameList = []
        #Commiting Data to main Data List
        for i in List:
            if i[0] != item.text():
                NewList.append(i)
            else:
                self.player_stat_list.append(i)
        
        newNameList = self.getName(NewList)
        self.calcPoint(item.text(),self.player_stat_list,self.player_match_stat,"-")
        self.player_team_list = NewList
        self.render_Selected_Player(newNameList)
        self.checkYourSelection(self.player_team_list)
        self.check_toggled()
    #Method to Check for Radio Buttons to Update GUI
    def check_toggled(self):
        if self.BAT_2.isChecked():
            self.toggle_radio("BAT",self.player_stat_list)
        elif self.BOW_2.isChecked():
            self.toggle_radio("BOW",self.player_stat_list)
        elif self.AR_2.isChecked():
            self.toggle_radio("AR",self.player_stat_list)
        elif self.WK_2.isChecked():
            self.toggle_radio("WK",self.player_stat_list)
        else:
            data = self.getName(self.player_stat_list)
            self.render_Player_List(data)
    #Method to Radio Buttons for category seperation
    def toggle_radio(self,text,players):
        self.Player_List.clear()
        if text == "BAT":
            data = []
            for i in players:
                if i[6] == "BAT":
                    data.append(i[0])
            self.render_Player_List(data)
        elif text == "BOW":
            data = []
            for i in players:
                if i[6] == "BWL":
                    data.append(i[0])
            self.render_Player_List(data)
        elif text == "AR":
            data = []
            for i in players:
                if i[6] == "AR":
                    data.append(i[0])
            self.render_Player_List(data)
        elif text == "WK":
            data = []
            for i in players:
                if i[6] == "WK":
                    data.append(i[0])
            self.render_Player_List(data)
    #Method to check for selected Player and Update Your Selection Header
    def checkYourSelection(self,List):
        bat = 0
        bow = 0
        ar = 0
        wk = 0
        for i in List:
            if i[6] == "BAT":
                bat+=1
            elif i[6] == "BWL":
                bow+=1
            elif i[6] == "AR":
                ar+=1
            elif i[6] == "WK":
                wk+=1
        self.setSelections(bat,bow,ar,wk)
    #Method top Render Player List
    def render_Player_List(self,List):
        self.Player_List.clear()
        _translate = QtCore.QCoreApplication.translate
        for i in range(0,len(List)):
            item = QtWidgets.QListWidgetItem()
            self.Player_List.addItem(item)
        count = 0
        for i in List:
            item = self.Player_List.item(count)
            item.setText(_translate("MainWindow", i))
            count+=1
    #Method to Render Selected Player List
    def render_Selected_Player(self,List):
        self.Player_List_Team.clear()
        _translate = QtCore.QCoreApplication.translate
        for i in range(0,len(List)):
            item = QtWidgets.QListWidgetItem()
            self.Player_List_Team.addItem(item)
        count = 0
        for i in List:
            item = self.Player_List_Team.item(count)
            item.setText(_translate("MainWindow", i))
            count+=1
    #Methods to Create and call a Evaluate Popup Object
    def evaluatePopup(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = popup.Ui_MainWindow2()
        self.ui.setup(self.window)
        self.window.show()
    #General Function to Create Popup 
    def message_popup(self,message,additionalInfo=''):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Warning)
        msg.setWindowIcon(QIcon("||"))
        msg.setText(message)
        msg.setInformativeText(additionalInfo)
        msg.setWindowTitle("Attention")
        msg.exec_()
    #Method to Set Points in Labels
    def setPoints(self, valueA, valueU):
        _translate = QtCore.QCoreApplication.translate
        setValAvail = "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#0055ff;\">"+str(valueA)+"</span></p></body></html>"
        self.Points_Avail_No.setText(_translate("MainWindow", setValAvail))
        setValUsed = "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#0055ff;\">"+str(valueU)+"</span></p></body></html>"
        self.Point_Used_No.setText(_translate("MainWindow", setValUsed))
    #Method to Set Values of Player category Label
    def setSelections(self,bat,bow,ar,wk):
        _translate = QtCore.QCoreApplication.translate
        setBat =  "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#0055ff;\">"+str(bat)+"</span></p></body></html>"
        setBow =  "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#0055ff;\">"+str(bow)+"</span></p></body></html>"
        setAr =  "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#0055ff;\">"+str(ar)+"</span></p></body></html>"
        setWk =  "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#0055ff;\">"+str(wk)+"</span></p></body></html>"
        self.BAT_NO.setText(_translate("MainWindow",setBat))
        self.WK_NO.setText(_translate("MainWindow", setWk))
        self.AR_NO.setText(_translate("MainWindow", setAr))
        self.BOW_NO.setText(_translate("MainWindow", setBow))

    #Auto Genererated Method from pyuic5
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fantasy Cricket Team Builder"))
        self.your_selections.setText(_translate("MainWindow", "Your Selections"))
        self.BAT.setText(_translate("MainWindow", "Batsmen (BAT) "))
        self.BAT_NO.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#0055ff;\">##</span></p></body></html>"))
        self.AR.setText(_translate("MainWindow", "AllRounders (AR) "))
        self.AR_NO.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#0055ff;\">##</span></p></body></html>"))
        self.WK.setText(_translate("MainWindow", "WicketKeeper (WK) "))
        self.WK_NO.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#0055ff;\">##</span></p></body></html>"))
        self.BOW.setText(_translate("MainWindow", "Bowlers (BOW )"))
        self.BOW_NO.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#0055ff;\">##</span></p></body></html>"))
        self.PointUsed.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Points Used: </span></p></body></html>"))
        self.Point_Used_No.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#0055ff;\">##</span></p></body></html>"))
        self.Team_Name_Label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Team Name:</span></p></body></html>"))
        self.Team_Name.setPlaceholderText(_translate("MainWindow", "Enter Team Name"))
        self.Points_Avail.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:10pt;\">Points Available: </span></p></body></html>"))
        self.Points_Avail_No.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600; color:#0055ff;\">##</span></p></body></html>"))
        self.BAT_2.setText(_translate("MainWindow", "BAT"))
        self.BOW_2.setText(_translate("MainWindow", "BOW"))
        self.AR_2.setText(_translate("MainWindow", "AR"))
        self.WK_2.setText(_translate("MainWindow", "WK"))
        __sortingEnabled = self.Player_List.isSortingEnabled()
        self.Player_List.setSortingEnabled(False)
        
        self.Player_List.setSortingEnabled(__sortingEnabled)
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))

#Main Method to Start Application Process
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())