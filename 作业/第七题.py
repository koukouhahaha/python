# -*- coding: utf-8 -*-
"""
Created on Fri Jun 22 13:57:23 2018
练习七:全球天气未来3天
1.使用多选其一，完成天气的提醒
2.一定要多ci使用到for循环,偶尔用一次while循环
3.初步学会使用debug，知道里面的设置断点，下一步执行，下一个断点执行。
4.《闪屏的制作》进入我们天气程序的时候，有一个温馨图形的提示。使用循环实现，
  要知道是什么意思，照抄网上代码不行。
@author: Administrator
"""
import urllib.request as r#导入联网工具包，命令为r
url='http://api.openweathermap.org/data/2.5/forecast?q=zhengzhou,cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)

print("     \   |   /   ")
print("       ____       ")          
print("---   /    \   --- ")     
print("     | ~  ~ |      ")   
print("---   \__O_/   --- ")
print("     /    |    \   ")                          
for i in range(5):
    print("    !!!!!!!!!!    ")
    print("      notice      ")
for i in range(0,30):
    time=data['list'][i]['dt_txt']
    desc=data['list'][i]['weather'][0]['description']
    if desc=='晴':
        print(time,"出门请带伞 注意防晒 多喝水")
    elif desc=='阴':
        print(time,"出门请带伞 多喝水 可出门活动")
    elif desc=='多云':
        print(time,"出门请带伞 多喝水 可出门活动")
    else:
        print(time,"出门请带伞 多喝水 注意防水")
