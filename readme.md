<p align="center"><a href="https://www.python.org/" target="_blank"><img src="https://imgs.search.brave.com/vB3rIUOwUdSCy9FquSiK2jlHfO7i8b1KcIbEvkFdqWs/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly9sb2dv/cy1kb3dubG9hZC5j/b20vd3AtY29udGVu/dC91cGxvYWRzLzIw/MTYvMTAvUHl0aG9u/X2xvZ29faWNvbi5w/bmc" width="400" alt="python Logo"></a></p>

<p align="center">
<a href="https://code.visualstudio.com/"><img src="https://imgs.search.brave.com/vBRkfxjpgJxuXlTYnLgXXdHxWEUTcRfGW6yYmeIC15g/rs:fit:800:600:1/g:ce/aHR0cHM6Ly91c2Vy/LWltYWdlcy5naXRo/dWJ1c2VyY29udGVu/dC5jb20vMTAzNzk5/OTQvMzE5ODU3NTQt/YzU2YjhkYmEtYjk5/OC0xMWU3LTk3MDUt/YTdmOTg0NDMzMDQ5/LnBuZw" alt="vs code"></a>


# Pytho Tkinter for building GUI

> this repo contains some basics about how to work with tkinter (classes and methods of this library)

#### Example

> Create an Entry
```
from tkinter import *

window = Tk()
entry = Entry(window, font=("Arial",50), fg="#00FF00", bg="black",show='*')
entry.pack(side=LEFT)

window.mainloop()
```

> Create a messageBox

```
from tkinter import *

def click():
    # messagebox.showinfo("this is a message", 'you are a person')
    if messagebox.askokcancel('ask ok cancel','do you want to do the thing?'):
        print("you did it")
    else:
        print("you didn't do it")


window = Tk()

window.mainloop()

--there is other boxe types like:
    `showError`
    `showwarning`
    `askokcancel`
    .
    .
    .

```
> Create Button

```
from tkinter import * 
window = Tk()

button = Button(window, text="submit" #just an exmaple)
button.pack()

window.mainloop()
```
