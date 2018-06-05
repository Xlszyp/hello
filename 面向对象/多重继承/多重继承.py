#/usr/bin/python3
#-*-coding:UTF-8-*-

class Animal(object):   #定义大类：动物，属父类
    pass

class Mammal(Animal):   #定义类：哺乳动物，继承动物Animal
    pass

class Bird(Animal):     #定义类：鸟类，继承动物Animal
    pass

class Dog(Mammal):      #定义类：狗，继承哺乳动物Mammal
    pass

class Bat(Mammal):      #定义类：蝙蝠，继承哺乳动物Mammal
    pass

class Parrot(Bird):     #定义类：鹦鹉，继承鸟类Bird
    pass

class Ostrich(Bird):    #定义类：鸵鸟，继承鸟类Bird
    pass

class Runnable(object): #定义类：奔跑的，属父类
    def run(self):
        print('Running...')

class Flyable(object):  #定义类：飞行的，属父类
    def fly(self):
        print('Flying...')

class Dog(Mammal,Runnable):     #定义类狗，分别继承哺乳动物Mammal、奔跑的Runnable
    def run(self):
        print('Dog is running...')
class Bat(Mammal,Flyable):      #定义类蝙蝠，分别继承哺乳动物Mammal、飞行的Flyable
    def fly(self):
        print('Bat is flying...')
class Parrot(Bird,Flyable):
    def fly(self):
        print('Parrot is flying')
class Ostrich(Bird,Runnable):
    def run(self):
        print('Ostrich is running...')

dog=Dog()
dog.run()

bat=Bat()
bat.fly()

parrot=Parrot()
parrot.fly()

ostrich=Ostrich()
ostrich.run()
