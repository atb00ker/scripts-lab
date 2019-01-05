import scrapy

class imdbSpider(scrapy.Spider):
    name = "imdb"

    def start_requests(self):
        urls = [
            'http://www.imdb.com/movies-in-theaters/?ref_=nv_mv_inth_1'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        data = response.xpath('//h4[@itemprop]/a/text()').extract()
        for x in range(0,len(data)):
            data[x] = data[x] + '<br>\n'
        data = ''.join(data)
        print (data)
        with open('/home/atb00ker/Mega/File.Local/Python/WebScraping/data/imdb_Scraped.html','w') as f:
            f.write(data)

# -o to save in a file
