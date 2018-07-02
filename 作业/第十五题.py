# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 09:46:32 2018

题目十五：未来三天 天气类天气对象
1.定义一个天气类Weather 静态的属性(temp,description,pre) 动态属性(msg打印当前天气属性)
2.创建3天的天气对象，并调用msg方法

@author: Administrator
"""

class Weather:
    #天气对象产生的时候，会调用这个方法Weather()
    def __init__(self,temp,description,pre):
        self.temp=temp
        self.description=description
        self.pre=pre
    def msg(self):
        print("温度为{},{},气压为{}".format(self.temp,self.description,self.pre))

a=Weather('15','多云','1584')
b=Weather('25','小雨','15854')
c=Weather('36','晴','1574')
a.msg()
b.msg()
c.msg()