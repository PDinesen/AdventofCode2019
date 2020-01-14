# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 20:26:32 2019

@author: Mitfo
"""
import copy
import time

test = [[[-1,0,2],[0,0,0]],[[2,-10,-7],[0,0,0]],[[4,-8,8],[0,0,0]],[[3,5,-1],[0,0,0]]]

def lcm(x, y):
   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y
   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
   return lcm

print(lcm(-1,lcm(2,lcm(4,3))))
print(lcm(0,lcm(-10,lcm(-8,5))))
print(lcm(-1,lcm(2,lcm(4,3))))


st = [[[-9,-1,-1],[0,0,0]],
      [[2,9,5],[0,0,0]],
      [[10,18,-12],[0,0,0]],
      [[-6,15,-7],[0,0,0]]]

'''
st2 = [((-9,-1,-1),(0,0,0)),
       ((2,9,5),(0,0,0)),
       ((10,18,-12),(0,0,0)),
       ((-6,15,-7),(0,0,0))]
'''
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
    start_time = time.time()

    myDict = copy.deepcopy(TheDict)
    i = 0
    while True:
        NewPos(NewVel(myDict))
        i += 1
        if myDict == TheDict:
            return i
        if i%10000000 == 0:
            print("--- %s seconds ---" % (time.time() - start_time))
            print(i)
            start_time = time.time()

print(Search1state(st))
'''
start_time = time.time()

st3 = copy.deepcopy(st)
steps = 0
while True:
    for i in range(0,3):
        for k in range(i+1,4):
            for j in range(3):
                if st3[i][0][j] < st3[k][0][j]:
                    st3[i][1][j] += 1
                    st3[k][1][j] -= 1
                elif st3[i][0][j] > st3[k][0][j]:
                    st3[i][1][j] -= 1
                    st3[k][1][j] += 1
        for j in range(3):
            st3[i][0][j] += st3[i][1][j]
    for j in range(3):
        st3[-1][0][j] += st3[-1][1][j]
    steps += 1
    if st3 == st:
        print(steps)
        break
    elif steps%1000000 == 0:
        print("--- %s seconds ---" % (time.time() - start_time))
        print(steps)
        start_time = time.time()
        
'''
        








