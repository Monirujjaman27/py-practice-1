from curses import window
from tkinter import *
window =  Tk()
# app size
window.geometry('500x500')
# app title 
window.title('Practice Title')
# app image 
icone = PhotoImage(file="edu.png")
window.iconphoto(True, icone)
# app background 
window.config(background="#707070")

window.mainloop()