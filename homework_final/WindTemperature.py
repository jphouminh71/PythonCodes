#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 22:59:05 2017

@author: jonathanphouminh
"""

#Enter the temperature or t
t = input("Please enter the actual temperature:")
t = float(t)
#Enter the wind speed or v
v = input("Please enter the wind speed:")
v = float(v)
#calculations to find the wind chill
w = 35.74 + 0.6215 *t + (0.4275 *t - 35.75)*(v **0.16)
w = int(w)
#print how the temperature feels with wind chill
print ("The temperature feels like (wind chill):", w ,"degrees")

