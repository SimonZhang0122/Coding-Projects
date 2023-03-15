"""
Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. 
One .txt file has a list of all prime numbers under 1000, and the other .txt file has a list of happy numbers up to 1000.
"""

h_list = []
p_list = []
c_list = []


with open("happynumbers.txt", "r") as happy:
    for line in happy:
        h_list.append(int(line))
        
with open('primenumbers.txt', 'r',) as prime:
    for line in prime:
        p_list.append(int(line))
        
c_list = [p for p in p_list for h in h_list if p == h]


print(c_list)
