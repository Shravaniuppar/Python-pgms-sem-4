# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 17:11:30 2024

@author: cseweb
"""
def perfect_check(n):
    sum=0
    #flag=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    if sum==n:
        return True
    return False
n=int(input("Enter a number:\n"))
if perfect_check(n):
    print("perfect number")
else:
    print("not a perfect number")