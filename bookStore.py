from tkinter import *

app = Tk(screenName="Bookstore")

titleValue = StringVar()
titleLabel = Label(text="Title",width=7)
titleEntry = Entry(app,textvariable=titleValue)
titleEntry.grid(row = 0, column = 1)
titleLabel.grid(row = 0, column = 0)

authorValue = StringVar()
authorLabel = Label(text="Author",width=7)
authorEntry = Entry(app,textvariable=authorValue)
authorEntry.grid(row = 0, column = 3)
authorLabel.grid(row = 0, column = 2)

yearValue = StringVar()
yearLabel = Label(text="Year",width=7)
yearEntry = Entry(app,textvariable=yearValue)
yearEntry.grid(row = 1, column = 1)
yearLabel.grid(row = 1, column = 0)

isbnValue = StringVar()
isbnLabel = Label(text="ISBN",width=7)
isbnEntry = Entry(app,textvariable=isbnValue)
isbnEntry.grid(row = 1, column = 3)
isbnLabel.grid(row = 1, column = 2)

print()
viewBtn = Button(text="View All")
viewBtn.grid(row=2,column=3)

app.mainloop()