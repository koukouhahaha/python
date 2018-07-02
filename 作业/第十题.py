# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 17:10:13 2018
第十题：火车票交互查询
1.动态输入出发站和到达站，然后查询火车票情况
2.将火车余票站中的三字码转换成车站名
3.按照出发时间排序，按照历时时间排序
@author: Administrator
"""

def translate(s):
    ls=open('./火车站编码.csv','r',encoding='utf-8').readlines()
    #开发思路，首先拿到全部的火车站列表-》循环比对是否有 某个火车站(.split(',')[0])，找到之后，[1]
    abc=''
    for i in ls:
        if s==i.split(',')[0]:
            abc=i.split(',')[1]
            break
    return abc

import urllib.request as r#导入联网工具包，命令为r
date=input('请输入日期')
from_station=input('出发站')#北京
from_station=translate(from_station)
to_station=input('到达站')#成都
to_station=translate(to_station)
print(date,from_station,to_station)
#https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2018-07-17&leftTicketDTO.from_station=BJP&leftTicketDTO.to_station=NJH&purpose_codes=0X00
url='https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'
url=url.format(date,from_station,to_station).replace('\n','')
#print(url)
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)
data1=data['data']['result']

p='  '
len([p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p])
title='车次{}出发站{}到达站{}出发时间{}到达时间{}历时{}商务座/特等座{}一等座{}二等座{}高级软卧{}软卧{}动卧{}硬卧{}软座{}硬座{}无座{}其他{}备注'.format(p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p,p)
title=title.split(p)
for i in title:
    print(i.center(9),end='')
for j in range(len(data1)):
    s=data1[j]   
    print()
#车次   车发站，到达站 出发时间,到达时间 历时间
    ls=s.split('|')
    ls[6]=data['data']['map'].get('{}'.format(ls[6]))
    ls[7]=data['data']['map'].get('{}'.format(ls[7]))
    ls=[ls[3],ls[6],ls[7],ls[8],ls[9],ls[10],ls[32],ls[31],ls[30],ls[21],ls[23],'--',ls[28],'--',ls[29],ls[26],'--',ls[1]]
    for i in ls:
        print(str(i).center(11),end='')

mysort=lambda x:x.split('|')[10]
ls.sort(key=mysort,reverse=True)

       
time=[]
for i in range(len(data1)):
    s=data1[i]
    ls=s.split('|')
    ll=ls[10]
    time.append(ll)
sorted(time)

time1=[]
for i in range(len(data1)):
    s=data1[i]
    ls=s.split('|')
    ll=ls[8]
    time1.append(ll)
    #print()
sorted(time1)