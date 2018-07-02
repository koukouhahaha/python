# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 17:25:41 2018
函数：
变量(生命周期)
全局变量，局部变量(函数内)
练习五:实现练习四，
1.使用函数写出来。定义函数，输出每一天6:00,12:00,18:00的天气信息
2.打印折线图,使用字符串的*号操作
10----------
5-----
@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)



def time(i):
    time=data['list'][i]['dt_txt']
    return time
def a(i):
    a=data['list'][i]['main']['temp']
    return a
def b(i):
    b=data['list'][i]['weather'][0]['main']
    return b
def c(i):
    c=data['list'][i]['main']['pressure']
    return c
def d(i):
    d=data['list'][i]['main']['temp_max']
    return d
def e(i):
    e=data['list'][i]['main']['temp_min']
    return e
def msg(time,a,b,c,d,e):
    print('时间:{},温度是:{},天气是：{},气压是：{},最高温度是：{},最低温度是：{}'.format(time,a,b,c,d,e))
msg(time(0),a(0),b(0),c(0),d(0),e(0))
msg(time(2),a(2),b(2),c(2),d(2),e(2))
msg(time(7),a(7),b(7),c(7),d(7),e(7))
msg(time(8),a(8),b(8),c(8),d(8),e(8))
msg(time(10),a(10),b(10),c(10),d(10),e(10))
msg(time(15),a(15),b(15),c(15),d(15),e(15))
msg(time(16),a(16),b(16),c(16),d(16),e(16))
msg(time(18),a(18),b(18),c(18),d(18),e(18))
msg(time(23),a(23),b(23),c(23),d(23),e(23))
msg(time(24),a(24),b(24),c(24),d(24),e(24))
msg(time(26),a(26),b(26),c(26),d(26),e(26))
msg(time(31),a(31),b(31),c(31),d(31),e(31))
msg(time(32),a(32),b(32),c(32),d(32),e(32))
msg(time(34),a(34),b(34),c(34),d(34),e(34))


def y(i):
    print(int(a(i))*'-')
y(0)
y(2)
y(7)
y(8)
y(10)
y(15)
y(16)
y(18)
y(23)
y(24)
y(26)
y(31)
y(32)
y(34)


    


    