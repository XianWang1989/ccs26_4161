
import scrapy

class RadioButtonSpider(scrapy.Spider):
    name = 'radio_button_spider'
    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        formdata = {
            'rd1': 'E',  # Selecting the radio button with value 'E'
            'rd2': 'o',  # Include if necessary for other radio buttons
        }
        return scrapy.FormRequest.from_response(
            response,
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully')
        # You can now extract data from the response
