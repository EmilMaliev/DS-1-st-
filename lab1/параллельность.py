# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a1 = input('a1= ')
b1 = input('b1= ')
c1 = input('c1= ')
a2 = input('a2= ')
b2 = input('b2= ')
c2 = input('c2= ')
if float(a1) > 0 and float(b1) > 0 and float(a2) > 0 and float(b2) > 0:
    if float(a1)/float(a2) == float(b1)/float(b2) and float(b1)/float(b2) != float(c1)/float(c2):
        print('Паралельны')
elif float(a1) == 0 and float(a2) == 0:
    float(b1)/float(b2) and float(b1)/float(b2) != float(c1)/float(c2)
elif float(b1) == 0 and float(b2) == 0:
    float(a1)/float(a2) != float(c1)/float(c2)
else:
    print('Не параллельны')