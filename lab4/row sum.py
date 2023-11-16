# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 12:45:04 2022

@author: Professional
"""
import numpy as np
import time as tm

N = int(input('кол-во итераций = '))

def func1(z, N):
    start = tm.time()
    res = 0
    for i in range(0, N + 1, 1):
        res += (np.sin(z) * np.sin(i*z))/ np.sqrt(i + z**2)
    print('Время первой функции', tm.time() - start)
    return res
def func2(z, N):
    start = tm.time()
    rng = np.arange(0, N + 1, 1)
    res = sum(map(lambda i :(np.sin(z) * np.sin(i*z))/ np.sqrt(i + z**2) , rng))
    print('Время второй функции:', tm.time() - start)
    return res
z = int(input('z = '))
print(func1(z, N))
print(func2(z, N))