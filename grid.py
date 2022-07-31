
from tkinter import * 
from tkinter import ttk

window = Tk()

first_name = Label(window, text="First Name").grid(row=0, column=0)
first_entry = Entry(window).grid(row=0, column=1)

last_name = Label(window, text="Last Name").grid(row=1, column=0)
first_entry = Entry(window).grid(row=1, column=1)

window.mainloop()