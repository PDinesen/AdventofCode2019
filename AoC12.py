# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 09:04:39 2019

@author: Mitfo
"""

import AoCHelper as AC
import copy

st = AC.readInputLines("input12.txt")

stDict = {'Oi':{'Pos':[-9,-1,-1],'Vel':[0,0,0]},
          'Europa':{'Pos':[2,9,5],'Vel':[0,0,0]},
          'Ganymede':{'Pos':[10,18,-12],'Vel':[0,0,0]},
          'Callisto':{'Pos':[-6,15,-7],'Vel':[0,0,0]}}

test = {'Oi':{'Pos':[-1,0,2],'Vel':[0,0,0]},
          'Europa':{'Pos':[2,-10,-7],'Vel':[0,0,0]},
          'Ganymede':{'Pos':[4,-8,8],'Vel':[0,0,0]},
          'Callisto':{'Pos':[3,5,-1],'Vel':[0,0,0]}}

test2 = {'Oi':{'Pos':[-8,-10,0],'Vel':[0,0,0]},
          'Europa':{'Pos':[5,5,10],'Vel':[0,0,0]},
          'Ganymede':{'Pos':[2,-7,3],'Vel':[0,0,0]},
          'Callisto':{'Pos':[9,-8,-3],'Vel':[0,0,0]}}


    

def NewVel(myDict):
    names = [i for i in myDict]
    for i in range(0,len(names)-1):
        for j in range(i+1,len(names)):
            for k in range(len(myDict[names[i]]['Pos'])):
                if myDict[names[i]]['Pos'][k] < myDict[names[j]]['Pos'][k]:
                    myDict[names[i]]['Vel'][k] += 1
                    myDict[names[j]]['Vel'][k] -= 1
                elif myDict[names[i]]['Pos'][k] > myDict[names[j]]['Pos'][k]:
                    myDict[names[i]]['Vel'][k] -= 1
                    myDict[names[j]]['Vel'][k] += 1
                    
    return myDict
 
def NewPos(myDict):
    for name in myDict:
        for i in range(len(myDict[name]['Pos'])):
            myDict[name]['Pos'][i] += myDict[name]['Vel'][i]

    return myDict              
                
    

def CalEnergy(TheDict):
    pot = 0
    Kin = 0
    Total = 0
    for name in TheDict:
        for k in range(len(TheDict[name]['Pos'])):
            pot += abs(TheDict[name]['Pos'][k])
            Kin += abs(TheDict[name]['Vel'][k])
        Total += pot * Kin
        pot = 0
        Kin = 0
    return Total

    
def RunProgram(TheDict,steps):
    myDict = copy.deepcopy(TheDict)
    for i in range(steps):
        NewPos(NewVel(myDict))
        
    return CalEnergy(myDict)

#print(RunProgram(test,10))

print(RunProgram(test2,100))

print(RunProgram(stDict,1000))


def SamePos(TheDict):
    myDict = copy.deepcopy(TheDict)
    positions = [myDict]
    i = 0
    while True:
        myDict = NewPos(NewVel(myDict))
        i += 1
        if not myDict in positions:
            positions.append(myDict)
        else:
            return i
    
#print(SamePos(test))
#print(SamePos(test2))

def Search1state(TheDict):
    myDict = copy.deepcopy(TheDict)
    i = 0
    while True:
        NewPos(NewVel(myDict))
        i += 1
        if myDict == TheDict:
            return i
        if i%1000000 == 0:
            print(i)
print(Search1state(stDict))

        
    
    