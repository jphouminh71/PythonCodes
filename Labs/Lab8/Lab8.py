#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 20 14:25:17 2017

@author: jonathanphouminh
"""

def fizzbuzz(n):
    
        if n % 3 == 0 and n % 5 == 0:
            return("FizzBuzz")
        elif n % 5 == 0:
            return("Buzz")
        elif n % 3 == 0:
            return("Fizz")
        else:
            return(str(n))
    

    

def no_values(init):
    i = 1
    while init > 1:
        if init % 2 == 0:
            init //= 2
        else:
            init = init * 3 + 1
            
        i+=1
    return i

def main():
    file = open('numbers.txt','r')
    otherfile = open('outputfile.txt','w')
    
    for line in file:
        values = no_values(int(line))
        to_write = fizzbuzz(values)
        otherfile.write(to_write + '\n')
        print(to_write+'\n')
        
if __name__ == '__main__':
    main()
            