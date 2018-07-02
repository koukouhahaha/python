# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 10:01:58 2018




题目十二：使用re爬取天气信息
1.天气描述，天气温度，天气气压



@author: Administrator
"""
#####11

    
#####12
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=chongqing,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
print(data)
import re
ls1=re.compile('"description":"(.*?)"').findall(data)
ls2=re.compile('"temp":(.*?),',re.S).findall(data)
ls3=re.compile('"pressure":(.*?),').findall(data)
ls4=re.compile('"dt_txt":"(.*?)"').findall(data)
for i in range(len(ls4)):
    print("日期:{},描述:{},温度:{},气压:{}".format(ls4[i],ls1[i],ls2[i],ls3[i]))

