import random   
a = []
b = []
x = 1
y = 1
common = []
size = int(input("What size do you want List_A to be: "))
size2 = int(input("What size do you want List_B to be: "))
a_range1, a_range2 = input("Please enter the ranges for List_A: ").split()
b_range1, b_range2 = input("Please enter the ranges for List_B: ").split()
while x <= size:
    rand = random.randint(int(a_range1), int(a_range2))
    a.append(rand)
    x = x + 1
while y <= size2:
    rand = random.randint(int(b_range1), int(b_range2))
    b.append(rand)
    y = y +1
print("The randomly generated List_A ranges from " + str(a_range1) + " to " + str(a_range2) + " and contains: " + ' ' .join(str(size) for size in a ))
print("The randomly generated List_B ranges from " + str(b_range1) + " to " + str(b_range2) + " and contains: " + ' '.join(str(size2) for size2 in b))
for num in a:
    if num in b:
        common.append(num)
print("The two randomly generated lists have these common numbers:" + str(list(dict.fromkeys(common))))