#!/usr/bin/env python
import sqlite3,urllib2,datetime,time
# -*- coding: utf-8 -*-

user_id = "2714800"
url = "https://api.vk.com/method/users.get?user_id="+user_id+"&fields=online,online_mobile&v=5.32"

con = sqlite3.connect('chase.db')
cur = con.cursor()

cur.execute('INSERT INTO vk_chase (id, firstName, last_name, online, online_mobile, add_time)VALUES(NULL, "Ivan", "Void", 1, 1, {time_add})'.\
	format(time_add=time.time()))

con.commit()
print cur.lastrowid	
cur.execute('SELECT * FROM vk_chase')
for row in cur:
	print row[1],row[2],row[3],row[4],row[5]
# print cur.fetchall()
con.close()