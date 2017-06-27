# 
# @author Jake Runyan 
# @git www.github.com/runyanjake/summersim
# @file /summergame/fs_tools.py
# 

#LIBRARY IMPORTS
import os

#LOCAL IMPORTS


#FUNCTIONS

#create a file
def create_file(name):
	print('create_file TODO')

#read text in from a file
def read_file(path):
	print('read_file TODO')

#process environment conditions
def env_check():
	if os.name == 'posix':
		print('Operating system module: POSIX')
		os_is_posix = 1
	elif os.name == 'nt':
		print('Operating system module: NT')
	elif os.name == 'java':
		print('Operating system module: JAVA')
	else:
		print('No operating system module found.')
		return -1;