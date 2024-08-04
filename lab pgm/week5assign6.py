# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 15:49:16 2024

@author: cseweb
"""

l1=[]
n1=int(input("Enter the size of list:"))
print(f"enter {n1} elements:")
for i in range(n1):
    l1.append(int(input()))
l1=tuple(l1)
l2=[]
n2=int(input("Enter the size of list:"))
print(f"enter {n2} elements:")
for i in range(n2):
    l2.append(int(input()))
l2=tuple(l2)
res=[]
if n1==n2:
    for i in range(n1):
        res.append(l1[i]&l2[i])
restuple=tuple(res)
print(restuple)