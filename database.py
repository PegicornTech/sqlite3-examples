#!/usr/bin/python
import os
import sqlite3
cwd=os.getcwd()
db=cwd+'/customer.db'


#query database and return all records
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
    
def add_one(first, last, email):

    #connect to database
    conn = sqlite3.connect(db)
    
    #create a cursor
    c = conn.cursor()
    
    c.execute("INSERT INTO Customers VALUES (?,?,?)",(first, last, email))
    
    #commit command
    conn.commit()
    
    #close connection
    conn.close()
    
def add_many(List):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.executemany("INSERT INTO Customers VALUES (?,?,?)", List)
    conn.commit()
    conn.close()
    
    
def delete_one(id):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("DELETE FROM customers WHERE rowid = (?)", id)
    #commit command    #close connection
    conn.commit()
    conn.close()

def email_lookup(email):
    conn = sqlite3.connect('customer.db')
    c = conn.cursor()
    c.execute("SELECT rowid, * FROM customers WHERE email = (?)", (email,))
    items = c.fetchall()
    for item in items:
        print(item)
    conn.close()
    
    
    
    
    
