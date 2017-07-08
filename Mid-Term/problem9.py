#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 13:13:13 2017

@author: wilson
"""

def is_list_permutation(L1, L2):
    '''
    L1 and L2: lists containing integers and strings
    Returns False if L1 and L2 are not permutations of each other. 
            If they are permutations of each other, returns a 
            tuple of 3 items in this order: 
            the element occurring most, how many times it occurs, and its type
    '''
    finalTuple = (None, None, None)
    majorSizeList = []
    minorSizeList = []
    listCounterOfElementsMajor = {}
    listCounterOfElementsMinor = {}
    
    #check if empty
    if len(L1) == 0 and len(L2) == 0:
        return finalTuple
    
    #check for difference on sizes of both lists
    if len(L1) != len(L2):
        return False
    
    #Set Minor and Major lists
    if len(L1) > len(L2):
        majorSizeList = L1
        minorSizeList = L2
    else:
        majorSizeList = L2
        minorSizeList = L1
         
    #Conform Major List Counter
    for element in majorSizeList:
        try:
            listCounterOfElementsMajor[element]  = listCounterOfElementsMajor.get(element, 0) + 1
            
        except:
            return False
    #Conform Minor List Counter
    for element in minorSizeList:
        
        try:
            listCounterOfElementsMinor[element]  = listCounterOfElementsMinor.get(element, 0) + 1
            
        except:
            return False

    #loop both lists for counter Differences
    for key,value in listCounterOfElementsMajor.items():
        
        if listCounterOfElementsMajor[key] != listCounterOfElementsMinor[key]:
            return False
    
    #loop major to get numbers and keys
    elementThatOccursTheMost    = ""
    howManyTimesOccurs          = 0
    typeOfelementThatOccurs     = ""
    for key,value in listCounterOfElementsMajor.items():
        if int(value) > howManyTimesOccurs:
            howManyTimesOccurs = value
            elementThatOccursTheMost = key
            typeOfelementThatOccurs = type(key)
            
    #set if everything is complete
    finalTuple = (elementThatOccursTheMost, howManyTimesOccurs, typeOfelementThatOccurs)
    return finalTuple


print(is_list_permutation([1, 2, '5', 2, 5, 3, 4, 4, 5, 5, 6], [3, 5, 1, '5', 2, 5, 2, 6, 4, 5, 4]))