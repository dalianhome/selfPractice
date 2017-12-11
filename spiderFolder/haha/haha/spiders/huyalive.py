# -*- coding: utf-8 -*-
import scrapy

import urllib
from scrapy.selector import HtmlXPathSelector
from scrapy.http import Request
import json
from tzlocal import get_localzone
from datetime import datetime
from time import localtime, strftime,gmtime
import pytz

from haha.items import HahaItem,PageItem
class HuyaliveSpider(scrapy.Spider):
    name = 'huyalive'
    allowed_domains = ['huya.com']
    start_urls = ['http://www.huya.com/g']

    def parse(self,response):

       for box in response.xpath('.//div[@class = "box-bd"]//li[@class="game-list-item"]'):
           gameurl=box.xpath('.//@href').extract()[0]
           yield scrapy.Request(gameurl,callback=self.parseNX)
       #for nx in response.xpath('.//div[@class = "box-bd"]//div[@class="js-list-page"]'):
        #  yield scrapy.Request(gameurl, callback=self.parseNX)
    def parseNX(self,response):
        item = HahaItem()
        item['gameurl'] = response.url
        item['gamename'] = response.xpath('.//h2[@class = "title"]//a/text()').extract()[0]
        item['gid'] = response.xpath('.//div[@class="box game-live-box"]//@gid').extract()[0]
        #item['tUTC'] = strftime("%Y-%m-%d %H:%M:%S",gmtime())
        #item['ttime'] = datetime.now(tz=pytz.timezone('Singapore'))
        #item['ttime'] = datetime.now(get_localzone())
        item['ttime'] = strftime("%Y-%m-%d %H:%M:%S", localtime())
        url = 'http://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId='+ item['gid'] + '&tagAll=0&page=1'
        #print(item['gid'])
       # yield item

        yield scrapy.Request(url,callback=self.parseGameroom)
       
        
        
     
    def parseGameroom(self,response):
        finalitem = PageItem()
        print (response.url)
        js = response.body
        json_dict = json.loads(js)
        finalitem['page'] = json_dict['data']['page']
        next = json_dict['data']['page'] + 1
        maxpage = json_dict['data']['totalPage']
       # host = response.xpath('.//div[@class="room-hd-main-l"]//h3//@title').extract()[0]
        #pNum = response.xpath('.//div[@class="room-hd-main-l"]//span[@class="host-spectator"]//em[@id="live-count"]//text()').extract()[0]
       # cat1 = response.xpath('.//div[@class="host-detail J_roomHdDetail"]//span[@class="host-channel"]//a//text()').extract()[0]
      #  cat2 =  response.xpath('.//div[@class="host-detail J_roomHdDetail"]//span[@class="host-channel"]//a//h3//text()').extract()[0]
       # print (r_url + ' :' + host +" : " + pNum + " --"+ cat1+"/"+cat2)
       # print (str(page) + ' page')
        for it in json_dict['data']['datas']:
           # print ('Game->' + it['gid'] +  ' : ' + it['nick'])
            finalitem['introduction'] = it['introduction']
            finalitem['totalCount'] = it['totalCount']
            finalitem['gid'] = it['gid']
            finalitem['nick'] = it['nick']
            finalitem['localDT'] = strftime("%Y-%m-%d %H:%M:%S", localtime())
            yield finalitem

            if (next<=maxpage):
                url2 = 'http://www.huya.com/cache.php?m=LiveList&do=getLiveListByPage&gameId='+ it['gid'] +'&tagAll=0&page='+ str(next)
                yield scrapy.Request(url2,callback=self.parseGameroom)


   # def parse_game(self,response):
   #     print (response.url)

