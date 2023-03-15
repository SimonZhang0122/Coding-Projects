import math
def main():
    global tgt
    tgt = int(input("Think of a number between 0 to 100: "))
    if tgt < 0 or tgt > 100:
        print("Invalid target, number must be between 0 and 100 inclusively")
        tgt = int(input("Think of a number between 0 to 100: "))
    guessing(tgt)

def guessing(tgt):
    global attmps
    global guess
    attmps = 2
    guess = 50
    if tgt == 0:
        print("Your number must be 0, 1 attempt taken.")
        exit()
    elif tgt == 50:
        print("Your number must be 50, 1 attempt taken.")
        exit()
    elif tgt == 100:
        print("Your number must be 100, 1 attempt taken.")
        exit()
    while tgt != guess:
        usr = input("Is your number lower or higher than: " + str(guess) + "\n")        
        if usr == "higher":
            guess = guess + math.ceil(100 / 2 ** attmps)
            attmps = attmps + 1
        if usr == "lower":
            guess = guess - math.ceil(100 / 2 ** attmps)
            attmps = attmps + 1
        if guess < 0 or guess > 100:
            print("invalid guess, number must be between 0 and 100 inclusively.")
            guess = 50        
        if usr != "lower" and usr != "higher":
            print("Invalid input, please type: 'lower' or 'higher'")
    else:
        print("Your number must be: " + str(guess) + ", " + str(attmps - 2) + " attempts taken.")
        
main()