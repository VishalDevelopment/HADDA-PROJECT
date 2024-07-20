
import sqlite3
import json

def getAllOrdersitem():
    conn=sqlite3.connect("HADDA_APP.db")
    cursor= conn.cursor()
    
    cursor.execute("SELECT * From Orders")
    orders= cursor.fetchall()
    conn.close()
   
    orderJson=[]
    for order in orders:
        tempOrder= {
        "id": order[0],
        "user_id": order[1],
        "name"  :order[2] ,
        "email": order[3],
        "phone_no": order[4],
        "category":order[5],
        "price": order[6],
        "address": order[7]  ,
        "orderTiming": order[8] ,
        "orderDate": order[9]    
        }

        orderJson.append(tempOrder)

    return json.dumps(orderJson)
