# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 17:59:47 2022

@author: Professional
"""

import matplotlib.pyplot as plt
import numpy as np


t = np.arange(0, 1, 0.01)

y = np.sin(t**2) + np.power(1 - t * np.cos(t), 1/4)
z = (np.log(t + 1))/np.sqrt(1 + t**2)
w = z - y

plt.plot(t, y, color='g', label='y', marker='.', linestyle='--')
plt.plot(t, z, color='r', label='z', marker='o', linestyle='-')
plt.plot(t, w, color='y', label='w', marker='+', linestyle='')

plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Three graphs")

plt.legend()

plt.show()