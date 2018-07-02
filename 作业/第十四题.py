# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 10:26:40 2018


题目十四：家长帮大数据爬虫项目
1.根据all_school.txt获取全中国学校网址编号：1304，生成一个2300列表
2.根据http://www.gaokaopai.com/daxue-zhaosheng-学校编号.html 获取全国城市的编号 例如北京：11
3.班级团队(需要下载142600(2300*31*2)次)：
    中国划分区域-分组(城市)
    区域分组员
    如何下载策略-分时间下载
    执行人物2300-分配到自己的任务一般是2300
    保存数据---组长全部合并--班长统计
4.待定


@author: Administrator
"""


######方法一

f=open('C:/Users/Administrator/Desktop/1212/all_school.txt','r',encoding='utf-8')
p=f.read()
import re
ls1=re.compile('jianjie-(.*?).html').findall(p)
ls2=re.compile('(.*?)\t....\t').findall(p)
for i in range(2300):
    print("学校:{}\t\t对应网址编码为:{}".format(ls2[i],ls1[i]))

#g=open('C:/Users/Administrator/Desktop/1212/bianma.csv','a')
#for i in range(2300):
    #f.write('{}'.format(ls[i]))
#f.close()




import urllib.request as r
import re
#url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
#url='http://www.gaokaopai.com/daxue-zhaosheng-477.html'
url='http://www.gaokaopai.com/daxue-0-0-0-0-0-0-0.html'
data='id=2948&type=2&city=50&state=1'.encode()
req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
d=r.urlopen(req).read().decode('utf-8','ignore')
a='<span><a href="http://www.gaokaopai.com/daxue-(.*?)-0-0-0-0-0-0.html">'
b='<span><a href="http://www.gaokaopai.com/daxue-..-0-0-0-0-0-0.html">(.*?)</a></span>'
e=re.compile(a,re.S).findall(d)
f=re.compile(b,re.S).findall(d)
for i in range(len(f)):
    print("{}-{}".format(e[i],f[i]))
g=[]
for i in range(31):
    g.append(e[i])

#
#######方法二
import urllib.request as r#导入联网工具包，命令为r
url='file///C:/Users/Administrator/Desktop/1212/all_school.txt'
data=r.urlopen(url).read().decode('utf-8')
import re
ls=re.compile('jianjie-(.*?).html').findall(data)
print(ls)










##########14.3

import urllib.request as r
for i in ls1:
    url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
    data='id={}&type=2&city=54&state=1'.format(i).encode()
    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
    d=r.urlopen(req).read().decode('utf-8','ignore')
    if d[0]=='{':
        f=open('./ting2.txt','a')
        f.write('{}\n'.format(d))
        f.close()
        print(i)
    else:
        while d[0]!='{':
            url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
            data='id={}&type=2&city=54&state=1'.format(i).encode()
            req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
            d=r.urlopen(req).read().decode('utf-8','ignore')
        f=open('./ting2.txt','a')
        f.write('{}\n'.format(d))
        f.close()
        
        
q=open('./xxx.txt','w')
for i in range(len(ls)):
    q.write(ls[i]+'\n')
q.close()

########

f=open('C:/Users/Administrator/Desktop/1212/广东理科.txt','r',encoding='utf-8')
p=f.read()
import json
p=json.loads(p)

##########
import urllib.request as r#导入联网工具包，命令为r
url='file///C:/Users/Administrator/Desktop/1212/广东理科.txt'
data=r.urlopen(url).read().decode('utf-8')
########
    #import re
    #k=re.compile('plan:"(.*?)"',re.S).findall(d))
#######
#g=open('./111.txt','w')
#ls=[]
#import urllib.request as r
#for i in ls1:
#    url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
#    data='id={}&type=2&city=44&state=1'.format(i).encode()
#    req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
#    d=r.urlopen(req).read().decode('utf-8','ignore')
#    ls.append(d)
#    g.write('{}\n'.format(d))
#    print('{}ok'.format(i))
#g.close()
#
#for i in ls1:
#    h=ls[i]
#    if h.startswith('<!DOCTYPE html>'):
#        print('第{}存在错误'.format(i))
#        url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
#        data='id={}&type=2&city=44&state=1'.format(i)
#        data=data.encode()
#        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
#        d1=r.urlopen(req).read().decode('utf-8','ignore')
#        ls[i]=d1
#g=open('./xxx.txt','w',encoding='utf-8')
#for i in range(2300):
#    k=ls[i]
#    q.write(k+'\n')
#g.close()
########### 
#g=open('./111.txt','w')
#for i in ls1:
#    try:
#        url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
#        data='id={}&type=2&city=44&state=1'.format(i).encode()
#        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
#        d=r.urlopen(req).read().decode('utf-8','ignore')
#        g.write(d,'\n')


###########
#f=open('C:/Users/Administrator/Desktop/1212/ee.csv','a')
#for j in range(100):
#    import urllib.request as r#导入联网工具包，命令为r
#    url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
#    data=r.urlopen(url).read().decode('utf-8')
#    #讲str类型转换为dict
#    import json
#    data=json.loads(data)
    
    
    
    








import urllib.request as r
url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
data=r.urlopen(req).read().decode('utf-8','ignore')
import re


#w=open('./school.txt','w',encoding='utf-8')
for i in ls1:
    try:
        import urllib.request as r
        url='http://www.gaokaopai.com/university-ajaxGetMajor.html'
        data='id={}&type=2&city=44&state=1'.format(i).encode()
        req=r.Request(url,data=data,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.146 Safari/537.36','X-Requested-With':'XMLHttpRequest'})
        d=r.urlopen(req).read().decode('utf-8','ignore')
        import json
        d=json.loads(d)
        for j in range(len(d['data'])):
            aa=d['data'][j]['school']
            bb=d['data'][j]['profess']
            cc=d['data'][j]['plan']
            ee=d['data'][j]['city']
            print("招生地区:{},学校:{}:专业:{},招生人数:{}\n".format(ee,aa,bb,cc))
            #f.write("招生地区:{},学校:{}:专业:{},招生人数:{}\n".format(ee,aa,bb,cc))
    except Exception as err:
        print('该学校不在此地招生')
#f.close()



w=0
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
        t=int(ls9[e]['data'][j]['plan'])
        w=w+t
print("总招生人数为{}".format(w))













