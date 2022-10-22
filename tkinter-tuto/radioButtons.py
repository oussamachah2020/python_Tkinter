from tkinter import *

food = ["pizza", "humberger", "hotdog"]
window = Tk()
x = IntVar()

for index in range(len(food)):
    radioButton = Radiobutton(
        window, text=food[index], 
        variable=x, #groups buttons if they share the same variables 
        value=index #assigns each button a different value
        )
    radioButton.config()
    radioButton.pack()

window.mainloop()
