'''
Created on 2017年6月6日

@author: Alex
45pythony
'''

import re
pattern = "\w\dpython\w"
string = "abcdfphp345pythony_py"
result1 = re.search(pattern, string)
print(result1)
#输出匹配的字符串
print(result1.group())