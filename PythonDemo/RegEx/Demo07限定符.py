'''
Created on 2017年6月6日

@author: Alex
'''

import re
#py与n之间可以是除换行符以外的任意字符,并且该任意字符可以出现0次, 1次或多次
#匹配结果为 python
pattern1 = "py.*n"

#要求cd字符串中 d 恰好出现2次 
#匹配结果为cdd
pattern2 = "cd{2}"

#要求cd字符串中 d 恰好出现3次
#匹配结果为 cddd
pattern3 = "cd{3}"


#要求cd字符串中 d 至少出现2次
#匹配结果为cddd
pattern4 = "cd{2,}"

string = "abcdddfphp345pythony_py"
result1 = re.search(pattern1, string)
result2 = re.search(pattern2, string)
result3 = re.search(pattern3, string)
result4 = re.search(pattern4, string)

print(result1)
print(result2)
print(result3)
print(result4)

