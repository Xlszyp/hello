#!/usr/bin/python3
#-*-coding:UTF-8-*-

import threading
import time

from queue import Queue

def job(l,q):
    
    for i in range(len(l)):
        l[i]=l[i]**2
    q.put(l)

def multithreading():

    q=Queue()
    threads=[]
    data=[[1,2,3],[4,5,6],[7,8,9]]

    for i in range(3):

        t=threading.Thread(target=job,args=(data[i],q))
        t.start()
        threads.append(t)

    for thread in threads:
        thread.join()

    results=[]

    for _ in range(3):
        results.append(q.get())
    print(results)

multithreading()
