# -*- coding: utf-8 -*-
import scrapy


class TedcrawlSpider(scrapy.Spider):
    name = 'tedcrawl'
    allowed_domains = ['ted.com']
    start_urls = ['https://www.ted.com/talks/']

    def parse(self, response):

        for items in response.xpath('.//div[@class="container results"]//h4//a'):
            print(items.xpath('.//text()').extract()[0])
            print('https://www.ted.com' + items.xpath('.//@href').extract()[0])
            title = items.xpath('.//text()').extract()[0]
            link = 'https://www.ted.com' + items.xpath('.//@href').extract()[0]
            f = open('items.csv', 'a')
            f.write(title + " : " + link)

            f.write('\n')
            f.close()
        try:
            url = 'https://www.ted.com' + response.xpath('.//a[@class="pagination__next pagination__flipper pagination__link"]//@href').extract()[0]
            yield scrapy.Request(url, callback=self.parse)
        except:
            print("Bye")
