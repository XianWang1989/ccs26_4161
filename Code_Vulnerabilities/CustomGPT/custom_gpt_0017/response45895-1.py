
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        formdata = {
            'rd1': 'E',  # Selecting the radio button with value 'E'
            'rd2': 'o',  # You can include this for completeness; it won't affect the radio selection
        }
        yield scrapy.FormRequest.from_response(
            response,
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
