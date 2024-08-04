# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:07:31 2024

@author: cseweb
"""

f=open("file1.txt","r")
u=0
l=0
for i in f:
    for j in range(len(i)):
        if i[j].isupper():
            u+=1
        if i[j].islower():
            l+=1
print("upper case letters:",u)
print("lower case letters:",l)    