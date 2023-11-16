# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 11:52:16 2022

@author: Professional
"""
import numpy as np

def func():
    C = np.loadtxt('matrix.txt', dtype = 'i', delimiter= ' ')
    return sum(map(lambda x : np.abs(x),filter(lambda x: -3 < x < 4, C[:, 0])))
print('Result = ', func())
