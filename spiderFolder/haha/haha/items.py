# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HahaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    gamename = scrapy.Field()
    gameurl =scrapy.Field()
   # tUTC=scrapy.Field()
    ttime = scrapy.Field()
    gid=scrapy.Field()

class PageItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    introduction = scrapy.Field()
    totalCount =scrapy.Field()
   # tUTC=scrapy.Field()
    nick = scrapy.Field()
    gid=scrapy.Field()
    page = scrapy.Field()
    localDT =scrapy.Field()