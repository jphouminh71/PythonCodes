#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 20:31:42 2017

@author: jonathanphouminh
"""

import random

x = random.randrange(1,100)

if x % 10 < 7:
    print(x, " player wins")
else:
    print(x, " player loses")