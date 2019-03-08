# -*- coding: utf-8 -*-


# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HorseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 比赛时间以及场地
    horse_date = scrapy.Field()
    # 名次
    mingci_id = scrapy.Field()
    # 马号
    horse_id = scrapy.Field()
    # 马名
    horse_name = scrapy.Field()
    # 骑师姓名
    reinsman_name = scrapy.Field()
    # 驯马师姓名
    trainer_name = scrapy.Field()
    # 马匹实际负重
    horse_fuzhong = scrapy.Field()
    # 赛马排位体重
    paiwei_tizhong = scrapy.Field()
    # 档位
    dangwei_id = scrapy.Field()
    # 头马距离
    horse_touma = scrapy.Field()
    # 沿途走位
    yantu_zouwei = scrapy.Field()
    # 比赛完成时间
    finish_time = scrapy.Field()
    # 独赢赔率
    horse_odds = scrapy.Field()