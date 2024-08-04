# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 16:32:54 2024

@author: cseweb
"""
def convertdictlist(d1):
    l=[]
    for j in d1:
        l1=[]
        l1.append(j)
        l1.append(d1[j])
        l.append(l1)
    return l
d1={}
n1=int(input("enter the number of elements in dictionary:\n"))
for i in range(n1):
    d1.update({int(input("Enter key :")):input("Enter value:")})
print(d1)
print(convertdictlist(d1))