'''
Created on 2017年5月22日

@author: Alex
'''

'''
Q:%r 和 %s有什么不同?

用%r显示的是变量“原始”的数据值，%r在打印的时候能够重现它代表的对象，但其他的符号用来给用户显示变量值。看下面的例子理解一下：
> text = "I am %d years old." % 22 > > print "I said: %s." % text > > print "I said: %r." % text
返回的结果：
> I said: I am 22 years old.. > > I said: 'I am 22 years old.'. // %r 给字符串加了单引号

'''

x = "There are %d types of people." %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)

print(x)
print(y)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print(joke_evaluation % hilarious)

w = "This is the left side of..."
e = "a string with a right side."

print(w+e)
