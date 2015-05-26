#!/usr/bin/env python
import sqlite3
# -*- coding: utf-8 -*-

con = sqlite3.connect('chase.db')
cur = con.cursor()
cur.execute('CREATE TABLE vk_chase (id INTEGER PRIMARY KEY, vk_id VARCHAR(100), online INTEGER(30), online_mobile INTEGER(30),add_time INTEGER(30))')
cur.execute('CREATE TABLE vk_users (id INTEGER PRIMARY KEY, vk_id VARCHAR(100))')

con.commit()
con.close()