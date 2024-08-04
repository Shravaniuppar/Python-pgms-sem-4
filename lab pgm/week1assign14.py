# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:06:33 2024

@author: cseweb
"""

m=int(input('enter the marks:'))
if m<=100 and m>=90:
    print('s grade')
if m<90 and m>=80:
    print('a grade')
if m<80 and m>=70:
    print('b grade')
if m<70 and m>=60:
    print('c grade')
if m<60 and m>=50:
    print('d grade')
else:
    print('f grade')