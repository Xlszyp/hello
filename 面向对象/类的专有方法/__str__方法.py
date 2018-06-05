#/usr/bin/python3
#-*-coding:UTF-8-*-

#old

class Student(object):
    def __init__(self,name):
        self.name=name

    def info(self):
        print('学生名字：%s'%(self.name))


stud=Student('Zhangsan')
stud.info()


#new

class Students(object):
    def __init__(self,names):
        self.names=names

    def __str__(self):
        return '学生name：%s'%(self.names)
    #__repr__=__str__

print(Students('Zhaowu'))


#在交互模式下输入：>>> y=Students('Zhaowu')
                  #>>> y
#<__main__.Students object at 0x02DD5910>
#因为直接显示变量调用的不是__str__(),而是__repr__(),__str__()返回用户看到的字符串
#__repr__()返回的是程序开发者看到的字符串,解决方法则是再定义一个__repr__=__str__
#如果以上new代码不定义__str__()方法则也会输出<__main__.Students object at 0x02DD5910>
