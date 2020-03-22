import sqlite3
#Create and check for connection
def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)
    return conn

#Show all data in the database
def select_all_data(conn,table_name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM {tn}".format(tn=table_name))
    rows = cur.fetchall()
    if rows:
        return rows
    else:
        return None

#Search a Name from the database
def search_name(conn,table_name):
    cur = conn.cursor()
    cur.execute("SELECT * FROM {tn}".format(tn=table_name))
    dat = cur.fetchall()
    names = []
    for i in dat:
        names.append(i[0])
    if names:
        return names
    else :
        return 0

#Search a Category from the database
def search_ctg(conn,table_name,ctg):
    if ctg == "BAT":
        cur = conn.cursor()
        cur.execute("SELECT * FROM {tn} where ctg=('BAT')".format(tn=table_name))
        dat = cur.fetchall()
        x= []
        for i in dat:
            x.append(i[0])
        if x:
            return x
        else :
            return 0
    elif ctg == "BOW":
        cur = conn.cursor()
        cur.execute("SELECT * FROM {tn} where ctg=('BWL')".format(tn=table_name))
        dat = cur.fetchall()
        x= []
        for i in dat:
            x.append(i[0])
        if x:
            return x
        else :
            return 0
    elif ctg == "AR":
        cur = conn.cursor()
        cur.execute("SELECT * FROM {tn} where ctg=('AR')".format(tn=table_name))
        dat = cur.fetchall()
        x= []
        for i in dat:
            x.append(i[0])
        if x:
            return x
        else :
            return 0
    elif ctg == "WK":
        cur = conn.cursor()
        cur.execute("SELECT * FROM {tn} where ctg=('WK')".format(tn=table_name))
        dat = cur.fetchall()
        x= []
        for i in dat:
            x.append(i[0])
        if x:
            return x
        else :
            return 0
    else:
        return 0


#Insert a data in the Database
def insert_data(conn,table_name,data):
    cur = conn.cursor()
    team_name = data[0]
    player_list = ' '.join(map(str, data[1]))
    team_points = data[2]
    try:
        cur.execute("INSERT INTO {tn} ({bn}, {cn1},{cn2}) VALUES ('{dat1}','{dat2}','{dat3}')".format(tn=table_name, bn="name", cn1="players",cn2="value",dat1=team_name,dat2=player_list,dat3=team_points))
        conn.commit()
        return 1
    except sqlite3.IntegrityError:
        return 0

#Delete a book from the database
def delete_team(conn, table_name, teamName):
    cur = conn.cursor()
    cur.execute("SELECT * FROM {tn} WHERE name='{bn}'".format(tn=table_name,bn=teamName))
    dat = cur.fetchall()
    if dat:
        cur.execute("DELETE FROM {tn} WHERE name='{bn}'".format(tn=table_name,bn=teamName))
        conn.commit()
        return 1
    else :
        return 0

#Module Utility Functions for Score

def bat_score(x):
    #Sorting Data according to Column
    points = 0
    runs  = x[1]
    fours = x[3]
    sixes = x[4]
    balls = x[2]
    field = x[9] + x[10] + x[11] + x[6]
    if balls != 0:
        strike_rate = float((runs/balls)*100)
    else:
        strike_rate = 0
    if runs > 100:
        points = 15 + int(runs/2)
        points = points + fours + sixes*2
        if strike_rate > 100:
            points+=6
        elif strike_rate > 80:
            points+=2
    elif runs > 50:
        points = 5 + int(runs/2)
        points = points + fours + sixes*2
        if strike_rate > 100:
            points+=6
        elif strike_rate > 80:
            points+=2
    else:
        points = int(runs/2)
        points = points + fours + sixes*2
        if strike_rate > 100:
            points+=6
        elif strike_rate > 80:
            points+=2
    if field > 0:
        points += field*10
    return points

def bowl_score(x):
    #Sorting Data According to Column
    points = 0
    wkts  = x[8]
    overs = int(x[5]/6)
    runs = x[7]
    field = x[9] + x[10] + x[11] + x[6]
    if overs != 0:
        economy_rate = float(runs/overs)
    else:
        economy_rate = 0
    if wkts >= 5:
        points+= wkts*10 +15
        if economy_rate <= 2:
            points += 21
        elif economy_rate <= 3.5:
            points +=11
        elif economy_rate <= 4.5:
            points +=4
    elif wkts >=3:
        points+= wkts*10 +5
        if economy_rate <= 2:
            points += 21
        elif economy_rate <= 3.5:
            points +=11
        elif economy_rate <= 4.5:
            points +=4
    else :
        points+= wkts*10
        if economy_rate <= 2:
            points += 21
        elif economy_rate <= 3.5:
            points +=11
        elif economy_rate <= 4.5:
            points +=4
    if field > 0:
        points += field*10
    return points