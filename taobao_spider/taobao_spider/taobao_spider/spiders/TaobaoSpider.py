# -*- coding: utf-8 -*-
import scrapy
import json
from jsonpath import jsonpath
import re
from ..items import TaobaoSpiderItem
from ..settings import cookies
from urllib import parse

error_num = 0
class TaobaospiderSpider(scrapy.Spider):
    name = 'TaobaoSpider'
    # allowed_domains = ['taobao.com', 'tmall.com']
    start_urls = [
        'https://s.m.taobao.com/search?event_submit_do_new_search_auction=1'\
        '&_input_charset=utf-8&topSearch=1&atype=b&searchfrom=1&'\
        'action=home%3Aredirect_app_action&from=1&q=帆布鞋&sst=1&n=20&'\
        'buying=buyitnow&m=api4h5&abtest=5&wlsort=5&page='
        + str(num) for num in range(1, 101)]
    def parse(self, response):
        response_str = response.body.decode()
        response_json = json.loads(response_str)
        for goods_info in jsonpath(response_json, '$..listItem')[0]:
            item = TaobaoSpiderItem()
            item['rate'] = []
            item['count'] = 0
            item['url'] = jsonpath(goods_info,'$..url')[0]
            item['item_id'] = jsonpath(goods_info,'$..item_id')[0]
            item['title'] = jsonpath(goods_info,'$..title')[0]
            item['user_id'] = jsonpath(goods_info,'$..userId')[0]
            item['price_wap'] = jsonpath(goods_info,'$..priceWap')[0]
            item['buy_num'] = jsonpath(goods_info,'$..act')[0]
            base_url = 'https://rate.tmall.com/list_detail_rate.htm?'
            itemId = 'itemId=' + item['item_id'] + '&'
            sellerId = 'sellerId=' + item['user_id'] + '&'
            for page in range(1, 11):
                item['count_302'] = 0
                item['error_num'] = 0
                second_url = '&order=3&currentPage=' + str(
                    page) + '&pageSize=10&&callback=_DLP_2533_der_3_currentPage_' + str(
                    page) + '_pageSize_10_'
                url = base_url + itemId + sellerId + second_url
                yield scrapy.Request(url, callback=self.parse_rate, meta={"item": item})
    def parse_rate(self,response):
        item = response.meta['item']
        if response.status == 302:
            item['error_num'] = 0
            patten1 = re.compile(r"smReturn=(.+?)&smSign=")
            url = re.search(patten1,response.url).group(1)
            url = parse.unquote(url)
            if item['count_302'] >= 20:
                item['count_302'] = 0
                response_list = []
                print(url)
                print("I Cant Kill ThisOne!Fuck TaoBao!")
                for goods_info in response_list:
                    item['rate'].append(goods_info)
                item['count'] += 1
                yield item
            else:
                item['count_302'] += 1
                print('kill_302__{}'.format(item['count_302']))
                yield scrapy.Request(url, callback=self.parse_rate, meta={"item": item},dont_filter=True)
        else:
            try:
                item['count_302'] = 0
                response_str = response.body.decode('GBK')
                item['error_num'] = 0
                patten = re.compile(r'"rateContent":"(.*?)","', re.S)
                response_list = re.findall(patten, response_str)
                for goods_info in response_list:
                    item['rate'].append(goods_info)
                item['count'] += 1
                # print('success__{}'.format(item['count']))
                yield item
            except UnicodeDecodeError:
                if item['error_num'] >= 20:
                    item['error_num'] = 0
                    global error_num
                    error_num += 1
                    print("UnicodeError__{}".format(error_num))
                    response_list = []
                    for goods_info in response_list:
                        item['rate'].append(goods_info)
                    item['count'] += 1
                    yield item
                else:
                    print(response.url)
                    item['error_num'] += 1
                    yield scrapy.Request(response.url, callback=self.parse_rate, meta={"item": item},dont_filter=True)
