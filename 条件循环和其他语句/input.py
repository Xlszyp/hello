#/usr/bin/python3
#-*-coding:UTF-8-*-

name='Hello world!'

while True:

    name_input=input('请输入：')

    if name!=name_input:

        print('ERROR！请重新输入！')

    else:

        print('emmmmmmmmmm...')
        break


#input语句需要放进while循环中才能在错误的时候继续循环调用input输出，直到正确再跳出循环
