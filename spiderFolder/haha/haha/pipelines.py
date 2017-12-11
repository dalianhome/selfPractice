# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors

class HahaPipeline(object):
    def __init__(self):
        self.conn=MySQLdb.connect('127.0.0.1','root','admin123','spiderdb',charset='utf8')
        self.cursor = self.conn.cursor()
        print ('connect successed')


    def process_item(self, item, spider):
        insert_sql = """
                insert into gameroom(gid,page,introduction,nick,totalCount,localDT)
                    VALUES (%s,%s,%s,%s,%s,%s)                
                """
        gametable = (item["gid"],item["page"], item["introduction"],item['nick'],item['totalCount'],item['localDT'])
        self.cursor.execute(insert_sql, gametable)
        self.conn.commit()


class GamePipeline(object):
    def __init__(self):
        self.conn=MySQLdb.connect('127.0.0.1','root','admin123','spiderdb',charset='utf8')
        self.cursor = self.conn.cursor()
        #print ('connect successed')



    def process_item(self, item, spider):
        insert_sql = """
                insert into huyalive_gamelist(gamename,gid,gameurl,ttime)
                    VALUES (%s,%s,%s,%s)                
                """
        gtable = (item["gamename"],item["gid"],item["gameurl"], item['ttime'])
        self.cursor.execute(insert_sql, gtable)
        self.conn.commit()



