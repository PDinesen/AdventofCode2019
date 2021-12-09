# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 09:49:02 2019

@author: Mitfo
"""


def readInputLines(fileName):
    return [line.rstrip('\n') for line in open("C:/Users/Mitfo/Dropbox/Privat/AdventofCode/2019/" + fileName)]


def readInputCommaLine(fileName):
    lines = readInputLines(fileName)
    return lines[0].split(',')


def strtoint(listname):
    temp = []
    for i in listname:
        temp.append(int(i))
    return temp
