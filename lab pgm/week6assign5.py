# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:43:26 2024

@author: cseweb
"""

def mirror_char(n,og_st,alphabets):
    #newst=og_st[n]
    m=og_st[:n:]
    n1=og_st[n:]
    n2=''
    for i in range(len(n1)):
        k=25
        for j in range(len(alphabets)):
            if n1[i]==alphabets[j]:
                n=alphabets[j+k]
                n2=n2+n
                break
            k=k-2
    return m+n2
n=int(input("Enter the position:\n"))
s1=input('enter a word:\n')
alpha='abcdefghijklmnopqrstuvwxyz'
m=mirror_char(n-1,s1,alpha)
print("Mirrored word: ",m)