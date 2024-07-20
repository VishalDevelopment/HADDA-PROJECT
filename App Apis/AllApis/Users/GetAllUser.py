import sqlite3
import json
def GetAllUser():
    conn = sqlite3.connect("HADDA_APP.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * From Users")
    users= cursor.fetchall()
    conn.close()
    userjson=[]
    for user in users:
        tempUser= {
        "id": user[0],
        "userID": user[1],
        "name"  :user[2] ,
        "email": user[3],
        "phone_no": user[4],
        "address": user[5]
        }
        userjson.append(tempUser)
    return json.dumps(userjson)