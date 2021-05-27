# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 16:51:23 2019

@author: Mitfo
"""

import AoCHelper as AC


st = AC.readInputLines("input10.txt")
#print(st)

def gcd(a,b):
    a,b = abs(a),abs(b)
    if a == 0:
        return b
    else:
        return gcd(b%a,a)

    
print(gcd(0,0))

def removeDiv(a,b):
    c = gcd(a,b)
    while c != 1:
        a,b = int(a/c), int(b/c)
        c = gcd(a,b)
    return a,b


def Angel(point1,point2):
    a = point2[0] - point1[0]
    b = point2[1] - point1[1]
    return removeDiv(a,b)

st1 = ['...###...','..#..#..#']


def myCode(iname):
    res = 0
    
    for i in range(len(iname)):
        for j in range(len(iname[0])):
            if iname[i][j] == '#':
                temp = {(0,0)}
                for k in range(len(iname)):
                    for l in range(len(iname[0])):
                        if i == k and j == l:
                            continue
                        if iname[k][l] == '#':
                            temp.add(removeDiv(k-i,l-j))
                temp.remove((0,0))
                if len(temp) > res:
                    res = len(temp)
                    x,y = i,j
                    temp1 = temp
    print(res,x,y)
    return temp1,x,y

for i in myCode(st)[0]:
    print(i[0])
    break


def splittheres(setofvec):
    res1 = []
    res2 = []
    res3 = []
    res4 = []
    for i in setofvec:
        if i[0] >= 0 and i[1] < 0:
            res1.append([i[0],i[1]])
        elif i[0] > 0 and i[1] >= 0:
            res2.append([i[0],i[1]])
        elif i[0] <= 0 and i[1] > 0:
            res3.append([i[0],i[1]])
        elif i[0] < 0 and i[1] <= 0:
            res4.append([i[0],i[1]])
    print(len(res1),len(res2),len(res3),len(res4))
    return [res1,res2,res3,res4]


te = []
for i in splittheres(myCode(st)[0])[3]:
    te.append(i[1]/i[0])
    
print(te.index(min(te)))
    
def myCode2(iname,num):
    temp,x,y = myCode(iname)
    temp1 = splittheres(temp)
    left = num
    
    left -= len(temp1[0]) + len(temp1[1]) + len(temp1[2])
    while 0 < left:
        te =[]
        for j in temp1[3]:
            te.append(j[1]/j[0])
        res = temp1[3][te.index(min(te))]
        del temp1[3][te.index(min(te))]
        left -= 1
      
    print(res)
    return res

myCode2(st,200)
print(31-13,25-9)
print(st[31-13][25-9])
        
    

       