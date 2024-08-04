# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 09:26:07 2024

@author: cseweb
"""

print("Enter x1 and y1 coordinates;")
x1=int(input())
y1=int(input())
print("Enter x2 and y2 coordinates;")
x2=int(input())
y2=int(input())
print("Enter x3 and y3 coordinates;")
x3=int(input())
y3=int(input())
d=0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
if d==0:
    print("The entered coordinates are collinear")
else:
    print("The entered coordinates are not collinear")