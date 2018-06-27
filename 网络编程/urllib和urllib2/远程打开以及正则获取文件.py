#!/use/bin/python3
#-*-coding:UTF-8-*-

from urllib.request import urlopen
import re

#打开远程文件
webpage=urlopen('http://www.python.org')

#正则获取
text=webpage.read()
m=re.search('<a href="([^"]+)".*?>about</a>',text,re.IGNORECASE)
print(m.group(1))
