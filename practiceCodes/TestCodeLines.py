#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 19:51:53 2017

@author: PetterReistad
"""

import random

MilesTraveled = 0
oxen = 0
food = 0
Cash = 1600
wagon_parts = 0
med_kit=0
bullets = 0
DayCount = 0
player=input("What is your name?")
player1=input("What would you like to call your first companion?")
player2=input("What would you like to call your second companion?")
player3=input("What would you like to call your third companion?")
player4=input("What would you like to call your fourth companion?")
Quit = 0
StoreBill=0
Travelers=5



player_health = 100
player1_health = 100
player2_health = 100
player3_health = 100
player4_health = 100

def Welcome():
    print("welcome to the Oregon Trail!")
 #brief welcome to the user to the game
'''Initial welcoming remarks to the game'''

#def PlayerName ():
   # print("Starting travelers need a name")
    #playerName = str("Enter your starting name here: ")  

'''startingNames is a function housing the names given by the player. The names, specifically, are for
defining the other four characters in the game'''
#def startingNames ():
    #'''firstName is the first defined player'''
    #firstName = input("What are the first name of another of the other four members of your party?")
    #'''secondName is the second defined player'''
    #secondName = input("What are the first name of another of the other four members of your party?")
    #'''thirdName is the third defined player'''
    #thirdName =  input("What are the first name of another of the other four members of your party?")
    #'''fourthName is the fourth defined player'''
    #fourthName = input("What are the first name of another of the other four members of your party?")



def store():
    global Cash
    global StoreBill
    print("Welcome to the store!")
    print("You have saved $1600 for the trip. You will need to spend the rest of your money on the following items: ")
    print("- Oxen: You must spend between $100 and $200 on oxen. The more you purchase for your team the faster you will go.")
    print("- Food: The more you have the less chance you have of getting sick.")
    print("- Ammunition: You will need bullets to for attacks by animals and bandits, and for hunting food.")
    print("Miscellaneous Supplies: This includes medicine and other things you may need before you begin your journey.")
    print("You can spend all of your money now or you can save some of your cash to spend in forts along the way.")
    oxen_store()
    food_store()
    bullets_store()
    miscellaneous_parts_store()
    Cash=Cash-StoreBill
    print("Your total cost is: ", StoreBill)
    print("Your remaining balance is: ", Cash)
    print("Thank you for shopping with us!")
    

def oxen_store():
    global Cash
    global StoreBill
    global oxen
    yoke=input("How many yokes of oxen would you like to purchase? (Each yoke contains 2 oxen)")
    yoke=int(yoke)
    oxen_price=40
    if yoke <3 and yoke>0:
        yoke=input("You must purchase at least 3 yokes. How many yokes would you like to purchase?")#ask again
    if yoke >3 and yoke <=5:
        oxen_price=yoke * 40
    if yoke >5:
        yoke=input("There is no need to purchase more than 5 yokes. How many would you like to purchase?")#ask again
    StoreBill=StoreBill + oxen_price
    Cash=Cash-StoreBill
    oxen=oxen +(yoke*2)
    print("Thank you for your purchase!")
    print("Your remaining balance is", Cash)
    return StoreBill
    
def food_store():
    global Cash
    global StoreBill
    global food
    print("It is recommended that you purchase at least 200 lbs. per person. Each pound is 50 cents.")
    cost_of_food=0
    lbs_of_food=input("How many lbs. of food would you like to purchase? ")#ask user how many lbs of food they want to buy
    lbs_of_food=int(lbs_of_food)
    cost_of_food=lbs_of_food * 0.5
    StoreBill=StoreBill + cost_of_food
    food=food + lbs_of_food
    print("Thank you for your purchase!")
    return StoreBill

def bullets_store():
    global Cash
    global StoreBill
    global bullets
    Bullets=input("How many boxes of bullets (each containing 20 bullets) would you like to purchase? (Each box costs $2)" )#ask user how many boxes of bullets they want(contains 20 bullets each)
    Bullets=int(Bullets)
    Bullets=Bullets*2
    cost_of_bullets=Bullets * 2
    StoreBill=StoreBill + cost_of_bullets
    bullets=bullets + Bullets
    print("Thank you for your purchase!")
    return StoreBill

def miscellaneous_parts_store():
    global Cash
    global StoreBill
    global wagon_parts
    global med_kit
    wagon_parts=input("Wagon parts are necessary in case your wagon breaks down. Each part is $10. How many wagon parts would you like to purchase?" )#ask user how many parts they want
    wagon_parts=int(wagon_parts)
    cost_of_parts=wagon_parts * 10
    med_kit=input("Medical kits($15 each) are helpful if a traveler becomes sick. How many would you like to purchase?")# ask user how many med kits they want
    med_kit=int(med_kit)
    cost_of_kit=med_kit * 15
    StoreBill=StoreBill + cost_of_parts + cost_of_kit
    print("Thank you for your purchase!")
    return StoreBill

def TakeTurn():
    ToDo = str(input('It is your turn. What would you like to do? You can continue your trip (1), rest (2), hunt (3) or quit the game (4). Please type the number corresponding to what you would like to do. '))
    if ToDo == '1':
        Continue()
    elif ToDo == '2':
        Rest()
    elif ToDo == '3':
        hunt(DayCount, bullets, player1_health, player2_health, player3_health, player4_health, player_health, food)
    elif ToDo == '4':
        QuitGame()

def hunt():

    global DayCount
    global bullets
    global player1_health
    global player2_health
    global player3_health
    global player4_health
    global player_health
    global food
    '''
    current_day = day 
    bullet_count = bullets
    total_food = food
    CURRENT_Player_Health = player_health
    CURRENT_Player1_Health = player1_health
    CURRENT_Player2_Health = player2_health
    CURRENT_Player3_Health = player3_health
    CURRENT_Player4_Health = player4_health
    '''
    
    
    
    number = random.randrange(0,101)
    animal = 0    #        ELIGiBLE AMOUNT OF FOOD THEY CAN HUNT
    bool = False
    for animals in range(1):
        number = random.randrange(0,101)
        if number < 50:
            print("YOU HAVE ENCOUNTERED A RABBIT")
            animal = animal + 2
            bool = True
        number = random.randrange(0,101)
        if number <= 25:
            print("YOU HAVE ECOUNTERED A FOX")
            animal = animal + 5
            bool = True 
        number = random.randrange(0,101)
        if number <= 20:
            deer_weight = random.randrange(35,61)    
            print("YOU HAVE ENCOUNTERED A DEER")
            animal = animal + deer_weight
            bool = True
        
        number = random.randrange(0,101)
        if number <= 10:
            bear_weight = random.randrange(100,301)
            print("YOU HAVE ENCOUNTERED A BEAR")
            animal = animal + bear_weight
            bool = True
        if number <= 5 :
            moose_weight = random.randrange(300,701)
            print ("YOU HAVE ENCOUNTERED A MOOSE")
            animal = animal + moose_weight
            bool = True
       
    
            
    
        decision = input("WOULD YOU LIKE TO HUNT? (1) = Yes (2) = NO\n")
        if decision == "1":
            if player_health != 0:
                player_health = 100
            elif player1_health != 0:
                player1_health = 100
            elif player2_health != 0:
                player2_health = 100
            elif player3_health != 0:
                player3_health = 100
            elif player4_health != 0:
                player4_health = 100
        
            
            if bullets < 10:
                print("INSUFFICIENT BULLETS")
                print("THE HUNT WAS UNSUCCESSFUL TRY AGAIN NEXT TIME")
                DayCount == DayCount + 1
            else:
                bool = RaiderPuzzle()
                if bool == "True":
                    lost_ammunition = random.randrange(5,31)
                    print("THE HUNT WAS SUCCESSFUL")
                    food = food + animal 
                    bullets = bullets - lost_ammunition
                    print("YOU ATTAINED ", food, "POUNDS OF FOOD!")
                    print("YOU LOST ", bullets, " BULLETS!")
                
                elif bool == "False":
                    print("THE HUNT WAS UNSUCCESSFUL")
                    DayCount = DayCount + 1
        
            if decision == "2":
                print("YOU CHOSE NOT TO HUNT TODAY")
            
        if bool == False:
            print ("BAD LUCK! NO ANIMALS WERE FOUND")
        
    
    decision_two = input("HOW WELL WOULD YOU LIKE TO EAT TODAY? POORLY, MODERATLEY, WELL: \n")
    decision_two = str(decision_two)
    if decision_two == "POORLY" or "poorly":
        print("YOU HAVE CHOSEN TO EAT POORLY AND ATE 10 LBS OF FOOD AS A GROUP.")
        food = food - 10
    elif decision_two == "MODERATELY" or "moderately":
        print("YOU HAVE CHOSEN TO EAT MODERATELY WELL AND ATE 16 LBS OF FOOD AS A GROUP.")
        food = food - 15 
    elif decision_two == "WELL" or "well":
        print("YOU HAVE CHOSEN TO EAT WELL AND ATE 25 LBS OF FOOD AS A GROUP FOR THE DAY.")
        total_food = food - 25
        
        
    total_food = food
    if total_food > 1000:
        total_food = 1000
        print("THE WAGON CANNOT SUPPORT MORE THAN 1000LBS OF FOOD SO YOU HAD TO LEAVE SOME BEHIND")



def status():
    global food
    global bullets
    global oxen
    global wagon_parts
    global med_kit
    global player_health
    global player1_health
    global player2_health
    global player3_health
    global player4_health
    
    misc = wagon_parts + med_kit
    if food > 1000 :
        food = 1000
    elif food <= 0:
        game_over(food,player_health,wagon_parts,oxen)
    elif player_health <= 0:
        game_over(food,player_health,wagon_parts,oxen)
    elif oxen <= 0:
        game_over(food,player_health,wagon_parts,oxen)
    elif bullets <= 0:
        bullets = 0
    elif med_kit <= 0:
        med_kit = 0
        
    print("TOTAL MILES TRAVELED: ",MilesTraveled)
    print("YOU HAVE ", misc, " MISC. PARTS")
    print("YOU HAVE ",food, "LBS OF FOOD")
    print("YOU HAVE ",bullets, "BULLETS LEFT")
    print("YOU HAVE ",oxen, " OXEN REMAINING")
    print(player," has",  player_health, " PERCENT HEALTH")
    print(player1, " has",player1_health, " PERCENT HEALTH")
    print(player2, " has", player2_health, " PERCENT HEATLH")
    print(player3, " has",player3_health, " PERCENT HEALTH")
    print(player4, " has",player4_health, " PERCENT HEATLH")



    

def Rest():
    global DayCount
    global Health
    global food
    global Travelers
    global player_health
    global player1_health
    global player2_health
    global player3_health
    global player4_health

    DaysRest = int(1 + (2 * random.random()))
    DayCount = DayCount + DaysRest
    print('You spent', DaysRest, 'days resting')
    FoodConsumed = (Travelers * 3 * DaysRest)
    food = food - FoodConsumed
    if food <= 0:
        game_over(food,player_health,wagon_parts, oxen)
    print('During the rest, you consumed', FoodConsumed, 'lbs. of your food.')
    if 0 < player_health < 100 or 0 < player1_health < 100 or 0 < player2_health < 100 or 0 < player3_health < 100 or 0 < player4_health < 100:
        print('All travelers that were sick are now recovered')
    if player_health > 0:
        player_health = 100
    if player1_health > 0:
        player_health = 100
    if player2_health > 0:
        player_health = 100
    if player3_health > 0:
        player_health = 100
    if player4_health > 0:
        player_health = 100

    
def Continue():
    global DayCount
    global MilesTraveled
    global Travelers
    global food
    DayCount = DayCount + 14
    food_loss=int(Travelers*(14*3))
    food=int(food)
    food = food - food_loss
    if food <= 0:
        game_over(food,player_health,wagon_parts,oxen)
    TurnDistance = 70 + int(70 * random.random())
    MilesTraveled = MilesTraveled + TurnDistance
    mileStones()
    '''print('You traveled', TurnDistance, 'miles.')'''

    

def misfortune():
    if Quit==0:
        num=random.randrange(0,101)
        if num <=6:
            sick()
        elif num>6 and num <=12:
            oxen_death()
        elif num>12 and num<=18:
            thief()
        elif num>18 and num<=24:
            wagon_break()
        elif num>24 and num <30:
            bad_weather()
        
        


def sick():
    global player
    global player1
    global player2
    global player3
    global player4
    global player_health
    global player1_health
    global player2_health
    global player3_health
    global player4_health
    sickness=random.randrange(0,61)
    sick_player=random.randrange(0,51)
    if sick_player <=10:
        sick_player=player
        player_health=player_health-50
        if player_health==0:
            game_over(food,player_health,wagon_parts,oxen)
    elif sick_player >10 and sick_player <=20:
        sick_player=player1
        player1_health=player1_health-50
        if player1_health==0:
            print(player1, "has perished after falling ill. RIP")
    elif sick_player >20 and sick_player <=30:
        sick_player=player2
        player2_health=player2_health-50
        if player2_health==0:
            print(player2, "has perished after falling ill. RIP")
    elif sick_player >30 and sick_player <=40:
        sick_player=player3
        player3_health=player3_health-50
        if player3_health==0:
            print(player3, "has perished after falling ill. RIP")
    elif sick_player >40: 
        sick_player=player4
        player4_health=player4_health-50
        if player4_health==0:
            print(player4, "has perished after falling ill. RIP")
    if sickness <=10: 
        print(sick_player,"has come down with Typhoid! Rest, hunt, or use a medical kit to speed up their recovery!")
    elif sickness >10 and sickness <=20:
        print(sick_player,"has come down with Cholera! Rest, hunt, or use a medical kit to speed up their recovery!")
    elif sickness >20 and sickness <=30:
        print(sick_player,"has come down with Diarrhea! Rest, hunt, or use a medical kit to speed up their recovery!")
    elif sickness >30 and sickness <=40:
        print(sick_player,"has come down with Measles! Rest, hunt, or use a medical kit to speed up their recovery!")
    elif sickness >40 and sickness <=50:
        print(sick_player,"has come down with Dysentery! Rest, hunt, or use a medical kit to speed up their recovery!")
    elif sickness >50 and sickness <=60:
        print(sick_player,"has come down with a fever! Rest, hunt, or use a medical kit to speed up their recovery!")
    recover=input("Would you like to use a medical kit? (1=Yes, 2=No) ")
    if recover==1:
        print(sick_player, "will be recovered in two days.")
    if recover==2:
        print(sick_player, "will take five days to recover.")
        


def oxen_death():
    global oxen
    oxen=oxen-1
    print("One of your oxen died! Your progress slowed but you were able to continue thanks to the remaining oxen." )
    if oxen==0:
        game_over(food,player_health,wagon_parts,oxen)


def thief():
    global food
    num=random.randrange(15,26)
    food=food-num
    if food <= 0:
        game_over(food,player_health,wagon_parts,oxen)
    print("You have been attacked by a thief! You have lost",num,"lbs of food. ")
    return food 
    

def wagon_break():
    global DayCount
    global wagon_parts
    global food
    global player_health
    global player1_health
    global player2_health
    global player3_health
    global player4_health
    food_loss= Travelers *3
    num=random.randrange(0,31)
    if num >=20:
        print("One of your wagon wheels has broken! Use a wagon part to repair it!")
    if num >=10 and num <20:
        print("An axel on your wagon has broken! Use a wagon part to repair it!")
    if num <10:
        print("A wagon tongue has broken! Use a wagon part to repair it!")
    if wagon_parts>0:
        response=input("Would you like to repair your wagon? (1=Yes, 2=No)")
        if response==1:
            DayCount+=1
            wagon_parts=wagon_parts - 1
            food=food-food_loss
            if player_health > 0:
                player_health = 100
            if player1_health > 0:
                player_health = 100
            if player2_health > 0:
                player_health = 100
            if player3_health > 0:
                player_health = 100
            if player4_health > 0:
                player_health = 100
        if response==2:
            game_over(food,player_health,wagon_parts,oxen)
    else:
        game_over(food,player_health,wagon_parts,oxen)            
        

def bad_weather():
    global DayCount
    global player_health
    global player1_health
    global player2_health
    global player3_health
    global player4_health
    num=random.randrange(0,51)
    if num <=10:
        print("You have encountered heavy rains. You have stopped to seek shelter for the day.")
        DayCount=DayCount +1
        player_health=100
        player1_health=100
        player2_health=100
        player3_health=100
        player4_health=100
    if num>10 and num <=20:
        print("You have encountered a large thunderstorm! You have stopped to seek shelter for three days.")
        DayCount=DayCount +3
        player_health=100
        player1_health=100
        player2_health=100
        player3_health=100
        player4_health=100
    if num>20 and num <=30:
        print("You have encountered a hail storm! You have stopped to seek shelter for the day.")
        DayCount +1
        player_health=100
        player1_health=100
        player2_health=100
        player3_health=100
        player4_health=100
    if num>30 and num <=40:
        print("You have encountered a blizzard! You have stopped to seek shelter for three days.")
        DayCount=DayCount +1
        player_health=100
        player1_health=100
        player2_health=100
        player3_health=100
        player4_health=100
    if num>40 and num <=50:
        print("You have encountered a hurricane! You have stopped to seek shelter for five days!")
        DayCount=DayCount +5
        player_health=100
        player1_health=100
        player2_health=100
        player3_health=100
        player4_health=100

def game_over(food,player_health,wagon_parts,oxen):
    if food==0:
        print("You have run out of food. Game Over!")
    if player_health==0:
        print("You perished on your journey. Game Over!")
    if wagon_parts==0:
        print("Your wagon is broken and you have no way to repair it. Game Over!")
    if oxen==0:
        print("Your oxen are dead and you have no way to continue your journey. Game Over!")  

def RaiderProb():
    global Quit
    if Quit==0:
        Prob = (((((MilesTraveled/100) - 4)**2) + 72)/((((MilesTraveled/100) - 4)**2) + 12) - 1)/10
        Random = random.random()
        if Random < Prob:
            return True
        else:
            return False

def RaiderAttack():
#function that calls a misfortune (separate from the misfortune function)
    '''It gives the user 3 options: run, attack and surrender. Run allows the users to escape leaving many resources behind. Attack allows the user to fight for their resources by solving a PUZZLE from the puzzle function, if they succeed then they gain resources, if they lose they lose resources. The third option is to surrender, if the user decides this they lose many resources including cash and bullets.'''

    global oxen
    global food
    global Cash
    global wagon_parts
    global bullets
    print('Raiders are attacking you. You have three options: To run (1), attack(2) or surrender(3)')
    temp = input('What do you choose to do? ')
    if temp == '1':
        oxen = oxen - 1
        food = food - 10
        if food <= 0:
            game_over(food,player_health,wagon_parts,oxen)
        wagon_parts = wagon_parts - 1
        print('You have lost 1 oxen, 10 lbs of food and 1 wagon part')
    elif temp == '3':
        Cash = Cash * 0.75
        print('You have lost a quarter of your cash.')
    elif temp == '2':
        if RaiderPuzzle() == True:
            print('Congratulations. You have successfully fought off the raiders and gained 50 lbs. of food and 50 bullets.')
            food = food + 50
            bullets = bullets + 50
        else:
            print('You have lost to the raiders. You have lost 50 bullets and a quarter of your cash reserves.')
            Cash = Cash * 0.75
            bullets = bullets - 50
            
            
def RaiderPuzzle():
    print('To win, you must guess what the answer number between 1 and 10.')
    KeyNumber = int(random.random() * 9) + 1
    count = 3
    while count > 0:
        temp = int(input('Please guess the number. '))
        if temp == KeyNumber:
            count = 0
            return True
        else:
            print('The number is wrong.')
            count = count - 1
            if count > 0:
                print('Please try again. ')
                return False



def fort():
    fort = int("would you like to stop by the store while you are staying here?(1 = yes)(2 = no)")
    if fort == 1:
        store(Cash,StoreBill)

def river(Cash):
    River = print("you need a ferry to cross this river, it will cost you $5")
    print(River)
    Cash = Cash - 5 

def mileStones():#also needs the status function parameter
    #distanceTraveled is the total distance traveled to track if the player is at a landmark
    
    global MilesTraveled
    
    if MilesTraveled > 101 and MilesTraveled<173:
        print("YOU ARRIVED AT THE KANSAS RIVER CROSSING")
        milestone = input("WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE")
        if milestone == 2: 
            MilesTraveled == 102
            river()
        else:
            MilesTraveled == 102
            Rest()
    if MilesTraveled > 185 and MilesTraveled< 236:
        print("YOU ARRIVED AT THE BLUE RIVER CROSSING.")
        milestone = input("WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE")
        if milestone == 2: 
            MilesTraveled == 185
            Continue()
        else:
            MilesTraveled == 185
            Rest()
    if MilesTraveled > 303 and MilesTraveled< 374:
        print("YOU ARRIVED AT FORT KEARNEY.")
        fort()
        milestone = input("WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE")
        if milestone == 2: 
            MilesTraveled ==  304
            Continue()   
        else:
            MilesTraveled == 304
            Rest()
    if MilesTraveled > 553 and MilesTraveled< 624:
        milestone = int("YOU WERE PREPARED TO TRAVEL %s MILES BUT YOU ARRIVED AT CHIMNEY ROCK. WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE", MilesTraveled)    
        if milestone == 2: 
            MilesTraveled == 554
            Continue()   
        else:
            Rest()
            MilesTraveled == 554
            mileStones()
    if MilesTraveled > 639 and MilesTraveled < 710:
        milestone = int("YOU WERE PREPARED TO TRAVEL %s MILES BUT YOU ARRIVED AT FORT LARAMIE. WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE", MilesTraveled) 
        store(Cash,StoreBill)
        if milestone == 2: 
            MilesTraveled == 640
            Continue()
        else:    
            fort()
            MilesTraveled == 640
            Rest()
    if MilesTraveled > 829 and MilesTraveled< 901:
        milestone = int("YOU WERE PREPARED TO TRAVEL %s MILES BUT YOU ARRIVED AT INDEPENDENCE ROCK. WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE", MilesTraveled)    
        if milestone == 2:
            MilesTraveled == 830
            Continue()    
        else:
            Rest()
            MilesTraveled == 830
            mileStones()
    if MilesTraveled > 931 and MilesTraveled< 989:
        milestone = int("YOU WERE PREPARED TO TRAVEL %s MILES BUT YOU ARRIVED AT SOUTH PASS. WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE", MilesTraveled)    
        if milestone == 2: 
            MilesTraveled == 932
            Continue()    
        else:
            Rest()
            MilesTraveled == 932
            mileStones()
                
    if MilesTraveled > 988 and MilesTraveled< 1062:
        milestone = int("YOU WERE PREPARED TO TRAVEL %s MILES BUT YOU ARRIVED AT FORT BRIDGER. WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE", MilesTraveled) 
        store(Cash,StoreBill)
        if milestone == 2: 
            MilesTraveled == 989
            Continue()    
        else:
            fort()
            MilesTraveled == 989
            Rest()
                
                
    if MilesTraveled > 1150 and MilesTraveled< 1220:
        milestone = int("YOU WERE PREPARED TO TRAVEL %s MILES BUT YOU ARRIVED AT THE GREEN RIVER CROSSING. WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE", MilesTraveled)    
        if milestone == 2: 
           MilesTraveled == 1151
           river()
        else:
            Rest()
            MilesTraveled == 1151
            mileStones()
    if MilesTraveled > 1294 and MilesTraveled<1364:
        milestone = int("YOU WERE PREPARED TO TRAVEL %s MILES BUT YOU ARRIVED AT THE SODA SPRINGS. WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE", MilesTraveled)    
        if milestone == 2: 
            MilesTraveled == 1295
            Continue()    
        else:
           MilesTraveled == 1295
           Rest()
           mileStones()
    if MilesTraveled > 1395 and MilesTraveled< 1465:
        milestone = int("YOU WERE PREPARED TO TRAVEL %s MILES BUT YOU ARRIVED AT FORT HALL. WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE", MilesTraveled)  
        store(Cash,StoreBill)
        if milestone == 2:
            MilesTraveled == 1395
            Continue()    
        else:
            MilesTraveled == 1395
            fort()
            Rest()
                
                
    if MilesTraveled > 1534 and MilesTraveled< 1604:
        milestone = int("YOU WERE PREPARED TO TRAVEL %s MILES BUT YOU ARRIVED AT SNAKE RIVER CROSSING. WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE", MilesTraveled)    
        if milestone == 2: 
           MilesTraveled == 1534
           river()
        else:
            MilesTraveled == 1534
            Rest()
            mileStones()
    if MilesTraveled > 1648 and MilesTraveled< 1718:
        milestone = int("YOU WERE PREPARED TO TRAVEL %s MILES BUT YOU ARRIVED AT FORT BOISE. WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE", MilesTraveled)  
        store(Cash,StoreBill)
        if milestone == 2:
            MilesTraveled == 1648
            Continue()    
        else:
            MilesTraveled == 1648
            fort()
            Rest()
                
                
    if MilesTraveled > 1807 and MilesTraveled< 1877:
        milestone = int("YOU WERE PREPARED TO TRAVEL %s MILES BUT YOU ARRIVED AT THE BLUE MOUNTAINS. WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE", MilesTraveled)    
        if milestone == 2: 
            MilesTraveled == 1808
            Continue()    
        else:
           MilesTraveled == 1808
           Rest()
           mileStones()
                
    if MilesTraveled > 1863 and MilesTraveled< 1933:
        milestone = int("YOU WERE PREPARED TO TRAVEL %s MILES BUT YOU ARRIVED AT FORT WALLA WALLA. WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE", MilesTraveled)
        store(Cash,StoreBill)
        if milestone == 2: 
            MilesTraveled == 1863
            Continue()    
        else:
            MilesTraveled == 1863
            fort()
            Rest()
                
    if MilesTraveled > 2039:
        Gameend()

def QuitGame():
    global Quit
    Quit = 1
    print('You quit the game.')
    '''Show status update?'''

def Gameend():
    global Quit
    Quit==2
    if Quit==2:
        print("You have successfully completed your journey to Oregon! Congratulations!")
        
def main():
    global Quit
    Welcome()
    store()
    while Quit == 0:
        status()
        TakeTurn()
        misfortune()
        if RaiderProb() == True:
            RaiderAttack()
    
    
if __name__ == '__main__':
    main()


