import requests
from lxml import etree, html
import datetime

query = input("Enter Your Query:")
cookie_JAR = datetime.datetime.today().strftime('%Y-%m-%d') + '-12'
cookie={'1P_JAR':cookie_JAR,'DV':'I3FFRz7sn8IToMCKdBuTnHTXAYed8xU','NID':'114=mdwhZi8jdIZ08wP0hYS5MJdYLjUOw0D_Da8_V7XYPqJf0d-hYN9wljPxSF3y3KvFfsESTreIQOTv1QxvqBPmKyD73Rh-xzllEvlZTdLOyi9rayhcEMNPVXMk_5HFIhso','SNID':'114=mb3hMoCETHrhL78nsTC8ltQO_cZlesv_sQ3UN3jNxA=_azu1gR6b2bqwP57'}

data = requests.get('https://www.google.co.in/search?q='+query, cookies=cookie)

et = html.fromstring(data.text)
rawPut = et.xpath("//h3[@class='r']/a/text()")
for results in rawPut:
    print(results)
