# Using a function to make a star

# Import section of the code
import turtle

tur = turtle.Turtle()

# from turtle import *
tur.shape('turtle')
tur.speed(1)

# Define a star function


def star(length):
    for i in range(5):
        tur.forward(length)
        tur.right(144)


# Draw a star, with the turtle ending in the middle
#   of the horizontal line

side_length = int(input("Enter the length of the stars long side: "))


tur.backward(side_length/2)
star(side_length)
tur.forward(side_length/2)

turtle.exitonclick()
