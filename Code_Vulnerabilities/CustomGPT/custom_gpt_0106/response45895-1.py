
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']  # Replace with your URL

    def parse(self, response):
        # Fill in the form data
        formdata = {
            'rd1': 'E',  # Select the radio button with value 'E'
            'rd2': 'o'   # You can include other fields if necessary
        }

        # Submit the form
        yield scrapy.FormRequest(
            url=response.url,  # The same URL for the form submission
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log('Form submitted!')
        # Continue processing
