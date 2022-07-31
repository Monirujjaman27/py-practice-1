from cProfile import label
from cgitb import text
from curses import window
from tkinter import *
from turtle import left

from click import confirm
window =  Tk()
# app size
window.geometry('1000x700')
# app title 
window.title('Practice Title')
# app image 
icone = PhotoImage(file="edu.png")
window.iconphoto(True, icone)
# app background 
window.config(background="#e7e7e7")
# entry
entry = Entry(window,show="*")
entry.place(x=0, y=0)

def submit():
    print('submit')

def delete():
    print('delete')

submit_btn = Button(window, text="SUbmit", command=submit) 
submit_btn.place(x=0, y=20)

del_btn = Button(window, text="DELETE", command=delete) 
del_btn.place(x=70, y=20)



window.mainloop()