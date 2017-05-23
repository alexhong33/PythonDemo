'''
Created on 2017年5月23日

@author: Alex

学习目标:

1.定义一个函数
2.函数括号中可以进行运算
3.定义变量

'''
#定义函数方法和变量
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print("You have %d cheeses!" %cheese_count)
    print("You have %d boxes of crackers!" %boxes_of_crackers)
    print("Man that's enough for a party!")
    print("Get a blanket. \n")
    

print("We can just give the function numbers directly: ")
cheese_and_crackers(20, 30)


print("OR, we can use variables from our script: ")
amount_of_cheese = 10
amount_of_crackers = 50

#向函数中添加参数
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print("We can even do math inside too: ")
#在括号中进行运算
cheese_and_crackers(10+20, 5+6)

print("And we can combine the two, variables and math: ")
#输出cheese总量并加100, crackers总量加1000
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)










