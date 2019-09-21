#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 15:01:42 2017

@author: jonathanphouminh
"""
def hash_func(a_string):
    counter = 0 
    letter_values = "0123456789"
    for a_char in (a_string):
        if a_char == "a":
            a = 3
            b = 5
            c = 7
            counter = counter + a
        if a_char == "b":
            b = 5
            counter = counter + b
        if a_char == "c":
            c = 7
            counter = counter + c
        
    return counter