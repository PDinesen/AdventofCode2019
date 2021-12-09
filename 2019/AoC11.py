# -*- coding: utf-8 -*-
"""
Created on Wed Dec 11 09:33:18 2019

@author: Mitfo
"""

import AoCHelper as AC
import AoC9

st = AC.readInputCommaLine("input11.txt")

def Robot(inputname, input):
    a , temp = AoC9.runProgram(inputname,input)
    #print(AoC9.runProgram(temp,a,a))
    R = [0,0,0]
    reslist = [R[0:2],'.']
    if R[0:2] in reslist:
        if reslist[reslist.index(R[0:2])+1] == '.':
            c = 0
        elif reslist[reslist.index(R[0:2])+1] == '#':
            c = 1
    for i in range(10):
        a , temp = AoC9.runProgram(temp,c)
        
        if a == '0':
            R[2] = (R[2] + 1) % 4
        elif a == '1':
            R[2] = (R[2] - 1) % 4
        if R[2] == 0:
            R[1] += 1
        elif R[2] == 1:
            R[0] -= 1
        elif R[2] == 2:
            R[1] -= 1
        elif R[2] == 3:
            R[0] += 1
        if [R[0],R[1]] in reslist:
            c = 1
        else:
            reslist.append([R[0],R[1]])
        a , temp = AoC9.runProgram(temp,c)
        print(R)
    print(len(reslist))
    return reslist

Robot(st,0)

a , temp = AoC9.runProgram(st,0)
print(type(a))