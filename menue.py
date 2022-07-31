from tkinter import Menu, Tk
from click import command
from tk import *

# methods 
def openFile():
    print('file open')


def saveFile():
    print('file save')


def Exit():
    print('file exit')

# edit
def cut():
    print('file exit')
def copy():
    print('file exit')
def paste():
    print('file exit')




window = Tk()
window.geometry("500x500")
window.title("Python Menue")
menuebar = Menu(window)
window.config(menu=menuebar)

# file menue 
filemenue = Menu(menuebar, tearoff=0)
menuebar.add_cascade(label="File", menu=filemenue)
filemenue.add_command(label="Open", command=openFile)
filemenue.add_command(label="Save", command=saveFile)
filemenue.add_separator() 
filemenue.add_command(label="Exit", command=Exit)
#edit menue 
editMenue = Menu(menuebar, tearoff=0)
menuebar.add_cascade(label="Edit", menu=editMenue)
editMenue.add_command(label="Cut", command=cut)
editMenue.add_command(label="Copy", command=copy)
editMenue.add_command(label="Past", command=paste)










window.mainloop()