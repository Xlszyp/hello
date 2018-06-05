#/usr/bin/python3
#-*-coding:UTF-8-*-

import re

#贪婪匹配
content='Hello 1234567 World_This is a Regex Demo'

result=re.match('^He.*(\d+).*Demo$',content)

print(result)
print('')
print(result.group())
print('贪婪模式的输出：',result.group(1))
print('')

#非贪婪匹配
results=re.match('^He.*?(\d+).*Demo$',content)

print(results)
print('')
print('非贪婪模式的输出：',results.group(1))

#贪婪匹配下.*会尽可能匹配多的字符，所以在贪婪匹配中.*将数字123456也匹配进去,剩下7来满足(\d+),所以得到的内容就只有7

#非贪婪匹配下.*?会尽可能的少匹配字符,所以在非贪婪匹配中.*?匹配到Hello后面的空格后就是数字，刚好满足(\d+)匹配,即停止匹配,后面的数字交给(\d+)去匹配，所以得出1234567
