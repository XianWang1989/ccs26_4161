
import scrapy
from scrapy.http import FormRequest

class RadioButtonSpider(scrapy.Spider):
    name = 'radio_button_spider'
    start_urls = ['http://yourwebsite.com/form']

    def parse(self, response):
        # Assuming the radio buttons are in a form
        formdata = {
            'rd1': 'E',  # Selecting 'Employee'
            'rd2': ''    # Not selecting 'Other'
        }

        yield FormRequest.from_response(
            response,
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Process the response after the form submission
        self.log('Form submitted successfully!')
