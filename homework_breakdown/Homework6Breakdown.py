#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 15:01:35 2017

@author: jonathanphouminh
"""
#   Jonathan Phouminh
#   Rajarshi Basak
#   Jeapordy Dice
#   Payden Burke
#   Our program will let players play jeapordy dice


# 2 players will play, computer and player
# The user always goes first
# game ends when score either player reaches 100
#  If a player rolls one turn ends; anything else they can keep rolling or hold
#  Holding: if a player holds, they score their current turn total and their turn ends. If,
#  for example, a player rolled a 3, 4, and 2, then decides to hold, they score 9 points.
# if the player is the user then they can decide to hold or keep rolling
# If the player is the computer then they will automatically keep rolling until they score over 10


# -*- coding: utf-8 -*-

import random

def print_current_player(is_user_turn): #THIS FUNCTION WORKS PROPERLY
    '''This function will take the boolean value from is_user_turn and return a print statement'''
    if is_user_turn == True:
        print("It is now human's turn")
    if is_user_turn == False:
        print("it is now computer's turn")
    
def roll_dice(): #THIS FUNCTION WORKS PROPERLY
    '''This function will take no arguments but will return an int value from 1,6'''
    for dice in range(1):
        dice = random.randrange(1,7)
        dice = int(dice)
        
        return dice
            
def take_turn(is_user_turn, COMPUTER_HOLD):         # other guy helped me
    if is_user_turn == True:    # USER TURN
        turn_total = 0
        dice_roll = roll_dice()
        
        while dice_roll > 1:
            dice_roll = roll_dice()
            print("Your rolled a ", dice_roll)
            print("Your turn total is ", dice_roll)
            turn_total = turn_total + dice_roll
            re_roll = input("Do you want to roll again (Y/N) ?")
            if re_roll in "Yy" :
                dice_roll = roll_dice()
                turn_total = turn_total + dice_roll
                print("You rolled a ", dice_roll)
            elif re_roll in "Nn" :
                turn_total = turn_total + dice_roll
            
            elif re_roll == 1:
                turn_total = 1
            
        if dice_roll == 1:
            turn_total = 1
            re_roll = "Nn"
            
    if is_user_turn == False:      #COMPUTER TURN
        computer_point_total = 0
        
        while computer_point_total < COMPUTER_HOLD:
            dice_roll = roll_dice()
            print("Your rolled a ", dice_roll)
            computer_point_total = computer_point_total + dice_roll
            
            
            if dice_roll == 1 :
                computer_point_total = 1
                re_roll = "Nn"
  
def report_points(user_point_total, computer_point_total): #AS OF RIGHT NOW THE FUNCTION WORKS BUT ONLY UPDATES THE RUNNING TOTAL ONCE PER TURN
    '''This function will receive the two parameters above and then return a print statement saying the total points'''
    print(user_point_total)
    print(computer_point_total)
def get_next_player(is_user_turn):
    if is_user_turn == True:
        return False
    if is_user_turn == False:
        return True
    
def game
    
def main():
    GAME_POINT_ENDS = 100
    COMPUTER_HOLD =10
    is_user_turn = True
    dice_roll=(roll_dice()) 
    is_user_turn = get_next_player(is_user_turn)
    x = int(take_turn(is_user_turn, COMPUTER_HOLD)
  
    
    user_point_total = 0
    computer_point_total = 0
    
    print("Welcome to Jeapordy Dice!")
    while user_point_total < GAME_POINT_ENDS and computer_point_total < GAME_POINT_ENDS:
        print_current_player(is_user_turn)
        if is_user_turn == True:
            user_point_total = user_point_total + take_turn(is_user_turn, COMPUTER_HOLD)
        elif is_user_turn == False:
            computer_point_total = computer_point_total + x
        
        report_points(user_point_total, computer_point_total)
        is_user_turn = get_next_player(is_user_turn)
        
        
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    #print("Welcome to Jeopardy Dice!")
    #print_current_player(is_user_turn)
    #take_turn(is_user_turn , COMPUTER_HOLD)
    #report_points(turn_total_total, turn_total_total)
    #get_next_player(is_user_turn)    
    
    
    
            


# while 
# print_player
# take turn()
# report_points
# get next player

    
    

    

