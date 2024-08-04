# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:02:33 2024

@author: cseweb
"""

n=int(input("enter the size of the list:"))
l=[]
m=int(input("enter the size of each tuple within the list:"))
for i in range(n):
    p=[]
    print("enter the elements of tuple",i+1)
    for j in range(m):
        p.append(int(input()))
    l.append(tuple(p,))
sl=[]
for i in range(n):
    s=0
    for j in range(m):
        s=s+l[i][j]
    sl.append(s)
print(sl)