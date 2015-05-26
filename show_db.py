#!/usr/bin/env python
import sqlite3, datetime, sys
# -*- coding: utf-8 -*-

con = sqlite3.connect(sys.path[0]+'/chase.db')
cur = con.cursor()


cur.execute('SELECT * FROM vk_chase')
for row in cur:
	print row[1],row[2],row[3],row[4]
con.close()
	

