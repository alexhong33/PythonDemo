'''
Created on 2017年6月6日

@author: Alex
'''


import re

pattern = "\w+([.+-]\w+)*@\w+([.-]\w+)*\.\w+([.-]\w+)*"

#string = "<a href='http://www.baidu.com'>百度首页</a><br><a href='mailto:c_e+o@iqi-anyue.com.cn>电子邮箱地址</a>"
string = "<a href='http://www.baidu.com'>百度首页</a><br><a href='alexhongf@163.com>电子邮箱地址</a>"
result = re.search(pattern, string)
print(result)

