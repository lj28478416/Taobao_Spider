# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import csv
import pymongo

class TaobaoSpiderPipeline(object):
    def open_spider(self,spider):
        self.client = pymongo.MongoClient(host='0.0.0.0', port=27017)
        self.collection = self.client.taobao.taobao_watch
        self.collection.drop()
    def process_item(self, item, spider):
        dict1 ={}
        if item['count'] == 10:
            dict1.update(item.__dict__['_values'])
            # print(str(self.num/2178000 * 100) + '%')
            self.collection.insert(dict1)
        return item
