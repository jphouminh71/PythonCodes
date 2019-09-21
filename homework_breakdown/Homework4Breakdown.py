#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 15:12:16 2017

@author: jonathanphouminh
"""
#                                   HOMEWORK 4

#Homework Details: Goal = create two or more turtles and have them race down
#the screen from top to bottom, Turtle that goes the furthest wins.

#Several different and equally plausible solutions

#sequence of steps we need to accomplish include
#importing the modules
#createing a sreen
#create grid to track the progress of our turtles through the race
#create both the turtles
#send them moving down the screen

'''Task 1a'''
'''Task 1b'''


import turtle

def drawLine(t,x,y,l):
    ''' This function will draw the grid pattern'''
    wn = turtle.Screen()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(l)
    wn.exitonclick()
    
def writeText(t,x,y,text):
    '''This function writes the the string text'''
    
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.write(text)
    #turtle.forward(l)
    
    
def main():
    '''Function is used to call other functions'''
    t = turtle.Turtle
    t2 = turtle.Turtle
    drawLine(t, -240, 240, 500)
    writeText(t2, -240, 240, "text")
    
    
    
main()

'''Task 1d'''
import turtle
def drawDashLine(t,x,y,DashLength,NumDashes):
    turtle.penup()
    turtle.goto(x,y)
    for i in range(NumDashes):
        turtle.pendown()
        turtle.forward(DashLength)
        turtle.penup()
        turtle.forward(20)
    
    
    
def main():
    '''Function is used to call other functions'''
    StartingLineTurtle = turtle.Turtle
    WritingTurtle = turtle.Turtle
    DashDrawingTurtle = turtle.Turtle
    
    drawDashLine(DashDrawingTurtle, -50, 40, 10, 8)
    
    
main()
    
'''Task 1e'''

import turtle

def drawLine(t,x,y,l):
    ''' This function will draw the grid pattern'''
    wn = turtle.Screen()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(l)
    wn.exitonclick()
    
def writeText(t,x,y,text):
    '''This function writes the the string text'''
    
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.write(text)
    #turtle.forward(l)
    
def drawDashLine(t,x,y,DashLength,NumDashes):
    turtle.penup()
    turtle.goto(x,y)
    for i in range(20):
        for i in range(NumDashes):
            turtle.pendown()
            turtle.forward(DashLength)
            turtle.penup()
            turtle.forward(DashLength)
            turtle.penup()
            
        
        
        turtle.goto(x,y-20)
        
    
def main():
    '''Function is used to call other functions'''
    StartingLineTurtle = turtle.Turtle
    WritingTurtle = turtle.Turtle
    DashDrawingTurtle = turtle.Turtle
    
    
    
    
    drawLine(StartingLineTurtle, -170, 140, 500)
    writeText(WritingTurtle, -170, 140, "START")
    drawDashLine(DashDrawingTurtle, -170, 115, 25,20)
    
main()
    
#                       Task 2
import turtle

def drawLine(t,x,y,l):
    ''' This function will draw the grid pattern'''
    wn = turtle.Screen()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(l)

    
def writeText(t,x,y,text):
    '''This function writes the the string text'''
    
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.write(text)
    #turtle.forward(l)
    
def drawDashLine(t,x,y,DashLength,NumDashes):
    turtle.speed(10000)
    turtle.penup()
    turtle.goto(x,y)
    for i in range(2):
        for i in range(NumDashes):
            turtle.pendown()
            turtle.forward(DashLength)
            turtle.penup()
            turtle.forward(DashLength)
            turtle.penup()
            
        
        
        turtle.goto(x,y-20)
        
def JaneStart(t,x,y):
    '''moving jane to the starting line'''
    turtle.shape("turtle")
    turtle.color("red")
    turtle.pencolor("red")
    turtle.penup()
    turtle.right(90)
    turtle.goto(x,y)
    turtle.pendown()
    

def JoeStart(t,x,y):
    '''moving joe to the starting line'''
    turtle.shape("turtle")
    turtle.color("blue")
    turtle.pencolor("blue")
    turtle.penup()
    turtle.right(90)
    turtle.goto(x,y)
    turtle.pendown()
    

def main():
    '''Creating the turtles to sketch the grid'''
    StartingLineTurtle = turtle.Turtle
    WritingTurtle = turtle.Turtle
    DashDrawingTurtle = turtle.Turtle
    
    '''calling the actual functions to draw the grid'''
    drawLine(StartingLineTurtle, -240, 240, 500)
    writeText(WritingTurtle, -270, 240, "START")
    drawDashLine(DashDrawingTurtle, -240, 215, 25,10)
    
    
    ''' Creating the turtles that will actually be racing'''
    joe = turtle.Turtle()
    jane = turtle.Turtle()
    JaneStart(jane, -77.5, 240)
    JoeStart(joe,77.5,240)
    
    
main()

#                               Task 3
import turtle
import random

def drawLine(t,x,y,l):
    ''' This function will draw the grid pattern'''
    wn = turtle.Screen()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.forward(l)

    
def writeText(t,x,y,text):
    '''This function writes the the string text'''
    
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.write(text)
    #turtle.forward(l)
    
def drawDashLine(t,x,y,DashLength,NumDashes):
    
    turtle.penup()
    turtle.goto(x,y)
    for i in range(2):
        for i in range(NumDashes):
            turtle.pendown()
            turtle.forward(DashLength)
            turtle.penup()
            turtle.forward(DashLength)
            turtle.penup()
            
        
        
        turtle.goto(x,y-20)
        
def JaneStart(t,x,y):
    
    '''moving jane to the starting line'''
    turtle.shape("turtle")
    
    turtle.color("red")
    turtle.pencolor("red")
    turtle.penup()
    turtle.right(90)
    turtle.goto(x,y)
    turtle.pendown()
    janerandomspeed = random.randrange(100,200)
    turtle.speed(janerandomspeed)
    turtle.forward(400)
    

def JoeStart(t,x,y):
    '''moving joe to the starting line'''
    turtle.shape("turtle")
    turtle.color("blue")
    turtle.pencolor("blue")
    turtle.penup()
    turtle.right(90)
    turtle.goto(x,y)
    turtle.pendown()
    joerandomspeed = random.randrange(100,200)
    turtle.speed(joerandomspeed)
    turtle.forward(400)

def main():
    '''Creating the turtles to sketch the grid'''
    StartingLineTurtle = turtle.Turtle
    WritingTurtle = turtle.Turtle
    DashDrawingTurtle = turtle.Turtle
    
    '''calling the actual functions to draw the grid'''
    drawLine(StartingLineTurtle, -240, 240, 500)
    writeText(WritingTurtle, -270, 240, "START")
    drawDashLine(DashDrawingTurtle, -240, 215, 25,10)
    
    
    ''' Creating the turtles that will actually be racing'''
    joe = turtle.Turtle()
    jane = turtle.Turtle()
    JaneStart(jane, -77.5, 240)
    #JoeStart(joe,77.5,240)
    
    
main()







#  in my final code (Task 3) ultimately I couldn't figure out how to repeat the
# dashed line function to start under the each line and I also commented out 
# JoeStart function because whenever I ran the code it would always take out
# the turtle jane, so commented out JoeStart so the code could run. I did 
# edit the body of Joe start so that the speed would also be random number
# between 100 and 200, but I just couldn't figure out why the code couldn't
# run two turtles at one time. 
