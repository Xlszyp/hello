#/usr/bin/python3
#-*-coding:UTF-8-*-

class Animal(object):   #定义的父类
    def run(self):
        print('`Animal is running')

class Dog(Animal):      #定义的子类
    def run(self):
        print('Dog is running')

class Cat(Animal):      #定义的子类
    def run(self):
        print('Cat is running')

animal=Animal()
animal.run()

dog=Dog()
print('实例化Dog类')
dog.run()


cat=Cat()
print('实例化Cat类')
cat.run()

#当子类和父类存在相同的run()方法时，子类的run()方法就会覆盖父类的run()方法，在代码运行时总是会调用子类的run()方法
