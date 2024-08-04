# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:14:57 2024

@author: cseweb
"""
a=[]
for i in range(3):
    b=[]
    for j in range(4):
        c=[]
        for k in range(6):
            c.append('*')
        b.append(c)
    a.append(b)
'''for i in range(3):
    print(a[i])
    print('\n')'''
for i in a:
    print(i)
    print('\n')