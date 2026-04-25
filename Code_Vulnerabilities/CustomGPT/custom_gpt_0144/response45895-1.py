import scrapy
from scrapy.http import FormRequest

class RadioButtonSpider(scrapy.Spider):
    name = 'radio_button_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Simulate selecting the radio button with value "E" for "rd1"
        return FormRequest.from_response(
            response,
            formdata={
                'rd1': 'E',
                'rd2': 'o'  # Include other fields as necessary
            },
            callback=self.after_post
        )

    def after_post(self, response):
        # Process the response after the form is submitted
        self.log("Form submitted")
        # Further processing...
