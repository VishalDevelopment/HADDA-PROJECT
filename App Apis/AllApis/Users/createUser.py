import sqlite3
from datetime import date
import uuid
def createUser(name,email,phone_no,address,password):
    conn = sqlite3.connect("HADDA_APP.db")
    cursor = conn.cursor()
    user_id = str(uuid.uuid4())

    cursor.execute("SELECT COUNT(*) FROM Users WHERE email = ?", (email,))
    email_exists = cursor.fetchone()[0]  # Get the first element (count)

    if email_exists > 0:
        print("Email already exists. Please use a different email address.")
        conn.close()
        return False

    cursor.execute("""INSERT INTO Users(
                   id,userID,name,email,phone_no,address,password)
                   VALUES
                   (?,?,?,?,?,?,?)""",(None,user_id,name,email,phone_no,address,password))
    
    conn.commit()
    conn.close()
    return True