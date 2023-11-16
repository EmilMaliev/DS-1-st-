# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 18:22:02 2022

@author: Professional
"""

import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0, np.pi, 0.1)
y = np.arange(0, np.pi, 0.1)

[x, y] = np.meshgrid(x, y)

#размещение осей на сетке
fig, ax = plt.subplots(1, 1)

z = x**2 * np.cos(y)**2 - 2 * y**2

ax.contour(x, y, z)

ax.set_title('Contour Plot')
ax.set_xlabel('x')
ax.set_ylabel('y')

plt.show()

ax = plt.axes(projection='3d')
ax.plot_surface(x, y, z)
ax.set_title('Surface Plot')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()
