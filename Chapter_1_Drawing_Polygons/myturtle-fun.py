# Using a function to make  a square

# Import section of the code
import turtle

tur = turtle.Turtle()

# from turtle import *
tur.shape('turtle')
def square():
    for i in range(4):
        tur.forward(100)
        tur.right(90)

square()

turtle.exitonclick()
