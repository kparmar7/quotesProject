# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class QuotesprojectItem(scrapy.Item):
    iTitle = scrapy.Field()
    iAuth = scrapy.Field()
    iTag = scrapy.Field()
    
