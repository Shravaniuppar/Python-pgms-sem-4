# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 09:45:27 2024

@author: cseweb
"""

sm=0
i=100
while i<=200:
    if i!=104:
        sm=sm+i
    i=i+2
print("Sum of all even numbers between 100 and 200 without 104 is ",sm)
sm=0
i=100
while i<=200:
   # if i!=104:
    sm=sm+i
    i=i+2
print("Sum of all even numbers between 100 and 200 with 104 is ",sm)
