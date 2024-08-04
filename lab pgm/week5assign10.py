# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:55:43 2024

@author: cseweb
"""

l=[]
n=int(input("Enter the no of list elements:"))
print(f"enter {n} elements:")
for i in range(n):
    x=int(input())
    l.append(x)
l1=set(l)
l1=list(l1)
pr=1
for i in range(len(l1)):
    pr*=l1[i]
print(f"Product of all the unique elements in the list is {pr}")