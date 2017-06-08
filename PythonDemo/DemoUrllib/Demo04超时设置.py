'''
Created on 2017年6月8日

@author: Alex
'''

import urllib.request


for i in range(1, 200):
    try:
        file = urllib.request.urlopen("http://military.china.com/", timeout=1)
        data = file.read()
        print(len(data))
    except Exception as e:
        print("出现异常-->" + str(e))
