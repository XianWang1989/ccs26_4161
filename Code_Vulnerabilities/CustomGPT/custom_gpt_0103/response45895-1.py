
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'

    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        # Submit the form with the radio button selection
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Change to your form submission URL
            formdata={'rd1': 'E'},  # Select the radio button with value 'E'
            callback=self.after_post
        )

    def after_post(self, response):
        # Handle the response after the form submission
        self.log('Form submitted successfully!')  # Add your processing here
