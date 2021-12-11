#!/bin/python3
#
# Author: Jonathan Heard
# Programs for Chapter 4, Transforming & Storing Numbers
#   with Algebra.
#
# Setting up a function definition for 2nd degree equations

# Import external function

from math import sqrt

# End of import section

# Function definition section


def quad(a, b, c):
    """This function returns both solutions an
        equation of the form a*x**2 + b*x +c = 0"""
    x1 = (-b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    return x1, x2


x = quad(2, 7, -15)


print("\nX1 =", x[0], "\n\tand\nX2 =", x[1])