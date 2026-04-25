
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form-page']

    def parse(self, response):
        # Fill in the form data
        formdata = {
            'rd1': 'E',  # Selecting the "Employee" radio button
            'rd2': 'o'   # This can be included if needed
        }

        # Submit the form
        yield scrapy.FormRequest(
            url='http://example.com/form-submit',  # Update with the actual form action URL
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle response after form submission
        self.log('Form submitted successfully')
