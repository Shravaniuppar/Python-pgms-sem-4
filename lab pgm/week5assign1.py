# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 17:24:46 2024

@author: cseweb
"""

l=[]
n=int(input("Enter the size of tuple:"))
n1=int(input("enter the size of subtuple:"))
print(f"enter {n*n1} elements:")
for i in range(n):
    print("enter the elements of subtuple",i)
    c=[]
    for j in range(n1):
        c.append(input())
    l.append(tuple(c))
print(l)

for i in range(n):
    l.sort(l[i][1])