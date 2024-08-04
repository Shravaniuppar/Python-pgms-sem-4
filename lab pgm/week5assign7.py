# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 15:26:47 2024

@author: cseweb
"""

l=[]
n=int(input("Enter the size of list:"))
print(f"enter {n} elements:")
for i in range(n):
    l.append(int(input()))
pos1=int(input("enter 1st position:"))
pos2=int(input("enter 2nd position:"))
print("old list")
print(l)
m=l[pos1-1]
l[pos1-1]=l[pos2-1]
l[pos2-1]=m
print("new list")
print(l)