#!/usr/bin/python3
#-*-coding:UTF-8-*-

d={1:{'name':'xls'},2:{'name':'zyp'}}

print('1号人员:',d[1]['name'])
print('2号人员:',d[2]['name'])


def db_test(db):
    print(db)

db_test('testing...')
