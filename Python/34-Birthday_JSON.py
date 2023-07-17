"""
Modify your program from Project 33 to load the birthday dictionary from a JSON file on disk, rather than having the dictionary defined in the program.
"""

import json


def printRecord():
    with open("34-birth_record.json", "r") as record:
        bday_dict = json.load(record)
    for k, v in bday_dict.items():
        print(k + ":\t\t" + v)


def writeRecord(bday_dict):
    with open("34-birth_record.json", "w") as record:
        json.dump(bday_dict, record, indent = 4)


def Search():
    print("\n\t---Search Mode---\n")
    printRecord()
    with open('34-birth_record.json', 'r') as record:
        bday_dict = json.load(record)
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
    import datetime    
    print("\n\t---File Entry Mode---\n")
    printRecord()
    print("Type 'e' to go back.")
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
    check = input(">>>Are you sure you want to add '" + name + "',\nwith birthday '" + bday + "'? (Y/N):").upper()
    while check not in ["Y", "N"]:
        print("Invalid input! Please type 'y' or 'n'")
        check = input(">>>Are you sure you want to add '", name, "',\nwith birthday '", bday, "'? (Y/N):").upper()
    if check == "Y":
        with open("34-birth_record.json", "r") as record:
            bday_dict = json.load(record)
            bday_dict[name] = bday
            writeRecord(bday_dict)
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
        check = input(">>>Are you sure you want to add '" + name + "'\nwith birthday '" + bday + "'? (Y/N):").upper()
        while check not in ["Y", "N"]:
            print("Invalid input! Please type 'y' or 'n'")
            check = input(">>>Are you sure you want to add '", name, "'\nwith birthday '", bday, "'? (Y/N):").upper()
        if check == "Y":
            with open('34-birth_record.json', 'r') as record:
                bday_dict = json.load(record)
                bday_dict[name] = bday
                writeRecord(bday_dict)
            printRecord()
            print("\n    ---Entry added.---\n")


def DEL():
    with open('34-birth_record.json', 'r') as record:
        bday_dict = json.load(record)
    print("\n\t---File Deletion Mode---\n")    
    printRecord()
    print("\nPress any other keys to exit")
    inp = input(">>>Do you want to delete by name or birthday(N/B): ").upper()
    if inp == "N":
        print()
        for key, value in bday_dict.items():        
            print(key)
        delete = input("\n>>>What is the name you want to delete: ")
        while delete not in bday_dict.keys():
            print("Invalid name, name don't exist in record.")
            delete = input("\n>>>What is the name you want to delete: ")            
        choice = input("\n>>>Are you sure you want to delete '" + delete + " : " + bday_dict[delete] + "' (Y/N): ").upper()
        while choice not in ["Y", "N"]:
            print("ERROR! Invalid input, please type 'y' or 'n'.")
            choice = input("\n>>>Are you sure you want to delete '" + delete + " : " +  bday_dict[delete] + "' (Y/N): ").upper()        
        if choice == "Y":
            del bday_dict[delete]
            writeRecord(bday_dict)
            printRecord()
        else:
            DEL()
    elif inp == "B":
        print()
        for key, value in bday_dict.items():
            print(value)
        delete = input("\n>>>What is the birthday you want to delete: ")
        while delete not in bday_dict.values():
            print("Invalid date, birthday don't exist in record.")
            delete = input("\n>>>What is the birthday you want to delete: ")
        rawname = [k for k, v in bday_dict.items() if v == delete]
        name = rawname[0]
        choice = input("\n>>>Are you sure you want to delete '" + name  + " : " + delete + "' (Y/N): ").upper()
        while choice not in ["Y", "N"]:
            print("ERROR! Invalid input, please type 'y' or 'n'.")
            choice = input("\n>>>Are you sure you want to delete '" + name + " : " +  delete + "' (Y/N): ").upper()        
        if choice == "Y":
            del bday_dict[name]
            writeRecord(bday_dict)
            printRecord()
        else:
            DEL()
    else:
        Edit()


def main():
    print("\t---Welcome to the Birthday Archieve---\n")
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
