# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:11:59 2024

@author: cseweb
"""

s=input("Enter the main string:")
sub=input("Enter the sub string:")
if sub in s:
    print("Entered substring is already in main string")
    new=input("Enter new sub string to replace:")
    st=s.replace(sub,new)
    print("Main string with new substring",st)
else:
    print("Entered substring is not in main string")
    n=len(s)/2
    n=int(n)
   # p=s[:n:]
   # q=s[n::]
    s=s[:n:]+sub+s[n::]
    print(f"Main string with sub string is {s}")
    
    