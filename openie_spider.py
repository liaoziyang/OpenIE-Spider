import scrapy
import sys
import re
import json
import os
from scrapy import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from BeautifulSoup import BeautifulSoup

class OpenieSpider(scrapy.Spider):
    name = 'openie_spider'
    allowed_domains = []
    start_urls = []
    global results
    results = []
    custom_settings = {
        "DOWNLOAD_DELAY": 0.5,
    }

    def __init__(self,args1='', rel='',args2='', *args, **kwargs):
        self.start_urls.append('http://openie.allenai.org/search/?arg1=%s&rel=%s&arg2=%s' %(args1, rel, args2,))

    def start_requests(self):
        global start_url
        for start_url in self.start_urls:
            yield Request(start_url, callback = self.parse)

    def parse(self, response):
        global results
        global start_url
        arrScore = []
        sel = Selector(response)
        page = 1
        answer_count_string = sel.xpath("//div[@id='stats']/b[1]/text()")
        for s in answer_count_string.extract()[0].split():
            if s.isdigit():
                answer_count = int(s)
        page_count = answer_count/20
        relationships = sel.xpath("//*[contains(@href, '#L')]/span/text()")
        relationship_counts = sel.xpath("//*[contains(@href, '#L')]/text()")
        pattern = re.compile(r"\((\d+)\)")
        for relationship_count in relationship_counts:
            a = BeautifulSoup(relationship_count.extract()).text
            arrScore.append(pattern.findall(a))
            arrScore = [item for item in arrScore if len(item)]

        for index, relationship in enumerate(relationships):
            results.append(BeautifulSoup(relationship.extract()).text)
            yield {
                    BeautifulSoup(relationship.extract()).text: int(arrScore[index][0])
                }

        if page_count > 0:
            while page <= page_count:
                next_page_url = start_url + "&page=%s" % (page)
                page = page + 1
                yield scrapy.Request(response.urljoin(next_page_url))
