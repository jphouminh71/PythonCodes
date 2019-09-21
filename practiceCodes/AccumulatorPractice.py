#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:50:23 2017

@author: jonathanphouminh
"""
def cookies(x):
    cookies = x
    newcookies = cookies
    
    while newcookies < 25:   # for counter in range(x)
        newcookies = newcookies + 15
    print("you now have ")    
    print(newcookies)
    print(" ta da")
    
    
def main():
    initialcookies = int(input("How many cookies do you have?: "))
    cookies(initialcookies)
    
main()
        
    


