# -*- coding: utf-8 -*-
import scrapy


class HorseSpider(scrapy.Spider):
    name = 'horse'
    allowed_domains = ['racing.hkjc.com']
    start_urls = ['https://racing.hkjc.com/racing/info/meeting/Results/Chinese/Local/20190302/ST']

    def parse(self, response):
        node_list = response.xpath("//div[@class='rowDiv5']")
        node_list2 = response.xpath("//div[@class='clearDivFloat rowDiv15']")
        for node in node_list:
            name1 = node.xpath("//td[@class='tdAlignL number13 color_black']/text()").extract()[0]
            name = name1.strip('\r').strip('\n').strip('\t')
            print(name)
        for node2 in node_list2:
            info1 = node2.xpath("//tr[@class='trBgGrey']/td[@class='tdAlignL font13 fontStyle']/a/text()[1]").extract()[0]
            info = info1.strip('\r').strip('\n').strip('\t')
            print(info)











