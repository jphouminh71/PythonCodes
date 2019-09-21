#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:32:31 2017

@author: jonathanphouminh
"""

#   Jonathan Phouminh
#   Oregon Trail Skeleton
#   November 17th 2017
#   Partern: Bryan Dumpert


#This program will simulate the oregon trail, a family of 5 will try to cover a 2040 mile distance in'''
# 5 to 6 months, and if they do not make it to the end of the trail by November 30th they will die
'''Concepts'''
# Players can buy supplies before the game starts
# They can also go to forts and buy food/ hunt
# player will manage supplies along the way for the game
# Misfortunes frequently
# Game will end when they either finish the game, die, or when they run out of parts/ supplies.
'''Initial Conditions of the game'''
# Player will start with intial traveling distance of 0 and 1600 dollars of money
'''Process'''
# Before the game actually begins the player can go to the store first and purchase whatever they want
# Give the player a default start date, 6 months before November 30th.
# If the player doesn't want to start on the default date then they will have an option to enter whatever date. 
# No matter what day they start, the game will end on November 30th

def get_player_player_information():
    '''This function will assign player names to the 5 travelers and return them as strings'''
def visit_the_store():
    '''This function will be where the player can use whatever money they have and then buy stuff'''
    # insert the print statement will print the text from the pdf file.
    # ask what they would like to purchase with while statement 
    # Example, while they would like to purchase
    # Then this function will ask what they would like to buy 
    # IF STATEMENTS
    # Oxen, makes them progress faster
    # Food, makes it so they wont get sick
    # Bullets, hunting
    # Miscallaneous, Wagon wheel parts or med kits
    '''Each store price will also increase by increments'''
    '''Important to know that if the player has insufficient funds that the while loop will terminate and print out a text that they have no money'''
def take_turn():
    '''This function will take the parameters of the players and will act as a function that essentially calls all the other functions again'''
    # Each turn represents two weeks
    # The typical traveling distance will be from 70 and 140 miles each turn
    # At the beginning of each turn the function will print out the status of the players turn
    # During the turn the player has options you have to ask
    # IF they want to rest. 
    # IF they want to continue on the trail
    # IF they want to hunt
    '''Inside of the hunt function will have a puzzle function that the user will need to complete if they kill the animal or not'''
        # the hunt function will be very large because of the amount of animals they can encounter
    # IF they want to quot the game entirely
        # If they quit the game terminates and prints a certain statement
        
def misfortunes():
    '''After each turn ends there will be a 30% probability that a misfortune will happen'''
def raider_attack():
    ''' After each turn and misfortune occurs the program will go to this function where there will be a chance for raider attacks'''
    '''This function will contain a function on puzzles to defeat raiders'''
def milestones():
    '''When the distance traveled reaches this'''
    
def main():
    '''This function will hold my local variables that will be needed to be kept track of throughout the duration of the game'''
    
