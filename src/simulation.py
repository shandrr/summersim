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
width = 720 #also hardcoded in gui.py
height = 480 #also hardcoded in gui.py
cell_width = 5
cell_height = 5
num_width = int(width/cell_width)
num_height = int(height/cell_height)
field_type = [[0 for x in range(num_width)] for y in range(num_height)]
field_attr_saturation = [[0 for x in range(num_width)] for y in range(num_height)]

#FUNCTIONS

#draw
#modifies array, declared above
def repaint(canvas):
	print('repainting...')
	#delete all elements to ready for repaint
	canvas.grid_forget()
	#put into frame
	canvas.pack()

	for x in range(num_width):
		for y in range(num_height):
			cell_loc_w = cell_width * x
			cell_loc_h = cell_height * y
			color = 'black'
			col = field_type[y][x]
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
			canvas.create_rectangle(cell_loc_w, cell_loc_h, cell_loc_w + cell_width, cell_loc_h + cell_height, fill=color, outline='')
	

#
def start_sim():
	gui.load_simstate('tmp')
	gui.create_GUI()

#randomizes the sim grid color and saturation values
def randomize_sim(canvas):
	for x in range(num_width):
		for y in range(num_height):
			col = rand.randint(1,5)
			field_type[y][x] = col
			sat = rand.randint(1,255)
			field_attr_saturation[y][x] = sat
	repaint(canvas)

def save_sim_grid(filename):
	print('save_sim_grid TODO')

def load_sim_grid(filename):
	print('load_sim_grid TODO')
	
def step_sim():
	print('step_sim TODO')

def run_sim():
	print('run_sim TODO')

def pause_sim():
	print('pause_sim TODO')

def close_sim():
	print('close_sim TODO')
