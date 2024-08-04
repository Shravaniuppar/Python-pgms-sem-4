# -*- coding: utf-8 -*-
"""
Created on Tue May 28 11:18:48 2024

@author: cseweb
"""

d=int(input('enter the no of days:'))
y=d//365
m=d//30-y*12
remd=d-(y*365+m*30)
print('years=',y,'\nmonths=',m,'\nremaining days=',remd)
print(y,m,remd)