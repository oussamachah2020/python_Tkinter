<p align="center"><a href="https://www.python.org/" target="_blank"><img src=[["[[https://imgs.search.brave.com/vB3rIUOwUdSCy9FquSiK2jlHfO7i8b1KcIbEvkFdqWs/rs:fit:1200:1200:1/g:ce/aHR0cHM6Ly9sb2dv/cy1kb3dubG9hZC5j/b20vd3AtY29udGVu/dC91cGxvYWRzLzIw/MTYvMTAvUHl0aG9u/X2xvZ29faWNvbi5w/bmc](https://imgs.search.brave.com/eho3YAMBsacJ7VyI1zzZCWB4w7IwU20AsDTfl4bJulo/rs:fit:461:274:1/g:ce/aHR0cHM6Ly8xLmJw/LmJsb2dzcG90LmNv/bS8tU2V5eVZxYjFx/VjAvV1pJb2lLajBu/Y0kvQUFBQUFBQUFB/dWMva0pUTmFVdVda/MG8wc3NfNlR6SkFj/bkp5S1hjTVJiLUlB/Q0xjQkdBcy9zMTYw/MC9HVUklMkJweXRo/b24lMkJUa2ludGVy/LnBuZw)](https://imgs.search.brave.com/OiHLAaNl7sD43SfPjnvEw7gEBkiNc2T_Twx-iNFuKkA/rs:fit:200:200:1/g:ce/aHR0cHM6Ly9zdGF0/aWMuamF2YXRwb2lu/dC5jb20vcHl0aG9u/L2ltYWdlcy90a2lu/dGVyLXR1dG9yaWFs/LnBuZw)](https://imgs.search.brave.com/9-1CVGcb1nc2G9xvhcPgHy-SA-nypynCOi-Mf56S1XI/rs:fit:375:422:1/g:ce/aHR0cHM6Ly91Y2Fy/ZWNkbi5jb20vZTFm/YzhlMTUtMmY1Mi00/YjYwLWJkOWItZDM1/MmYzMzI1MWQ1Lw)"](https://imgs.search.brave.com/9-1CVGcb1nc2G9xvhcPgHy-SA-nypynCOi-Mf56S1XI/rs:fit:375:422:1/g:ce/aHR0cHM6Ly91Y2Fy/ZWNkbi5jb20vZTFm/YzhlMTUtMmY1Mi00/YjYwLWJkOWItZDM1/MmYzMzI1MWQ1Lw) width="400" alt="python Logo"></a></p>


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
