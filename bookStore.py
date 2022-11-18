from tkinter import *
import dbQuery

entryWidth = 30
btnWidth = entryWidth // 2
labelWidth = 7
listWidth = labelWidth + entryWidth

def dupa(e):
    titleEntry.delete(0,END)
    titleEntry.insert(END,listView.selection_get())

def viewAll():
    listView.delete(0,END)
    entries = dbQuery.viewAll()
    for i in entries:
        listView.insert(END,i)

def addEntry():
    dbQuery.addRow(titleValue.get(),authorValue.get(),yearValue.get(),isbnValue.get())
app = Tk()
dbQuery.createTable()
app.minsize(500,250)
app.title("Bookstore")
wholeList = Frame(app)
wholeList.grid(row=3, column=0,columnspan=3,rowspan=3)

titleValue = StringVar()
titleLabel = Label(text="Title", width=labelWidth)
titleEntry = Entry(app, textvariable=titleValue, width=entryWidth)
titleEntry.grid(row=0, column=1)
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

scrollbarListY = Scrollbar(wholeList)
scrollbarListY.pack(side=RIGHT,fill=Y)

scrollbarListX = Scrollbar(wholeList, orient=HORIZONTAL)
scrollbarListX.pack(side=BOTTOM,fill=X)

listView = Listbox(wholeList, width=listWidth,height=6,yscrollcommand=scrollbarListY.set,  xscrollcommand=scrollbarListX.set)
listView.pack()

scrollbarListY.config(command=listView.yview)
scrollbarListX.config(command=listView.xview)

viewBtn = Button(text="View All", width=btnWidth, command=viewAll)
viewBtn.grid(row=2, column=3)

searchBtn = Button(text="Search Entry", width=btnWidth)
searchBtn.grid(row=3, column=3)

addBtn = Button(text="Add Entry", width=btnWidth,command=addEntry)
addBtn.grid(row=4, column=3)

updateBtn = Button(text="Update Selected", width=btnWidth)
updateBtn.grid(row=5, column=3)

deleteBtn = Button(text="Delete Selected", width=btnWidth)
deleteBtn.grid(row=6, column=3)

closeBtn = Button(text="Close", width=btnWidth)
closeBtn.grid(row=7, column=3)

listView.bind("<<ListboxSelect>>",dupa)


app.mainloop()
