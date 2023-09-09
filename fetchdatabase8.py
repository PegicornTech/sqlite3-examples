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
c.execute("""UPDATE customers SET first_name = 'Dakota'
	WHERE last_name = 'South'
""")


c.execute("SELECT rowid, * FROM customers")


items = c.fetchall()

for item in items:
    print(item)
    

#commit command
conn.commit()


#close connection
conn.close()
