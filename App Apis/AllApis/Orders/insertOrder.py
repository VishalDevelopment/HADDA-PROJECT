import sqlite3
from datetime import datetime
from datetime import date




import uuid
def insertOrder(user_id,name,email,phone_no,category,price,address):

    conn = sqlite3.connect("HADDA_APP.db")
    cursor = conn.cursor()
    time = datetime.now().strftime('%H:%M')
    dateCurrent = date.today()
    
    cursor.execute("""INSERT INTO Orders(
                   id,userID,name,email,phone_no,category,price,address,orderTiming,orderDate)
                   VALUES
                   (?,?,?,?,?,?,?,?,?,?)""",(None,user_id,name,email,phone_no,category,price,address,time,dateCurrent))
    
    conn.commit()
    conn.close()
    return True