# -*- coding: utf-8 -*-
"""
Created on Tue May 28 09:38:15 2024

@author: cseweb
"""

x=int(input('enter x coordinates:'))
y=int(input('enter y coordinates:'))
if x==0 and y==0:
    print('point is at origin')
if x>0:
    if y>0:
        print('point is in 1st quadrant')
    if y<0:
        print('point is in 4th quadrant')
elif x==0 and y!=0:
    if y>0:
        print('point is on positive y axis')
    else:
        print('point is on negative y axis')
elif y==0 and x!=0:
    if x>0:
        print('point is on positive x axis')
    else:
        print('point is on negative x axis')
else:
    if y>0:
        print('point is in 2nd quadrant')
    if y<0:
        print('point is in 3rd quadrant')
    