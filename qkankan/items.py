# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QkankanItem(scrapy.Item):
    title = scrapy.Field()
    click = scrapy.Field()
    website = scrapy.Field()
    siteinfo = scrapy.Field()
    position = scrapy.Field()
    sitelogo = scrapy.Field()
    sitepic = scrapy.Field()

