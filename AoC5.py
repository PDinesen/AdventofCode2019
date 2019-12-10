# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 08:57:46 2019

@author: Mitfo
"""

import AoCHelper as AC

st = AC.readInputCommaLine("input5.txt")


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


def runProgram(programTo, input, input2):
    programToRun = programTo.copy()
    instructionPosition = 0
    output = 0
    inputparam = input
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
            programToRun[firstInput] = inputparam
            inputparam = input2 
            nextStep = instructionPosition + 2
        if instruction == 4:
            output = programToRun[firstInput]
            #print("Output is " + str(programToRun[firstInput]))
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

    return output

#print(runProgram(st, 1,1)) #task 1
#print(runProgram(st, 5,5)) #task 2

