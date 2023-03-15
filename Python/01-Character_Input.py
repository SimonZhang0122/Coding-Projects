"""
Asks the user for their name and age and print out a message addressed to them that tells them what year they will turn 100. 
"""

import datetime

name = input("What is your name: ")
age = int(input("How old are you: "))
today = datetime.datetime.now()

ageyear = str(100 - age + int(today.strftime("%Y")))

print("Hello " + name + ", you will be 100 years old in " + ageyear)