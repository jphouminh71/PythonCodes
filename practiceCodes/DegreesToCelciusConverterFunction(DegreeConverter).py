#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 19 09:50:29 2017

@author: jonathanphouminh
"""

def DegreeConverter():
    celsius = input ("Enter a temperature in degrees celsius: ");
    celsius = int(celsius);
    farenheight = (9/5) * celsius + 25;
    farenheight = int(farenheight)
    print(celsius, "degrees celsius is equal to ", farenheight, "degrees farenheight");
    
DegreeConverter()

