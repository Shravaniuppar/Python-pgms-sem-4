# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:46:03 2024

@author: cseweb
"""

l=[]
n=int(input("enter the size of tuple"))
for i in range(n):
    print("Enter 4 values of tuple",i)
    m=[]
    for j in range(4):
        m.append(int(input()))
    l.append(tuple(m,))
print(l)
l=tuple(l)
s=[]
for i in range(4):
    sum=0
    for j in range(n):
        sum=sum+l[j][i]
    s.append(sum)
print(s)