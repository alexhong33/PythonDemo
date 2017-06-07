'''
Created on 2017年6月7日

@author: Alex
'''

import urllib.request
import http.cookiejar

url = "http://www.163.com/"

headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Accept-Language": "zh-CN,zh;q=0.8",
           "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2669.400 QQBrowser/9.6.10990.400",
           "Connection": "keep-alive"}


#设置cookie
cjar = http.cookiejar.CookieJar()
proxy = urllib.request.ProxyHandler({'http':'127.0.0.1:8888'})
opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler,
                                     urllib.request.HTTPCookieProcessor(cjar))


#建立空列表, 为了以指定格式存储头信息
headall = []
#通过for循环遍历字典, 构造出指定格式的headers信息
for key,value in headers.items():
    item = (key,value)
    headall.append(item)
    
#将指定格式的headers信息添加好
opener.addheaders = headall

#将opener安装为全局
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read()
fhandle = open("F:/PythonWrite/h1.html", "wb")
fhandle.write(data)
fhandle.close()

