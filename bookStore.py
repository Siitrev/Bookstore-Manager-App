from tkinter import *
import dbQuery

entryWidth = 30
btnWidth = entryWidth // 2
labelWidth = 7
listWidth = labelWidth + entryWidth

# Deactivating selection in Listbox
def deAct(e):
    listView.selection_clear(0,END)

# Filling entries with data
def autoComplete(e):
    if len(listView.curselection()) != 0:  
        titleEntry.delete(0,END)
        authorEntry.delete(0,END)
        yearEntry.delete(0,END)
        isbnEntry.delete(0,END)
         
        rowId = listView.selection_get().split(" ")[0]

        titleEntry.insert(END,dbQuery.viewRowById(rowId)[0][0])
        authorEntry.insert(END,dbQuery.viewRowById(rowId)[0][1])
        yearEntry.insert(END,dbQuery.viewRowById(rowId)[0][2])
        isbnEntry.insert(END,dbQuery.viewRowById(rowId)[0][3])

# Viewing all the data from database
def viewAll():
    listView.delete(0,END)
    entries = dbQuery.viewAll()
    for i in entries:
        listView.insert(END,i)

# Adding data to database
def addEntry():
    dbQuery.addRow(titleValue.get(),authorValue.get(),yearValue.get(),isbnValue.get())
    viewAll()

# Updating selected row in database
def updateSelected():
    dbQuery.updateRow(titleValue.get(),authorValue.get(),yearValue.get(),isbnValue.get())
    viewAll()

# Searching for a certain row and showing it in a Listbox
def searchEntry():
    listView.delete(0,END)
    searchedEntries = dbQuery.viewRowByTitleAndAuth(titleValue.get(),authorValue.get(),yearValue.get(),isbnValue.get())
    for i in searchedEntries:
        listView.insert(END,i)

# Deleting selected row in a database
def deleteEntry():
    dbQuery.deleteRow(isbnValue.get())
    viewAll()
    listView.selection_set(0,0)
    
# Starting the app
app = Tk()

# Creating table for books
dbQuery.createTable()

app.minsize(500,250)
app.title("Bookstore")

# Creating frames for button widgets and listbox widget
wholeList = Frame(app,pady=40)
wholeList.grid(row=3, column=0,columnspan=3,rowspan=3)

buttonFrame = Frame(app,pady=25)
buttonFrame.grid(row=2,column=3,rowspan=6)

# Creating Entries and labels

titleValue = StringVar()
titleLabel = Label(text="Title", width=labelWidth)
titleEntry = Entry(app, textvariable=titleValue, width=entryWidth)
titleEntry.grid(row=0, column=1,pady=10)
titleLabel.grid(row=0, column=0)

authorValue = StringVar()
authorLabel = Label(text="Author", width=labelWidth)
authorEntry = Entry(app, textvariable=authorValue, width=entryWidth)
authorEntry.grid(row=0, column=3)
authorLabel.grid(row=0, column=2)

yearValue = StringVar()
yearLabel = Label(text="Year", width=labelWidth)
yearEntry = Entry(app, textvariable=yearValue, width=entryWidth)
yearEntry.grid(row=1, column=1)
yearLabel.grid(row=1, column=0)

isbnValue = StringVar()
isbnLabel = Label(text="ISBN", width=labelWidth)
isbnEntry = Entry(app, textvariable=isbnValue, width=entryWidth)
isbnEntry.grid(row=1, column=3)
isbnLabel.grid(row=1, column=2)

# Creating Listbox with scrollbars
scrollbarListY = Scrollbar(wholeList)
scrollbarListY.pack(side=RIGHT,fill=Y)

scrollbarListX = Scrollbar(wholeList, orient=HORIZONTAL)
scrollbarListX.pack(side=BOTTOM,fill=X)

listView = Listbox(wholeList, width=listWidth,height=6,yscrollcommand=scrollbarListY.set,  xscrollcommand=scrollbarListX.set)
listView.bind("<<ListboxSelect>>",autoComplete)
listView.bind("<FocusOut>",deAct)
listView.pack()

scrollbarListY.config(command=listView.yview)
scrollbarListX.config(command=listView.xview)

# Creating buttons

viewBtn = Button(buttonFrame,text="View All", width=btnWidth, command=viewAll)
viewBtn.pack()

searchBtn = Button(buttonFrame,text="Search Entry", width=btnWidth, command=searchEntry)
searchBtn.pack()

addBtn = Button(buttonFrame,text="Add Entry", width=btnWidth,command=addEntry)
addBtn.pack()

updateBtn = Button(buttonFrame,text="Update Selected", width=btnWidth, command=updateSelected)
updateBtn.pack()

deleteBtn = Button(buttonFrame,text="Delete Selected", width=btnWidth, command=deleteEntry)
deleteBtn.pack()

closeBtn = Button(buttonFrame,text="Close", width=btnWidth, command=exit)
closeBtn.pack()




app.mainloop()
