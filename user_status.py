#!/usr/bin/env python
import sqlite3,urllib2,json,time,sys
from datetime import datetime
# -*- coding: utf-8 -*-


# user_id_arg = sys.argv[1]
# date_arg = sys.argv[2]

# print '------'
# print user_id_arg
# print date_arg

# date_max = str(int(date_arg[:2])+1)+date_arg[2:] # current day + 1 
# date_pointer = datetime.strptime(date_arg, '%d%m%Y') # parse data
# date_max_pointer = datetime.strptime(date_max, '%d%m%Y') # parse data
# ts_date_pointer = time.mktime(date_pointer.timetuple()) # timestamp format
# ts_date_max_pointer = time.mktime(date_max_pointer.timetuple()) # timestamp format

### debug ###

# user_id = user_id_arg

users_id = []

con = sqlite3.connect(sys.path[0]+'/chase.db')
cur = con.cursor()
cur.execute('SELECT * FROM vk_users')

for user in cur: 
	users_id.append(user[1])

print users_id

for user in users_id:
	# user_id = "2714800"
	#############
	url = "https://api.vk.com/method/users.get?user_id="+user+"&fields=online,online_mobile&v=5.32"
	page = urllib2.urlopen(url).read()
	# print page
	print "------------"
	j = json.loads(page)
	online = j['response'][0]['online']
	try:
		online_mobile = j['response'][0]['online_mobile']
	except:
		online_mobile = 0
	cur.execute('INSERT INTO vk_chase (id, vk_id, online, online_mobile, add_time)VALUES(NULL, {vk_id}, {online}, {online_mob}, {time_add})'.\
		format(vk_id=user,online=online,online_mob=online_mobile,time_add=time.time()))
	con.commit()	
print cur.lastrowid	
# cur.execute('SELECT * FROM vk_chase')
con.close()
	