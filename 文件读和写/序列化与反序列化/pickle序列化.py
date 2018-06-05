#!/usr/bin/python3
#-*-coding:UTF-8-*-

import pickle

d=dict(name='Zhangsan',num='1001')

print(pickle.dumps(d))



try:

    f_name=open('E:/dump.txt','wb')
    pickle.dump(d,f_name)

finally:

    f_name.close()
