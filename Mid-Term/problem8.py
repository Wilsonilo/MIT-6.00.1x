#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 12:49:51 2017

@author: wilson
"""

def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
    
    def calculatebyX(x):
        total = 0    
        counter = len(L)
        
        for element in L:
            counter -= 1
            total += (x ** counter) * element
        return total
    return calculatebyX

general_poly([1, 2, 3, 4])