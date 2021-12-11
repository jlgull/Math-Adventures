#!/bin/python3
#
# Author: Jonathan Heard
# Programs for Chapter 4, Transforming & Storing Numbers
#   with Algebra.
#
# Function Definition Section
#
#   Define function to use brute force to solve an
#   a 3rd degree equation


def g(x):
    return 6*x**3 + 31*x**2 + 3*x - 10


def plug():
    x = -100 # Set the lower limit for x
    while x < 100: # set the upper limit of x
        if g(x) == 0: # use the if statement for the equation
            print("When x =", x, "then g(x) =", g(x))
            # print the results
        x += 1 # increment x until the answer is received
    print("done.")

# End of function definition

# Execute the function

plug()
