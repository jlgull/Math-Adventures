#!/bin/python3
#
# Author: Jonathan Heard
# Programs for Chapter 4, Transforming & Storing Numbers
#   with Algebra.
#
# Setting up a function definition for all 1st degree equations


def equation(a, b, c, d):
    """Solve all equations of the form
        ax + b = cx + d """
    return (d - b) / (a - c)


# End of function difinition.

x = equation((1/2), (2/3), (1/5), (7/8))

print("x =", x)

leftside = (1/2) * x + (2/3)
rightside = (1/5) * x + (7/8)

print("\nLeft side  =", leftside)
print("Right side =", rightside)

print("\n\tDifference is =", leftside - rightside)