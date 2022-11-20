import sqlite3


class Database():
    
    
    def __init__(self,dbPath):
        self.conn = sqlite3.connect(dbPath)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS store(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, title TEXT, author TEXT, year INT, ISBN TEXT)")
        self.conn.commit()
    
    def addRow(self,titleV,authorV,yearV,isbnV):
        self.cur.execute(f"INSERT INTO store(title,author,year,ISBN) VALUES('{titleV}','{authorV}',{yearV},'{isbnV}')")
        self.conn.commit()
        
    def viewAll(self):
        self.cur.execute("SELECT * FROM store")
        result = self.cur.fetchall()
        return result

    def viewRowById(self,rowId):
        self.cur.execute(f"SELECT title,author,year,ISBN FROM store WHERE id={rowId}")
        result = self.cur.fetchall()
        return result

    def updateRow(self,titleV,authorV,yearV,isbnV):
        self.cur.execute(f"UPDATE store SET title='{titleV}',author='{authorV}', year={yearV}, isbn='{isbnV}' WHERE isbn='{isbnV}'")
        self.conn.commit()

    def viewRowByTitleAndAuth(self,titleV="",authorV="",yearV="",isbnV=""):
        self.cur.execute(f"SELECT * FROM store WHERE year='{yearV}' OR title='{titleV}' OR author='{authorV}' OR ISBN='{isbnV}'")
        result = self.cur.fetchall()
        return result
        
    def deleteRow(self,isbnV):
        self.cur.execute(f"DELETE FROM store WHERE ISBN = '{isbnV}'")
        self.conn.commit()
    
    def __del__(self):
        self.conn.close()
    
    