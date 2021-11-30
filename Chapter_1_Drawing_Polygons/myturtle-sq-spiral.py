#!/bin/python3
# Created by Jonathan Heard
#
# Program to make a rotating and growing square sprial

#   using 2 functions and looping
#
# Import module Section and assign short name

import turtle

tur = turtle.Turtle()
tur.shape('turtle')
tur.speed(5)

# End of import section

# Function creation section
# Create a function to draw squares


def square(length):
    for i in range(4):
        tur.forward(length)
        tur.right(90)


# Create a function to draw growing square spiral


def spiral_squares(side):
    for i in range(60):
        square(side)
        tur.right(5)
        print("Iteration: ", (i + 1), "Side length: ", side)
        side += 5


# End of square function creation section

# Call to function to create spiral squares

spiral_squares(5)

# End of call

# A wait a click to end the program

turtle.exitonclick()
