# 
# @author Jake Runyan 
# @git www.github.com/runyanjake/summersim
# @file /summergame/main.py
# 

#LIBRARY IMPORTS
import numpy as np 
import time
#import tkinter as tk #python default graphics package
import string

#LOCAL IMPORTS
import fileio as fio
import neuralnet as nnet
import gui as gui
import fs_tools as opsys


#run function
def run():
	fio.read_file('temp')

###################################
#_________________________________#
#____O___O__OOOO__OOOOO__O__O_____#
#____OO_OO__O__O____O____OO_O_____#
#____O_O_O__OOOO____O____O_OO_____#
#____O___O__O__O__OOOOO__O__O_____#
#_________________________________#
###################################

#take note of start time
start_time = time.time()

#check environment
opsys.env_check()

#run program
run()

print('Exiting after {} seconds.'.format(time.time()-start_time))
