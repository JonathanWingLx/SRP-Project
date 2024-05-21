from tkinter import *
from tkinter.filedialog import *

def MainScreen():

    def Text():
        print("Test")

    def OpenFile():
        filename = askopenfilename(parent=MScreen)
        f = open(filename)
        print(f.read())

    MScreen = Tk()
    MScreen.geometry("1080x720")

    MenuBar = Menu(MScreen)
    filemenu = Menu(MenuBar, tearoff=0)
    filemenu.add_command(label="New", command=Text)
    filemenu.add_command(label="Open", command=OpenFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=MScreen.quit)
    MenuBar.add_cascade(label='File', menu=filemenu)

    editmenu = Menu(MenuBar, tearoff=0)
    editmenu.add_command(label="Undo", command=Text)

    helpmenu = Menu(MenuBar, tearoff=0)

    MScreen.config(menu=MenuBar)
    MScreen.mainloop()

MainScreen()


#Documentation/Outside Sources
#"https://www.tutorialspoint.com/python/tk_menu.htm"
#"https://stackoverflow.com/questions/16429716/opening-file-tkinter"
