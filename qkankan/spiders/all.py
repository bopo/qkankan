# -*- coding: utf-8 -*-
import scrapy
from qkankan.items import QkankanItem

class AllSpider(scrapy.Spider):
    name = 'all'
    allowed_domains = ['qkankan.com']
    start_urls = ['http://www.qkankan.com/map.html']

    def parse(self, response):
        area = response.xpath('//div[@class="blueborder"]//a[not(@class="linklblack")]/@href').extract()

        for x in area:
            url = response.urljoin(x)
            yield scrapy.Request(url=url, callback=self.parseItem)

    def parseItem(self, response):
        items = response.xpath('//div[@class="blueborder"]/div[@class="slist"]/div[@class="pic"]/a/@href').extract()
        pages = response.xpath('//a[@title="下一页"]/@href')

        if pages:
            url = response.urljoin(pages.extract()[0])
            yield scrapy.Request(url=url, callback=self.parseItem)
        
        for item in items:
            url = response.urljoin(item)
            yield scrapy.Request(url=url, callback=self.parseDetail)

    def parseDetail(self,response):
        items = QkankanItem()
        items['title'] = response.xpath('//h1/text()').extract()
        items['click'] = response.xpath('//span[@id="clicks"]/text()').extract()
        items['website'] = response.xpath('//*[@id="siteinfo"]/div[3]/a[1]/@href').extract()
        items['siteinfo'] = response.xpath('//div[@id="sitetext"]/text()').extract()
        items['position'] = response.xpath('//*[@id="position"]/a/text()').extract()
        items['sitelogo'] = response.urljoin(response.xpath('//*[@id="sitepic"]/a/img/@src').extract()[0])
        items['sitepic'] = response.urljoin(response.xpath('//*[@id="sitepic"]/a/img/@src').extract()[0])

        yield items



