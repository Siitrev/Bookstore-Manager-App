from tkinter import *
from dbQuery import Database
from tkinter import filedialog
import sys

class Main:
    
    def __init__(self,app : Tk, dbPath:str):
        
        
        self.app = app
        entryWidth = 30
        btnWidth = entryWidth // 2
        labelWidth = 7
        listWidth = labelWidth + entryWidth
        self.db = Database(dbPath)
        
        app.minsize(500,250)
        app.title("Bookstore")
        
        # Creating frames for button widgets and listbox widget
        wholeList = Frame(app,pady=40)
        wholeList.grid(row=3, column=0,columnspan=3,rowspan=3)

        buttonFrame = Frame(app,pady=25)
        buttonFrame.grid(row=2,column=3,rowspan=6)

        # Creating Entries and labels

        self.titleValue = StringVar()
        titleLabel = Label(text="Title", width=labelWidth)
        self.titleEntry = Entry(app, textvariable=self.titleValue, width=entryWidth)
        self.titleEntry.grid(row=0, column=1,pady=10)
        titleLabel.grid(row=0, column=0)

        self.authorValue = StringVar()
        authorLabel = Label(text="Author", width=labelWidth)
        self.authorEntry = Entry(app, textvariable=self.authorValue, width=entryWidth)
        self.authorEntry.grid(row=0, column=3)
        authorLabel.grid(row=0, column=2)

        self.yearValue = StringVar()
        yearLabel = Label(text="Year", width=labelWidth)
        self.yearEntry = Entry(app, textvariable=self.yearValue, width=entryWidth)
        self.yearEntry.grid(row=1, column=1)
        yearLabel.grid(row=1, column=0)

        self.isbnValue = StringVar()
        isbnLabel = Label(text="ISBN", width=labelWidth)
        self.isbnEntry = Entry(app, textvariable=self.isbnValue, width=entryWidth)
        self.isbnEntry.grid(row=1, column=3)
        isbnLabel.grid(row=1, column=2)

        # Creating Listbox with scrollbars
        scrollbarListY = Scrollbar(wholeList)
        scrollbarListY.pack(side=RIGHT,fill=Y)

        scrollbarListX = Scrollbar(wholeList, orient=HORIZONTAL)
        scrollbarListX.pack(side=BOTTOM,fill=X)

        self.listView = Listbox(wholeList, width=listWidth,height=6,yscrollcommand=scrollbarListY.set,  xscrollcommand=scrollbarListX.set)
        self.listView.bind("<<ListboxSelect>>",self.autoComplete)
        self.listView.bind("<FocusOut>",self.deAct)
        self.listView.pack()

        scrollbarListY.config(command=self.listView.yview)
        scrollbarListX.config(command=self.listView.xview)

        # Creating buttons

        viewBtn = Button(buttonFrame,text="View All", width=btnWidth, command=self.viewAll)
        viewBtn.pack()

        searchBtn = Button(buttonFrame,text="Search Entry", width=btnWidth, command=self.searchEntry)
        searchBtn.pack()

        addBtn = Button(buttonFrame,text="Add Entry", width=btnWidth,command=self.addEntry)
        addBtn.pack()

        updateBtn = Button(buttonFrame,text="Update Selected", width=btnWidth, command=self.updateSelected)
        updateBtn.pack()

        deleteBtn = Button(buttonFrame,text="Delete Selected", width=btnWidth, command=self.deleteEntry)
        deleteBtn.pack()

        closeBtn = Button(buttonFrame,text="Close", width=btnWidth, command=sys.exit)
        closeBtn.pack()

    # Deactivating selection in Listbox
    def deAct(self,e):
        self.listView.selection_clear(0,END)

    # Filling entries with data
    def autoComplete(self,e):
        if len(self.listView.curselection()) != 0:  
            self.titleEntry.delete(0,END)
            self.authorEntry.delete(0,END)
            self.yearEntry.delete(0,END)
            self.isbnEntry.delete(0,END)
            
            rowId = self.listView.selection_get().split(" ")[0]

            self.titleEntry.insert(END,self.db.viewRowById(rowId)[0][0])
            self.authorEntry.insert(END,self.db.viewRowById(rowId)[0][1])
            self.yearEntry.insert(END,self.db.viewRowById(rowId)[0][2])
            self.isbnEntry.insert(END,self.db.viewRowById(rowId)[0][3])

    # Viewing all the data from database
    def viewAll(self):
        self.listView.delete(0,END)
        entries = self.db.viewAll()
        for i in entries:
            self.listView.insert(END,i)

    # Adding data to database
    def addEntry(self):
        self.db.addRow(self.titleValue.get(),self.authorValue.get(),self.yearValue.get(),self.isbnValue.get())
        self.viewAll()

    # Updating selected row in database
    def updateSelected(self):
        self.db.updateRow(self.titleValue.get(),self.authorValue.get(),self.yearValue.get(),self.isbnValue.get())
        self.viewAll()

    # Searching for a certain row and showing it in a Listbox
    def searchEntry(self):
        self.listView.delete(0,END)
        searchedEntries = self.db.viewRowByTitleAndAuth(self.titleValue.get(),self.authorValue.get(),self.yearValue.get(),self.isbnValue.get())
        for i in searchedEntries:
            self.listView.insert(END,i)

    # Deleting selected row in a database
    def deleteEntry(self):
        self.db.deleteRow(self.isbnValue.get())
        self.viewAll()
        self.listView.selection_set(0,0)
