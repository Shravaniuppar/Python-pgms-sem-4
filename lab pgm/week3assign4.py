# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:10:23 2024

@author: cseweb
"""

s=input("Enter a string:")
l=''
for i in s:
    if i not in l:
        l=l+i
print(l)
        