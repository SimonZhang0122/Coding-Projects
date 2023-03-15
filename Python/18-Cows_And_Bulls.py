"""
Randomly generate a 4-digits number and ask the user to guess it. 
For every digit that the user guessed correctly in the correct place, they have a “cow”.
For every digit the user guessed correctly in the wrong place is a “bull.”
Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
Once the user guesses the correct number, the game is over.
Keep track of the number of guesses the user makes throughout the game and tell the user at the end.
"""

import random

def no_rep_num_gen(leng):
    size = 0 
    num = []
    while size <= leng:
        rand = random.randint(0, 9)
        if size < 1:
            num.append(rand) 
            if rand not in num:
                num.append(rand)
        final = ''.join(str(i) for i in num)
        size = len(final) + 1
    return final

def comparator(user, target):
    usr = str(user)
    tgt = str(target)
    cows = 0
    bulls = 0
    pos = 0
    size = len(tgt)
    while pos < size:
        if usr[pos] == tgt[pos]:
            cows = cows + 1
        if usr[pos] != tgt[pos] and usr[pos] in tgt:
            bulls = bulls + 1
        pos = pos + 1
    print("Cows: " + str(cows) + "  Bulls: " + str(bulls))
    return cows

def main():
    size = int(input("How many digits do you want to guess: "))
    inp_t = no_rep_num_gen(size)
    inp_u = 0
    attemps = 0
    while True:
        inp_u = int(input("Place your " + str(size) + " digit guess, no repeating numbers: "))
        cow = comparator(user = inp_u, target = inp_t)
        print(inp_t, inp_u)
        if cow != size:
            attemps = attemps + 1
            
        if cow == size:
            attempts = attemps + 1
            print("Congratulation, you guessed the number in " + str(attempts) + " tries!")
            break

main()