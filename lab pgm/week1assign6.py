# -*- coding: utf-8 -*-
"""
Created on Tue May 28 09:51:15 2024

@author: cseweb
"""
from math import *
p=int(input('enter principle amount:'))
t=int(input('enter time:'))
r=int(input('enter rate:'))
si=(p*t*r)/100
ci=p*pow(1+r/100,t)
print('simple interest=',si)
print('compound interest=',ci)