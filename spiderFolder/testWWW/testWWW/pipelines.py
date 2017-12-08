# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors

class TestwwwPipeline(object):
        def __init__(self):
            self.conn = MySQLdb.connect('127.0.0.1', 'root', 'admin123', 'spider', charset='utf8')
            self.cursor = self.conn.cursor()
            print('connect successed')

        def process_item(self, item, spider):
            insert_sql = """
                     insert into movie_tbl(mp4_link,actor,img_link,TIMETag)
                         VALUES (%s,%s,%s,%s)                
                     """
            itemtbl = (item["mp4_link"],item['actor'],item["img_link"], item['TIMETag'])
            self.cursor.execute(insert_sql, itemtbl)
            self.conn.commit()
