# -*- coding: utf-8 -*-
"""
Created on Tue Oct 27 01:38:34 2020

@author: manas
"""
#this is a testing program various conditions are tested here not used in the main code 
from alpha_vantage.timeseries import TimeSeries
from alpha_vantage.techindicators import TechIndicators 
import start_work as sw
import pandas as pd
import select_company as sc
ts = TimeSeries(key='A4GJGEAIETZ3UBQZ', output_format='pandas')
ti=TechIndicators(key='A4GJGEAIETZ3UBQZ',output_format='pandas')
name='APPLE'
duration='60min'
str1='2020-10-22'
#sr_type=input("enter")
#data_sma,meta_data_sma=ti.get_sma(symbol=name,interval=duration,time_period='60',series_type=sr_type)
#data, metadata= ts.get_intraday(symbol=name,interval=duration,outputsize='full')
#ata=data['2. high'].loc[str1]
#print(data_sma)
raw_data=sc.Company.get_intraday(name,duration)
data=raw_data['2. high'].loc[str1]
print(data)
'''def check(one,two,three):
    return one,two,three;
one=input("enter the data")
two=input("enter the data") 
three=input("enter the data") 
x=check(one,two,three)    
print(x[0])'''

str1='2020-10-31'

'''predict=pd.DataFrame(index=range(0,24),columns=['Date','Close'])
print(str1)
for i in range(0,24,1):
    predict['Date'][i]=str1+' '+str(i)+':00:00'
print(predict)  '''