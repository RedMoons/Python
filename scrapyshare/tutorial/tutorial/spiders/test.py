from scrapy.Spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

class MySpider(BaseSpider):
    name = "craig"
    allowed_domains = ["craigslist.org"]
    start_urls = ["http://sfbay.craigslist.org/search/sfc/npo",]

    def parse(self,response):
    hxs = HtmlXPathSelector(response)
    titles = hxs.select("//p")
    for titles in titles:
        title = titles.select("a/text()").extract()
        link = titles.select("a/@href").extract()
        print title,link


"""

import scrapy

from tutorial.items import DmozItem

class DmozSpider(scrapy.Spider):
name = "dmoz"
allowed_domains = ["dmoz.org"]
start_urls = [
"http://www.dmoz.org/Computers/Programming/Languages/Python/",
]

def parse(self, response):
for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
url = response.urljoin(href.extract())
yield scrapy.Request(url, callback=self.parse_dir_contents)

def parse_dir_contents(self, response):
for sel in response.xpath('//ul/li'):
item = DmozItem()
item['title'] = sel.xpath('a/text()').extract()
item['link'] = sel.xpath('a/@href').extract()
item['desc'] = sel.xpath('text()').extract()
yield item
"""