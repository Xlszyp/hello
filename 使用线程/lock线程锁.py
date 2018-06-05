#!/usr/bin/python3
#-*-coding:UTF-8-*-

import threading

#未加lock线程锁

def job1():

    global A

    for i in range(10):
        A+=1
        print('job1',A)


def job2():

    global A

    for i in range(10):
        A+=10
        print('job2',A)


A=0
t1=threading.Thread(target=job1)
t2=threading.Thread(target=job2)

t1.start()
t2.start()
    
t1.join()
t2.join()


#加lock线程锁

#B=0
def job3():

    global B,lock   #B,lock传入全局变量

    lock.acquire()  #程序开始之前将共享内存上锁,确保当前线程执行时内存不会被其它线程访问

    for i in range(10):
        B+=1
        print('job3:',B)

    lock.release()  #程序运行完毕后再将锁打开,确保其它线程可以使用该共享内存

def job4():

    global B,lock

    lock.acquire()

    for i in range(10):
        B+=10
        print('job4:',B)

    lock.release()

lock=threading.Lock()   #定义一个lock

B=0

t3=threading.Thread(target=job3)
t4=threading.Thread(target=job4)

t3.start()
t4.start()

t3.join()
t4.join()
