'''
Created on 2017年6月2日

@author: Alex

不换行
print(x, end="")
'''

i = 1

while i <= 5:
    j = 1
    while j <= 5:
        print("*", end="")
        j+=1
    #换行
    print("")
    i+=1
