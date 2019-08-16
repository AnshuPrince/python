from tkinter import filedialog
from tkinter import *

mainWindow = Tk()


def browseAndReadFile():
    mainWindow.fileName = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("kget files", "*.log"), ("all files", "*.*")))
    file = open(mainWindow.fileName)



menu = Menu(mainWindow)
mainWindow.config(menu=menu)
filemenu = Menu(menu)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=browseAndReadFile)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=mainWindow.quit)
helpmenu = Menu(menu)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')
mainWindow.mainloop()
