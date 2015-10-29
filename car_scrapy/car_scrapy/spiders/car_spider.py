# -*- coding: utf-8 -*-

__author__ = 'xiaowang'
__date__ = '15-10-25'

from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from car_scrapy.items import CarItem
import re


class CarSpider(CrawlSpider):
    name = 'car'

    start_urls = [
        'http://newcar.xcar.com.cn/car/'
    ]
    rules = [
        Rule(SgmlLinkExtractor(allow="/car/(0-){11}\d*/"), follow=True),
        Rule(SgmlLinkExtractor(allow="com\.cn/m\d*/$"), callback='parse_info', follow=True),
    ]

    def parse_info(self, response):
        item = CarItem()
        sel = Selector(response)
        pattern = '\d+'
        item['car_id'] = int(re.search(pattern, str(response.url)).group())
        li = sel.xpath('//div[@id="basic_info"]/ul/li')
        item['title'] = li.xpath('div[@class="focus_title"]/h1/span/text()').extract()[0]
        images = li.xpath('div[@class="focus_photo2"]/a/img/@src').extract()
        if images:
            item['image'] = images[0]
        item['price'] = float(li.xpath('div[@class="focus_info"]/div[1]/a/b/text()').extract()[0])
        down_price = li.xpath('div[@class="focus_info"]/div[1]/i/a/b/text()').extract()
        if down_price:
            item['down_price'] = float(down_price[0])
        else:
            item['down_price'] = 0
        labels_dds = li.xpath('div[@class="focus_info"]/div[@class="deploy_box"]/div/dl/dd')
        labels = []
        for lable in labels_dds:
            la_name = lable.xpath('text()').extract()
            if la_name:
                labels.append(la_name[0])
        item['labels'] = labels
        yield item
