import requests
from bs4 import BeautifulSoup

raw_url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"
r = requests.get(raw_url)
soup = BeautifulSoup(r.text, "html.parser")
result = []

for inp in soup.find_all("p", "paywall"):
    result.append(inp.text)

for line in result:
    print(line)
    
with open('test_write.txt', 'w') as open_file:
    for line in result:
        open_file.write(line)
