#/usr/bin/python3
#-*-coding:UTF-8-*-

class Student(object):
    def __init__(self):
        self.name='Zhangsan'

    def __getattr__(self,attr): #动态返回上个方法没有定义的‘score’
        if attr=='score':
            return 99
        elif attr=='addr':
            return 'Hangzhou'
        else:
            attr=='id'
            return 1

stu=Student()

print('学生名称：%s\n学生成绩：%d\n来自的城市：%s'%(stu.name,stu.score,stu.addr))

print('ID:',stu.id)
