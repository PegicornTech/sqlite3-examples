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


#c.fetch

#c.fetchmany(3)

cdata = c.fetchall()

print(cdata)

#commit command
conn.commit()


#close connection
conn.close()
