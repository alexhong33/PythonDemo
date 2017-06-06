'''
Created on 2017年6月6日

@author: Alex

re.I 匹配时忽略大小写
re.M 多行匹配
re.L 做本地化识别匹配
re.U 根据Unicode字符及解析字符
re.S 让.匹配包括换行符, 即用了该模式修正后, "."匹配就可以匹配任意的字符了

'''

import re
pattern1 = "python"
pattern2 = "python"
string = "abcdfphp345Pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string, re.I)
print(result1)
print(result2)
