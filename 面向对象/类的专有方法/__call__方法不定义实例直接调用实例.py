#/usr/bin/python3
#-*-coding:UTF-8-*-

class Student(object):
    def __init__(self,name):
        self.name=name

    #def __str__(self):
     #   return '名称：%s'%self.name

    def __call__(self):
        print('名称：%s'%(self.name))

stu=Student('Zhangsan')
print(stu)

