# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:43:57 2024

@author: cseweb
"""

st=input("Enter a alphanumeric and spl cahracter string:")
ct1=0
ct2=0
ct3=0
for i in range(len(st)):
    if st[i].isdigit():
        ct1=ct1+1
    elif st[i].isalpha():
        ct2=ct2+1
    else:
        ct3=ct3+1
print('alphabet count:',ct1)
print('numbers count:',ct2)
print('spl character count:',ct3)
     