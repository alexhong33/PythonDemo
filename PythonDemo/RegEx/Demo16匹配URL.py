'''
Created on 2017年6月5日

@author: Alex
'''

'''
将一串字符串里面以.com 或 .cn为域名后缀的URL网址匹配出来, 过滤掉其他的无关信息

'''
import re


'''
S1: "://" 是固定的 可以直接写出
S2: 结尾是.com或者.cn  使用 模式选择符  [.com|.cn]
S3: 在"://" 和  [.com|.cn] 之间不能出现空格  所以  [^\s]* 从开始的位置除了空格字符 以外的 

'''
pattern = "[a-zA-z]+://[^\s]*[.com|.cn]"
string = "<a href='https://www.baidu.com'>百度首页</a>"
result = re.search(pattern, string)
print(result)
print("="*20)
print(result.group())