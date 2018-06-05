#!/usr/bin/python3
#-*-coding:UTF-8-*-

import threading
import datetime
import time

today=datetime.datetime.today()
print('开始时间:',today)

def test1():
    print('test1 start\n')
    for i in range(10):
        time.sleep(0.5)
    print('test1 finish\n')

def test2():
    print('test2 start\n')
    print('test2 finish\n')

test1()
test2()

print('all done\n')
print('现在一共有{}线程正在工作'.format(threading.active_count()))

'''def main():
    test_1=test1
    test_2=test2
    print('all done\n')

if __name__='__main__':
    main()
'''
today1=datetime.datetime.today()
print('结束时间:',today1)

t=today1-today
print('花了%s秒'%t)
