#/usr/bin/python3
#-*-coding:UTF-8-*-

import time

t=(1970,1,1,8,1,0,0,0,0)

print('time.mktime():',time.mktime(t))

#mktime()函数用于执行与gmtime()、localtime()相反的操作
#接受struct_time对象作为参数，返回秒数表示时间的浮点数.
#返回的是从时间戳起始点的时间到t时间的秒数
