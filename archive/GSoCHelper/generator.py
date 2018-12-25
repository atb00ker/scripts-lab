import requests
from lxml import etree, html
import json

def scrapeNews():
    urls = ["https://summerofcode.withgoogle.com/archive/2017/organizations/" , "https://summerofcode.withgoogle.com/archive/2016/organizations/"]
    orgBoxes = []
    for url in urls:
        data = requests.get(url).text
        et = html.fromstring(data)
        orgBoxes = et.xpath("//main//ul/li/a/@href")
        iterator = 0
        with open('organizations.js','a+') as f:
            for orgBox in orgBoxes:
                data = requests.get("https://summerofcode.withgoogle.com" + orgBox).text
                et = html.fromstring(data)
                nameContainer = et.xpath("//h3[@class='banner__title']/text()")
                techContainer = et.xpath("//ul[contains(@class,'org__tag-container')]/li[@class='organization__tag organization__tag--technology']/text()")
                linkContainer = et.xpath("//a[contains(@class,'org__link')]/@href")
                value = "organizations[" + str(iterator) + "] = " + str({'name' :nameContainer, 'tech': techContainer, 'link': linkContainer}) + "\n"
                f.write(value)
                print (value)
                iterator +=1
            f.close()
if __name__ == '__main__':
    scrapeNews()
