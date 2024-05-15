# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 12:34:39 2022

@author: neil_
"""
i = 20

j = 150.45

str1 = "AkiSoft"

var1,var2 = 300, 300

var3, var4, var5 =1, 2, "AkiSoft"

print(i, j, str1, var1, var2, var3, var4, var5)

strs = "This is my second Python program!"

stradd = "And I love it!"

print(strs)

print(strs[0])

print(strs[2:6])

print(strs[2:])

print(strs * 2)

w = strs.partition("my")

print(w)

print(strs+"TEST")

print(strs.join(stradd))

for x in range(10):
    print("number: "+str(x))
    
def printMul(x,y):
    print(x*y)
    
    
    

printMul(4,5)