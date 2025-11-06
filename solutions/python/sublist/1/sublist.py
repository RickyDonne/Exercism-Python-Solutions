"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 1
SUPERLIST = 2
EQUAL = 3
UNEQUAL = 4


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
        
    l1, l2 = len(list_one), len(list_two)
    
    if l1 != 0 and l2 == 0:
        return SUPERLIST

    if l2 != 0 and l1 == 0:
        return SUBLIST

    if l2 > l1:
        for i in range(0, l2):
            if list_one == list_two[i:i+l1]:
                return SUBLIST

    if l1 > l2:
        for i in range(0, l1):
            if list_two == list_one[i:i+l2]:
                return SUPERLIST
            

    return UNEQUAL
                    
                
                        
        
