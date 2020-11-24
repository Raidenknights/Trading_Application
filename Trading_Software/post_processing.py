# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 14:17:19 2020

@author: manas
"""
import credentials as crd
# here this class will write the data into the database that was fetched from the user with
# permission
class collection:
    #function to insert data into database
    def insertion(name,duration):
        #database credentials are entered and we connect to database 
        mydb=crd.credentials.connect()
        comp_name=name
        duration_used=duration
        add_data=("Insert into user_data" "(Company_name,duration)" "values(%s,%s)")
        values=(comp_name,duration_used)
        cursor=mydb.cursor()
        cursor.executemany(add_data,(values,))
        mydb.commit()
        return

        
