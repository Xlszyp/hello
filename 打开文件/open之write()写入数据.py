#/usr/bin/python3
#-*-coding:UTF-8-*-

test=open('D:/xls.txt','w')
print('write lenght:',test.write('Hello,world!'))

test=open('D:/xls.txt','r')
print('read result:',test.read())

test=open('D:/xls.txt','a')
print('add lenght:',test.write(' xls!'))

test=open('D:/xls.txt','r')
print('read result:',test.read())
