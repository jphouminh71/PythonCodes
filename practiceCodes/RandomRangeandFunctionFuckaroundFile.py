#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 13:23:04 2017

@author: jonathanphouminh
"""

#import random as m

#prob = m.randrange(1,5)
#print(prob)

def hello():
    '''prints hellow world'''
    print("hello, world!")
        
def HelloX(name):
        '''prints Hell, <input name>'''
        print("hello " + name + " !")
        
def main():
    hello()
    
    yourName = input("What's your name? ")
    HelloX(yourName)
    
    #HelloX("Amy")
    
main()

    
    