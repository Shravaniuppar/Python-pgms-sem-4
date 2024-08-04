# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:08:35 2024

@author: cseweb
"""

d1={}
d2={}
d3={}
d={}
n1=int(input("enter the number of values in dictionary 1:\n"))
for i in range(n1):
    d1.update({int(input("Enter key :")):int(input("Enter value:"))})
n2=int(input("enter the number of values in dictionary 2:\n"))
for i in range(n2):
    d2.update({int(input("Enter key :")):int(input("Enter value:"))})
n3=int(input("enter the number of values in dictionary 3:\n"))
for i in range(n3):
    d3.update({int(input("Enter key :")):int(input("Enter value:"))})
'''k1=d1.keys()
k2=d2.keys()
k3=d3.keys()
k=d.keys()
for i in k1:
    if i not in k:
        d.update({i:d1[i]})
for i in k2:
    if i not in k:
        d.update({i:d2[i]})
for i in k3:
    if i not in k:
        d.update({i:d3[i]})'''
for k in d1:
    d[k]=d1[k]
for k in d2:
    d[k]=d2[k]
for k in d3:
    d[k]=d3[k]
print(d)
        