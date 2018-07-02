# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 11:46:57 2018
1.打印每天的6:00,12:00,18:00的天气(城市,温度，情况，气压，最高温度，最低温度)
2.同上写出[英文版的]
3.根据天气的情况，给出建议：例如，今天下雨，提示带伞。今天温度高，穿衬衫...三个件以上
@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
ls=[]
city1=data['city']['name']
time1=data['list'][0]['dt_txt']
a1=data['list'][0]['main']['temp']
b1=data['list'][0]['weather'][0]['main']
c1=data['list'][0]['main']['pressure']
d1=data['list'][0]['main']['temp_max']
e1=data['list'][0]['main']['temp_min']
print("{}{}temp:{}，description:{},pressure:{},max_temp:{},min_temp:{}".format(city1,time1,a1,b1,c1,d1,e1))
if b1=='Sunny':
    print("记得带伞，多喝水，注意防晒")
if b1=='Clouds':
    print("记得带伞，多喝水，注意防水")
if b1=='Clear':
    print("记得带伞，多喝水，注意防水")
ls.append(a1)
city=data['city']['name']
time2=data['list'][2]['dt_txt']
a2=data['list'][2]['main']['temp']
b2=data['list'][2]['weather'][0]['main']
c2=data['list'][2]['main']['pressure']
d2=data['list'][2]['main']['temp_max']
e2=data['list'][2]['main']['temp_min']
print("{}{}temp:{}，description:{},pressure:{},max_temp:{},min_temp:{}".format(city,time2,a2,b2,c2,d2,e2),"pay attention:today is cloudy,you should drink more water,take sunglass and umbraller")
ls.append(a2)
city=data['city']['name']
time3=data['list'][4]['dt_txt']
a3=data['list'][4]['main']['temp']
b3=data['list'][4]['weather'][0]['main']
c3=data['list'][4]['main']['pressure']
d3=data['list'][4]['main']['temp_max']
e3=data['list'][4]['main']['temp_min']
print("{}{}temp:{}，description:{},pressure:{},max_temp:{},min_temp:{}".format(city,time3,a3,b3,c3,d3,e3),"pay attention:today is sunny,you should drink more water,take sunglass and umbraller")
ls.append(a3)
city=data['city']['name']
time4=data['list'][8]['dt_txt']
a4=data['list'][8]['main']['temp']
b4=data['list'][8]['weather'][0]['main']
c4=data['list'][8]['main']['pressure']
d4=data['list'][8]['main']['temp_max']
e4=data['list'][8]['main']['temp_min']
print("{}{}temp:{}，description:{},pressure:{},max_temp:{},min_temp:{}".format(city,time4,a4,b4,c4,d4,e4),"pay attention:today is sunny,you should drink more water,take sunglass and umbraller")
ls.append(a4)
city=data['city']['name']
time5=data['list'][10]['dt_txt']
a5=data['list'][10]['main']['temp']
b5=data['list'][10]['weather'][0]['main']
c5=data['list'][10]['main']['pressure']
d5=data['list'][10]['main']['temp_max']
e5=data['list'][10]['main']['temp_min']
print("{}{}temp:{}，description:{},pressure:{},max_temp:{},min_temp:{}".format(city,time5,a5,b5,c5,d5,e5),"pay attention:today is sunny,you should drink more water,take sunglass and umbraller")
ls.append(a5)
city=data['city']['name']
time6=data['list'][12]['dt_txt']
a6=data['list'][12]['main']['temp']
b6=data['list'][12]['weather'][0]['main']
c6=data['list'][12]['main']['pressure']
d6=data['list'][12]['main']['temp_max']
e6=data['list'][12]['main']['temp_min']
print("{}{}temp:{}，description:{},pressure:{},max_temp:{},min_temp:{}".format(city,time6,a6,b6,c6,d6,e6),"pay attention:today is sunny,you should drink more water,take sunglass and umbraller")
ls.append(a6)
city=data['city']['name']
time7=data['list'][16]['dt_txt']
a7=data['list'][16]['main']['temp']
b7=data['list'][16]['weather'][0]['main']
c7=data['list'][16]['main']['pressure']
d7=data['list'][16]['main']['temp_max']
e7=data['list'][16]['main']['temp_min']
print("{}{}temp:{}，description:{},pressure:{},max_temp:{},min_temp:{}".format(city,time7,a7,b7,c7,d7,e7),"pay attention:today is sunny,you should drink more water,take sunglass and umbraller")
ls.append(a7)
city=data['city']['name']
time8=data['list'][18]['dt_txt']
a8=data['list'][18]['main']['temp']
b8=data['list'][18]['weather'][0]['main']
c8=data['list'][18]['main']['pressure']
d8=data['list'][18]['main']['temp_max']
e8=data['list'][18]['main']['temp_min']
print("{}{}temp:{}，description:{},pressure:{},max_temp:{},min_temp:{}".format(city,time8,a8,b8,c8,d8,e8),"pay attention:today is sunny,you should drink more water,take sunglass and umbraller")
ls.append(a8)
city=data['city']['name']
time9=data['list'][20]['dt_txt']
a9=data['list'][20]['main']['temp']
b9=data['list'][20]['weather'][0]['main']
c9=data['list'][20]['main']['pressure']
d9=data['list'][20]['main']['temp_max']
e9=data['list'][20]['main']['temp_min']
print("{}{}temp:{}，description:{},pressure:{},max_temp:{},min_temp:{}".format(city,time9,a9,b9,c9,d9,e9),"pay attention:today is sunny,you should drink more water,take sunglass and umbraller")
ls.append(a9)
city=data['city']['name']
time10=data['list'][24]['dt_txt']
a10=data['list'][24]['main']['temp']
b10=data['list'][24]['weather'][0]['main']
c10=data['list'][24]['main']['pressure']
d10=data['list'][24]['main']['temp_max']
e10=data['list'][24]['main']['temp_min']
print("{}{}temp:{}，description:{},pressure:{},max_temp:{},min_temp:{}".format(city,time10,a10,b10,c10,d10,e10),"pay attention:today is sunny,you should drink more water,take sunglass and umbraller")
ls.append(a10)
city=data['city']['name']
time11=data['list'][26]['dt_txt']
a11=data['list'][26]['main']['temp']
b11=data['list'][26]['weather'][0]['main']
c11=data['list'][26]['main']['pressure']
d11=data['list'][26]['main']['temp_max']
e11=data['list'][26]['main']['temp_min']
print("{}{}temp:{}，description:{},pressure:{},max_temp:{},min_temp:{}".format(city,time11,a11,b11,c11,d11,e11),"pay attention:today is sunny,you should drink more water,take sunglass and umbraller")
ls.append(a11)
city=data['city']['name']
time12=data['list'][28]['dt_txt']
a12=data['list'][28]['main']['temp']
b12=data['list'][28]['weather'][0]['main']
c12=data['list'][28]['main']['pressure']
d12=data['list'][28]['main']['temp_max']
e12=data['list'][28]['main']['temp_min']
print("{}{}temp:{}，description:{},pressure:{},max_temp:{},min_temp:{}".format(city,time12,a12,b12,c12,d12,e12),"pay attention:today is sunny,you should drink more water,take sunglass and umbraller")
ls.append(a12)
city=data['city']['name']
time13=data['list'][32]['dt_txt']
a13=data['list'][32]['main']['temp']
b13=data['list'][32]['weather'][0]['main']
c13=data['list'][32]['main']['pressure']
d13=data['list'][32]['main']['temp_max']
e13=data['list'][32]['main']['temp_min']
print("{}{}temp:{}，description:{},pressure:{},max_temp:{},min_temp:{}".format(city,time13,a13,b13,c13,d13,e13),"pay attention:today is sunny,you should drink more water,take sunglass and umbraller")
ls.append(a13)
city=data['city']['name']
time14=data['list'][34]['dt_txt']
a14=data['list'][34]['main']['temp']
b14=data['list'][34]['weather'][0]['main']
c14=data['list'][34]['main']['pressure']
d14=data['list'][34]['main']['temp_max']
e14=data['list'][34]['main']['temp_min']
print("{}{}temp:{}，description:{},pressure:{},max_temp:{},min_temp:{}".format(city,time14,a14,b14,c14,d14,e14),"pay attention:today is sunny,you should drink more water,take sunglass and umbraller")
ls.append(a14)
city=data['city']['name']
time15=data['list'][36]['dt_txt']
a15=data['list'][36]['main']['temp']
b15=data['list'][36]['weather'][0]['main']
c15=data['list'][36]['main']['pressure']
d15=data['list'][36]['main']['temp_max']
e15=data['list'][36]['main']['temp_min']
print("{}{}temp:{}，description:{},pressure:{},max_temp:{},min_temp:{}".format(city,time15,a15,b15,c15,d15,e15),"pay attention:today is sunny,you should drink more water,take sunglass and umbraller")
ls.append(a15)
ls=sorted(ls)
print(ls)
def msg(x):
    print(int(x)*'-')
msg(a1)
msg(a2)
msg(a3)
print(int(a1)*'-')
print(int(a2)*'-')
print(int(a3)*'-')
print(int(a4)*'-')
print(int(a5)*'-')
print(int(a6)*'-')
print(int(a7)*'-')
print(int(a8)*'-')
print(int(a9)*'-')
print(int(a10)*'-')
print(int(a11)*'-')
print(int(a12)*'-')
print(int(a13)*'-')
print(int(a14)*'-')
print(int(a15)*'-')

