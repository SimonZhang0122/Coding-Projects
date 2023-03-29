"""
Making a game of Hangman, project 30 - 31.
Part 1, 30 - write a function that picks a random word from a list of words from the SOWPODS dictionary.
part 2, 31 - write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly.
Part 3, 32 - add logic for handling guesses, the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms) before they lose the game.
             keep track of the letters the user guessed. If the user guesses a letter they already guessed, don’t penalize them - let them guess again.
             when the player wins or loses, let them start a new game.
             rather than telling the user "You have 4 incorrect guesses left", display some picture art for the Hangman.
"""

def wordPicker():
    import random
    wordlist = []
    leng = 0
    with open("30-sowpods.txt", "r") as wordfile:
        word = wordfile.readline().strip()
        while word:
            wordlist.append(word)
            leng += 1
            word = wordfile.readline().strip()
    pos = random.randint(0, leng - 1)
    return wordlist[pos]

def guesser():
    display = []
    word = []
    matched = []
    dup = []
    tries = 6
    l = 1
    for c in wordPicker():
        word.append(c)
    print(word)
    while l <= len(word):
        display.append("_")
        l += 1
    print("  ".join(display), end = visual(tries))
    while tries > 0:
        i = 0        
        usr = input("\n\n>>>Guess a letter: ").upper()
        dup.append(usr)
        if dup.count(usr) > 1:
            print("\n    --- You already tried: \'" + usr + "\' ---")
            print("  ".join(display), end = visual(tries))
        elif(
                len(usr) > 1 or
                "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ".find(usr) == -1 or
                usr == '' or
                usr == " "
            ):
            print("\n    ---INVALID INPUT! Please input a single letter.---")
            print("  ".join(display), end = visual(tries))
        elif usr not in word:
            tries -= 1
            print("\n    ---Wrong guess! You have " + str(tries) + " incorrect guesses left.---")
            print("  ".join(display), end = visual(tries))
        else:
            while i < len(word):
                if usr == word[i]:
                    matched.append(i)
                i += 1
            for i in matched:
                display[i] = usr
            matched.clear()
            print("\n    ---Good guess!---")
            print("  ".join(display), end = visual(tries))
        if display == word:
            print("\n    ---CONGRATULATION! You guessed the word!---\n")
            return
    else:
        print("    ---GAME OVER! You didn't guess the word---\n")
        print("The word was: " + " ".join(word)) 
        return


def visual(tries):
    hangman = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    print(hangman[tries])

def main():
    print("Welcome to the Hangman game!\nYou have 6 chances to guess the randomly selected word, good luck!\n")
    guesser()    
    while True:
        inp = ""
        inp = input("\nWould you like to play again(Y/N): \n").upper()
        while inp not in ["Y", "N"]:
            print("\n--Invalid input, please type 'y' or 'n'--\n")
            inp = input("\nWould you like to play again(Y/N): \n").upper()
        if inp == "Y":
            guesser()
        else:
            print("\nExiting Hangman, thanks for playing!\n")
            exit()

main()