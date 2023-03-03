"""
A game of rock paper scissors. 
"""

import random

scorep = 0
scorec = 0
namep = input("How may I call you: ")
print()
namec =  random.choice(["Tommy", "Eric", "James", "John", "Jeff", "Nicholas", "David", "Thomas", "Charles", "William", "Daniel"])
print("Welcome to rock, paper, scissors, " + namep + ". You can quit anytime during the game by typing: quit")
print()
print("Let the game begin, you are up against: " + namec)
while True:
    player = input("What is your choice: ")
    comp = random.choice(["rock", "paper", "scissors"])
    if player == "quit":
        if scorep > scorec:
            print("Quitting rock, paper, scissors. Your final score is: " + namep + ": " + str(scorep) + " to " + namec + ": " + str(scorec) + ". You Win! Thanks for playing!")
        if scorep < scorec:
            print("Quitting rock, paper, scissors. Your final score is: " + namep + ": " + str(scorep) + " to " + namec + ": " + str(scorec) + ". " + namec + " wins! Thanks for playing!")
        if scorep == scorec:
            print("Quitting rock, paper, scissors. Your final score is: " + namep + ": " + str(scorep) + " to " + namec + ": " + str(scorec) + ". It's a tie! Thanks for playing!")
        exit()
    if player not in ["rock", "paper", "scissors"]:
        print("You have entered: " + player + ". Please enter one of these 3 words: rock, paper, scissors.")
    if player == comp:
        print("You chose: " + player + " \\\ " + namec + " chose: " + comp)
        print("You both chose: " + player + ", it's a tie!")
        print("The current score is " + namep + ": " + str(scorep) + " to " + namec + ": " + str(scorec))
    if player == "rock" and comp == "paper":
        print("You chose: " + player + " \\\ " + namec + " chose: " + comp)
        print("Paper beats rock, " + namec + " wins!")
        scorec = scorec + 1
        print("The current score is " + namep + ": " + str(scorep) + " to " + namec + ": " + str(scorec))
    if player == "rock" and comp == "scissors":
        print("You chose: " + player + " \\\ " + namec + " chose: " + comp)
        print("Rock beats scissors, " + namep + " wins!")
        scorep = scorep + 1
        print("The current score is " + namep + ": " + str(scorep) + " to " + namec + ": " + str(scorec))
    if player == "paper" and comp == "rock":
        print("You chose: " + player + " \\\ " + namec + " chose: " + comp)
        print("Paper beats rock, " + namep + " wins!")
        scorep = scorep + 1
        print("The current score is " + namep + ": " + str(scorep) + " to " + namec + ": " + str(scorec))
    if player == "paper" and comp == "scissors":
        print("You chose: " + player + " \\\ " + namec + " chose " + comp)
        print("Scisscors beats paper, " + namec + " wins!")
        scorec = scorec + 1
        print("The current score is " + namep + ": " + str(scorep) + " to " + namec + ": " + str(scorec))
    if player == "scissors" and comp == "rock":
        print("You chose: " + player + " \\\ " + namec + " chose: " + comp)
        print("Rock beats scissors, " + namec + " wins!")
        scorec = scorec + 1
        print("The current score is " + namep + ": " + str(scorep) + " to " + namec + ": " + str(scorec))
    if player == "scissors" and comp == "paper":
        print("You chose: " + player + " \\\ " + namec + " chose: " + comp)
        print("Scissors beats paper, " + namep + " wins!")
        scorep = scorep + 1
        print("The current score is " + namep + ": " + str(scorep) + " to " + namec + ": " + str(scorec))