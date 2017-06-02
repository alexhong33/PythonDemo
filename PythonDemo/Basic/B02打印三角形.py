'''
Created on 2017年6月2日

@author: Alex
'''

i = 1

while i <= 5:
    j = 1
    while j <= i:
        print("*", end="")
        j+=1
    #换行
    print("")
    i+=1
