
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Sending a POST request with the selected radio button
        formdata = {
            'rd1': 'E',  # Select Employee radio button
            'rd2': 'o'   # Optionally include this if needed
        }

        yield scrapy.FormRequest(
            url='http://example.com/submit',
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully')
        # Process the response data
