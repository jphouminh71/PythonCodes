#   Jonathan Phouminh
#   Rajarshi Basak
#   Section 301
#   FortuneTeller
#   This program will give 'fortunes' to the user depending on their input


#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 20:42:22 2017

@author: jonathanphouminh
"""

def greeting_the_user ():
    '''This function will be the initial greet for the user'''
    print("Welcome to Madame Maxine's Fortune Palace.")
    print("Here, we gaze deeply into your soul and find the ")
    print("secrets that only destiny has heretofore known!", )
    print(" ")
    print("The power of my inner eye clouds my ability to keep")
    print("track of mundane things like the date.")
def get_today():
    '''This function asks for day of month and returns as integer'''
    
    
    x = input("Tell me, what day of the month is it today: ")
    x = int(x)
    
    
    return x;
    
    
def get_birthday():
    '''This function asks user for date of birth'''
    print("Numerology is vitally important to fortune telling")
    day_of_birth = input("Tell me, what day of the month were you born on: ")
    day_of_birth = int(day_of_birth)
   
    
    return  day_of_birth;
def get_birthmonth():
    '''This function will collect the month the user was born in (int)'''
    
    x = int(input("Tell me what month you were born in:"))
    
    
   
    return x;
    
def likes_spicy_food():
    '''This function asks user if they like s.foods and returns boolean'''
    print("One more question before we begin.")
    x = int(input("Do you like spicy food? (1 = yes,2 = no):"))
    result = bool
    if (x == 1):
        result = True
    elif (x == 2):
        result = False
        
    return result;                                              #CHECK THIS
def read_lifeline( today, dayofbirth, likesspicyfoodornot):
    '''This function uses 3 arguments to evalate read_lifeline'''
    #tt = True
    #ff = False
    if likesspicyfoodornot == True and dayofbirth % 3 == 0:
        print("You have a long, deep line. Your life will be filled with health and balance.")
    elif likesspicyfoodornot == True and today % 4 == 0 or today % 5 == 0:
        print("You have a short, deep line. You possess remarkable fortitude")
    elif likesspicyfoodornot == True and  dayofbirth % 3  != 0 or today % 4 != 0 or today % 5 != 0:
        print("A dark cloud passes over my inner eye.")
    elif likesspicyfoodornot == False:
        print("Your line is forked and branching. Interesting events await you")

def read_heartline(today, birthmonth):
    '''This function uses 2 arguments to evaluates read_heartline'''
    if today == birthmonth:
        print("Your heartline is the perfect example of long. You are filled with warmth and love.")
    elif ((today - birthmonth) < -10) or ((today - birthmonth) > 10):
        print("You have a faint line. You will need to work to stay present emotionally.")
    else:
        print("The deepness of your heartline will cause trouble if you are not aware.")
def read_headline(dayofbirth, birthmonth):
    '''This function takes 2 arguments and evaluates read_headline'''
    if birthmonth <= 3:
        print("I'm afraid the crosses that I see here cannot be good.")
    elif birthmonth == dayofbirth :
        print("The deep and wavy line here shows excellent memory but not without conflict")
    elif birthmonth % 2 == 0 and dayofbirth % 2 == 0 or birthmonth % 2 != 0 and dayofbirth != 0:
        print("The branched and upwards line here shows big dreams and self awareness.")
    else:
        print("The branched line here shows many events unknown to even the spirits")
    
        
       
    
def main():
    greeting_the_user()
    today = get_today() 
    dayofbirth = get_birthday()    
    likesspicyfoodornot = likes_spicy_food()
    birthmonth = get_birthmonth()
    
    if (today >= 1 and today <= 9):
        print("I will now read your lifeline. ")
        read_lifeline(today,birthmonth,likesspicyfoodornot)
    elif (today >=10 and today <=19):
        print("I will now read you heartline. ")
        read_heartline(today, birthmonth)
    elif (today >=20 and today <=29):
        print("I will now read your headline. ")
        read_headline(dayofbirth, birthmonth)
    elif (today  == 30):
        print("Today is a bad day to read fortunes")
    elif (today == 31):
        print("The winning lottery numbers are 1,21,22,34,43,45")
        
    
main()
print("These insights into your future are not to be enjoyed or dreaded,")
print("they simply come to pass.")
print("Good day")




# FIX MAIN FUNCTION , ADD IF OR ELSE STATEMENTS
# Add last statement that concludes the program
# Fix Last print statement in main function
# make sure it matches the trials
    
    