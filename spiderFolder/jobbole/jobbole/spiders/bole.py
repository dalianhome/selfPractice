# -*- coding: utf-8 -*-
import scrapy
import re

class BoleSpider(scrapy.Spider):
    name = 'bole'
    allowed_domains = ['jobbole.com']
    start_urls = ['http://blog.jobbole.com/112499/']

    def parse(self, response):

      createDate =  response.xpath('.//p[@class="entry-meta-hide-on-mobile"]//text()').extract()[0].strip().replace(" ·","")
      title = response.xpath('.//div[@id="post-112499"]//div[@class="entry-header"]//h1//text()').extract()[0]
      zan = response.xpath('.//span[contains(@class,"vote-post-up")]//h10//text()').extract()[0]
      #------------------------------------------------------------------------------------------
      fav_num = response.xpath('.//span[contains(@class,"bookmark-btn")]//text()').extract()[0]
      getstr = (r".*(\d+).*")
      mach_obj = re.match(getstr,fav_num)
      if mach_obj:
          fav_num  =mach_obj.group(1)


      # ------------------------------------------------------------------------------------------
      # ------------------------------------------------------------------------------------------

      comm_nums = response.xpath('.//div[@class="post-adds"]//span[@class="btn-bluet-bigger href-style hide-on-480"]//text()').extract()[0]
      #mach_commobj = re.match(".*(\d+).*", comm_nums)
    #  if mach_commobj:
     #     if (mach_commobj.group(1) == ' '):
      #        comm_nums = 0
       #   else:
        #      comm_nums = mach_commobj.group(1)
      # ------------------------------------------------------------------------------------------
      print(title + " : " + createDate + " : " + zan + "/up" + " : "+ fav_num + " : "+ comm_nums)
       #  print(comm_nums)