# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:14:53 2024

@author: cseweb
"""

'''n=int(input('enter n value;'))
maxmark=0
print('enter marks of %d students'%n)
for i in range(n):
    mark=int(input())
    if mark>maxmark:
        maxmark=mark
print('max marks is %d'%maxmark)'''

#n=int(input('enter n value;'))
l=[]
#print('enter marks of %d students'%n)
for i in range(int(input('enter n value;'))):
    #mark=int(input())
    l.append(int(input()))
print(max(l))