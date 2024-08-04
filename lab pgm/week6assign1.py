# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:00:30 2024

@author: cseweb
"""

n=int(input("Enter the n value:\n"))
l=[]
print(f"Enter {n} values:\n")
for i in range(n):
    l.append(int(input()))
dict1={}
for i in l:
    if i not in dict1:
        dict1.update({i:l.count(i)})
print(dict1)
