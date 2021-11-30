#!/bin/python3
#
# Author: Jonathan Heard
# Programs for Chapter 4, Transforming & Storing Numbers
#   with Algebra.
#
# Function Definition Section
#
#   Define function to use brute force to solve an equation


def plug():
    x = -100 # Set the lower limit for x
    while x < 100: # set the upper limit of x
        if 2*x + 5 == 13: # use the if statement for the equation
            print("When x =", x, ", you have solved the equation.")
            # print the results
        x += 1 # increment x until the answer is received


# End of function definition

# Execute the function

plug()
