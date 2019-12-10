# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 10:19:05 2019

@author: Mitfo
"""

import AoCHelper as AC

st = AC.readInputLines("input8.txt")


def splitlen(listname,ant):
    temp = []
    leng = int(len(listname[0])/ant)
    for i in range(leng):
        temp.append(listname[0][ant * i: ant * (i + 1)])
        
    return temp


def check0andcal(inputname,numInLay):
    temp = splitlen(inputname,numInLay)
    test = len(temp[0])
    #print(temp)
    for i in temp:
        sum0 = 0
        sum1 = 0
        sum2 = 0
        for j in i:
            if j == '0':
                sum0 += 1
            elif j == '1':
                sum1 += 1
            elif j == '2':
                sum2 += 1
        #print(sum0,sum1,sum2,sum0+sum1+sum2)
        if sum0 < test:
            test = sum0
            temp1 = sum1*sum2
            #print(temp1)
        
    return temp1

print(check0andcal(st,6*25))

def findImage(inputname,numInLay):
    temp = splitlen(inputname,numInLay)
    res = ['2']*numInLay
    for i in temp:
        for j in range(len(i)):
            if res[j] == '2':
                res[j] = i[j]
        print(res)
        
    ans = ''
    for i in res:
        ans += i
    return ans

print(findImage(st,25*6))
a = findImage(st,25*6)

for i in range(6):
    print(a[25*i:25*(i+1)])
            

