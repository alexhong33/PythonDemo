# -*- coding: utf-8 -*-
# @Time        : 2017/7/3 11:32
# @Author      : Hong
# @Contact     : alexhongf@163.com
# @File        : Demo01List.py
# @Description : STOP wishing START doing. 



list1 = ["Alice", "Tom", "Mike", "John"]
print(list1)


# 增删改查

# 添加元素
list1.append("Alex")
print(list1)

list1.insert(2, "Fizz")
print(list1)

print(list1[0:])
del list1[1]
print(list1)

list1[1] = 'Tom'
print(list1)

list1.reverse()
print(list1)

list1.sort()
print(list1)

list1 = list1 * 2
print (list1)

for i in list1:
    print (i)

print(list1.count('Alex'))
