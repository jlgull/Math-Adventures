#!/bin/python3
#
# Author: Jonathan Heard
# Program for Chapter 3, using conditionals to find factors of a number
#

# Define a function to determine factors of an entered number


def factor(num):
    """ returns a list of factors for num """
    factorlist = []
    for i in range(2, num+1):  # go from 2 to num + 1, all numbers
        #   are divisible by 1
        if num % i == 0:       # if i divides into num evenly
            # its a factor, so add it to the list
            factorlist.append(i)
    # finally return the factor list
    return factorlist


# End of function definition

# Request number to be evaluated

enteredValue = int(input("Enter number to find factors for: "))

# Test the length of the list of returned factors,
#   if only one number, print factor. If > 1 print factors

if len(factor(enteredValue)) == 1:
    print("\n\t", enteredValue, "is a Prime Number, its only factor is:", enteredValue)

else:
    print("\nThe factors for", enteredValue, "are:", factor(enteredValue))
    print("\n\t", enteredValue, "is NOT a Prime Number")
