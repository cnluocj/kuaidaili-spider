# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import redis
import json
from networkutils import scan
from scrapy.exceptions import DropItem


class ProxySpiderPipeline(object):

    def process_item(self, item, spider):
        if scan(item['ip'], int(item['port'])):
            r = redis.Redis(host='localhost', port=6379, db=0)
            r.rpush('proxy', json.dumps(dict(item)))
            return item
        else:
            raise DropItem('drop %s' % item)
