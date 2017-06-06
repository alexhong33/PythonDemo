'''
Created on 2017年6月6日

@author: Alex
'''

import re
string = "hellomypythonhispythonourpythonend"
pattern = ".python."

# 获得结果为None 源字符串string的开始位置不符合正则表达式格式
result = re.match(pattern, string)

# match='ypythonh'
result2 = re.search(pattern, string)

print(result)
print(result2)


