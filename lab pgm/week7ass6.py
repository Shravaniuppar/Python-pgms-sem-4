# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:59:16 2024

@author: cseweb
"""


import re
s=input("enter a password:")
if(len(s)>=6 and len(s)<8):
    uc=re.search(r'[A-Z]+',s)
    lc=re.search(r'[a-z]+',s)
    d=re.search(r'[0-9]+',s)
    sc=re.search(r'[#@$]+',s)
    if uc and lc and d and sc:
        print("valid")
    else:
        print("invalid")
else:
    print("invalid")
