#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 18:40:31 2017

@author: wilson
"""
import math

#(x % p) != 0
def genPrimes():
    p = 2
    while True:
        nextPrime = isPrime(p)
        if nextPrime:
            yield p
        p = p + 1
        
def isPrime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
         if num % i == 0:
             return False
    return True

foo = genPrimes()
print(foo.__next__())
print(foo.__next__())