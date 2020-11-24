# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 15:48:33 2020

@author: manas
"""
#import libraries
from alpha_vantage.timeseries import TimeSeries 
from alpha_vantage.techindicators import TechIndicators 
#this class is the main unit here API is verified and upon verification data is send to other modules
class Company:
    #this is company dictionary only company names specified here can be called by the user 
    #this list will be extented once developement is over
     comp={'APPLE':'AAPL','Microsoft Corp':'MSFT','TESLA':'TSLA'}
     # get data to Start_work class
     def get_intraday(name,duration):
        ts = TimeSeries(key='YOUR_OWN_API', output_format='pandas')
        data, metadata= ts.get_intraday(symbol=Company.comp[name],interval=duration,outputsize='full')
        return data;
    #get SMA using API
     def get_SMA(name,duration,sr_type):
        ti=TechIndicators(key='YOUR_OWN_API',output_format='pandas')
        data_sma,meta_data_sma=ti.get_sma(symbol=Company.comp[name],interval=duration,time_period='60',series_type=sr_type)
        return data_sma
    #get WMA data using API
     def get_WMA(name,duration,sr_type):
        ti=TechIndicators(key='YOUR_OWN_API',output_format='pandas')
        data_wma,meta_data_wma=ti.get_wma(symbol=Company.comp[name],interval=duration,time_period='60',series_type=sr_type)
        return data_wma        
     def get_EMA(name,duration,sr_type):
        ti=TechIndicators(key='YOUR_OWN_API',output_format='pandas')
        data_wma,meta_data_wma=ti.get_wma(symbol=Company.comp[name],interval=duration,time_period='60',series_type=sr_type)
        
        
    
    
    
  
    
