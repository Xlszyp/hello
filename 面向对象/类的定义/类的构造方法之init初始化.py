#/usr/bin/python3
#-*-coding:UTF-8-*-

class Myclass(object):  #定义类
    
    i=666
    
    def __init__(self,name):    #定义初始化构造方法
        self.name=name

    def f(self):    #定义方法
        return 'Hello,'+self.name


me=Myclass('Zhangsan')  #定义实例

print('调用类的属性：',me.i)
print('调用类的方法：',me.f())
