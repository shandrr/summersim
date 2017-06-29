#
# @author Jake Runyan
# @git www.github.com/runyanjake/summersim
# @file /summersim/gui.py
#
# Window architecture adapted from https://stackoverflow.com/questions/7546050/switch-between-two-tk.Frames-in-tkinter
#

#LIBRARY IMPORTS
from tkinter import font as tkfont
from tkinter import Widget
import tkinter as tk


#LOCAL IMPORTS
import fileio as fio
import simulation as sim

#CLASSES

#FUNCTIONS

#VARIABLES
width = 1000 #also hardcoded in simulation.py
height = 750 #also hardcoded in simulation.py
ctrllr_background = 'red'
stats_background = 'green'
viewr_background = 'blue'
default_background = 'gray'
default_foreground = 'white'
default_textcolor = 'black'

#application class
class Sim(tk.Tk):
	def __init__(self, *args, **kwargs):
		tk.Tk.__init__(self, *args, **kwargs)

		self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

		# the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
		container = tk.Frame(self,width=width,height=height)
		container.pack(side="top", fill="both", expand=True)
		container.grid_rowconfigure(0, weight=1)
		container.grid_columnconfigure(0, weight=1)

		container.configure(background=default_background)

		self.frames = {}
		for F in (LandingPage, SimPage, HelpPage, ResultsPage):
			page_name = F.__name__
			frame = F(parent=container, controller=self)
			self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
			frame.grid(row=0, column=0, sticky="nsew")
		self.show_frame("LandingPage")
		#make it move to top window real quick. TODO
		# self.attributes('-topmost', 1)
		# self.attributes('-topmost', 0)
		#define hotkeys
		self.bind("<Escape>", lambda e: e.widget.quit())
		self.bind("<h>", lambda e: self.show_frame("HelpPage"))

	def show_frame(self, page_name):
        #'''Show a frame for the given page name'''
		frame = self.frames[page_name]
		frame.tkraise()

#class defining landing page
class LandingPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.configure(background=default_background)
		#define label
		label = tk.Label(self, text="Home", font=controller.title_font, bg=default_background, fg=default_textcolor)
		label.pack(side="top", fill="x", pady=10)
		#transition control
		simbutton = tk.Button(self, text="Go to the sim page", command=lambda: controller.show_frame("SimPage"), bg=default_background, fg=default_foreground)
		simbutton.pack()
		helpbutton = tk.Button(self, text="Go to the help page", command=lambda: controller.show_frame("HelpPage"), bg=default_background, fg=default_foreground)
		helpbutton.pack()

#class defining simulation page
class SimPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.configure(background=default_background)
		#define labels
		label = tk.Label(self, text="Simulation", font=controller.title_font, bg=default_background, fg=default_textcolor)
		label.pack(side="top", fill="x", pady=10)
		#set up controller bottom window
		ctrls = tk.Frame(self, width=width, height=int(height/5.0), background = ctrllr_background)
		# controllerlabel = Label(controller, text="controller", background = ctrllr_background)
		# controllerlabel.pack()
		ctrls.pack(side=tk.BOTTOM)
		       
		#set up stats RHS
		stats = tk.Frame(self, width=((width/10)*3), height=int((height/5.0)*4), background = stats_background)
		# statslabel = Label(stats, text="stats")
		# statslabel.pack()
		stats.pack(side=tk.RIGHT)
		
		#****************************************** CURRENTLY IN PLACE OF VIEWER
		#add in the simulation window(will eventually be one of many options)
		sim.repaint(self)
		#******************************************

		#transition control
		homebutton = tk.Button(ctrls, text="Go to the homepage", command=lambda: controller.show_frame("LandingPage"), bg=default_background, fg=default_foreground)
		homebutton.pack()
		resultsbutton = tk.Button(ctrls, text="Go to the results page", command=lambda: controller.show_frame("ResultsPage"), bg=default_background, fg=default_foreground)
		resultsbutton.pack()
		reseedbutton = tk.Button(ctrls, text="Re-seed", command=lambda: sim.repaint(self))
		reseedbutton.pack()

#class defining help page
class HelpPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.configure(background=default_background)
		#create labels
		label = tk.Label(self, text="Help", font=controller.title_font)
		label.configure(bg=default_background, fg=default_textcolor)
		label.pack(side="top", fill="x", pady=10)
		#transition control
		homebutton = tk.Button(self, text="Go to the home page", command=lambda: controller.show_frame("LandingPage"), bg=default_background, fg=default_foreground)
		homebutton.pack()

#class defining results page
class ResultsPage(tk.Frame):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.configure(background=default_background)
		#create labels
		label = tk.Label(self, text="Results", font=controller.title_font)
		label.configure(bg=default_background, fg=default_textcolor)
		label.pack(side="top", fill="x", pady=10)
		#transition control
		homebutton = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("LandingPage"), bg=default_background, fg=default_foreground)
		homebutton.pack()
		simbutton = tk.Button(self, text="Return to sim", command=lambda: controller.show_frame("SimPage"), bg=default_background, fg=default_foreground)
		simbutton.pack()




#create the program window
#win=0: landing page
#win=1: sim page
def create_GUI():
	simulation = Sim()
	#create a non-resizeable 800x600window
	simulation.geometry('{}x{}'.format(width, height))
	simulation.resizable(width=True, height=True)
	simulation.mainloop()

#save game state to a file
def save_simstate():
    print('save_simstate TODO')

#load existing game state from file, if such files exist.
def load_simstate(filename):
    print('load_simstate TODO')
