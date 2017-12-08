# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors

class HuyaNextpagePipeline(object):
    def __init__(self):
        self.conn = MySQLdb.connect('127.0.0.1', 'root', 'admin123', 'spiderdb', charset='utf8')
        self.cursor = self.conn.cursor()
        print('connect successed')

    def process_item(self, item, spider):
        insert_sql = """
                   insert into gameroom(introduction,gid,nick,totalCount)
                       VALUES (%s,%s,%s,%s)                
                   """
        gametable = (item["introduction"], item["gid"],item["nick"],item["totalCount"])
        self.cursor.execute(insert_sql, gametable)
        self.conn.commit()