#!/bin/python3
# Created by Jonathan Heard
#
# Program to make a star based spiral
# Using 2 functions to make a star based spiral
#   2nd function uses looping to make the spiral.
#
# Import module Section and assign short name

import turtle

tur = turtle.Turtle()
tur.shape('turtle')
tur.speed(5)

# End of import section

# Using 2 functions to make a star based spiral


# Define all functions
# Basic Star first


def star(length):
    for i in range(5):
        tur.forward(length)
        tur.right(144)


# Star Spiral of growing stars.


def spiral_star(side):
    for i in range(60):
        star(side)
        tur.right(5)
        print("Iteration: ", (i + 1), "Side length: ", side)
        side += 5


# End of function creation section

# Call to function to create star spiral

spiral_star(5)

# End of call

# Wait for a click to end the program

turtle.exitonclick()
