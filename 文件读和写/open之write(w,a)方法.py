#/usr/bin/python3
#-*-coding:UTF-8-*-

file=open('E:/test.txt','w')
file.write('Hello,World!\nWelcome!\n')

file=open('E:/test.txt','a')
file.write('Python is so good!')


file=open('E:/test.txt','r')

print(file.read())
