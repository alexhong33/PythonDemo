'''
Created on 2017年5月22日

@author: Alex

总结:
本节 学习使用Python 格式化字符
常用 %d 十进制整数, %f浮点, %s 字符串, %r 字符串(用于debug) (使用%r会有单引号)
'''


'''
%s    字符串 (采用str()的显示)

%r    字符串 (采用repr()的显示)

%c    单个字符

%b    二进制整数

%d    十进制整数

%i    十进制整数

%o    八进制整数

%x    十六进制整数

%e    指数 (基底写为e)

%E    指数 (基底写为E)

%f    浮点数

%F    浮点数，与上相同

%g    指数(e)或浮点数 (根据显示长度)

%G    指数(E)或浮点数 (根据显示长度)
          
'''

my_name = 'Zed A. Shaw'
my_age = 25 # not a lie
my_height = 171 # cm
my_weight = 140 # kg
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'

print("Let's talk about %s." %my_name)
print("He's %d cm tall." %my_height)
print("He's %d kg heavy." %my_weight)
print("Actually that's not too heavy.")
print("He's got %s eyes and %s hair." %(my_eyes, my_hair))
print("His teeth are usually %s depending on the coffee." %my_teeth)


# this line is tricky, try to get it exactly right
print("If I add %d, %d, and %d I get %d." %(
    my_age, my_height, my_weight, my_age+my_height+my_weight))
