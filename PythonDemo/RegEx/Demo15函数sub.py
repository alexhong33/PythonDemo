'''
Created on 2017年6月6日

@author: Alex
'''

'''

re.sub(pattern, repl, string, count=0, flags=0)
Return the string obtained by replacing the leftmost non-overlapping occurrences of 
pattern in string by the replacement repl. 
If the pattern isn’t found, string is returned unchanged

pattern 正则
repl 替换的内容
string 目标string
count 替换的次数  0位全部替换

'''

import re

string = "hellomypythonhispythonourpythonend"

pattern = "python."

#全部替换
result1 = re.sub(pattern, "php", string)

#最多替换两次
result2 = re.sub(pattern, "php", string, 2)

print(result1)
print(result2)
