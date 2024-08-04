# -*- coding: utf-8 -*-
"""
Created on Tue May 28 10:43:02 2024

@author: cseweb
"""

t=int(input('enter the temperature value:'))
type=input('enter the temperature type=>c for celcius, f for farhenheit:')
if type=='c':
    f=t*(9/5)+32
    print('temperature is converted from celcius to farhenheit and temperature in farhenheit is',f)
if type=='f':
    cel=(t-32)*5/9
    print('temperature is converted from farhenheit to celcius and temperature in celcius is',cel)