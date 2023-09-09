#!/usr/bin/python
import os
import sqlite3
cwd=os.getcwd()
db=cwd+'/customer.db'

#connect to database
conn = sqlite3.connect(db)

#create a cursor
c = conn.cursor()

many_customers = [
('Dakota', 'South', 'dakota.south@emample.com'),
('Oscar', 'Pike', 'oscar.pike@example.com'),
('Greenbriar', 'John', 'john.greenbriar@example.com'),
]

#create a table
c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

#datatypes are null, integer, real, text, and blob

#commit command
conn.commit()

#close connection
conn.close()
