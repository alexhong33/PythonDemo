'''
Created on 2017年6月8日

@author: Alex
'''

import urllib.request
from Cookie.CookieSpider import fhandle

url = "http://www.guokr.com/"
req = urllib.request.Request(url)
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 \
    Safari/537.36 Core/1.53.2669.400 QQBrowser/9.6.10990.400')

data = urllib.request.urlopen(req).read()

fhandle = open("F:/PythonWrite/headers2.html", "wb")
fhandle.write(data)
fhandle.close