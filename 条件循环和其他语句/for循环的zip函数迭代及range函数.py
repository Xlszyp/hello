#! /usr/bin/python3
#-*- coding:UTF-8-*-
student=['Zhangsan','Lisi','Zhaowu']
number=[1001,1002,1003]
for name,num in zip(student,number):
    print(name,'的学号是：',num)#zip函数的for循环迭代


for num1,num2 in zip(range(3),range(3)):
    print(num1,num2)

for i in range(3,10):
    print(i)#range函数的使用

a=range(0,6)
for n in a:
    print(n)#range函数的使用


a=['a','b']
b=[1,2]
c=['p','y']
for x,y,z in zip(a,b,c):
    print(x,y,z)
