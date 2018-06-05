#/usr/bin/python3
#-*-coding:UTF-8-*-

class Myclass(object):
    i=666
    def test(self,name):
        print('Hello,',name)
me=Myclass()    #实例，类的实例化
print('调用类的属性：',me.i)
me.test('xulesong') #self不用传递，除外的参数正常传入，xulesong对应test(name)


#类里面用def定义方法，它不叫函数，每一个方法的第一个参数都是self，在调用时不必提供，程序会自动将第一个参数绑定到所属的实例上


class MyClass(object):
    i=777

    def f(self):
        return 'Hello,world'

use_MyClass=MyClass()   #类的实例化，实例名=定义的类名

print('调用类的属性：',use_MyClass.i)  #类定义后直接调用到i值
print('调用类的方法：',use_MyClass.f())    #调用方法中f(self)的输出值，因为self已经被绑定到use_MyClass实例上了






class Myclassd(object):     #定义类
    def f(self,name,age):   #定义方法
        print('hello,',name)    #除self外不用定义输出
        print(age)
me=Myclassd()   #定义实例
me.f('Xulesong',22) #调用方法输出
