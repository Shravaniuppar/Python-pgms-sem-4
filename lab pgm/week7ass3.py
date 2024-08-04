# -*- coding: utf-8 -*-
"""
Created on Tue Jul 16 15:18:33 2024

@author: cseweb
"""
f=open("file2.txt","r")
f1=open("file3.txt","r")
f2=open("combine.txt","w")
l=[]
l1=[]
for i in f:
    a=i.rstrip()
    l.append(a)
print(l)
for j in f1:
     a=j.rstrip()
     l1.append(a)    
print(l1)
if len(l)>len(l1):
    n=len(l1)
else:
    n=len(l)
for k in range(n):
    c=l[k]+' '+l1[k]+'\n'
    print(c)
    f2.write(c)
f.close()
f1.close()  
f2.close()  