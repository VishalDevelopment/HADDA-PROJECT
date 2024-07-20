import sqlite3
from datetime import datetime
from datetime import date




import uuid
def insertOrder(user_id,name,email,phone_no,category,unit,price,address):

    conn = sqlite3.connect("HADDA_APP.db")
    cursor = conn.cursor()
    time = datetime.now().strftime('%H:%M')
    dateCurrent = date.today()
    weight =0.00
    status = "Pending"
    cursor.execute("""INSERT INTO Orders(
                   id,userID,name,email,phone_no,category,unit,weight,price,address,status,orderTiming,orderDate)
                   VALUES
                   (?,?,?,?,?,?,?,?,?,?,?,?,?)""",(None,user_id,name,email,phone_no,category,unit,weight,price,address,status,time,dateCurrent))
    
    conn.commit()
    conn.close()
    return True