# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from . import settings

class DiyigaokaonetbugPipeline(object):
    def __init__(self, ):
        self.conn = pymysql.connect(
            host=settings.MYSQL_HOST,
            db=settings.MYSQL_DBNAME,
            user=settings.MYSQL_USER,
            passwd=settings.MYSQL_PASSWORD,
            charset='utf8',  # 编码要加上，否则可能出现中文乱码问题
            use_unicode=False)
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        # 调用插入数据的方法
        self.insertData(item)
        return item
# 插入数据方法
    def insertData(self, item):
        check = '''
            SELECT count(1) as count
            FROM school
            WHERE source_id = %s
        '''
        self.cursor.execute(check, (item['source_id']))
        result = self.cursor.fetchone()
        print(result)
        if result[0] == 0:
            insert = '''
            INSERT INTO school(id, source_id, school_name, school_type, school_level, school_subjection, create_year,
            area, country_rank, other_rank, other_rank_type, address, school_two, school_nine, study_count, academician_count, master_degree_count,
            doctoral_degree_count, school_homepage, school_join_page, logo_url) 
            VALUES (uuid(), %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            '''

            params = (item['source_id'],
                      item['school_name'],
                      item['school_type'],
                      item['school_level'],
                      item['school_subjection'],
                      item['create_year'],
                      item['area'],
                      item['country_rank'],
                      item['other_rank'],
                      item['other_rank_type'],
                      item['address'],
                      item['school_two'],
                      item['school_nine'],
                      item['study_count'],
                      item['academician_count'],
                      item['master_degree_count'],
                      item['doctoral_degree_count'],
                      item['school_homepage'],
                      item['school_join_page'],
                      item['logo_url'])
            self.cursor.execute(insert, params)
            self.conn.commit()

