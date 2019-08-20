# coding=utf-8
# -*- coding: utf-8 -*-

import scrapy
import requests
from ..items import DiyigaokaonetbugItem
import time
import random
import re


class GaokaoSpider(scrapy.Spider):
    # name是spider最重要的属性, 它必须被定义。同时它也必须保持唯一
    name = 'gaokao'
    start_urls = []
    # 给start_urls加入不同页面的地址
    for i in range(1, 3200):
        start_urls.append('http://www.diyigaokao.com/college/' + str(i))
    # 可选定义。包含了spider允许爬取的域名(domain)列表(list)
    allowed_domains = ['www.diyigaokao.com']

    # bash_url = 'https://search.51job.com/list/050000,000000,0000,00,9,99,PHP,2,'
    # bashurl = '.html'

    # def start_requests(self):
    #     for i in range(1, 4):
    #         url = self.bash_url + str(i) + self.bashurl
    #
    #         yield scrapy.Request(url, self.parse)

    # response是根据start_urls请求的结果，也可以用start_requests自己编写
    def parse(self, response):
        time.sleep(random.randint(2, 5))

        school_list = response.xpath("//div[@class='grid-body']")

        for i in school_list:
            # 理解成实例化吧
            item = DiyigaokaonetbugItem()
            # 记得要加 . 表示从当前节点
            # [0]是拿取第一个列表内容文本，如果没有则会拿到一个列表
            item['school_name'] = i.xpath('//div[@class="tag"]/h2/text()')[0].extract()
            item['school_type'] = i.xpath('//div[@class="info cf"]/ul/li[1]/text()')[0].extract()
            item['school_level'] = re.split('：', i.xpath('//div[@class="info cf"]/ul/li[2]/text()')[0].extract())[1]
            item['school_subjection'] = re.split('：', i.xpath('//div[@class="info cf"]/ul/li[3]/text()')[0].extract())[1]
            item['create_year'] = \
            re.findall(r"\d+\.?\d*", i.xpath('//div[@class="info cf"]/ul/li[4]/text()')[0].extract())[0]
            item['source_id'] = int(re.findall(r"\d+\.?\d*", str(response))[1])
            item['area'] = re.split('市', i.xpath('//div[@class="details"]/p/text()')[0].extract().strip())[0]

            if len(i.xpath('//div[@class="info cf"]/ul/li[5]/a[1]/text()')) == 0:
                item['country_rank'] = ''
            else:
                item['country_rank'] = int(i.xpath('//div[@class="info cf"]/ul/li[5]/a[1]/text()')[0].extract())
            if len(i.xpath('//div[@class="info cf"]/ul/li[5]/a[2]/text()')) == 0:
                item['other_rank'] = 0
            else:
                item['other_rank'] = int(i.xpath('//div[@class="info cf"]/ul/li[5]/a[2]/text()')[0].extract())
            if len(i.xpath('//div[@class="info cf"]/ul/li[5]/a[2]/i/text()')) == 0:
                item['other_rank_type'] = 0
            else:
                item['other_rank_type'] = i.xpath('//div[@class="info cf"]/ul/li[5]/a[2]/i/text()')[0].extract()
            item['address'] = i.xpath('//div[@class="details"]/p/text()')[0].extract().strip()

            if len(i.xpath('//div[@class="g-collegeTag"]/span[@title="211 院校"]/text()')) == 0:
                item['school_two'] = ''
            else:
                item['school_two'] = i.xpath('//div[@class="g-collegeTag"]/span[@title="211 院校"]/text()')[0].extract()
            if len(i.xpath('//div[@class="g-collegeTag"]/span[@title="985 院校"]/text()')) == 0:
                item['school_nine'] = ''
            else:
                item['school_nine'] = i.xpath('//div[@class="g-collegeTag"]/span[@title="985 院校"]/text()')[0].extract()
            item['study_count'] = i.xpath('//div[@class="details"]/ol/li[1]/em/text()')[0].extract().strip()
            item['academician_count'] = i.xpath('//div[@class="details"]/ol/li[2]/em/text()')[0].extract().strip()
            item['master_degree_count'] = i.xpath('//div[@class="details"]/ol/li[3]/em/text()')[0].extract().strip()
            item['doctoral_degree_count'] = i.xpath('//div[@class="details"]/ol/li[4]/em/text()')[0].extract().strip()

            item['school_homepage'] = i.xpath('//a[@title="官方网站"]/@href')[0].extract()
            item['school_join_page'] = i.xpath('//a[@title="招生网址"]/@href')[0].extract()
            item['logo_url'] = i.xpath('//div[@class="college_logo"]/img/@src')[0].extract()
            print('++++++++++++++++++++++++++++++++++++++内容start++++++++++++++++++++++++++++++++++++++++++++++')
            print(item)
            print('++++++++++++++++++++++++++++++++++++++内容end++++++++++++++++++++++++++++++++++++++++++++++')
            yield item

