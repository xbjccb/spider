# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#定义赛马派彩所需采集的数据
class HorseItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    HORSE_DATE = scrapy.Field()  # 比赛时间以及场地
#    MINGCI_ID = scrapy.Field()         #名次
#    HORSE_ID = scrapy.Field()          #马号
#    HORSE_NAME = scrapy.Field()        #马名
#    REINSMAN_NAME = scrapy.Field()        #骑师姓名
#    TRAINER_NAME = scrapy.Field()         #驯马师姓名
#    HORSE_FUZHONG = scrapy.Field()        #马匹实际负重
#    PAIWEI_TIZHONG = scrapy.Field()        #赛马排位体重
#    DANGWEI_ID = scrapy.Field()         #档位
#    HORSE_TOUMA = scrapy.Field()         #头马距离
#    YANTU_ZOUWEI = scrapy.Field()        #沿途走位
#    FINISH_TIME = scrapy.Field()         #比赛完成时间
#    HORSE_ODDS = scrapy.Field()          #独赢赔率







