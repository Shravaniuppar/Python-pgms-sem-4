# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 16:40:53 2024

@author: cseweb
"""

def find_pow(n,p):
    if p==0:
        return 1
    if p==1:
        return n
    return find_pow(n,p-1)**find_pow(n,p-2)
n=int(input("enter base value:\n"))
p=int(input("Enter power value;\n"))
print(f"{n} power {p}=",find_pow(n,p+1))