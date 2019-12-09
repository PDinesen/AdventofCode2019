# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 11:53:31 2019

@author: Mitfo
"""
start = 108457
slut = 562041

def CheckCritiria(input):
    temp = str(input)
    Increasing = True
    Double = False
    for i in range(len(temp)-1):
        if temp[i] > temp[i+1]:
            Increasing = False
        elif temp[i] == temp[i+1]:
            Double = True
    if Increasing and Double:
        return True
    else:
        return False
    
sums = 0
for i in range(start,slut+1):
    if CheckCritiria(i):
        sums += 1
        
print(sums)

def CheckCritiria2(input):
    temp = str(input)
    Increasing = True
    Double = False
    for i in range(len(temp)-1):
        if temp[i] > temp[i+1]:
            Increasing = False
    if Increasing:
        for i in temp:
            if temp.count(i) == 2:
                Double = True
    if Increasing and Double:
        return True
    else:
        return False
    
sums = 0
for i in range(start,slut+1):
    if CheckCritiria2(i):
        sums += 1   


print(sums)
        