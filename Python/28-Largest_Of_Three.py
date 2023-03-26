"""
Implement a function that takes as input three variables, and returns the largest of the three. Do this without using the Python max() function!
"""

def main():
    rawa,rawb,rawc = input("What are your numbers: ").split()
    a = int(rawa)
    b = int(rawb)
    c = int(rawc)
    print(largestOfThree(a, b, c))
    
def largestOfThree(a, b, c):
    largest = 0
    if a > b:
        if a > c:
            largest = a
        else:
            largest = c
    else:
        if b < c:
            largest = c
        else:
            largest = b
    return largest

main()