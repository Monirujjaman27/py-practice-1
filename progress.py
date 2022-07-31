
from heapq import merge
from tkinter import * 
from tkinter.ttk import *

def start():
    bar['val']+=5
    print(bar)

window = Tk()



bar = Progressbar(window, orient="horizontal", length=500).pack(pady=5)

Button(window, text="click", command=start).pack()

window.mainloop()