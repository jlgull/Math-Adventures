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
        print("Hello", name.title())
    return name


def numberGame():
    # Pick a random number between 1 and 100
    number = randint(1, 100)
    # return number

# Get a user's guess for the number being thought of

    player = greet()
    print(player.title(), ", I'm thinking of a number between 1 and 100.")
    guess = int(input("What is your guess? "))
    attempt = 1

# test the results of the guess against the random number

# begin loop to ask until the guess is correct
    while guess:
        if number == guess:
            print("\n", player.title(), "that is correct! The number was", number)
            print("\t You guessed it right in", attempt, "trys.")
            break
        elif number > guess:
            print("Nope! Try higher.")
        else:
            print("Nope! Try lower.")
        guess = int(input("What is your new guess? "))
        attempt += 1

# End of Definition Section

# Playing the game, using the function

numberGame()

# Get a user's guess for the number being thought of

