#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 14:08:26 2017

@author: jonathanphouminh
"""

def find_words(input_string):
    selective_words = []
    all_words = input_string.split
    for word in range(all_words):
        for letters in range(word):
            if len(letters) > 4:
                return letters
    return selective_words
    