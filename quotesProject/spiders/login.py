import scrapy
from scrapy.http import FormRequest
from scrapy.utils.response import open_in_browser
from ..items import QuotesprojectItem


class quotesSpider(scrapy.Spider):
    name = "login"
    start_urls = [
        "https://quotes.toscrape.com/login"
    ]

    def parse(self, response):
        token = response.css("form  input::attr(value)").extract_first()
        # print(token)
        return FormRequest.from_response(response, formdata={
            'csrf_token': token,
            'username': 'kashyap@12.com',
            'password': '1234',
        }, callback = self.start_scraping)

    def start_scraping(self, response):
        open_in_browser(response)
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
            yield response.follow(next_page,  callback=self.start_scraping)
