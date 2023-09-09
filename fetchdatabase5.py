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


#c.fetchone(()[0])

#c.fetchmany(3)

items = c.fetchall()

print("NAME " + "\t\tEMAIL")
print("----" + "\t\t-----")
for item in items:
    print(item[0] + " " + item[1] + "\t" + item[2])
    

#commit command
conn.commit()


#close connection
conn.close()
