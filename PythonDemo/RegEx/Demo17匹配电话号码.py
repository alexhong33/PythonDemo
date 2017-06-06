'''
Created on 2017年6月6日

@author: Alex
'''

import re

'''
思路

电话号码 
区号4位-数字7位
或者
区号3位-数字8位


"-"固定位置  左侧4位 整数 右侧7位整数

'''

#匹配电话号码的正则表达式
pattern = "\d{4}-\d{7}|\d{3}-\d{8}"
string = "021-6728263653682382265236"
result = re.search(pattern, string)
print(result)