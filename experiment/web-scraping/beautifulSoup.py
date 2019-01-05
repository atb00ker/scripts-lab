from bs4 import BeautifulSoup

import requests

with open('/home/atb00ker/Mega/File.Local/Python/WebScraping/data/BeautifulSoup_link.html','w') as f:
    f.write("Links:")

url = input("Enter a website to extract the URL's from: ")
print (url)
r  = requests.get(url)

data = r.text

soup = BeautifulSoup(data)
for link in soup.find_all('a'):
    if(link.get('href')!=None):
        print(link.get('href'))
        with open('/home/atb00ker/Mega/File.Local/Python/WebScraping/data/BeautifulSoup_link.html','a') as f:
            f.write(link.get('href'))
            f.write('\n')
