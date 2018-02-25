#!/usr/bin/python

import tkinter as tk
from tkinter import messagebox
from apscheduler.schedulers.blocking import BlockingScheduler
from Cleano import Cleano
import os

limit = 5 #number of files
time_before_alert = 5 #in hours

def popup():

	home = os.path.expanduser('~')
	desktop = os.path.join(home,'Desktop')
	files = list()
	dirs = list()

	c = Cleano(home)
	c.list_files_and_directories(files, dirs, desktop)
	
	if len(files) > limit:
		root = tk.Tk()
		root.withdraw()
		result = messagebox.askyesno("Title", "You have "+str(len(files))+' unorganized files.\n'+"Do you wish to \norganize your Desktop?")
		
		if result==True:
			c.clean_desktop(desktop)			
		else:
			pass

def main():
	
	scheduler = BlockingScheduler()
	job = scheduler.add_job(popup, 'interval', hours = time_before_alert)
	
	try:
		scheduler.start()
	except SystemExit:
		if root:
			root.destroy()

main()