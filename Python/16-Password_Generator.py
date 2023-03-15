import random

def main():
    choice = input("Do you want a strong or weak password: ")
    if choice == "strong":
        leng = int(input("How many digits do you want your password to be: "))
        result = strong_gen(leng)
        print("Your new strong password is: " + result)
    if choice == "weak":
        result = weak_gen()
        print("Your new weak password is: " + result)
        
    
def strong_gen(size):
    strong = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'Z', 'X', 'C', 'V', 'B', 'N', 'M', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '?']
    pas = []
    i = 0
    while i < size:
        rand = random.randint(0, (len(strong) - 1))
        curr = strong[rand]
        pas.append(curr)
        i = i + 1
        password = ''.join(pas)
    return password

def weak_gen():
    weak = ['password', '123456', 'pass', '1234', 'enter', 'user', 'computer', 'secret']
    rand = random.randint(0, (len(weak) - 1))
    password = weak[rand]
    return password

main()
