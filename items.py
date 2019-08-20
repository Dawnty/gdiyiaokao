# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DiyigaokaonetbugItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 学校编号
    source_id = scrapy.Field()
    # 学校名称
    school_name = scrapy.Field()
    # 学校类型
    school_type = scrapy.Field()
    # 学校地区
    area = scrapy.Field()
    # 学校隶属
    school_subjection = scrapy.Field()
    # 学校层次
    school_level = scrapy.Field()
    # 学校排名
    country_rank = scrapy.Field()
    # 学校类排
    other_rank = scrapy.Field()
    # 学校类别
    other_rank_type = scrapy.Field()
    # 学校地址
    address = scrapy.Field()
    # 学校211是否
    school_two = scrapy.Field()
    # 学校985是否
    school_nine = scrapy.Field()
    # 建校时间
    create_year = scrapy.Field()
    # 学生人数
    study_count = scrapy.Field()
    # 院士人数
    academician_count = scrapy.Field()
    # 硕士点个数
    master_degree_count = scrapy.Field()
    # 博士点个数
    doctoral_degree_count = scrapy.Field()
    # 官方网站
    school_homepage = scrapy.Field()
    # 招生网址
    school_join_page = scrapy.Field()
    # logourl
    logo_url = scrapy.Field()
    pass
