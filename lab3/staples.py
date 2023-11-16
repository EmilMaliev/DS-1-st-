# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 17:56:46 2022

@author: Professional
"""

a = input('String = ')
d = ' '
b = a.find('(')
c = a.find(')')
if b < c:
    for i in range(b + 1, c, 1):
        d = d + a[i]
    print(d)
elif b > c:
    for i in range(c + 1, b, 1):
        d = d + a[i]
    print(d)
    
