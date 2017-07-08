#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 11:43:18 2017

@author: wilson
"""

class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')
            
    def intersect(self, other):
        newset = []
        for element in other.vals:
            if element in self.vals:
                newset.append(element)
        
        newInset = intSet()
        if len(newset) > 0:
            for elementNew in newset:
                newInset.insert(elementNew)
        
        return newInset
    
    def __len__(self):
        return len(self.vals)

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'
    
a1 = intSet()
a1.insert(2)
a1.insert(3)
a1.insert(4)
a2 = intSet()
a2.insert(2)
a2.insert(3)
a2.insert(5)
a3 = a1.intersect(a2)
print(a1, a2, a3, len(a1))
