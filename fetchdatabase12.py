#!/usr/bin/python
import os
import sqlite3
cwd=os.getcwd()
db=cwd+'/customer.db'







def show_all():
    #connect to database
    conn = sqlite3.connect(db)
    
    #create a cursor
    c = conn.cursor()
    
    c.execute("SELECT rowid, * FROM customers")
    items = c.fetchall()
    for item in items:
    print(item)
    
    #commit command
    conn.commit()
    
    #close connection
    conn.close()
    
    







    







