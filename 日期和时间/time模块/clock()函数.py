#/usr/bin/python3
#-*-coding:UTF-8-*-

import time

def procedure():

    time.sleep(2)

#measure process time测量过程时间

t1=time.clock()

procedure()

print('seconds process time:',time.clock()-t1)


#measure wall time

t2=time.time()

procedure()
print('seconds wall time:',time.time()-t2)

#第一次调用时，返回该程序运行的实际时间
#第二次调用时，返回自第一次调用后到这次调用的时间间隔
