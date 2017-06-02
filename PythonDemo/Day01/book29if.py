'''
Created on 2017年6月2日

@author: Alex

IF 语句的规则：
1.每一个“if 语句”必须包含一个 else.

2.如果这个else永远都不应该被执行到，因为它本身没有任何意义，
那你必须在else语句后面使用一个叫做die的函数，让它打印出错误信息,这和上一节的习题类似，
这样你可以找到很多的错误。

3.“if 语句”的嵌套不要超过 2 层，最好尽量保持只有 1 层。

4.将“if 语句”当做段落来对待，其中的每一个if-elif-else 组合就跟一个段落的句子一样。
在这种组合的最前面和最后面留一个空行以作区分。

5.你的布尔测试应该很简单，如果它们很复杂的话，你需要将它们的运算事先放到一个 变量里，并且为变量取一个好名字。
'''

people=20
cats=30
dogs=15

if people<cats:
    print("Too many cats! The world is doomed!")
    
if people>cats:
    print("Not many cats! The world is saved!")

if people<dogs:
    print("The world is drooled on!")
    
if people>dogs:
    print("The world is dry!")
    
    
dogs+=5

if people>=dogs:
    print("People are greater than or equal to dogs")

if people<=dogs:
    print("People are less than or equal to dogs")
    
if people==dogs:
    print("People are dogs.")
    
