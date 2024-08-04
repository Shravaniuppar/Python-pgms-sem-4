# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 16:53:20 2024

@author: cseweb
"""

l1=[]
n=int(input('enter the row size of matrix 1:'))
n1=int(input("enter the column size of matrix 1:"))
print(f"enter {n*n1} elements:")
for i in range(n):
    print("enter the elements of sublist",i)
    c=[]
    for j in range(n1):
        c.append(int(input()))
    l1.append(c)
for i in l1:
    print(i)
print()
l2=[]
m=int(input('enter the row size of matrix 2:'))
m1=int(input("enter the column size of matrix 2:"))
print(f"enter {m*m1} elements:")
for i in range(m):
    print("enter the elements of sublist",i)
    c=[]
    for j in range(m1):
        c.append(int(input()))
    l2.append(c)
for i in l2:
    print(i)
print()
res=[]
for i in range(n):
    a=[]
    for j in range(m1):
        s=0
        for k in range(m1):
            s+=l1[i][k]*l2[k][j]
        a.append(s)
    res.append(a)
for i in res:
    print(i)