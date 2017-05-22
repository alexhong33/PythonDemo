'''
Created on 2017年5月22日

@author: Alex

使用input()方法 输入信息

注意%r 和 %s的区别
'''


name = input('please enter your name: ')
print('hello,',name)

print("How old are you?")
age = input()
print("How tall are you?")
height = input()
print("How much do you weight?")
weight = input()

#So, you're '25yrs old' old, '171cm' tall and '70kg' heavy.
print("So, you're %r old, %r tall and %r heavy." %(age, height, weight))
#So, you're 25yrs old old, 171cm tall and 70kg heavy.
print("So, you're %s old, %s tall and %s heavy." %(age, height, weight))
