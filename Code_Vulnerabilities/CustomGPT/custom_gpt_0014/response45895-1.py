
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/myform']

    def parse(self, response):
        # Fill the form and select the radio button for 'Employee'
        formdata = {
            'rd1': 'E',  # Selecting the radio button with value 'E'
            'rd2': 'o'   # This can be included but will not be selected
        }

        # Submit the form
        yield scrapy.FormRequest.from_response(
            response,
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully.')
