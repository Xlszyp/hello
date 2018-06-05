#/usr/bin/python3
#-*-coding:UTF-8-*-

class Animal(object):
    def run(self):
        print('Animal is runing...')

    def jump(self):
        print('Animal is jumping...')

    def __run(self):    #定义私有方法
        print('Iam a private method')

    def f(self):        #定义公有方法
        self.__run()    #获取私有方法

class Dog(Animal):
    pass

class Cat(Animal):
    pass


dog=Dog()
dog.run()
dog.jump()

cat=Cat()
cat.run()
cat.jump()
cat.f()
    
