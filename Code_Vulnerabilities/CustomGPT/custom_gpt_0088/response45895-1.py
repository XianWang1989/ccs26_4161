
import scrapy

class RadioButtonSpider(scrapy.Spider):
    name = 'radio_buttons'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Selecting the radio button for 'Employee'
        formdata = {
            'rd1': 'E',  # Selecting 'Employee'
            'rd2': ''    # Ensure 'Other' is not selected
        }

        yield scrapy.FormRequest(
            url='http://example.com/submit',
            method='POST',
            formdata=formdata,
            callback=self.parse_result
        )

    def parse_result(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully')
        # Process the response further as needed
