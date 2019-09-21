#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 18:003:50 2017

@author: jonathanphouminh
"""

#Homework2 Calculator

#Userinput
firstnumber = input("Enter the first number:");
firstnumber = float(firstnumber);
secondnumber = input("Enter the second number:");
secondnumber = float(secondnumber);

#calculations
addition = firstnumber + secondnumber;
subtraction = firstnumber - secondnumber;
multiply = firstnumber * secondnumber;
division = firstnumber / secondnumber;
exponents = firstnumber ** secondnumber;

#printing out the calculations
print(firstnumber, "+ ", secondnumber, "= ", addition)
print(firstnumber, "-", secondnumber, "= ", subtraction)
print(firstnumber, "* " , secondnumber, "= ",  multiply)
print(firstnumber, "/ ", secondnumber, "= ", division)
print(firstnumber, "** ", secondnumber, "= ", exponents)