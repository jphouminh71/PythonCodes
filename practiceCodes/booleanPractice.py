#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 13:05:13 2017

@author: jonathanphouminh
"""
#                               Homework 5 tips
#           Oragnize code like normal use man only for calling.
#           write them in modules

#def main():
#    n = 5
#    if n == 6 or 7 or 8:
        #print(n)
#main()

import random

x = random.randrange(1,100)

if x % 10 < 7:
    print(x, " player wins")
else:
    print(x, " player loses")


def isDivisible(x, y):
    if x % y == 0:
        result = True
    else:
        result = False
    
    return result

a = 13
b = 5
if isDivisible(a, b):
    print ( a , "is dvisible by", b)
    
else:
    print( a, "is not divisible by", b)