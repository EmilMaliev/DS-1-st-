# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 18:42:14 2022

@author: Professional
"""

txt = input('Text = ')
d = dict()
sym = set(txt)
for e in sym:
    d[e] = txt.count(e)
print('Словарь: ', d)