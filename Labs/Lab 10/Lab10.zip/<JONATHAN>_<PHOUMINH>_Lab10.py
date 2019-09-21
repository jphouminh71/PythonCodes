# Jonathan Phouminh
# Akshit Arora
# CS1200

import random
import dice 
import player

def take_turn(human, computer, COMPUTER_HOLD): # you might need to change the parameter(s) for this function
    turn_total = 0
    while True:
        amount = roll_die()
        print('You rolled a %i' % amount)
        turn_total += amount 
        if amount == 1:
            return amount
        else:
            total_str = 'Your turn total is ' + str(turn_total)
            print(total_str)
            if not human.get_is_next() == True and turn_total >= COMPUTER_HOLD:
                return turn_total
            elif human.get_is_next() == True:
                again = input('Do you want to roll again (Y/N)? ')
                if again.lower() == 'n':
                    return turn_total

def roll_die(): # you can keep this function, or just use a call to the roll() method of the dice object
    return random.randint(1, 6)

def get_next_player(human, computer): # you might need to change the parameter(s) for this function
    if human.get_is_next() == True:
        human.set_is_next(False)
  
    else:
        human.set_is_next(True)

def report_points(user_total, computer_total): # you might need to change the parameter(s) for this function
    print('Human: %i' % computer_total)
    print('Computer: %i' % user_total)
    print()

def print_current_player(human): # you might need to change the parameter(s) for this function
    if human.get_is_next() == True:
        print("It is now the user's turn")
        print()
    else:
        print("It is now the computer's turn")
        print()

def main():
    GAME_END_POINTS = 100
    
    COMPUTER_HOLD = 10
    
    is_user_turn = True
    
    print('Welcome to Jeopardy Dice!')
    print()
    
    # create a dice object
    
    # create an instance of a player object for the human player and an instance of a player object for the computer player. You must supply initial values for the 4 attributes of the player object. Note: for the human player, for the hold_value, it is ok to use the GAME_ENDS_POINTS variable above.
    human = player.Player(True, True, 0, GAME_END_POINTS)
    computer = player.Player(False, False, 0, COMPUTER_HOLD)    
  
    # keep this while loop for game turns but replace variables like user_total or computer_total with appropriate calls to methods that would return these values from the values of a player object attribute
    while human.get_total_score() < GAME_END_POINTS and computer.get_total_score() < GAME_END_POINTS:
       
        print_current_player(human)

        # keep on playing. Our advice: keep the functions created by this solution, but you might need to change the parameters passed to functions
        points = take_turn(human, computer, COMPUTER_HOLD)
        if not human.get_is_next():
            human.total_score += points
        else:
            computer.total_score += points
        report_points(human.total_score, computer.total_score)
        get_next_player(human, computer)
    
    if human.total_score >= GAME_END_POINTS:
        print('Congratulations! User won this round of jeopardy dice!' )
    else:
        print('Congratulations! Computer won this round of jeopardy dice!')
#modify function take turn
 #modify line 76

if __name__ == '__main__':
    main()