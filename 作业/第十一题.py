# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 10:47:00 2018


题目十一：爬取百度网页数据
1.爬取百度搜索标题
2.爬取标题下的描述
3.搜索的标题的网站

@author: Administrator
"""

import urllib.request as r#导入联网工具包，命令为r
url='http://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&ch=4&tn=56060048_4_pg&wd=study&oq=Python&rsv_pq=bb4229a60004f554&rsv_t=615cXymSpSdHNyBF54J7%2Fc1IShxA2J5zj9EJzZ06HW6kyvvHSRnlMIQBKy8eVSUqf6JutQ&rqlang=cn&rsv_enter=1&inputT=72761&rsv_sug3=27&rsv_sug1=25&rsv_sug7=101&bs=Python'
data=r.urlopen(url).read().decode('utf-8')
print(data)
import re
ls1=re.compile('"title":"(.*?)"').findall(data)
for i in range(len(ls1)):
    print("标题:{}".format(ls1[i]))
ls2=re.compile('<div class="c-abstract">(.*?)</div>',re.S).findall(data)
for i in range(len(ls2)):
    print("描述:{}".format(ls2[i]))
ls3=re.compile('style="text-decoration:none;">(.*?)&nbsp').findall(data)
for i in range(len(ls3)):
    print("网站:{}".format(ls3[i]))