#JonathanPhouminh 
#joph0114@colorado.edu
#The purpose of this program was to create a program that executes  
#mathematical operations with any 2 given floating points inputted by a user
#CSCI1200
#IOANA FLEMING


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 18:003:50 2017

@author: jonathanphouminh
"""

#Homework2 Calculator Task 4

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






#HomeWork2
#PseudoCode

#Ex)
#Enter first number: 23.0
#Enter Second number: 10.0

#23.0 + 10.0 = 33.0
#23.0 - 10.0 = 13.0
#23.0 * 10.0 = 230.0
#23.0 / 10.0 = 2.3
#23.0 ** 10.0 = 41426511213649.0

#Enter first number : 1.0
#Enter second number : 2.0

#1.0 + 2.0 = 3.0
#1.0 - 3.0 = -1.0
#1.0 * 2.0 = 2.0
#1.0 / 2.0 = 0.5
#1.0 ** 2.0 = 1

#Enter first number: 3.0
#Enter second number: 4.0

#3.0 + 4.0 = 7.0
#3.0 - 4.0 = -1.0
#3.0 * 4.0 = 12.0
#3.0 / 4.0 = 0.75
#3.0 ** 4.0 =  81.0

#Task 2
#Two positive numbers, Inputs: 15, 7 Expected outputs: 22, 8, 105, 2.14, 170859375

#Two negative numbers, Inputs: -8, -123 Expected Outputs:  -131.0, 115.0, 984.0, #0.06504065040650407 , -8.31632781251592e-112

#One Positive and One negative number: 5, -20 Expected Outputs: -15.0, 25.0, -100.0, #-0.25, 1.048576e-14

#Two positive numbers with both fractions: 4.5 ,9.2 Expected Outputs: 13.7, #-4.699999999999999, 41.4, 0.48913043478260876, 1022245.3100451452
#One positive number and one negative number both fractions: 3.2 , -4.5 Expected #Outputs:-1.2999999999999998, 7.7, -14.4, -0.7111111111111111, 0.005331201499700043

#One whole number and one number with a fraction: 4 , 3,2 Expected Outputs: 7.2, #0.7999999999999998 , 12.8, 1.25, 84.44850628946526

#First number is 0 second is 0: 0 ,0 Expected outputs: 0, 0 , error, 0, 0
#First number is 0 second is not 0: 0,5 Expected outputs: 5.0, -5.0, 0.0, 0.0, 0.0
#First number is not 0 second number is 0: 5,0  Expected Outputs: 5, -5, 0, error, 1
#First number is 0 second number is not 0: 0 , -1 Expected Outputs:-1, -1, 0, 0, error

#Possible inputs that could result in an error would be if you were using the division #operator and tried to divide by 0 because it isn’t possible.

#Task 3
#-Ask user to input any 2 numbers 
#-make sure numbers inputted are floating points
#-take numbers and perform operations
#-add both floating points together and print
#-subtract both floating points together and print
#-multiply both floating numbers and print
#-divide both floating numbers and print
#-raise first inputted number by second number and print
#-end program
