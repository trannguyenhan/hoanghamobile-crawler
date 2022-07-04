# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HoanghamobilecrawlerItem(scrapy.Item):
    url = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    color = scrapy.Field()
    
    cpu = scrapy.Field()
    ram = scrapy.Field()
    rom = scrapy.Field()
    pin = scrapy.Field()
