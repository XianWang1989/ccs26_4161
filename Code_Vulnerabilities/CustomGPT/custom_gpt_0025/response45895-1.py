
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Fill out the form data
        formdata = {
            'rd1': 'E',  # Select "Employee"
            'rd2': 'o'   # Optional, select "Other" if needed
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/form-submit',
            formdata=formdata,
            callback=self.after_post
        )

    def after_post(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully.')
