
import scrapy

class RadioButtonSpider(scrapy.Spider):
    name = "radio_buttons_spider"

    start_urls = ['http://example.com/form']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,
            formdata={'rd1': 'E'},  # Select the Employee radio button
            callback=self.after_post
        )

    def after_post(self, response):
        self.log("Form submitted!")
