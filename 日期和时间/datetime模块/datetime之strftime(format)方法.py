#/usr/bin/python3
#-*-coding:UTF-8-*-

import datetime

dt=datetime.datetime.now()
print('当前时间：')
print(dt)
print('格式化后的时间：')
print(dt.strftime('%Y-%m-%d %H:%M:%S %f'))
print('格式化后的PM时间：')
print(dt.strftime('%y-%m-%d %I:%M:%S %p'))
print('星期%s'%dt.strftime('%a'))
print('星期%s'%dt.strftime('%A'))
print('{}月份'.format(dt.strftime('%b')))
print('{}月份'.format(dt.strftime('%B')))
print('本地对应的日期时间:%s'%dt.strftime('%c'))
print('日期:%s'%dt.strftime('%x'))
print('时间:{}'.format(dt.strftime('%X')))
print('今天是这周的第%s天'%dt.strftime('%w'))
print('今天是这年的第%s天'%dt.strftime('%j'))
print('这周是今年的第{}周'.format(dt.strftime('%U')))