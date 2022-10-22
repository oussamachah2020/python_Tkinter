![tkinter](https://user-images.githubusercontent.com/72669865/197356232-8b7af17b-f94c-4a1c-920c-f70534eaad9d.jpg)



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
