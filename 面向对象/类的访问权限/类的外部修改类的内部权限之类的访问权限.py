#/usr/bin/python3
#-*-coding:UTF-8-*-

class Student(object):      #定义类
    def __init__(self,name,score):      #定义init构造方法
        self.name=name
        self.score=score

    def info(self):     #定义方法
        print('学生：%s\n分数：%d'%(self.name,self.score))    #调用init构造方法中name和score参数


stu=Student('张三',99)    #定义实例
print('修改之前的分数',stu.score)
stu.info()      #通过实例调用出方法中的值

stu.score=0     #类的外部修改类的内部属性，将score修改为0

print('修改之后的分数',stu.score)
stu.info()
