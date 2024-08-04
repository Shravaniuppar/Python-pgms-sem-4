# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:09:57 2024

@author: cseweb
"""

n=int(input("enter the size of the list:"))
l=[]
#m=int(input("enter the size of each tuple within the list:"))
for i in range(n):
    p=[]
    print("enter the name, age and score of tuple",i+1)
    for j in range(3):
        p.append(input())
    l.append(tuple(p,))
l1=sorted(l)
print(l1)