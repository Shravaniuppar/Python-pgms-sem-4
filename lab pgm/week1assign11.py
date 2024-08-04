# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:21:39 2024

@author: cseweb
"""

n=int(input('enter n value;'))
m=int(input('enter m value;'))
print('prime numbers from',n,'to',m)
for j in range(n,m+1):
    for i in range(2,j//2+1):
        if j%i==0:
           #print(n,'is not a prime number')
           break
    else:
        #if j!=4:
            print(j)
        