"""
Load the birthday records JSON file from disk and count using the built in Python Counter how many birthdays are in common. 
"""

import json
from collections import Counter

def birthcount():
    with open("35-records.json", "r") as record:
        bday_dict = json.load(record)
    name = []
    date = []
    for v, k in bday_dict.items():
        name.append(v)
        date.append(k)
        print(k)
    c = Counter(date)
    inp = input("What date do you want to look up(MM/DD/YYYY): ")
    print(("There are {} birthdays on " + inp).format(c[inp]))

birthcount()