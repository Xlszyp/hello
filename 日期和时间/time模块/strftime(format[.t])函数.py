#/usr/bin/python3
#-*-coding:UTF-8-*-

import time

t=time.localtime()

print(time.strftime('%b %d %Y %H:%M:%S',t))