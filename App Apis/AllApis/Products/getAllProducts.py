import sqlite3
import json
def getAllProducts():
    conn=sqlite3.connect("HADDA_APP.db")
    cursor= conn.cursor()
    cursor.execute("SELECT * From Products")
    users= cursor.fetchall()
    conn.close()

    productJson=[]
    for product in users:
        tempProduct= {
        "id": product[0],
        "category": product[1],
        "price"  : product[2] ,
        "status": product[3],
        "Unit": product[4],
        }
        productJson.append(tempProduct)
    return json.dumps( productJson)
   

    
