# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import os
import numpy as np

a = os.getcwd()
## Advent exercise 0.0
print(a)

input1 = np.loadtxt(fname = "input1.txt")

print(input1)

sum1 = 0
for i in input1 :
    sum1 += int(i / 3) - 2
    
print(sum1)

## Advent exercise 0.1
sum2 = 0 
for i in input1 :
    mass = int(i/3)-2
    while mass > 0:
        print(mass)
        sum2 += mass
        mass = int(mass/3) -2 
    
        
print(sum2)
b=int(input1[-1]/3)-2
print(b)
print(int(37923/3)-2)