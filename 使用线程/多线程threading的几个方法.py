#!/usr/bin/python3
#-*-coding:UTF-8-*-

import threading

def main():

    print('获取已激活的线程数：',threading.active_count())
    print('查看所有线程信息：',threading.enumerate())
    print('查看现在正在运行的线程：',threading.current_thread())


if __name__=='__main__':
    main()
