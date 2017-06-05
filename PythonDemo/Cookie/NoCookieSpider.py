'''
Created on 2017年6月5日

@author: Alexhong

无Cookie处理的登录
'''

import urllib.request
import urllib.parse

url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LDFKE"
postdata = urllib.parse.urlencode({"username":"alexhong33", "password":"Shenzhen2017"}).encode('utf-8')
#构建request对象
req = urllib.request.Request(url, postdata)
req.add_header('User-Agent',  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2669.400 QQBrowser/9.6.10990.400")
#登录并爬取页面
data = urllib.request.urlopen(req).read()
fhandle = open("D:/PythonWebSpider/NoCookie/1.html","wb")
#将内容写入对应data
fhandle.write(data)
fhandle.close()
#设置要爬取的该网站下其他网页地址
url2 = "http://bbs.chinaunix.net/"
req2 = urllib.request.Request(url2, postdata)
req2.add_header('User-Agent',  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2669.400 QQBrowser/9.6.10990.400")
#爬取该站下的其他网页
data2 = urllib.request.urlopen(req2).read()
fhandle = open("D:/PythonWebSpider/NoCookie/2.html","wb")
fhandle.write(data2)
fhandle.close()












