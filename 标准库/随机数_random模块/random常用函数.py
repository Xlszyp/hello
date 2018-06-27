#!/usr/bin/python3
#-*-coding:UTF-8-*-

import random

#1.random返回一个0~1的随机实数
print('0~1随机实数:',random.random())

#2.getrandbits以长整数方式返回n个随机的二进制位
print(random.getrandbits(3))

#3.uniform返回一个a~b的随机实数
print('1~10中随机实数:',random.uniform(1,10))

#4.randrange从range(start,stop,step)中随机选择一个数
print('1~10的随机数:',random.randrange(1,11))
print('1~10的随机数:',random.randrange(10)+1)
print('生成一个小于20的随机正奇数:',random.randrange(1,20,2))

#5.choice从序列中随机选择一个元素
name=['zhangsan','lisi','zhaowu','xiaoliu']
print('序列随机选择元素:',random.choice(name))

#6.shuffle打乱序列
random.shuffle(name)
print('打乱序列:',name)

#7.sample从序列中选择n个值不同的元素
print('随机从序列选择2个元素:',random.sample(name,2))
