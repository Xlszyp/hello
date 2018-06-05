#!/usr/bin/python3
#-*-coding:UTF-8-*-

f_name=open('D:/xls.txt','r')

while True:

    c_str=f_name.read(1)

    if not c_str:
        break

    print('read str is:',c_str)

f_name.close()
