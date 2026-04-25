
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/']

    def parse(self, response):
        # Assuming there's a form to submit
        formdata = {
            'rd1': 'E',  # Selecting the Employee radio button
            'rd2': 'o'   # Include this if you also want Other, but it's not checked
        }

        yield scrapy.FormRequest(
            url='http://example.com/form-submit',  # Replace with the actual form action URL
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Handle the response after form submission
        self.log('Form submitted and response received.')
