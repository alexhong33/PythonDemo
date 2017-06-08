'''
Created on 2017年6月8日

@author: Alex
'''

import urllib.request


url = "http://www.guokr.com/"
headers = ("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2669.400 QQBrowser/9.6.10990.400")

#添加报头方式一
opener = urllib.request.build_opener()
opener.addheaders = [headers]
data = opener.open(url).read()


#写入文件
fhandle = open("F:/PythonWrite/headers1.html", "wb")
fhandle.write(data)
fhandle.close()




