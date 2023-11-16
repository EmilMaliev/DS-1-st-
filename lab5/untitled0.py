# -*- coding: utf-8 -*-
"""
Created on Wed Dec 14 17:45:57 2022

@author: Professional
"""

import numpy as np
from numpy.polynomial import Polynomial
from scipy import integrate

x = np.zeros(6)
y = np.zeros(7)
for i in range(6):
    y[i + 1] = 1
    x[i] = Polynomial([y])
    y = np.zeros(7)

m = np.zeros(6)

f = Polynomial([0, 0, 0, 0, 0, 0, 0, 1])

for i in range(6):
    (m[i], err) = integrate.quad(f * x[i], 0, 1)

print(m)
