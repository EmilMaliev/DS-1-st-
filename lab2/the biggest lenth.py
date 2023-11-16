# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 19:36:43 2022

@author: Professional
"""
from random import randint

a = []
check = set(a)
for i in range(randint(1, 20)):
    a.append(randint(0, 1))
if len(check) == 1 and 0 in check:
    print('Only zeros')
else:
    res = [0, 0]
    prev = [0, 0]
    print(*a)
    i = 0
    while i < len(a):
        if a[i] == 1:
            res[0] = i
            while i + 1 != len(a) and a[i + 1] != 0:
                i += 1
            
            res[1] = i
        if res[1] - res[0] >= prev[1] - prev[0]:
            prev = res.copy()    
        i += 1    
    print(*prev)