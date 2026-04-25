
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form-page']

    def parse(self, response):
        # Assuming there's a form on this page
        yield scrapy.FormRequest(
            url='http://example.com/form-page',  # Replace with the form action URL
            formdata={'rd1': 'E'},  # Selecting the radio button with value 'E'
            callback=self.after_post  # Specify a callback to handle the response
        )

    def after_post(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
        # You can process the response further here
