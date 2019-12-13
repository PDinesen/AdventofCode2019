# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 20:26:32 2019

@author: Mitfo
"""
import copy


test = [[[-1,0,2],[0,0,0]],[[2,-10,-7],[0,0,0]],[[4,-8,8],[0,0,0]],[[3,5,-1],[0,0,0]]]

st = [[[-9,-1,-1],[0,0,0]],
      [[2,9,5],[0,0,0]],
      [[10,18,-12],[0,0,0]],
      [[-6,15,-7],[0,0,0]]]

#print(test)

def NewVel(myDict):
    for i in range(len(myDict)-1):
        for k in myDict[i+1:len(myDict)]:
            for j in range(len(myDict[0][0])):
                if myDict[i][0][j] < k[0][j]:
                    myDict[i][1][j] += 1
                    k[1][j] -= 1
                elif myDict[i][0][j] > k[0][j]:
                    myDict[i][1][j] -= 1
                    k[1][j] += 1
    return myDict

#print(NewVel(test))
#print(NewVel(test))

 
def NewPos(myDict):
    for name in myDict:
        for i in range(len(name[0])):
            name[0][i] += name[1][i]

    return myDict  

#print(NewPos(test))            
                
    

def CalEnergy(TheDict):
    pot = 0
    Kin = 0
    Total = 0
    for name in TheDict:
        for k in range(len(name[0])):
            pot += abs(name[0][k])
            Kin += abs(name[1][k])
        Total += pot * Kin
        pot = 0
        Kin = 0
    return Total

#print(CalEnergy(test))

    
def RunProgram(TheDict,steps):
    myDict = copy.deepcopy(TheDict)
    for i in range(steps):
        NewPos(NewVel(myDict))
        
    print(TheDict)
    return CalEnergy(myDict)

#print(RunProgram(test,10))

#print(RunProgram(test2,100))

#print(RunProgram(st,1000))


def SamePos(TheDict):
    myDict = copy.deepcopy(TheDict)
    positions = [TheDict]
    i = 0
    while True:
        NewPos(NewVel(myDict))
        i += 1
        if not myDict in positions:
            positions.append(copy.deepcopy(myDict))
        else:
            return i
    
#print(SamePos(test))
#print(SamePos(test2))

def Search1state(TheDict):
    myDict = copy.deepcopy(TheDict)
    i = 0
    while True:
        a = NewPos(NewVel(myDict))
        i += 1
        if myDict == TheDict:
            return i
        if i%1000000 == 0:
            print(i)
print(Search1state(st))
