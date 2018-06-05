#/usr/bin/python3
#-*-coding:UTF-8-*-

class Myclass(object):      #定义类

    def __init__(self):     #定义init构造方法
        print('我是不带参数的__init__方法')

    def __init__(self,name,age):    #定义init构造方法
        print('我是带了两个参数的__init__方法：',name,age)  #输出定义的两个参数

Myclass('Zhangsan',22)      #类的实例化

print('类实例化结束')



#一个类中可以定义多个构造方法，但是实例化类时只实例化最后的构造方法，并且需要根据最后一个构造方法的形式进行实例化，也就是最后一个构造方法中定义了几个参数则实例化时对应输出几个值。
