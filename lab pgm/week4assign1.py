# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 14:35:08 2024

@author: cseweb
"""
l=[]
flag=0
for i in range(1000,3001):
    m=str(i)
    for j in range(len(m)):
        if int(m[j])%2!=0:
            flag=1
            #print('t')
            break
    if flag==1:
        pass
    else:
        l.append(m)
print(l)
'''
for i in range(1000,3001):
    k=i
    for j in range(4):
        m=i%10
        i=i/10
        if m%2!=0:
            flag=1
    if flag==1:
        l.append(k)
print(l)'''