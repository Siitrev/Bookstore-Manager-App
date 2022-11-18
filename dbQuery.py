import sqlite3

def createTable():
    conn = sqlite3.connect("bookStore.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title TEXT, author TEXT, year INT, ISBN TEXT)")
    conn.close()
    
def addRow(titleV,authorV,yearV,isbnV):
    with sqlite3.connect("bookStore.db") as conn:
        cur = conn.cursor()
        cur.execute(f"INSERT INTO store(title,author,year,ISBN) VALUES('{titleV}','{authorV}',{yearV},'{isbnV}')")

def viewAll():
    with sqlite3.connect("bookStore.db") as conn:
        cur = conn.cursor()
        cur.execute("SELECT * FROM store")
        result = cur.fetchall()
        return result