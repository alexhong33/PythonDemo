'''
Created on 2017年5月23日

@author: Alex

输入 python book16.py test.txt

1.'r'是open(filename)的默认方式

2.它只是打开文件的一种模式。如果你用了这个参数，
表示"以写（write）模式打开文件。
同样有'r'表示只读模式，'a'表示追加模式，还有一些其他的修饰符。

3.
以写入的模式创建文件
target = open(filename, 'w')
清空文件
target.truncate()
'''


from sys import argv

script, filename = argv

print("We're going to erase %r." %filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
#清空文件
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()










