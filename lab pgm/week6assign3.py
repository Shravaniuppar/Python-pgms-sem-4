# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:38:14 2024

@author: cseweb
"""

s1=input("Enter a line of text:\n").split( )
d={}
for i in s1:
   d.update({i[0]:i}) 
print(d)