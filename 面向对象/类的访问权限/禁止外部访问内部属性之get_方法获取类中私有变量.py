#/usr/bin/python3
#-*-coding:UTF-8-*-

class Student(object):
    def __init__(self,name,score):
        self.__name=name    #定义私有变量
        self.__score=score

    def info(self):
        print('学生：%s\n分数：%d'%(self.__name,self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):    #通过get_score方法获取私有变量，也就是内部的属性值
        return self.__score #输出get_score方法获取到的私有变量

stu=Student('张三',99)

print('修改前分数:',stu.get_score(),stu.get_name())
stu.info()
