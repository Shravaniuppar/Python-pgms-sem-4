# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 15:01:57 2024

@author: cseweb
"""

l=[]
n=int(input("enter the no of elements:"))
print(f"enter {n} elements:")
for i in range(n):
    l.append(int(input()))
k=int(input("Enter the frequency value:"))
ct=[]
for i in range(n):
    if l.count(l[i])>k:
        if l[i] not in ct:
            ct.append(l[i])
print(ct)