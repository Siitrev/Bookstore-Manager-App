from tkinter import *

entryWidth = 30
btnWidth = entryWidth // 2
labelWidth = 7
listWidth = labelWidth + entryWidth

app = Tk(screenName="Bookstore")

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

scrollbarList = Scrollbar(app)
scrollbarList.grid(row=4,column=2)

listView = Listbox(app, width=listWidth,height=6,yscrollcommand=scrollbarList.set)
listView.grid(row=3, column=0,columnspan=2,rowspan=3)

scrollbarList.config(command=listView.yview)

viewBtn = Button(text="View All", width=btnWidth)
viewBtn.grid(row=2, column=3)

searchBtn = Button(text="Search Entry", width=btnWidth)
searchBtn.grid(row=3, column=3)

addBtn = Button(text="Add Entry", width=btnWidth)
addBtn.grid(row=4, column=3)

updateBtn = Button(text="Update Selected", width=btnWidth)
updateBtn.grid(row=5, column=3)

deleteBtn = Button(text="Delete Selected", width=btnWidth)
deleteBtn.grid(row=6, column=3)

closeBtn = Button(text="Close", width=btnWidth)
closeBtn.grid(row=7, column=3)

listView.insert(END,"dupa1")
listView.insert(END,"dupa2")
listView.insert(END,"dupa3")
listView.insert(END,"dupa4")
listView.insert(END,"dupa5")
listView.insert(END,"dupa6")
listView.insert(END,"dupa7")
listView.insert(END,"dupa8")
listView.insert(END,"dupa9")
listView.selection_set(1,1)

app.mainloop()
