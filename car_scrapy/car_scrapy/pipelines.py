# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from pymongo import MongoClient
from settings import DB_NAME


class CarPipeline(object):
    def __init__(self):
        """初始化链接"""
        self.db = MongoClient()[DB_NAME]

    def process_item(self, item, spider):
        json_str = {}
        for key in item.keys():
            json_str[key] = item[key]

        if self.db.car.find({'car_id': item['car_id']}).count() == 0:
            self.db.car.insert(json_str)
        else:
            self.db.car.update({'car_id': item['car_id']}, json_str)
        return item


