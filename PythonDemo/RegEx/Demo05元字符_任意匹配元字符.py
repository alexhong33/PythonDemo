'''
Created on 2017年6月6日

@author: Alex

匹配字符串前面1位,后面3位的字符, 这前1后3可以是除了换行符以外的任意字符
'''

import re
pattern = ".python..."
string = "abcdfphp345 pythony_py"
result1 = re.search(pattern, string)
print(result1)


