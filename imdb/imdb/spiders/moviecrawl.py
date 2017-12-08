# -*- coding: utf-8 -*-
import scrapy
import re

class MoviecrawlSpider(scrapy.Spider):
    name = 'moviecrawl'
    allowed_domains = ['imdb.com']
    start_urls = ['http://www.imdb.com/chart/top']

    def parse(self, response):
        names = response.xpath('.//tbody[@class="lister-list"]//tr')
        for name in names :
            movie = name.xpath('.//td[@class="titleColumn"]//a/text()').extract()[0]
            sn = name.xpath('.//td[@class="titleColumn"]/text()').extract()[0]


            print(sn +" "+  movie)