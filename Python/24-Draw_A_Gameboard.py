def main():
    global wid 
    wid = int(input("What is your width: "))
    global hei 
    hei = int(input("What is your height: "))
    width()
    height()

def width():
    print(" ---" * wid + "\n" + "|   " * (wid + 1))
    
def height():
    h = 1
    while h < hei:
        width()
        h = h + 1
    print(" ---" * wid)

main()