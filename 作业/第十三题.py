# -*- coding: utf-8 -*-
"""
Created on Tue Jun 26 16:29:37 2018

题目十三：糗事百科数据爬取
1.爬取作者和内容
2.爬取13页
3.下载图片。想做就做


@author: Administrator
"""
import urllib.request as r#导入URL工具包 并且命令为r
for i in range(1,14):
    req=r.Request('https://www.qiushibaike.com/8hr/page/{}/'.format(i),headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'})
    myurl=r.urlopen(req)
    #print(myurl.getcode())
    data=myurl.read().decode('utf-8')
    import re
    ls3=re.compile('alt="(.*?)"',re.S).findall(data)
    ls4=re.compile('<span>\n\n\n(.*?)\n</span>',re.S).findall(data)
    for j in range(len(ls4)):
        print("作者:{}\n内容:{}".format(ls3[j],ls4[j]))
    

import urllib.request as r#导入URL工具包 并且命令为r
#for i in range(1,14):
req=r.Request('http://www.qiushibaike.com/8hr/page/2/',headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.98 Safari/537.36'})
myurl=r.urlopen(req)
print(myurl.getcode())
data=myurl.read().decode('utf-8')
import re
ls1=re.compile('alt="(.*?)"></a>').findall(data)
ls2=re.compile('<div class="content"><span>(.*?)</span></div>',re.S).findall(data)
for j in range(len(ls1)):
    print("作者:{},内容:{}".format(ls1[j],ls2[j]))
    
    
    
    
url='https://pic.qiushibaike.com/system/pictures/11292/112920206/medium/app112920206.jpg'
r.urlretrieve(url,'./tmp.jpg')#retrieve下载文件
