# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 09:14:11 2019

@author: Mitfo
"""
import AoCHelper as AC

st = AC.readInputLines("input6.txt")

print(st)

def splitparen(stringname):
    str1 = ''
    str2 = ''
    paren = True
    for i in stringname:
        if i == ')':
            paren = False
            continue
        if paren:
            str1 += i
        else:
            str2 += i
    return [str1,str2]

    
a = list(map(splitparen,st))

print(a)    

def getargs(listname):
    temp = []
    for i in listname:
        if not i[0] in temp:
            temp.append(i[0])
            temp.append(0)
        if not i[1] in temp:
            temp.append(i[1])
            temp.append(0)
        
    return temp

b = getargs(a)
print(b)
list1 = []
list2 = []
for i in a:
    list1.append(i[0])
    list2.append(i[1])
    
list3 = []
for i in list1:
    if not i in list2:
        list3.append(i)
        
print(list1,list2,list3)

for i in list3:
    for j in a:
        if i == j[0]:
            b[b.index(j[1])+1] += 1 + b[b.index(j[0])+1]
            a.remove(j)
            
print(a,b)
            


def mycode(inname):
    a = list(map(splitparen,inname))
    b = getargs(a)
    while len(a) != 0:
        list1 = []
        list2 = []
        for i in a:
            list1.append(i[0])
            list2.append(i[1])
            
        list3 = []
        for i in list1:
            if not i in list2:
                list3.append(i)
                
        
        for i in list3:
            for j in a:
                if i == j[0]:
                    b[b.index(j[1])+1] += 1 + b[b.index(j[0])+1]
                    a.remove(j)      
    print(b)
    sums = 0
    for i in range(1,len(b),2):
        sums += b[i]
        
    if 'YOU' in b:
        print('yes')
    print(sums)
    return sums

mycode(st)

def Pathto(inname,sname):
    a = list(map(splitparen,inname))
    b = []
    c = sname
    list1 = []
    list2 = []
    for i in a:
        list1.append(i[0])
        list2.append(i[1])
    while True:
        if sname in list2:
            findindex = list2.index(sname)
            sname = a[findindex][0]
            b.append(sname)
        else:
            return b

f = Pathto(st,'YOU')
g = Pathto(st,'SAN')

for i in f:
    if i in g:
        h = g.index(i) + f.index(i) 
        print(h)
        break

def result(inname,YOU='YOU',SAN='SAN'):
    list1 = Pathto(inname,YOU)
    list2 = Pathto(inname,SAN)
    print(list1,list2)
    for i in list1:
        if i in list2:
            sums = list1.index(i) + list2.index(i) 
            break
           
    print(sums)
    return sums

result(st)
            

    



        
        

    



    


