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

x = equation(12, 18, -34, 67)

print("x =", x)

leftside = 12 * x + 18
rightside = -34 * x + 67

print("\nLeft side  =", leftside)
print("Right side =", rightside)

print("\n\tDifference is =", leftside - rightside)