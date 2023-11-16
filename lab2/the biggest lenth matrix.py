# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 21:53:25 2022

@author: Professional
"""

from random import randint
import numpy as np
a = []
b =[]
for i in range(randint(1, 30)):
    a.append(randint(0, 100))
res = [0, 0]
prev = [0, 0]
print(*a)
A = np.zeros((max(a),max(a)))
i = 0
while i < len(a):
    if i + 1 < len(a) and a[i] < a[i + 1]:
        res[0] = i
        while i + 1 != len(a) and a[i] < a[i + 1]:
            i += 1
        
        res[1] = i
        A[res[0]][res[1]] = res[1] - res[0]
    if res[1] - res[0] >= prev[1] - prev[0]:
        prev = res.copy()
    i += 1
print('A= ', A)
lenth = prev[1] - prev[0]
print('Lenth= ', lenth + 1)
if lenth != 0:
    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j] == lenth:
                for i in range(i,j + 1,1):
                    b.append(a[i])
                print(b)
                b = []
                b
elif lenth == 0:
    for i in range(0, len(a), 1):
        print(a[i])