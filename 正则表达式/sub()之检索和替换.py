#/usr/bin/python3
#-*-coding:UTF-8-*-

import re

content='54aK54yr5oiR54ix5L2g'
content=re.sub('\D+','',content)

print(content)

#第一个传入的参数\D来匹配所有的字母,作用为替换掉这些字母
#第二个参数是替换成的字符串,''不加参数则为空
#第三个参数就是原字符串
#输出结果为排除了字母，只输出了所有的数字


html = '''<div id="songs-list">
    <h2 class="title">经典老歌</h2>
    <p class="introduction">
        经典老歌列表
    </p>
    <ul id="list" class="list-group">
        <li data-view="2">一路上有你</li>
        <li data-view="7">
            <a href="/2.mp3" singer="任贤齐">沧海一声笑</a>
        </li>
        <li data-view="4" class="active">
            <a href="/3.mp3" singer="齐秦">往事随风</a>
        </li>
        <li data-view="6"><a href="/4.mp3" singer="beyond">光辉岁月</a></li>
        <li data-view="5"><a href="/5.mp3" singer="陈慧琳">记事本</a></li>
        <li data-view="5">
            <a href="/6.mp3" singer="邓丽君"><i class="fa fa-user"></i>但愿人长久</a>
        </li>
    </ul>
</div>'''

html=re.sub('<div.*?>|</div>|<h2.*?>|</h2>|<p.*?>|</p>|<ul.*?>|</ul>|<li.*?>|</li>|<a.*?>|</a>|<i.*?>|</i>','',html)
#html=re.sub('</ul.*?>|</ul>|<div.*?>|</div>|</p.*?>|</p>|<h2.*?>|</h2>|<li.*?>|</li>|<a.*?>|</a>','',html)
print(html.strip())
