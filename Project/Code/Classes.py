from tkinter import *
from tkinter.ttk import *

class Item():
    def __init__(self, screen, arrayPoint, attr1, attr2, attr3, attr4):
        self.arrayPoint = arrayPoint
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3
        self.attr4 = attr4

        self.lblFrame = Frame(screen, style="Frame2.TFrame", width=300, height=200)

        self.barFrameA1 = Scrollbar(self.lblFrame)#, orient='horizontal', width=20)
        self.barFrameA2 = Scrollbar(self.lblFrame)
        self.barFrameA3 = Scrollbar(self.lblFrame)
        self.barFrameA4 = Scrollbar(self.lblFrame)

        self.lblAttr1 = Text(self.lblFrame, height=1, width=15, wrap='none', xscrollcommand=self.barFrameA1.set)
        self.lblAttr2 = Text(self.lblFrame, height=1, width=15, wrap='none', xscrollcommand=self.barFrameA2.set)
        self.lblAttr3 = Text(self.lblFrame, height=1, width=15, wrap='none', xscrollcommand=self.barFrameA3.set)
        self.lblAttr4 = Text(self.lblFrame, height=1, width=15, wrap='none', xscrollcommand=self.barFrameA4.set)

        #self.lblAttr2 = Label(self.lblFrame, text=self.attr2)
        #self.lblAttr3 = Label(self.lblFrame, text=self.attr3)
        #self.lblAttr4 = Label(self.lblFrame, text=self.attr4)

        self.lblAttr1.insert(END, self.attr1)
        self.lblAttr2.insert(END, self.attr2)
        self.lblAttr3.insert(END, self.attr3)
        self.lblAttr4.insert(END, self.attr4)

        self.barFrameA1.config(command=self.lblAttr1.xview)
        self.barFrameA2.config(command=self.lblAttr2.xview)
        self.barFrameA3.config(command=self.lblAttr3.xview)
        self.barFrameA4.config(command=self.lblAttr4.xview)

    def labelMake(self, screen):
        print(self.attr1)

    def labelDestroy(self):
        #print("Test")
        self.lblFrame.destroy()

    def labelShow(self, xpos, ypos):
        #print('Placeholder')
        NewYPos = 0
        self.lblFrame.grid(row=ypos, column=xpos, padx=10, pady=10)
        self.lblAttr1.grid(row=1, column=2, padx=2, pady=10)
        NewYPos = NewYPos + 20
        self.lblAttr2.grid(row=2, column=2, padx=10, pady=10)
        NewYPos = NewYPos + 20
        self.lblAttr3.grid(row=3, column=2, padx=10, pady=10)
        NewYPos = NewYPos + 20
        self.lblAttr4.grid(row=4, column=2, padx=10, pady=10)
        NewYPos = NewYPos + 20

        self.barFrameA1.grid(row=1, column=3, padx=5, columnspan=10, sticky='e')
        self.barFrameA2.grid(row=2, column=3, padx=5, columnspan=10, sticky='e')
        self.barFrameA3.grid(row=3, column=3, padx=5, columnspan=10, sticky='e')
        self.barFrameA4.grid(row=4, column=3, padx=5, columnspan=10, sticky='e')

        #self.lblFrame.update()
        #print(self.lblFrame.winfo_width())
#change labels to text
#change from .place to .grid
#scrollbar not chaning size WHY!??????

#JUST PUT 4 SCROLLBARS ON THE SIDE VERTICALLY. IT'LL WORK AND YOU CAN MOVE ON TO THE MORE IMPORTANT PARTS!!!

#https://www.geeksforgeeks.org/python-grid-method-in-tkinter/?ref=lbp
#https://www.geeksforgeeks.org/python-tkinter-text-widget/?ref=lbp


#create a frame encompassing the entire window
#create smaller frames inside for the different elements
#this inlcudes MainFrame
#then allows

#???????? IM SO CONFUSED!

#limit frame size and give it a scrollbar?
