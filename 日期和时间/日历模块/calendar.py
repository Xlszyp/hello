#/usr/bin/python3
#-*-coding:UTF-8-*-

import calendar
'''
class Calendar(object):
    """
    Base calendar class. This class doesn't do any formatting. It simply
    provides data to subclasses.
    """
    ................................................

class TextCalendar(Calendar):
    """
    Subclass of Calendar that outputs a calendar as a simple plain text
    similar to the UNIX program cal.
    """
    ................................................

class HTMLCalendar(Calendar):
    """
    This calendar returns complete HTML pages.
    """
    ................................................
'''

'''
calendar.setfirstweekday(weekday)
设置每周的起始日期码。0（星期一）到6（星期日）。

calendar.firstweekday()
返回当前每周起始日期的设置。默认情况下，首次载入calendar模块时返回0，即星期一。

'''
calendar.setfirstweekday(calendar.SUNDAY)
print(calendar.firstweekday())

'''
calendar.calendar(year,w=2,l=1,c=6)
返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。
每日宽度间隔为w字符。
每行长度为21* W+18+2* C。l是每星期行数。
'''
c = calendar.calendar(2018)
# c = calendar.TextCalendar()
# c = calendar.HTMLCalendar()
print(c)

'''
calendar.isleap(year)
是闰年返回True，否则为false。
'''
print(calendar.isleap(2016))

'''
calendar.leapdays(y1,y2)
返回在Y1，Y2两年之间的闰年总数。
'''
print(calendar.leapdays(2010, 2017))

'''
calendar.month(year,month,w=2,l=1)
返回一个多行字符串格式的year年month月日历，两行标题，一周一行。
每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
'''
m = calendar.month(2017, 7)
print(m)

'''
calendar.monthcalendar(year,month)
返回一个整数的单层嵌套列表。每个子列表装载代表一个星期的整数。
Year年month月外的日期都设为0;范围内的日子都由该月第几日表示，从1开始。
'''
print(calendar.monthcalendar(2017, 7))

'''
calendar.monthrange(year,month)
返回两个整数。第一个是该月的首日所在星期的日期码(0~6)，第二个是该月的天数(28-31)。
'''
print(calendar.monthrange(2017, 7))

'''
calendar.timegm(tupletime)
和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间辍（1970纪元后经过的浮点秒数）。
很多Python函数用一个元组装起来的9组数字处理时间:
序号     字段    值
   4位数年    2008
   月    1 到 12
   日    1到31
   小时    0到23
   分钟    0到59
   秒    0到61 (60或61 是闰秒)
   一周的第几日    0到6 (0是周一)
   一年的第几日    1到366 (儒略历)
   夏令时    -1, 0, 1, -1是决定是否为夏令时的旗帜

上述也就是struct_time元组。这种结构具有如下属性：
序号    属性    值
   tm_year    2008
   tm_mon    1 到 12
   tm_mday    1 到 31
   tm_hour    0 到 23
   tm_min    0 到 59
   tm_sec    0 到 61 (60或61 是闰秒)
   tm_wday    0到6 (0是周一)
   tm_yday    1 到 366(儒略历)
   tm_isdst    -1, 0, 1, -1是决定是否为夏令时的旗帜
'''
print(calendar.timegm((2017, 7, 24, 11, 19, 0, 0, 0, 0)))

'''
calendar.weekday(year,month,day)
返回给定日期的日期码。0（星期一）到6（星期日）。月份为 1（一月） 到 12（12月）。
'''
print(calendar.weekday(2017, 7, 23))
