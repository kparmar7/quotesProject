import scrapy
from ..items import QuotesprojectItem

class SecondDivScrapy(scrapy.Spider):
    name = 'second'
    start_urls = [
        "https://quotes.toscrape.com/"
    ]

    def parse(self, response):
        # all_div = response.css('div.quote')[0]
        # title = all_div.css('span.text::text').extract()
        # author = all_div.css('.author::text').extract()
        # tag = all_div.css('.tag::text').extract()
        # yield{
        #     'title':title,
        #     'author':author,
        #     'tag':tag,
        # }
        
        # all_div = response.css('div.quote')
        # for quot in all_div:
        #     title = quot.css('span.text::text').extract()
        #     author = quot.css('.author::text').extract()
        #     tag = quot.css('.tag::text').extract()
        #     yield{
        #         'title':title,
        #         'author':author,
        #         'tag':tag,
        #     }

        items = QuotesprojectItem()

        all_div = response.css('div.quote')
        for quot in all_div:
            title = quot.css('span.text::text').extract()
            author = quot.css('.author::text').extract()
            tag = quot.css('.tag::text').extract()

            items["iTitle"] = title
            items["iAuth"] = author
            items["iTag"] = tag

            yield items

