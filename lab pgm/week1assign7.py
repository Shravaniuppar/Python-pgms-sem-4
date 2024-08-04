# -*- coding: utf-8 -*-
"""
Created on Tue May 28 09:56:33 2024

@author: cseweb
"""

a=int(input('enter the a values of quadratic equation:'))
b=int(input('enter the b values of quadratic equation:'))
c=int(input('enter the c values of quadratic equation:'))
d=b*b-4*a*c
if d>=0:
    if d>0:
        r1=(-b+pow(d,1/2))/2*a
        r2=(-b-pow(d,1/2))/2*a
        print('roots are real and distinct')
        print('roots are',r1,'and',r2)
    else:
        r1=(-b+pow(d,1/2))/2*a
        print('roots are real and equal')
        print('roots are',r1,'and',r1)
else:
    print('roots are imaginary')
       