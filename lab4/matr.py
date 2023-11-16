# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 11:29:13 2022

@author: Professional
"""

import numpy as np




N = int(input('Demension of matrix = ')) 


def create_Matr(N):
    A = np.zeros((N,N))
    
    np.fill_diagonal(A, 8)
    j = 0
    k = 6
    for i in range(1, 7):
        A[i, j] = k
        j += 1
        k -= 1
    if N > 1:
        for i in range(N):
            A[2, i] = 5
    if N > 7:
        for i in range(6, N):
            A[i, 7] = 0
    print("A:\n", A)
    
    O = np.zeros((N,N))
    E = np.eye(N)
    Exp = np.exp(A)
    res_matr = np.vstack((A, O))
    tmp = np.vstack((E, Exp))
    return np.hstack((res_matr, tmp))

res = create_Matr(N)
np.savetxt('test.txt', res)


