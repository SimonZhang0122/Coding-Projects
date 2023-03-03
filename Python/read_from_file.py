counter = {}

with open("Training_01.txt", "r") as file:
    line = file.readline()
    while line:
        cat = line[3: -26]
        if cat in counter:
            counter[cat] += 1
        else:
            counter[cat] = 1
        line = file.readline()

for x, y in counter.items():
    print( x, ' : ' , y)