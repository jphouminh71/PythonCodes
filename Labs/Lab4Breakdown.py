#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 14:07:29 2017

@author: jonathanphouminh
"""

#  TASK 1
# Objectives
    #   named convertCF that converts temperature from degrees celsius in degrees fahrenheit
    #   Equation Celcius-->Farenheight  = multiply(or 9/5) and add 32.

#def convertCF(x):
    #''' convert degrees to farenheight'''
    #farenheight = (9/5) * x + 13
    ##farenheight = int(farenheight)
    #return()

#def main(celcius):
    #celcius = input("Enter a value in degrees celcius to and I will convert it into Farenheight: ")
    #celcius = int(celcius)
    
    #x = celsius
#main()

#def convertCF():
    #c = input("Give me a degree in celcius ")
    #c = int(c)
    
    #f = (9/5) * c +32
    #f = int(f)
    #print(f)
    #return(f)
    
    
#convertCF()

#def convertCF(c):
   # c = int(c)
    #f = (9/5) * c +32
    #f = int(f)
    #return(f)

def whatdayoftheweek():
    month = input("what month is it? (Enter Numerical Values)")
    m = int (month)

    day = input("what day is it? (Enter Numerical Values)" )
    d = int(day)

    year = input("what year is it? (Enter Numerical Values)")
    y = int(year)

    y0 = y - (14 - m) // 12
    x = y0 + y0 // 4 - y0 // 100 + y0 // 400
    m0 = m + 12 * ((14 - m) // 12) - 2
    d0 = (d + x + (31*m0) // 12) % 7
    
    print (d0)
    
    
whatdayoftheweek()
