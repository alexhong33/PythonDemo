'''
Created on 2017年5月23日

@author: Alex

1.确认你弄懂了三个引号 """ 可以定义多行字符串，而 % 是字符串的格式化工具。
2.定义了prompt变量

'''

from sys import argv

script, user_name = argv
prompt = '> '

print("Hi %s, I'm the %s script." %(user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me %s?" %user_name)
likes = input(prompt)

print("Where do you live %s?" %user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""

Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.

""" %(likes, lives, computer))