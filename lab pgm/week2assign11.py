# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 11:12:37 2024

@author: cseweb
"""

n=int(input("Enter a number to check whether it is a buzz number or not:"))
m=str(n)
if m[-1]=='7' or n%7==0:
    print(n,'is a buzz word')
else:
    print(n,'is not a buzz word')