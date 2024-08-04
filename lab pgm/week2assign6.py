# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:02:04 2024

@author: cseweb
"""
n=int(input("enter n value for the series"))
sum=0
for i in range(1,n+1):
    sum+=(1/i)
print(f"sum of series 1+1/2+....1/{n} is {sum}")
sum=0
for i in range(1,n+1):
    sum+=((i**i)/i)
print(f"sum of series 1+2^2/2+3^3/3....{n}^{n}/{n} is {sum}")