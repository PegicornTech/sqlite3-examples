#!/usr/bin/python
import os
import sqlite3
cwd=os.getcwd()
db=cwd+'/customer.db'


#connect to database
conn = sqlite3.connect(db)

#create a cursor
c = conn.cursor()

#query the database
c.execute("SELECT * FROM customers")


#c.fetchone()

cdata = c.fetchmany(3)

#c.fetchall()

print(cdata)

#commit command
conn.commit()


#close connection
conn.close()
