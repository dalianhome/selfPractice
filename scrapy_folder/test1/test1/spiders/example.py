# -*- coding: utf-8 -*-
import scrapy
import csv

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['fairprice.com.sg']
    start_urls = ['https://www.fairprice.com.sg']

    def parse(self, response):
        for urllink in  response.xpath('.//div[@class="essentials_category_menu hidden"]//ul//li'):
            goto1 = urllink.xpath('.//a//@href').extract()[0]
            yield scrapy.Request(goto1,callback=self.parseGoto1)

    def parseGoto1(self, response):


        # for items in response.xpath('.//div[@class="tab-menu"]//ul//li'):
        #     print(response.url)
        #     print(items.xpath('.//a//span//text()').extract())
        for items in response.xpath('.//div[@class="tab-menu"]//ul//li'):
            itemlink = items.xpath('.//a//@href').extract()[0]
            # f = open('csvfile.csv', 'a')
            # f.write(itemlink)
            # f.write('\n')
            # print(itemlink)
            yield scrapy.Request(itemlink, callback=self.parseGoto2)
            # f.close()

    def parseGoto2(self, response):
        for url in response.xpath('.//div[@class="tab-menu"]//ul//li'):
            # f = open('csvfile.csv', 'a')
            # f.write(url.xpath('.//a//@href').extract()[0])
            # f.write('\n')
            # f.close()
            # print(url.xpath('.//a//@href').extract()[0])
            yield scrapy.Request(url.xpath('.//a//@href').extract()[0], callback=self.parseGoto3)

    def parseGoto3(self, response):

        for terms in response.xpath('.//div[@class="product_listing_container"]//ul//li//div[@class="product"]'):
            # print(terms.xpath('.//div[@class="pdt_list_wrap"]//div//div//a//@href').extract()[0])
            urlgoto4 = terms.xpath('.//div[@class="pdt_list_wrap"]//div//div//a//@href').extract()[0]

        #     f = open('csvfile.csv', 'a')
        #     f.write(terms.xpath('.//div[@class="pdt_list_wrap"]//div//div//a//@href').extract()[0])
        #     f.write('\n')
        # f.close()
            yield scrapy.Request(urlgoto4, callback=self.parseGoto4)

    def parseGoto4(self, response):
        name = response.xpath('.//div[@class="top namePartPriceContainer"]//h1//text()').extract()[0]
        vol = response.xpath('.//div[@class="pdt_weightMgDiv"]//span//text()').extract()[0]
        Cprice = response.xpath('.//span[@class="pdt_C_price"]//text()').extract()[0].strip()
        try:
            Oprice = " < " + response.xpath('.//span[@class="pdt_O_price"]//text()').extract()[0].strip()

        except:
            Oprice = " "
        print(str(name) + " " + Cprice + Oprice)
        contents= str(name) + " " + Cprice + Oprice
        f = open('items.csv', 'a')
        f.write(contents)
        f.write('\n')
        f.close()
