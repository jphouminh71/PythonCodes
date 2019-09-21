#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  1 17:30:43 2017

@author: jonathanphouminh
"""

#           Homework 4

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
    joe = turtle.Turtle()
    jane = turtle.Turtle()
    
    JaneStart(jane, -77.5, 240)
    JoeStart(joe,77.5,240)
    JoeStart
    StartingLineTurtle = turtle.Turtle
    WritingTurtle = turtle.Turtle
    DashDrawingTurtle = turtle.Turtle
    
    '''calling the actual functions to draw the grid'''
    drawLine(StartingLineTurtle, -240, 240, 500)
    writeText(WritingTurtle, -270, 240, "START")
    drawDashLine(DashDrawingTurtle, -240, 215, 25,10)
    
    
    ''' Creating the turtles that will actually be racing'''
    #joe = turtle.Turtle()
    #jane = turtle.Turtle()
    #JaneStart(jane, -77.5, 240)
    #JoeStart(joe,77.5,240)
    
    
main()