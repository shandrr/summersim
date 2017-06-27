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

#return the time elapsed
print('Exiting after',end='')
exit_time = time.time()
elapsed_time = exit_time - start_time
if int(elapsed_time / 86400) > 0:
	days = int(elapsed_time / 86400)
	elapsed_time = elapsed_time - (days * 86400)
	if days == 1:
		print(' {} day'.format(days),end='')
	else:
		print(' {} days'.format(days),end='')
if int(elapsed_time / 3600) > 0:
	hrs = int(elapsed_time / 3600)
	elapsed_time = elapsed_time - (hrs * 3600)
	if hrs == 1:
		print(' {} hour'.format(hrs),end='')
	else:
		print(' {} hours'.format(hrs),end='')
if int(elapsed_time / 60) > 0:
	mins = int(elapsed_time / 60)
	elapsed_time = elapsed_time - (mins * 60)
	if mins == 1:
		print(' {} minute'.format(mins),end='')
	else:
		print(' {} minutes'.format(mins),end='')
if int(elapsed_time) == 1:
	print(' {} second'.format(int(elapsed_time)),end='')
elif int(elapsed_time) == 0:
	print(' 0 seconds',end='')
else:
	print(' {} seconds'.format(int(elapsed_time)),end='')
print('.')
