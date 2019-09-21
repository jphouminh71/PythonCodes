#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 08:52:18 2017

@author: jonathanphouminh
"""
#Task1
#Assume you have a list of numbers;
#ubmit your solutions on Moodle, under the Hmwk 3 quiz.
#list of numbers = [3, 10, 12, 17, 20, 32, 42, 66, 99 ]
#1a) Using a for loop, write a program that prints each of the numbers on a new line.
#1b) a for loop, write a program that prints each number and its square on a new line.

# 1a)for _list in [3, 10, 12, 17, 20, 32, 42, 66, 99]:
    #print(_list)
    
# 1b)
#for _list in [3, 10, 12, 17, 20, 32, 42, 66, 99]:
    #print(_list, _list ** 2)
    
#Task 2 (30 points) Write a program that asks the user to input four values:
#• the number of sides, done
#• the length of the side, done
#• the color of the perimeter, and done
#• the fill color of a regular polygon.done


#UserInputShape
number_of_sides = input("Please enter any a number of sides you want for your polygon :")
number_of_sides = int(number_of_sides)
length_of_side = input("Please enter a value that defines the length of a side: ")
length_of_side = int(length_of_side)

generated_number_of_sides = number_of_sides
generated_side_length = length_of_side
#Define the shape with motions for jamaal

                                                    #polygons all add up to 360 degrees
                                                    #minimum of 3 sides
#find algorithm for creating shapes of different polygons or create 9 working shapes
                                                       #number o
#coloroptionsForTurtle/Screen
_perimetercolor = input("What color do you want the pen to be? ")
_perimetercolor = str(_perimetercolor)
_polygonfillcolor = input("What color do you want the polygon to be? ")
_polygonifllcolor = str(_polygonfillcolor)
#ShapeCalculations











#importing the turtle function
import turtle
wn = turtle.Screen()                               #AssigningTurtleAttributes
jamaal = turtle.Turtle()
jamaal.color(_perimetercolor, _polygonfillcolor)
jamaal.begin_fill()
for square in [1,2,3,4]:        #can you assign variable to loops
    jamaal.forward(100)                          #This section will be for shape equations
    jamaal.left(90)
jamaal.end_fill()
for triangle in[1,2,3]:
    jamaal.forward(100)
    jamaal.left(60)

wn.exitonclick()
    
