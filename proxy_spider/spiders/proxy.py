# coding:utf-8

from scrapy.spider import Spider
from scrapy.http import Request
from proxy_spider.items import Proxy


class ProxySpider(Spider):
    name = 'proxy'
    allowed_domains = ['kuaidaili.com']
    start_urls = [
        'http://www.kuaidaili.com/'
    ]

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Accept-Language': 'en-US,en;q=0.8,zh-TW;q=0.6,zh;q=0.4',
        # 'Connection': 'keep-alive',
        'Referer': 'http://www.kuaidaili.com/',
        'Upgrade-Insecure-Requests': 1,
        'Cache-Control': 'max-age=0',
    }

    cookies = {
        '_ydclearance': '05802e42ea361c37251d6c30-6ed2-4c1e-ae06-69243190dc41-1491035318',
        'channelid': '0',
        'sid': '1491028837567397',
        # 'Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31': '1490974747',
        # 'Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31': '1490976307',
        # '_ga': 'GA1.2.1602496365.1490974747',
    }

    def start_requests(self):
        for i, url in enumerate(self.start_urls):
            yield Request(url,
                          dont_filter=True,
                          headers=self.headers,
                          cookies=self.cookies,
                          callback=self.parse)

    def parse(self, response):
        for sel in response.xpath("//tbody/tr"):
                proxy = Proxy()
                proxy['ip'] = sel.xpath("td[@data-title='IP']/text()").extract()[0]
                proxy['port'] = sel.xpath("td[@data-title='PORT']/text()").extract()[0]
                proxy['faceless'] = sel.xpath("td[@data-title='%s']/text()" % u'匿名度').extract()[0]
                proxy['type'] = sel.xpath("td[@data-title='%s']/text()" % u'类型').extract()[0]
                proxy['method'] = sel.xpath("td[@data-title='%s']/text()" % u'get/post支持').extract()[0]
                proxy['address'] = sel.xpath("td[@data-title='%s']/text()" % u'位置').extract()[0]
                proxy['respSpeed'] = sel.xpath("td[@data-title='%s']/text()" % u'响应速度').extract()[0]
                proxy['lastVerifyAt'] = sel.xpath("td[@data-title='%s']/text()" % u'最后验证时间').extract()[0]
                yield proxy

