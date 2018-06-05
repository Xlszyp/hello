#!/usr/bin/python3
#-*-coding:UTF-8-*-

import json


#进行序列化，数据进行编码
data={'num':1000,'name':'Lisi'}
json_str=json.dumps(data)

print('python原始数据:',data)
print('JSON对象:',json_str)


#反序列化,数据进行解码

data1=json.loads(json_str)
print('data1 name:',data1['name'])
print('data1 num:',data1['num'])
