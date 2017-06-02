'''
Created on 2017年6月2日

@author: Alex

Q: for 循环和while循环有什么区别？

for 循环只能对某种事物的集合做循环，而while可以进行任何种类的循环。
但是，while循环很容易出错，大部分情况for循环也是一个很好的选择。
'''

i = 0
numbers = []

while i<6:
    print("At the top i is %d" % i)
    numbers.append(i)
    
 
    i = i + 1
    print("Numbers now: ", numbers)
    print("At the bottom i is %d" % i)
    
print("The numbers: ")

for num in numbers:
    print(num)
    
print(numbers)
    
    
