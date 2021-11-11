#!/bin/python3
#
# Author: Jonathan Heard
# Program for Chapter 3, using conditionals to
#   create a wandering turtle, inside of a 200 x 200 box.
#

# Import section of the code.

# Import the turtle module

import turtle

# Import the random module

from random import randint

# End of import section.

# Assign handle for turtle module

tur = turtle.Turtle()

# End of assignment section.

# Assign shape and speed to turtle

tur.shape('turtle')
tur.speed(0)


# Define wander function


def wander():
    while True:
        tur.fd(3)
        if tur.xcor() >= 200 or tur.xcor() <= -200 or tur.ycor() >= 200 or tur.ycor() <= -200:
            tur.rt(randint(90,180))

# End of wander function

# Draw a box 400 X 400

tur.fd(200)
tur.rt(90)
tur.fd(200)
tur.rt(90)
tur.fd(400)
tur.rt(90)
tur.fd(400)
tur.rt(90)
tur.fd(400)
tur.rt(90)
tur.fd(200)
tur.rt(90)
tur.fd(200)
tur.rt(180)

# Call wander function to fill in the box

wander()


# wait for click to exit
tur.exitonclick()
