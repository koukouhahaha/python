# -*- coding: utf-8 -*-
"""
Created on Thu Jun 21 15:52:44 2018
练习六：获取淘宝数据并且展示(只要第一页的商品48个)
1.每一行显示4个商品信息(商品名，价格，付款，店铺名,地址，)
2.列出12排商品
3.给商品排序，从价格高到低
4.给商品排序，按照销量排序
5.商品过滤，只要15天退款的商品，包邮的商品

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='https://s.taobao.com/search?q=%E8%82%89%E6%9D%BE&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&ajax=true'
data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
import json
data=json.loads(data)

#data字典-》mods 字典-》itemlist 字典-》data字典-》auctions 列表-》index 0 字典-》raw_title 变量
data['mods']['itemlist']['data']['auctions'][0]['raw_title']


for i in range(10):
    for j in range(4):
        a=data['mods']['itemlist']['data']['auctions'][i+j*4]['raw_title']
        b=data['mods']['itemlist']['data']['auctions'][i+j*4]['view_price']
        c=data['mods']['itemlist']['data']['auctions'][i+j*4]['view_sales']
        d=data['mods']['itemlist']['data']['auctions'][i+j*4]['nick']
        e=data['mods']['itemlist']['data']['auctions'][i+j*4]['item_loc']
        print("商品名:{},价格:{},付款人数:{},店铺名:{},地址:{}".format(a,b,c,d,e))
    print("\n-----------------")
    
ls=[]
for i in range(36):
    b=data['mods']['itemlist']['data']['auctions'][i]['view_price']
    b1=float(b)
    ls.append(b1)
sorted(ls)
lls=sorted(ls,reverse=True)
print(lls)

import re   
ls=[]
for i in range(36):
    c=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
    c1=re.sub("\D","",c)
    c2=int(c1)
    ls.append(c2)
sorted(ls)
lls=sorted(ls,reverse=True)
print(lls)

for i in range(36):
    a=data['mods']['itemlist']['data']['auctions'][i]['raw_title']
    b=data['mods']['itemlist']['data']['auctions'][i]['view_fee']
    if b=='0.00':
        print("商品名:{}".format(a))

for i in range(36):
    a=data['mods']['itemlist']['data']['auctions'][i]['raw_title']
    try:
        f=data['mods']['itemlist']['data']['auctions'][i]['icon'][1]['iconPopupComplex']['popup_title']
        print('商品名称为{},提供{}'.format(a,f))
    except Exception as eer:
        print('商品名称为{},不提供保险理赔'.format(a))