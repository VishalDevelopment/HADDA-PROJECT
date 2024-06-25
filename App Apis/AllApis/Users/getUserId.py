import sqlite3
def get_user_id_by_credentials(email, password):

    conn = sqlite3.connect("HADDA_APP.db")
    cursor = conn.cursor()

   
    cursor.execute("SELECT userID FROM Users WHERE email=? AND password=?", (email, password))
    user_id = cursor.fetchone()

    conn.close()

    return user_id[0] if user_id else None  