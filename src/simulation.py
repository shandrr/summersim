# 
# @author Jake Runyan 
# @git www.github.com/runyanjake/summersim
# @file /summergame/simulation.py
# 

#LIBRARY IMPORTS
import tkinter as tk

#LOCAL IMPORTS
import gui

#FIELDS
field_width = 100
field_height = field_width
field_data = [[0 for x in range(field_width)] for y in range(field_height)]

#FUNCTIONS

#class for creating the grid window, meant to be refreshed rapidly.
class Sim2DField(tk.Canvas):
	def __init__(self, parent, controller):
		tk.Frame.__init__(self, parent)
		self.controller = controller
		self.configure(background='black')
		for x in range(field_width):
			for y in range(field_height):
				print('hi')
	#start moving
	def run():
		print ('running')
	#stop moving
	def pause():
		print ('paused')




#
def start_sim():
	gui.load_simstate('tmp')
	gui.create_GUI()
	
def step_sim():
	print('step_sim TODO')

def run_sim():
	print('run_sim TODO')

def pause_sim():
	print('pause_sim TODO')

def close_sim():
	print('close_sim TODO')
