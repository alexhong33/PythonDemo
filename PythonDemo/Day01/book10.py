'''
Created on 2017年5月22日

@author: Alex

转义字符的应用 反斜杠 \
'''

print("I am 6'2\" tall.") #将字符串中的双引号转义
print('I am 6\'2" tall.') #将字符串中的单引号转义


tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\a \\cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)



#输出\ 反斜杠的时候 要用到转义字符 
b = 0
while b < 15:
    for i in ["/","-","|","\\","|"]:
        b = b +1
        print("%s\r" %i,)
        