'''
Created on 2017年5月23日

@author: Alex

学习目标:


'''

from sys import argv

#在命令行中 输入
script, input_file = argv

def print_all(f):
    print(f.read())
    
def rewind(f):
    f.seek(0)
    
def print_a_line(line_count, f):
    print(line_count, f.readline())
    
current_file = open(input_file)
   
