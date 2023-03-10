"""
Asks the user for the size of a list and the range of the list(input as X Y), then print out the list and a new list with only even numbers.
"""

import random

list = []
x = 1
size = int(input("What size do you want your list to be: "))
range1, range2 = input("Please enter the ranges for your list: ").split()
while x <= size:
    rand = random.randint(int(range1), int(range2))
    list.append(rand)
    x = x + 1
print(list)
newlist  = [ a for a in list if a % 2 == 0]
print(newlist)
