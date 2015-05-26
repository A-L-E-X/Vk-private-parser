#!/usr/bin/env python
import sqlite3,urllib2,json,time,sys
from datetime import datetime
# -*- coding: utf-8 -*-


user_id_arg = sys.argv[1]
date_arg = sys.argv[2]


date_max = str(int(date_arg[:2])+1)+date_arg[2:] # current day + 1 
date_pointer = datetime.strptime(date_arg, '%d%m%Y') # parse data
date_max_pointer = datetime.strptime(date_max, '%d%m%Y') # parse data
ts_date_pointer = time.mktime(date_pointer.timetuple()) # timestamp format
ts_date_max_pointer = time.mktime(date_max_pointer.timetuple()) # timestamp format

### debug ###

user_id = user_id_arg
# user_id = "2714800"

#############

con = sqlite3.connect(sys.path[0]+'/chase.db')
cur = con.cursor()

cur.execute('SELECT * FROM vk_chase WHERE vk_id={vk_id} AND add_time>{date_pointer} AND add_time<{date_max_pointer}'.\
	format(vk_id=user_id, date_pointer=ts_date_pointer, date_max_pointer=ts_date_max_pointer))

for row in cur:
	print row[1],row[2],row[3],row[4]
con.close()
	