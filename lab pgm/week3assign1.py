# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 14:42:54 2024

@author: cseweb
"""

word=['zero','one','two','three','four','five','six','seven','eight','nine']
num=[0,1,2,3,4,5,6,7,8,9]
s=input("enter a numeric words string:").split(' ')
print(s)
for i in range(len(s)):
    for j in range(len(word)):
        if s[i]==word[j]:
            print(num[j],end=' ')
