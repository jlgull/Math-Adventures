#!/bin/python3
#   Author: Jonathan Heard
#
# The start of a mathematics set of functions

# Define a function to calculate the average of 2 numbers


def average1(a, b):

    return (a + b) / 2


# End of function definition
# Use function to calculate an average

print("Average of 10 and 20 is", average1(10, 20))

# Define a new function to use a loop for summation


def mysum(num):
    running_sum = 0
    for i in range(1, num+1):
        running_sum += i
    return running_sum


# End of definition

# Define a new function n**2 + 1


def mysum2(num):
    running_sum = 0
    for i in range(num+1):
        running_sum += i**2 + 1
    return running_sum


# End of definition


# Define a new function to average a list of numbers


def average3(numlist):
    return sum(numlist)/int(len(numlist))


# End of definition


# Request the final number for the summation

num = int(input("Enter the number to sum to: "))

# Print the results of simple summation

print("Results of summing 1 to", num, "is", mysum(num))

# Print the results of summing (i^2 + 1)

print("Result of summing (i^2 + 1) from 0 to", num, "is", mysum2(num))

# Using a try block to handle entering integers for a list,
#   exit the enter when an exception occurs.
try:
    lista = []

    while True:
        lista.append(int(input("Enter Numbers, blank to end: ")))

except:

    # if the input is not-integer, then print the list and the average

    print("The average of", lista, "is",  average3(lista))

# End of program
