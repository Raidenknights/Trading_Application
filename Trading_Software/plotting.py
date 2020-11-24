# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 18:34:39 2020

@author: manas
"""

from tkinter import *
from matplotlib.figure import Figure 
import start_work as sw
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk) 

# plot function is created for 
# plotting the graph in 
# tkinter window
name=input("please enter the name of the company")
duration=input("please enter duration in min for ex 1min")
srtype=input("enter type") 
def plot(): 

	# the figure that will contain the plot 
	fig = Figure(figsize = (5, 5), 
				dpi = 100) 
	# list of squares 
	y = sw.work.select_name(name,duration,srtype);

	# adding the subplot 
	plot1 = fig.add_subplot(111) 
    
	# plotting the graph 
	plot1.plot(y[0],y[1])
    
    # creating the Tkinter canvas 
	# containing the Matplotlib figure 
	canvas = FigureCanvasTkAgg(fig, 
							master = window) 
	canvas.draw() 

	# placing the canvas on the Tkinter window 
	canvas.get_tk_widget().pack() 

	# creating the Matplotlib toolbar 
	toolbar = NavigationToolbar2Tk(canvas, 
								window) 
	toolbar.update() 

	# placing the toolbar on the Tkinter window 
	canvas.get_tk_widget().pack() 

# the main Tkinter window 
window = Tk() 

# setting the title 
window.title('Plotting in Tkinter') 

# dimensions of the main window 
window.geometry("500x500") 

# button that displays the plot 
plot_button = Button(master = window, 
					command = plot, 
					height = 2, 
					width = 10, 
					text = "Plot") 

# place the button 
# in main window 
plot_button.pack() 

# run the gui 
window.mainloop() 
