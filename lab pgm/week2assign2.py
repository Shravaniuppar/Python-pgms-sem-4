# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 09:35:38 2024

@author: cseweb
"""
import math
print("Enter x and y centre coordinates of a circle")
x1=int(input())
y1=int(input())
rad=int(input("Enter radius of the circle:"))
print("Enter x2 and y2 coordinates to check where they lie with respect to the circle")
x2=int(input())
y2=int(input())
d=math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
print(d)
if d==rad:
    print(f'Points ({x2},{y2}) lies on the circle')
elif d>rad:
    print(f'Points ({x2},{y2}) lies outside the circle')
elif d<rad:
    print(f'Points ({x2},{y2}) lies inside the circle')