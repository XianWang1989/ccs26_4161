
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Form fields to send with the request
        formdata = {
            'rd1': 'E',  # Selecting 'Employee'
            'rd2': 'o'   # This can be left out or set to select 'Other'
        }

        # Make the POST request to submit the form
        yield scrapy.FormRequest(
            url=response.url,  # Replace with the actual form submission URL
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Handle response after form submission
        self.log('Form submitted successfully!')
        # Continue processing the response as needed
