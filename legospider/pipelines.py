# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SetsPipeline(object):
    def open_spider(self, spider):
        pass
    def process_item(self, item, spider):
        print '----------'
        print(item['name'])
        return item
    def close_spider(self, spider):
        pass
