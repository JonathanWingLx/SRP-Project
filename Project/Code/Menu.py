from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import *
from sqlite3 import *

from ReadDB import *
from Classes import *
from ScrollableFrame import *
from SearchLogic import *

global dbObjArray
dbObjArray = []

def MainScreen():

    def RefreshPlace():
        #print("Test")
        MainFrame.update()
        MaxX = MainFrame.canvas.winfo_width() // 195
        temp = 0

        #print(MainFrame.scrollable_frame.winfo_width())
        #print(MaxX)
        #bug where shrinking the screen causes the first row to be
        #1 item longer, fixes when regrowing the screen

        if MaxX != temp:
            x = 0
            y = 0

            i = 0

            for e in dbObjArray:
                if x + 1 > MaxX:
                    x = 0
                    y += 1
                else:
                    dbObjArray[i].labelShow(x, y)
                    x += 1
                i += 1
            temp = MaxX
        else:
            return


    def WindowSize(event):
        NewWidth = event.width
        #NewWidth = NewWidth - 100
        NewHeight = event.height
        #print(event.widget)
        if event.widget == MScreen:
            NewWidth = NewWidth - 50
            NewHeight = NewHeight - 100
            #MainFrame.config(width = NewWidth, height = NewHeight)
            MainFrame.scrollable_frame.configure(width = NewWidth, height = NewHeight)
            MainFrame.canvas.configure(width = NewWidth, height = NewHeight)
            RefreshPlace()

            #print(MainFrame.winfo_width())
            #print(MainFrame.scrollable_frame.winfo_width())
            #print(MainFrame.canvas.winfo_width())
            #print()

    def Text():
        print("Test")
        print(dbObjArray[1])

    def objArray(Array):
        print("Test")
        global dbObjArray

        dbLen = len(Array)
        dbObjArray = []
        i = 0
        for x in range(dbLen):
            #print("Test")

            #Object init on sepertae file
            #define object within loop
            ItemTemp = Item(MainFrame.scrollable_frame, i, Array[i][cmbA1.current()], Array[i][cmbA2.current()], Array[i][cmbA3.current()], Array[i][cmbA4.current()])
            #Other options for obj come from dropdown options on screen

            #dbObjArray.append() with each object
            dbObjArray.append(ItemTemp)
            #create dbObjArray
            #Object attributes - Channel, array pointer + any other data shown on screen

            #each item on screen is an object
            #the details of the item is stored in the object
            #go through the object array and place them on screen
            i += 1

    def AddItems(fileName):
        #global dbObjArray
        print("Test")
        #Grab a list from the database
        #parse in filename?
        file = connect("Test.db")
        cs = file.cursor()
        fileName = fileName.replace(' ', '_')
        fileName = fileName.split('/')

        cs.execute("SELECT * FROM {}".format('DB_'+fileName[-1]))
        dbArray = cs.fetchall()
        objArray(dbArray)
        #print(dbArray[0][1])
        #for loop to look at each item in the database
            #create object with channel, dimmer and address

        #Check code
        #End of Check

        RefreshPlace()

        #dbObjArray[1].labelMake(MScreen)
        #dbObjArray[0].labelShow(0, 0)
        #dbObjArray[1].labelShow(1, 0)
        #dbObjArray[2].labelShow(2, 0)
        #dbObjArray[3].labelShow(3, 0)
        #dbObjArray[4].labelShow(4, 0)

        #each item is 300px + 20px
        #width of MainFrame/320 round down = max x

        #print(cmbA1.current())
        #add objects to screen
        #take window size - extra bits on screen for usable size
        #if x + gap > usablesize(x)
        #then x = 0ish and y = y + gap
        #else x = x + gap

        #use frame for both usable area and each item
        #add scroll bar for master frame

        #https://tkdocs.com/tutorial/widgets.html#frame

    def OpenFile():
        global filename
        filename = askopenfilename(parent=MScreen)
        #f = open(filename)
        #print(f.read())
        #Read(filename)
        AddItems(filename)

    def ItemSearch():
        #print("Test")
        SearchedArray = Search(filename, cmbChoice1.current(), Choice2.get())

        i = 0
        dbLen = len(dbObjArray)
        for x in range(dbLen):
            dbObjArray[i].labelDestroy()
            i += 1

#        dbObjArray.labelDestroy()

#        print(SearchedArray)

        objArray(SearchedArray)
        RefreshPlace()

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
    MFX = MScreen.winfo_screenwidth() - 50
    MFY = MScreen.winfo_screenheight() - 50
    MainFrame = ScrollableFrame(MScreen, height=MFY, width=MFX)
    MainFrame.scrollable_frame.config(style="TFrame", height=MFY, width=MFX)

    #MainScroll = Scrollbar(MainFrame)

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

    Choice2 = StringVar(MScreen)

    cmbChoice1 = Combobox(MScreen, width=10)
    cmbChoice2 = Combobox(MScreen, width=10, textvariable=Choice2)

    cmbChoice1['values'] = ('Missing', 'Duplicate')
    cmbChoice2['values'] = ('Purpose', 'Channel', 'Dimmer', 'Address', 'Position', 'Unit#', 'Instrument Type', 'Load', 'Accessory', 'Color', 'Gobo', 'Gobo Size', 'Circiut Name', 'Circuit#', 'Cable', 'Data Cable', 'Mark', 'System', 'User 1', 'User 2', 'User 3', 'User 4', 'User 5', 'User 6', 'User 7', 'User 8', 'User 9', 'User 10', 'User 11', 'User 12', 'User 13', 'User 14', 'User 15', 'User 16', 'User 17', 'User 18', 'User 19', 'User 20', 'User 21', 'User 22', 'User 23', 'User 24', 'Scenery', 'Focus L/R', 'Focus U/D', 'Focus Note', 'US', 'DS', 'SR', 'SL', 'Top', 'Bot', 'Focus Status', 'Axis', 'Beam', 'VW Layer', 'VW Label Legend', 'VW Class', 'VW X Coordinate', 'VW Y Coordinate', 'VW Z Coordinate', 'VW Symbol Rotation', 'VW Focus Plot', 'Order of Light within Position', 'LightWright ID', 'Vectorworks UID', 'Symbol', 'On Light Plot', 'Universe', 'DMX#', 'Dimmer Phase', 'Position Order', 'Work Note Status', 'Device Type', 'Color Frame', '"When, What and Who Changed"', 'Position & Unit#', 'Instrument Type & Accessory', 'Instrument Type & Load', 'Instrument Type & Accessory & Load', 'Circiut Name & Circiut#', 'Color & Gobo', 'Color Flags', 'DMX Qty', 'Instrument Type Weight')

    lblFind = Label(MScreen, text="Find all with")

    btnFind = Button(MScreen, text="Search", command=ItemSearch)

    #Place on screen attributes
    MainFrame.grid(row=12, column=0, columnspan=10, padx=10, pady=5, sticky='w')
    #MainFrame.scrollable_frame.grid_propagate(False)

    #MainScroll.grid(column=10, sticky='e')
    #MainFrame.config(yscrollcommand=MainScroll.set)
    #MainScroll.config(command=MainFrame.yview)

    cmbA1.grid(row=1, column=0, sticky='w', padx=10, columnspan=1)
    cmbA2.grid(row=2, column=0, sticky='w', padx=10, columnspan=1)
    cmbA3.grid(row=3, column=0, sticky='w', padx=10, columnspan=1)
    cmbA4.grid(row=4, column=0, sticky='w', padx=10, columnspan=1)

    cmbChoice1.grid(row=1, column=2, sticky='w')
    cmbChoice2.grid(row=1, column=3, sticky='w')

    lblFind.grid(row=1, column=1)

    btnFind.grid(row=1, column=4)

    #Utility Addons
    cmbA1.current(0)
    cmbA2.current(1)
    cmbA3.current(2)
    cmbA4.current(3)

    cmbChoice1.current(0)
    cmbChoice2.current(0)

    MScreen.bind('<Configure>', WindowSize)
    MScreen.config(menu=MenuBar)
    MScreen.mainloop()

MainScreen()

#Event for when cmbChoice1 is selected. Depending on choice
#Change options for cmbChoice2

#Documentation/Outside Sources
#"https://www.tutorialspoint.com/python/tk_menu.htm"
#"https://stackoverflow.com/questions/16429716/opening-file-tkinter"
