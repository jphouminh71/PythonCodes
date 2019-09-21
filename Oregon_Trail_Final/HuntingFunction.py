#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 14:32:31 2017

@author: jonathanphouminh
"""

#   Jonathan Phouminh
#   Oregon Trail Skeleton
#   November 17th 2017
#   Partner: Bryan Dumpert


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
    
    
   #                                    ACTUAL LAYOUT 
import random
mile=0
money=1600
def get_info():
    player = input() # ask user name
    comp_1= #ask companion name
    comp_2= #ask companion name
    comp_3= #ask companion name
    comp_4= #ask companion name
    initial_time=input()#ask for starting date/time


def distance(mile):
    # Travel = random distance in range 70-140 miles
    return travel

def store(money):
    # Explain what the user can buy
    # call functions of the four categories
    bill=0

def oxen(money,bill):
    yoke=input()#Ask user how many oxen they want(must be at least 6, each yoke contains 2 oxen)
    if yoke <3:
        yoke=input()#ask again
    if yoke >3 and yoke <=5:
        oxen_price=yoke * 40
        bill=oxen_price
    if yoke >5:
        yoke=input()#ask again
    money=money - bill
    return bill
    
def food(money,bill):
    #Recommend amount of food
    cost_of_food=0
    lbs_of_food=input()#ask user how many lbs of food they want to buy
    cost_of_food=lbs_of_food * 0.5
    bill=bill + cost_of_food
    money=money-bill
    return bill

def bullets(money, bill):
    bullets=input()#ask user how many boxes of bullets they want(contains 20 bullets each)
    cost_of_bullets=bullets * 2
    bill=bill + cost_of_bullets
    money=money - bill
    return bill

def miscellaneous_parts(money, bill)
    wagon_parts=input()#ask user how many parts they want
    cost_of_parts=wagon_parts * 10
    med_kit=input()# ask user how many med kits they want
    cost_of_kit=med_kit * 15
    bill=bill + cost_of_parts + cost_of_kit
    money=money - bill
    return bill

def status_update(time,miles,money,food,bullets,landmark):
    #print the current values supplies,distances,and time

def rest(time,food,health):
    #update time to add between 1 and 3 days
    #food= food - (number of players * 3)
    #if health is low, reset to full

def continue_trail(time,miles,food):
    #time=call time function
    #food=food-(number of playsers *3)
    #call distance function

def hunt(time,bullets,food,health):
    #call time fuction
    #num=randint(0,100)
    #for animal in num:
        #if num <=50:
            #animal=rabbit
        #num=randint(0,100)
        # if num<=25:
            #animal=fox
    #repeat loop for each animal
    #ask user if they want to hunt the animal
    #if yes and bullets <10, hunt unsuccessful
    #if yes and bullets >10, hunt successful
    #if hunt successful:
        #bullets=bullets - number per animal
        #food=food + amount per animal
    #ask user how well they want to eat
    #set rate of food loss per day
    #if player is sick, health restored to full

def quit_game():
    #Print message to end game
    
def take_turn(time,miles,money,food,bullets,health,landmark):
    #ask user what they want to do in their turn
    #call the appropriate function based on player input
    #call misfortune function
    #call the raider function

def misfortune(#set of supplies):
    num_1=rand.int(0,100):
        if num_1<=30:
            misfortune=rand.int()
            #use random integer to determine what misfortune occurs
            #call function of misfortune

def sick(#players,health):
    sickness=rand.int()
    #if sickness=__, report typhoid,cholera,diarrhea,measles,dysentary,or fever
    #if player gets sick, health-50
    #if health=0, player dies
    #if not resting, health+10 each day
    #if med kit is used, health+25 each day

def oxen_death(oxen):
    oxen=oxen-1
    if oxen==0:
        #call game over function

def thief(food):
    num-rand.int(15,25)
    food=food-num
    return food

def wagon_break(wagon_parts):
    num=rand.int(0,30):
        #if num =___, report which part breaks
        #if wagon parts:
            #time+1
            #wagon_parts-1
            #health restores at normal rate
            #if no wagon parts:
                #call game over function

def bad_weather(food,health):
    num=randint(0,5)
    #if num=0, report heavy rain, day=day+1
    #if num=1, report storm, day=day+3
    #if num=2, report hail, day=day+1
    #if num=3, report blizzard, day=day+3
    #if num=4,report hurricane, day=day+5
    #health restores
    
def raider_attack(miles,#other supplies):
    attack=((((miles/100)-4))**2)+72)/((((miles/100)-4))**2)+12)-1
    #if attack, ask user what they want to do
    #If run:
        #ox-1
        #food-10
        #wagon_parts-1
    #if attack:
        #call puzzle function
        #if win/pass puzzle:
            #food+50
            #bullets+50
        #if lose/fail puzzle:
            #reduce=cash*.25
            #cash=cash-reduce
            #bullets-50
    #if surrender:
        #reduce=cash*.25
        #cash=cash-reduce
        
def puzzle():
    puzzle_num=randint(1,10)
    #ask user to guess num
    #if correct, puzzle solved
    #if incorrect, ask again
    #if still incorrect, ask again
    #if not correct, puzzle failed
    
def milestones(miles):
    #open the milestones file in read mode
    #for line in file:
        #split line
        #if line=length of 3:
            #print current mileage
            #print distance to next river
            #mile+=distance
            #ask user to rest or cross
            #if river >3, ferry==true
            #if ferry==true:
                #money-5
                #call continue function
        #if line=length of 2:
            #print current mileage
            #print distance to next fort
            #mile+=distance
            #ask user to rest, visit store, or continue, call function
        #if line=length of 1:
            #print current mileage
            #print distance to next landmark
            #mile+=distance
            #ask user to rest or continue, call appropriate function
            
def game_over(miles,#supplies,misfortune):
    #if mile=2040 and time<number of days:
        #print message congratulating player on winning the game
    #if food=0:
        #print game over message
    #if oxen=0:
        #print game over message
    #if misfortune=broken wagon and wagon_parts=0:
        #print game over message
    #if player_health=0:
        #print game over message
        
def main(#miles, time, supplies, health, etc):
    #print game start messages
    #call store function
    #while player turn:
        #call take turn function
        #other functions called in take turn function based on player choice
        #if supplies=0 or player health=0 or wagon broken:
            #call game over function
        #if miles=2040 and time<number of days:
            #call game over function
    
    
