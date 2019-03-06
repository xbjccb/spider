# -*- coding: utf-8 -*-
import scrapy


from scrapy.selector import Selector
from horse.items import HorseItem

class HorseSpider(scrapy.Spider):
    name = 'horse'
#    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.119 Safari/537.36'}
    allowed_domains = ['racing.hkjc.com']
    start_urls = ['https://racing.hkjc.com/racing/info/meeting/Results/Chinese/Local/20190302/ST']






    def parsePaperContent(self, response):

        # instantie the item
        item = HorseItem()
        selector = Selector(response)
        item['HORSE_DATE'] = selector.xpath('div[@class="rowDiv5"]/table/tbody/tr/td[td.tdAlignL.number13.color_black]/text()').extract()[0]
        return item







