# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:09:14 2024

@author: cseweb
"""

n=int(input('enter a number check whether it is prime or not:'))
if n==1:
    print('1 is not a prime number')
for i in range(2,n//2+1):
    if n%i==0:
        print(n,'is not a prime number')
        break
else:
    print(n,'is  a prime number')