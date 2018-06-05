#/usr/bin/python3
#-*-coding:UTF-8-*-

import time

print('time.gmtime():',time.gmtime())

#用于将一个时间戳转换为UTC时区的struct_time，gmtime()函数的默认值为time.time()
#返回的时间等于本地时间：time.localtime()
