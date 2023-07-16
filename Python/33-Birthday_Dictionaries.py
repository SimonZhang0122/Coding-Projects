"""
Create a dictionary (in your file) of names and birthdays. 
Search mode asks the user to enter a name, and return the birthday of that person back to them and vise versa. 
Edit mode asks the user if they want to add a person's name and birthday and can also delete any records. 
"""

def Search():
    bday_dict = {}
    with open("33-birth_record.txt", "r") as record:
        line = record.readline().strip()
        while line:
            name = (line[ : -12])
            birth = (line[-10: ])
            bday_dict[name] = birth
            line = record.readline().strip()
    print("\n\t---Search Mode---\n")
    printRecord()
    print("\nPress any other keys to go back.")
    choice = input(">>>Hello, are you searching by name or by birthday(N/B):").upper()
    if choice == "N":
        print("\nThese are the names you can search from:\n (FIRST LAST)\n","\n ".join(sorted(bday_dict.keys())))
        inp = input("\n>>>Who's birthday are you looking up: ")
        while inp not in bday_dict.keys():
            print("Unable to find the name: '" + inp + "', name not in record.")
            inp = input("\n>>>Who's birthday are you looking up: ")
        print( inp + "'s birthday is on " + bday_dict[inp])
        choice = input("Exit search mode? (Y/N): ").upper()
        while choice not in ["Y", "N"]:
            print("ERROR! Invalid input, please type 'y' or 'n'.")
            choice = input("Exit search mode? (Y/N): ").upper()            
        if choice == "Y":
            main()
        else:
            Search()
    elif choice == "B":
        print("\nThese are the birthdays you can search from:\n (MM/DD/YYYY)\n","\n ".join(sorted(bday_dict.values())))
        inp = input("\n>>>Which birthday are you looking up: ")
        while inp not in bday_dict.values():
            print("Unable to find the birthday: '" + inp + "', birthday not in record.")
            inp = input("\n>>>Which birthday are you looking up: ")
        for name, bir in bday_dict.items():
            if bir == inp:
                print(name + "'s birthday is on " + inp)
        choice = input("Exit search mode? (Y/N): ").upper()
        while choice not in ["Y", "N"]:
            print("ERROR! Invalid input, please type 'y' or 'n'.")
            choice = input("Exit search mode? (Y/N): ").upper()            
        if choice == "Y":
            main()
        else:
            Search()
    else:
        main()

def printRecord():
    bday_dict = {}
    srt_dict = {}
    with open("33-birth_record.txt", "r") as record:
        line = record.readline().strip()
        while line:
            name = (line[ : -12])
            birth = (line[-10: ])
            bday_dict[name] = birth
            line = record.readline().strip()
    for i in sorted(bday_dict):
        srt_dict[i] = bday_dict[i]
    for n, b in srt_dict.items():
        print(" ", n, " : ", b)


def Edit():
    print("\n\t---Editor Mode---\n")
    printRecord()
    print("\nType any keys to go back.")
    choice = input(">>>Do you want to add or delete an entry(A/D): ").upper()
    if choice == "A":
        ADD()
        while True:
            inp = input(">>>Add more entries? (Y/N): ").upper()
            while inp not in ["Y", "N"]:
                print("Invalid input! Please type 'y' or 'n'")
                inp = input(">>>Add more entries? (Y/N): ").upper()
            if inp == "Y":
                ADD()
            else:
                main()
    elif choice == "D":
        DEL()
        while True:
            inp = input(">>>Delete more entries? (Y/N): ").upper()
            while inp not in ["Y", "N"]:
                print("Invalid input! Please type 'y' or 'n'")
                inp = input(">>>Delete more entries? (Y/N): ").upper()
            if inp =="Y":
                DEL()
            else:
                Edit()
    else:
        main()
            
def ADD():
    print("\n\t---FIle Entry Mode---\n")    
    import datetime
    print("Press 'e' to go back.")
    name = input(">>>What is the name you want to add: ")
    if name == "e" or name == "E":
        Edit()
    while name == '':
        print("Error! Empty name.")
        name = input(">>>What is the name you want to add: ")
        if name == "e" or name == "E":
            Edit()
    while True:
        try:
            mm, dd, yy = input(">>>What is the birthday(MM DD YYYY): ").split()
            while int(mm) > 12 or int(mm) < 1 or int(dd) > 31 or int(dd) < 1 or int(yy) > int((datetime.date.today()).year) or int(yy) < (int((datetime.date.today()).year) - 100):
                print("ERROR! Invalid date.")
                mm, dd, yy = input(">>>What is the birthday(MM DD YYYY): ").split()
            break
        except:
            pass
        print("ERROR! Please type the date sepeprated by spaces(MM DD YYYY).")
    bday = (mm + "/" + dd + "/" + yy)
    check = input(">>>Are you sure you want to add '" + name + "', with birthday '" + bday + "'? (Y/N):").upper()
    while check not in ["Y", "N"]:
        print("Invalid input! Please type 'y' or 'n'")
        check = input(">>>Are you sure you want to add '", name, "', with birthday '", bday, "'? (Y/N):").upper()
    if check == "Y":
        with open("33-birth_record.txt", "a") as file:
            entry = (name + ": " + bday + "\n")
            file.writelines(entry)
        print()
        printRecord()
        print("\n    ---Entry added.---\n")
    while check == "N":
        print("Press 'e' to go back.")
        name = input(">>>What is the name you want to add: ")
        if name == "e" or name == "E":
            Edit()
        while name == '':
            print("Error! Empty name.")
            name = input(">>>What is the name you want to add: ")
            if name == "e" or name == "E":
                Edit()        
        while True:
            try:
                mm, dd, yy = input(">>>What is the birthday(MM DD YYYY): ").split()
                while int(mm) > 12 or int(mm) < 1 or int(dd) > 31 or int(dd) < 1 or int(yy) > int((datetime.date.today()).year) or int(yy) < (int((datetime.date.today()).year) - 100):
                    print("ERROR! Invalid date.")
                    mm, dd, yy = input(">>>What is the birthday(MM DD YYYY): ").split()
                break
            except:
                pass
            print("ERROR! Please type the date sepeprated by spaces(MM DD YYYY).")
        bday = (mm + "/" + dd + "/" + yy)
        check = input(">>>Are you sure you want to add '" + name + "', with birthday '" + bday + "'? (Y/N):").upper()
        while check not in ["Y", "N"]:
            print("Invalid input! Please type 'y' or 'n'")
            check = input(">>>Are you sure you want to add '", name, "', with birthday '", bday, "'? (Y/N):").upper()
        if check == "Y":
            with open("33-birth_record.txt", "a") as file:
                entry = (name + ": " + bday + "\n")
                file.writelines(entry)
            print()
            printRecord()
            print("\n    ---Entry added.---\n")
def DEL():
    print("\n\t---File Deletion Mode---\n")    
    with open("33-birth_record.txt", "r") as record:
        line = record.readline().strip()
        index = 1
        file = []
        while line:
            fline = (line + "\n")
            file.append(fline)
            print(str(index) + ":\t" + line)
            index += 1            
            line = record.readline().strip()
        while True:
            try:
                print("\nPress Enter to go back.")
                delete = int(input(">>>Which entry do you want to delete: "))
                break
            except:
                delete = input("\n>>>Exit?(Y/N): ").upper()
                if delete == "Y":
                    Edit()
                if delete == "N":
                    DEL()
            print("Please choose a number between 1 - " + str(index - 1))
        while delete < 0 or delete > (index-1):
            print("Entry doesn't exist, choose a number between 1 - " + str(index - 1)  + "\n")
            while True:
                try:
                    delete = int(input("\n>>>Which entry do you want to delete: "))
                    break
                except:
                    pass
                print("ERROR! Please choose a number between 1 - " + str(index - 1))
        choice = input(">>>Are you sure you want to delete(Y/N):\n" + file[delete - 1]).upper()
        while choice not in ["Y", "N"]:
            print("Invalid input! Please type 'y' or 'n'")
            choice = input(">>>Are you sure you want to delete(Y/N):\n" + file[delete - 1]).upper()
        if choice == "Y":
            print("\nDeleting ---> " + file[delete - 1])
            file.pop(delete - 1)
        while choice == "N":
            while True:
                try:
                    print("\nPress Enter to go back.")
                    delete = int(input(">>>Which entry do you want to delete: "))
                    break
                except:
                    delete = input("\n>>>Exit?(Y/N): ").upper()
                    if delete == "Y":
                        Edit()
                    if delete == "N":
                        DEL()
                print("Please choose a number between 1 - " + str(index - 1))
            while delete < 0 or delete > index:
                print("Entry doesn't exist, choose a line between 1 - " + str(index - 1))
                delete = int(input(">>>Which entry do you want to delete: "))
            choice = input(">>>Are you sure you want to delete(Y/N):\n" + file[delete - 1]).upper()
            while choice not in ["Y", "N"]:
                print("Invalid input! Please type 'y' or 'n'")
                choice = input(">>>Are you sure you want to delete(Y/N):\n" + file[delete - 1]).upper()
            if choice == "Y":
                print("\nDeleting ---> " + file[delete - 1])
                file.pop(delete - 1)
        with open("33-birth_record.txt", "w") as record:
            record.writelines(file)
        printRecord()

def main():
    print("\t---Wlecome to the birthday Archieve---\n")
    printRecord()
    print("\nTo search for an archieve press 's', \nTo edit existing files press 'e', \nTo quit press any other keys.")
    inp = input("\n>>>What would you like to do(S/E): ").upper()
    if inp == "S":
        Search()
    elif inp == "E":
        Edit()
    else:
        print("\n\t---Exiting---")
        exit()
    
main()