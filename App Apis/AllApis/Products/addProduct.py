import sqlite3
def AddProduct(category,price,status,unit):
    conn = sqlite3.connect("HADDA_APP.db")
    cursor = conn.cursor()

    cursor.execute("""INSERT INTO Products(
                   id,category,price,status,unit)
                   VALUES
                   (?,?,?,?,?)""",(None,category,price,status,unit))
    
    conn.commit()
    conn.close()
    return True