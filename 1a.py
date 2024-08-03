# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 13:49:20 2024

@author: Administrator
"""
from math import *
print("Enter a,b and c value of quadratic equation:")
a=int(input())
b=int(input())
c=int(input())
d=pow(b,2)-4*a*c
if d==0:
    r=(-b)/(2*a)
    print(f"Roots are {r} and {r}")
elif d>0:
    r1=(-b+sqrt(d))/(2*a)
    r2=(-b-sqrt(d))/(2*a)
    print(f"Roots are {r1} and {r2}")
elif d<0:
    rp=-b/(2*a)
    ip=sqrt(-d)/(2*a)
    print("Roots are",rp,"+i",ip,"and",rp,"-i",ip,)
  