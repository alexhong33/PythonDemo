'''
Created on 2017年6月6日

@author: Alex
'''

import re
pattern = "\n"
string = '''http://yum.iqianyue.com
    http://baidu.com'''
result1 = re.search(pattern, string)
print(result1)