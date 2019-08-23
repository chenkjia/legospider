# -*- coding: utf-8 -*-
import scrapy


class LegoSpider(scrapy.Spider):
    name = 'lego'
    allowed_domains = ['example.com']
    start_urls = ['http://example.com/']

    def parse(self, response):
        pass
