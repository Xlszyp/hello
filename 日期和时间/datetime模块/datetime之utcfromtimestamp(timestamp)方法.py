#/usr/bin/python3
#-*-coding:UTF-8-*-

import datetime
import time

print('utcfromtimestamp is :',datetime.datetime.utcfromtimestamp(time.time()))


#utcfromtimestamp()方法根据时间戳创建一个datetime对象，返回一个为UTC时区的时间
