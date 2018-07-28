#!/usr/bin/pythonw
__author__ = 'Jay Diggily'

from Tkinter import *

import tkFont



root = Tk()

font = tkFont.Font(family = "Helvetica")

topFrame = Frame(root)
topFrame.pack(side=TOP)

middleFrame = Frame(root)
middleFrame.pack(side=TOP)

bottomFrame = Frame(root, bg="green")
bottomFrame.pack(side=BOTTOM)

topFrame_Label = Label(topFrame, text="Runner", )
topFrame_Label.pack()

middleFrame_Label = Label(middleFrame, text="Updates HASS configurations at the click of a button", )
middleFrame_Label.pack()

bottomFrame_Label = Label(middleFrame, text="Click to deploy")
bottomFrame_Label.pack()

configButton = Button(middleFrame, text="Button", fg="red", bg="black")
configButton.pack()

groupsButton = Button(middleFrame, text="Button", fg="red", bg="black")
groupsButton.pack()

sensorsButton = Button(middleFrame, text="Button", fg="red", bg="black")
sensorsButton.pack()

allButton = Button(middleFrame, text="Button", fg="red", bg="black")
allButton.pack()


root.minsize(400, 400)
root.mainloop()
