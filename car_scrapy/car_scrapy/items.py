# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class CarItem(Item):
    car_id = Field()  # 汽车id
    image = Field()  # 图片地址
    price = Field()  # 价格
    down_price = Field()  # 降价幅度
    title = Field()  # 汽车名称
    labels = Field()  # 标签
