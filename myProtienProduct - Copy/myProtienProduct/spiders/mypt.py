# -*- coding: utf-8 -*-
import scrapy
import urllib.parse
from urllib.parse import urljoin,urlparse
from urllib import parse
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from lxml import html
from myProtienProduct.items import MyprotienproductItem
class MyptSpider(CrawlSpider):
    name = 'mypt'
    allowed_domains = ['ics-cert.us-cert.gov']
    start_urls = ['https://ics-cert.us-cert.gov/advisories']

    def parse(self, response):
        response.url
        for items in response.xpath('.//div[@class="view-content"]//div//ul'):
            item = items.xpath('.//li//span[@class="field-content"]//a//text()').extract()[0]
            number = items.xpath('.//li//span[@class="field-content"]//text()').extract()[0]
            url = "https://ics-cert.us-cert.gov"+str(items.xpath('.//li//span[@class="field-content"]//@href').extract()[0])
            print(number + "  :  "+item + "  -->  "+ url)
        # for items in response.xpath('.//div[@id="block-views-advisory-index-view-block-1"]//div//div//div//div[2]//div//ul//li[1]'):
        #     item = items.xpath('.//span[1]//span//text()').extract()[0]
        #     print(item)
        nextpage = response.xpath('.//a[@title="Go to next page"]//@href').extract()[0]
        nextpage1 ="https://ics-cert.us-cert.gov"+str(nextpage)
        yield scrapy.Request(url=nextpage1, callback=self.parse)













