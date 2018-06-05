#/usr/bin/python3
#-*-coding:UTF-8-*-

test=open('D:/1.txt','w')
test.write('hello!'+'\n')
test.write('world!'+'\n')

test=open('D:/1.txt','r')
print(test.read())
