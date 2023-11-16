# -*- coding: utf-8 -*-
"""
Created on Wed Nov 23 17:35:27 2022

@author: Professional
"""

import matplotlib.pyplot as plt
import numpy as np


N = int(input('N = '))
M = int(input('M = '))
T = int(input('T = '))
E = np.zeros((M+1,N+1))
H = np.zeros((M+1,N+1))
z = np.zeros(N+1)
t = np.zeros(M+1)
h = 200/N
tau = T/M

for i in range(N+1):
    z[i] = i*h

for j in range(M+1):
    t[j] = j*tau

for i in range(N+1):
    E[0][i] = 0.1 * np.sin(2 * np.pi * z[i] * 0.01)
    H[0][i] = 0.1 * np.sin(2 * np.pi * z[i] * 0.01)
    
for j in range(M):
    for i in range(N+1):
        E[(j + 1) % N, (i - 1/2) % N] = E[j, (i - 1/2) % N] - (tau * (H[(j - 1/2) % N, i] - H[j + 1/2, (i - 1) % N]) / h)
    for i in range(N+1):
        H[j + 1/2, i] = H[j - 1/2 , i] - (tau * (E[j, (i + 1/2) % N] - E[j, (i - 1) % N]) / (2*h))