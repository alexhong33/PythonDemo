'''
Created on 2017年6月8日

@author: Alex

处理异常主要有2个类
1> URLError类
2> HTTPError类

产生UrlError的情况
1) 连接不上服务器
2) 远程URL不存在
3) 无网络
4) 触发了HTTPError(如爬虫被禁止访问)
'''

#整合后代码

import urllib.request
import urllib.error


try:
    urllib.request.urlopen("http://blog.csdn.net")
except urllib.error.URLError as e:
    if hasattr(e, "code"):
        print(e.code)
    if hasattr(e, "reason"):
        print(e.reason)








