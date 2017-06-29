# 
# @author Jake Runyan 
# @git www.github.com/runyanjake/summersim
# @file /summergame/simulation.py
# 

#LIBRARY IMPORTS
import tkinter as tk
import random as rand

#LOCAL IMPORTS
import gui

#FIELDS
width = 800 #also hardcoded in gui.py
height = 600 #also hardcoded in gui.py
num_width = 100
num_height = 100
field_data = [[0 for x in range(num_width)] for y in range(num_height)]

#FUNCTIONS

#draw
#modifies array, declared above
def repaint(frame):
	canvas = tk.Canvas(frame,width=width,height=height) #setting size doesn't work with winfo_width
	canvas.create_line(0,0,100,100)
	print('width is {}'.format(frame.winfo_width()))
	canvas.pack()
	#drawing constants
	wid = width
	hei = height
	cell_height = int(wid/num_width)
	cell_width = int(hei/num_height)
	for x in range(num_width):
		for y in range(num_height):
			cell_loc_w = int(wid/num_width) * x
			cell_loc_h = int(hei/num_height) * y
			color = 'black'
			col = rand.randint(1,5)
			if col == 1:
				color = 'red'
			elif col == 2:
				color = 'orange'
			elif col == 3:
				color = 'yellow'
			elif col == 4:
				color = 'green'
			elif col == 5:
				color = 'cyan'
			canvas.create_rectangle(cell_loc_w, cell_loc_h, cell_loc_w + cell_width, cell_loc_h + cell_height, fill=color)
	

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
