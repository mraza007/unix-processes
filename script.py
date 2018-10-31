#! /usr/bin/python3
"""Unix Processes.

Usage:
  basic.py hello <name>
  basic.py goodbye <name>
  basic.py add <x>
  basic.py (-h | --help)

Options:
  -h --help     Show this screen.

"""
from docopt import docopt
import psutil
from termcolor import colored, cprint
def process_id():
	for process in psutil.pids():
		p = psutil.Process(process)
		ids = colored(process,'green', attrs=['bold'])
		names = colored(p.name(),'cyan',attrs=['bold']) 
		print('Process ID: ' + ids +' Name: ' + names)

process_id()







# text = colored('Hello, World!', 'green', attrs=[ 'blink','bol'])
# print(text)
# cprint('Hello, World!', 'green', 'on_red')









# Commandline logic
# if __name__ == '__main__':
#     arguments = docopt(__doc__)

#     # if an argument called hello was passed, execute the hello logic.
#     if arguments['hello']:
#         hello(arguments['<name>'])
#     elif arguments['goodbye']:
#         goodbye(arguments['<name>'])
#     elif arguments['add']:
#     	add(int(arguments['<x>']))