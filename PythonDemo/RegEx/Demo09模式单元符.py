'''
Created on 2017年6月6日

@author: Alex

使用单元符 () 可以把当做一个整体去使用
'''

import re
#(cd)出现1次以上
pattern1 = "(cd){1,}"
#d出现1次以上
pattern2 = "cd{1,}"
string = "abcdcdcdcdfphp345pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
print(result1)
print(result2)


