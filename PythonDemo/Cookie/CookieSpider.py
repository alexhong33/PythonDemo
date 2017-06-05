'''
Created on 2017年6月5日

@author: Alex
'''
import urllib.request
import urllib.parse
import http.cookiejar
from Cookie.NoCookieSpider import postdata

#爬取链接
url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LDFKE"
#提交登录账号密码
postdata = urllib.parse.urlencode({"username":"alexhong33", "password":"Shenzhen2017"}).encode('utf-8')
req = urllib.request.Request(url, postdata)
req.add_header('User-Agent',  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) \
    Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2669.400 QQBrowser/9.6.10990.400")


#使用http.cookiejar.CookiJar() 创建CookieJar对象
cjar = http.cookiejar.CookieJar()
#使用HTTPCookieProcessor创建cookie处理器, 并以其为参数构建opener对象
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
#将opener安装为全局
urllib.request.install_opener(opener)
file = opener.open(req)
data = file.read()
file = open("D:/PythonWebSpider/NoCookie/3.html","wb")
file.write(data)
file.close()
url2 = "http://bbs.chinaunix.net/"
data2 = urllib.request.urlopen(url2).read()
fhandle = open("D:/PythonWebSpider/NoCookie/4.html","wb")
fhandle.write(data2)
fhandle.close()