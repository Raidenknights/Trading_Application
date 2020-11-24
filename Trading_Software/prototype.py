# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 18:29:08 2020

@author: manas
"""

import tkinter as tk
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image
import start_work as sw
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, 
NavigationToolbar2Tk)
from matplotlib.figure import Figure 
import post_processing as pstprc
#MAKE A VARIABLE SO THAT MAIN WINDOW CAN BE MADE
root=tk.Tk()
root.geometry("600x600")
root.title("Make Your Trading Analysis")
#THIS CLASS MAKES A NEW WINDOW AND CALL THE MAIN ANALYSIS CLASS FROM THE START_WORK.PY
class View_creation:
    name_gui=tk.StringVar()
    time_gui=tk.StringVar()
    sr_type_gui=tk.StringVar()
    date=tk.StringVar()
    #CALL FUNCTION FROM THE OTHER FILE TO EXECUTE THE MAIN WORK
    def perform_task():
        #creating another window for graph 
        graph=Toplevel(root)
        graph.geometry('800x800')
        #getting value from GUI to create graph
        name=View_creation.name_gui.get()
        time=View_creation.time_gui.get()
        name=name.upper()
        time=time.lower()
        sr_type=View_creation.sr_type_gui.get()
        sr_type=sr_type.lower()
        graph.title(name.upper())
        date=View_creation.date.get()
        y=sw.work.select_name(name,time,sr_type,date)
        #making graph window scrollable
        ver=Scrollbar(graph,orient='vertical')
        ver.pack(side = RIGHT, fill = Y)
        hori=Scrollbar(graph,orient='horizontal')
        hori.pack(side=BOTTOM,fill=X)
        #adding graph to GUI
        fig = Figure(figsize = (10, 5), 
				dpi = 150)
        plot1 = fig.add_subplot(111)
        #plotting the graph
        plot1.plot(y[0],y[1])
        plot1.plot(y[0],y[2])
        plot1.plot(y[0],y[3])
        canvas = FigureCanvasTkAgg(fig, 
							master = graph)
        canvas.get_tk_widget().pack()
        canvas.draw()
        #calling toolbar to edit graph accordingly
        toolbar = NavigationToolbar2Tk(canvas, 
								graph)
        toolbar.update()
        canvas.get_tk_widget().pack()
        #calling function that collects user data ,please let the user know that you are collecting
        #data for better understanding .
        pstprc.collection.insertion(name,time)
        #MAKES A NEW WINDOW WHEN EVER CALLED UPON IT HELPS TO COMPARE TWO COMPANIES TOGETHER
    def new_window():
        #SECONDARY WINDOW GENERATION
        new_file=Toplevel(root)
        #NAME OF THE NEW WINDOW
        new_file.title("My new Company Analysis")
        new_file.geometry("600x600")
        #TAKE INPUT FROM GUI SO CREATE LABELS AND ENTRY POINTS FOR USER INPUT
        name_label=tk.Label(new_file,text="Enter the Company name",font=('italic',10,'bold'))
        name_entry=tk.Entry(new_file,textvariable=View_creation.name_gui)
        time_label=tk.Label(new_file,text="Enter the time",font=('calibre',10,'bold'))
        time_entry=tk.Entry(new_file,textvariable=View_creation.time_gui)
        sr_type_label=tk.Label(new_file,text='Enter the the Type')
        sr_type_entry=tk.Entry(new_file,textvariable=View_creation.sr_type_gui)
        date_label=tk.Label(new_file,text="enter the date")
        date_entry=tk.Entry(new_file,textvariable=View_creation.date)
        #USE GRID TO PLACE THEM ON GUI
        name_label.grid(row=0,column=0)
        name_entry.grid(row=0,column=1)
        time_label.grid(row=1,column=0)        
        time_entry.grid(row=1,column=1)
        sr_type_label.grid(row=2,column=0)
        sr_type_entry.grid(row=2,column=1)
        date_label.grid(row=3,column=0)
        date_entry.grid(row=3,column=1)
        #A BUTTON TO CALL PERFORM TASK FUNCTION THAT WILL INITIATE THE GRAPH MAKING PROCESS
        btn=Button(new_file,text="Get Stocks Graph",command=View_creation.perform_task)
        btn1=Button(new_file,text="Close",command=new_file.destroy)
        btn2=Button(new_file,text="Get SMA",command=None)
        btn3=Button(new_file,text='Get WMA',command=None)
        btn4=Button(new_file,text='Get EMA',command=None)
        btn2.grid(row=5,column=0)
        btn3.grid(row=6,column=0)
        btn4.grid(row=7,column=0)
        btn1.grid(row=8,column=0)
        btn.grid(row=4,column=1)
#this is the root window or master window      
root.configure(background='red')        
button = Button(root,text="Click to make New Analysis",command=View_creation.new_window)
button1=Button(root,text="quit",command=root.destroy)
button.pack()
button1.pack()
root.mainloop()
