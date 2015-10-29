# -*- coding: utf-8 -*-

# Scrapy settings for car_scrapy project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'car_scrapy'

DB_NAME = 'car'

SPIDER_MODULES = ['car_scrapy.spiders']
NEWSPIDER_MODULE = 'car_scrapy.spiders'

ITEM_PIPELINES = {
    'car_scrapy.pipelines.CarPipeline': 300,
}

DOWNLOADER_MIDDLEWARES = {
    # 'car_scrapy.misc.middleware.CustomHttpProxyMiddleware': 400,
    'car_scrapy.misc.middleware.CustomUserAgentMiddleware': 401,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'car_scrapy (+http://www.yourdomain.com)'


