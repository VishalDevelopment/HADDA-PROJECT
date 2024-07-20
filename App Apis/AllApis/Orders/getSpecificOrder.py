import sqlite3
import json

def getOrdersByUserId(user_id):
    conn = sqlite3.connect("HADDA_APP.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Orders WHERE userID = ?", (user_id,))
    orders = cursor.fetchall()
    conn.close()

    order_list = []
    for order in orders:
        order_dict = {
            "id": order[0],
            "userID": order[1],
            "name": order[2],
            "email": order[3],
            "phone_no": order[4],
            "category": order[5],
            "unit":order[6],
            "weight":order[7],
            "price": order[8],
            "address": order[9],
            "status":order[10],
            "orderTiming": order[11],
            "orderDate": order[12]
        }
        order_list.append(order_dict)

    return order_list  

def OrderbyOrderId(id):
    conn = sqlite3.connect("HADDA_APP.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM Orders where id = ?",(id))
    gotorder = cursor.fetchall()
    conn.close()
    order ={}
    for specOrder in gotorder:
        tempOrder = {
            "id": specOrder[0],
            "userID": specOrder[1],
            "name": specOrder[2],
            "email": specOrder[3],
            "phone_no": specOrder[4],
            "category": specOrder[5],
            "unit":specOrder[6],
            "weight":specOrder[7],
            "price": specOrder[8],
            "address": specOrder[9],
            "status":specOrder[10],
            "orderTiming": specOrder[11],
            "orderDate": specOrder[12]
        }
        order = tempOrder

    return json.dumps(order)
