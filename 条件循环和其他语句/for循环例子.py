print('---for的字符串循环---')
a='hello,world'
for x in a:
    print(x)

print('---for的数字循环---')
number=[1,2,3,4,5]
for num in number:
    print(num)


print('---dict的for循环---')
zidian={'name':'Zhangsan','num':'1001'}
for y in zidian:
    print('%s:%s'%(y,zidian[y]))
