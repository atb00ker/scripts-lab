import requests
from lxml import etree
from lxml import html

url = 'http://asetalias.in'
data = requests.get(url).text
et = html.fromstring(data)
rawPut = et.xpath("//h2[@class='youtubeVideoTitletext-small']/a/text()")
print(rawPut)
