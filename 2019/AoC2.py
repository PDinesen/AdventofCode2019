# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 14:28:55 2019

@author: Mitfo
def readInputLines(fileName):
    return [line.rstrip('\n') for line in open("Inputs/" + fileName)]

def readInputCommaLine(fileName):
    lines = readInputLines(fileName)
    return lines[0].split(',')
"""
import os
import numpy as np
import AoCHelper as AC



in2 = AC.readInputCommaLine("input2.txt")



print(AC.strtoint(in2))

#print(input2)
#print(len(input2))
input2 = AC.strtoint(in2)
input2[1] = 12
input2[2] = 2
#input2 = [1,1,1,4,99,5,6,0,99]
def findoutput(listname):
    temp = listname.copy()
    for i in range(0,len(temp),4):
        if temp[i] == 1:
            temp[temp[i+3]] = temp[temp[i+1]] + temp[temp[i+2]]
        elif temp[i] == 2:
            temp[temp[i+3]] = temp[temp[i+1]] * temp[temp[i+2]]
        elif temp[i] == 99:
            break
        else:
            print("wrong input at")
            print(i)
            break
    return temp

print(findoutput(input2)[0])

for noun in range(1,99):
    for verb in range(1,99):
        input2[1] = noun
        input2[2] = verb
        ans = findoutput(input2)[0]
        if ans == 19690720:
            print(100*noun + verb)
            

