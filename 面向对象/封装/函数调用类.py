#/usr/bin/python3
#-*-coding:UTF-8-*-

#普通方法，函数调用类
class Student(object):
    def __init__(self,name,score):
        self.name=name
        self.score=score

    def info(self):
        print('学生：%s\n分数：%d'%(self.name,self.score))

stu=Student('Zhangsan',66)
stu.info()
