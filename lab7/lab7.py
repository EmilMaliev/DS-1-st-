# -*- coding: utf-8 -*-
"""
Created on Wed Nov  9 15:13:15 2022

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
        E[j + 1, i] = E[j, i] - (tau * (H[j, i] - H[j, (i - 1) % N]) / h)
    for i in range(N+1):
        H[j + 1, i] = H[j , i] - (tau * (E[j, (i + 1) % N] - E[j, (i - 1) % N]) / (2*h))

print(E)
print(H)

t1 = int(input('t1 = '))
x = np.arange(0, (N + 1) * h, h)
y = H[t1]

plt.plot(x, y, color='y', marker='.', linestyle='-')
# Naming the x-axis, y-axis and the whole graph
plt.xlabel("Z")
plt.ylabel("H")
plt.title("H graph")

# Adding legend, which helps us recognize the curve according to it's color
plt.legend()

# To load the display window
plt.show()

y = E[t1]

plt.plot(x, y, color='b', marker='+', linestyle='-')
# Naming the x-axis, y-axis and the whole graph
plt.xlabel("Z")
plt.ylabel("E")
plt.title("E graph")

# Adding legend, which helps us recognize the curve according to it's color
plt.legend()

# To load the display window
plt.show()