# 
# @author Jake Runyan 
# @git www.github.com/runyanjake/summersim
# @file /summergame/main.py
# 

#LIBRARY IMPORTS
import numpy as np 
import time
import string

#LOCAL IMPORTS
import fileio as fio
import neuralnet as nnet
import gui as gui
import fs_tools as opsys
import simulation as sim

##################################
#________________________________#
#____O___O__OOOO__OOOOO__O__O____#
#____OO_OO__O__O____O____OO_O____#
#____O_O_O__OOOO____O____O_OO____#
#____O___O__O__O__OOOOO__O__O____#
#________________________________#
##################################

#take note of start time
start_time = time.time()

#
# Make sure we're safe to run.
#
print('\nChecking envorinment...')
#check environment
opsys.env_check()
#check filesystem structure
fio.check_filesystem()
print('Success.\n')

#
# Run program.
#
print('Beginning simulation...')
#run program
sim.start_sim()
print('Success.\n')

print('Exiting after {} seconds.'.format(time.time()-start_time))
