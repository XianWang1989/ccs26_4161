
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        # Submitting the form with selected radio button
        formdata = {
            'rd1': 'E',  # Select the radio button with value 'E'
        }

        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the form submission URL
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log('Form submitted! Response received.')
