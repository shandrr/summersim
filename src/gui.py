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
ctrllr_background = 'red'
stats_background = 'green'
viewr_background = 'blue'


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
    controller = Frame(root, width=width, height=int(height/5.0), background = ctrllr_background)
    # controllerlabel = Label(controller, text="controller", background = ctrllr_background)
    # controllerlabel.pack()
    controller.pack(side=BOTTOM)
        
    #set up stats RHS
    stats = Frame(root, width=((width/10)*3), height=int((height/5.0)*4), background = stats_background)
    # statslabel = Label(stats, text="stats")
    # statslabel.pack()
    stats.pack(side=RIGHT)
        
    # set up viewer LHS
    viewer = Frame(root, width=((width/10)*7), height=int((height/5.0)*4), background = viewr_background)
    # viewerlabel = Label(viewer, text="viewer")
    # viewerlabel.pack()
    viewer.pack(side=LEFT)

#close the program window
def close_GUI():
    print('close_GUI TODO')

#update the user interface
def show_GUI():
    #show gui to window.
    root.focus_force()
    root.mainloop()

#save game state to a file
def save_simstate():
    print('save_simstate TODO')

#load existing game state from file, if such files exist.
def load_simstate(filename):
    print('load_simstate TODO')
