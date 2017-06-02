'''
Created on 2017年6月2日

@author: Alex

Q: 如何定义一个两层（2D）的列表？

就是一个列表在另一个列表里面，比如[[1,2,3],[4,5,6]]

Q: 列表和数组不是同一种东西吗？

依赖于语言和实现方式。在经典设计角度，由于数组列表的实现方式不同，数组列表是非常不同的。
在Ruby中程序员称之为数组。在Python中,他们称之为列表。因为现在是Python调用它们，所以我们就称呼它为列表。

Q: 为什么for i in range(1, 3):只循环了两次？

range()函数循环的次数不包括最后一个。所以range(1,3)只循环到2,这是这种循环最常用的方法。


Q: elements.append()实现什么功能？

它能实现在列表的末尾追加一个元素。打开Python解析器，自己写一个列表做些实验。
当你遇到这类问题的时候，都可以在Python的解析器中做些实验，自己找到问题的答案。
'''

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']


# this first kind of for-loop goes through a list
for number in the_count:
    print("This is count %d" % number)
    

# same as above
for fruit in fruits:
    print("A fruit of type: %s" % fruit)


# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it

for i in change:
    print("I got %r" % i)
    
# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print("Adding %d to the list." % i)
    # append is a function that lists understand
    elements.append(i)
    
    
# now we can print them out too
for i in elements:
    print("Element was: %d" % i)

