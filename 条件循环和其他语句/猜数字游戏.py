#!/usr/bin/python3
#-*-coding:UTF-8-*-

import random   #导入随机模块

number=random.randint(1,100)    #定义随机数字范围

guess=0     #计算猜的次数

while True:
    num_input=input('输入一个1到100之间的数字:')  #输入数字
    guess+=1    #循环，统计猜的次数
    if not num_input.isdigit():     #假如输入的不是数字则输出
        print('请输入数字')
    elif int(num_input)<0 or int(num_input)>=100:   #假如输入的数字不在1至100范围
            print('请输入一个1到100之间的数字')
    else:
            if number==int(num_input):  #假如输入的数字等于随机的数字
                print('恭喜，猜对了，共猜了：%d次'%guess)
                break #退出
            elif number<int(num_input): #假如输入的数字大于随机要猜的数字
                print('输入的数字大了')
            elif number>int(num_input):
                    print('输入的数字小了')    #假如输入的数字小于要猜的数字
            else:
                        print('Erro')
