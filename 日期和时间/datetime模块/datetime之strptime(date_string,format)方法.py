#/usr/bin/python3
#-*-coding:UTF-8-*-

import datetime

dt=datetime.datetime.now()

print('striptime is :',dt.strptime(str(dt),'%Y-%m-%d %H:%M:%S.%f'))
#strptime()方法为将格式化字符串转化为datetime对象，返回定义固定格式化后的时间格式
#%f为微秒
