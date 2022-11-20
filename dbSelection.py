from tkinter import *
from tkinter import filedialog
import os

class DbSelection(object):
    
    def __init__(self,app : Tk):
        
        
        self.app = app
        self.dbPath = f"{os.curdir}/bookStore.db"
        app.wm_title("Bookstore")
        
        self.dbPathLabel = Label(text=f"Path of a selected .db file: {self.dbPath}")
        dbPathBtn = Button(app,text="Change database path",command=self.dbSelection)
        self.dbPathLabel.pack()
        dbPathBtn.pack(side=BOTTOM)
        
        submitBtn = Button(app,text="Submit a path",command=self.submit)
        submitBtn.pack(side=BOTTOM)
        
    def dbSelection(self):
        self.dbPath = filedialog.askopenfilename(initialdir="/",title="Select a .db file", filetypes = (("Database files","*.db*"),))
        self.dbPathLabel["text"] = f"Path of a selected .db file: {self.dbPath}"
    def submit(self):
        self.app.destroy()
