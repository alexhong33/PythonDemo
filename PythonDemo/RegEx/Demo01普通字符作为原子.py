'''
Created on 2017年6月6日

@author: Alex

re.search(pattern, string, flags=0)
Scan through string looking for the first location where 
the regular expression pattern produces a match, and return 
a corresponding match object. 

Return None if no position in the string matches the pattern; 
note that this is different from finding a zero-length match at
 some point in the string.
'''

import re
#普通字符作为原子
pattern = "yue"
string = "http://yum.iqianyue.com"
result1 = re.search(pattern, string)
print(result1)
print(result1.group())