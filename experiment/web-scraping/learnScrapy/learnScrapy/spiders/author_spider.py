import scrapy

class imdbSpider(scrapy.Spider):
    name = "google"

    def start_requests(self):
        query = input('Enter Query: ');
        urls = [
            ''
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = response.xpath('//h3[@r]/a/text()').extract()
        for x in range(0,len(data)):
            data[x] = data[x] + '\n'
        print (data)
        data = ''.join(data)
        print (data)
        with open('/home/atb00ker/Mega/File.Local/Python/WebScraping/learn/data/googleSearch.html','w') as f:
            f.write(data)
