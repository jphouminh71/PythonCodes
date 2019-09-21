# JONATHAN PHOUMINH
# CSCI 1200
# HOMEWORK 3
# SEPTEMBER 24, 2017

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 12:18:54 2017

@author: jonathanphouminh
"""
#Task1
#Assume you have a list of numbers;
#ubmit your solutions on Moodle, under the Hmwk 3 quiz.
#list of numbers = [3, 10, 12, 17, 20, 32, 42, 66, 99 ]
#1a) Using a for loop, write a program that prints each of the numbers on a new line.
#1b) a for loop, write a program that prints each number and its square on a new line.

#1a)

for _list in [3, 10, 12, 17, 20, 32, 42, 66, 99]:
    print(_list)
    
#1b)

for _list in [3, 10, 12, 17, 20, 32, 42, 66, 99]:
    print(_list, _list ** 2)
    
                                    #done
#                                   Task 2
#Write a program that asks the user to input four values:
#• the number of sides, done
#• the length of the side, done
#• the color of the perimeter, and done
#• the fill color of a regular polygon.done

 
import turtle                                   #header

def drawSquare(_SCREENcolor, turtle, _PENcolor, _SHAPEcolor, _NUMsides, _LENGTHsides,  ):
    '''This function just be used to draw square'''
    wn = turtle.Screen()
    wn.bgcolor(_SCREENcolor)
    alex = turtle.Turtle()
    alex.color(_PENcolor, _SHAPEcolor)
    alex.begin_fill()
    for i in range(_NUMsides):
        alex.forward(_LENGTHsides)
        alex.left((360/_NUMsides))
    alex.end_fill()
    wn.exitonclick
    
    
        
def main():
    '''use this function only to call other functions with given attributes'''
    _numberofsides = input("How many sides do you want your polygon to be?: ")
    _NUMsides = int(_numberofsides)
    _lengthofsides = input("How long do you want each side to be, (units), ?: ")
    _LENGTHsides = int(_lengthofsides)
    _perimetercolor = input("What color do you want your pen to be? :")
    _PENcolor = str(_perimetercolor)
    _polygonfillcolor = input("What color do you want your polygon to be?: ")
    _SHAPEcolor = str(_polygonfillcolor)
    _bgcolor = input("What color do you want the background to be?: ")
    _SCREENcolor = str(_bgcolor)
    drawSquare(_SCREENcolor, turtle, _PENcolor, _SHAPEcolor,_NUMsides, _LENGTHsides, )
    
main()
    

                                    #DONE
                                    
                                    #TASK 3 1A
                                    # draw a “house”
                                    #the length of each segment of the house was 50.
import turtle

def drawTriangle_Square(turtle, size, speed):
    '''This function draws the house in with two turtle motions.'''
    turtle.speed(speed)
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.speed(speed)
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
        
def main():
    wn = turtle.Screen()
    alex = turtle.Turtle()
    drawTriangle_Square(alex, 50, 5)
    wn.exitonclick()
main()    
    
                                    #Task 3 1B
                                    #modify the house
                                    #adding a second house
                                    
                                   
import turtle

def drawTriangle(turtle, size, speed):
    '''This function draws the house in with two turtle motions.'''
    turtle.speed(speed)
    turtle.color("black","tan")
    turtle.begin_fill()
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()
    turtle.speed(speed)
def drawSquare(turtle, size, speed):
    turtle.speed(speed)
    turtle.color("black","darkgrey")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()
def drawSecondTriangle(turtle, size, speed):
    turtle.speed(speed)
    turtle.penup()
    turtle.forward(50)
    turtle.pendown()
    turtle.color("black", "lightblue")
    turtle.begin_fill()
    
    for i in range(3):
        turtle.forward(size)
        turtle.left(120)
    turtle.end_fill()
    turtle.speed(speed)

def drawSecondSquare(turtle, size, speed):
    turtle.speed(speed)
    
  
    turtle.pendown()
    turtle.color("black","black")
    turtle.begin_fill()
    for i in range(4):
        turtle.forward(size)
        turtle.right(90)
    turtle.end_fill()
def main():
    '''This function will draw the first house'''
    wn = turtle.Screen()
    alex = turtle.Turtle()
    drawTriangle(alex, 50, 10)
    
    drawSquare(alex, 50, 10)
    
    wn.exitonclick()
def main2():
    '''This function will draw the second house'''
    jamaal = turtle.Turtle()
    
    drawSecondTriangle(jamaal, 50, 10)
    drawSecondSquare(jamaal, 50, 10)
    
main()    
main2()
                                #Extra Credit Attempt
                                



import turtle 

def Draw1(_sidelength)




def main():
    wn = turtle.Screen()
    alex = turtle.Turtle()
    

alex.forward(5)
alex.left(90)
    
    
    
    





