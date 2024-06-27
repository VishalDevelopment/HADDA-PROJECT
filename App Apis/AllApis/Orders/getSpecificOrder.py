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
            "price": order[6],
            "address": order[7],
            "orderTiming": order[8],
            "orderDate": order[9],
        }
        order_list.append(order_dict)

    return order_list

