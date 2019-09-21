#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 00:30:06 2017

@author: ioanafleming
"""

class Player():
    def __init__(self, is_human, is_next, total_score, hold_value):  #constructor
        self.is_human = is_human    # a boolean value 
        self.is_next = is_next      # a boolean value 
        self.total_score = total_score  # an integer representing the total number of points (after each turn)
        self.hold_value = hold_value  # an integer representing the value the player holds at (meaning, the value at which it automatically chooses to pass rather than roll). 
        
    def get_is_human(self):
        return self.is_human
    
    def set_is_human(self, is_human):
        self.is_human = is_human
    
    def get_is_next(self):
        return self.is_next
    
    def set_is_next(self, is_next):
        self.is_next = is_next
        
    def get_total_score(self):
        return self.total_score
    
    def set_total_score(self, total_score):
        self.total_score = total_score
        
    def get_hold_value(self):
        return self.hold_value
    
    def set_hold_value(self, hold_value):
        self.hold_value = hold_value