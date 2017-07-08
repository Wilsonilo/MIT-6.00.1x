#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 11:58:28 2017

@author: wilson
"""
import operator

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}
    '''
    
    newListReturn = {}
    
    #first lest get the keys or values in order
    for key,value in d.items():

        newListReturn[value]  = newListReturn.get(value, [])
        newListReturn[value].append(key)
    
    #order Values
    for key, element in newListReturn.items():
        newListReturn[key] = sorted(element)

        
    return newListReturn   

print(dict_invert({8: 6, 2: 6, 4: 6, 6: 6}))