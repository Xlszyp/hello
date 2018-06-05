#!/usr/bin/python3
#-*-coding:UTF-8-*-

import json

#写入JSON数据
data=dict(name='xls',num=666)

with open('E:/dump1.txt','w') as f:
    json.dump(data,f)


#读取JSON数据
with open('E:/dump1.txt','r') as i:
    file=json.load(i)

    print('file is:',file)
