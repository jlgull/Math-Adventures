#!/bin/python3
#
# Author: Jonathan Heard
# Program for Chapter 3, using conditionals to find
#   the Greatest Common Factors of 2 number
#

# Define a function to determine the GDF of any 2 entered numbers


def gcf(num1, num2):
    """ returns a list of Common Factors for num(1 & 2)
            as well as the Greatest Common Factor(GCF) """
    factorlist = []
    gcfactor = 0
    # Determine which number is largest and use it the for loop limit
    if num1 > num2:
        looper = num1
    else:
        looper = num2

    for i in range(2, looper+1):  # go from 2 to looper + 1, since all numbers
        #   are divisible by 1 start at 2
        if num1 % i == 0 and num2 % i == 0:       # if i divides into both numbers
            # evenly its a factor, so add it to the list
            factorlist.append(i)
            # if i is greater that the current GCF (gcfactor), update GCF
            if i > int(gcfactor):
                gcfactor = i
    # Rewriting the end of function to use a tuple

    return factorlist, gcfactor


# End of function definition
#
# Request numbers to be evaluated
# Use lst to hold the 2 numbers entered
#
lst = []
for i in range(0, 2):
    print("Enter number", i + 1, ":",)
    ele = int(input())
    lst.append(ele)

print("\nThe 2 numbers entered were:", lst)

# Call the function and create a Tuple for the results

GCF = gcf(lst[0], lst[1])

# Print the results of the returned tuple

if len(GCF[0]) == 1:
    print("\nThe common Factor is:", GCF[0])
else:
    print("\nThe common Factors are:", GCF[0])

print("\n\tThe Greatest Common Factor is:", GCF[1])

