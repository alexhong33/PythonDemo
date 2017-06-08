'''
Created on 2017年6月8日

@author: Alex
'''

import urllib.request

file = urllib.request.urlopen("http://www.autohome.com.cn/beijing/?pvareaid=102550")

data = file.read()
dataline = file.readline()

print(data)