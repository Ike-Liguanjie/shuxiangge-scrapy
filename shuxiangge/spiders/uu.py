import re
from scrapy import Spider

from ..items import UuItem


class UuSpider(Spider):
    name = 'uu'
    allowed_domains = ['www.uuxsw8.net']
    start_urls = ['https://www.uuxsw8.net/quanben/list_1.html']

    def parse(self, response, **kwargs):
        books = response.xpath("/html/body/div[4]/div[1]/ul/li")
        for i in books:
            book_item = UuItem()
            book_item['serial'] = i.xpath("./span[1]/text()").extract_first()
            book_item['category'] = i.xpath("./span[2]/text()").extract_first()
            book_item['name'] = i.xpath("./span[2]/a[1]/text()").extract_first()
            book_item['status'] = i.xpath("./span[3]/text()").extract_first()
            book_item['size'] = i.xpath("./span[4]/text()").extract_first()
            book_item['author'] = i.xpath("./span[5]/a/text()").extract_first()
            yield book_item
        next_link = response.xpath("/html/body/div[4]/div[1]/div[2]/div/a[@class='next']/@href").extract()[0]
        m = re.match(r'http://www.uuxsw8.net/quanben/list_(\d+).html', next_link)
        if int(m.group(1)) < 6:
            yield response.follow(next_link, callback=self.parse)
