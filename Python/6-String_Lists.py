"""
Asks the user for a word then print out whether the word is a palindrome or not.
"""

import math

inp = input("What is the words: ")
leng = len(inp)
if leng % 2 == 0:
    half2 = str(inp[int(leng /2) :] [::-1])
    half1 = inp[:int(leng/2)]
    if half1 == half2:
        print(half1 + " = " + half2 + " :" + inp + " is a palindrome.")
    else:
        print(half1 + " ≠ " + half2 + " :" + inp + "is NOT a palindrome.")
if leng % 2 != 0:
    half22 = str(inp[math.floor(leng/2):] [::-1])
    half21 = inp[:(math.floor(leng/2) + 1)]
    if half22 == half21:
        print(half21 + " = " + half22 + " :" + inp + " is a palindrome.")
    else:
        print(half21 + " ≠ " + half22 + " :" + inp + " is NOT a palindrome.")