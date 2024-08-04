# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:56:11 2024

@author: cseweb
"""

'''n=int(input("ENter a number to check nud of that number"))
flag=0
m=n
for i in range(len(str(n))):
    t=m%10
    if m%t!=0:
        flag=1
    m=m/10
if flag==0:
    print(n,'is not a nud number')
else:
    print(n,'is a nud number')'''
n=int(input("ENter a number to check nud of that number"))
m=str(n)
flag=0
for i in range(len(m)):
    if n%(int(m[i]))!=0:
        flag=1
if flag==1:
    print(n,'is not a nud number')
else:
    print(n,'is a nud number')