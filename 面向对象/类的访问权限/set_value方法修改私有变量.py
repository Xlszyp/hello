#/usr/bin/python3
#-*-coding:UTF-8-*-

class Student(object):  #定义类
    def __init__(self,name,score):  #定义init构造方法并含有两个属性值（变量）
        self.__name=name    #将类中方法的变量私有化
        self.__score=score

    def info(self):     #定义方法，获取init方法中的属性值，调用用以输出
        print('学生：%s\n分数：%d'%(self.__name,self.__score))

    def get_score(self):    #使用get_value方法获取类中的私有变量：score
        return self.__score

    def set_score(self,score):  #使用set_value方法修改类中的私有变量：score
        self.__score=score

stu=Student('张三',95)    #定义实例
print('修改前的分数',stu.get_score())

stu.info()

stu.set_score(0)    #修改类中的私有变量

print('修改过后的分数',stu.get_score())

stu.info()

#最后输出的值都是在定义了实例之后，所有输出的语句都需要加上实例名.的前缀接定义的方法
