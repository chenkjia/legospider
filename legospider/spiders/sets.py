# -*- coding: utf-8 -*-
import scrapy

from legospider.items import SetsItem


class SetsSpider(scrapy.Spider):
    name = 'sets'
    allowed_domains = ['lego.com']
    start_urls = ['http://lego.com/zh-cn/products/themes']

    def parse(self, response):
        # item = SetsItem()
        for sets in response.css('.list-grid__item>a.content-item'):
            item = SetsItem()
            item['name'] = sets.css('::attr(title)').extract()[0]
            # item['title'] = sets.css('::attr(title)').extract()[0].encode('utf-8')
            yield item
