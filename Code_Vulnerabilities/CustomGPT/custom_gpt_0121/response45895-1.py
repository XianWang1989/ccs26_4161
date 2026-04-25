
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/your-form-url']

    def parse(self, response):
        # Prepare form data with the desired radio button selection
        formdata = {
            'rd1': 'E',  # Selecting the radio button with value 'E'
            'rd2': 'o'   # You can include other fields as necessary
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/your-form-url',  # Endpoint for the form submission
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Handle the response after form submission
        self.log('Form submitted and response received.')
        # Process response data as required
