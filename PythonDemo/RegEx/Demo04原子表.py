'''
Created on 2017年6月6日

@author: Alex

在python中, 原子表由[]表示, 比如[xyz]就是一个原子表
这个原子表中定义了3个原子, 这3个额原子的地位平等, 
[xyz]py 对应 源字符串 xpython, 用re.search()匹配可以得出结果  xpy
'''

import re
pattern1 = "\w\dpython[xyz]\w"
#[^]表示除了中括号里面的原子均可以匹配
pattern2 = "\w\dpython[^xyz]\w"
#匹配除字母, 数字和下划线意外的任意一个其他字符
pattern3 = "\w\dpython[xyz]\W"

string = "abcdfphp345pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
result3 = re.search(pattern3, string)

print(result1)
print(result2)
print(result3)
