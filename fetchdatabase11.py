#!/usr/bin/python
import os
import sqlite3
cwd=os.getcwd()
db=cwd+'/customer.db'


#connect to database
conn = sqlite3.connect(db)

#create a cursor
c = conn.cursor()

#query the database -ORDER BY
c.execute("SELECT rowid, * FROM customers ORDER BY last_name")


items = c.fetchall()

for item in items:
    print(item)
    

#commit command
conn.commit()


#close connection
conn.close()
