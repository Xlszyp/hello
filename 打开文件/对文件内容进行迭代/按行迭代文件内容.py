#!/usr/bin/python3
#-*-coding:UTF-8-*-

f=open('D:/1.txt','r')

while True:

    line=f.readline(1)

    if not line:
        break

    print(line)

f.close()
