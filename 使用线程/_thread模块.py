#!/usr/bin/python3
#-*-coding:UTF-8-*-

import _thread
from time import sleep
from datetime import datetime

date_time_format='%y-%M-%d %H:%M:%S'


def date_time_str(date_time):
    return datetime.strftime(date_time,date_time_format)


def loop_one():
    print('+++线程一开始于:',date_time_str(datetime.now()))
    print('\n')
    print('+++线程一休眠4秒')
    print('\n')
    sleep(4)
    print('+++线程一休眠结束,结束于:',date_time_str(datetime.now()))
#loop_one()


def loop_two():
    print('***线程二开始时间:',date_time_str(datetime.now()))
    print('***线程二休眠2秒')
    sleep(2)
    print('***线程二休眠结束,结束时间:',date_time_str(datetime.now()))
#loop_two()

def main():
    print('------所有线程开始时间:',date_time_str(datetime.now()))
    _thread.start_new_thread(loop_one,())
    _thread.start_new_thread(loop_two,())
    sleep(6)
    print('------所有线程结束时间:',date_time_str(datetime.now()))

if __name__=='__main__':
    main()
