#!/usr/bin/python3
#-*-coding:UTF-8-*-

n=int(input('请输入一个数字计算和:'))
sum=0
for i in range(n):
    sum+=i

    if sum>2000:
        print('2333')
        print('最后大于2000的和为:',sum)

        break

