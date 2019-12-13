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

    return AoC5.runProgram(programDefinition, input1, input2)[0]


combinations = permutations([0,1,2,3,4])

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

st = AC.readInputCommaLine("input7.txt")

combinations = permutations([5, 6, 7, 8, 9])

maxThrust = 0

st = ['3','26','1001','26','-4','26','3','27','1002','27','2','27','1','27','26','27','4','27','1001','28','-1','28','1005','28','6','99','0','0','5']

for c in combinations:
    outputE = 0
    prg = st
    for i in range(10):
        outputA, prg = AoC5.runProgram(prg,c[0],outputE)
        outputB, prg = AoC5.runProgram(prg,c[0],outputA)
        outputC, prg = AoC5.runProgram(prg,c[0],outputB)
        outputD, prg = AoC5.runProgram(prg,c[0],outputC)
        outputE, prg = AoC5.runProgram(prg,c[0],outputD)
        if outputE == 99:
            break
    if outputE > maxThrust:
        maxThrust = outputE
    
print(maxThrust)






