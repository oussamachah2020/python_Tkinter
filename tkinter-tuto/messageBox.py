from tkinter import *
from tkinter import messagebox

window = Tk()

def click():
    # messagebox.showinfo("this is a message", 'you are a person')
    if messagebox.askokcancel('ask ok cancel','do you want to do the thing?'):
        print("you did it")
    else:
        print("you didn't do it")

button = Button(window, command=click, text="click me")
button.pack()

window.mainloop()