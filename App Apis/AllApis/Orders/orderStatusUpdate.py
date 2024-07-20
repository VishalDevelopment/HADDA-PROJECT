import sqlite3

def orderstatusUpdate(orderId, weight, price, status):
    conn = sqlite3.connect("HADDA_APP.db")
    cursor = conn.cursor()

    # Parameterized query to prevent SQL injection and potential type mismatches
    try:
        if status == "0":
            cursor.execute("UPDATE Orders SET weight = ?, price = ?, status = 'Failed' WHERE id = ?", (weight, price, orderId))
        elif status == "1":
            cursor.execute("UPDATE Orders SET weight = ?, price = ?, status = 'Successful' WHERE id = ?", (weight, price, orderId))
        conn.commit()
    except sqlite3.Error as e:
        # Handle specific SQLite errors
        print(f"SQLite error: {e}")
    finally:
        conn.close()  