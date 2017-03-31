# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class Proxy(Item):

    ip = Field()
    port = Field()
    faceless = Field()
    type = Field()
    method = Field()
    address = Field()
    respSpeed = Field()
    lastVerifyAt = Field()
