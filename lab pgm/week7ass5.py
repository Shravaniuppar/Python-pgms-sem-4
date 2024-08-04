# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:49:28 2024

@author: cseweb
"""

import re
s=input("enter a voter id number:")
k=r"[ A-Z]{3}[0-9]{7}"
v=re.findall(k,s)
if v:
    print("valid")
else:
    print("invalid")