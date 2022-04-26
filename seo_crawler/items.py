# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class SeoCrawlerItem(scrapy.Item):

    crawl_date = Field()
    download_time = Field()
    address = Field()
    url_len = Field()
    domain = Field()
    path = Field()
    directories = Field()
    status_code = Field()
    robot = Field()
    canonical = Field()
    count_canonical = Field()
    content_type = Field()
    title = Field()
    count_title = Field()
    long_title = Field()
    missing_title = Field()
    description = Field()
    count_description = Field()
    keywords = Field()
    h1 = Field()
    count_h1 = Field()
    missing_h1 = Field()
    h2 = Field()
    count_h2 = Field()
    h3 = Field()
    count_h3 = Field()
    h4 = Field()
    count_h4 = Field()
    user_agent = Field()

    
