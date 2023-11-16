# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 14:29:21 2022

@author: Professional
"""

import numpy as np
from numpy import linalg as LA

A = np.array([[8,0,0,0,0,0,0], 
               [6,8,0,0,0,0,0],
               [5,5,5,5,5,5,5],
               [0,0,4,8,0,0,0],
               [0,0,0,3,8,0,0],
               [0,0,0,0,2,8,0],
               [0,0,0,0,0,1,8]])

def eigenvalues(A):
    if LA.det(A):
        w, v = LA.eig(A)
    else:
        print('Матрица линейно зависима')
    min_ = abs(w[0])
    for i in range(0, 7, 1):
        if abs(w[i]) < abs(min_):
            min_ = w[i]
            ind = i
    v = np.transpose(v)
    a = A.dot(v[ind])
    b = np.multiply(min_, v[ind])
    print('Мин по модулю собственное значение = ', min_)
    print('Соответсвующий ему собственный вектор = ', v[ind] )
    if a.all() == b.all():
        print('Равенство Ах = lx сработало')
    return w, v
print(eigenvalues(A))