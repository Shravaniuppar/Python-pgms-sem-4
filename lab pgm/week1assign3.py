# -*- coding: utf-8 -*-
"""
Created on Tue May 28 09:27:26 2024

@author: cseweb
"""

a=int(input('enter 1st number:'))
b=int(input('enter 2nd number:'))
c=int(input('enter 3rd number:'))
if a>b:
    if a>c:
        print('largest number is',a)
    elif c>b:
        print('largest number is',c)
else:
    if b>c:
        print('largest number is',b)
    else:
        print('largest number is',c)