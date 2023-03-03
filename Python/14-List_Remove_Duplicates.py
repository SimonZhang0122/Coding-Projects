def random_list(leng, range1, range2):
    import random
    list = []
    i = 0
    while i < leng:
        x = random.randint(range1, range2)
        list.append(x)
        i = i + 1
    print(list)
    return list

def remove_dup(inp):
    new = list(dict.fromkeys([x for x in inp for y in inp if x == y]))
    return new

a = int(input("What is the length of your list: "))
rawb, rawc = input("What is the range of your list: ").split()
b = int(rawb)
c = int(rawc)
print(remove_dup(random_list(a, b, c)))