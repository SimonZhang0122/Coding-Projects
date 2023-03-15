
def int_list(inp = "What is your list of intergers: "):
    raw = list(input(inp).split())
    fin = [int(x) for x in raw]
    return fin

def list_ends(list):
    ends = [list[0], list[-1]]
    return ends

print(list_ends(int_list()))
