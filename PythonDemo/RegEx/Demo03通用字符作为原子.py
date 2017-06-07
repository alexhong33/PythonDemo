'''
Created on 2017年6月6日

@author: Alex
45pythony


/w 任意字母, 数字和下划线
/W 除了字母, 数字和下划线

/d 任意十进制数字
/D 除了十进制数字

/s 任意一个空白字符
/S 除了空白字符以外的任意其他字符
'''

import re


#输出 <_sre.SRE_Match object; span=(9, 18), match='45pythony'>
pattern = "\w\dpython\w"
string = "abcdfphp345pythony_py"
result1 = re.search(pattern, string)
print(result1)
#输出匹配的字符串
print(result1.group())