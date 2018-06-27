#!/usr/bin/python3
#-*-coding:UTF-8-*-

import sqlite3

conn=sqlite3.connect('somedatabase.db')

#从连接获得游标
curs=conn.cursor()

#提交所做的修改
conn.commit()

conn.close()
