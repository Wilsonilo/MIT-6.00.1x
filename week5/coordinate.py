#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 11:00:16 2017

@author: wilson
"""

class Coordinate(object):
    
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y
    
    #return string
    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'    
    
    #return repr
    def __repr__(self):
        return 'Coordinate(' + str(self.getX()) + ',' + str(self.getY()) + ')'

    #x and y equal?
    def __eq__(self, other):

        if isinstance(other, Coordinate):
            return self.x == other.x and self.y == other.y
        else:
            return False