from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from sqlite3 import *

from ReadDB import *
from Classes import *

def MainScreen():

    def WindowSize(event):
        NewWidth = event.width
        #NewWidth = NewWidth - 100
        NewHeight = event.height
        #print(event.widget)
        if event.widget == MScreen:
            NewWidth = NewWidth - 150
            NewHeight = NewHeight - 200
            MainFrame.config(width = NewWidth, height = NewHeight)

    def Text():
        print("Test")

    def AddItems(fileName):
        print("Test")
        #Grab a list from the database
        #parse in filename?
        file = connect("Test.db")
        cs = file.cursor()
        fileName = fileName.replace(' ', '_')
        fileName = fileName.split('/')

        cs.execute("SELECT * FROM {}".format('DB_'+fileName[-1]))
        dbArray = cs.fetchall()
        print(dbArray[0][1])
        #for loop to look at each item in the database
            #create object with channel, dimmer and address

        #Check code
        dbLen = len(dbArray)
        dbObjArray = []
        i = 0
        for x in range(dbLen):
            #print("Test")

            #Object init on sepertae file
            #define object within loop
            ItemTemp = Item(MainFrame, i, dbArray[i][cmbA1.current()], dbArray[i][cmbA2.current()], dbArray[i][cmbA3.current()], dbArray[i][cmbA4.current()])
            #Other options for obj come from dropdown options on screen

            #dbObjArray.append() with each object
            dbObjArray.append(ItemTemp)
            #create dbObjArray
            #Object attributes - Channel, array pointer + any other data shown on screen

            #each item on screen is an object
            #the details of the item is stored in the object
            #go through the object array and place them on screen
            i += 1
        #End of Check
        #dbObjArray[1].labelMake(MScreen)
        dbObjArray[0].labelShow(70, 110)
        print(cmbA1.current())
        #add objects to screen
        #take window size - extra bits on screen for usable size
        #if x + gap > usablesize(x)
        #then x = 0ish and y = y + gap
        #else x = x + gap

        #use frame for both usable area and each item
        #add scroll bar for master frame

        #https://tkdocs.com/tutorial/widgets.html#frame

    def OpenFile():
        filename = askopenfilename(parent=MScreen)
        #f = open(filename)
        #print(f.read())
        #Read(filename)
        AddItems(filename)

    #Create the screen
    MScreen = Tk()
    MScreen.geometry("1080x720")

    #Menu bar attributes
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

    #On screen attributes
    MFrameStyle = Style()
    MFrameStyle.configure("TFrame", background="lightgrey")
    MFrameStyle.configure("Frame2.TFrame", background="darkgrey")
    MFX = MScreen.winfo_screenwidth() - 100
    MFY = MScreen.winfo_screenheight() - 200
    MainFrame = Frame(MScreen, style="TFrame", height=MFY, width=MFX)

    A1 = StringVar(MScreen)
    A2 = StringVar(MScreen)
    A3 = StringVar(MScreen)
    A4 = StringVar(MScreen)

    cmbA1 = Combobox(MScreen, width=27, textvariable=A1)
    cmbA2 = Combobox(MScreen, width=27, textvariable=A2)
    cmbA3 = Combobox(MScreen, width=27, textvariable=A3)
    cmbA4 = Combobox(MScreen, width=27, textvariable=A4)

    cmbA1['values'] = ('Purpose', 'Channel', 'Dimmer', 'Address', 'Position', 'Unit#', 'Instrument Type', 'Load', 'Accessory', 'Color', 'Gobo', 'Gobo Size', 'Circiut Name', 'Circuit#', 'Cable', 'Data Cable', 'Mark', 'System', 'User 1', 'User 2', 'User 3', 'User 4', 'User 5', 'User 6', 'User 7', 'User 8', 'User 9', 'User 10', 'User 11', 'User 12', 'User 13', 'User 14', 'User 15', 'User 16', 'User 17', 'User 18', 'User 19', 'User 20', 'User 21', 'User 22', 'User 23', 'User 24', 'Scenery', 'Focus L/R', 'Focus U/D', 'Focus Note', 'US', 'DS', 'SR', 'SL', 'Top', 'Bot', 'Focus Status', 'Axis', 'Beam', 'VW Layer', 'VW Label Legend', 'VW Class', 'VW X Coordinate', 'VW Y Coordinate', 'VW Z Coordinate', 'VW Symbol Rotation', 'VW Focus Plot', 'Order of Light within Position', 'LightWright ID', 'Vectorworks UID', 'Symbol', 'On Light Plot', 'Universe', 'DMX#', 'Dimmer Phase', 'Position Order', 'Work Note Status', 'Device Type', 'Color Frame', '"When, What and Who Changed"', 'Position & Unit#', 'Instrument Type & Accessory', 'Instrument Type & Load', 'Instrument Type & Accessory & Load', 'Circiut Name & Circiut#', 'Color & Gobo', 'Color Flags', 'DMX Qty', 'Instrument Type Weight')
    cmbA2['values'] = ('Purpose', 'Channel', 'Dimmer', 'Address', 'Position', 'Unit#', 'Instrument Type', 'Load', 'Accessory', 'Color', 'Gobo', 'Gobo Size', 'Circiut Name', 'Circuit#', 'Cable', 'Data Cable', 'Mark', 'System', 'User 1', 'User 2', 'User 3', 'User 4', 'User 5', 'User 6', 'User 7', 'User 8', 'User 9', 'User 10', 'User 11', 'User 12', 'User 13', 'User 14', 'User 15', 'User 16', 'User 17', 'User 18', 'User 19', 'User 20', 'User 21', 'User 22', 'User 23', 'User 24', 'Scenery', 'Focus L/R', 'Focus U/D', 'Focus Note', 'US', 'DS', 'SR', 'SL', 'Top', 'Bot', 'Focus Status', 'Axis', 'Beam', 'VW Layer', 'VW Label Legend', 'VW Class', 'VW X Coordinate', 'VW Y Coordinate', 'VW Z Coordinate', 'VW Symbol Rotation', 'VW Focus Plot', 'Order of Light within Position', 'LightWright ID', 'Vectorworks UID', 'Symbol', 'On Light Plot', 'Universe', 'DMX#', 'Dimmer Phase', 'Position Order', 'Work Note Status', 'Device Type', 'Color Frame', '"When, What and Who Changed"', 'Position & Unit#', 'Instrument Type & Accessory', 'Instrument Type & Load', 'Instrument Type & Accessory & Load', 'Circiut Name & Circiut#', 'Color & Gobo', 'Color Flags', 'DMX Qty', 'Instrument Type Weight')
    cmbA3['values'] = ('Purpose', 'Channel', 'Dimmer', 'Address', 'Position', 'Unit#', 'Instrument Type', 'Load', 'Accessory', 'Color', 'Gobo', 'Gobo Size', 'Circiut Name', 'Circuit#', 'Cable', 'Data Cable', 'Mark', 'System', 'User 1', 'User 2', 'User 3', 'User 4', 'User 5', 'User 6', 'User 7', 'User 8', 'User 9', 'User 10', 'User 11', 'User 12', 'User 13', 'User 14', 'User 15', 'User 16', 'User 17', 'User 18', 'User 19', 'User 20', 'User 21', 'User 22', 'User 23', 'User 24', 'Scenery', 'Focus L/R', 'Focus U/D', 'Focus Note', 'US', 'DS', 'SR', 'SL', 'Top', 'Bot', 'Focus Status', 'Axis', 'Beam', 'VW Layer', 'VW Label Legend', 'VW Class', 'VW X Coordinate', 'VW Y Coordinate', 'VW Z Coordinate', 'VW Symbol Rotation', 'VW Focus Plot', 'Order of Light within Position', 'LightWright ID', 'Vectorworks UID', 'Symbol', 'On Light Plot', 'Universe', 'DMX#', 'Dimmer Phase', 'Position Order', 'Work Note Status', 'Device Type', 'Color Frame', '"When, What and Who Changed"', 'Position & Unit#', 'Instrument Type & Accessory', 'Instrument Type & Load', 'Instrument Type & Accessory & Load', 'Circiut Name & Circiut#', 'Color & Gobo', 'Color Flags', 'DMX Qty', 'Instrument Type Weight')
    cmbA4['values'] = ('Purpose', 'Channel', 'Dimmer', 'Address', 'Position', 'Unit#', 'Instrument Type', 'Load', 'Accessory', 'Color', 'Gobo', 'Gobo Size', 'Circiut Name', 'Circuit#', 'Cable', 'Data Cable', 'Mark', 'System', 'User 1', 'User 2', 'User 3', 'User 4', 'User 5', 'User 6', 'User 7', 'User 8', 'User 9', 'User 10', 'User 11', 'User 12', 'User 13', 'User 14', 'User 15', 'User 16', 'User 17', 'User 18', 'User 19', 'User 20', 'User 21', 'User 22', 'User 23', 'User 24', 'Scenery', 'Focus L/R', 'Focus U/D', 'Focus Note', 'US', 'DS', 'SR', 'SL', 'Top', 'Bot', 'Focus Status', 'Axis', 'Beam', 'VW Layer', 'VW Label Legend', 'VW Class', 'VW X Coordinate', 'VW Y Coordinate', 'VW Z Coordinate', 'VW Symbol Rotation', 'VW Focus Plot', 'Order of Light within Position', 'LightWright ID', 'Vectorworks UID', 'Symbol', 'On Light Plot', 'Universe', 'DMX#', 'Dimmer Phase', 'Position Order', 'Work Note Status', 'Device Type', 'Color Frame', '"When, What and Who Changed"', 'Position & Unit#', 'Instrument Type & Accessory', 'Instrument Type & Load', 'Instrument Type & Accessory & Load', 'Circiut Name & Circiut#', 'Color & Gobo', 'Color Flags', 'DMX Qty', 'Instrument Type Weight')

    #Place on screen attributes
    MainFrame.place(x=50, y=120)

    cmbA1.place(x=10, y=10)
    cmbA2.place(x=10, y=35)
    cmbA3.place(x=10, y=60)
    cmbA4.place(x=10, y=85)

    #Utility Addons
    cmbA1.current(0)
    cmbA2.current(1)
    cmbA3.current(2)
    cmbA4.current(3)

    MScreen.bind('<Configure>', WindowSize)
    MScreen.config(menu=MenuBar)
    MScreen.mainloop()

MainScreen()


#Documentation/Outside Sources
#"https://www.tutorialspoint.com/python/tk_menu.htm"
#"https://stackoverflow.com/questions/16429716/opening-file-tkinter"
