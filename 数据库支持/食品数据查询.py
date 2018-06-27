#!/usr/bin/python3
#-*-coding:UTF-8-*-


import sqlite3, sys

conn = sqlite3.connect('food.db')
curs = conn.cursor()
'''    
query = 'SELECT * FROM food WHERE'+ sys.argv[1]
print(query)

curs.execute(query)
names = [f[0] for f in curs.description]
for row in curs.fetchall():
    for pair in zip(names, row):
        print('{}:{}'.format(*pair))
    print()







'''
for i in range(5):
    curs.execute('SELECT * FROM food WHERE id=?',(i,))
    result=curs.fetchall()
    print(result)
conn.commit()
curs.close()
conn.close()
