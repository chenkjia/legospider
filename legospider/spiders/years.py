# -*- coding: utf-8 -*-
import scrapy


class YearsSpider(scrapy.Spider):
    name = 'years'
    allowed_domains = ['bricklink.com']
    start_urls = ['http://bricklink.com/catalogTree.asp?itemType=S&itemBrand=1000']

    def parse(self, response):
        # for sets in response.css('.list-grid__item>a.content-item'):
        #     item = SetsItem()
        #     item['name'] = sets.css('::attr(title)').extract()[0]
        #     # item['title'] = sets.css('::attr(title)').extract()[0].encode('utf-8')
        #     yield item
        for link in response.css('tr:nth-child(5) a::attr(href)').extract():
            print(link)
            crapy.Request('http://bricklink.com/' + link, callback=self.parse_sets)
        pass

    def parse_sets(self, response):
        # this would log http://www.example.com/some_page.html
        response
        self.logger.info("Visited %s", response.url)