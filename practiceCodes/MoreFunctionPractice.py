#           Homework 4

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
        
def Movingjanetostart(t,x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

def Movingjoetostart(t,x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
def main():
    '''Function is used to call other functions'''
    StartingLineTurtle = turtle.Turtle
    WritingTurtle = turtle.Turtle
    DashDrawingTurtle = turtle.Turtle
    
    
    
    
    drawLine(StartingLineTurtle, -170, 140, 500)
    writeText(WritingTurtle, -170, 140, "START")
    drawDashLine(DashDrawingTurtle, -170, 115, 25,20)
    
    
    ''' Creating the turtles that will actually be racing'''
    jane = turtle.Turtle()
    jane.color("purple","pink")
    joe = turtle.Turtle()
    joe.color("blue","black")
   
    '''Calling their functions to move them to the start'''
    Movingjanetostart(jane, -77.5, 240)
    Movingjoetostart(joe, 77.5, 240)
    
main()
    
