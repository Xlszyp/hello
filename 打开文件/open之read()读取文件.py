#/usr/bin/python3
#-*-coding:UTF-8-*-

#path='D:/1.txt'

name=open('D:/1.txt','r')

print('read result:',name.read(10))
print('read results:',name.read())


#10代表读取文件中的10个字节的内容,如不加任何参数则默认返回该文件内所有内容
