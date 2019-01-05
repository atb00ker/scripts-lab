import requests
from lxml import etree
from lxml import html
import datetime

payload = {
            'minTomato':'30',
            'maxTomato':'100',
            'minPopcorn':'30',
            'maxPopcorn':'100',
            'services':'amazon;amazon_prime',
            'genres':'1;2;4;5;6;8;9;10;11;13;18;14',
            'sortBy':'popularity'
            }
query = input("Enter Your Query:")
url = 'https://www.rottentomatoes.com/browse/top-dvd-streaming'
data = requests.get(url, params=payload)
et = html.fromstring(data.text)
# with open('/media/atb00ker/Windows(Main)/Mega/File.Local/Python/WebScrapping/data/raw_dig.txt','w') as f:
#     f.write(data.text)
# rawPut = et.xpath("//div[@class='movie_info']/a/div/span[@class='tMeterIcon']/span[@class='tMeterScore']/text()")
rawPut = et.xpath("//h3[@class='r']/a/text()")
for x in rawPut:
    print(x)
