# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:54:53 2024

@author: cseweb
"""

n=int(input('enter the size of queue:'))
l=[]
ch=int(input('enter your choice:\n1-insertion\n2-deletion\n3-display\n4-count'))
if ch==1:
    l.append(int(input('enter element:')))
elif ch==2:
    k=l.pop(0)
    print("popped element:",k)
elif ch==3:
    print(l)
elif ch==4:
    print("queue count=",len(n))
else:
    print("Invalid choice")
