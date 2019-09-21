#Jonathan Phouminh
#CS1200
#Decemeber 6, 2017
#Partner : Bryan Dumpert
#Final Project: The Oregon Trail Game
#       Quick note:  All variables are referenced globally. 





import random
'''Initiallization of all global variables'''
miles_traveled = 0
oxen = 0
food = 0
cash = 1600
wagon_parts = 0
med_kit=0
bullets = 0
day = 0
quit = 0
bill=0
travelers=5
player_health = 100
player1_health = 100
player2_health = 100
player3_health = 100
player4_health = 100


'''Player Identification'''
player=input("WHAT IS YOUR NAME?")
print("NOW YOU MUST NAME YOUR TRAVELING COMPANIONS")
player1=input("WHAT WOULD YOU LIKE TO NAME YOUR FIRST COMPANION?")
player2=input("WHAT WOULD YOU LIKE TO NAME YOUR SECOND COMPANION?")
player3=input("WHAT WOULD YOU LIKE TO NAME YOUR THIRD COMPANION?")
player4=input("WHAT WOULD YOU LIKE TO NAME YOUR FOURTH COMPANION?")
def welcome():
    '''This function intiallizes the game by greeting the user?'''
    print("WELCOME TO THE OREGON TRAIL")
    print("THE JOURNEY AHEAD IS LONG AND TREACHEROUS. GOOD LUCK!")
 #brief welcome to the user to the game
'''Initial welcoming remarks to the game'''

def store():
    '''function accepts cash and bill parameters that will be used in purchasing items that will be returned to their inventory'''
    global cash
    global bill
    if cash < 0:
        cash = 0
        print("INSUFFICIENT FUNDS: ", cash)
        Continue()
    if cash > 0:
        print("WELCOME TO THE STORE!")
        print("YOU HAVE SAVED $1600 FOR THE TRIP. YOU WILL NEED TO SPEND YOUR MONEY ON THE FOLLOWING ITEMS: ")
        print("-OXEN: YOU MUST SPEND BETWEEN $100 AND $200 ON OXEN. THE MORE YOU PURCHASE FOR YOUR TEAM THE LONGER YOU CAN TRAVEL.")
        print("- FOOD: A LONG JOURNEY MEANS THAT A LOT OF FOOD WILL BE NECESSARY IF YOU WISH TO SURVIVE")
        print("- AMMUNITION: YOU WILL NEED BULLETS TO HUNT AND DEFEND YOURSELF FROM BANDITS.")
        print("MISCELLANEOUS SUPPLIES: MEDICINE AND REPAIR PARTS ARE ESSENTIAL IF DISASTER STRIKES ON YOUR JOURNEY.")
        print("YOU CAN SPEND ALL YOUR MONEY NOW OR SAVE IT FOR FORTS ALONG THE WAY.")
        oxen_store()
        food_store()
        bullets_store()
        miscellaneous_parts_store()
        cash=cash-bill
        print("YOUR TOTAL COST IS: ", bill)
        print("YOUR REMAINING BALANCE IS: ", cash)
        print("THANK YOU FOR SHOPPING WITH US!")
    

def oxen_store():
    '''Part of the store(): accepts cash / bill parameters and returns a new oxen count depending on what user buys'''
    global cash
    global bill
    global oxen
    yoke=input("HOW MANY YOKES OF OXEN WOULD YOU LIKE TO PURCHASE? (EACH YOKE CONTAINS 2 OXEN)")
    yoke=int(yoke)
    oxen_price=40
    if yoke <3 and yoke>0:
        yoke=input("YOU MUST PURCHASE AT LEAST 3 YOKES. HOW MANY YOKES WOULD YOU LIKE TO PURCHASE?")#ask again
        yoke = int(yoke)
    if yoke >3 and yoke <=5:
        oxen_price=yoke * 40
    if yoke >5:
        yoke=input("THERE IS NO NEED TO PURCHASE MORE THAN 5 YOKES. HOW MANY WOULD YOU LIKE TO PURCHASE?")#ask again
    bill=bill + oxen_price
    oxen=oxen +(yoke*2)
    print("THANK YOU FOR YOUR PURCHASE!")
    print("YOUR REMAINING BALANCE IS:", cash)
    return bill
    
def food_store():
    '''Part of the store(): accepts cash / bill parameters and returns a new food count depending on what user buys'''
    global cash
    global bill
    global food
    print("iT IS RECOMMENDED THAT EVERYONE HAS 200 LBS OF FOOD. EACH POUND IS 50 CENTS.")
    cost_of_food=0
    lbs_of_food=input("HOW MANY LBS OF FOOD WOULD YOU LIKE TO PURCHASE? ")#ask user how many lbs of food they want to buy
    lbs_of_food=int(lbs_of_food)
    cost_of_food=lbs_of_food * 0.5
    bill=bill + cost_of_food
    food=food + lbs_of_food
    print("THANK YOU FOR YOUR PURCHASE!!")
    return bill

def bullets_store():
    '''Part of the store(): accepts cash / bill parameters and returns a new bullet count depending on what user buys'''
    global cash
    global bill
    global bullets
    Bullets=input("HOW MANY BOXES OF BULLETS (EACH CONTAINING 20 BULLETS) WOULD YOU LIKE TO PURCHASE? (EACH BOX COSTS $2) " )#ask user how many boxes of bullets they want(contains 20 bullets each)
    Bullets=int(Bullets)
    Bullets=Bullets*2
    cost_of_bullets=Bullets * 2
    bill=bill + cost_of_bullets
    bullets=bullets + Bullets
    print("THANK YOU FOR YOUR PURCHASE!")
    return bill

def miscellaneous_parts_store():
    '''Part of the store(): accepts cash / bill parameters and returns new misc count depending on what user buys'''
    global cash
    global bill
    global wagon_parts
    global med_kit
    wagon_parts=input("WAGON PARTS ARE NECESSARY IN CASE YOUR WAGON BREAKS DOWN. EACH PART IS $10. HOW MANY PARTS WOULD YOU LIKE TO PURCHASE?" )#ask user how many parts they want
    wagon_parts=int(wagon_parts)
    cost_of_parts=wagon_parts * 10
    med_kit=input("MEDICAL KITS ($15 EACH) ARE HELFUL IF A TRAVELER FALLS ILL. HOW MANY WOULD YOU LIKE TO PURCHASE?")# ask user how many med kits they want
    med_kit=int(med_kit)
    cost_of_kit=med_kit * 15
    bill=bill + cost_of_parts + cost_of_kit
    print("THANK YOU FOR YOUR PURCHASE!")
    return bill

    return bill

def take_turn():
    '''Takes not parameters, prompts user for input, takes input to call desired function''' 
    choice = str(input("IT'S YOUR TURN! WHAT DO YOU WANT TO DO? CONTINUE JOURNEY (1), STOP TO REST (2), HUNT FOR FOOD (3) OR QUIT GAME  (4). TYPE NUMBER FOR CHOICE"))
    if choice == '1':
        Continue()
    elif choice == '2':
        rest()
    elif choice == '3':
        hunt()
    elif choice == '4':
        quit_game()

def hunt():
    '''Takes day,bullets,player1_health,player3_health,player4_health,player_health,and food parameters and returns new values of each dependant on how the hunt goes'''
    global day
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
            print("YOU HAVE ENCOUNTERED A FOX")
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
       
    
            
    
        decision = input("WOULD YOU LIKE TO HUNT? (1) = YES (2) = NO\n")
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
                day=day + 1
            else:
                bool = puzzle()
                if bool == "True":
                    lost_ammunition = random.randrange(5,31)
                    print("THE HUNT WAS SUCCESSFUL")
                    food = food + animal 
                    bullets = bullets - lost_ammunition
                    print("YOU ATTAINED ", food, "POUNDS OF FOOD!")
                    print("YOU LOST ", bullets, " BULLETS!")
                
                elif bool == "False":
                    print("THE HUNT WAS UNSUCCESSFUL")
                    day = day + 1
        
            if decision == "2":
                print("YOU CHOSE NOT TO HUNT TODAY")
            
        if bool == False:
            print ("BAD LUCK! NO ANIMALS WERE FOUND")
        
    
    decision_two = input("HOW WELL WOULD YOU LIKE TO EAT TODAY? POORLY, MODERATLEY, WELL: \n")
    decision_two = str(decision_two)
    if decision_two == "POORLY" or decision_two == "poorly":
        print("YOU HAVE CHOSEN TO EAT POORLY AND ATE 10 LBS OF FOOD AS A GROUP.")
        food = food - 10
    elif decision_two == "MODERATELY" or decision_two == "moderately":
        print("YOU HAVE CHOSEN TO EAT MODERATELY WELL AND ATE 16 LBS OF FOOD AS A GROUP.")
        food = food - 15 
    elif decision_two == "well" or decision_two == "WELL":
        print("YOU HAVE CHOSEN TO EAT WELL AND ATE 25 LBS OF FOOD AS A GROUP FOR THE DAY.")
        food = food - 25
        
        
    
    if food <= 0:
        game_over()
      



def status_update():
    '''Accepts all global variables and returns print statements to inform user of their inventory and also checks to see if they have enough required materials to continue the journey'''
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
    global cash
    
    cash = int(cash)
    misc = wagon_parts + med_kit
    if food <= 0:
        game_over()
    elif food > 1000 :
        print("YOUR WAGON CAN ONLY CARRY 1000LBS OF FOOD. YOU HAD TO LEAVE SOME BEHIND")
        food = 1000
    elif player_health <= 0:
        game_over()
    elif oxen <= 0:
        game_over()
    elif bullets <= 0:
        bullets = 0
    elif med_kit <= 0:
        med_kit = 0
    elif cash < 0:
        cash = 0
    print("TOTAL MILES TRAVELED: ",miles_traveled)
    print("YOU HAVE ", misc, " MISC. PARTS")
    print("YOU HAVE ",food, "LBS OF FOOD")
    print("YOU HAVE ",bullets, "BULLETS LEFT")
    print("YOU HAVE ",oxen, " OXEN REMAINING")
    print(player," has",  player_health, " PERCENT HEALTH")
    print(player1, " has",player1_health, " PERCENT HEALTH")
    print(player2, " has", player2_health, " PERCENT HEATLH")
    print(player3, " has",player3_health, " PERCENT HEALTH")
    print(player4, " has",player4_health, " PERCENT HEATLH")
    print("YOUR REMAINING CASH BALANCE IS: ", cash)



def rest():
    '''Accepts all paraemters and returns new player health level, adds to day counter.'''
    global day
    global Health
    global food
    global travelers
    global player_health
    global player1_health
    global player2_health
    global player3_health
    global player4_health

    day_rest = int(1 + (2 * random.random()))
    day = day + day_rest
    print("YOU SPENT", day_rest, "DAY'S RESTING")
    consumed = (travelers * 3 * day_rest)
    if food <= 0:
        game_over()
    food = food - consumed
    print('YOU CONSUMED', consumed, 'LBS. OF FOOD DURING YOUR REST.')
    if 0 < player_health < 100 or 0 < player1_health < 100 or 0 < player2_health < 100 or 0 < player3_health < 100 or 0 < player4_health < 100:
        print('ALL SICK TRAVELERS HAVE REGAINED THEIR HEALTH ')
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
    '''Accepts day, global miles_traveled, travelers, food and updates their values'''
    global day
    global miles_traveled
    global travelers
    global food
    day = day + 14
    if food <= 0:
        game_over()
    food_loss=int(travelers*(14*3))
    food=int(food)
    food = food - food_loss
    distance = 70 + int(70 * random.random())
    miles_traveled = miles_traveled + distance
    landmark()


    

def misfortune():
    '''A function that serves as a probability to determing what misfortune the user will experience'''
    if quit==0:
        num=random.randrange(0,101)
        if num <=6:
            illness()
        elif num>6 and num <=12:
            oxen_death()
        elif num>12 and num<=18:
            thief()
        elif num>18 and num<=24:
            wagon_break()
        elif num>24 and num <30:
            storm()
        
        


def illness():
    '''Accepts all player information parameters and adjusts all players health accordingly'''
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
            print(player1, "HAS PERISHED AFTER FALLING ILL. RIP")
    elif sick_player >20 and sick_player <=30:
        sick_player=player2
        player2_health=player2_health-50
        if player2_health==0:
            print(player2, "HAS PERISHED AFTER FALLING ILL. RIP")
    elif sick_player >30 and sick_player <=40:
        sick_player=player3
        player3_health=player3_health-50
        if player3_health==0:
            print(player3, "HAS PERISHED AFTER FALLING ILL. RIP")
    elif sick_player >40: 
        sick_player=player4
        player4_health=player4_health-50
        if player4_health==0:
            print(player4, "HAS PERISHED AFTER FALLING ILL. RIP")
    if sickness <=10: 
        print(sick_player,"HAS COME DOWN WITH TYPHOID! REST, HUNT, OR USE A MEDICAL KIT TO SPEED UP THEIR RECOVERY!")
    elif sickness >10 and sickness <=20:
        print(sick_player,"HAS COME DOWN WITH CHOLERA! REST, HUNT, OR USE A MEDICAL KIT TO SPEED UP THEIR RECOVERY!")
    elif sickness >20 and sickness <=30:
        print(sick_player,"HAS COME DOWN WITH DIARHHEA! REST, HUNT, OR USE A MEDICAL KIT TO SPEED UP THEIR RECOVERY!")
    elif sickness >30 and sickness <=40:
        print(sick_player,"HAS COME DOWN WITH MEASLES! REST, HUNT, OR USE A MEDICAL KIT TO SPEED UP THEIR RECOVERY!")
    elif sickness >40 and sickness <=50:
        print(sick_player,"HAS COME DOWN WITH DYSENTARY! REST, HUNT, OR USE A MEDICAL KIT TO SPEED UP THEIR RECOVERY!")
    elif sickness >50 and sickness <=60:
        print(sick_player,"HAS COME DOWN WITH A FEVER! REST, HUNT, OR USE A MEDICAL KIT TO SPEED UP THEIR RECOVERY!")
    recover=input("WOULD YOU LIKE TO USE A MEDICAL KIT?? (1=YES, 2=NO) ")
    if recover==1:
        print(sick_player, "WILL BE RECOVERED IN 2 DAYS.")
    if recover==2:
        print(sick_player, "WILL TAKE 5 DAYS TO RECOVER")
        


def oxen_death():
    '''Accepts oxen parameter and returns oxen count subtracted by one'''
    global oxen
    oxen=oxen-1
    print("ONE OF THE OXEN DIED! YOUR PROGRESS WAS HINDERED BUT THE JOURNEY CONTINUES ON!" )
    if oxen==0:
        game_over()


def thief():
    '''Accepts food parameter and updates the current food count by subtracting a randomly generated number'''
    global food
    num=random.randrange(15,26)
    food=food-num
    if food <= 0:
        game_over()

    print("YOU WERE STOLEN FROM BY A THIEF IN THE NIGHT ! YOU LOST ",num,"LBS. OF FOOD.")
    return food 
    

def wagon_break():
    '''Accepts day, wagon parts, food, all player health, and food loss, updates player health, updates wagon part count, checks to see if player has sufficient food'''
    global day
    global wagon_parts
    global food
    global player_health
    global player1_health
    global player2_health
    global player3_health
    global player4_health
    food_loss= travelers *3
    num=random.randrange(0,31)
    if num >=20:
        print("ONE OF THE WAGON WHEELS BROKE! USE A PART TO REPAIR IT!")
    if num >=10 and num <20:
        print("AN AXEL BROKE ON THE WAGON! USE A PART TO REPAIR IT !")
    if num <10:
        print("A WAGON TONGUE HAS BROKEN! USE A PART TO REPAIR IT!")
    if wagon_parts>0:
        response=input("WOULD YOU LIKE TO REPAIR YOUR WAGON? (1=YES, 2=NO)")
        if response==1:
            day+=1
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
            game_over()
    else:
        game_over()            
        

def storm():
    '''Accepts day, and all player health parameters and returns an updated travel time dependant on which misfortune occurs'''
    global day
    global player_health
    global player1_health
    global player2_health
    global player3_health
    global player4_health
    num=random.randrange(0,51)
    if num <=10:
        print("YOU HAVE ENCOUNTERED HEAVY RAINS. YOUR TEAM HAS STOPPED TO SEEK SHELTER FOR THE DAY.")
        day=day +1
        player_health=100
        player1_health=100
        player2_health=100
        player3_health=100
        player4_health=100
    if num>10 and num <=20:
        print("YOU HAVE ENCOUNTERED A THUNDERSTORM. THE STORM HAS CAUSED YOU TO SEEK SHELTER FOR 3 DAYS.")
        day=day +3
        player_health=100
        player1_health=100
        player2_health=100
        player3_health=100
        player4_health=100
    if num>20 and num <=30:
        print("YOU HAVE ENCOUNTERED A HAIL STORM. YOUR TEAM HAS STOPPED TO SEEK SHELTER FOR THE DAY.")
        day=day+1
        player_health=100
        player1_health=100
        player2_health=100
        player3_health=100
        player4_health=100
    if num>30 and num <=40:
        print("YOU HAVE ENCOUNTERED A BLIZZARD. THE STORM HAS HALTED YOUR PROGRESS AND YOU NEED TO SEEK SHELTER FOR 3 DAYS.")
        day=day+1
        player_health=100
        player1_health=100
        player2_health=100
        player3_health=100
        player4_health=100
    if num>40 and num <=50:
        print("YOU HAVE ENCOUNTERED A HURRICANE. YOUR TEAM HAS STOPPED TO SEEK SHELTER FOR 5 DAYS")
        day=day +5
        player_health=100
        player1_health=100
        player2_health=100
        player3_health=100
        player4_health=100

def game_over():
    '''Accepts quit, ofod, player_health, and oxen and checks all those parameters if they meet the requirement. If they dont this function ends the while loop in the main function by updating the quit parameter'''
    global quit
    global food
    global player_health
    global wagon_parts
    global oxen
    #quit=1
    x = 1
    if x == 1:
        if food==0:
            print("YOU HAVE RUN OUT OF FOOD. GAME OVER!")
            quit = 1
        elif player_health==0:
            print("YOU PERISHED ON YOUR JOURNEY. GAME OVER!")
            quit = 1
        elif wagon_parts==0:
            print("YOUR WAGON IS BROKEN AND YOU HAVE NO WAY TO REPAIR IT TO CONTINUE THE JOURNEY. GAME OVER!")
            quit = 1
        elif oxen==0:
            print("ALL OF YOUR OXEN ARE DEAD AND YOU ARE UNABLE TO CONTINUE. GAME OVER!")  
            quit = 1

def raider_chance():
    '''Accepts quit variable and calculates probability of raider attack and also returns boolean value'''
    global quit
    if quit==0:
        prob = (((((miles_traveled/100) - 4)**2) + 72)/((((miles_traveled/100) - 4)**2) + 12) - 1)/10
        random_num = random.random()
        if random_num < prob:
            return True
        else:
            return False

def raider_attack():
#function that calls a misfortune (separate from the misfortune function)
    #'''#It gives the user 3 options: run, attack and surrender. Run allows the users to escape leaving many resources behind. Attack allows the user to fight for their resources by solving a PUZZLE from the puzzle function, if they succeed then they gain resources, if they lose they lose resources. The third option is to surrender, if the user decides this they lose many resources including cash and bullets.'''

    global oxen
    global food
    global cash
    global wagon_parts
    global bullets
    print('YOU HAVE BEEN ATTACKED BY RAIDERS. YOU CAN: RUN(1), ATTACK(2) OR SURRENDER(3)')
    temp = input('WHAT WOULD YOU LIKE TO DO? ')
    if temp == '1':
        oxen = oxen - 1
        if oxen <= 0 :
            game_over()
        food = food - 10
        if food <= 0:
            game_over()
        wagon_parts = wagon_parts - 1
        print('YOU HAVE LOST 1 OXEN, 10 LBS OF FOOD AND 1 WAGON PART')
    elif temp == '3':
        cash = cash * 0.75
        print('YOU HAVE LOST 1 FOURTH OF YOUR CASH.')
    elif temp == '2':
        if puzzle() == True:
            print('WELL DONE! YOU SUCCESSFULLY DEALT WITH THE RAIDERS AND GAINED 50 LBS OF FOOD AND 50 BULLETS.')
            food = food + 50
            bullets = bullets + 50
        else:
            print('YOU WERE DEFEATED BY THE RAIDERS. THEY TOOK 50 BULLETS AND A QUARTER OF YOUR CASH')
            cash = cash * 0.75
            bullets = bullets - 50
            
def puzzle():
    '''Accepts no parameter and returns boolean value'''
    print('To SOLVE THE PUZZLE, GUESS A NUMBER BETWEEN 1 AND 10.')
    KeyNumber = int(random.random() * 9) + 1
    count = 3
    while count > 0:
        temp = int(input('PLEASE GUESS THE NUMBER. '))
        if temp == KeyNumber:
            count = 0
            return True
        else:
            print('THE NUMBER IS WRONG')
            count = count - 1
            if count > 0:
                print('PLEASE GUESS AGAIN. ')


def fort():
    '''Accepts no parameters , directs user to store() function'''
    fort = input("WOULD YOU LIKE TO VISIT THE STORE AT THE FORT?(1 = YES)(2 = NO)")
    fort = int(fort)
    if fort == 1:
        store()

def river():
    '''Accepts cash parameter and returns new cash value-5'''
    global cash
    print("YOU NEED TO USE A FERRY TO CROSS THE RIVER. YOU SPEND $5 FOR A RIDE. ")
    cash = cash - 5 

def landmark():#also needs the status function parameter
    #distanceTraveled is the total distance traveled to track if the player is at a landmark
    
    global miles_traveled
    
    if miles_traveled > 101 and miles_traveled<173:
        print("YOU ARRIVED AT THE KANSAS RIVER CROSSING")
        milestone = input("WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE")
        if milestone == 2: 
            miles_traveled == 102
            river()
        else:
            miles_traveled == 102
            rest()
    if miles_traveled > 185 and miles_traveled< 236:
        print("YOU ARRIVED AT THE BLUE RIVER CROSSING.")
        milestone = input("WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE")
        if milestone == 2: 
            miles_traveled == 185
            Continue()
        else:
            miles_traveled == 185
            rest()
    if miles_traveled > 303 and miles_traveled< 374:
        print("YOU ARRIVED AT FORT KEARNEY.")
        fort()
        milestone = input("WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE")
        if milestone == 2: 
            miles_traveled ==  304
            Continue()   
        else:
            miles_traveled == 304
            rest()
    if miles_traveled > 553 and miles_traveled< 624:
        print("YOU ARRIVED AT CHIMNEY ROCK.")
        milestone = input("WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE")    
        if milestone == 2: 
            miles_traveled == 554
            Continue()   
        else:
            rest()
            miles_traveled == 554
    if miles_traveled > 639 and miles_traveled < 710:
        print("YOU ARRIVED AT FOR LARAMIE.")
        fort()
        milestone = input("WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE") 
        if milestone == 2: 
            miles_traveled == 640
            Continue()
        else:    
            miles_traveled == 640
            rest()
    if miles_traveled > 829 and miles_traveled< 901:
        print("YOU ARRIVED AT INDEPENDENCE ROCK.")
        milestone = input("WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE")    
        if milestone == 2:
            miles_traveled == 830
            Continue()    
        else:
            rest()
            miles_traveled == 830
    if miles_traveled > 931 and miles_traveled< 989:
        print("YOU ARRIVED AT SOUTH PASS.")
        milestone = input("WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE")    
        if milestone == 2: 
            miles_traveled == 932
            Continue()    
        else:
            rest()
            miles_traveled == 932
                
    if miles_traveled > 988 and miles_traveled< 1062:
        print("YOU ARRIVED AT FORT BRIDGER")
        fort()
        milestone = input("WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE") 
        if milestone == 2: 
            miles_traveled == 989
            Continue()    
        else:
            miles_traveled == 989
            rest()
                
                
    if miles_traveled > 1150 and miles_traveled< 1220:
        print("YOU ARRIVED AT THE GREEN RIVER CROSSING.")
        milestone = input("WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE")    
        if milestone == 2: 
           miles_traveled == 1151
           river()
        else:
            rest()
            miles_traveled == 1151
    if miles_traveled > 1294 and miles_traveled<1364:
        print("YOU ARRIVED AT SODA SPRINGS.")
        milestone = input("WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE")    
        if milestone == 2: 
            miles_traveled == 1295
            Continue()    
        else:
           miles_traveled == 1295
           rest()
    if miles_traveled > 1395 and miles_traveled< 1465:
        print("YOU ARRIVED AT FORT HALL.")
        fort()
        milestone = input("WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE")  
        if milestone == 2:
            miles_traveled == 1395
            Continue()    
        else:
            miles_traveled == 1395
            rest()
                
                
    if miles_traveled > 1534 and miles_traveled< 1604:
        print("YOU ARRIVED AT THE SNAKE RIVER CROSSING.")
        milestone = input("WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE")    
        if milestone == 2: 
           miles_traveled == 1534
           river()
        else:
            miles_traveled == 1534
            rest()
    if miles_traveled > 1648 and miles_traveled< 1718:
        print("YOU ARRIVED AT FORT BOISE.")
        fort()
        milestone = input("WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE")  
        if milestone == 2:
            miles_traveled == 1648
            Continue()    
        else:
            miles_traveled == 1648
            rest()
                
                
    if miles_traveled > 1807 and miles_traveled< 1877:
        print("YOU ARRIVED AT THE BLUE MOUNTAINS.")
        milestone = input("WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE")    
        if milestone == 2: 
            miles_traveled == 1808
            Continue()    
        else:
           miles_traveled == 1808
           rest()
                
    if miles_traveled > 1863 and miles_traveled< 1933:
        print("YOU ARRIVED AT FORT WALLA WALLA.")
        fort()
        milestone = input("WHAT DO YOU WANT TO DO: (1) REST (2) CONTINUE")
        if milestone == 2: 
            miles_traveled == 1863
            Continue()    
        else:
            miles_traveled == 1863
            rest()
                
    if miles_traveled > 2039:
        game_win()



def quit_game():
    '''Accepts quit parameter and updates value of quit if funtion is called'''
    global quit
    quit = 1
    print('YOU QUIT THE GAME.')
    '''Show status update?'''

def game_win():
    '''accepts quit parameter and if this function is called returns new quit parameter value'''
    global quit
    quit==2
    if quit==2:
        print("YOU HAVE SUCCESSFULLY COMPLETED THE JOURNEY TO OREGON! CONGRATULATIONS! YOU WIN! ")
        
def main():
    '''Function serves by starting the initiallization of game and executes a while loop until quit variable is updated globally to any other value than 0'''
    global quit
    welcome()
    store()
    while quit == 0:
        status_update()
        take_turn()
        misfortune()
        if raider_chance() == True:
            raider_attack()
    
    
if __name__ == '__main__':
    main()


