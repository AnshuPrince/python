from tkinter import filedialog,ttk
from tkinter import *
from tkinter.ttk import Treeview

mainWindow = Tk()


def browseAndReadFile():
    mainWindow.fileName = filedialog.askopenfilename(initialdir="/", title="Select file",filetypes=(("kget files", "*.log"), ("all files", "*.*")))
    file = open(mainWindow.fileName)
    tree = ttk.Treeview(mainWindow)
    tree["columns"] = ("EUtranCellFDD")
    tree.column("EUtranCellFDD", width=400)
    tree.heading("EUtranCellFDD", text="EUtranCellFDD")
    ID = []
    for line in file:
        index = line.find('EUtranCellFDD=')
        id = line[index: index+33]
        if index > -1 and id not in ID:
            ID.append(id)
    for index, w in enumerate(ID):
        tree.insert("", index+1, text="ID", values=(w))
    # tree.insert("", 0, text="Line 1", values=("1A", "1b"))
    # tree.insert("", 1, text="Dir 2", values=("2A", "2B"))
    # ##alternatively:
    # tree.insert("", 3, "dir3", text="Dir 3")
    # tree.insert("dir3", 3, text=" sub dir 3", values=("3A", " 3B"))
    tree.pack()

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
