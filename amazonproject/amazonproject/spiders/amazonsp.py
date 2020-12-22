import scrapy


class AmazonspSpider(scrapy.Spider):
    name = 'amazonsp'
    allowed_domains = ['amazon.com']
    start_urls = ['http://amazon.com/']

    def parse(self, response):
        pass
