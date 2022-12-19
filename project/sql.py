import pyodbc

import pandas as pd

import numpy as np
# Some other example server values are
# server = 'localhost\sqlexpress' # for a named instance
# server = 'myserver,port' # to specify an alternate port
server = '.'
database = 'BookDB122'
username = 'sa'
password = '223366'
conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()

cursor.execute('select * from 读者信息')
for index in cursor.fetchall():
    print(index)

