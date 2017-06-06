'''
Created on 2017年6月6日

@author: Alex
'''

import re
string = "apythonhellomypythonhispythonourpythonend"

pattern = ".python."

#用match 从起始位置匹配, 得到 apythonh
result = re.match(pattern, string)

'''
match.span([group])
For a match m, return the 2-tuple (m.start(group), m.end(group)). 
Note that if group did not contribute to the match, 
this is (-1, -1). group defaults to zero, the entire match.
'''
#返回截取字符串的数组(0,8)
result2 = re.match(pattern, string).span()
print(result)
print(result2)