# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 12:38:37 2022

@author: Professional
"""

x = float(input('X= '))
p = int(input('P= '))
y = float(input('Y= '))
count = 0
while x < y:
    x = x * ((100 + p)/100)
    x = int(x * 100)/100
    count += 1
print('Через ',count, ' лет')