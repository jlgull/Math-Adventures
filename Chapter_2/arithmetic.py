#!/bin/python3
#   Author: Jonathan Heard
#
# The start of a mathematics set of functions

# Define a function to calculate the average of 2 numbers


def average(a, b):

    return (a + b) / 2


# End of function definition
# Use function to calculate an average

print("Average of 10 and 20 = ", average(10, 20))

# Define a new function to use a loop for summation


def mysum(num):
    running_sum = 0
    for i in range(1, num+1):
        running_sum += i
    return running_sum


# End of definition

# Request a number so sum to

num = int(input("Enter the number to sum to: "))

# mysum(num)

Summation = mysum(num)

print("Results of summing 1 to ", num, "is ", Summation)
# Print results of the Summation
# print("Sum of 1 to :", num, "is", running_sum)
