#!/bin/python3
#
# Author: Jonathan Heard
# Program for Chapter 3, using conditionals to
#   create a number guessing game.
#

# Import section of the code.

from random import randint

# Function Definition Section


def greet():
    name = input("Please enter your name: ")
    if name == "Jonathan":
        print("Hey, that's my name!")
    else:
        print("Hello", name)
    return name


def numberGame():
    # Pick a random number between 1 and 100
    number = randint(1,100)
    # return number

# Get a user's guess for the number being thought of

    print("\n", greet(), " I'm thinking of a number between 1 and 100.")
    guess = int(input("What is your guess? "))

# test the results of the guess against the random number

    if number == guess:
        print("\nThat is correct! The number was", number)
    elif number > guess:
        print("\nNope! Your guess was to low.")
    else:
        print("\nNope! Your guess was to high.")


# Playing the game, using the function


numberGame()

# Get a user's guess for the number being thought of

