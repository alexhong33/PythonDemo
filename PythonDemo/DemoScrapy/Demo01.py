'''
Created on 2017年6月12日

@author: Alex

Run

scrapy runspider Demo01.py -o Demo01.json

输出Demo01.json在DemoScrapy目录下
'''

import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/tag/humor/',
    ]
    
    
    def parse(self, response):
        #解析div名为quote的项目
        for quote in response.css('div.quote'):
            yield{
                #获取内容
                'text': quote.css('span.text::text').extract_first(),
                #获取作者名
                'author':quote.xpath('span/small/text()').extract_first(),
            }
        
        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
