'''
Created on 2017年5月22日

@author: Alex

在控制台输入 python book13.py first 2nd 3rd
'''

from sys import argv

script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

'''
python book13.py first 2nd 3rd
The script is called: book13.py
Your first variable is: first
Your second variable is: 2nd
Your third variable is: 3rd
'''