import sqlite3


def createTables():
    conn = sqlite3.connect("HADDA_APP.db")
    cursor = conn.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS Users(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   userID VARCHAR(30),
                   name VARCHAR(15),
                   email VARCHAR(50),
                   phone_no VARCHAR(11),
                   address VARCHAR(200),
                   password VARCHAR(30)
                   );""")
    
    cursor.execute("""CREATE TABLE IF NOT EXISTS Products(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   category VARCHAR(100),
                   price REAL NOT NULL,
                   status VARCHAR (50),
                   Unit INTEGER);""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS Orders(
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   userID VARCHAR(30),
                   name VARCHAR(15),
                   email VARCHAR(50),
                   phone_no VARCHAR(11),
                   category VARCHAR(100),
                   price REAL NOT NULL,
                   address VARCHAR(200),
                   orderTiming VARCHAR(100),
                   orderDate VARCHAR(100))""")
    
    conn.commit()
    conn.close()
    