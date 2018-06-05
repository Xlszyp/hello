#/usr/bin/python3
#-*-coding:UTF-8-*-

f=open('D:/1.txt','w')
str_list=['hello,world\n','welcome\n','welcome\n']

print('write length:',f.writelines(str_list))

f=open('D:/1.txt','r')
print('read result:',f.read())

f=open('D:/1.txt','r')
print(f.readline())

f=open('D:/1.txt','r')
print(f.readlines())


#readline()方法是从文件中读取单独一行内容并返回
#readlines()方法是从文件中读取所有的内容并返回
#writelines()方法会将所有格式的字符串写入文件,等同于write()方法
