
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Submit the form with the selected radio button
        yield scrapy.FormRequest.from_response(
            response,
            formxpath='//form',  # adjust if needed to target the correct form
            formdata={'rd1': 'E'},  # select the radio button with value 'E'
            callback=self.after_post
        )

    def after_post(self, response):
        # Handle the response after submitting the form
        self.log('Form submitted successfully!')
