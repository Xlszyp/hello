#!/usr/bin/python3
#-*-coding:UTF-8-*-


#r权限不加也可以
f_name=open('E:/xls.txt','r')

for line in f_name:
    print(line)

f_name.close()
