# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TaobaoSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    item_id = scrapy.Field()
    title = scrapy.Field()
    user_id = scrapy.Field()
    price_wap = scrapy.Field()
    buy_num = scrapy.Field()
    rate = scrapy.Field()
    count = scrapy.Field()
    count_302 =scrapy.Field()
    error_num = scrapy.Field()
