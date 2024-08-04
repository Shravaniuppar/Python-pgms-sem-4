# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:35:03 2024

@author: cseweb
"""

def list2(list0,list1):
    for i in range(len(list0)):
        for j in range(len(list1)):
            if list0[i]==list1[j]:
                return True
l=[]
print("enter the elements of list 1:")
for i in range(5):
    l.append(int(input()))
m=[]
print("enter the elements of list 2:")
for j in range(5):
    m.append(int(input()))
if list2(l,m):
    print('common elements exist')
else:
    print('common elements does not exist')