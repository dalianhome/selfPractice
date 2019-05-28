# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import MySQLdb
import MySQLdb.cursors
import codecs
import json

class MyprotienproductPipeline(object):
     def __init__(self):
         self.conn = MySQLdb.connect('127.0.0.1', 'root', 'admin123', 'newdb', charset='utf8')
         self.cursor = self.conn.cursor()
         print('connect successed')

     def process_item(self, item, spider):
            insert_sql = """
                       insert into protien(url) VALUES (%s)                
                       """
            table = [item["url"]]
            self.cursor.execute(insert_sql, table)
            self.conn.commit()
