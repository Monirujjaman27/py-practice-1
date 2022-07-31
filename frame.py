from curses import window
from tkinter import Button, Tk, Toplevel
from typing import Text
from tk import  *

window = Tk()

def Create():
    # Toplevel()
    Tk()
    window.destroy()

Button(window, text="Create New window", command=Create).pack()


window.mainloop()