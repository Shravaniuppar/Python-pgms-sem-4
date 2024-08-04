# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 14:53:47 2024

@author: cseweb
"""

s=input("Enter a string:")
ch=int(input("Enter your choice:\n1 for left or anticlockwise rotation of string\n2 for right or clockwise rotation of string"))
d=int(input("Enter the no of elements to be shifted:"))
if ch==1:
    s1=s[-d::1]+s[:len(s)-d:]
    print(s[-d::1])
    print(s1)
elif ch==2:
    s1=s[d::]+s[:d:]
    print(s[d::1])
    print(s1)
else:
    print("invalid choice")
    