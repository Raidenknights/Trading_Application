# -*- coding: utf-8 -*-
"""
Created on Thu Nov  5 14:39:27 2020

@author: manas
"""
import mysql.connector
class credentials:
    def getuser():
        user="root"
        return user
    def getpassword():
        password="54321@#"
        return password
    def gethostname():
        hostname="localhost"
        return hostname
    def gethost():
        host='127.0.0.1'
        return str(host)
    def get_database():
        db='mydb'
        return db
    def connect():
        mydb=mysql.connector.connect(
            user="root",
            password="54321@#",
            host="127.0.0.1",
            database="mydb");
        return mydb