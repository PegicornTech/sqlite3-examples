#!/usr/bin/python
import os
import sqlite3
cwd=os.getcwd()
db=cwd+'/customer.db'


#connect to database
conn = sqlite3.connect(db)

#create a cursor
c = conn.cursor()

#create a table
c.execute("INSERT INTO customers VALUES ('Dakota', 'North', 'dakota.north@example.com')")


#datatypes are null, integer, real, text, and blob

#commit command
conn.commit()


#close connection
conn.close()
