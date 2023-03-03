import random
tries = 0
print("Welcome to the guessing game!")
range1, range2 = input("What is the range of the number you wanna guess from(type low_range top_range): ").split()
print("You choosed to guess from " + range1 + " to " + range2 + "." + " To quit the game type: quit.")
print()
choice = input("Do you want to guess a whole number or a decimal number(type whole / decimal): ")
if choice == "whole":
    rand = int(random.randint(int(range1), int(range2)))
    print("You've chosen to guess a random whole number ranging from " + range1 + " to " + range2)
if choice == "decimal":
    print("You've chosen to guess a random decimal number ranging from " + range1 + " to " + range2)
    dec = int(input("how many decimal places do u want the random number to have: "))
    rand =  round(random.uniform(int(range1), int(range2)) , dec) 
    
while choice == "decimal":
    inp = input("Please guess your number in " + str(dec) + " decimal places: ")
    if inp == "quit":
        print("Exiting the game, " + str(rand) + " was the right number, you've tried a total of " + str(tries) + " times. Thanks for playing!")
        exit()
    if float(inp) == rand:
        tries = tries + 1
        print("Congratulation! " + str(rand) + " is the right number! You've tried a totoal of " + str(tries) + " times. Thanks for playing!")
        exit()
    if inp is not float:
        print(inp + " is not a float, please input a float.")
    if float(inp) < float(range1) or float(inp) > float(range2):
            tries = tries + 1
            print("Your guess is out of range, the random number is higher than " + range1 + " and smaller than " + range2 + ".")
    if float(inp) > rand and float(inp) < float(range2) and float(inp) > float(range1):
        tries = tries + 1
        print("Your guess is higher than the random number, try a number smaller than " + str(inp) + ".")
    if float(inp) < rand and float(inp) < float(range2) and float(inp) > float(range1):
        tries = tries + 1
        print("Your guess is lower than the random number, try a number bigger than " + str(inp) + ".")
        
while choice == "whole":
    inp = input("Please input your guess as an interger: ")
    if inp == "quit":
        print("Exiting the game, " + str(rand) + " was the right number, you've tried a total of " + str(tries) + " times. Thanks for playing!")
        exit()
    if int(inp) == rand:
        tries = tries + 1
        print("Congratulation! " + str(rand) + " is the right number! You've tried a totoal of " + str(tries) + " times. Thanks for playing!")
        exit()
    if inp is not int:
        print(inp + " is not an interger, please input a whole number.")
    if int(inp) < int(range1) or int(inp) > int(range2):
            tries = tries + 1
            print("Your guess is out of range, the random number is higher than " + range1 + " and smaller than " + range2 + ".")
    if int(inp) > rand and int(inp) < int(range2) and int(inp) > int(range1):
        tries = tries + 1
        print("Your guess is higher than the random number, try a number smaller than " + str(inp) + ".")
    if int(inp) < rand and int(inp) < int(range2) and int(inp) > int(range1):
        tries = tries + 1
        print("Your guess is lower than the random number, try a number bigger than " + str(inp) + ".")