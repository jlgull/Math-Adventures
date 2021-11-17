#!/bin/python3
#
# Author: Jonathan Heard
# Program for Chapter 3, create a functions to
#   approximate the square root of a number using
#   the same concepts as used in the number guessing game.
#
#
# Function Definition Section


# Calculate the average of 2 numbers passed to the function

def average(a, b):
    return (a + b) / 2

def squareRoot(num):
    """Finds the square root of num by playing
    the Number Guessing Game strategy
    by guessing over the range from "low = 1 " to "high = num" """
    low = 1
    high = num
    done = False
    for i in range(100):
        guess = average(low, high)
        if guess ** 2 == num:
            print("\nSince the Square Root of", num, "is not irrational")
            print("\tthen the perfect Square Root is:", guess)
            done = True
            break
        elif guess ** 2 > num:
            print(guess, "is high at try", i, "guess Lower.")
            high = guess
        else:
            print(guess, "is low at try", i, "guess Higher.")
            low = guess
    if done is False:
        print("\nThe best approximation for the Square root of", num, "is:", guess)
        print("\tThe Square of the final guess is", guess ** 2)

squareRoot(640)
