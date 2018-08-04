# -*- coding: utf-8 -*-

# Scrapy settings for taobao_spider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'taobao_spider'

SPIDER_MODULES = ['taobao_spider.spiders']
NEWSPIDER_MODULE = 'taobao_spider.spiders'
# LOG_FILE='TaobaoLog.log'
LOG_LEVEL = 'ERROR'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = '%E6%89%8B%E6%9C%BA%E6%B7%98%E5%AE%9D/10052339 CFNetwork/902.2 Darwin/17.7.0'
USER_AGENT = 'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
CONCURRENT_REQUESTS = 64

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False
# cookies ={
#     # 宿舍登录
#     "cna":"ayAlE2msyAACAXd7QqlPLKJE",
#     " enc":"jfs%2Fc3x8cv6RgeCDcJVtWFVLJ0KVFemA3QMvvCbTHT3o6qJIr6%2FunmEv8rvm9DR0s6rFs7PKQuSv7fYxt82pYQ%3D%3D",
#     " otherx":"e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0",
#     " tk_trace":"1",
#     " t":"2481f7233f43953e62ba2608bbc79c7f",
#     " _tb_token_":"5e545b51fe31a",
#     " cookie2":"11fcf96f50562d9ffbff45914c09a364",
#     " tracknick":"tb813630_2011",
#     " ck1":"",
#     " lgc":"tb813630_2011",
#     " skt":"2bb92bfba5a2ec10",
#     " hng":"CN%7Czh-CN%7CCNY%7C156",
#     " dnk":"tb813630_2011",
#     " JSESSIONID":"8F5050B00694B410EDBA3BA1728E3F10",
#     " _m_h5_tk":"9c0bcaa7ec948208d714d7100cee7e1f_1532409936972",
#     " _m_h5_tk_enc":"06864d5fc08cb281169d775e13bc862f",
#     " uc1":"cookie21=UtASsssme%2BBq&cookie15=UtASsssmOIJ0bQ%3D%3D&cookie14=UoTfKfMxc%2Bs%2BPQ%3D%3D",
#     " uc3":"vt3=F8dBzrmU7UKds59br9w%3D&id2=VWhbSp8%2Bb9ee&nk2=F5RNZLMB4hvda%2FFU5A%3D%3D&lg2=UtASsssmOIJ0bQ%3D%3D",
#     " _l_g_":"Ug%3D%3D",
#     " unb":"670348438",
#     " cookie1":"BxBB0WsBdxOWBvlUhcHGfdxSZDqHifxboIeAnOaCLdw%3D",
#     " login":"true",
#     " cookie17":"VWhbSp8%2Bb9ee",
#     " _nk_":"tb813630_2011",
#     " sg":"183",
#     " csg":"94c41ee9",
#     " isg":"BPb2Fa9hsRcIeUR9pKyXtT9dRyw4vzo8g0OcJWDf41l3o5Q9yKaYYP0Rv3nPCzJp"
#     }
#浏览器
cookies={
    "cna": "ayAlE2msyAACAXd7QqlPLKJE",
    " enc": "jfs%2Fc3x8cv6RgeCDcJVtWFVLJ0KVFemA3QMvvCbTHT3o6qJIr6%2FunmEv8rvm9DR0s6rFs7PKQuSv7fYxt82pYQ%3D%3D",
    " otherx": "e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0",
    " tk_trace": "1",
    " t": "2481f7233f43953e62ba2608bbc79c7f",
    " _tb_token_": "5e545b51fe31a",
    " cookie2": "11fcf96f50562d9ffbff45914c09a364",
    " tracknick": "tb813630_2011",
    " ck1": "",
    " lgc": "tb813630_2011",
    " skt": "2bb92bfba5a2ec10",
    " hng": "CN%7Czh-CN%7CCNY%7C156",
    " dnk": "tb813630_2011",
    " _m_h5_tk": "8cec05e150b93eeffcfb5301c00b1843_1532450142995",
    " _m_h5_tk_enc": "647ac6415f4c55b28871803ac8dbc910",
    " isg": "BD09zw5ZOgum95_oW9FsuKioTJn3cnFBdBYnkP-CeBTHNl9oxyuG_Ybk5Gxwtonk",
    " JSESSIONID": "80697F5040D9B8A37A76B9F0ABC1A465",
    " uc1": "cookie21=VFC%2FuZ9ainBZ&cookie15=WqG3DMC9VAQiUQ%3D%3D&cookie14=UoTfKfMxcor3LA%3D%3D",
    " uc3": "vt3=F8dBzrmU7UMAZAnjhBc%3D&id2=VWhbSp8%2Bb9ee&nk2=F5RNZLMB4hvda%2FFU5A%3D%3D&lg2=W5iHLLyFOGW7aA%3D%3D",
    " csg": "bba68fb0"
}
# cookies={
#      #教室登录
#     "isg":"BBQUwBMjM5OZQ6afSgE5TJa271aGbThXrJ1TdK71oB8imbTj1n0I58qbnVedenCv",
#     "ucn":"unsz",
#     "WAPFDFDTGFG":"%2B4cMKKP%2B8PI%2BKK8WloKFDxF2aW%2Br7NSd",
#     "_w_tb_nick":"tb813630_2011",
#     "imewweoriw":"36DO3l7smwbUVjScm8ABS3vmhBj1Mpgz%2FDYjr%2Flv824%3D",
#     "WAPFDFDTGFG":"%2B4cMKKP%2B8PI%2BKK8WloKFDxF2aW%2Br7NSd",
#     "_cc_":"UIHiLt3xSw%3D%3D",
#     "_l_g_":"Ug%3D%3D",
#     "_nk_":"tb813630_2011",
#     "_tb_token_":"ywB390wi1mUo5n4",
#     "_w_tb_nick":"tb813630_2011",
#     "cookie1":"BxBB0WsBdxOWBvlUhcHGfdxSZDqHifxboIeAnOaCLdw%3D",
#     "cookie17":"VWhbSp8%2Bb9ee",
#     "cookie2":"189dc21189922c1b6847bb0c00274c86",
#     "csg":"d9f337fa",
#     "imewweoriw":"36DO3l7smwbUVjScm8ABS3vmhBj1Mpgz%2FDYjr%2Flv824%3D",
#     "lgc":"tb813630_2011",
#     "munb":"670348438",
#     "ockeqeudmj":"ppt71Vo%3D",
#     "sg":"183",
#     "skt":"b6e16ce846f5e082",
#     "t":"e576855074b3d332251b8380917196da",
#     "tracknick":"tb813630_2011",
#     "uc1":"cookie21=W5iHLLyFe3xmcookie15=V32FPkk%2Fw0dUvg%3D%3Dcookie14=UoTfKfWV5gG%2BpQ%3D%3D",
#     "uc3":"vt3=F8dBzrhOxiTrFEcguxw%3Did2=VWhbSp8%2Bb9eenk2=F5RNZLMB4hvda%2FFU5A%3D%3Dlg2=VT5L2FSpMGV7TQ%3D%3D",
#     "unb":"670348438",
#     "cna":"bGcJEwpYthECAXBh4NtBkLDB"
# }


headers = {
    'user_agent' : 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1 like Mac OS X; zh-CN) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/15G77 UCBrowser/11.8.8.1060 Mobile  AliApp(TUnionSDK/0.1.20.2)',
    'cookies':"isg=BBQUwBMjM5OZQ6afSgE5TJa271aGbThXrJ1TdK71oB8imbTj1n0I58qbnVedenCv;ucn=unsz;WAPFDFDTGFG=%2B4cMKKP%2B8PI%2BKK8WloKFDxF2aW%2Br7NSd;_w_tb_nick=tb813630_2011;imewweoriw=36DO3l7smwbUVjScm8ABS3vmhBj1Mpgz%2FDYjr%2Flv824%3D;WAPFDFDTGFG=%2B4cMKKP%2B8PI%2BKK8WloKFDxF2aW%2Br7NSd;_cc_=UIHiLt3xSw%3D%3D;_l_g_=Ug%3D%3D;_nk_=tb813630_2011;_tb_token_=ywB390wi1mUo5n4;_w_tb_nick=tb813630_2011;cookie1=BxBB0WsBdxOWBvlUhcHGfdxSZDqHifxboIeAnOaCLdw%3D;cookie17=VWhbSp8%2Bb9ee;cookie2=189dc21189922c1b6847bb0c00274c86;csg=d9f337fa;imewweoriw=36DO3l7smwbUVjScm8ABS3vmhBj1Mpgz%2FDYjr%2Flv824%3D;lgc=tb813630_2011;munb=670348438;ockeqeudmj=ppt71Vo%3D;sg=183;skt=b6e16ce846f5e082;t=e576855074b3d332251b8380917196da;tracknick=tb813630_2011;uc1=cookie21=W5iHLLyFe3xmcookie15=V32FPkk%2Fw0dUvg%3D%3Dcookie14=UoTfKfWV5gG%2BpQ%3D%3D;uc3=vt3=F8dBzrhOxiTrFEcguxw%3Did2=VWhbSp8%2Bb9eenk2=F5RNZLMB4hvda%2FFU5A%3D%3Dlg2=VT5L2FSpMGV7TQ%3D%3D;unb=670348438;cna=bGcJEwpYthECAXBh4NtBkLDB"
}

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'taobao_spider.middlewares.TaobaoSpiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   # 'taobao_spider.middlewares.TaobaoSpiderDownloaderMiddleware': 543,
    # 'taobao_spider.middlewares.TaobaoSpiderRedirectMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'taobao_spider.pipelines.TaobaoSpiderPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
