import sqlite3
from datetime import date
import uuid
def createUser(name,email,phone_no,address,password):
    conn = sqlite3.connect("HADDA_APP.db")
    cursor = conn.cursor()
    user_id = str(uuid.uuid4())

    cursor.execute("""INSERT INTO Users(
                   id,userID,name,email,phone_no,address,password)
                   VALUES
                   (?,?,?,?,?,?,?)""",(None,user_id,name,email,phone_no,address,password))
    
    conn.commit()
    conn.close()
    return True