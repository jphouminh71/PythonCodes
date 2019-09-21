#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 13:13:20 2017

@author: jonathanphouminh
"""

def before_Sam(li):
    '''returns how many words before the word Sam'''
    count = 0
    before = True
    idx = 0
    while idx <len(li) and before == True:
        if li[idx] == "Sam":
            count = count +1
            before = False
        else:
            count = count +1
        idx = idx + 1
        
    return count
    
def words_before_sam_vi(li):
    '''returns list of words before and including "Sam"'''
    count = 0
    before = True
    idx = 0 
    new_list = []
    while idx <len(li) and before == True:
        if li[idx] == "Sam":
            count = count + 1
            before = False
            new_list.append(li[idx])
        else:
            count = count + 1
            new_list.append(li[idx])
        idx = idx + 1
    return new_list
def main():
    my_string = "I do not like them Sam I am"
    my_list = my_string.split()
    c = before_Sam(my_list)
    print(c)
    print(words_before_sam_vi(my_list))



main()