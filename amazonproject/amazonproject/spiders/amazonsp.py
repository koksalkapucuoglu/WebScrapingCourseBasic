import scrapy


class AmazonspSpider(scrapy.Spider):
    name = 'amazonsp'
    allowed_domains = ['amazon.com']

    custom_settings = {
        'FEED_URI': 'brand.txt',
        'FEED_FORMAT': 'json'
    }

    def start_requests(self):
        url = 'https://www.amazon.com/s?k=phone&i=mobile&rh=n%3A2335752011%2Cp_89%3ASamsung+Electronics&dc&qid=1608662423&ref=sr_ex_n_1'
        yield scrapy.Request(url)

    def parse(self, response):
        brand = response.xpath('.//span[@class="a-size-medium a-color-base a-text-normal"]/text()').extract()
        star = response.xpath('.//span[@class="a-size-base"]/text()').extract()
        sumofBrandandStar = []

        for i in range(len(brand)):
            sum = f'{star[i]} people voted for {brand[i]}.'
            sumofBrandandStar.append(sum)

        yield {'sum':sumofBrandandStar}
