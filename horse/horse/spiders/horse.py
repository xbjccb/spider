# -*- coding: utf-8 -*-
import scrapy
from horse.items import HorseItem

class HorseSpider(scrapy.Spider):
    name = 'horse'

    allowed_domains = ['hkjc.com']
    start_urls = ['https://racing.hkjc.com/racing/info/meeting/Results/Chinese/Local/']

    def parse(self, response):
        node_list = response.xpath("//div[@class='rowDiv5']")
        node_list2 = response.xpath("//div[@class='clearDivFloat rowDiv15']")
        for node in node_list:
            HORSE_DATE1 = node.xpath("//td[@class='tdAlignL number13 color_black']/text()").extract()[0]
            HORSE_DATE = HORSE_DATE1.strip('\r').strip('\n').strip('\t')
            item = HorseItem()
            item['HORSE_DATE'] = HORSE_DATE
            print(HORSE_DATE)
            yield item
        for node2 in node_list2:
            HORSE_NAME1 = node2.xpath("//tr[@class='trBgGrey']/td[@class='tdAlignL font13 fontStyle']/a/text()[1]").extract()[0]
            HORSE_NAME = HORSE_NAME1.strip('\r').strip('\n').strip('\t')
            item = HorseItem()
            item['HORSE_NAME'] = HORSE_NAME
            print(HORSE_NAME)
#            yield item











