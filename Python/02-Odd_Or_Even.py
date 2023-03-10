"""
Asks the user for a number. Depending on if the number is even or odd, print out a message.
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

num = int(input("Please give me a number: "))
check = int(input("Please give a number to divide by: "))
mod = num % 2
if num == 0:
    print("Please give a number other than 0.")
elif num % 4 == 0:
    print("This number is a multiple of 4.")
elif mod == 0:
    print("This given number is a even number.")
elif mod == 1:
    print ("This number is a odd number.")
    
try:
    print("Dividing " + str(num) + " by " + str(check))
except:
    print("The number to divide by doesn't exist.")
else:
    if num % check == 0:
        print("The second number divides evenly into the first number.")
    else:
        print("The second number doesn't divide evenly into the first number with a remainder of " + str(num % check))
