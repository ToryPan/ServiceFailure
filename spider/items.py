# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DewuItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    current_count = scrapy.Field()
    url_lis = scrapy.Field()
    weibo_url = scrapy.Field()
    summary = scrapy.Field()
    title = scrapy.Field()
    username = scrapy.Field()
    mtime = scrapy.Field()
    complaint_detail = scrapy.Field()
    process_detail = scrapy.Field()


