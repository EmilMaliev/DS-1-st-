# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 17:37:56 2022

@author: Professional
"""

import numpy as np


def func(C, b = None):
    if b == None:
        b = np.random.normal(-1, 2, np.shape(C)[0])
    print('C = ', C)
    print('b = ', b)
    if np.linalg.det(С) == 0:
        print("The matrix is singular")
    x = np.linalg.solve(С, b)
    return x, np.linalg.norm(x, ord = 1)


С = np.array([[5, -1], [2, 3]])
print(func(С))