'''
Created on 2017年6月6日

@author: Alex

选择python 或者 php 任意一个模式匹配
'''


import re
pattern = "python|php"
string = "abcdfphp345pyth2ony_py"
result1 = re.search(pattern, string)
print(result1)