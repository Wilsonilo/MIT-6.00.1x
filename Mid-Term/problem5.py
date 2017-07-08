#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 10:49:14 2017

@author: wilson
"""

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    if s != '':
        newstring = ""
        for letter in s:
            if letter.lower() != "a" and letter.lower() != "e" and letter.lower() != "i" and letter.lower() != "o" and letter.lower() != "u":
                newstring += letter
        
        if len(newstring) > 0:
            print(newstring)
        else:
            print('')
    else:
        print('')
    
    
print(print_without_vowels("a"))