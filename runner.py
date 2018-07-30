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

topFrame_Label = Label(topFrame, text="Runner")
topFrame_Label.pack()

middleFrame_Label = Label(middleFrame, text="Updates HASS configurations at the click of a button", )
middleFrame_Label.pack()

bottomFrame_Label = Label(middleFrame, text="Click to deploy")
bottomFrame_Label.pack()

configButton = Button(middleFrame, text="Send Config", fg="red", bg="black")
configButton.pack(side="top")

groupsButton = Button(middleFrame, text="Send Groups", fg="red", bg="black")
groupsButton.pack(side="left")

sensorsButton = Button(middleFrame, text="Send Sensors", fg="red", bg="black")
sensorsButton.pack(side="right")

allButton = Button(bottomFrame, text="Send All", fg="red", bg="black")
allButton.pack(side="top")

server = "0.0.0.0"
rootdirectory = "/homeassistant/.homeassistant"


root.minsize(400, 400)
root.mainloop()

doowoop = Tk()

topFrame = Frame(doowoop)
topFrame.pack(side=TOP)

doowoop.minsize(400, 400)
doowoop.mainloop()
