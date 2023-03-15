"""
Using 'BeautifulSoup' and 'requests' Python packages, print out all article titles on the 'New York Times' homepage.
"""

import requests
from bs4 import BeautifulSoup

url = 'https://www.nytimes.com'
r = requests.get(url)
soup = BeautifulSoup(r.text, features="lxml")

for heading in soup.find_all(class_="indicate-hover"):
    print(heading)
        