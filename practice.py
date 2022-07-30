from cProfile import label
from curses import window
from tkinter import *

from click import confirm
window =  Tk()
# app size
window.geometry('500x500')
# app title 
window.title('Practice Title')
# app image 
icone = PhotoImage(file="edu.png")
window.iconphoto(True, icone)
# app background 
window.config(background="#e7e7e7")
# label
label =Label(window,
            text="Welome",
            font=("Arial",40,'bold'),
            fg="red",
            bg="green",
            relief=RIDGE, #RIDGE, RAISED
            bd=20,
            padx=10,
            pady=10,
            )
label.pack() 
# label.place(x = 0, y=0) 


# button 
clicktime = 0
def btnClick():
    global clicktime
    clicktime+=1
    print(clicktime)

btn = Button(window,
            text="Click",
            command=btnClick,
            font=("Comic Sanse", 30),
            bg="white",
            fg="black",
            activebackground="yellow",
            activeforeground='green',
            # state=DISABLED
            image=icone,
            compound='top',
            # width=50
            )                
btn.pack()


window.mainloop()