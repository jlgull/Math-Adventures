#!/bin/python3
#
# Author: Jonathan Heard
# Program for Chapter 3, about conditionals

# Get age from user
age = int(input("Enter your age: "))

# Using if, elif and else to print various items.

if age <= 10:
    print("What school do you attend?")
elif 11 <= age < 20:
    print("You are cool!")
elif 20 <= age < 30:
    print("What job do you have?")
elif 30 <= age < 40:
    print("Are you married?")
else:
    print("Wow, you're old!!")
