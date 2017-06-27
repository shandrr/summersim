#
# @author Jake Runyan
# @git www.github.com/runyanjake/summersim
# @file /summersim/gui.py
#

#LIBRARY IMPORTS
from tkinter import *

#LOCAL IMPORTS
import fileio as fio

#CLASSES

#FUNCTIONS

#VARIABLES
root = Tk() #where we'll put stuff in tkinter
width = 800
height = 600

#EXAMPLE MAKING BLANK WINDOW (uses root defined above)
#label = Label(root, text = "newlabel") #create new label
#label.pack() #pack label, get ready to do stuff.
#root.mainloop() #puts root in infinite loop until we close so it doesnt open and close in a frame.

#create the program window
def create_GUI():
    #non-resizeable 800x600window
    root.geometry('{}x{}'.format(width, height))
    root.resizable(width=False, height=False)
        
    #setup exit hotkey
    root.bind("<Escape>", lambda e: e.widget.quit())
        
    #set up controller bottom window
    controller = Frame(root)
    controllerlabel = Label(controller, text="controller")
    controllerlabel.pack()
    controller.pack(side=BOTTOM)
        
    #set up stats RHS
    stats = Frame(root)
    statslabel = Label(stats, text="stats")
    statslabel.pack()
    stats.pack(side=RIGHT)
        
    #set up viewer LHS
    viewer = Frame(root)
    viewerlabel = Label(viewer, text="viewer")
    viewerlabel.pack()
    viewer.pack(side=LEFT)

#close the program window
def close_GUI():
    print('close_GUI TODO')

#update the user interface
def show_GUI():
    #show gui to window.
    root.mainloop()
    #root.after(1000, lambda: root.focus_force())

#save game state to a file
def save_simstate():
    print('save_simstate TODO')

#load existing game state from file, if such files exist.
def load_simstate(filename):
    print('load_simstate TODO')
