#!/usr/bin/python3
#-*-coding:UTF-8-*-

import pickle

try:

    f_name=open('E:/dump.txt','rb')
    print('load result:',pickle.load(f_name))

finally:
    f_name.close()
