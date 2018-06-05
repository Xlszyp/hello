#!/usr/bin/python3
#-*-coding:UTF-8-*-

import threading

def thread_job():
    print('This is a thread of %s'%(threading.current_thread()))
    #print('count thread:',threading.active_count())

def main():

    thread=threading.Thread(target=thread_job)  #定义/添加线程
    thread.start()  #让线程开始工作

if __name__=='__main__':
    main()
