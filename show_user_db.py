#!/usr/bin/env python
import sqlite3,urllib2,datetime,time,sys
# -*- coding: utf-8 -*-


con = sqlite3.connect('chase.db')
cur = con.cursor()


# cur.execute('DELETE FROM vk_users')
# con.commit()
cur.execute('SELECT * FROM vk_users')

for row in cur:
	print row[1]	
con.close()
