#/usr/bin/python3
#-*-coding:UTF-8-*-

import time

t=time.localtime()

print('asctime()返回可读形式时间：',time.asctime(t))

#asctime()函数用于接收时间元组并返回一个可读形式的24个字符的字符串，时间


#或

import time

t=(2018, 1, 28, 15, 17, 11, 6, 28, 0)

print('asctime():',time.asctime(t))
