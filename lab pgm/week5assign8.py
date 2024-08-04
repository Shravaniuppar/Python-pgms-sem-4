# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 15:08:05 2024

@author: cseweb
"""
l=[]
n=int(input('enter the size of the list:'))
n1=int(input("enter the size of sublist:"))
print(f"enter {n*n1} elements:")
for i in range(n):
    print("enter the elements of sublist",i)
    c=[]
    for j in range(n1):
        c.append(int(input()))
    l.append(c)
print(l)
nl=[]
for a in l:
    m=[]
    for i in range(n1-1):
          s=[]
          s.append(a[i])
          s.append(a[n1-1])
          m.append(s)
    nl.append(m)
print(nl)