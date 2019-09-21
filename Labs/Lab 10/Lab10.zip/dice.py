#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 12:14:23 2017

@author: ioanafleming
"""
import random

class dice():
    def __init__(self, sides):  #constructor
        self.sides = sides    # number of sides for the dice

    def roll(self):
        return random.randint(1, self.sides)