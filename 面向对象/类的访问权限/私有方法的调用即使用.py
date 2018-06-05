#/usr/bin/python3
#-*-coding:UTF-8-*-

class Xls(object):
    def __init__(self):
        pass

    def __foo(self):
        print('这是私有方法')

    def foo(self):
        print('这是公有方法')
        print('公有方法调用私有方法')

        self.__foo()
        print('公有方法调用私有方法结束')

test=Xls()
print('开始调用公有方法')
test.foo()

print('开始调用私有方法')
test.__foo()


#私有方法除了用get_value方法获取之外，还能在内部以公有方法调用，但是不能在
#外部直接调用私有方法
