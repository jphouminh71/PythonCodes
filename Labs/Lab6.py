#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:07:03 2017

@author: jonathanphouminh
"""

#def oneSum(n):
    #'''This function will take user input blah blah blah'''
    #val = 0
    #for i in range (0 , n):
        #for x in range (0, i):
            #val += 10**i
    #return counter
#print(oneSum(5))

def nSum():
    '''This function will take user input blah blah blah'''
    x = int(input("Enter a number: "))
    i_altitude = x
   
  
    if i_altitude % 2 == 0:
        new_i_altitude = i_altitude / 2;
        print(new_i_altitude)
    elif i_altitude % 2 != 0:
        new_i_altitude = i_altitude*3 + 1
        print(i_altitude)
    return new_i_altitude

nSum()
            

        
            
         
            
        

    
    
    
    
    
    
    
