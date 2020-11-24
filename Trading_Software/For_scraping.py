# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:49:07 2020

@author: manas
"""
import os
import datetime as dt
import pandas as pd
from matplotlib import style
import matplotlib.pyplot as plt
import pandas_datareader.data as web
from alpha_vantage.timeseries import TimeSeries 
from tkinter import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk) 

'''
ts = TimeSeries(key='A4GJGEAIETZ3UBQZ', output_format='pandas')
data, metadata= ts.get_intraday(symbol='AAPL',interval='30min',outputsize='full')
df=len(data.loc['2020-10-21'].index);
end=dt.date.today();
df1=data['2. high'].loc[end];
print(df1)
print(df)
'''
'''
start = dt.datetime(2015, 1, 1)
end = dt.datetime.now()
f=ts.get_daily("AAPL", "av-daily", start=start,end=end,api_key=os.getenv('A4GJGEAIETZ3UBQZ'))
f.loc["2017-02-09"]
plt.show(f);'''


# plot function is created for 
# plotting the graph in 
# tkinter window 
def plot(): 

	# the figure that will contain the plot 
	fig = Figure(figsize = (5, 5), 
				dpi = 100) 

	# list of squares 
	y = [i**2 for i in range(101)] 

	# adding the subplot 
	plot1 = fig.add_subplot(111) 

	# plotting the graph 
	plot1.plot(y) 

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
