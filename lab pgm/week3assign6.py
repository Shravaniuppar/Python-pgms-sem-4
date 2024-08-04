# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 16:23:55 2024

@author: cseweb
"""

s=input("enter colour names separated by commma:").split(',')
l=[]
for i in s:
    if i not in l:
        l.append(i)
#l=sorted(l)
l.sort()
print(l)
l1=','.join(l)
print(l1)