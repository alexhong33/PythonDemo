'''
Created on 2017年5月23日

@author: Alex
输入 python book15.py book15_sample.txt

'''

from sys import argv

#从命令行中获取脚本名, 文件名
script, filename = argv
#打开文件
txt = open(filename)

print("Here's your file %r:" %filename)
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

txt.close()
txt_again.close()