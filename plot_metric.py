#!/usr/bin/env python
import sqlite3, datetime
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
# -*- coding: utf-8 -*-


time=[]
activity=[]

con = sqlite3.connect('chase.db')
cur = con.cursor()
cur.execute('SELECT * FROM vk_chase')

for row in cur:
	# time.append(datetime.datetime.fromtimestamp(int(row[4]))).strftime('%H-%M')
	cur_time = int(row[4])
	data_temp = datetime.datetime.fromtimestamp(cur_time)
	time.append(data_temp)

	if(int(row[2])<1):
		activity.append(0)
	elif(int(row[3])==1):
		activity.append(2)
	else: 
		activity.append(1)

	print row[1],row[2],row[3],row[4]

color1 = '#212020'
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
############################################
ax1.spines['bottom'].set_linewidth(0.5)
ax1.spines['top'].set_linewidth(0.5)
ax1.spines['right'].set_linewidth(0.5)
ax1.spines['left'].set_linewidth(0.5)
############################################
ax1.tick_params(axis='y', colors=color3)
ax1.tick_params(axis='x', colors=color3)
ax1.xaxis.set_tick_params(width=1, colors=color2)
ax1.yaxis.set_tick_params(width=0)
############################################
plt.rcParams.update({'font.size': 10})
# plt.tick_params(axis='y', which='major', visible='false')
############################################
ax = plt.plot(time,activity, linewidth=1, color=color4)
######### GRAPH LIMITS ###################
datemin = datetime.datetime(2015, 5, 19, 0, 0, 0, 0)
datemax = datetime.datetime(2015, 5, 20, 0, 0, 0, 0)
ax1.set_xlim(datemin, datemax)
ax1.set_ylim(-1, 3)
##########################################
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
plt.show()