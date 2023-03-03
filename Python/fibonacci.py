def fibonacci(inp):
    digits, raw = inp.split()
    a = int(raw)
    i = 0
    list = []
    while i < int(digits):
        if i <= 1:
            list.append(a)
        else:
            a = a + list[(i - 2)]
            list.append(a)
        i = i + 1
    return list

print(fibonacci(input("How many digits and what's the first number: ")))