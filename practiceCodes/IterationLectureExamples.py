#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 13:06:05 2017

@author: jonathanphouminh
"""

#           While example Code

#num = 7
#while num > 0:
    #print("ok")
    #num = num - 1
    

 #          Countdown for a rocket: 5,4,3,2,1, Blastoff!
import time

num = 5
while num > 0:
    print(num)
    num = num - 1
    time.sleep(1)
    
print("Send Nudes")


# ask the user to enter some numbers/integers between 0-100, we want to add them
# ask the user to enter 999 when the're done entering scores
# display the sum
# working accumulator function
def main():
    '''This function asks user for inputs and multiplies them out'''
    user_scores = int(input("enter your score. If done, enter 999: "))
    total_sum = 0
    while user_scores != 999:
        total_sum = total_sum + user_scores
        user_scores = int(input("enter your score. If done, enter 999: "))
    print(total_sum)
def avg():
    '''This function will find the average of the inputted variables'''
    user_score != 999:
    total_sum = total_sum + user_score
    total_prod = total_prod * user_score
    counter = counter + 1
    user_score = int(input("Enter your score. If done, enter 999. "))
        
    pirnt


