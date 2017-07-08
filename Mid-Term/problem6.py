#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 11:07:27 2017

@author: wilson
"""

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
        
    #MARK: - Properties
    majorNumber = 0
    counterForNumbers = {}
    
    #create list counter of elements
    for number in L:
        counterForNumbers[number] = counterForNumbers.get(number,0) + 1

    
    #loop list
    majorElementVal = 0
    for key, value in counterForNumbers.items():
        if value > majorElementVal and value % 2 != 0 and key > majorNumber:
            majorNumber = key
    
    #return
    if majorNumber == 0:
        return None
    else:
        return majorNumber

print(largest_odd_times([3, 9, 5, 3, 5, 3]))