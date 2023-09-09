#!/usr/bin/python
import os
import sqlite3
cwd=os.getcwd()
db=cwd+'/customer.db'

conn = sqlite3.connect(db)

conn.close()
