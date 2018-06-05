#!/usr/bin/python3
#-*-coding:UTF-8-*-

import multiprocessing as mp

def job(a,d):

    print('this is Process a test!')




p1=mp.Process(target=job,args=(1,2))
p1.start()
p1.join()

job(1,2)
