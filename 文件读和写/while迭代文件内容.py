#!/usr/bin/python3
#-*-coding:UTF-8-*-

f_name=open('E:/test.txt','r')

while True:

    f=f_name.read(1)

    if not f:

        break

    print('迭代文件内容:',f)

f_name.close()
