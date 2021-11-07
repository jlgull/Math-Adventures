#!/bin/python3
#
# Author: Jonathan Heard
# Program for Chapter 3, using conditionals to find
#   the Greatest Common Factors of 2 number
#

# Define a function to determine the GDF of any 2 entered numbers


def gcf(num1, num2):
    """ returns a list of common factors for num(1 & 2)
        as well as the Greatest Common Factor(GCF) """
    factorlist = []
    gcfactor = 0
    # Determine which number is largest and use it the for loop limit
    if num1 > num2:
        looper = num1
    else:
        looper = num2

    for i in range(2, looper+1):  # go from 2 to looper + 1, since all numbers
        #   are divisible by 1
        if num1 % i == 0 and num2 % i == 0:       # if i divides into either numbers
            # evenly its a factor, so add it to the list
            factorlist.append(i)
            # if i is greater that the current GCF, update GFF
            if i > int(gcfactor):
                gcfactor = i
    # This was commented out, since I couldn't figure out how to split the
    #   2 returned values.
    # finally return the 2 factor lists
    # return factorlist,gcfactor
    #
    # This was moved from the function call section, since I could figure out
    #   how to split 2 returned values. I simply added to print section section
    #   to the function.

# If there is no GCF, then there are not common Factors as well
    if gcfactor == 0:
        print("\nThere are no common Factors and no GCF!")
    else:
        # added test to control the (s) at the end of factor
        if len(factorlist) == 1:
            print("\nThe common Factor is:", factorlist)
        else:
            print("\nThe common Factors are:", factorlist)
        # Print out the GCF
        print("\nThe Greatest Common Factor (GCF) is:", gcfactor)


# End of function definition
#
# Request numbers to be evaluated
# Use lst to hold the 2 numbers entered
#
lst = []
for i in range(0, 2):
    print("Enter number", i + 1)
    ele = int(input())
    lst.append(ele)

print("\nThe 2 numbers entered were:", lst)

# Call the gcf function to execute it.
gcf(lst[0], lst[1])

# Since I couldn't figure out to split the 2 returned values, I move the print
#   function inside the actual gcf function
# print("\nThe common factors are in []'s and the GCF is after the ,:", gcf(pass1, pass2))
