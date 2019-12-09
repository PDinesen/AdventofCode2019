# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 08:57:46 2019

@author: Mitfo
"""

import AoCHelper as AC

in5 = AC.readInputCommaLine("input5.txt")
in5 = AC.strtoint(in5)
print(in5)
#in5[1] = 12
#in5[2] = 2
def findoutput(listname,inputed):
    temp = listname.copy()
    i = 0
    while i < len(temp):
        if temp[i] == 1:
            temp[temp[i+3]] = temp[temp[i+1]] + temp[temp[i+2]]
            i += 4
        elif temp[i] == 2:
            temp[temp[i+3]] = temp[temp[i+1]] * temp[temp[i+2]]
            i += 4
        elif temp[i] == 3:
            temp[temp[i+1]] = inputed
            i += 2
        elif temp[i] == 4:
            print(temp[temp[i+1]])
            i += 2
        elif len(str(temp[i])) > 2:
            tnum = str(temp[i])
            if len(tnum) == 4:
                A = temp[i+3]
            else:
                A = i+3
            if tnum[-1] == 1:
                add = True
            elif tnum[-1] == 2:
                add = False
            else:
                print('error')
                break
            if tnum[-3] == 1:
                C = i+1
            else:
                C = temp[i+1]
            if len(tnum) > 3 and tnum[-4] == 1:
                B = i+2
            else:
                B = temp[i+2]
                
            print(C,B,A)
            if add:
                temp[A] = temp[C] + temp[B]
            else:
                temp[A] = temp[C] * temp[B]
            i += 4
            
        elif temp[i] == 99:
            break
        else:
            print("wrong input at")
            print(i,temp[i])
            break
        print(i)
    return temp

#print(findoutput(in5,1))
#print(in5)

programToRun = AC.readInputCommaLine("input5.txt")


def getNextInstruction(instructionParam):
    return int(instructionParam) % 10


def getParameter(io, paramPos, instructionPos, programToRun):
    iofields = list(io)
    iofields.reverse()
    iofields = iofields + ['0', '0', '0', '0', '0']

    intermediate = int(iofields[paramPos + 1])

    if intermediate == 0:
        return int(programToRun[instructionPos + paramPos])
    elif intermediate == 1:
        return instructionPos + paramPos


def runProgram(programToRun, input):
    instructionPosition = 0

    instruction = getNextInstruction(int(programToRun[instructionPosition]))

    while instruction in (1, 2, 3, 4, 5, 6, 7, 8):

        instructionObject = str(programToRun[instructionPosition])

        if len(instructionObject) > 2:
            firstInput = getParameter(instructionObject, 1, instructionPosition, programToRun)
            secondInput = getParameter(instructionObject, 2, instructionPosition, programToRun)
            output = getParameter(instructionObject, 3, instructionPosition, programToRun)
        else:
            firstInput = int(programToRun[instructionPosition + 1])
            secondInput = int(programToRun[instructionPosition + 2])
            try:
                output = int(programToRun[instructionPosition + 3])
            except IndexError:
                output = 0

        if instruction == 1:
            programToRun[output] = int(programToRun[firstInput]) + int(programToRun[secondInput])
            nextStep = instructionPosition + 4
        if instruction == 2:
            programToRun[output] = int(programToRun[firstInput]) * int(programToRun[secondInput])
            nextStep = instructionPosition + 4
        if instruction == 3:
            programToRun[firstInput] = input
            nextStep = instructionPosition + 2
        if instruction == 4:
            print("Output is " + str(programToRun[firstInput]))
            nextStep = instructionPosition + 2
        if instruction == 5:
            if int(programToRun[firstInput]) != 0:
                nextStep = int(programToRun[secondInput])
            else:
                nextStep = instructionPosition + 3
        if instruction == 6:
            if int(programToRun[firstInput]) == 0:
                nextStep = int(programToRun[secondInput])
            else:
                nextStep = instructionPosition + 3
        if instruction == 7:
            if int(programToRun[firstInput]) < int(programToRun[secondInput]):
                programToRun[output] = 1
            else:
                programToRun[output] = 0
            nextStep = instructionPosition + 4

        if instruction == 8:
            if int(programToRun[firstInput]) == int(programToRun[secondInput]):
                programToRun[output] = 1
            else:
                programToRun[output] = 0
            nextStep = instructionPosition + 4

        instruction = getNextInstruction(programToRun[nextStep])
        instructionPosition = nextStep

    return programToRun

runProgram(programToRun, 5)

