
import scrapy

class MySpider(scrapy.Spider):
    name = 'my_spider'
    start_urls = ['http://example.com/form']

    def parse(self, response):
        # Prepare the form data
        formdata = {
            'rd1': 'E',  # Selects the "Employee" radio button
            'rd2': 'o'   # Optional, if you need another field
        }

        # Send the POST request with the form data
        yield scrapy.FormRequest(
            url='http://example.com/submit',
            formdata=formdata,
            callback=self.after_submission
        )

    def after_submission(self, response):
        # Handle the response after form submission
        self.log('Form submitted successfully!')
