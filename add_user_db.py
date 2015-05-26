#!/usr/bin/env python
import sqlite3,urllib2,datetime,time,sys
# -*- coding: utf-8 -*-

# user_id = "2714800"
user_id_arg = sys.argv[1]

con = sqlite3.connect('chase.db')
cur = con.cursor()

cur.execute('INSERT INTO vk_users (id, vk_id)VALUES(NULL, {vk_id})'.\
	format(vk_id=user_id_arg))

con.commit()

print cur.lastrowid	
cur.execute('SELECT * FROM vk_users')

for row in cur:
	print row[1]	
con.close()
