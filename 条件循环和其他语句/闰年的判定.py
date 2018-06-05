#!/usr/bin/python3
#-*-coding:UTF-8-*-

year=int(input('请输入年份：'))
if year%4==0 and year%100!=0:
    print('{}为闰年'.format(year))
elif year%400==0:
        print('{}为闰年'.format(year))
else:
            print('{}不是闰年'.format(year))
