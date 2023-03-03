def string_list(string, arg=" "):
    global choice
    arg = choice
    new = string.split(arg)
    print(new)
    return new

def list_reverse(par):
    size = len(par)
    run = 0
    i = -1
    rev = []
    while run < size:
        rev.append(par[i])
        i = i - 1
        run = run + 1
    return rev

choice = input("What is your choice of seperator: ")
if choice == "":
    choice = " "
print(list_reverse(string_list(input("What is your string of words: "))))