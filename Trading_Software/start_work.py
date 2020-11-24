# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 16:00:13 2020

@author: manas
"""
#import important libraries and modules from the working folder
import datetime as dt
import pandas as pd
from matplotlib import style
import matplotlib.pyplot as plt
import select_company as sc
from bokeh.plotting import figure, output_file, show
from matplotlib.pyplot import figure as fg
fg(num=None, figsize=(8,8), dpi=100, facecolor='w', edgecolor='k')
#this class works mainly in getting the values for plotting the graph this class
#will called by gui to execute query
class work:
    #gets all the data and send it to prototype.py
    def select_name(name,duration,sr_type,date):
        #this gives unfiltered data of 13 days so we have to filter it using date
        raw_data=sc.Company.get_intraday(name,duration)
        #here Y3 is calling another function that will filter SMA data
        y3=work.get_sma_graph(name,duration,sr_type,date)
        x=raw_data.loc[date].index
        y1=raw_data['2. high'].loc[date]
        y2=raw_data['3. low'].loc[date]
        #return values required for plotting of graph
        return x,y1,y2,y3
    #gets filtered SMA data
    def get_sma_graph(name,duration,sr_type,date):
        sma_data=sc.Company.get_SMA(name,duration,sr_type)
        return sma_data.loc[date]
       

        