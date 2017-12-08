# -*- coding: utf-8 -*-
import scrapy

import json
import re
from testWWW.items import TestwwwItem
from datetime import datetime
from time import gmtime, strftime
from tzlocal import get_localzone

class HuyaliveSpider(scrapy.Spider):
    name = 'huyalive'
    allowed_domains = ['japanesebeauties.net']
    start_urls = ['https://www.japanesebeauties.net/tube/yui.hatano/',
                  'https://www.japanesebeauties.net/tube/julia/',
                  'https://www.japanesebeauties.net/tube/azumi.kinoshita']

    def parse(self, response):
        print ('just visited ' + response.url)

        items = response.xpath('.//div[@class="middle"]')
        item_eles = items.xpath('.//div[@class="tubesearch"]')
        for item_ele in item_eles:
            video_url = item_ele.xpath('.//@href').extract()[0]
            img_url = item_ele.xpath('.//@src').extract()[0]
            # print video_url +' : '+ img_url
            yield scrapy.Request(video_url, callback=self.parse_inside)

        # nextpage =  response.xpath(u".//div[@class='page']/a[text()='下一页']/@href").extract()[0]
        nextpage = response.xpath(".//div[@class='details']/a[last()-1]/@href").extract()[0]
        if nextpage is not None:
            nextpage = response.urljoin(nextpage)
            yield scrapy.Request(nextpage, callback=self.parse)

    def parse_inside(self, response):
        item = TestwwwItem()
        in_items = response.xpath('.//div[@class="middle"]')
        inItem_eles = in_items.xpath('.//div[@class="mp4"]')
        actor = in_items.xpath('.//div[@class="details"]//a//text()').extract_first()

        for inItem_ele in inItem_eles:
            item['TIMETag'] = datetime.now(get_localzone())#strftime("%Y-%m-%d %H:%M:%S", gmtime())
            item['mp4_link'] = inItem_ele.xpath('.//@src').extract_first()
            item['img_link']= inItem_ele.xpath('.//@poster').extract_first()
            item['actor'] =  actor
            print (item['actor'] + ' :' +item['mp4_link']+' : '+ item['img_link'] )
            yield item