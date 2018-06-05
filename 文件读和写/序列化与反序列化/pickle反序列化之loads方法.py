#!/usr/bin/python3
#-*-coding:UTF-8-*-

import pickle

try:
    f_name=open('E:/dump.txt','rb')

    f=pickle.loads(f_name.read())

    print('loads result:',f)

finally:

    f_name.close()
