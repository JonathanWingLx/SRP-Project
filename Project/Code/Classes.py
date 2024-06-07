from tkinter.ttk import *

class Item():
    def __init__(self, screen, arrayPoint, attr1, attr2, attr3, attr4):
        self.arrayPoint = arrayPoint
        self.attr1 = attr1
        self.attr2 = attr2
        self.attr3 = attr3
        self.attr4 = attr4

        self.lblFrame = Frame(screen, style="Frame2.TFrame", width=50, height=100)

        self.barFrame = Scrollbar(self.lblFrame, orient='horizontal')

        self.lblAttr1 = Label(self.lblFrame, text=self.attr1, xscrollcommand=self.barFrame.set)
        self.lblAttr2 = Label(self.lblFrame, text=self.attr2)
        self.lblAttr3 = Label(self.lblFrame, text=self.attr3)
        self.lblAttr4 = Label(self.lblFrame, text=self.attr4)

    def labelMake(self, screen):
        print(self.attr1)


    def labelShow(self, xpos, ypos):
        print('Placeholder')
        NewYPos = 0
        self.lblFrame.place(x=xpos, y=ypos)
        self.lblAttr1.place(x=0, y=NewYPos)
        NewYPos = NewYPos + 20
        self.lblAttr2.place(x=0, y=NewYPos)
        NewYPos = NewYPos + 20
        self.lblAttr3.place(x=0, y=NewYPos)
        NewYPos = NewYPos + 20
        self.lblAttr4.place(x=0, y=NewYPos)
        NewYPos = NewYPos + 20
        self.barFrame.place(x=0, y=NewYPos)

#change labels to text
#change from .place to .grid


#create a frame encompassing the entire window
#create smaller frames inside for the different elements
#this inlcudes MainFrame
#then allows

#???????? IM SO CONFUSED!

#limit frame size and give it a scrollbar?
