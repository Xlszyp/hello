#!/usr/bin/python3
#-*-coding:UTF-8-*-

f_name=open('E:/test.txt','r')

while True:
    c_str=f_name.readline(1)

    if not c_str:
        break

    print(c_str)

f_name.close()
