# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class UuItem(scrapy.Item):
    # define the fields for your item here like:
    serial = scrapy.Field()
    category = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
    size = scrapy.Field()
    author = scrapy.Field()
