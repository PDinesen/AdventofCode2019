# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 08:23:31 2019

@author: Mitfo
"""
import ACH as AC


input31 = AC.readInputCommaLine("input31.txt")
input32 = AC.readInputCommaLine("input32.txt")
"""

def MakePathPoints(listname):
    temp = [[0,0]]
    for i in listname:
        if i[0] == 'R':
            temp.append([temp[-1][0]+int(i[1:]),temp[-1][1]])
        elif i[0] == 'L':
            temp.append([temp[-1][0]-int(i[1:]),temp[-1][1]])
        elif i[0] == 'U':
            temp.append([temp[-1][0],temp[-1][1]+int(i[1:])])
        elif i[0] == 'D':
            temp.append([temp[-1][0],temp[-1][1]-int(i[1:])])
        else:
            print('R, L, U or D wasn"t recognized')
    return temp

def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C

def intersection(L1, L2):
    D  = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x,y
    else:
        return False

Path1 = MakePathPoints(input31)
Path2 = MakePathPoints(input32)

def checkIntersection(listname1,listname2):
    tpath1 = MakePathPoints(listname1)
    tpath2 = MakePathPoints(listname2)
    Intersectiondist = 10000
    for i in range(len(tpath1)-1):
        L1 = line(tpath1[i],tpath1[i+1])
        for j in range(len(tpath2)-1):
            L2 = line(tpath2[j],tpath2[j+1])
            R = intersection(L1,L2)
            if R and R != (0,0):
                if abs(R[0]) + abs(R[1]) < Intersectiondist:
                    Intersectiondist = abs(R[0]) + abs(R[1])
    return Intersectiondist

tlist1=['R10','U10']
tlist2=['U5','R20']

print(checkIntersection(input31,input32))
"""            
def MakePathPoints2(listname):
    tlist = set()
    temp = [0,0]
    for i in listname:
        if i[0] == 'R':
            for j in range(int(i[1:])):
                temp = [temp[0]+1,temp[1]]
                tlist.add((temp[0],temp[1]))
        elif i[0] == 'L':
            for j in range(int(i[1:])):
                temp = [temp[0]-1,temp[1]]
                tlist.add((temp[0],temp[1]))
        elif i[0] == 'U':
            for j in range(int(i[1:])):
                temp = [temp[0],temp[1]+1]
                tlist.add((temp[0],temp[1]))
        elif i[0] == 'D':
            for j in range(int(i[1:])):
                temp = [temp[0],temp[1]-1]
                tlist.add((temp[0],temp[1]))
        else:
            print('R, L, U or D wasn"t recognized')
        
    return tlist


def CheckInter2(listname1,listname2):
    tpath1 = MakePathPoints2(listname1)
    tpath2 = MakePathPoints2(listname2)
    Interdist = 10000
    temp = tpath1.intersection(tpath2)
    for i in temp:
        if abs(i[0]) + abs(i[1]) < Interdist:
            Interdist = abs(i[0]) + abs(i[1])
    return Interdist

print(CheckInter2(input31,input32))

def loweststeps(listname1,listname2):
    tlist = MakePathPoints2(listname1).intersection(MakePathPoints2(listname2))
    steps = 100000
    temp1 = (0,0)
    sums1 = 0
    for i in listname1:
        r1,l1,u1,d1 = 0,0,0,0
        if i[0] == 'R':
            r1 = 1
        elif i[0] == 'L':
            l1 = 1
        elif i[0] == 'U':
            u1 = 1
        elif i[0] == 'D':
            d1 = 1
        else:
            print('R, L, U or D wasn"t recognized')
        for j in range(int(i[1:])):
            temp1 = (temp1[0]+r1-l1,temp1[1]+u1-d1)
            sums1 += 1
            if temp1 in tlist:
                temp2 = (0,0)
                sums2 = 0
                for k in listname2:
                    r2,l2,u2,d2 = 0,0,0,0
                    if k[0] == 'R':
                        r2 = 1
                    elif k[0] == 'L':
                        l2 = 1
                    elif k[0] == 'U':
                        u2 = 1
                    elif k[0] == 'D':
                        d2 = 1
                    else:
                        print('R, L, U or D wasn"t recognized')
                    for l in range(int(k[1:])):
                        temp2 = (temp2[0]+r2-l2,temp2[1]+u2-d2)
                        sums2 += 1
                        if temp1 == temp2:
                            if sums1 + sums2 < steps:
                                steps = sums1 + sums2
                            break
    return steps
        
print(loweststeps(input31,input32))
                                
            
