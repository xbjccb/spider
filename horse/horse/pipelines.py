# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from twisted.enterprise import adbapi
import pymysql
import pymysql.cursors
from scrapy.crawler import Settings as settings
class HorsePipeline(object):
    #定义数据库连接信息
    def process_item(self, item, spider):
        host = settings['MYSQL_HOSTS']
        db = settings['MYSQL_DB']
        user = settings['MYSQL_USER']
        psd = settings['MYSQL_PASSWORD']
        c = settings['UTF8']
        port = settings['MYSQL_PORT']
        con = pymysql.connect(host=host, user=user, passwd=psd, db=db, charset=c, port=port)
        cue = con.cursor()
        print("数据库连接成功！")
        try:
            conn.execute("insert into  horse_history(HORSE_DATE) values(%s)",(item['HORSE_DATE']))
#            conn.execute("insert into horse_history(MINGCI_ID) values(%s)",(item['MINGCI_ID']))
#            conn.execute("insert into horse_history(HORSE_ID) values(%s)", (item['HORSE_ID']))
#            conn.execute('insert into horse_history(HORSE_NAME) values(%s)', (item['HORSE_NAME']))
#            conn.execute('insert into horse_history(REINSMAN_NAME) values(%s)', (item['REINSMAN_NAME']))
#            conn.execute('insert into horse_history(TRAINER_NAME) values(%s)', (item['TRAINER_NAME']))
#            conn.execute('insert into horse_history(HORSE_FUZHONG) values(%s)', (item['HORSE_FUZHONG']))
#            conn.execute('insert into horse_history(PAIWEI_TIZHONG) values(%s)', (item['PAIWEI_TIZHONG']))
#            conn.execute('insert into horse_history(DANGWEI_ID) values(%s)', (item['DANGWEI_ID']))
#            conn.execute('insert into horse_history(HORSE_TOUMA) values(%s)', (item['HORSE_TOUMA']))
#            conn.execute('insert into horse_history(YANTU_ZOUWEI) values(%s)', (item['YANTU_ZOUWEI']))
#            conn.execute('insert into horse_history(FINISH_TIME) values(%s)', (item['FINISH_TIME']))
#            conn.execute('insert into horse_history(HORSE_ODDS) values(%s)', (item['HORSE_ODDS']))
        except Exception as e:
            print('Insert error:', e)
            con.rollback()
        else:
            con.commit()
        con.close()
        return item
