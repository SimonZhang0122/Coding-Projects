"""
Using function, ask the user for a number and determine if it's a prime number or not.
"""

def is_prime(num):
    i = 0
    divs = []
    while num >= i:
        i = i + 1
        if num % i == 0:
            divs.append(i)
    return divs

ans = is_prime(int(input("What is your number: ")))
print(ans)
