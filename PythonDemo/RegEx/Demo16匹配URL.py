'''
Created on 2017年6月5日

@author: Alex
'''

import re


pattern = "[a-zA-z]+://[^\s]*[.com|.cn]"
string = "<a href='https://www.baidu.com'>百度首页</a>"
result = re.search(pattern, string)
print(result)