import scrapy
from ..items import QuotesprojectItem

class quotesSpider(scrapy.Spider):
    name = "pressNext"
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response):
        items = QuotesprojectItem()
        all_div = response.css('div.quote')

        for qu in all_div:
            title = qu.css("span.text::text").extract()
            author = qu.css(".author::text").extract()
            tag = qu.css(".tag::text").extract()

            items['iTitle'] = title
            items['iAuth'] = author
            items['iTag'] = tag
            
            yield items

        next_page = response.css("li.next a::attr(href)").get()

        if next_page is not None:
            yield response.follow(next_page,  callback = self.parse)
