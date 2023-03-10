"""
Return only the common numbers etween the two list and remove and duplicates within by using list comprehension. 
"""

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(list(dict.fromkeys([x for x in a for y in b if x == y])))
