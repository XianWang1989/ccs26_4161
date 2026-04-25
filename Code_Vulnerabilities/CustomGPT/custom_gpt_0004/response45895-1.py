
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Select the radio button for 'Employee'
        formdata = {
            'rd1': 'E',  # Selecting the radio button with value 'E'
            'rd2': 'o'   # Optionally set other radios if needed
        }

        # Submit the form
        yield scrapy.FormRequest.from_response(
            response,
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Process the response after form submission
        self.log('Form submitted successfully.')
        # Further processing...
