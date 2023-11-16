# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 11:28:46 2022

@author: Professional
"""

num = int(input('Число= '))
a =[]
num_copy = num
count = 0
while num_copy > 0:
    a.append(int(num_copy % 10))
    num_copy = int(num_copy/10)
    count += 1
left_sum = 0
right_sum = 0
for i in range(0,int(count/2)):
    right_sum += a[i]
if count % 2 == 1:
    for i in range(int(count/2) + 1,int(count)):
        left_sum += a[i]
else:
    for i in range(int(count/2),int(count)):
        left_sum += a[i]
if right_sum > left_sum:
    print('right')
elif left_sum > right_sum:
    print('left')
else:
    print('Balanced')
    
    
