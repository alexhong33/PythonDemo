'''
Created on 2017年6月6日

@author: Alex
'''

import re


string = "hellomypythonhispythonourpythonend"

'''

#预编译
pattern = re.compile(".python.")
#找出符合模式的所有结果
result = pattern.findall(string)

'''

pattern = ".python."

result = re.compile(pattern).findall(string)

print(result)