# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 15:51:19 2024

@author: cseweb
"""

s=input("Enter a string:")
spf1=input("Enter the start char to be checked:")
spf2=input("Enter the end char to be checked:")
if s.startswith(spf1) and s.endswith(spf2):
    print('the entered string starts with',spf1,'and ends with',spf2)
else:
    print('the entered string do not starts with',spf1,'and ends with',spf2)
