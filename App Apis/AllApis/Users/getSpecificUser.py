import sqlite3
from datetime import date
import json

def getUserData(userId):
    conn=sqlite3.connect("HADDA_APP.db")
    cursor= conn.cursor()
    cursor.execute("SELECT * From Users WHERE userID=?", (userId,))
    users= cursor.fetchall()
    conn.close()
   
    userJson=[]
    for user in users:
        tempUser= {
        "id": user[0],
        "userID": user[1],
        "name"  : user[2] ,
        "email": user[3],
        "phone_no": user[4],
        "address": user[5],
        "password": user[6] 
        }

        userJson.append(tempUser)

    return json.dumps(userJson)
