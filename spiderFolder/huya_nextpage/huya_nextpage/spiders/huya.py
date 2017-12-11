# -*- coding: utf-8 -*-
import scrapy
import json
from huya_nextpage.items import HuyaNextpageItem
from scrapy.spiders import BaseSpider
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.selector import XmlXPathSelector
import lxml.etree as etree
from dicttoxml import dicttoxml
class HuyaSpider(BaseSpider):
    name = 'huya'
    allowed_domains = ['huya.com']
    start_urls = ['http://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId=1&tagAll=0&page=1']
   # rules =[
     #   Rule(LinkExtractor(
    #        allow=['/r/pics/\?count=\d*&after=\w*']),
    #        callback='parse_item',
    #        follow=True)
       #'https://www.reddit.com/r/pics/?count=25&after=t3_70e784'
      #  Rule(LinkExtractor(
      #      allow=['/r/pics/\?count=\d*&after=\w*']),
      #      callback='parse_item',
       #     follow=True)
  #  ]

    def parse(self, response):
        js = response.body
        json_dict = json.loads(js)
      #  xml = dicttoxml.dicttoxml(json_dict)
     #   xml = etree.fromstring(xml)
    #    xml = XmlXPathSelector(text=xml)
     #   data = xml.select("*").extract()
        #print(type(json_dict['data']['page']))
        print(json_dict['data']['page'])
        next = json_dict['data']['page'] + 1
        maxpage = json_dict['data']['totalPage']
        item=HuyaNextpageItem()
        for nick in json_dict['data']['datas']:
            item['introduction'] = nick['introduction']
            item['totalCount'] = nick['totalCount']
            item['gid'] = nick['gid']
            item['nick'] = nick['nick']
            print (item['gid']  + ' : ' + item['nick'] )
          #  yield item
        if (next<=maxpage):
            url = 'http://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId='+ str(item['gid'])+ '&tagAll=0&page='+ str(next)
        #url = response.joinurl(url)
        yield scrapy.Request(url,callback=self.parse)
    #def another_func(self,response):

      #  item = HuyaNextpageItem()
      #  for item_divs in response.xpath('.//div[@class="box game-live-box"]//li[@class="game-live-item"]'):
       #     item['host'] = item_divs.xpath('.//a//@title').extract()[0]
       #     item['slogan'] = item_divs.xpath('.//a[2]//@title').extract()[0]
           # yield item
