"""
Using Boolean, write a function that takes an ordered list of numbers and another number.
The function decides whether or not the given number is inside the list and prints an appropriate boolean.
"""

import random 
lst = []
x = 0
size = random.randrange(1, 50)
#range1, range2 =input("What is the size of your elements(Low_range High_range): ").split()

while size >= x:
    ele = random.randint(1, 100)
    lst.append(ele)
    x = x + 1
lst2 = list(dict.fromkeys(sorted(lst)))
print(lst2)

def element_search(lst2):
    srh = int(input("What is the number you are searching for: "))
    if srh in lst2:
        print("True")
    else:
        print("False")
    
"""
def element_search(lst2):
    strt = 1
    nd = len(lst2) - 1
    print( strt, nd)
    srh = int(input("What number are you searching for: "))
    
    while True:
        mid = (round((nd - strt) / 2))
        print(mid)
        if mid < strt or mid > nd or mid < 0:
            return False
        mid_ele = lst2[mid]
        print(mid_ele)
        if mid_ele == srh:
            return True
        elif mid_ele < srh:
            strt = mid
        else:
            nd = mid
"""            
        

"""
def element_search(lst2):
    srh = int(input("What number are you searching within the list: "))
    print(srh)
    if srh < lst2[0] or srh > lst2[-1]:
        print("The number you are searching for doesn't exist inside this lst of elements.")
        exit()
    while len(lst2) > 1:
        print(lst2)
        mid = (round((len(lst2)) / 2) - 2)
        if srh < lst2[mid]:
            lst2 = lst2[0 : mid]
        if srh > lst2[mid]:
            lst2 = lst2[mid:]
        if srh == lst2[mid]:
            print("The number you are searching for exists inside this list of elements.")
            exit()
            
    if lst2 != srh:
        print("The number you are searching for doesn't exist inside this list of element.")
    else:
        print("The number you are searching for exists inside this list of element.")
        
"""

element_search(lst2)