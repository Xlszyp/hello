#!/usr/bin/python3
#-*-coding:UTF-8-*-

import multiprocessing as mp

def job(x):

    return x*x

def multicore():

    pool=mp.Pool(processes=2)   #自定义CPU核数量为2

    res=pool.map(job,range(10)) #将job放进pool进程池,pool.map()
    print(res)

    res=pool.apply_async(job,(2,))  #apply_async()只能传一个值并且只会放入一个核运算
    print(res.get())    #用get获得结果
    
    #迭代器,i=0时apply一次,i=1时apply一次等等
    multi_res=[pool.apply_async(job,(i,)) for i in range(10)]
    #从迭代器中取出
    print([res.get() for res in multi_res])


if __name__=='__main__':
    multicore()
