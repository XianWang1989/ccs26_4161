
import scrapy

class RadioButtonSpider(scrapy.Spider):
    name = 'radio_button_spider'
    start_urls = ['http://example.com/form']  # Replace with your target URL

    def parse(self, response):
        formdata = {
            'rd1': 'E',  # Select the "Employee" radio button
            'rd2': 'o'   # Include this if you need to submit the other option too
        }
        yield scrapy.FormRequest(
            url='http://example.com/submit',  # Replace with the form's action URL
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        self.logger.info('Form submitted successfully!')
        # Process the response here
