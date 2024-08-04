# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:15:44 2024

@author: cseweb
"""

n=int(input('enter how many numbers:'))
print('enter',n,'numbers')
sumeven=0
sumodd=0
for i in range(n):
    x=int(input())
    if x%2==0:
        sumeven=sumeven+x
    else:
        sumodd=sumodd+x
print('odd sum =',sumodd,'\neven sum=',sumeven)