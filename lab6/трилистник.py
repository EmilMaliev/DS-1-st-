# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 18:12:28 2022

@author: Professional
"""

import matplotlib.pyplot as plt
import numpy as np


t = np.linspace(0, 2 * np.pi, 10000)

x = np.sin(3*t) * np.cos(t)
y = np.sin(3*t) * np.sin(t)

fig = plt.figure()
# получение осей
ax = fig.gca()
ax.plot(x, y, label='Трилистник ')
# добавление сетки
ax.grid(True, color = 'red')
#Легенда - это помощник, позволяющий определить что соответствует определенному цвету линии 
ax.legend()

plt.xlabel("X")
plt.ylabel("Y")
plt.show()