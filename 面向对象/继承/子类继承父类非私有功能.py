#/usr/bin/python3
#-*-coding:UTF-8-*-

class Animal(object):   #定义类，属于父类
    def run(self):      #定义方法
        print('Animal is runing')

class Dog(Animal):      #定义类，属于子类，括号中为父类，用来继承
    pass

class Cat(Animal):      #定义类，属于子类
    def test(self):     #子类也能自己定义方法
        print('子类中自己定义的方法')


dog=Dog()   #定义实例
dog.run()   #子类获得父类中的run方法

cat=Cat()
cat.run()
cat.test()  #获取子类自己定义的方法
