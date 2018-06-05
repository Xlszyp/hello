#!/usr/bin/python3
#-*-coding:UTF-8-*-

class MemberCounter(object):

    members=0

    def init(self):
        MemberCounter.members+=1

m1=MemberCounter()
m1.init()
print('当前类实例化的数量：',MemberCounter.members)


m2=MemberCounter()
m2.init()
print('当前类实例化的数量：',MemberCounter.members)

#每个实例都可以访问这个类作用域内的变量
print(m1.members)
print(m2.members)

#在一个实例中给属性members赋值

m1.members='xls'
print('重新赋值后的结果为:',m1.members)

#将一个实例的属性改变,另一个实例属性不会发生变化
print('m1被赋值后,m2的值为:',m2.members)
