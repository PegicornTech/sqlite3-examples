#!/usr/bin/python
import database


#drop a record from the database
#database.delete_one('5')

#add a record
#database.add_one("dick","shuven","dick.shuven@example.com")


stuff = [
	('don', 'punch', 'steamdonkey@example.com'),
	('tiffany', 'fisterson', 'tiffany.fisterson@example.com')
	]

#database.add_many(stuff)

database.email_lookup('dakota.north@example.com')

#show the database
#database.show_all()




