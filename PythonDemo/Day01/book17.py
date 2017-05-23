'''
Created on 2017年5月23日

@author: Alex

学习目标:

现在让我们再学习几种文件操作。
我们将编写一个Python脚本，
将一个文件中的内容拷贝到另外一个文件中

'''

from sys import argv
from os.path import exists

#用户输入 脚本名, 输入文件名, 输出文件名.
script, from_file, to_file = argv

print("Copying from %s to %s" %(from_file, to_file))

#we could do these two on one line, how?
#打开目标文件
in_file = open(from_file)
#读取目标文件
indata = in_file.read()


print("The input file is %d bytes long" %len(indata))


print("Does the output file exist? %r" %exists(to_file))
print("Ready, hit RETURN to continue, CTRL-C to abort.")
input()
#写入目标文件
out_file = open(to_file, 'w')
#向目标文件输入文字
out_file.write(indata)


print("Alright, all done")
#关闭文件
out_file.close()
#关闭文件
in_file.close()





