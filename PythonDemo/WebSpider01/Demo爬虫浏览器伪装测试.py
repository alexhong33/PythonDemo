'''
Created on 2017年6月7日

@author: Alex
'''

import urllib.request
import http.cookiejar

url = "http://www.ifeng.com/?from=newtab"
cjar = http.cookiejar.CookieJar()
proxy = urllib.request.ProxyHandler({'http':'127.0.0.1:8888'})
opener = urllib.request.build_opener(proxy, urllib.request.HTTPHandler, \
                                      urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
data = urllib.request.urlopen(url).read()
fhandle = open("F:/PythonWrite/5.html", "wb")
fhandle.write(data)
fhandle.close()


