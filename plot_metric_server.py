#!/usr/bin/env python
import sqlite3,sys,time
from datetime import datetime
from datetime import timedelta
import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# -*- coding: utf-8 -*-


##############
user_id = sys.argv[1]
date_arg = sys.argv[2]


date_max = str(int(date_arg[:2])+1)+date_arg[2:] # current day + 1 
date_pointer = datetime.strptime(date_arg, '%d%m%Y') # parse data
date_max_pointer = datetime.strptime(date_max, '%d%m%Y') # parse data
ts_date_pointer = time.mktime(date_pointer.timetuple()) # timestamp format
ts_date_max_pointer = time.mktime(date_max_pointer.timetuple()) # timestamp format
#############


time=[]
activity=[]


con = sqlite3.connect(sys.path[0]+'/chase.db')
cur = con.cursor()


# cur.execute('SELECT * FROM vk_chase')

cur.execute('SELECT * FROM vk_chase WHERE vk_id={vk_id} AND add_time>{date_pointer} AND add_time<{date_max_pointer}'.\
	format(vk_id=user_id, date_pointer=ts_date_pointer, date_max_pointer=ts_date_max_pointer))



for row in cur:
	# time.append(datetime.datetime.fromtimestamp(int(row[4]))).strftime('%H-%M')
	cur_time = int(row[4])
	data_temp = datetime.fromtimestamp(cur_time)
	time.append(data_temp)

	if(int(row[2])<1):
		activity.append(0)
	elif(int(row[3])==1):
		activity.append(2)
	else: 
		activity.append(1)

	print row[1],row[2],row[3],row[4]

color1 = '#ffffff'
color2 = '#bf7c82'
color3 = '#bf7c82'
color4 = '#a0a9d9'
color5 = '#423f3f'

fig = plt.figure()
fig.patch.set_facecolor(color1)
ax1 = plt.subplot(111, axisbg=color1)

############axies color######################
ax1.spines['bottom'].set_color(color2)
ax1.spines['top'].set_color(color2) 
ax1.spines['right'].set_color(color2)
ax1.spines['left'].set_color(color2)
#############axies linewidth#################
ax1.spines['bottom'].set_linewidth(0.5)
ax1.spines['top'].set_linewidth(0.5)
ax1.spines['right'].set_linewidth(0.5)
ax1.spines['left'].set_linewidth(0.5)
############dont work on server##############
#ax1.tick_params(axis='y', colors=color3)
#ax1.tick_params(axis='x', colors=color3)
#ax1.xaxis.set_tick_params(width=1, colors=color2)
#ax1.yaxis.set_tick_params(width=0)
############################################
plt.rcParams.update({'font.size': 10})
# plt.tick_params(axis='y', which='major', visible='false')
############################################
ax = plt.plot(time,activity, linewidth=1, color=color4)
######### GRAPH LIMITS ###################
# datemin = datetime.datetime(2015, 5, 20, 0, 0, 0, 0)
# datemax = datetime.datetime(2015, 5, 21, 0, 0, 0, 0)

datemin = datetime(time[0].year, time[0].month, time[0].day, 0, 0, 0, 0)
datemax = datemin + timedelta(days=1)

print 'datemin=',datemin
print 'datemax=',datemax

ax1.set_xlim(datemin, datemax)
##########################################
title_string = str(datemin)+' User id: '+str(user_id) 
plt.title(title_string)
# plt.xlabel('TIME')
# plt.ylabel('ACTIVITY')
plt.yticks([-1, 0, 1, 2, 3])
# plt.gca().axes.get_yaxis().set_visible(False)
plt.gca().axes.yaxis.grid(True, color='r')
# plt.gca().axes.set_axis_bgcolor((1, 155, 0))
# tick.label.set_fontsize(14) 
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M'))
plt.gca().xaxis.set_major_locator(mdates.HourLocator(byhour=[0,4,8,12,16,20,0], interval=2))
plt.gcf().autofmt_xdate()
plt.savefig('plot1.png', facecolor=color1, edgecolor='none')
# plt.show()