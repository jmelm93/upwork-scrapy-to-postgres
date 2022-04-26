# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from datetime import datetime
from urllib.parse import urlparse, urlsplit
from seo_crawler.items import SeoCrawlerItem

class SeoCrawlSpider(scrapy.spiders.CrawlSpider):

    name = 'seo_spider'

    start_urls = ['https://inseev.com/']

    allowed_domains = []

    for url in start_urls:
        allowed_domains.append(urlparse(url).netloc)
    
    custom_settings = {
        "DEPTH_LIMIT": 2,
    } 

    user_agent = 'Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/W.X.Y.Z‡ Mobile Safari/537.36 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'


    def start_request(self):
        yield scrapy.Request(url=self.start_urls, headers={
            'User-Agent': self.user_agent
        })

    rules = (
        Rule(LinkExtractor(allow_domains=allowed_domains), follow=True, callback="parse_item", process_request="set_user_agent"),
        Rule(LinkExtractor(deny=('.png', )), process_request="set_user_agent")

    )

    def set_user_agent(self, request, response):
        request.headers['User-Agent'] = self.user_agent
        return request


    def parse_item(self, response):
        self.logger.info('Hi, this is a log from %s', response.url)
        item = SeoCrawlerItem()
        item['crawl_date'] = datetime.now().strftime("%Y-%m-%d")
        item['status_code'] = response.status
        item['download_time'] = round(response.meta['download_latency'], 3)
        item['domain'] = urlparse(response.url).netloc
        item['path'] = urlsplit(response.url).path
        item['directories'] = ', '.join([x for x in urlsplit(response.url).path.split('/')[1:]]),
        item['address'] = response.url
        item['url_len'] = len(item['address'])
        item['canonical'] = response.xpath("//link[@rel='canonical']/@href").extract_first()
        item['count_canonical'] = len(response.xpath("//link[@rel='canonical']/@href"))
        item['content_type'] = response.headers['Content-Type']
        item['title'] = response.xpath("//title/text()").extract()
        item['count_title'] = len(item['title'])
        if item['count_title'] > 65:
            item['long_title'] = "TRUE"
        else:
            item['long_title'] = "FALSE"
        if item['count_title'] < 1:
            item['missing_title'] = "TRUE"
        else:
            item['missing_title'] = "FALSE"
        item['description'] = response.xpath("//meta[@name='description']/@content").extract_first()
        if item['description']:
            item['count_description'] = len(item['description'])
        else:
            item['count_description'] = 0
        item['keywords'] = response.xpath("//meta[@name='keywords']/@content").extract_first()
        item['h1'] = response.xpath('//body//h1//text()').extract_first()
        if item['h1'] == None:
            item['count_h1'] = 0
        else:
            item['count_h1'] = len(item['h1'])
        if item['count_h1'] == 0:
            item['missing_h1'] = "True"
        else:
            item['missing_h1'] = "False"
        item['h2'] = response.xpath('//body//h2//text()').extract_first()
        item['count_h2'] = len(response.xpath('//h2'))
        item['h3'] = response.xpath('//body//h3//text()').extract_first()
        item['count_h3'] = len(response.xpath('//h3'))
        item['h4'] = response.xpath('//body//h4//text()').extract_first()
        item['count_h4'] = len(response.xpath('//body//h4'))
        item['robot'] = response.xpath("//meta[@name='robots']/@content").extract_first()
        item['user_agent'] = response.request.headers["User-Agent"]

        yield item
        # return item
