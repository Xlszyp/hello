#/usr/bin/python3
#-*-coding:UTF-8-*-

class Animal(object):
    def run(self):
        print('Animal is running...')
    
class Dog(Animal):
    def run(self):
        print('Dog is running')

class Cat(Animal):
    def run(self,score):
        print('Cat is running：',score,'米')


dog=Dog()
dog.run()

cat=Cat()
cat.run(66)

if isinstance(Dog,Animal)==True:
    print('Dog数据类型正确')

else:
        print('Dog is False')


if isinstance(Animal,object)==True:
    print('Animal数据类型正确')

else:
    print('Animal is False')

#isinstance()函数使用方法：isinstance(class1,class2),类型相同返回True,不同则返回False
#能用type()判断的基本类型也可以用isinstance()判断
