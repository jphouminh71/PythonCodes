#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 22 20:27:55 2017

@author: jonathanphouminh
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 15:32:23 2017
#   Jonathan Phouminh
#   Rajarshi Basak
#   Jeapordy Dice
#   Austin Rowen
#   Our program will let players play jeapordy dice


"""


import random   

def print_current_player(is_user_turn):
    '''This function accepts the parameter is_user_turn and returns a print statement onto the console'''
    if is_user_turn==True:
        print("\nIt is now the human's turn.\n")
    else:#if not true print this
        print("\nIt is now the computer's turn.\n")
      
def roll_die():
    '''This function takes no parameters but when the function runs it will return a integer value from 1,6'''
    dice_throw=random.randrange(1,7)
    return dice_throw


def take_turn(is_user_turn, COMPUTER_HOLD):
    '''This function takes the parameters is_user_turn and COMPUTER_HOLD and returns the count to take_turn function'''
    count=0#initializes count to zero at beginning of round regardless of player
    re_roll=True#initializes re_roll to be true and beginning of round
    if is_user_turn==True:#first if statement, which is used to distinguish between the player and computer. This is the user's turn
        while re_roll==True:#start of the while loop to allow the player to do multiple roll in a single turn
            roll_numb=roll_die()#saves the function roll_die to a variable, which will allow the program to simulate a dice roll
            count=count+roll_numb#allows the count to update with every roll of the die
            if roll_numb==1:#nested if statement, that determines if the roll is a one
                count=1 # 1 is rolled count is automatically a one
                re_roll=False#then it changes re_roll to false which terminates the entire while loop
                print('You rolled a 1' )#then prints this statement
                print('Your turn total is 1')#then prints this statement
                
            elif roll_numb!=1:#the else statement that determines if the roll is anything but a one
                print('You rolled a',roll_numb)#prints this statement
                print('You turn total is',count)#prints this statement
                re_roll=input('Do you want to roll again? ')#asks the user for an input which will terminate the loop or allow it to run again
                if re_roll == 'q':#this is a force quit part of the if statement, that will allaw anyone who is manipulating the program end it when testing
                    int(re_roll)
                elif re_roll=='y' or re_roll=='Y':#the input the user needs to put in to allow the loop to run again
                    re_roll=True
                elif re_roll=='n' or re_roll=='N':#the input the user needs to put in to end the loop
                    re_roll=False
                      
    else:#this is the part of the if statement that is the computers turn
        while is_user_turn==False and count < COMPUTER_HOLD:#the requirements that the must be met for the computer turn to start and continue
            roll_numb=roll_die()#saves the function roll_die to a variable, which will allow the program to simulate a dice roll
            count=count+roll_numb#allows the count to update with every roll of the die
            print('You rolled a',roll_numb)#print this statement
            if roll_numb==1:#if rolled a one do this
                count=1#set count to one
                print('Your turn total is 1')#print this
                is_user_turn=True# set computer turn to true which will terminate the loop
            elif roll_numb!=1:#if 1 isnt rolled continue with loop until condition are met to end the loop
                print('Your turn total is',count,)#print this
    return count# return the count to take turn


def report_points(user_score,computer_score):#takes two parameters
    '''This function takes the parameters user_score and computer_score from the main function and will just return them as a print statement'''
    print('human:',user_score,'\ncomputer:',computer_score,)#prints a statement using the two parameters
  

def get_next_player(is_user_turn):#function utilizes one parameter
    '''This function takes the is_user turn and returns the inverse of the boolean value that was given'''
    if is_user_turn==True:#if user turn is true
        return False#return it as false 
    elif is_user_turn==False:#if user turn is false
        return True#return it as false
    


def game_ends(is_user_turn):#function utilizes one parameter
        if is_user_turn==False:#if is user turn is false, print statement
            print('Congratulations! human won this round of Jeopardy Dice!')
        elif is_user_turn==True:#if is user turn is true, print statement
            print('Congratulations! computer won this round of Jeopardy Dice!')
    
        

    
    
    
    
    
    
'''
This is the main function. It contains all semi global variables, and the while loop
that the program will use to run the entirety of the game. This means it will have the beginning, and ending
conditions of the game, and the basic rule that the computer must follow for the game.
'''    

def main ():
    GAME_END_POINTS=100#the number that must be attained by a player to terminate the loop(win game)
    COMPUTER_HOLD=10#the number the computer must end its turn at if a one is never rolled
    is_user_turn= True#sets the game up so that it is always the humans turn first
    computer_count=0#initializes the computers count at 0
    user_count=0#initializes the users count at 0
    
    print('Welcome to Jeopardy Dice!')
    
    while user_count<GAME_END_POINTS and computer_count<GAME_END_POINTS:#a while loop that states that as long as
                                                                          #both the user and computer counts are bellow the game end points the loop will run
        print_current_player(is_user_turn)#runs the function
        if is_user_turn==True:#if it is the users turn
            user_count += take_turn(is_user_turn, COMPUTER_HOLD)#take user count add take turn to it and save it in user count
        else: # if it is the computers turn 
            computer_count += take_turn(is_user_turn, COMPUTER_HOLD)#take computer count add take turn to it and save it in computer count
        is_user_turn = get_next_player(is_user_turn)#use get next player to get the next players turn
        report_points(user_count,computer_count)#run the report points function with whatever the user and computer count is at the time this function runs
    
    game_ends(is_user_turn)#run this function after the while loop terminates


if __name__ == '__main__':
    main()