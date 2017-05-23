'''
Created on 2017年5月23日

@author: Alex

学习目标:


'''
from sys import argv
from os.path import exists


script, from_file, to_file = argv 

out_file = open(to_file, 'w').write(open(from_file).read())

