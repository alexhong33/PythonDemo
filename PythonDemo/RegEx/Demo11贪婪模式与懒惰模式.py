'''
Created on 2017年6月6日

@author: Alex
'''

import re


#贪婪模式 核心 尽可能多地匹配
# match='php345pythony_py'

# 在p 之后最远的的一个y
pattern1 = "p.*y" 


#懒惰模式 可信 尽可能少地匹配
# 输出  match='php345py' 

# 在p 之后 最近的一个y
pattern2 = "p.*?y"

string = "abcdfphp345pythony_py"

result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)

print(result1)
print(result2)

