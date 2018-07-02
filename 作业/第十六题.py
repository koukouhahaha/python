# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 12:59:48 2018


题目十六：高考派2300数据统计
1.根据2300下载的两百多M文件，统计招生总人数
2.统计7各地域的人数各是多少
3.计算比例


@author: Administrator
"""

w1=0
w2=0
w3=0
w4=0
w5=0
w6=0
w7=0
ls7=[]#华北
ls6=[]#西北
ls5=[]#西南
ls4=[]#华南
ls3=[]#华中
ls2=[]#华东
ls1=[]#东北
qq={}
ls9=[] 
f=open('C:/Users/Administrator/Desktop/1212/全国招生计划表0206C正确.txt','r',encoding='utf-8')
p=f.readlines()
import json
for i in range(142600):
    qq[i]=json.loads(p[i])
for y in range(142600):
    if qq[y]['status']==1:
        ls9.append(qq[y])
for e in range(len(ls9)):
    for j in range(len(ls9[e]['data'])):
        if ls9[e]['data'][j]['city']=='黑龙江' or ls9[e]['data'][j]['city']=='吉林' or ls9[e]['data'][j]['city']=='辽宁' or ls9[e]['data'][j]['city']=='吉林' or ls9[e]['data'][j]['city']=='吉林':
            ls1.append(ls9[e])
            break
        elif ls9[e]['data'][j]['city']=='福建' or ls9[e]['data'][j]['city']=='江西' or ls9[e]['data'][j]['city']=='山东' or ls9[e]['data'][j]['city']=='上海' or ls9[e]['data'][j]['city']=='江苏' or ls9[e]['data'][j]['city']=='浙江' or ls9[e]['data'][j]['city']=='安徽':
            ls2.append(ls9[e])
            break
        elif ls9[e]['data'][j]['city']=='河南' or ls9[e]['data'][j]['city']=='湖北' or ls9[e]['data'][j]['city']=='湖南':
            ls3.append(ls9[e])
            break
        elif ls9[e]['data'][j]['city']=='广东' or ls9[e]['data'][j]['city']=='广西' or ls9[e]['data'][j]['city']=='海南':
            ls4.append(ls9[e])
            break
        elif ls9[e]['data'][j]['city']=='四川' or ls9[e]['data'][j]['city']=='贵州' or ls9[e]['data'][j]['city']=='云南' or ls9[e]['data'][j]['city']=='重庆' or ls9[e]['data'][j]['city']=='西藏':
            ls5.append(ls9[e])
            break
        elif ls9[e]['data'][j]['city']=='陕西' or ls9[e]['data'][j]['city']=='甘肃' or ls9[e]['data'][j]['city']=='青海' or ls9[e]['data'][j]['city']=='宁夏' or ls9[e]['data'][j]['city']=='新疆':
            ls6.append(ls9[e])
            break
        elif ls9[e]['data'][j]['city']=='北京' or ls9[e]['data'][j]['city']=='天津' or ls9[e]['data'][j]['city']=='山西' or ls9[e]['data'][j]['city']=='河北' or ls9[e]['data'][j]['city']=='内蒙古':
            ls7.append(ls9[e])
            break
            
for i in range(len(ls1)):
    for j in range(len(ls1[i]['data'])):
        t1=int(ls1[i]['data'][j]['plan'])
        w1=w1+t1
print("在东北地区的招生人数为{}".format(w1))

for i in range(len(ls2)):
    for j in range(len(ls2[i]['data'])):
        t2=int(ls2[i]['data'][j]['plan'])
        w2=w2+t2
print("在华东地区的招生人数为{}".format(w2))

for i in range(len(ls3)):
    for j in range(len(ls3[i]['data'])):
        t3=int(ls3[i]['data'][j]['plan'])
        w3=w3+t3
print("在华中地区的招生人数为{}".format(w3))

for i in range(len(ls4)):
    for j in range(len(ls4[i]['data'])):
        t4=int(ls4[i]['data'][j]['plan'])
        w4=w4+t4
print("在华南地区的招生人数为{}".format(w4))

for i in range(len(ls5)):
    for j in range(len(ls5[i]['data'])):
        t5=int(ls5[i]['data'][j]['plan'])
        w5=w5+t5
print("在西南地区的招生人数为{}".format(w5))

for i in range(len(ls6)):
    for j in range(len(ls6[i]['data'])):
        t6=int(ls6[i]['data'][j]['plan'])
        w6=w6+t6
print("在西北地区的招生人数为{}".format(w6))

for i in range(len(ls7)):
    for j in range(len(ls7[i]['data'])):
        t7=int(ls7[i]['data'][j]['plan'])
        w7=w7+t7
print("在华北地区的招生人数为{}".format(w7))

s=w1+w2+w3+w4+w5+w6+w7
print("招生总人数为{}".format(s))

