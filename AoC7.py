# -*- coding: utf-8 -*-
"""
Created on Mon Dec  9 12:50:13 2019

@author: Mitfo
"""
import AoCHelper as AC
import AoC5
from itertools import permutations

def runDay7Program(input1, input2):
    programDefinition = AC.readInputCommaLine("input7.txt")

    return AoC5.runProgram(programDefinition, input1, input2)


combinations = permutations([0, 1, 2, 3, 4])

maxThrust = 0

for c in combinations:
    outputA = runDay7Program(c[0], 0)
    outputB = runDay7Program(c[1], outputA)
    outputC = runDay7Program(c[2], outputB)
    outputD = runDay7Program(c[3], outputC)
    outputE = runDay7Program(c[4], outputD)

    if outputE > maxThrust:
        maxThrust = outputE

print(maxThrust)