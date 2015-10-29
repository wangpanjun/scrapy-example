# -*- coding: utf-8 -*-

__author__ = 'xiaowang'
__date__ = '15-10-25'

import random
from car_scrapy.misc.agent import AGENTS
from car_scrapy.misc.proxy import PROXIES
from car_scrapy.misc.log import *

class CustomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        agent = random.choice(AGENTS)
        request.headers['User-Agent'] = agent


class CustomHttpProxyMiddleware(object):

    def process_request(self, request, spider):
        p = random.choice(PROXIES)
        request.meta['proxy'] = "http://%s" % p['ip_port']


