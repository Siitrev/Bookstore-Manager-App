from mainApp import Main
from tkinter import *
from dbSelection import DbSelection

firstWindow = Tk()
root = DbSelection(firstWindow)
firstWindow.mainloop()

secondWindow = Tk()
Main(secondWindow,root.dbPath)
secondWindow.mainloop()
