# -*- coding: utf-8 -*-
import pymysql
import pymysql.cursors
class HorsePipeline(object):
    def __init__(self):
        # 连接MySQL数据库
        self.connect = pymysql.connect(host='47.101.165.197', user='root', password='SdT0817%<789?', db='horse', port=2762)
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):
        # 往数据库里面写入数据
        self.cursor.execute('insert into horse_history(HORSE_DATE) values(%s)', (item['HORSE_DATE']))
#        self.cursor.execute('insert into horse_history(MINGCI_ID) values(%s)', (item['MINGCI_ID']))
#        self.cursor.execute('insert into horse_history(HORSE_ID) values(%s)', (item['HORSE_ID']))
        self.cursor.execute('insert into horse_history(HORSE_NAME) values(%s)', (item['HORSE_NAME']))
#        self.cursor.execute('insert into horse_history(REINSMAN_NAME) values(%s)', (item['REINSMAN_NAME']))
#        self.cursor.execute('insert into horse_history(TRAINER_NAME) values(%s)', (item['TRAINER_NAME']))
#        self.cursor.execute('insert into horse_history(HORSE_FUZHONG) values(%s)', (item['HORSE_FUZHONG']))
#        self.cursor.execute('insert into horse_history(PAIWEI_TIZHONG) values(%s)', (item['PAIWEI_TIZHONG']))
#        self.cursor.execute('insert into horse_history(DANGWEI_ID) values(%s)', (item['DANGWEI_ID']))
#        self.cursor.execute('insert into horse_history(HORSE_TOUMA) values(%s)', (item['HORSE_TOUMA']))
#        self.cursor.execute('insert into horse_history(YANTU_ZOUWEI) values(%s)', (item['YANTU_ZOUWEI']))
#        self.cursor.execute('insert into horse_history(FINISH_TIME) values(%s)', (item['FINISH_TIME']))
#        self.cursor.execute('insert into horse_history(HORSE_ODDS) values(%s)', (item['HORSE_ODDS']))
        self.connect.commit()
        return item

    # 关闭数据库
    def close_spider(self, spider):
        self.cursor.close()
        self.connect.close()