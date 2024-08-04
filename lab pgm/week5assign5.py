# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 15:57:30 2024

@author: cseweb
"""

l1=[]
n=int(input("Enter the count of binary digits:"))
print(f"enter {n} binary elements:")
for i in range(n):
    l1.append(int(input()))
l1=tuple(l1)
print("binary value")
for i in l1:
    print(i,end='')
s=0
for i in range(0,len(l1)):
    if l1[i]==1:
        s=s+2**(n-i-1)
print("\ndecimel value:")
print(s)