#/usr/bin/python3
#-*-coding:UTF-8-*-


#定义天气查找类，类中定义两个方法，一个方法根据传入的input_daytime值返回对应的可见度，一个返回对应的温度
class WeatherSearch(object):

    def __init__(self,input_daytime):   #定义input_daytime方法

        self.input_daytime=input_daytime

    def seach_visibility(self):         #定义搜索可见度方法

        visible_leave=0                 #可见度初始值为0

        if self.input_daytime=='daytime':

            visible_leave=2             #当输入daytime时可见度的级别为2

        if self.input_daytime=='night':

            visible_leave=9             #当输入night时可见度的级别为9

        return visible_leave


    def seach_temperature(self):        #定义搜索温度方法

        temperature=0                   #温度初始值为0

        if self.input_daytime=='daytime':

            temperature=26              #当输入daytime时温度为26

        if self.input_daytime=='night':

            temperature=16              #当输入night时温度为16

        return temperature


#定义建议类，该类继承WeatherSearch类，类中定义两个方法，一个覆盖父类的温度查找方法，具有传入input_daytime的值，返回建议使用的交通工具，另一个方法返回整体建议
class OutAdvice(WeatherSearch):

    def __init__(self,input_daytime):   

        WeatherSearch.__init__(self,input_daytime)  #传入input_daytime的值

    def seach_temperature(self):    #覆盖父类的温度查找方法

        vehicle=''

        if self.input_daytime=='daytime':

            vehicle='bike'          #当输入daytime则返回bike

        if self.input_daytime=='night':

            vehicle='taxi'          #当输入night则返回taxi

        return vehicle


    def out_advice(self):

        visible_leave=self.seach_visibility()   #可见度级别=可见度

        if visible_leave==2:    #当可见度=2则调用搜索温度方法中的daytime，返回bike

            print('The weather is good,suitable for use %s.'%self.seach_temperature())

        elif visible_leave==9:  #当可见度=9则调用搜索温度方法中的night，返回taxi

            print('The weather is bad,you should use %s.'%self.seach_temperature())

        else:

            print('The weather is beyond my scope,I can not give you any advice')


check=OutAdvice('night')
check.out_advice()
print(check.seach_temperature())
