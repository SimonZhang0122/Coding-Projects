list = []
num =   int(input("How many numbers are you querying: "))
print("Please enter your numbers: ")
for i in  range(0, num):
    char  = int(input())
    list.append(char)
print("Your list of number is: " + ' '.join(str(num) for num in list)) 
newlist = []
newerlist = []
for ele in list:
    if ele < 5:
        newlist.append(ele)
print("This new list only have numbers smaller than 5: " + ' '.join(str(num) for num in newlist))
lim = int(input("What number do you want to set as the limit for the list: "))
for el in list:
    if el < lim:
        newerlist.append(el)
print("This list only have numbers smaller than " + str(lim) +  ": " + ' '.join(str(num) for num in newerlist))