'''
Created on 2017年6月6日

@author: Alex

换行符


'''

import re
pattern = "\n"
string = '''http://yum.iqianyue.com
    http://baidu.com'''
result1 = re.search(pattern, string)

#  <_sre.SRE_Match object; span=(23, 24), match='\n'>
print(result1)
