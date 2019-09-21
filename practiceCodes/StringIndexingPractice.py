#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 13:05:43 2017

@author: jonathanphouminh
"""

# Contacination
first_name = "Jonathan"
last_name = "Phouminh"
student_name = (first_name) + " " + (last_name)

print(student_name)
print(first_name, last_name)
print(first_name + " " + last_name)
print(first_name, last_name)  # commas automatically add spaces
print((first_name + last_name)*2)

user_number = "1111"
username_full = user_number +"_"+ last_name + first_name
print(username_full)

print(first_name < last_name)

#printing individual characters
school = "Luther College"
m = school[0]
print(m)

print(len(first_name))  #prints length of string
print(ord(first_name[0]))  #prints the indexing character
print(first_name[1]<last_name[3])

#Slicing
username_first_part = first_name[0:2]
print(username_first_part * 2)
print(username_first_part + last_name[0:2])

username = first_name 
username = username + "("
print(username)
print(id(username))

print(first_name[3:5])

length = len(first_name)
for index in range(length):   #rememeber that this counts 01234
    print(first_name[index])
    print (" ")
idx = 0
while(idx<length):
    print(first_name[idx])
    idx += 1     #same as doing idx = idx + 1
    
for a_char in first_name:
    print(a_char)
    
    
def numberJ(a_string):
    counter = 0
    length = len(a_string)
    for i in range(length):
        if a_string[i] == "j" or a_string[i] == "J":
            counter = counter + 1
    return counter
    
if_name == "_main_":
    name = input("type a name")
    number_of_Js
    print(number_of_Js"

numberJ("Juilo")

