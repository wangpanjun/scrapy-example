# -*- coding: utf-8 -*-

__author__ = 'xiaowang'
__date__ = '15-10-25'


from scrapy import log

def warn(msg):
    log.msg(str(msg), level=log.WARNING)


def info(msg):
    log.msg(str(msg), level=log.INFO)


def debug(msg):
    log.msg(str(msg), level=log.DEBUG)

