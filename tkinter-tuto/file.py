from tkinter import *
from tkinter import filedialog


# def openFile():
#     filepath = filedialog.askopenfilename(
#         initialdir="/home/oussama/Work/Python/tkinter-tuto", filetypes=(("text files", "*.txt"),
#                                                                         ("all files", "*.*")))
#     file = open(filepath, 'r')
#     print(file.read())
#     file.close()


# button = Button(text="Open", command=openFile)
# button.pack()


# ---------file saving-------------

def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[
        ("Text file", ".txt"),
        ("Html file", ".html"),
        ("All files", ".*"),
    ])
    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()

    if file is None:
        return

window = Tk()

button = Button(text='save', command=saveFile)
button.pack()
text = Text(window)
text.pack()

window.mainloop()
