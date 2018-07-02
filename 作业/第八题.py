# -*- coding: utf-8 -*-
"""
Created on Mon Jun 25 11:33:06 2018
第七题：保存淘宝数据(小组项目)
1.每个组员爬取100页数据(同一种商品)，条件是北京，上海，广州，成都...
2.保存的商品信息有(同第六题),并且是以为csv格式保存
3.单个组员求出当前城市的商品的众数(最多的价格)
4.小组文件合并，求出商品的平均价格
@author: Administrator
"""
#import urllib.request as r#导入联网工具包，命令为r
#ur1='https://s.taobao.com/search?q=%E9%9E%8B%E5%AD%90&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306&loc=%E9%95%BF%E6%B2%99&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s=44&ajax=true'
#data=r.urlopen(url).read().decode('utf-8')
#讲str类型转换为dict
#import json
#data=json.loads(data)
        
#def msg(i):
   # a=data['mods']['itemlist']['data']['auctions'][i]['raw_title']
   # b=data['mods']['itemlist']['data']['auctions'][i]['view_price']
   # c=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
   # d=data['mods']['itemlist']['data']['auctions'][i]['nick']
   # e=data['mods']['itemlist']['data']['auctions'][i]['item_loc']
   # f=open('C:/Users/Administrator/Desktop/1212/tao.csv','a')
   # f.write("{},{},{},{},{}\n".format(a,b,c,d,e))
   # f.close()
#for i in range (44):
   # msg(i)

f=open('C:/Users/Administrator/Desktop/1212/ee.csv','a')
for j in range(100):
    import urllib.request as r#导入联网工具包，命令为r
    url='https://s.taobao.com/search?q=%E9%9E%8B%E5%AD%90&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20180625&ie=utf8&loc=%E9%95%BF%E6%B2%99&bcoffset=3&ntoffset=3&p4ppushleft=1%2C48&s={}&ajax=true'.format(j*44)
    data=r.urlopen(url).read().decode('utf-8')
    #讲str类型转换为dict
    import json
    data=json.loads(data)
    for i in range(len(data['mods']['itemlist']['data']['auctions'])):
        a=data['mods']['itemlist']['data']['auctions'][i]['raw_title']
        b=data['mods']['itemlist']['data']['auctions'][i]['view_price']
        c=data['mods']['itemlist']['data']['auctions'][i]['view_sales']
        d=data['mods']['itemlist']['data']['auctions'][i]['nick']
        e=data['mods']['itemlist']['data']['auctions'][i]['item_loc']
        f.write("{},{},{},{},{}\n".format(a,b,c,d,e))
   # print('第{}页数据已经获取'.format(i+1))
f.close()
    #for i in range(len(data['mods']['itemlist']['data']['auctions'])):
     #   msg(i)
#读取文件某一列数据
import csv
with open('C:/Users/Administrator/Desktop/1212/ee.csv','r') as csvfile:
    reader=csv.reader(csvfile)
    column=[row[1] for row in reader]
print(column)

def get_mode(column):  
    mode = [];  
    column_appear = dict((a, column.count(a)) for a in column);  # 统计各个元素出现的次数  
    if max(column_appear.values()) == 1:  # 如果最大的出现为1  
        return;  # 则没有众数  
    else:  
        for k, v in column_appear.items():  # 否则，出现次数最大的数字，就是众数  
            if v == max(column_appear.values()):  
                mode.append(k);  
    return mode;  
print(get_mode(column))




  



        
        
        
    