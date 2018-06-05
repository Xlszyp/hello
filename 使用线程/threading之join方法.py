#!/usr/bin/python3
#-*-coding:UTF-8-*-

import threading
import time
import datetime

today=datetime.datetime.today()
print('开始的时间:',today)
def T1_job():
    print('T1 start\n')
    for i in range(10):
        time.sleep(0.5) #任务间隔时间0.5s
    print('T1 finish\n')

def T2_job():
    print('T2 start\n')
    print('T2 finish\n')

def main():
    thread_1=threading.Thread(target=T1_job,name='T1')
    thread_2=threading.Thread(target=T2_job,name='T2')
    thread_1.start()    #开启T1
    thread_2.start()    #开启T2
    thread_1.join()
    thread_2.join()
    print('all done\n')

    print('现在一共有{}个线程正在工作'.format(threading.active_count()))

if __name__=='__main__':
    main()

today1=datetime.datetime.today()
print('结束时间:',today1)

t=today1-today
print('花了%s秒'%t)
#join控制着线程的工作顺序,否则会导致输出顺序杂乱无章
