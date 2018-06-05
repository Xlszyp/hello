#!/usr/bin/python3
#-*-coding:UTF-8-*-

import multiprocessing as mp
import time

def job(v,num,l):
    l.acquire() #锁住
    for _ in range(10):
        time.sleep(0.5) #暂停0.5秒
        v.value+=num    #v.value获取共享变量值
        print(v.value)

    l.release() #释放


def multicore():
    l=mp.Lock()
    v=mp.Value('i',0)   #定义共享变量
    p1=mp.Process(target=job,args=(v,1,l))  #args中为job()中的参数
    p2=mp.Process(target=job,args=(v,3,l))

    p1.start()
    p2.start()
    p1.join()
    p2.join()

if __name__=='__main__':
    multicore()